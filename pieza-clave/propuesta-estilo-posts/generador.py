# Generador de la propuesta de estilo de posts (copia de trabajo; rutas apuntan al scratchpad de la sesión).
import json
# v4: sistema con personalidad (producto protagonista, tipografía grande, diagonales, fichas con íconos)
SP='/tmp/claude-0/-home-user-Claude-movil/59907f33-5efd-5727-b54e-ecaa26a4f53b/scratchpad'
FD=SP+'/fonts/'; CUT='file://'+SP+'/cut/'; SC='file://'+SP+'/esc/sel/'
LG='file:///home/user/Claude-movil/pieza-clave/logo-v2/'
AC='#12343b'; CH='#f26a1b'; GR='#161b1d'; CO='#eef1f1'; LI='#cbd3d5'; EX='#2f7d4a'; VO='#f7c531'
CSS=f"""
@font-face{{font-family:BC;font-weight:600;src:url(file://{FD}Barlow_Condensed_wght_600.ttf)}}
@font-face{{font-family:BC;font-weight:700;src:url(file://{FD}Barlow_Condensed_wght_700.ttf)}}
@font-face{{font-family:BC;font-weight:800;src:url(file://{FD}Barlow_Condensed_wght_800.ttf)}}
@font-face{{font-family:B;font-weight:400;src:url(file://{FD}Barlow_wght_400.ttf)}}
@font-face{{font-family:B;font-weight:500;src:url(file://{FD}Barlow_wght_500.ttf)}}
@font-face{{font-family:B;font-weight:600;src:url(file://{FD}Barlow_wght_600.ttf)}}
@font-face{{font-family:AX;font-weight:900;src:url(file://{FD}Archivo_wdth_wght_125_900.ttf)}}
@font-face{{font-family:AW;font-weight:900;src:url(file://{FD}Archivo_wdth_wght_112_900.ttf)}}
*{{box-sizing:border-box;margin:0}} body{{margin:0}}
.s{{position:relative;overflow:hidden;font-family:B;color:{GR};background:{CO}}}
.ab{{position:absolute}}
.ax{{font-family:AX;font-weight:900;text-transform:uppercase;line-height:.86;letter-spacing:-1px}}
.aw{{font-family:AW;font-weight:900;text-transform:uppercase;line-height:.9;letter-spacing:-.5px}}
.bc{{font-family:BC;font-weight:800;text-transform:uppercase;line-height:.92}}
.lab{{font:600 24px/1 B;letter-spacing:.16em;text-transform:uppercase}}
.body{{font:500 34px/1.35 B}}
.tag{{display:inline-block;transform:skewX(-12deg);padding:10px 30px 12px}}
.tag>span{{display:inline-block;transform:skewX(12deg)}}
.prod{{position:absolute;object-fit:contain;filter:drop-shadow(0 30px 28px rgba(18,52,59,.35)) drop-shadow(0 6px 8px rgba(18,52,59,.25))}}
.shadow{{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(18,52,59,.38),rgba(18,52,59,0))}}
.pill{{white-space:nowrap;display:inline-flex;align-items:center;gap:16px;border-radius:999px;padding:18px 34px;font:700 34px/1 BC;letter-spacing:.04em;text-transform:uppercase}}
.specs{{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;background:#fff;border-radius:6px;box-shadow:0 14px 30px rgba(18,52,59,.12)}}
.spec{{display:flex;gap:18px;align-items:center;padding:26px 24px}}
.spec+.spec{{border-left:2px solid {LI}}}
.spec .v{{font:800 46px/1 BC;color:{AC};text-transform:uppercase}}
.spec .k{{font:600 22px/1.15 B;color:#5b6b70;letter-spacing:.06em;text-transform:uppercase;margin-top:6px}}
.ico{{width:66px;height:66px;flex:none}}
.dot{{position:absolute;width:20px;height:20px;border-radius:50%;background:{CH};border:4px solid #fff;box-shadow:0 0 0 2px {CH}}}
.co{{position:absolute;font:700 30px/1.05 BC;text-transform:uppercase;color:{AC}}}
.co small{{display:block;font:500 22px/1.2 B;text-transform:none;color:#5b6b70;margin-top:4px}}
"""
BP=f"""<svg class="ab" style="inset:0" width="100%" height="100%" viewBox="0 0 1080 1350" preserveAspectRatio="none"><defs>
<pattern id="g" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M54 0H0V54" fill="none" stroke="#c4cfd1" stroke-width="1"/></pattern></defs>
<rect width="1080" height="1350" fill="url(#g)" opacity=".55"/>
<g fill="none" stroke="#b9c6c8" stroke-width="1.5" opacity=".7"><circle cx="820" cy="560" r="300"/><circle cx="820" cy="560" r="210" stroke-dasharray="6 8"/><path d="M500 560H1080M820 240V900"/></g></svg>"""
ICO={
'peso':f'<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="{CH}" stroke-width="4" stroke-linejoin="round"><path d="M14 54L20 22H44L50 54Z"/><circle cx="32" cy="15" r="6"/></svg>',
'altura':f'<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="{CH}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 6V58M20 18L32 6L44 18M20 46L32 58L44 46"/><path d="M8 6H20M8 58H20" opacity=".5"/></svg>',
'estuche':f'<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="{CH}" stroke-width="4" stroke-linejoin="round"><rect x="6" y="20" width="52" height="34" rx="4"/><path d="M22 20V12H42V20M6 34H58"/></svg>',
'camion':f'<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="{CH}" stroke-width="4" stroke-linejoin="round"><path d="M4 16H38V44H4ZM38 26H50L60 36V44H38"/><circle cx="16" cy="48" r="6" fill="#fff"/><circle cx="48" cy="48" r="6" fill="#fff"/></svg>',
'chat':f'<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="{CH}" stroke-width="4" stroke-linejoin="round"><path d="M8 12H56V44H26L14 54V44H8Z"/><path d="M20 26H44M20 34H36" stroke-linecap="round"/></svg>',
}
WA='<svg width="44" height="44" viewBox="0 0 32 32"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-3.9-.5-5.6-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 0 0 2.1-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.1-.3-.2-.6-.4z"/></svg>'
def wa_pill(txt='Escríbenos por WhatsApp',bg=CH,fg=GR): return f'<span class="pill" style="background:{bg};color:{fg}">{WA}{txt}</span>'
def iso(neg=False,h=58): return f'<img src="{LG}isotipo-{"negativo" if neg else "color"}.svg" style="height:{h}px">'
def logo_h(neg=True,h=64): return f'<img src="{LG}logo-horizontal-{"negativo" if neg else "color"}.svg" style="height:{h}px">'
def prod(f,l,t,w,h,rot=0,shadow=True,sw=None):
    sh=f'<div class="shadow" style="left:{l+w*0.12}px;top:{t+h*0.86}px;width:{sw or w*0.76}px;height:{h*0.16}px"></div>' if shadow else ''
    return sh+f'<img class="prod" src="{CUT}{f}" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
