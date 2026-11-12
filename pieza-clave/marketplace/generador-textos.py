import re,os
SP='/tmp/claude-0/-home-user-Claude-movil/59907f33-5efd-5727-b54e-ecaa26a4f53b/scratchpad'
exec(open(SP+'/market.py').read())
MK='/home/user/Claude-movil/pieza-clave/marketplace/'
old=open(MK+'textos-marketplace.md').read()
OLDT={}
for sec in old.split('\n## ')[1:]:
    folder=re.search(r'Carpeta: `([^/]+)/`',sec); t=re.search(r'\*\*Título\*\*[^\n]*\n```\n(.*?)\n```',sec)
    if folder and t: OLDT[folder.group(1)]=t.group(1)
T={'gato-tijera-2t':'Gato de tijera 2 toneladas con manivela, para la maleta',
'gato-botella-20t':'Gato hidráulico tipo botella 20 toneladas',
'caja-dados-32':'Caja de dados 32 piezas con matraca y maletín',
'juego-dados-46':'Juego de dados 1/4" 46 piezas con matraca y maletín',
'dados-torx':'Juego de dados Torx tipo estrella (E-Torx) con estuche',
'set-3-matracas':'Set de 3 matracas (raches) 1/4", 3/8" y 1/2"',
'extractor-filtro-aceite':'Extractor de filtro de aceite de 3 patas ajustable',
'bomba-gasolina-2068':'Bomba de gasolina universal 2068 (pila de gasolina)',
'prensa-banco-5':'Prensa de banco 5 pulgadas giratoria con yunque',
'prensa-banco-6':'Prensa de banco 6 pulgadas giratoria con yunque',
'kit-repara-rosca':'Kit repara rosca helicoides (helicoil) con machos e insertador',
'medidor-presion-gasolina':'Medidor de presión de gasolina kit completo con maletín',
'kit-tiempo-renault-1':'Kit sincronizador de tiempo Renault (calado) con maletín',
'kit-tiempo-renault-2':'Kit sincronizador de tiempo Renault (calado) con maletín',
'recoge-espirales':'Recoge espirales reforzado con pines (compresor de resortes)',
'extractor-damper':'Extractor de damper y poleas 3 patas con maletín',
'careta-soldar':'Careta de soldar electrónica fotosensible',
'pistola-impacto-300nm-amarilla':'Pistola de impacto inalámbrica 300 Nm amarilla, con batería y cargador',
'pistola-impacto-300nm-verde':'Pistola de impacto inalámbrica 300 Nm verde, con batería y cargador',
'pistola-impacto-2000nm':'Pistola de impacto 3/4" 2000 Nm con 2 baterías y cargador',
'cargador-bateria-12v':'Cargador de batería 12 V 6 A para moto y carro',
'mini-ups':'Mini UPS para router y módem, 6 a 8 horas de internet',
'caracol-motobomba-2':'Caracol para motobomba 2 pulgadas',
'compresimetro':'Compresímetro de motor 9 piezas con estuche',
'taladro-inalambrico':'Taladro inalámbrico 21 V con 2 baterías y maletín'}
CAT={'bomba-gasolina-2068':'Repuestos y accesorios para vehículos','mini-ups':'Electrónica','caracol-motobomba-2':'Jardín y exteriores'}
EXTRA={'kit-tiempo-renault-1':'Modelo 1 (placas negras). Pregúntanos para qué motor es antes de comprar.','kit-tiempo-renault-2':'Modelo 2 (reglas y pasadores). Pregúntanos para qué motor es antes de comprar.',
'bomba-gasolina-2068':'Revisa que la referencia coincida con la de tu carro; si tienes dudas, mándanos foto de la tuya.',
'caracol-motobomba-2':'Mándanos foto de tu motobomba y te confirmamos que es el de ella.'}
CIERRE="""📍 Calle 181, Naguanagua, Carabobo (Multitienda JM)
🕗 Lunes a sábado, de 8 a. m. a 5 p. m.
🚚 Delivery en Valencia con costo según la zona, o retiro en el local
💵 Pago: efectivo, transferencia o pago móvil
🛡️ Garantía de 1 mes en casi todos los productos (confírmala al escribirnos)
💬 Escríbenos por aquí y te decimos si te sirve.
Pieza Clave · @piezaclave.valencia"""
CATN={'taller':'Taller','pro':'Taller pro','ext':'Exterior','ele':'Eléctricas'}
order=['taller','pro','ele','ext']
out=["# Textos para Facebook Marketplace","",
"Cada producto tiene su carpeta. Sube las imágenes en orden: `1-principal`, `2-ficha`, `3-como-comprar` y, si están, las fotos reales `4`, `5` y `6` (las reales dan confianza: súbelas).","",
"Contacto: por Messenger (el chat de Marketplace) e Instagram. Horario: lunes a sábado, 8 a. m. a 5 p. m. Ubicación de la publicación: Naguanagua, Carabobo. Estado: Nuevo (confírmalo).","",
"Sin precio todavía (completa **[precio]** y avísame para ponerlo en las imágenes): "+", ".join(f"{n} {s}".strip() for k,c,n,s,*_ in P if k not in PRICE)+".",""]
idx=["| Línea | Producto | Precio | Carpeta |","|---|---|---|---|"]
body=[]
for cat in order:
    body.append(f"\n# {CATN[cat]}\n")
    for k,c,name,sub,specs,uses in [x for x in P if x[1]==cat]:
        slug=SLUG[k]; pr=PRICE.get(k)
        tit=T.get(slug) or OLDT.get(slug,'').replace(' | Entregas en Valencia','')
        tit=(tit+' | Entregas en Valencia') if len(tit)+22<=99 else tit
        fotos=sorted(f for f in os.listdir(MK+slug) if f[0].isdigit())
        idx.append(f"| {CATN[cat]} | {name} {sub} | {str(pr)+'$' if pr else '—'} | `{slug}/` |")
        desc=[f"{name} {sub}."]+[f"• {v} – {kk.lower()}" for ic,v,kk in specs]+[f"• {u}" for u in uses]
        if slug in EXTRA: desc+=['',EXTRA[slug]]
        desc+=['',f"Precio: {str(pr)+'$' if pr else '[precio]'}",CIERRE]
        body+= [f"## {name} {sub}"+(" (amarilla)" if slug.endswith("amarilla") else " (verde)" if slug.endswith("verde") else "")+(f" — {pr}$" if pr else ""),f"Carpeta: `{slug}/` · Imágenes: {', '.join(fotos)}","",
            f"**Título** ({len(tit)} caracteres)","```",tit,"```",
            f"**Precio para el campo de precio:** {pr if pr else '[completar]'}",
            f"**Categoría:** {CAT.get(slug,'Herramientas')} · **Estado:** Nuevo","","**Descripción**","```","\n".join(desc),"```",""]
open(MK+'textos-marketplace.md','w').write("\n".join(out+idx+body)+"\n")
print(len(P), sum(1 for x in P if x[0] in PRICE))
