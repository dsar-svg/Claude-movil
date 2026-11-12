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
# ---- productos del grupo de proveedores (nov 2026), foto real recortada ----
PRICE.update({'compre':20,'taladro':40})
PK.update({'compre':'compre2-real','taladro':'taladro2-real'})
NEW=[
 ('tijera','taller','Gato de tijera','2 toneladas',[('peso','2 t','Capacidad'),('llave','Manivela','Incluida'),('check','Compacto','Para la maleta')],['Para llevar siempre en el carro','Repuesto del gato de fábrica','Sube girando la manivela'],25,'gato-tijera-2t'),
 ('botella','taller','Gato de botella','20 toneladas',[('peso','20 t','Capacidad'),('llave','Palanca','Incluida'),('altura','Hidráulico','Tipo botella')],['Camiones, camionetas y maquinaria','Prensas y trabajos de taller','Base firme de acero'],40,'gato-botella-20t'),
 ('dados32','taller','Caja de dados','32 piezas',[('piezas','32','Piezas'),('llave','Matraca','Incluida'),('estuche','Maletín','Incluido')],['Lo básico para el carro','Dados, matraca, extensiones y cardán','Todo ordenado en su maletín'],30,'caja-dados-32'),
 ('dados46','taller','Juego de dados 1/4"','46 piezas',[('piezas','46','Piezas'),('medida','1/4"','Encastre'),('estuche','Maletín','Incluido')],['Tornillos chicos: tablero, sensores, motos','Trae matraca, puntas y extensiones','Cabe en cualquier gaveta'],10,'juego-dados-46'),
 ('torx','taller','Dados Torx','tipo estrella (E)',[('piezas','Juego','Varias medidas'),('medida','E-Torx','Estrella'),('estuche','Estuche','Incluido')],['Tornillos de estrella de motor y caja','Comunes en carros modernos','Ordenados por medida'],15,'dados-torx'),
 ('ratchet','taller','Set de 3 matracas','1/4", 3/8" y 1/2"',[('piezas','3','Matracas'),('medida','1/4"–1/2"','Encastres'),('check','Mango','Con goma')],['Una matraca por cada encastre','Para tus dados de 1/4, 3/8 y 1/2','Cómodas para trabajar horas'],22,'set-3-matracas'),
 ('extfiltro','taller','Extractor de filtro','de aceite · 3 patas',[('llave','3 patas','Ajustable'),('medida','Varios','Tamaños'),('check','Matraca','O llave')],['Saca el filtro de aceite sin dañarlo','Se ajusta a varios tamaños','Úsalo con matraca o llave'],10,'extractor-filtro-aceite'),
 ('bomba','taller','Bomba de gasolina','universal 2068',[('gas','Eléctrica','Va en el tanque'),('check','Universal','Ref. 2068'),('llave','Repuesto','Directo')],['Repuesto de la bomba del tanque','Pregúntanos si es la de tu carro','Probada antes de entregar'],10,'bomba-gasolina-2068'),
 ('prensa5','taller','Prensa de banco','5 pulgadas',[('medida','5"','Mordaza'),('check','Giratoria','Base'),('llave','Yunque','Atrás')],['Sujeta piezas para cortar, limar o soldar','Se atornilla al banco','Gira para trabajar cómodo'],45,'prensa-banco-5'),
 ('prensa6','taller','Prensa de banco','6 pulgadas',[('medida','6"','Mordaza'),('check','Giratoria','Base'),('llave','Yunque','Atrás')],['Para piezas más grandes y pesadas','Se atornilla al banco','Gira para trabajar cómodo'],55,'prensa-banco-6'),
 ('helicoil','pro','Kit repara rosca','helicoides',[('piezas','Varias','Medidas'),('llave','Machos','E insertador'),('estuche','Caja','Metálica')],['Recupera roscas barridas','Bujías, cárter, culata y bloque','Sin cambiar la pieza'],40,'kit-repara-rosca'),
 ('gasol','pro','Medidor de presión','de gasolina · kit completo',[('gauge','Manómetro','Grande'),('piezas','Adaptadores','Varios'),('estuche','Maletín','Incluido')],['Diagnostica bomba y regulador','Para carros de inyección','Adaptadores para varias conexiones'],30,'medidor-presion-gasolina'),
 ('reno1','pro','Kit de tiempo Renault','sincronizador · modelo 1',[('check','Renault','Motores'),('piezas','Placas','Y pasadores'),('estuche','Maletín','Incluido')],['Para cambiar la correa de tiempo','Fija levas y cigüeñal en su punto','Pregúntanos si es para tu motor'],30,'kit-tiempo-renault-1'),
 ('reno2','pro','Kit de tiempo Renault','sincronizador · modelo 2',[('check','Renault','Motores'),('piezas','Reglas','Y pasadores'),('estuche','Maletín','Incluido')],['Para cambiar la correa de tiempo','Fija levas y cigüeñal en su punto','Pregúntanos si es para tu motor'],30,'kit-tiempo-renault-2'),
 ('espiral','pro','Recoge espirales','reforzado · con pines',[('escudo','Reforzado','Con pines'),('piezas','2','Prensas'),('estuche','Maletín','Incluido')],['Comprime el espiral para sacar el amortiguador','Pines de seguridad','Para la suspensión del carro'],30,'recoge-espirales'),
 ('damper','pro','Extractor de damper','3 patas',[('llave','3 patas','Ajustable'),('piezas','Pernos','Varios'),('estuche','Maletín','Incluido')],['Saca la polea del cigüeñal (damper)','También poleas y engranajes','Pernos para varias medidas'],30,'extractor-damper'),
 ('careta','pro','Careta de soldar','electrónica',[('escudo','Automática','Oscurece sola'),('check','Ajustable','A la cabeza'),('rayo','Soldadura','Eléctrica')],['Se oscurece sola al soldar','Manos libres: no tienes que bajarla','Para herrería y taller'],25,'careta-soldar'),
 ('pist300a','ele','Pistola de impacto','inalámbrica · 300 Nm',[('rayo','300 Nm','Torque'),('bateria','Batería','Y cargador'),('llave','Dado','22 mm incluido')],['Para tornillos de rueda y chasis','Sin compresor ni manguera','Trae batería, cargador y dado'],50,'pistola-impacto-300nm-amarilla'),
 ('pist300b','ele','Pistola de impacto','inalámbrica · 300 Nm',[('rayo','300 Nm','Torque'),('bateria','Batería','Y cargador'),('llave','Dado','22 mm incluido')],['Para tornillos de rueda y chasis','Sin compresor ni manguera','Trae batería, cargador y dado'],55,'pistola-impacto-300nm-verde'),
 ('pist2000','ele','Pistola de impacto 3/4"','inalámbrica · 2000 Nm',[('rayo','2000 Nm','Torque'),('bateria','2 baterías','Y cargador'),('llave','Dado','32 mm incluido')],['Camiones, gandolas y maquinaria','Afloja lo que la llave no puede','Trae 2 baterías, cargador y dado'],155,'pistola-impacto-2000nm'),
 ('cargador','ele','Cargador de batería','12 V · 6 A',[('bateria','12 V','Moto y carro'),('rayo','6 A','De carga'),('check','Gel','Y plomo-ácido')],['Carga baterías de moto y carro','También baterías de gel','Con pantalla y pinzas'],20,'cargador-bateria-12v'),
 ('ups','ele','Mini UPS','para internet · 6 a 8 h',[('bateria','6–8 h','De respaldo'),('enchufe','Router','Y módem'),('rayo','Automático','Al irse la luz')],['Tu internet sigue cuando se va la luz','Para router y módem','Lo conectas y listo'],45,'mini-ups'),
 ('caracol','ext','Caracol de motobomba','2 pulgadas',[('medida','2"','Entrada y salida'),('llave','Repuesto','Para motobomba'),('check','Con tapones','Llenado y drenaje')],['Repuesto para motobomba de 2"','Cambia el caracol roto o rajado','Pregúntanos si es para la tuya'],35,'caracol-motobomba-2'),
]
for k,cat,name,sub,specs,uses,pr,slug in NEW:
    P.append((k,cat,name,sub,specs,uses)); PRICE[k]=pr; SLUG[k]=slug; PK[k]=k+'-real'
