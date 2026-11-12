#!/usr/bin/env python3
"""Publicador de Pieza Clave para Instagram y Facebook (API Graph de Meta).

Lee calendario.json y publica cada entrada cuando llega su hora. Lo ya
publicado queda en estado/publicados.json para no repetir nada.

El token NO vive en este repositorio: el proxy del entorno lo agrega a cada
petición a graph.facebook.com. Para correrlo en otra máquina, define la
variable META_TOKEN. El script nunca imprime tokens.

Uso:
  python3 publicador.py verificar           # cuentas, permisos y archivos (no publica)
  python3 publicador.py estado              # qué falta, qué salió, qué está vencido
  python3 publicador.py preparar            # convierte las imágenes a JPG para Instagram
  python3 publicador.py probar <id>         # crea los contenedores de IG sin publicar
  python3 publicador.py publicar [--prueba] [--id <id>] [--forzar]
"""
import argparse, datetime as dt, json, os, sys, time
from pathlib import Path

import requests

AQUI = Path(__file__).resolve().parent
PIEZA = AQUI.parent                      # carpeta pieza-clave/
CFG = json.loads((AQUI / "meta.json").read_text())
CAL = AQUI / "calendario.json"
ESTADO = AQUI / "estado" / "publicados.json"
MEDIA = AQUI / "media"
API = f"https://graph.facebook.com/{CFG['version_api']}"
RAW = f"https://raw.githubusercontent.com/{CFG['repo']}/{CFG['rama']}/pieza-clave/"
VE = dt.timezone(dt.timedelta(hours=-4))
VENTANA_H = 12        # si se pasó la hora por más de esto, no se publica sola
S = requests.Session()
TOKEN = os.environ.get("META_TOKEN")


class ErrorMeta(Exception):
    pass


