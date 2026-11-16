#!/usr/bin/env python3
"""Herramienta del Agente de Cuentas: comentarios y mensajes de Instagram y Facebook.

  python3 comunidad.py pendientes            # JSON con lo nuevo sin atender (no responde nada)
  python3 comunidad.py responder <ref> "<texto>"
  python3 comunidad.py ocultar <ref>         # oculta un comentario (spam, insultos)
  python3 comunidad.py marcar <ref> <estado> # atendido | para_dueno | ignorado
  python3 comunidad.py resumen               # cifras rápidas (seguidores, likes, comentarios)

<ref> es el campo "ref" que da `pendientes` (p. ej. igc:1789..., fbc:122..., igdm:<conv>:<msg>).
Privacidad: el estado guarda solo huellas (sha256) de los IDs atendidos, nunca textos ni nombres,
porque el repositorio es público. Los textos de clientes solo se muestran en la sesión.
"""
import datetime as dt, hashlib, json, sys
from pathlib import Path

import publicador as P

ESTADO = P.AQUI / "estado" / "comunidad.json"
IG, PG = P.CFG["instagram_id"], P.CFG["pagina_id"]
VENTANA_DM_H = 23          # Meta solo deja responder mensajes dentro de 24 h
DIAS_COMENTARIOS = 21      # revisa comentarios de publicaciones de las últimas 3 semanas


def h(x):
    return hashlib.sha256(str(x).encode()).hexdigest()[:20]


def leer():
    return json.loads(ESTADO.read_text()) if ESTADO.exists() else {"vistos": {}}


def guardar(est):
    ESTADO.write_text(json.dumps(est, indent=1, sort_keys=True) + "\n")


def ahora():
    return dt.datetime.now(dt.timezone.utc)


def t(s):
    return dt.datetime.fromisoformat(s.replace("+0000", "+00:00"))


def pendientes():
    est, out = leer(), []
    vistos = est["vistos"]
    tk = P.token_pagina()
    yo_ig = P.CFG["instagram_usuario"]
    limite = ahora() - dt.timedelta(days=DIAS_COMENTARIOS)

    # comentarios de Instagram
    medias = P.g("GET", f"{IG}/media", fields="id,caption,timestamp,permalink,comments_count", limit=30).get("data", [])
    for m in medias:
        if t(m["timestamp"]) < limite or not m.get("comments_count"):
            continue
        cs = P.g("GET", f"{m['id']}/comments", fields="id,text,username,timestamp,hidden,replies{id,username,text}", limit=50).get("data", [])
        for c in cs:
            if c.get("username") == yo_ig or c.get("hidden") or h("igc" + c["id"]) in vistos:
                continue
            ya = any(r.get("username") == yo_ig for r in c.get("replies", {}).get("data", []))
            if ya:
                continue
            out.append({"ref": "igc:" + c["id"], "canal": "Instagram · comentario", "autor": c.get("username"),
                        "texto": c.get("text"), "fecha": c["timestamp"], "publicacion": (m.get("caption") or "")[:90],
                        "enlace": m.get("permalink")})

    # comentarios de Facebook
    posts = P.g("GET", f"{PG}/feed", token=tk, limit=25,
                fields="id,message,created_time,permalink_url,comments.limit(50){id,message,from,created_time,is_hidden,comments.limit(10){from}}").get("data", [])
    for p in posts:
        if t(p["created_time"]) < limite:
            continue
        for c in p.get("comments", {}).get("data", []):
            if (c.get("from") or {}).get("id") == PG or c.get("is_hidden") or h("fbc" + c["id"]) in vistos:
                continue
            if any((r.get("from") or {}).get("id") == PG for r in c.get("comments", {}).get("data", [])):
                continue
            out.append({"ref": "fbc:" + c["id"], "canal": "Facebook · comentario", "autor": (c.get("from") or {}).get("name"),
                        "texto": c.get("message"), "fecha": c["created_time"], "publicacion": (p.get("message") or "")[:90],
                        "enlace": p.get("permalink_url")})

    # mensajes directos (Instagram y Messenger)
    for plat, pref, canal in (("instagram", "igdm", "Instagram · mensaje"), ("messenger", "fbdm", "Messenger · mensaje")):
        convs = P.g("GET", f"{PG}/conversations", token=tk, platform=plat, limit=25,
                    fields="id,updated_time,messages.limit(6){id,message,from,created_time}").get("data", [])
        for cv in convs:
            msgs = cv.get("messages", {}).get("data", [])
            if not msgs:
                continue
            ult = msgs[0]   # el más reciente
            frm = ult.get("from") or {}
            if frm.get("id") in (PG, IG) or frm.get("username") == yo_ig:
                continue    # lo último lo escribimos nosotros
            if ahora() - t(ult["created_time"]) > dt.timedelta(hours=VENTANA_DM_H):
                continue
            if h(pref + ult["id"]) in vistos:
                continue
            historial = [{"de": ("tienda" if (m.get("from") or {}).get("id") in (PG, IG) else "cliente"), "texto": m.get("message")}
                         for m in reversed(msgs)]
            out.append({"ref": f"{pref}:{cv['id']}:{ult['id']}:{frm.get('id')}", "canal": canal,
                        "autor": frm.get("name") or frm.get("username"), "texto": ult.get("message"),
                        "fecha": ult["created_time"], "historial": historial})
    out.sort(key=lambda x: x["fecha"])
    print(json.dumps({"pendientes": out, "total": len(out)}, ensure_ascii=False, indent=1))


