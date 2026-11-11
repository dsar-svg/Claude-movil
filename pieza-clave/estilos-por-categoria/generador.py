# Generador de posts por categoría (copia de trabajo; las rutas apuntan al scratchpad de la sesión).
import json, os
# v5: un estilo por categoría (Taller, Taller pro, Exterior, Eléctricas, Marca) con formatos comunes
SP='/tmp/claude-0/-home-user-Claude-movil/59907f33-5efd-5727-b54e-ecaa26a4f53b/scratchpad'
FD=SP+'/fonts/'; CUTD=SP+'/cut/'; CUT='file://'+CUTD; PH='file://'+SP+'/fotos/'
LG='file:///home/user/Claude-movil/pieza-clave/logo-v2/'
AC='#12343b'; CH='#f26a1b'; GR='#161b1d'; CO='#eef1f1'; LI='#cbd3d5'; EX='#2f7d4a'; VO='#f7c531'
PK={'gato':'gato-pack','dados':'dados-pack','moto':'moto-pack','adapt':'adapt-pack','llaves':'llaves-pack','mano':'mano-pack',
    'taladro':'taladro-pack','engra':'engra-pack','compre':'compre-pack','multi':'multi-pack','corta':'corta-pack','poli':'poli-pack',
    'esmeril':'esmeril-pack','desma':'desma-pack'}
OLD={'adapt':'02-adaptadores-impacto','llaves':'03-llaves-combinadas-14','mano':'04-manifold-refrigeracion','taladro':'06-taladro-inalambrico',
     'engra':'08-engrasadora','compre':'09-compresimetro','multi':'10-multiplicador-torque','corta':'11-cortadora-cesped','poli':'12-polipasto-electrico',
     'esmeril':'13-esmeril-taladro','desma':'14-desmalezadora'}
