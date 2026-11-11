# Reel del gato: compositor v2 (copia de trabajo). Espera clips/, ov/, audio/ y words.json junto a él; ver README.
"""Edición v2 del reel del gato: python3 edit2.py A|B salida.mp4
Compositor cuadro a cuadro (PIL + numpy) sincronizado con la voz."""
import sys, os, json, math, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R=os.path.dirname(os.path.abspath(__file__)); os.chdir(R)
V, OUT = sys.argv[1], sys.argv[2]
W,H,FPS=1080,1920,30
FD='/tmp/claude-0/-home-user-Claude-movil/59907f33-5efd-5727-b54e-ecaa26a4f53b/scratchpad/fonts/'
F=lambda n,s: ImageFont.truetype(FD+n,s)
BC8=lambda s:F('Barlow_Condensed_wght_800.ttf',s); BC7=lambda s:F('Barlow_Condensed_wght_700.ttf',s); B6=lambda s:F('Barlow_wght_600.ttf',s)
ACERO=(18,52,59); CHISPA=(242,106,27); BLANCO=(255,255,255); GRAF=(22,27,29); VERDE=(47,125,74)
words=json.load(open('words.json'))[V]
def wt(key, n=1, edge='start'):
    c=0
    for w,s,e in words:
        if w.strip('¿?.,:') == key:
            c+=1
            if c==n: return s if edge=='start' else e
    raise KeyError(key)
T_V2=wt('Con')-0.08; T_V3=wt('bombeas')-0.08; T_V4=wt('Trae')-0.06; T_END=wt('Pieza')-0.06
DUR=words[-1][2]+0.75
ease_out=lambda t:1-(1-t)**3
def back(t,s=1.7): t-=1; return t*t*((s+1)*t+s)+1
clamp=lambda x:max(0.0,min(1.0,x))

# ---------- clips ----------
def load(path, start, dur, speed=None):
    cap=cv2.VideoCapture(path); fps=cap.get(cv2.CAP_PROP_FPS) or 24; fr=[]
    while True:
        ok,f=cap.read()
        if not ok: break
        fr.append(cv2.cvtColor(f,cv2.COLOR_BGR2RGB))
    n=int(round(dur*FPS)); out=[]
    sp=speed if speed else 1.0
    if speed=='fit': sp=(len(fr)/fps-start-0.05)/dur
    for i in range(n):
        idx=min(len(fr)-1,int((start+i/FPS*sp)*fps)); out.append(cv2.resize(fr[idx],(W,H),interpolation=cv2.INTER_AREA))
    return out
SH=[('clips/v1.mp4',0.2,0,T_V2,None),('clips/v2.mp4',0.3,T_V2,T_V3,None),('clips/v3b.mp4',0.4,T_V3,T_V4,'fit'),('clips/v4.mp4',0.4,T_V4,T_END,None)]
shots=[(a,b,load(p,ss,b-a,sp)) for p,ss,a,b,sp in SH]
endbg=np.array(Image.open('/home/user/Claude-movil/pieza-clave/semana-1/escenas-ia/gato916b.jpg').convert('RGB').resize((W,H)))