def footband(right='@piezaclave.valencia<br>Entregas en Valencia',bg=AC,h=150,pill=True):
    return f'''<div class="ab" style="left:0;right:0;bottom:0;height:{h}px;background:{bg};display:flex;align-items:center;justify-content:space-between;padding:0 40px">
{wa_pill() if pill else logo_h(True,64)}<span style="font:600 24px/1.3 B;color:#d5e2e4;text-align:right;letter-spacing:.04em">{right}</span></div>'''
def nxt(n,tot,col=AC): return f'<span class="lab" style="color:{col}">{n} / {tot}  →</span>'
V={}
def put(n,html,w=1080,h=1350): V[n]=(w,h,html)

# 1) Pieza clave de la semana: ficha estilo catálogo (diagonales + tag + íconos)
put('lun-2-pieza-clave-gato', f'''{BP}
<div class="ab" style="right:-340px;top:-60px;width:560px;height:300px;background:{AC};transform:skewX(-28deg)"></div>
<div class="ab" style="right:110px;top:-60px;width:46px;height:300px;background:{CH};transform:skewX(-28deg)"></div>
<div class="ab" style="left:-80px;bottom:150px;width:420px;height:120px;background:{CH};transform:skewX(-28deg)"></div>
<div class="ab" style="left:40px;top:44px;display:flex;gap:16px;align-items:center">{iso(False,62)}<span class="lab" style="color:{AC};line-height:1.25">La pieza clave<br>de la semana</span></div>
<div class="ab ax" style="left:40px;top:190px;font-size:190px;color:{AC}">Gato</div>
<div class="ab aw" style="left:44px;top:368px;font-size:92px;color:{AC}">hidráulico</div>
<div class="ab tag" style="left:48px;top:470px;background:{CH}"><span class="aw" style="font-size:64px;color:#fff">2 toneladas</span></div>
<div class="ab" style="right:44px;top:250px;text-align:right;font:600 22px/1.6 B;letter-spacing:.18em;color:#5b6b70;text-transform:uppercase">Sube rápido<br>Base ancha<br>Con estuche<div style="width:70px;height:4px;background:{CH};margin:12px 0 0 auto"></div></div>
{prod('gato-pack.png',130,470,900,592)}
<div class="ab specs" style="left:40px;right:40px;top:1072px">
 <div class="spec">{ICO['peso']}<div><div class="v">2 t</div><div class="k">Capacidad</div></div></div>
 <div class="spec">{ICO['altura']}<div><div class="v">12,5–30 cm</div><div class="k">Altura</div></div></div>
 <div class="spec">{ICO['estuche']}<div><div class="v">Estuche</div><div class="k">Incluido</div></div></div>
</div>
{footband(h=130)}''')