PRICE={'gato':42,'adapt':20,'llaves':20,'mano':38}  # precio al cliente en $ (los demás: precio por WhatsApp)
def price_sticker(k,x,y,d=210,rot=-8):
    if k not in PRICE: return ''
    return f'''<div class="ab" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;background:{CH};box-shadow:0 14px 30px rgba(0,0,0,.25);transform:rotate({rot}deg);display:flex;flex-direction:column;align-items:center;justify-content:center;border:6px solid #fff">
<div style="font:700 24px/1 BC;letter-spacing:.14em;text-transform:uppercase;color:{GR}">Precio</div><div class="ax" style="font-size:{int(d*0.36)}px;color:#fff;letter-spacing:-2px;margin-top:6px">{PRICE[k]}$</div></div>'''
def src(k):
    f=PK[k]
    if not os.path.exists(CUTD+f+'.png'): f=OLD[k]
    return CUT+f+'.png'

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
.s{{position:relative;overflow:hidden;font-family:B}}
.ab{{position:absolute}}
.ax{{font-family:AX;font-weight:900;text-transform:uppercase;line-height:.88;letter-spacing:-1px}}
.aw{{font-family:AW;font-weight:900;text-transform:uppercase;line-height:.92;letter-spacing:-.5px}}
.bc{{font-family:BC;font-weight:800;text-transform:uppercase;line-height:.92}}
.lab{{font:600 24px/1 B;letter-spacing:.16em;text-transform:uppercase}}
.tag{{display:inline-block;transform:skewX(-12deg);padding:10px 28px 12px}}
.tag>span{{display:inline-block;transform:skewX(12deg)}}
.prod{{position:absolute;object-fit:contain;filter:drop-shadow(0 30px 28px rgba(0,0,0,.30)) drop-shadow(0 6px 8px rgba(0,0,0,.20))}}
.shadow{{position:absolute;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.32),rgba(0,0,0,0))}}
.pill{{white-space:nowrap;display:inline-flex;align-items:center;gap:16px;border-radius:999px;padding:18px 34px;font:700 34px/1 BC;letter-spacing:.04em;text-transform:uppercase}}
.specs{{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;border-radius:6px}}
.spec{{display:flex;gap:16px;align-items:center;padding:24px 22px}}
.spec .v{{font:800 42px/1 BC;text-transform:uppercase}}
.spec .k{{font:600 21px/1.15 B;letter-spacing:.06em;text-transform:uppercase;margin-top:6px}}
.ico{{width:62px;height:62px;flex:none}}
.dot{{position:absolute;width:20px;height:20px;border-radius:50%;background:{CH};border:4px solid #fff;box-shadow:0 0 0 2px {CH}}}
.co{{position:absolute;font:700 30px/1.05 BC;text-transform:uppercase}}
.co small{{display:block;font:500 22px/1.2 B;text-transform:none;opacity:.8;margin-top:4px}}
.num{{font:800 120px/0.8 BC}}
"""
# ---------- iconos (trazo, color variable) ----------
def I(name,c):
    P={
    'peso':'<path d="M14 54L20 22H44L50 54Z"/><circle cx="32" cy="15" r="6"/>',
    'altura':'<path d="M32 6V58M20 18L32 6L44 18M20 46L32 58L44 46"/>',
    'estuche':'<rect x="6" y="20" width="52" height="34" rx="4"/><path d="M22 20V12H42V20M6 34H58"/>',
    'camion':'<path d="M4 16H38V44H4ZM38 26H50L60 36V44H38"/><circle cx="16" cy="48" r="6"/><circle cx="48" cy="48" r="6"/>',
    'chat':'<path d="M8 12H56V44H26L14 54V44H8Z"/><path d="M20 26H44M20 34H36"/>',
    'gas':'<path d="M32 6C32 6 14 28 14 40A18 18 0 0 0 50 40C50 28 32 6 32 6Z"/>',
    'hoja':'<path d="M10 54C10 24 30 10 56 8C54 34 40 54 10 54Z"/><path d="M10 54L36 28"/>',
    'escudo':'<path d="M32 6L54 14V30C54 44 44 54 32 58C20 54 10 44 10 30V14Z"/><path d="M22 32L30 40L44 24"/>',
    'gauge':'<circle cx="32" cy="34" r="24"/><path d="M32 34L44 22M14 34H18M46 34H50M32 14V18"/>',
    'bateria':'<rect x="10" y="16" width="40" height="34" rx="4"/><path d="M50 26H56V40H50M24 33H36M30 27V39"/>',
    'enchufe':'<path d="M22 6V20M42 6V20M14 20H50V32A18 18 0 0 1 14 32Z"/><path d="M32 50V60"/>',
    'llave':'<path d="M40 8A14 14 0 0 0 30 30L8 52L14 58L36 36A14 14 0 0 0 56 24L46 30L36 28L34 18Z"/>',
    'piezas':'<rect x="8" y="8" width="20" height="20" rx="3"/><rect x="36" y="8" width="20" height="20" rx="3"/><rect x="8" y="36" width="20" height="20" rx="3"/><rect x="36" y="36" width="20" height="20" rx="3"/>',
    'medida':'<rect x="6" y="22" width="52" height="20" rx="2"/><path d="M14 22V30M22 22V34M30 22V30M38 22V34M46 22V30"/>',
    'boton':'<rect x="18" y="6" width="28" height="52" rx="6"/><circle cx="32" cy="20" r="5"/><circle cx="32" cy="38" r="5"/>',
    'check':'<circle cx="32" cy="32" r="24"/><path d="M21 33L29 41L44 25"/>',
    'rayo':'<path d="M36 4L12 36H30L26 60L52 26H34Z"/>',
    'pin':'<path d="M32 58C32 58 12 38 12 24A20 20 0 0 1 52 24C52 38 32 58 32 58Z"/><circle cx="32" cy="24" r="7"/>',
    'pago':'<rect x="6" y="14" width="52" height="36" rx="4"/><path d="M6 24H58M14 40H26"/>',
    }
    return f'<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg>'
WA='<svg width="44" height="44" viewBox="0 0 32 32"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-3.9-.5-5.6-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 0 0 2.1-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.1-.3-.2-.6-.4z"/></svg>'

# ---------- temas por categoría ----------
def deco_taller(w,h,T):
    return f'''<svg class="ab" style="inset:0" width="{w}" height="{h}"><defs><pattern id="g" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M54 0H0V54" fill="none" stroke="#c4cfd1" stroke-width="1"/></pattern></defs>
<rect width="{w}" height="{h}" fill="url(#g)" opacity=".55"/><g fill="none" stroke="#b9c6c8" stroke-width="1.5" opacity=".7"><circle cx="{w*.76}" cy="{h*.42}" r="300"/><circle cx="{w*.76}" cy="{h*.42}" r="210" stroke-dasharray="6 8"/></g></svg>
<div class="ab" style="right:-300px;top:-60px;width:520px;height:160px;background:{AC};transform:skewX(-28deg)"></div>
<div class="ab" style="right:150px;top:-60px;width:40px;height:160px;background:{CH};transform:skewX(-28deg)"></div>'''
def deco_pro(w,h,T):
    ticks=''.join(f'<line x1="{w*.62+330*__import__("math").cos(a*3.14159/180)}" y1="{h*.47+330*__import__("math").sin(a*3.14159/180)}" x2="{w*.62+(300 if i%5 else 280)*__import__("math").cos(a*3.14159/180)}" y2="{h*.47+(300 if i%5 else 280)*__import__("math").sin(a*3.14159/180)}"/>' for i,a in enumerate(range(135,406,6)))
    ruler=''.join(f'<line x1="0" y1="{y}" x2="{28 if y%100==0 else 16}" y2="{y}"/>' for y in range(0,h,20))
    return f'''<div class="ab" style="inset:0;background:radial-gradient(circle at 62% 47%,#25333a 0,#151b1e 62%)"></div>
<svg class="ab" style="inset:0" width="{w}" height="{h}"><g stroke="#3b4a50" stroke-width="3" fill="none"><circle cx="{w*.62}" cy="{h*.47}" r="350" stroke-width="2"/>{ticks}</g>
<path d="M{w*.62+350*0.7071} {h*.47+350*0.7071}A350 350 0 0 0 {w*.62+350} {h*.47}" stroke="{CH}" stroke-width="6" fill="none"/>
<g stroke="#4c5d63" stroke-width="2">{ruler}</g></svg>'''
def deco_ext(w,h,T):
    rings=''.join(f'<ellipse cx="{w*.66}" cy="{h*.5}" rx="{r*1.2}" ry="{r}"/>' for r in range(40,1000,40))
    return f'''<div class="ab" style="inset:0;background:#e6ebe4"></div>
<svg class="ab" style="inset:0" width="{w}" height="{h}"><g fill="none" stroke="#cbd6c8" stroke-width="2">{rings}</g>
<path d="M0 {h*.80}C{w*.3} {h*.72} {w*.55} {h*.86} {w} {h*.76}V{h}H0Z" fill="{EX}"/>
<path d="M0 {h*.83}C{w*.35} {h*.76} {w*.6} {h*.9} {w} {h*.80}" stroke="#7fb08c" stroke-width="4" fill="none"/></svg>'''
def deco_ele(w,h,T):
    stripes=''.join(f'<line x1="{x}" y1="0" x2="{x-h*0.5}" y2="{h}"/>' for x in range(0,w+h,46))
    return f'''<div class="ab" style="inset:0;background:{VO}"></div>
<svg class="ab" style="inset:0" width="{w}" height="{h}"><g stroke="#e3b11b" stroke-width="10">{stripes}</g>
<path d="M{w*.62} {h*.06}L{w*.40} {h*.50}H{w*.56}L{w*.46} {h*.96}L{w*.88} {h*.40}H{w*.68}L{w*.80} {h*.06}Z" fill="{GR}" opacity=".07"/></svg>
<div class="ab" style="left:0;right:0;bottom:0;height:{h*.30}px;background:{GR};clip-path:polygon(0 30%,100% 0,100% 100%,0 100%)"></div>'''
def deco_marca(w,h,T):
    dots=f'<defs><pattern id="d" width="36" height="36" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="2" fill="#c3cdcf"/></pattern></defs><rect width="{w}" height="{h}" fill="url(#d)" opacity=".7"/>'
    return f'''<div class="ab" style="inset:0;background:{CO}"></div><svg class="ab" style="inset:0" width="{w}" height="{h}">{dots}</svg>
<img class="ab" src="{LG}isotipo-color.svg" style="right:-160px;top:{h*.30}px;height:{h*.62}px;opacity:.06">'''
T_TALLER=dict(k='taller',name='Taller',bg=CO,ink=AC,acc=CH,sub='#5b6b70',card='#fff',cardink=AC,line=LI,deco=deco_taller,iso='color',logo='color',chip=(CH,GR),dark=False,word=CH)
T_PRO=dict(k='pro',name='Taller pro',bg='#151b1e',ink='#fff',acc=CH,sub='#9fb1b5',card='#1f292d',cardink='#fff',line='#33444a',deco=deco_pro,iso='negativo',logo='negativo',chip=(CH,GR),dark=True,word='#2a383d')
T_EXT=dict(k='ext',name='Exterior',bg='#e6ebe4',ink='#1d3b28',acc=EX,sub='#53685a',card='#fff',cardink='#1d3b28',line='#cbd6c8',deco=deco_ext,iso='color',logo='color',chip=(EX,'#fff'),dark=False,word=EX)
T_ELE=dict(k='ele',name='Eléctricas',bg=VO,ink=GR,acc=GR,sub='#5a4a12',card=GR,cardink=VO,line='#3a3a3a',deco=deco_ele,iso='grafito',logo='grafito',chip=(GR,VO),dark=False,word=GR)
T_MARCA=dict(k='marca',name='Pieza Clave',bg=CO,ink=AC,acc=CH,sub='#5b6b70',card='#fff',cardink=AC,line=LI,deco=deco_marca,iso='color',logo='color',chip=(AC,'#fff'),dark=False,word=CH)

def iso(T,h=58): return f'<img src="{LG}isotipo-{T["iso"]}.svg" style="height:{h}px">'
def logo(T,h=64): return f'<img src="{LG}logo-horizontal-{T["logo"]}.svg" style="height:{h}px">'
def badge(T,extra=''):
    bg,fg=T['chip']
    ico={'pro':I('gauge',fg),'ext':I('hoja',fg),'ele':I('rayo',fg),'taller':I('llave',fg)}.get(T['k'],'')
    ico=ico.replace('class="ico"','style="width:30px;height:30px"')
    return f'<span class="tag" style="background:{bg}"><span style="display:inline-flex;gap:10px;align-items:center;font:700 26px/1 BC;letter-spacing:.1em;text-transform:uppercase;color:{fg}">{ico}{T["name"]}{extra}</span></span>'
def head(T,n=None,tot=None,left=None):
    r=f'<span class="lab" style="color:{T["sub"]}">{n} / {tot}</span>' if n else ''
    return f'<div class="ab" style="left:40px;top:44px;display:flex;gap:22px;align-items:center">{left or badge(T)}{r}</div>'
def prod(k,l,t,w,h,rot=0,shadow=True):
    sh=f'<div class="shadow" style="left:{l+w*0.12}px;top:{t+h*0.88}px;width:{w*0.76}px;height:{h*0.12}px"></div>' if shadow else ''
    return sh+f'<img class="prod" src="{src(k)}" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
def wa_pill(T,txt='Escríbenos por WhatsApp'):
    bg,fg=(CH,GR) if T['k']!='ele' else (GR,VO)
    if T['k']=='ext': bg,fg=('#fff',EX)
    return f'<span class="pill" style="background:{bg};color:{fg}">{WA}{txt}</span>'
def foot_next(T,label='Desliza'):
    return f'<div class="ab" style="left:40px;right:40px;bottom:40px;display:flex;justify-content:space-between;align-items:center">{iso(T,52)}<span class="lab" style="color:{T["acc"] if T["k"]!="ele" else GR}">{label} →</span></div>'
def foot_cta(T,n=None,tot=None):
    col='#fff' if T['k'] in ('ext','pro') else T['sub']
    r=f'<span class="lab" style="color:{col}">{n} / {tot}</span>' if n else f'<span style="font:600 24px/1.3 B;color:{col};text-align:right">@piezaclave.valencia<br>Entregas en Valencia</span>'
    return f'<div class="ab" style="left:40px;right:40px;bottom:44px;display:flex;justify-content:space-between;align-items:center">{wa_pill(T)}{r}</div>'
def specrow(T,items,top):
    bg=T['card']; bd=T['line']
    cells=''.join(f'<div class="spec" style="{"border-left:2px solid "+bd if i else ""}">{I(ic,CH if T["k"]!="ele" else VO)}<div><div class="v" style="color:{T["cardink"]}">{v}</div><div class="k" style="color:{T["sub"] if T["k"]!="ele" else "#cfc6a0"}">{k}</div></div></div>' for i,(ic,v,k) in enumerate(items))
    return f'<div class="ab specs" style="left:40px;right:40px;top:{top}px;background:{bg};box-shadow:0 14px 30px rgba(0,0,0,.12)">{cells}</div>'
V={}
def put(n,html,T,w=1080,h=1350): V[n]=(w,h,f'<div class="ab" style="inset:0;background:{T["bg"]}"></div>'+T['deco'](w,h,T)+html)

# ---------- formatos ----------
def portada(n,T,kicker,big,k,box,tot,size=150,top=170,extra='',maxh=None):
    l,t,w,h=box
    put(n,f'''{head(T,1,tot)}
<div class="ab" style="left:40px;right:40px;top:{top}px"><div style="font:600 46px/1.15 B;color:{T["sub"] if not T["dark"] else "#c9d6d9"}">{kicker}</div>
<div class="ax fit" data-maxh="{maxh or 1e9}" style="font-size:{size}px;color:{T["ink"]};margin-top:16px">{big}</div></div>
{extra}{prod(k,l,t,w,h) if k else ''}{foot_next(T,'Desliza y mira')}''',T)

def ficha(n,T,name,sub,tagtxt,k,box,specs,desc,i,tot,nsize=150,rot=0):
    l,t,w,h=box; t=max(t,470); h=min(h,985-t); l=max(l,40); w=min(w,1040-l)
    put(n,f'''{head(T,i,tot)}
<div class="ab" style="left:40px;right:40px;top:130px"><div class="ax fit" style="font-size:{nsize}px;color:{T["ink"]};white-space:nowrap">{name}</div>
<div class="aw" style="font-size:58px;color:{T["sub"] if T["k"]!="pro" else "#c9d6d9"};margin-top:10px">{sub}</div>
{f'<div class="tag" style="background:{T["acc"] if T["k"]!="ele" else GR};margin-top:18px"><span class="aw" style="font-size:44px;color:{"#fff" if T["k"]!="ele" else VO}">{tagtxt}</span></div>' if tagtxt else ''}</div>
{prod(k,l,t,w,h,rot)}{price_sticker(k,820,450)}
{specrow(T,specs,1000)}
<div class="ab" style="left:40px;right:40px;top:1150px;font:500 28px/1.35 B;color:{T["ink"] if T["k"]!="ext" else "#fff"}">{desc}</div>
<div class="ab" style="right:40px;bottom:36px">{iso(T,44) if T["k"]!="ext" else f'<img src="{LG}isotipo-negativo.svg" style="height:44px">'}</div>''',T)

def comparar(n,T,title,a,b,note,i,tot):
    def card(c,hl):
        bg=T['card']; ink=T['cardink']
        lines=''.join(f'<div style="display:flex;gap:14px;align-items:flex-start;font:500 30px/1.3 B;color:{ink}"><span style="color:{CH};font:800 30px/1.2 BC">›</span>{x}</div>' for x in c['lines'])
        img=prod(c['k'],0,0,0,0) if False else ''
        return f'''<div style="background:{bg};border-radius:10px;padding:34px;display:grid;gap:18px;align-content:start;{"outline:6px solid "+CH+";outline-offset:-6px" if hl else ""};box-shadow:0 14px 30px rgba(0,0,0,.10)">
<span class="tag" style="background:{CH if hl else LI};justify-self:start"><span class="bc" style="font-size:30px;color:{GR}">{c["tag"]}</span></span>
<div class="bc" style="font-size:54px;color:{ink}">{c["title"]}</div>{lines}</div>'''
    put(n,f'''{head(T,i,tot)}
<div class="ab ax fit" data-maxh="300" style="left:40px;right:40px;top:130px;font-size:84px;color:{T["ink"]}">{title}</div>
<div class="ab" style="left:40px;right:40px;top:450px;display:grid;grid-template-columns:1fr 1fr;gap:22px">{card(a,False)}{card(b,True)}</div>
<div class="ab" style="left:40px;right:40px;bottom:120px;background:{AC};border-radius:8px;padding:28px 32px;display:flex;gap:20px;align-items:center">{I("escudo",CH)}<div style="font:600 30px/1.3 B;color:#fff">{note}</div></div>
{foot_next(T)}''',T)

def lista(n,T,t1,t2,items,i,tot,dark=True):
    rows=''.join(f'<div style="display:grid;grid-template-columns:110px 1fr;gap:22px;align-items:center;padding:22px 0;border-top:2px solid {"#2c5560" if dark else LI}"><div class="num" style="color:{CH}">{j+1}</div><div style="font:600 34px/1.3 B;color:{"#fff" if dark else T["ink"]}">{x}</div></div>' for j,x in enumerate(items))
    bg=f'<div class="ab" style="inset:0;background:{AC}"></div><div class="ab" style="right:-300px;top:1100px;width:560px;height:400px;background:#173f47;transform:skewX(-24deg)"></div><div class="ab" style="right:210px;top:1100px;width:34px;height:400px;background:{CH};transform:skewX(-24deg)"></div>' if dark else ''
    put(n,f'''{bg}{head(T,i,tot)}
<div class="ab" style="left:40px;right:40px;top:140px"><div class="ax fit" style="font-size:96px;color:{"#fff" if dark else T["ink"]};white-space:nowrap">{t1}</div><div class="ax fit" style="font-size:96px;color:{CH};margin-top:8px;white-space:nowrap">{t2}</div></div>
<div class="ab" style="left:40px;right:40px;top:380px">{rows}</div>
<div class="ab" style="left:40px;right:40px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><img src="{LG}isotipo-negativo.svg" style="height:52px"><span class="lab" style="color:#fff">Desliza →</span></div>''',T)

def cta(n,T,pre,big,body,prods,i,tot,checks=None,size=150):
    ink='#fff';
    bg=f'<div class="ab" style="inset:0;background:{ {"taller":AC,"pro":"#0f1416","ext":"#1d3b28","ele":GR,"marca":AC}[T["k"]] }"></div>'
    acc=CH if T['k']!='ele' else VO
    if T['k']=='ext': acc='#8fd19e'
    slab=f'<div class="ab" style="right:-260px;top:780px;width:760px;height:700px;background:{ {"taller":"#173f47","pro":"#1d272b","ext":"#26503a","ele":"#262b2d","marca":"#173f47"}[T["k"]] };transform:skewX(-18deg)"></div><div class="ab" style="right:470px;top:780px;width:36px;height:700px;background:{acc};transform:skewX(-18deg)"></div>'
    ps=''.join(prod(k,*b) for k,b in prods)
    ch=''.join(f'<div style="display:flex;gap:14px;align-items:center;color:#fff;font:600 32px/1.1 B">{I(ic,acc)}{t}</div>' for ic,t in (checks or [('chat','Te decimos cuál te sirve'),('camion','Entregas en Valencia')]))
    put(n,f'''{bg}{slab}
<div class="ab" style="left:40px;top:56px">{f'<img src="{LG}logo-horizontal-negativo.svg" style="height:62px">'}</div>
<div class="ab fit" style="left:40px;right:40px;top:200px;font:600 44px/1.15 B;color:#d5e2e4;white-space:nowrap">{pre}</div>
<div class="ab ax fit" data-maxh="530" style="left:36px;right:36px;top:270px;font-size:{size}px;color:{ink}">{big.replace("<em>",f'<span style="color:{acc}">').replace("</em>","</span>")}</div>
<div class="ab" style="left:40px;width:520px;top:830px;font:500 30px/1.35 B;color:#d5e2e4">{body}</div>
<div class="ab" style="left:40px;top:1000px;display:grid;gap:18px">{ch}</div>
{ps}
<div class="ab" style="left:40px;right:40px;bottom:50px;display:flex;justify-content:space-between;align-items:center">{wa_pill(T if T["k"]!="ext" else T_TALLER)}<span class="lab" style="color:#a9c3c7">{i} / {tot}</span></div>''',T)

# ================= SEMANA 1 =================
# Lunes: presentación de marca (portada reel) + pieza clave + cómo comprar
put('lun-1-portada-reel-presentacion', f'''
<div class="ab" style="left:0;right:0;top:300px;display:flex;justify-content:center">{logo(T_MARCA,96)}</div>
<div class="ab ax fit" data-maxh="300" style="left:40px;right:40px;top:470px;font-size:150px;color:{AC};text-align:center">Esto es<br><span style="color:{CH}">Pieza Clave</span></div>
<div class="ab" style="left:80px;right:80px;top:820px;text-align:center;font:600 42px/1.3 B;color:#5b6b70">Herramientas para el carro, el taller y el patio. Valencia.</div>
{prod('gato',40,1120,520,342)}{prod('moto',540,1010,480,284,rot=-12)}{prod('dados',400,1180,280,383,rot=-6)}{prod('taladro',780,1250,240,305)}
<div class="ab" style="left:0;right:0;top:1610px;display:flex;justify-content:center;gap:16px">{''.join(badge(T) for T in (T_TALLER,T_PRO,T_EXT,T_ELE))}</div>''',T_MARCA,1080,1920)

V['lun-2-pieza-clave-gato']=None  # se llena abajo
ficha('lun-2-pieza-clave-gato',T_TALLER,'Gato','hidráulico','2 toneladas','gato',(140,470,880,579),
      [('peso','2 t','Capacidad'),('altura','12,5–30 cm','Altura'),('estuche','Estuche','Incluido')],
      'Sube rápido bombeando la palanca y queda firme con su base ancha. La pieza clave de la semana.',None,None,nsize=190)

portada('lun-3-cc-1-portada',T_MARCA,'Cómo comprar en Pieza Clave','Comprar<br>aquí es<br><span style="color:'+CH+'">escribir.</span>',None,(0,0,0,0),4,size=140,
        extra=f'''<div class="ab" style="left:40px;right:40px;top:760px;font:500 36px/1.4 B;color:#5b6b70;max-width:760px">Sin carrito ni formularios. Nos escribes, te asesoramos y te lo llevamos.</div>
<div class="ab" style="left:40px;top:960px;display:flex;gap:18px">{wa_pill(T_MARCA,"Escríbenos")}</div>
<div class="ab" style="right:40px;top:860px;width:520px;display:grid;gap:16px">
<div style="justify-self:end;background:#d9f2d0;border-radius:22px 22px 4px 22px;padding:20px 24px;font:500 28px/1.3 B;color:{GR};box-shadow:0 8px 18px rgba(0,0,0,.08)">Hola, ¿el gato le sirve a mi carro?</div>
<div style="justify-self:start;background:#fff;border-radius:22px 22px 22px 4px;padding:20px 24px;font:500 28px/1.3 B;color:{GR};box-shadow:0 8px 18px rgba(0,0,0,.08)">Dime el modelo y te confirmo 👍</div></div>''')
put('lun-3-cc-2-pasos', f'''{head(T_MARCA,2,4,badge(T_MARCA))}
<div class="ab ax" style="left:40px;right:40px;top:130px;font-size:96px;color:{AC}">Tres pasos.<br><span style="color:{CH}">Y listo.</span></div>
<div class="ab" style="left:40px;right:40px;top:420px;display:grid;gap:20px">
{''.join(f'<div style="background:#fff;border-radius:10px;padding:30px 34px;display:grid;grid-template-columns:96px 70px 1fr;gap:22px;align-items:center;box-shadow:0 12px 26px rgba(0,0,0,.08)"><div class="num" style="color:{CH};font-size:110px">{j}</div>{I(ic,AC)}<div><div class="bc" style="font-size:46px;color:{AC}">{t}</div><div style="font:500 28px/1.35 B;color:#5b6b70;margin-top:8px">{d}</div></div></div>' for j,ic,t,d in [(1,'chat','Escríbenos','Por WhatsApp o mensaje directo. Dinos qué necesitas o qué carro tienes.'),(2,'check','Te confirmamos','Precio, disponibilidad y cuál te sirve. Si no es lo que buscas, te lo decimos.'),(3,'camion','Te lo llevamos','Coordinamos la entrega en Valencia o pasas por el local.')])}
</div>{foot_next(T_MARCA)}''',T_MARCA)
put('lun-3-cc-3-pagos-entregas-PLANTILLA', f'''{head(T_MARCA,3,4,badge(T_MARCA))}
<div class="ab ax" style="left:40px;right:40px;top:130px;font-size:96px;color:{AC}">Pagos, entregas<br><span style="color:{CH}">y garantía</span></div>
<div class="ab" style="left:40px;right:40px;top:420px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
{''.join(f'<div style="background:#fff;border-radius:10px;padding:30px;display:grid;gap:14px;box-shadow:0 12px 26px rgba(0,0,0,.08)">{I(ic,CH)}<div class="bc" style="font-size:46px;color:{AC}">{t}</div><div style="font:500 26px/1.35 B;color:#5b6b70">{d}</div><span class="tag" style="background:{VO};justify-self:start"><span class="lab" style="color:{GR};font-size:20px">Por confirmar</span></span></div>' for ic,t,d in [('pago','Formas de pago','[Efectivo en dólares · Pago móvil · Zelle · …]'),('camion','Entregas','[Zonas de Valencia y costo]'),('escudo','Garantía','[Tiempo y qué cubre]'),('pin','El local','[Dirección o zona · Horario]')])}
</div>{foot_next(T_MARCA)}''',T_MARCA)
cta('lun-3-cc-4-cta',T_MARCA,'Ya sabes cómo comprar.','¿Qué te<br><em>falta?</em>','Escríbenos y te decimos cuál te sirve. El enlace a WhatsApp está en el perfil.',
    [('compre',(560,830,460,420)),('adapt',(800,960,240,300))],4,4,size=170)

# Martes: carrusel del gato (Taller)
portada('mar-1-portada',T_TALLER,'¿El gato que vino con tu carro…','¿te<br>sirve?','gato',(150,640,880,579),5,size=210,maxh=420,
        extra=f'<div class="ab" style="left:-100px;top:1000px;width:1400px;height:500px;background:{CH};transform:rotate(-6deg)"></div>')
comparar('mar-2-tijera-vs-patin',T_TALLER,'Los dos levantan. No trabajan igual.',
         dict(tag='Tijera',title='El que viene con el carro',lines=['Se sube dando vueltas a una manivela.','Base pequeña: se ladea en piso irregular.','Para una emergencia en la calle.'],k='gato'),
         dict(tag='Patín',title='Hidráulico, con ruedas',lines=['Se sube bombeando la palanca.','Base ancha y ruedas: entra y queda firme.','Para cambiar cauchos y trabajar en casa.'],k='gato'),
         'Para meterte debajo del carro, cualquiera de los dos necesita burros.',2,5)
put('mar-3-este-gato', f'''<div class="ab ax" style="left:-10px;top:1270px;transform-origin:0 0;transform:rotate(-90deg);font-size:330px;color:{CH};white-space:nowrap">Gato</div>
<div class="ab" style="right:40px;top:44px;background:{AC};color:#fff;padding:10px 16px;font:700 26px/1 BC;letter-spacing:.08em;text-transform:uppercase;border:3px solid {CH}">El que tenemos · 3 / 5</div>
<div class="ab bc" style="left:300px;top:120px;font-size:84px;color:{AC}">Así trabaja<br><span style="color:{CH}">por dentro</span></div>
{prod('gato',250,420,780,513)}
<svg class="ab" style="inset:0" width="1080" height="1350"><g stroke="{AC}" stroke-width="3" fill="none"><path d="M932 462V372"/><path d="M362 742V650"/><path d="M340 872V990"/><path d="M776 802V990"/></g></svg>
<div class="dot" style="left:922px;top:452px"></div><div class="co" style="left:800px;top:290px;width:240px;text-align:right;color:{AC}">Palanca<small>Bombeas y sube</small></div>
<div class="dot" style="left:352px;top:732px"></div><div class="co" style="left:262px;top:566px;width:260px;color:{AC}">Asiento<small>Va en el punto de apoyo</small></div>
<div class="dot" style="left:330px;top:862px"></div><div class="co" style="left:262px;top:1000px;width:260px;color:{AC}">Ruedas<small>Entra rodando bajo el carro</small></div>
<div class="dot" style="left:766px;top:792px"></div><div class="co" style="left:700px;top:1000px;width:300px;color:{AC}">Base ancha<small>No se ladea como la tijera</small></div>
<div class="ab" style="left:300px;right:40px;top:1120px;border-left:6px solid {CH};padding-left:22px;font:500 30px/1.35 B;color:{GR}">Capacidad 2 t · Altura 12,5–30 cm · Estuche incluido. Si tu carro es muy bajo, pregúntanos antes.</div>
<div class="ab" style="left:300px;bottom:40px;display:flex;gap:20px;align-items:center">{iso(T_TALLER,52)}<span class="lab" style="color:{AC}">Desliza →</span></div>''',T_TALLER)
lista('mar-4-seguridad',T_TALLER,'El gato levanta.','Los burros sostienen.',['Piso firme y plano. Nunca en tierra ni en bajada.','Freno de mano puesto y calza en la rueda contraria.','Levanta solo en el punto de apoyo que indica el manual.','Si te vas a meter debajo, pon burros. Nunca solo con el gato.'],4,5)
cta('mar-5-cta',T_TALLER,'Antes de comprar, dinos:','¿Qué<br>carro<br><em>tienes?</em>','Te decimos si este gato le sirve a tu carro.',[('gato',(470,860,580,382))],5,5,size=178)

# Miércoles: portada y cierre del reel con anuncio (1080x1920)
put('mie-1-portada-reel-anuncio', f'''
<div class="ab" style="left:40px;right:40px;top:300px">{badge(T_TALLER)}</div>
<div class="ab ax fit" data-maxh="520" style="left:40px;right:40px;top:400px;font-size:150px;color:{AC}">¿Todavía<br>con el gato<br><span style="color:{CH}">de tijera?</span></div>
<div class="ab" style="left:-120px;top:1150px;width:1400px;height:900px;background:{CH};transform:rotate(-7deg)"></div>
{prod('gato',60,930,960,632)}
<div class="ab" style="left:40px;top:1560px"><div class="tag" style="background:{GR}"><span class="aw" style="font-size:52px;color:#fff">Gato hidráulico 2 toneladas</span></div></div>''',T_TALLER,1080,1920)
put('mie-2-cierre-reel-anuncio', f'''
<div class="ab" style="inset:0;background:{AC}"></div>
<div class="ab" style="left:0;right:0;top:300px;display:flex;justify-content:center"><img src="{LG}logo-horizontal-negativo.svg" style="height:96px"></div>
{prod('gato',60,470,960,632)}
<div class="ab ax fit" data-maxh="240" style="left:40px;right:40px;top:1140px;font-size:110px;color:#fff;text-align:center">Gato hidráulico<br><span style="color:{CH}">2 toneladas</span></div>
<div class="ab" style="left:0;right:0;top:1420px;display:flex;justify-content:center">{wa_pill(T_TALLER)}</div>
<div class="ab" style="left:0;right:0;top:1530px;text-align:center;font:600 30px/1.4 B;color:#d5e2e4">@piezaclave.valencia · Entregas en Valencia</div>''',T_TALLER,1080,1920)

# Jueves: dados 108 + llaves (Taller)
put('jue-1-portada', f'''<div class="ab" style="inset:0;background:{AC}"></div>
<div class="ab ax" style="left:-30px;top:120px;font-size:560px;color:transparent;-webkit-text-stroke:4px #2c5560;letter-spacing:-10px">108</div>
<div class="ab" style="left:-100px;top:930px;width:1400px;height:440px;background:{CH};transform:rotate(-8deg)"></div>
{prod('dados',250,190,600,822,rot=-6)}
<div class="ab" style="left:40px;top:50px;display:flex;justify-content:space-between;right:40px">{badge(T_TALLER)}<span class="lab" style="color:#a9c3c7">1 / 4</span></div>
<div class="ab" style="left:40px;top:1060px;transform:rotate(-8deg);transform-origin:0 0"><div class="ax" style="font-size:118px;color:{GR}">108 piezas</div>
<div class="tag" style="background:{GR};margin-top:14px"><span class="aw" style="font-size:40px;color:#fff">¿Qué trae? Te lo explicamos →</span></div></div>''',T_TALLER)
put('jue-2-encastres', f'''{head(T_TALLER,2,4)}
<div class="ab ax" style="left:40px;right:40px;top:130px;font-size:96px;color:{AC}">Dos tamaños<br><span style="color:{CH}">de encastre</span></div>
<div class="ab" style="left:40px;right:40px;top:430px;display:grid;gap:22px">
{''.join(f'<div style="background:#fff;border-radius:10px;padding:34px;display:grid;grid-template-columns:300px 1fr;gap:26px;align-items:center;box-shadow:0 12px 26px rgba(0,0,0,.08)"><div class="ax" style="font-size:118px;color:{c}">{s}</div><div><div class="bc" style="font-size:50px;color:{AC}">{t}</div><div style="font:500 28px/1.35 B;color:#5b6b70;margin-top:8px">{d}</div></div></div>' for s,c,t,d in [('1/4"',AC,'Dados pequeños','Tornillos chicos: tablero, interior, sensores y piezas livianas del motor.'),('1/2"',CH,'Dados grandes','Tornillos duros: ruedas, suspensión y tren delantero.')])}
<div style="background:{AC};border-radius:10px;padding:30px 34px;display:flex;gap:22px;align-items:center">{I('piezas',CH)}<div style="font:600 30px/1.35 B;color:#fff">Además trae dos matracas, extensiones, cardán, barra en T y puntas de destornillador.</div></div>
</div>{foot_next(T_TALLER)}''',T_TALLER)
ficha('jue-3-llaves',T_TALLER,'Llaves','combinadas','14 piezas','llaves',(60,450,960,560),
      [('piezas','14','Piezas'),('medida','8–24 mm','Medidas'),('estuche','Tela','Estuche')],
      'Boca abierta de un lado y estría del otro. Para donde no entra la matraca.',3,4,nsize=170)
cta('jue-4-cta',T_TALLER,'Dinos qué carro tienes y qué le vas a hacer.','¿Dados, llaves<br><em>o los dos?</em>','Te decimos cuál te sirve, sin venderte de más.',
    [('dados',(560,780,330,452)),('llaves',(640,1000,420,245))],4,4,size=120)

# Viernes: portada del reel del multiplicador (1080x1920)
put('vie-1-portada-reel-multiplicador', f'''
<div class="ab" style="left:40px;right:40px;top:300px">{badge(T_TALLER)}</div>
<div class="ab ax fit" data-maxh="470" style="left:40px;right:40px;top:400px;font-size:132px;color:{AC}">El tornillo<br>de rueda que<br><span style="color:{CH}">nadie afloja</span></div>
<div class="ab" style="left:-120px;top:1100px;width:1400px;height:900px;background:{AC};transform:rotate(-7deg)"></div>
{prod('multi',200,960,680,600)}
<div class="ab" style="left:40px;top:1560px"><div class="tag" style="background:{CH}"><span class="aw" style="font-size:52px;color:{GR}">Multiplicador de fuerza</span></div></div>''',T_TALLER,1080,1920)

# Sábado: exterior
portada('sab-1-portada',T_EXT,'Para el patio y la parcela','¿Grama, monte<br><span style="color:'+EX+'">o ramas?</span>',None,(0,0,0,0),5,size=130,maxh=330,
        extra=prod('corta',30,700,400,500)+prod('desma',330,860,700,420,rot=-8)+prod('moto',600,640,440,260,rot=-12))
ficha('sab-2-cortadora',T_EXT,'Cortadora','de césped a gasolina','Corta y recoge','corta',(260,330,560,700),
      [('gas','Gasolina','Motor'),('hoja','Con bolsa','Recolección'),('check','Planos','Patios y jardines')],
      'Para grama pareja en patios y jardines planos. Corta y recoge en la bolsa.',2,5,nsize=130)
ficha('sab-3-desmalezadora',T_EXT,'Desmalezadora','a gasolina','Monte alto','desma',(40,420,1000,560),
      [('gas','Gasolina','Motor'),('llave','Cuchilla','Y nylon'),('escudo','Arnés','Incluido')],
      'Para monte alto, orillas y terreno irregular, donde la cortadora no entra.',3,5,nsize=112,rot=-6)
ficha('sab-4-motosierra',T_EXT,'Motosierra','a gasolina','Ramas y troncos','moto',(80,430,920,545),
      [('gas','Gasolina','Motor'),('escudo','Guantes','Incluidos'),('estuche','Protector','De espada')],
      'Úsala con lentes y botas. Para ramas gruesas y troncos.',4,5,nsize=124,rot=-10)
cta('sab-5-cta',T_EXT,'Mándanos una foto del patio o la parcela.','Cuéntanos<br>tu terreno.<br><em>Te decimos cuál.</em>','Por WhatsApp te recomendamos la que va con ese trabajo.',
    [('corta',(600,820,300,375)),('moto',(640,1020,400,236))],5,5,size=112)

# Domingo: historias
put('dom-1-historia-taller-pro', f'''
<div class="ab" style="left:40px;right:40px;top:300px">{badge(T_PRO)}</div>
<div class="ab ax fit" data-maxh="420" style="left:40px;right:40px;top:400px;font-size:120px;color:#fff">La próxima<br>semana:<br><span style="color:{CH}">el taller pro</span></div>
<div class="ab" style="left:40px;right:40px;top:860px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
{''.join(f'<div style="background:#1f292d;border:2px solid #33444a;border-radius:10px;height:360px;position:relative;overflow:hidden"><img src="{src(k)}" style="position:absolute;left:24px;right:24px;top:20px;width:calc(100% - 48px);height:270px;object-fit:contain"><span class="lab" style="position:absolute;left:20px;bottom:18px;color:#fff">{t}</span></div>' for k,t in [('compre','Compresímetro'),('mano','Manómetros A/C'),('engra','Engrasadora'),('adapt','Adaptadores')])}
</div>''',T_PRO,1080,1920)
put('dom-2-historia-encuesta', f'''
<div class="ab" style="left:40px;right:40px;top:300px">{badge(T_MARCA)}</div>
<div class="ab ax fit" data-maxh="430" style="left:40px;right:40px;top:400px;font-size:130px;color:{AC}">¿Qué quieres<br>que te<br><span style="color:{CH}">expliquemos?</span></div>
<div class="ab" style="left:40px;right:40px;top:860px;font:500 40px/1.35 B;color:#5b6b70">Vota aquí abajo. La más votada sale en el próximo reel.</div>
<div class="ab" style="left:40px;right:40px;top:1060px;height:300px;border:4px dashed {LI};border-radius:16px;display:grid;place-items:center;font:600 28px/1 B;color:#9aa8ab;letter-spacing:.1em;text-transform:uppercase">Espacio para el sticker de encuesta</div>
{prod('gato',60,1420,420,276)}{prod('taladro',760,1380,260,330)}''',T_MARCA,1080,1920)

# ================= SEMANA 2 =================
portada('tp-1-portada',T_PRO,'Cinco herramientas que no trae un juego de casa','Para el<br>mecánico<br><span style="color:'+CH+'">de oficio</span>','compre',(400,640,580,640),7,size=140,maxh=420)
ficha('tp-2-compresimetro',T_PRO,'Compre&shy;símetro','de motor','Diagnóstico','compre',(290,400,520,598),
      [('gauge','Por cilindro','Mide compresión'),('llave','Adaptadores','De bujía'),('estuche','Estuche','Incluido')],
      'Si un cilindro marca mucho menos que los otros, ahí está la falla: anillos, válvulas o empacadura.',2,7,nsize=118)
ficha('tp-3-manometros-ac',T_PRO,'Manómetros','de refrigeración','Aire acondicionado','mano',(300,400,480,600),
      [('gauge','Alta y baja','Presión'),('enchufe','Acoples','Rápidos'),('check','Mangueras','Incluidas')],
      'Para cargar gas y diagnosticar el aire acondicionado midiendo presión de alta y de baja.',3,7,nsize=118)
ficha('tp-4-engrasadora',T_PRO,'Engrasadora','manual','400 cc','engra',(80,440,920,520),
      [('gas','400 cc','Capacidad'),('check','Flexible','Manguera'),('medida','Rígido','Tubo')],
      'Para engrasar rótulas, crucetas y terminales por su grasera.',4,7,nsize=124,rot=-6)
ficha('tp-5-adaptadores',T_PRO,'Adaptadores','de impacto','8 piezas','adapt',(300,410,480,580),
      [('piezas','8','Piezas'),('medida','1/4"–1"','Encastres'),('escudo','Acero','De impacto')],
      'Para usar dados de un encastre en una pistola o matraca de otro.',5,7,nsize=124)
ficha('tp-6-polipasto',T_PRO,'Polipasto','eléctrico','Sube y baja','poli',(300,380,480,610),
      [('rayo','Eléctrico','Motor'),('boton','Botonera','De control'),('peso','Ver placa','Capacidad')],
      'Motores en el taller o cargas en la obra. Revisa la capacidad en la placa antes de usarlo.',6,7,nsize=124)
cta('tp-7-cta',T_PRO,'Escríbenos la lista de lo que necesitas.','¿Tienes taller?<br><em>Arma tu pedido.</em>','Te pasamos todo en un solo presupuesto.',
    [('compre',(560,780,330,380)),('mano',(800,900,240,300))],7,7,size=112)

portada('el-1-portada',T_ELE,'Herramientas eléctricas','¿Con batería<br><span style="color:#fff">o con cable?</span>',None,(0,0,0,0),4,size=130,maxh=330,
        extra=prod('taladro',60,720,440,550)+prod('esmeril',420,800,620,413))
ficha('el-2-taladro-inalambrico',T_ELE,'Taladro','inalámbrico','Con maletín','taladro',(320,380,440,550),
      [('bateria','Batería','Recargable'),('estuche','Maletín','Incluido'),('piezas','Brocas','Y puntas')],
      'Para la casa y para donde no llega un enchufe.',2,4,nsize=150)
ficha('el-3-esmeril-taladro',T_ELE,'Esmeril','y taladro con cable','Trabajo continuo','esmeril',(60,420,960,600),
      [('enchufe','Con cable','Potencia continua'),('llave','Corta y pule','Esmeril'),('check','Manuales','Y llave')],
      'El esmeril corta y pule; el taladro con cable aguanta trabajo continuo.',3,4,nsize=150)
cta('el-4-cta',T_ELE,'Huecos en pared, cortes de metal o trabajo fuera de casa.','Dinos qué<br>vas a hacer.<br><em>Te decimos cuál.</em>','Cada trabajo pide una herramienta distinta.',
    [('taladro',(640,800,300,375)),('esmeril',(560,1000,480,320))],4,4,size=112)

FIT='''<script>
function fit(){document.querySelectorAll('.fit').forEach(el=>{let fs=parseFloat(getComputedStyle(el).fontSize);const mh=parseFloat(el.dataset.maxh||'1e9');
el.style.overflowWrap='normal';let n=0;while((el.scrollWidth>el.clientWidth+1||el.scrollHeight>mh)&&fs>24&&n<200){fs-=2;n++;el.style.fontSize=fs+'px'}});document.body.dataset.fit='1'}
document.fonts.ready.then(fit);</script>'''
V={k:v for k,v in V.items() if v}
json.dump([{'name':n,'w':w,'h':h,'html':'<style>'+CSS+'</style><div class="s" style="width:%dpx;height:%dpx">'%(w,h)+html+'</div>'+FIT} for n,(w,h,html) in V.items()],open(SP+'/posts5.json','w'))
print(len(V))