def _marcar(ref, estado):
    est = leer()
    tipo, *partes = ref.split(":")
    clave = tipo + (partes[1] if tipo in ("igdm", "fbdm") else partes[0])
    est["vistos"][h(clave)] = {"estado": estado, "fecha": ahora().date().isoformat()}
    # poda: solo los últimos 60 días
    corte = (ahora() - dt.timedelta(days=60)).date().isoformat()
    est["vistos"] = {k: v for k, v in est["vistos"].items() if v["fecha"] >= corte}
    guardar(est)


def responder(ref, texto):
    tipo, *partes = ref.split(":")
    tk = P.token_pagina()
    if tipo == "igc":
        r = P.g("POST", f"{partes[0]}/replies", message=texto)
    elif tipo == "fbc":
        r = P.g("POST", f"{partes[0]}/comments", token=tk, message=texto)
    elif tipo in ("igdm", "fbdm"):
        r = P.g("POST", f"{PG}/messages", token=tk, messaging_type="RESPONSE",
                recipient=json.dumps({"id": partes[2]}), message=json.dumps({"text": texto}))
    else:
        raise SystemExit(f"ref desconocida: {ref}")
    _marcar(ref, "atendido")
    print("✓ respondido", tipo, (r.get("id") or r.get("message_id") or "")[:12] + "…")


def ocultar(ref):
    tipo, cid = ref.split(":")[:2]
    if tipo == "igc":
        P.g("POST", cid, hide="true")
    elif tipo == "fbc":
        P.g("POST", cid, token=P.token_pagina(), is_hidden="true")
    else:
        raise SystemExit("solo se ocultan comentarios")
    _marcar(ref, "ignorado")
    print("✓ oculto")


def resumen():
    tk = P.token_pagina()
    ig = P.g("GET", IG, fields="followers_count,media_count")
    pg = P.g("GET", PG, token=tk, fields="followers_count,fan_count")
    medias = P.g("GET", f"{IG}/media", fields="caption,timestamp,like_count,comments_count,permalink,media_type", limit=20).get("data", [])
    print(json.dumps({"instagram": ig, "facebook": pg,
                      "ultimas_ig": [{"fecha": m["timestamp"][:10], "tipo": m.get("media_type"), "likes": m.get("like_count"),
                                      "comentarios": m.get("comments_count"), "texto": (m.get("caption") or "")[:60],
                                      "enlace": m.get("permalink")} for m in medias]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    {"pendientes": lambda: pendientes(), "resumen": lambda: resumen(),
     "responder": lambda: responder(a[1], a[2]), "ocultar": lambda: ocultar(a[1]),
     "marcar": lambda: _marcar(a[1], a[2]) or print("✓ marcado")}[a[0]]()