for i,x in enumerate(P):
    if x[0]=='taladro': P[i]=('taladro','ele','Taladro inalámbrico','2 baterías · 21 V',[('bateria','2 baterías','21 V'),('estuche','Maletín','Incluido'),('piezas','Brocas','Y puntas')],['Para la casa y el trabajo','Donde no llega un enchufe','Viene completo en su maletín'])
    if x[0]=='compre': P[i]=('compre','pro','Compresímetro','de motor · 9 piezas',[('gauge','Por cilindro','Mide compresión'),('piezas','9','Piezas'),('estuche','Estuche','Incluido')],['Encuentra el cilindro que falla','Anillos, válvulas o empacadura','Para mecánicos y talleres'])
ONLY=__import__('os').environ.get('ONLY')
if ONLY: P=[x for x in P if x[0] in ONLY.split(',')]

OUT=[]
def pricetag(k): return f'<div style="text-align:right"><div style="font:700 22px/1 BC;color:#5b6b70;letter-spacing:.12em;text-transform:uppercase;margin-bottom:6px">Entregas en Valencia</div><span class="tag" style="background:{CH}"><span class="ax" style="font-size:92px;color:#fff;letter-spacing:-2px">{PRICE[k]}$</span></span></div>'
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
{pricetag(k) if k in PRICE else f'<span style="display:inline-flex;gap:10px;align-items:center;background:{AC};color:#fff;border-radius:999px;padding:12px 22px;font:700 26px/1 BC;letter-spacing:.05em;text-transform:uppercase">{I("camion","#fff").replace(chr(99)+"lass="+chr(34)+"ico"+chr(34),"style="+chr(34)+"width:34px;height:34px"+chr(34))}Entregas en Valencia</span>'}</div>
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
{f'<div style="display:flex;align-items:baseline;gap:18px"><span style="font:700 30px/1 BC;color:#c9d6d9;text-transform:uppercase;letter-spacing:.08em">Precio</span><span class="ax" style="font-size:78px;color:{CH};letter-spacing:-2px">{PRICE[k]}$</span></div>' if k in PRICE else '<div style="font:700 34px/1.1 BC;color:#fff;text-transform:uppercase;letter-spacing:.03em">Pregunta precio<br><span style="color:'+CH+'">y disponibilidad</span></div>'}{wa_pill(T_TALLER,'Escríbenos')}</div>''')
    # 3) cómo comprar
    steps=''.join(f'<div style="display:grid;grid-template-columns:70px 1fr;gap:20px;align-items:center;padding:22px 0;border-top:2px solid #2c5560">{I(ic,CH)}<div><div class="bc" style="font-size:44px;color:#fff">{t}</div><div style="font:500 26px/1.3 B;color:#c9d6d9;margin-top:4px">{d}</div></div></div>' for ic,t,d in [('chat','Escríbenos','Por Instagram o Messenger. Lun a sáb, 8 a. m. a 5 p. m.'),('check','Te confirmamos','Precio, disponibilidad y si te sirve.'),('camion','Te lo llevamos','Delivery según la zona o retiras en Calle 181, Naguanagua.')])
    page(f'{slug}-3-como-comprar',f'''<div class="ab" style="inset:0;background:{AC}"></div>
<div class="ab" style="right:-330px;top:-80px;width:620px;height:1300px;background:#173f47;transform:skewX(-16deg)"></div>
<div class="ab" style="right:220px;top:-80px;width:26px;height:1300px;background:{CH};transform:skewX(-16deg)"></div>
<div class="ab" style="left:40px;top:44px"><img src="{LG}logo-horizontal-negativo.svg" style="height:58px"></div>
<div class="ab ax fit" data-maxh="230" style="left:40px;width:640px;top:150px;font-size:96px;color:#fff">Comprar es<br><span style="color:{CH}">escribir</span></div>
<div class="ab" style="left:40px;width:600px;top:400px">{steps}</div>
{prod(k,640,330,400,420)}
<div class="ab" style="left:40px;right:40px;bottom:44px;display:flex;justify-content:space-between;align-items:center">{wa_pill(T_TALLER)}<span style="font:600 26px/1.3 B;color:#d5e2e4;text-align:right">@piezaclave.valencia</span></div>''')
json.dump(OUT,open(SP+'/market.json','w')); print(len(OUT))