# 2) Portada de carrusel: pregunta grande + ola naranja + producto (estilo Construlider)
put('mar-1-portada', f'''
<div class="ab" style="left:0;right:0;top:0;height:1350px;background:#f4f6f6"></div>
<svg class="ab" style="left:0;top:560px" width="1080" height="790" viewBox="0 0 1080 790"><defs><clipPath id="w"><path d="M0 120C260 10 520 0 760 70S1000 150 1080 40V790H0Z"/></clipPath></defs>
<g clip-path="url(#w)"><rect width="1080" height="790" fill="{CH}"/><image href="{SC}gato45b.jpg" x="0" y="-80" width="1080" height="1350" preserveAspectRatio="xMidYMid slice" opacity=".22" style="mix-blend-mode:multiply"/></g></svg>
<div class="ab" style="right:40px;top:52px">{logo_h(False,62)}</div>
<div class="ab" style="left:40px;right:40px;top:210px;text-align:center;font:600 50px/1.15 B;color:{GR}">¿El gato que vino con tu carro…</div>
<div class="ab ax" style="left:0;right:0;top:300px;text-align:center;font-size:126px;color:{AC};white-space:nowrap">¿te sirve?</div>
{prod('gato-pack.png',90,600,900,592,shadow=False)}
<div class="ab" style="left:0;right:0;bottom:70px;display:flex;justify-content:center"><span class="pill" style="background:#fff;color:{AC};box-shadow:0 10px 24px rgba(0,0,0,.18)">Desliza y compara  →</span></div>
<div class="ab tag" style="left:40px;top:60px;background:{AC}"><span class="lab" style="color:#fff">Taller · 1 / 5</span></div>''')

# 3) Ficha con señalamientos (estilo "TALADRO" vertical + callouts)
put('mar-3-este-gato', f'''{BP}
<div class="ab ax" style="left:-10px;top:1270px;transform-origin:0 0;transform:rotate(-90deg);font-size:330px;color:{CH};white-space:nowrap">Gato</div>
<div class="ab" style="right:40px;top:44px;background:{AC};color:#fff;padding:10px 16px;font:700 26px/1 BC;letter-spacing:.08em;text-transform:uppercase;border:3px solid {CH}">El que tenemos · 3 / 5</div>
<div class="ab bc" style="left:300px;top:120px;font-size:84px;color:{AC}">Así trabaja<br><span style="color:{CH}">por dentro</span></div>
{prod('gato-pack.png',250,420,780,513,shadow=True)}
<svg class="ab" style="inset:0" width="1080" height="1350"><g stroke="{AC}" stroke-width="3" fill="none">
<path d="M932 462V372"/><path d="M362 742V650"/><path d="M340 872V990"/><path d="M776 802V990"/></g></svg>
<div class="dot" style="left:922px;top:452px"></div><div class="co" style="left:800px;top:290px;width:240px;text-align:right">Palanca<small>Bombeas y sube</small></div>
<div class="dot" style="left:352px;top:732px"></div><div class="co" style="left:262px;top:566px;width:260px">Asiento<small>Va en el punto de apoyo</small></div>
<div class="dot" style="left:330px;top:862px"></div><div class="co" style="left:262px;top:1000px;width:260px">Ruedas<small>Entra rodando bajo el carro</small></div>
<div class="dot" style="left:766px;top:792px"></div><div class="co" style="left:700px;top:1000px;width:300px">Base ancha<small>No se ladea como la tijera</small></div>
<div class="ab" style="left:300px;right:40px;top:1120px;border-left:6px solid {CH};padding-left:22px;font:500 30px/1.35 B;color:{GR}">Capacidad 2 t · Altura 12,5–30 cm · Estuche incluido. Si tu carro es muy bajo, pregúntanos antes.</div>
<div class="ab" style="left:300px;bottom:40px;display:flex;gap:20px;align-items:center">{iso(False,52)}<span class="lab" style="color:{AC}">Desliza →</span></div>''')

