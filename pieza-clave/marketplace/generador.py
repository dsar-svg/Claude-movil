# Generador de imágenes para Marketplace (copia de trabajo; rutas al scratchpad de la sesión).
import json
# Imágenes para Facebook Marketplace: 3 cuadradas por producto (principal, ficha, cómo comprar)
SP='/tmp/claude-0/-home-user-Claude-movil/59907f33-5efd-5727-b54e-ecaa26a4f53b/scratchpad'
base=open(SP+'/posts5.py').read().split('# ================= SEMANA 1')[0]
exec(base)
FIT=open(SP+'/posts5.py').read().split("FIT='''")[1].split("'''")[0]
TH={'taller':T_TALLER,'pro':T_PRO,'ext':T_EXT,'ele':T_ELE}
P=[
 ('gato','taller','Gato hidráulico','2 toneladas',[('peso','2 t','Capacidad'),('altura','12,5–30 cm','Altura de trabajo'),('estuche','Estuche','Incluido')],['Para cambiar cauchos en casa','Sube bombeando la palanca','Base ancha con ruedas: queda firme']),
 ('dados','taller','Juego de dados','108 piezas',[('piezas','108','Piezas'),('medida','1/4" y 1/2"','Encastres'),('estuche','Maletín','Incluido')],['Dados chicos: tablero, sensores, motor','Dados grandes: ruedas y suspensión','Trae matracas, extensiones, cardán y puntas']),
 ('llaves','taller','Llaves combinadas','14 piezas',[('piezas','14','Piezas'),('medida','8–24 mm','Medidas'),('estuche','Tela','Estuche enrollable')],['Boca abierta de un lado, estría del otro','Para donde no entra la matraca','Ordenadas por medida en su estuche']),
 ('multi','taller','Multiplicador de fuerza','para tornillos de rueda',[('llave','Más fuerza','Con menos esfuerzo'),('piezas','Dados','Incluidos'),('estuche','Maletín','Incluido')],['Para tornillos de rueda muy apretados','Cuando la llave de cruz no puede','Viene completo en su maletín']),
 ('compre','pro','Compresímetro','de motor',[('gauge','Por cilindro','Mide compresión'),('llave','Adaptadores','De bujía'),('estuche','Estuche','Incluido')],['Encuentra el cilindro que falla','Anillos, válvulas o empacadura','Para mecánicos y talleres']),
 ('mano','pro','Manómetros','de refrigeración',[('gauge','Alta y baja','Presión'),('enchufe','Acoples','Rápidos'),('check','Mangueras','Incluidas')],['Para cargar gas del aire acondicionado','Diagnóstico de alta y de baja','Aire acondicionado y refrigeración']),
 ('engra','pro','Engrasadora manual','400 cc',[('gas','400 cc','Capacidad'),('check','Manguera','Flexible'),('medida','Tubo','Rígido')],['Para rótulas, crucetas y terminales','Engrasa por la grasera','Manguera para llegar a lo difícil']),
 ('adapt','pro','Adaptadores de impacto','8 piezas',[('piezas','8','Piezas'),('medida','1/4"–1"','Encastres'),('escudo','Acero','De impacto')],['Usa tus dados en otra pistola o matraca','Acero negro para impacto','En su estuche']),
 ('poli','pro','Polipasto eléctrico','con botonera',[('rayo','Eléctrico','Motor'),('boton','Botonera','De control'),('peso','Ver placa','Capacidad')],['Sube y baja peso con un botón','Motores en el taller, cargas en la obra','Revisa la capacidad en la placa']),
 ('corta','ext','Cortadora de césped','a gasolina',[('gas','Gasolina','Motor'),('hoja','Con bolsa','Recolección'),('check','Planos','Patios y jardines')],['Grama pareja en patios y jardines','Corta y recoge en la bolsa','Para terreno plano']),
 ('desma','ext','Desmalezadora','a gasolina',[('gas','Gasolina','Motor'),('llave','Cuchilla','Y nylon'),('escudo','Arnés','Incluido')],['Monte alto, orillas y terreno irregular','Donde la cortadora no entra','Trae cuchilla, nylon y arnés']),
 ('moto','ext','Motosierra','a gasolina',[('gas','Gasolina','Motor'),('escudo','Guantes','Incluidos'),('estuche','Protector','De espada')],['Ramas gruesas y troncos','Úsala con lentes y botas','Trae guantes y protector de espada']),
 ('taladro','ele','Taladro inalámbrico','con maletín',[('bateria','Batería','Recargable'),('estuche','Maletín','Incluido'),('piezas','Brocas','Y puntas')],['Para la casa y el trabajo','Donde no llega un enchufe','Viene completo en su maletín']),
 ('esmeril','ele','Esmeril y taladro','con cable',[('enchufe','Con cable','Trabajo continuo'),('llave','Corta y pule','Esmeril'),('check','Manuales','Y llave')],['El esmeril corta y pule metal','El taladro aguanta trabajo continuo','Los dos con sus manuales']),
]
SLUG={'gato':'gato-hidraulico-2t','dados':'juego-dados-108','llaves':'llaves-combinadas-14','multi':'multiplicador-fuerza','compre':'compresimetro','mano':'manometros-refrigeracion','engra':'engrasadora-400cc','adapt':'adaptadores-impacto','poli':'polipasto-electrico','corta':'cortadora-cesped','desma':'desmalezadora','moto':'motosierra','taladro':'taladro-inalambrico','esmeril':'esmeril-y-taladro'}
OUT=[]
def page(n,html,w=1080,h=1080): OUT.append({'name':n,'w':w,'h':h,'html':'<style>'+CSS+'</style><div class="s" style="width:%dpx;height:%dpx">'%(w,h)+html+'</div>'+FIT})
def chipc(T): return {'taller':CH,'pro':'#151b1e','ext':EX,'ele':VO}[T['k']]
for k,cat,name,sub,specs,uses in P:
    T=TH[cat]; slug=SLUG[k]; cc=chipc(T)
    # 1) principal
    page(f'{slug}-1-principal',f'''<div class="ab" style="inset:0;background:radial-gradient(circle at 50% 46%,#ffffff 0,#ffffff 38%,#e9eded 100%)"></div>
<div class="ab" style="left:40px;top:40px">{logo(T_MARCA,54)}</div><div class="ab" style="right:40px;top:40px">{badge(T)}</div>
{prod(k,90,150,900,740)}
<div class="ab" style="left:40px;right:40px;top:930px;display:flex;justify-content:space-between;align-items:flex-end">
<div><div class="bc fit" style="font-size:56px;color:{AC};white-space:nowrap;max-width:640px">{name}</div><div class="bc" style="font-size:36px;color:{CH};margin-top:4px">{sub}</div></div>
<span style="display:inline-flex;gap:10px;align-items:center;background:{AC};color:#fff;border-radius:999px;padding:12px 22px;font:700 26px/1 BC;letter-spacing:.05em;text-transform:uppercase">{I("camion","#fff").replace('class="ico"','style="width:34px;height:34px"')}Entregas en Valencia</span></div>
<div class="ab" style="left:0;right:0;bottom:0;height:14px;background:{cc}"></div>''')
    # 2) ficha
    sp=''.join(f'<div style="display:flex;gap:18px;align-items:center;padding:20px 0;border-top:2px solid {LI}">{I(ic,CH)}<div><div style="font:800 46px/1 BC;color:{AC};text-transform:uppercase">{v}</div><div style="font:600 22px/1.2 B;color:#5b6b70;letter-spacing:.06em;text-transform:uppercase;margin-top:4px">{kk}</div></div></div>' for ic,v,kk in specs)
    us=''.join(f'<div style="display:flex;gap:12px;font:500 27px/1.3 B;color:{GR}"><span style="color:{CH};font:800 30px/1.1 BC">›</span>{u}</div>' for u in uses)
    page(f'{slug}-2-ficha',f'''<div class="ab" style="inset:0;background:#f4f6f6"></div>
<svg class="ab" style="inset:0" width="1080" height="1080"><defs><pattern id="g2" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M54 0H0V54" fill="none" stroke="#dfe5e6" stroke-width="1"/></pattern></defs><rect width="1080" height="1080" fill="url(#g2)"/></svg>
<div class="ab" style="left:40px;top:40px;display:flex;gap:18px;align-items:center">{badge(T)}</div>
<div class="ab" style="left:40px;right:40px;top:110px"><div class="ax fit" style="font-size:96px;color:{AC};white-space:nowrap">{name}</div><div class="aw" style="font-size:44px;color:{CH};margin-top:8px">{sub}</div></div>
<div class="ab" style="left:40px;width:420px;top:300px">{sp}</div>
{prod(k,470,290,580,480)}
<div class="ab" style="left:40px;right:40px;top:800px;display:grid;gap:10px">{us}</div>
<div class="ab" style="left:0;right:0;bottom:0;height:120px;background:{AC};display:flex;align-items:center;justify-content:space-between;padding:0 40px">
<div style="font:700 34px/1.1 BC;color:#fff;text-transform:uppercase;letter-spacing:.03em">Pregunta precio<br><span style="color:{CH}">y disponibilidad</span></div>{wa_pill(T_TALLER,'Escríbenos')}</div>''')
    # 3) cómo comprar
    steps=''.join(f'<div style="display:grid;grid-template-columns:70px 1fr;gap:20px;align-items:center;padding:22px 0;border-top:2px solid #2c5560">{I(ic,CH)}<div><div class="bc" style="font-size:44px;color:#fff">{t}</div><div style="font:500 26px/1.3 B;color:#c9d6d9;margin-top:4px">{d}</div></div></div>' for ic,t,d in [('chat','Escríbenos','Por WhatsApp o mensaje. Dinos qué carro o trabajo tienes.'),('check','Te confirmamos','Precio, disponibilidad y si te sirve.'),('camion','Te lo llevamos','Entregas en Valencia o pasas por el local.')])
    page(f'{slug}-3-como-comprar',f'''<div class="ab" style="inset:0;background:{AC}"></div>
<div class="ab" style="right:-330px;top:-80px;width:620px;height:1300px;background:#173f47;transform:skewX(-16deg)"></div>
<div class="ab" style="right:220px;top:-80px;width:26px;height:1300px;background:{CH};transform:skewX(-16deg)"></div>
<div class="ab" style="left:40px;top:44px"><img src="{LG}logo-horizontal-negativo.svg" style="height:58px"></div>
<div class="ab ax fit" data-maxh="230" style="left:40px;width:640px;top:150px;font-size:96px;color:#fff">Comprar es<br><span style="color:{CH}">escribir</span></div>
<div class="ab" style="left:40px;width:600px;top:400px">{steps}</div>
{prod(k,640,330,400,420)}
<div class="ab" style="left:40px;right:40px;bottom:44px;display:flex;justify-content:space-between;align-items:center">{wa_pill(T_TALLER)}<span style="font:600 26px/1.3 B;color:#d5e2e4;text-align:right">@piezaclave.valencia</span></div>''')
json.dump(OUT,open(SP+'/market.json','w')); print(len(OUT))