def zoomed(img, s, dx=0, dy=0):
    M=np.float32([[s,0,(1-s)*W/2+dx],[0,s,(1-s)*H/2+dy]])
    return cv2.warpAffine(img,M,(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
def grade(a):
    a=a.astype(np.float32); a=(a-128)*1.05+128; a[...,0]*=1.02; a[...,2]*=0.98
    return np.clip(a,0,255).astype(np.uint8)

# ---------- graphic elements (RGBA PIL) ----------
def rrect(w,h,r,fill):
    im=Image.new('RGBA',(w,h),(0,0,0,0)); ImageDraw.Draw(im).rounded_rectangle([0,0,w-1,h-1],r,fill=fill); return im
def text_block(lines, size=104, pad=(40,30), maxw=900, chip=None):
    # lines: list of [(text,color),...] per line
    f=BC8(size); lh=int(size*0.95)
    widths=[sum(f.getlength(t) for t,_ in ln) for ln in lines]
    cw=0; ch=0
    if chip: fc=B6(26); cw=int(fc.getlength(chip))+32; ch=46
    w=int(max(max(widths),cw))+pad[0]*2; h=lh*len(lines)+pad[1]*2+(ch+16 if chip else 0)
    im=rrect(w,h,10,ACERO+(255,)); d=ImageDraw.Draw(im); y=pad[1]
    if chip:
        d.rounded_rectangle([pad[0],y,pad[0]+cw,y+ch],3,fill=CHISPA); d.text((pad[0]+16,y+9),chip,font=fc,fill=GRAF); y+=ch+16
    for ln in lines:
        x=pad[0]
        for t,c in ln: d.text((x,y-int(size*0.08)),t,font=f,fill=c); x+=f.getlength(t)
        y+=lh
    return im
U=lambda s:s.upper()
HOOK={'A':[[(U('¿Todavía con el gato '),BLANCO)],[(U('de tijera?'),CHISPA)]],'B':[[(U('¿Se te espichó '),BLANCO)],[(U('un caucho?'),CHISPA)]]}[V]
blk_hook=text_block(HOOK,112)
blk_t2=text_block([[(U('Gato hidráulico'),BLANCO)],[(U('2 toneladas'),CHISPA)]],100,chip='TALLER')
blk_t4=text_block([[(U('Trae estuche.'),BLANCO)],[(U('Cabe en la maleta.'),CHISPA)]],96)
logo=Image.open('ov/logo-horizontal-negativo.png').convert('RGBA'); logo=logo.crop(logo.getbbox())
iso=Image.open('ov/isotipo-negativo.png').convert('RGBA'); iso=iso.crop(iso.getbbox()); iso_s=iso.resize((int(iso.width*64/iso.height),64))

def stamp_x():
    s=420; im=Image.new('RGBA',(s,s),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([10,10,s-10,s-10],outline=CHISPA+(255,),width=26)
    d.line([110,110,s-110,s-110],fill=CHISPA+(255,),width=44); d.line([s-110,110,110,s-110],fill=CHISPA+(255,),width=44)
    return im
STAMP=stamp_x()
def badge(txt1,txt2):
    s=300; im=Image.new('RGBA',(s,s),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([0,0,s-1,s-1],fill=CHISPA+(255,)); d.ellipse([14,14,s-15,s-15],outline=GRAF+(255,),width=5)
    f1=BC8(150); f2=BC7(44)
    d.text((s/2,s/2-22),txt1,font=f1,fill=GRAF,anchor='mm'); d.text((s/2,s/2+70),txt2,font=f2,fill=GRAF,anchor='mm')
    return im
BADGE=badge('2 t','TONELADAS')
def check_pill(txt):
    f=BC8(70); w=int(f.getlength(txt))+150; h=110; im=rrect(w,h,55,VERDE+(255,)); d=ImageDraw.Draw(im)
    d.ellipse([18,18,92,92],fill=BLANCO); d.line([36,56,50,72],fill=VERDE,width=10); d.line([50,72,76,40],fill=VERDE,width=10)
    d.text((112,h/2),txt,font=f,fill=BLANCO,anchor='lm'); return im
CHECK=check_pill(U('Cabe en la maleta'))
def wa_button():
    f=BC8(72); txt=U('Escríbenos por WhatsApp'); w=int(f.getlength(txt))+170; h=124
    im=rrect(w,h,62,CHISPA+(255,)); d=ImageDraw.Draw(im)
    d.ellipse([22,18,110,106],fill=GRAF); d.polygon([(34,92),(28,114),(54,100)],fill=GRAF)
    for i,x in enumerate([46,66,86]): d.ellipse([x-6,56,x+6,68],fill=CHISPA)
    d.text((128,h/2),txt,font=f,fill=GRAF,anchor='lm'); return im
WA=wa_button()

def paste(base, im, x, y, scale=1.0, alpha=1.0, rot=0.0):
    if alpha<=0 or scale<=0.01: return
    if scale!=1.0 or rot: 
        im=im.resize((max(1,int(im.width*scale)),max(1,int(im.height*scale))),Image.BICUBIC)
        if rot: im=im.rotate(rot,resample=Image.BICUBIC,expand=True)
    if alpha<1: a=im.getchannel('A').point(lambda v:int(v*alpha)); im=im.copy(); im.putalpha(a)
    base.alpha_composite(im,(int(x-im.width/2),int(y-im.height/2)))

# captions: groups of words between T_V2 and T_END
cap_words=[(w.strip(),s,e) for w,s,e in words if T_V2<=s<T_END-0.05]
groups=[]; cur=[]
for w in cap_words:
    cur.append(w)
    if len(cur)>=3 or w[0][-1] in ',.:' or w[0].endswith('...'):
        groups.append(cur); cur=[]
if cur: groups.append(cur)
CF=BC8(78)
def caption(base,t):
    for g in groups:
        if g[0][1]-0.05<=t<=g[-1][2]+0.12:
            toks=[w.replace('...','').strip(',.:').upper() for w,_,_ in g]
            widths=[CF.getlength(x) for x in toks]; gap=22; tw=sum(widths)+gap*(len(toks)-1)
            w=int(tw)+60; h=110; pill=rrect(w,h,14,ACERO+(230,)); d=ImageDraw.Draw(pill); x=30
            for (wd,s,e),tok,wi in zip(g,toks,widths):
                col=CHISPA if s-0.03<=t<=e+0.08 else BLANCO
                d.text((x,h/2),tok,font=CF,fill=col,anchor='lm'); x+=wi+gap
            k=clamp((t-(g[0][1]-0.05))/0.12); paste(base,pill,W/2,1420+(1-ease_out(k))*30,1.0,k)
            return

def measure(base,t,t0,t1):
    # barra de altura: 12,5 -> 30 cm
    if t<t0-0.3: return
    a=clamp((t-(t0-0.3))/0.25); k=ease_out(clamp((t-t0)/(t1-t0+0.25)))
    x=930; ybot=1180; ytop0=1040; ytop1=760; ytop=ytop0+(ytop1-ytop0)*k
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    d.rounded_rectangle([x-70,ytop1-120,x+110,ybot+40],14,fill=ACERO+(int(215*a),))
    for i in range(0,11): yy=ybot-(ybot-ytop1)*i/10; d.line([x-40,yy,x-(10 if i%5 else 0),yy],fill=(203,211,213,int(255*a)),width=4)
    d.rectangle([x,ytop,x+44,ybot],fill=CHISPA+(int(255*a),))
    d.polygon([(x-14,ytop),(x+58,ytop),(x+22,ytop-30)],fill=CHISPA+(int(255*a),))
    val=12.5+(30-12.5)*k; txt=f'{val:.1f}'.replace('.',',') if val<29.95 else '30'
    d.text((x+20,ytop1-80),txt,font=BC8(74),fill=(255,255,255,int(255*a)),anchor='mm')
    d.text((x+20,ytop1-30),'CM',font=B6(28),fill=(203,211,213,int(255*a)),anchor='mm')
    base.alpha_composite(ov)

def frame(i):
    t=i/FPS
    if t<T_END:
        for a,b,fr in shots:
            if a<=t<b: idx=min(len(fr)-1,int((t-a)*FPS)); img=fr[idx]; ts=t-a; dur=b-a; break
        s=1.0+0.045*(ts/dur)
        if a>0 and ts<0.2: s+=0.10*(1-ease_out(ts/0.2))   # golpe de zoom al entrar
        img=grade(zoomed(img,s))
        base=Image.fromarray(img).convert('RGBA')
        if a>0 and ts<0.07 and a==T_V2: base=Image.blend(base,Image.new('RGBA',(W,H),(255,255,255,255)),0.6*(1-ts/0.07))
    else:
        ts=t-T_END; img=zoomed(endbg,1.0+0.04*ts/(DUR-T_END)); base=Image.fromarray(img).convert('RGBA')
    # hook
    if t<T_V2:
        k=ease_out(clamp((t-0.05)/0.3)); paste(base,blk_hook,40+blk_hook.width/2-(1-k)*(blk_hook.width+60),170+blk_hook.height/2,1.0,1.0)
        ts0=wt('tijera',edge='start')+0.1
        if t>=ts0:
            k=clamp((t-ts0)/0.16); sc=2.2-1.2*ease_out(k); paste(base,STAMP,640,1330,sc*0.85,min(1,k*1.5),rot=-10)
    # logo pequeño
    if T_V2<=t<T_END: paste(base,iso_s,W-40-iso_s.width/2,170,1.0,clamp((t-T_V2)/0.3)*0.95)
    # shot 2
    if T_V2<=t<T_V3:
        k=back(clamp((t-T_V2-0.1)/0.35)); paste(base,blk_t2,40+blk_t2.width/2-(1-clamp(k))*(blk_t2.width+60)+0,300+blk_t2.height/2)
        tb=wt('toneladas')-0.05
        if t>=tb: k=clamp((t-tb)/0.3); paste(base,BADGE,820,980,back(k)*1.0,clamp(k*2))
    # shot 3: medidor
    if T_V3<=t<T_V4: measure(base,t,wt('doce'),wt('treinta',edge='end'))
    # shot 4
    if T_V4<=t<T_END:
        k=back(clamp((t-T_V4-0.08)/0.35)); paste(base,blk_t4,40+blk_t4.width/2-(1-clamp(k))*(blk_t4.width+60),300+blk_t4.height/2)
        tc=wt('maleta')
        if t>=tc: k=clamp((t-tc)/0.28); paste(base,CHECK,W/2,1180,back(k),clamp(k*2))
    # cierre
    if t>=T_END:
        ts=t-T_END
        panel=rrect(1000,560,12,ACERO+(240,)); k=ease_out(clamp(ts/0.35)); paste(base,panel,W/2,520+(1-k)*80,1.0,k)
        k2=back(clamp((ts-0.15)/0.4)); paste(base,logo,W/2,380,0.82*clamp(k2),clamp(k2*2))
        f=BC8(96)
        if ts>0.35:
            k3=ease_out(clamp((ts-0.35)/0.3)); im=Image.new('RGBA',(1000,240),(0,0,0,0)); d=ImageDraw.Draw(im)
            d.text((500,60),U('Gato hidráulico'),font=f,fill=BLANCO,anchor='mm'); d.text((500,160),U('2 toneladas'),font=f,fill=CHISPA,anchor='mm')
            paste(base,im,W/2,600+(1-k3)*30,1.0,k3)
        tw=wt('WhatsApp')-0.1
        if t>=tw-0.25:
            kp=ease_out(clamp((t-(tw-0.25))/0.3)); paste(base,rrect(1000,330,12,ACERO+(240,)),W/2,1450+(1-kp)*60,1.0,kp)
        if t>=tw:
            k4=clamp((t-tw)/0.3); pulse=1+0.035*math.sin((t-tw)*2*math.pi*1.6)*clamp((t-tw-0.3)/0.2)
            paste(base,WA,W/2,1385,back(k4)*pulse,clamp(k4*2))
        tl=wt('llevamos')-0.05
        if t>=tl:
            k5=ease_out(clamp((t-tl)/0.3)); im=Image.new('RGBA',(1000,120),(0,0,0,0)); d=ImageDraw.Draw(im)
            d.text((500,30),'@piezaclave.valencia',font=B6(46),fill=BLANCO,anchor='mm'); d.text((500,88),U('Entregas en Valencia'),font=B6(32),fill=(203,211,213),anchor='mm')
            paste(base,im,W/2,1530+(1-k5)*20,1.0,k5)
    if T_V2<=t<T_END: caption(base,t)
    return np.asarray(base.convert('RGB'))

n=int(DUR*FPS)
p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
    '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','tmp_v2.mp4'],stdin=subprocess.PIPE)
for i in range(n): p.stdin.write(frame(i).tobytes())
p.stdin.close(); p.wait()

# ---------- audio ----------
ev=[('whoosh',T_V2-0.15,6),('whoosh',T_V3-0.15,4),('whoosh',T_V4-0.15,4),('whoosh',T_END-0.15,5),
    ('stamp',wt('tijera')+0.1,9),('pop',wt('toneladas')-0.05,3),('sfx',T_V3+0.1,12),('pop',wt('maleta'),3),('pop',wt('WhatsApp')-0.1,5)]
inp=['-i','tmp_v2.mp4','-i',f'audio/vo{V}.mp3','-i','audio/music.mp3']; fl=[]; mix=['[vo]','[mus]']
for j,(name,at,db) in enumerate(ev):
    inp+=['-i',f'audio/{name}.mp3']; ms=int(max(0,at)*1000)
    fl.append(f'[{j+3}:a]adelay={ms}|{ms},volume={db}dB[e{j}]'); mix.append(f'[e{j}]')
fc=(f'[1:a]apad=whole_dur={DUR},volume=1.6,asplit=2[vo][vosc];'
    f'[2:a]atrim=0:{DUR},afade=t=out:st={DUR-0.8}:d=0.8,volume=0.9[m0];'
    f'[m0][vosc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[mus];'+';'.join(fl)+';'
    +''.join(mix)+f'amix=inputs={len(mix)}:duration=longest:normalize=0,atrim=0:{DUR},alimiter=limit=0.95[a]')
subprocess.run(['ffmpeg','-y','-v','error',*inp,'-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT],check=True)
os.remove('tmp_v2.mp4'); print('ok',OUT,round(DUR,2))