# 4) Tarjeta de producto exterior con precio (estilo STIHL)
RINGS=''.join(f'<ellipse cx="700" cy="760" rx="{r*1.25}" ry="{r}" />' for r in range(40,900,38))
put('sab-4-motosierra', f'''
<div class="ab" style="inset:0;background:#e9eceb"></div>
<svg class="ab" style="inset:0" width="1080" height="1350"><g fill="none" stroke="#c9d0ce" stroke-width="2">{RINGS}</g></svg>
<div class="ab" style="left:0;width:700px;top:900px;height:250px;background:#9aa6a4"></div>
<div class="ab" style="left:40px;top:60px"><span class="lab" style="color:{EX}">Exterior · 4 / 5</span>
<div class="aw" style="font-size:118px;color:#4a5558;margin-top:18px">Motosierra</div><div class="bc" style="font-size:56px;color:#6b7679;margin-top:6px">a gasolina</div></div>
{prod('moto-pack.png',130,300,880,521,rot=-12,shadow=False)}
<div class="ab ax" style="left:40px;top:930px;font-size:74px;color:#fff">Ramas<br>y troncos</div>
<div class="ab" style="left:40px;top:1070px;font:500 26px/1.3 B;color:#fff;max-width:620px">Trae guantes y protector de espada. Úsala con lentes y botas.</div>
<div class="ab" style="right:40px;top:1010px;background:{EX};padding:18px 26px;display:flex;align-items:center;gap:14px">{iso(True,48)}<span class="aw" style="font-size:36px;color:#fff">Pieza Clave</span></div>
<div class="ab" style="left:40px;bottom:50px;display:flex;gap:16px;align-items:center;color:#4a5558">{WA}<div style="font:600 26px/1.2 B">WhatsApp<br><b style="font:700 34px/1 BC;letter-spacing:.03em">Te asesoramos</b></div></div>
<div class="ab" style="right:40px;bottom:46px;text-align:right"><div style="font:600 20px/1 B;color:#5b6b70;letter-spacing:.1em;text-transform:uppercase">Pregunta disponibilidad</div><div class="aw" style="font-size:44px;color:{AC};margin-top:10px">Precio por <span style="color:{CH}">WhatsApp</span></div></div>''')

# 5) Portada con número gigante
put('jue-1-portada', f'''
<div class="ab" style="inset:0;background:{AC}"></div>
<div class="ab ax" style="left:-30px;top:120px;font-size:560px;color:transparent;-webkit-text-stroke:4px #2c5560;letter-spacing:-10px">108</div>
<div class="ab" style="left:-100px;top:930px;width:1400px;height:440px;background:{CH};transform:rotate(-8deg)"></div>
{prod('dados-pack.png',250,190,600,822,rot=-6)}
<div class="ab" style="left:40px;top:50px;display:flex;justify-content:space-between;right:40px">{iso(True,58)}<span class="lab" style="color:#a9c3c7">Taller · 1 / 4</span></div>
<div class="ab" style="left:40px;top:1060px;transform:rotate(-8deg);transform-origin:0 0"><div class="ax" style="font-size:118px;color:{GR}">108 piezas</div>
<div class="tag" style="background:{GR};margin-top:14px"><span class="aw" style="font-size:40px;color:#fff">¿Qué trae? Te lo explicamos →</span></div></div>''')

# 6) Cierre / CTA
put('mar-5-cta', f'''
<div class="ab" style="inset:0;background:{AC}"></div>
<div class="ab" style="right:-260px;top:790px;width:760px;height:700px;background:#173f47;transform:skewX(-18deg)"></div>
<div class="ab" style="right:470px;top:790px;width:36px;height:700px;background:{CH};transform:skewX(-18deg)"></div>
<div class="ab" style="left:40px;top:60px">{logo_h(True,66)}</div>
<div class="ab" style="left:40px;top:220px;font:600 46px/1.1 B;color:#d5e2e4">Antes de comprar, dinos:</div>
<div class="ab ax" style="left:36px;top:290px;font-size:178px;color:#fff">¿Qué<br>carro<br><span style="color:{CH}">tienes?</span></div>
{prod('gato-pack.png',470,860,580,382,rot=-4)}
<div class="ab" style="left:40px;top:860px;display:grid;gap:20px">
 <div style="display:flex;gap:14px;align-items:center;color:#fff;font:600 32px/1 B">{ICO['chat']}Te decimos si te sirve</div>
 <div style="display:flex;gap:14px;align-items:center;color:#fff;font:600 32px/1 B">{ICO['camion']}Entregas en Valencia</div>
</div>
<div class="ab" style="left:40px;right:40px;bottom:60px;display:flex;justify-content:space-between;align-items:center">{wa_pill()}<span class="lab" style="color:#a9c3c7">5 / 5</span></div>''')

json.dump([{'name':n,'w':w,'h':h,'html':'<style>'+CSS+'</style><div class="s" style="width:%dpx;height:%dpx">'%(w,h)+html+'</div>'} for n,(w,h,html) in V.items()],open(SP+'/posts4.json','w'))
print(len(V))