def limpio(obj):
    """Copia sin campos que puedan traer tokens, para imprimir."""
    if isinstance(obj, dict):
        return {k: ("<oculto>" if "token" in k.lower() else limpio(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [limpio(x) for x in obj]
    return obj


def g(metodo, ruta, token=None, **params):
    url = ruta if ruta.startswith("http") else f"{API}/{ruta}"
    tok = token or TOKEN
    if tok:
        params["access_token"] = tok
    for intento in range(4):
        try:
            r = S.request(metodo, url, params=params if metodo == "GET" else None,
                          data=params if metodo != "GET" else None, timeout=180)
        except requests.RequestException as e:
            if intento == 3:
                raise ErrorMeta(f"red: {e.__class__.__name__}")
            time.sleep(2 ** intento * 3)
            continue
        try:
            j = r.json()
        except ValueError:
            j = {"error": {"message": r.text[:300], "code": r.status_code}}
        if "error" in j:
            err = j["error"]
            if err.get("is_transient") and intento < 3:
                time.sleep(2 ** intento * 5)
                continue
            raise ErrorMeta(f"{err.get('code')}/{err.get('error_subcode', '-')}: {err.get('message')}")
        return j
    raise ErrorMeta("sin respuesta")


_token_pagina = None


def token_pagina():
    """Token de la Página, solo en memoria (nunca se imprime ni se guarda)."""
    global _token_pagina
    if _token_pagina is None:
        _token_pagina = g("GET", CFG["pagina_id"], fields="access_token")["access_token"]
    return _token_pagina


# ---------- archivos ----------

def jpg_de(rel):
    """Instagram solo acepta JPG: devuelve la ruta del JPG en media/."""
    return MEDIA / (Path(rel).stem + ".jpg")


def preparar():
    from PIL import Image
    MEDIA.mkdir(exist_ok=True)
    n = 0
    for e in leer_cal():
        for rel in e["archivos"] + ([e["portada"]] if e.get("portada") else []):
            if rel.lower().endswith((".png", ".jpg", ".jpeg")):
                dst = jpg_de(rel)
                src = PIEZA / rel
                if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                    Image.open(src).convert("RGB").save(dst, "JPEG", quality=92, optimize=True, progressive=False)
                    n += 1
    print(f"JPG creados o actualizados: {n}")


def url_publica(rel):
    if rel.lower().endswith((".png", ".jpg", ".jpeg")):
        return RAW + "automatizacion/media/" + jpg_de(rel).name
    return RAW + rel


# ---------- calendario y estado ----------

def leer_cal():
    return json.loads(CAL.read_text())["publicaciones"]


def leer_estado():
    return json.loads(ESTADO.read_text()) if ESTADO.exists() else {}


def guardar_estado(est):
    ESTADO.parent.mkdir(exist_ok=True)
    ESTADO.write_text(json.dumps(est, ensure_ascii=False, indent=2) + "\n")


def fecha(e):
    return dt.datetime.fromisoformat(e["fecha"])


# ---------- Instagram ----------

def ig_esperar(cid, max_s=900):
    t0 = time.time()
    while True:
        st = g("GET", cid, fields="status_code,status").get("status_code")
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise ErrorMeta(f"contenedor {cid}: {st}")
        if time.time() - t0 > max_s:
            raise ErrorMeta(f"contenedor {cid}: tardó demasiado ({st})")
        time.sleep(10)


def ig_contenedores(e):
    ig = CFG["instagram_id"]
    urls = [url_publica(a) for a in e["archivos"]]
    t = e["tipo"]
    if t == "imagen":
        return g("POST", f"{ig}/media", image_url=urls[0], caption=e.get("texto", ""))["id"]
    if t == "historia":
        return g("POST", f"{ig}/media", image_url=urls[0], media_type="STORIES")["id"]
    if t == "reel":
        p = dict(media_type="REELS", video_url=urls[0], caption=e.get("texto", ""), share_to_feed="true")
        if e.get("portada"):
            p["cover_url"] = url_publica(e["portada"])
        return g("POST", f"{ig}/media", **p)["id"]
    if t == "carrusel":
        hijos = [g("POST", f"{ig}/media", image_url=u, is_carousel_item="true")["id"] for u in urls]
        for h in hijos:
            ig_esperar(h)
        return g("POST", f"{ig}/media", media_type="CAROUSEL", children=",".join(hijos),
                 caption=e.get("texto", ""))["id"]
    raise ErrorMeta(f"tipo desconocido {t}")


def publicar_ig(e):
    cid = ig_contenedores(e)
    ig_esperar(cid)
    mid = g("POST", f"{CFG['instagram_id']}/media_publish", creation_id=cid)["id"]
    try:
        link = g("GET", mid, fields="permalink").get("permalink")
    except ErrorMeta:
        link = None
    return {"id": mid, "enlace": link}


# ---------- Facebook ----------

def publicar_fb(e):
    pg, tk = CFG["pagina_id"], token_pagina()
    urls = [url_publica(a) for a in e["archivos"]]
    t, msg = e["tipo"], e.get("texto", "")
    if t == "imagen":
        r = g("POST", f"{pg}/photos", token=tk, url=urls[0], message=msg)
        return {"id": r.get("post_id") or r["id"]}
    if t == "carrusel":
        fotos = [g("POST", f"{pg}/photos", token=tk, url=u, published="false")["id"] for u in urls]
        adj = json.dumps([{"media_fbid": f} for f in fotos])
        return {"id": g("POST", f"{pg}/feed", token=tk, message=msg, attached_media=adj)["id"]}
    if t == "historia":
        foto = g("POST", f"{pg}/photos", token=tk, url=urls[0], published="false")["id"]
        return {"id": g("POST", f"{pg}/photo_stories", token=tk, photo_id=foto).get("post_id")}
    if t == "reel":
        vid = g("POST", f"{pg}/video_reels", token=tk, upload_phase="start")["video_id"]
        r = S.post(f"https://rupload.facebook.com/video-upload/{CFG['version_api']}/{vid}",
                   headers={"Authorization": f"OAuth {tk}", "file_url": urls[0]}, timeout=300)
        if not r.ok:
            raise ErrorMeta(f"subida del reel: HTTP {r.status_code}")
        g("POST", f"{pg}/video_reels", token=tk, upload_phase="finish", video_id=vid,
          video_state="PUBLISHED", description=msg)
        return {"id": vid}
    raise ErrorMeta(f"tipo desconocido {t}")


PUBLICAR = {"instagram": publicar_ig, "facebook": publicar_fb}


# ---------- comandos ----------

def cmd_verificar(_):
    ok = True
    def paso(nombre, fn):
        nonlocal ok
        try:
            print(f"✓ {nombre}: {json.dumps(limpio(fn()), ensure_ascii=False)}")
        except Exception as ex:
            ok = False
            print(f"✗ {nombre}: {ex}")
    paso("usuario del token", lambda: g("GET", "me", fields="id,name"))
    paso("página", lambda: g("GET", CFG["pagina_id"], fields="name,link,instagram_business_account"))
    paso("instagram", lambda: g("GET", CFG["instagram_id"], fields="username,name,media_count,followers_count"))
    paso("límite de publicación IG (24 h)", lambda: g("GET", f"{CFG['instagram_id']}/content_publishing_limit",
                                                     fields="quota_usage,config"))
    paso("token de página (solo se comprueba que exista)", lambda: {"obtenido": bool(token_pagina())})
    faltan = []
    for e in leer_cal():
        for rel in e["archivos"] + ([e["portada"]] if e.get("portada") else []):
            if rel.lower().endswith((".png", ".jpg", ".jpeg")) and not jpg_de(rel).exists():
                faltan.append(rel)
            u = url_publica(rel)
            h = S.head(u, timeout=60)
            if h.status_code != 200:
                faltan.append(f"{rel} (URL {h.status_code})")
    print("✓ archivos públicos" if not faltan else "✗ archivos con problema:\n  " + "\n  ".join(faltan))
    return 0 if ok and not faltan else 1


def cmd_estado(_):
    est, ahora = leer_estado(), dt.datetime.now(VE)
    for e in leer_cal():
        hecho = est.get(e["id"], {})
        if e.get("manual"):
            s = "MANUAL · " + e.get("nota", "")
        elif all(p in hecho for p in e["plataformas"]):
            s = "publicado · " + " ".join(f"{p}:{hecho[p].get('enlace') or hecho[p]['id']}" for p in e["plataformas"])
        elif fecha(e) <= ahora - dt.timedelta(hours=VENTANA_H):
            s = "VENCIDO (no salió a tiempo; usa publicar --id ... --forzar)"
        elif fecha(e) <= ahora:
            s = "toca ya"
        else:
            s = "programado"
        print(f"{e['fecha'][:16].replace('T', ' ')}  {e['tipo']:9} {e['id']:30} {s}")


def cmd_probar(a):
    e = next(x for x in leer_cal() if x["id"] == a.id)
    cid = ig_contenedores(e)
    ig_esperar(cid)
    print(f"✓ contenedor de Instagram listo ({cid}); NO se publicó y vence solo en 24 h.")


def cmd_publicar(a):
    est, ahora = leer_estado(), dt.datetime.now(VE)
    errores = 0
    for e in leer_cal():
        if a.id and e["id"] != a.id:
            continue
        if e.get("manual"):
            continue
        cuando = fecha(e)
        if not a.forzar and (cuando > ahora or cuando <= ahora - dt.timedelta(hours=VENTANA_H)):
            continue
        for p in e["plataformas"]:
            if p in est.get(e["id"], {}):
                continue
            if a.prueba:
                print(f"[prueba] publicaría {e['id']} en {p}: {[url_publica(x) for x in e['archivos']]}")
                continue
            try:
                r = PUBLICAR[p](e)
                r["fecha"] = dt.datetime.now(VE).isoformat(timespec="seconds")
                est.setdefault(e["id"], {})[p] = r
                guardar_estado(est)
                print(f"✓ {e['id']} → {p}: {r.get('enlace') or r['id']}")
            except Exception as ex:
                errores += 1
                print(f"✗ {e['id']} → {p}: {ex}")
    return 1 if errores else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verificar")
    sub.add_parser("estado")
    sub.add_parser("preparar")
    p = sub.add_parser("probar"); p.add_argument("id")
    p = sub.add_parser("publicar")
    p.add_argument("--prueba", action="store_true", help="muestra qué haría, sin publicar")
    p.add_argument("--id", help="solo esta entrada")
    p.add_argument("--forzar", action="store_true", help="ignora la hora (úsalo con --id)")
    a = ap.parse_args()
    if a.cmd == "publicar" and a.forzar and not a.id:
        ap.error("--forzar necesita --id")
    fn = {"verificar": cmd_verificar, "estado": cmd_estado, "preparar": lambda _: preparar(),
          "probar": cmd_probar, "publicar": cmd_publicar}[a.cmd]
    sys.exit(fn(a) or 0)


if __name__ == "__main__":
    main()
