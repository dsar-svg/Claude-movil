"""Editor de reels de producto Pieza Clave: python3 editor.py r1 [PREVIEW=t1,t2]
Tomas de Higgsfield + voz de José Manuel + subtítulos por palabra + cierre con precio."""
import sys, os, json, math, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
R = os.path.dirname(os.path.abspath(__file__)); os.chdir(R)
SP = '/tmp/claude-0/-home-user-Claude-movil/59907f33-5efd-5727-b54e-ecaa26a4f53b/scratchpad'
REPO = '/home/user/Claude-movil/pieza-clave/'
KEY = sys.argv[1]
W, H, FPS = 1080, 1920, 30
FD = SP + '/fonts/'
F = lambda n, s: ImageFont.truetype(FD + n, s)
BC8 = lambda s: F('Barlow_Condensed_wght_800.ttf', s); BC7 = lambda s: F('Barlow_Condensed_wght_700.ttf', s)
B6 = lambda s: F('Barlow_wght_600.ttf', s); AX = lambda s: F('Archivo_wdth_wght_125_900.ttf', s)
ACERO = (18, 52, 59); CHISPA = (242, 106, 27); BLANCO = (255, 255, 255); GRAF = (22, 27, 29); VERDE = (47, 125, 74); LINEA = (203, 211, 213)
U = lambda s: s.upper()

# ---------------- configuración de cada reel ----------------
C = {
 'r1': dict(cuts=[('Con', 1), ('Se', 2), ('pieza', 1)], clips=[('r1t1', 0.2), ('r1t2', 0.0), ('r1t3', 0.0)],
           hook=['¿Se fue la luz?', '¿Y el internet?'], title=['Mini UPS', '6 a 8 horas'], chip='Eléctricas',
           badge=('6-8', 'HORAS'), pill='Sigues conectado', name=['Mini UPS', 'para internet'], price=45, prod='ups', music='music_a'),
 'r2': dict(cuts=[('con', 1), ('trae', 1), ('pieza', 1)], clips=[('r2t1', 0.0), ('r2t2', 0.0), ('r2t3', 0.0)],
           hook=['¿Esa tuerca', 'no sale?'], title=['Pistola de impacto', '3/4" · 2000 Nm'], chip='Eléctricas',
           badge=('2000', 'NM'), pill='2 baterías + cargador', name=['Pistola de impacto', '3/4" · 2000 Nm'], price=155, prod='pist2000', music='music'),
 'r3': dict(cuts=[('Este', 1), ('Y', 1), ('Pieza', 1)], clips=[('r3t1', 0.0), ('r3t2', 0.0), ('r3t3', 0.0)],
           hook=['¿Camioneta', 'o camión?'], title=['Gato de botella', '20 toneladas'], chip='Taller',
           badge=('20 t', 'TONELADAS'), pill='Siempre con burros', name=['Gato de botella', '20 toneladas'], price=40, prod='botella', music='music_b'),
 'r4': dict(cuts=[('con', 1), ('sirve', 1), ('pieza', 1)], clips=[('r4t1', 0.0), ('r4t2', 0.0), ('r4t3', 0.0)],
           hook=['¿Amaneció', 'sin batería?'], title=['Cargador de batería', '12 V · 6 A'], chip='Eléctricas',
           badge=('12 V', '6 AMPERIOS'), pill='Moto · carro · gel', name=['Cargador de batería', '12 V · 6 A'], price=20, prod='cargador', music='music_a'),
 'r5': dict(cuts=[('esta', 1), ('ves', 1), ('Piesa', 1)], clips=[('r5t1', 0.0), ('r5t2', 0.0), ('r5t3', 0.0)],
           hook=['¿Todavía con', 'careta de vidrio?'], title=['Careta de soldar', 'electrónica'], chip='Taller pro',
           badge=('AUTO', 'OSCURECE SOLA'), pill='Manos libres', name=['Careta de soldar', 'electrónica'], price=25, prod='careta', music='music'),
 'r6': dict(cuts=[('dados', 2), ('lo', 1), ('Piesa', 1)], clips=[('r6t1', 1.2), ('r6t2', 0.0), ('r6t3', 0.0)],
           hook=['¿Qué trae', 'una caja de 32?'], title=['Caja de dados', '32 piezas'], chip='Taller',
           badge=('32', 'PIEZAS'), pill='Todo en su maletín', name=['Caja de dados', '32 piezas'], price=30, prod='dados32', music='music_b'),
 'r7': dict(cuts=[('con', 1), ('para', 1), ('Piesa', 1)], clips=[('r7t1', 0.0), ('r7t2', 0.0), ('r7t3', 0.0)],
           hook=['¿Se te barrió', 'la rosca?'], title=['Kit repara rosca', 'helicoides'], chip='Taller pro',
           badge=('NUEVA', 'ROSCA'), pill='Bujías · cárter · culata', name=['Kit repara rosca', 'helicoides'], price=40, prod='helicoil', music='music'),
}[KEY]
FIX = {'piesa': 'pieza', 'bugillas': 'bujías', 'brincándola': 'brincándole', 'n': 'Nm', 'ups': 'UPS', 'que': '¿qué'}
words = json.load(open('words.json'))[KEY]

def wt(key, n=1, edge='start'):
    c = 0
    for w, s, e in words:
        if w.strip('¿?.,:').lower() == key.lower():
            c += 1
            if c == n: return s if edge == 'start' else e
    raise KeyError(key)
T1 = wt(*C['cuts'][0]) - 0.08; T2 = wt(*C['cuts'][1]) - 0.08; T_END = wt(*C['cuts'][2]) - 0.06
DUR = words[-1][2] + 1.1
ease_out = lambda t: 1 - (1 - t) ** 3
def back(t, s=1.7): t -= 1; return t * t * ((s + 1) * t + s) + 1
clamp = lambda x: max(0.0, min(1.0, x))

# ---------------- tomas ----------------
def load(path, start, dur):
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS) or 24; fr = []
    while True:
        ok, f = cap.read()
        if not ok: break
        fr.append(f)
    avail = len(fr) / fps - start - 0.04
    sp = min(1.0, avail / dur)          # si la toma es corta, cámara lenta suave
    out = []
    for i in range(int(round(dur * FPS))):
        idx = min(len(fr) - 1, int((start + i / FPS * sp) * fps))
        im = cv2.resize(fr[idx], (W, H), interpolation=cv2.INTER_CUBIC)
        out.append(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    return out, sp
bounds = [0, T1, T2, T_END]
shots = []
for i, (clip, ss) in enumerate(C['clips']):
    fr, sp = load(f'clips/{clip}.mp4', ss, bounds[i + 1] - bounds[i]); shots.append((bounds[i], bounds[i + 1], fr))
    if sp < 0.999: print(f'toma {i+1}: velocidad {sp:.2f}')

def zoomed(img, s):
    M = np.float32([[s, 0, (1 - s) * W / 2], [0, s, (1 - s) * H / 2]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
def grade(a):
    a = a.astype(np.float32); a = (a - 128) * 1.06 + 128; a[..., 0] *= 1.02; a[..., 2] *= 0.98
    b = cv2.GaussianBlur(a, (0, 0), 1.2); a = a + (a - b) * 0.6     # nitidez tras escalar de 720p
    return np.clip(a, 0, 255).astype(np.uint8)

# ---------------- gráficos ----------------
def rrect(w, h, r, fill):
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, h - 1], r, fill=fill); return im
def text_block(lines, size=104, pad=(40, 30), chip=None):
    f = BC8(size); lh = int(size * 0.95)
    widths = [sum(f.getlength(t) for t, _ in ln) for ln in lines]
    cw = ch = 0
    if chip: fc = B6(26); cw = int(fc.getlength(chip)) + 32; ch = 46
    w = int(max(max(widths), cw)) + pad[0] * 2; h = lh * len(lines) + pad[1] * 2 + (ch + 16 if chip else 0)
    im = rrect(w, h, 10, ACERO + (255,)); d = ImageDraw.Draw(im); y = pad[1]
    if chip:
        d.rounded_rectangle([pad[0], y, pad[0] + cw, y + ch], 3, fill=CHISPA); d.text((pad[0] + 16, y + 9), chip, font=fc, fill=GRAF); y += ch + 16
    for ln in lines:
        x = pad[0]
        for t, c in ln: d.text((x, y - int(size * 0.08)), t, font=f, fill=c); x += f.getlength(t)
        y += lh
    return im
def fit_size(lines, size, maxw=1000):
    while size > 50 and max(BC8(size).getlength(U(l)) for l in lines) + 80 > maxw: size -= 4
    return size
hs = fit_size(C['hook'], 112); BLK_HOOK = text_block([[(U(C['hook'][0]), BLANCO)], [(U(C['hook'][1]), CHISPA)]], hs)
ts = fit_size(C['title'], 100, 900); BLK_T = text_block([[(U(C['title'][0]), BLANCO)], [(U(C['title'][1]), CHISPA)]], ts, chip=U(C['chip']))
logo = Image.open(SP + '/reel/ov/logo-horizontal-negativo.png').convert('RGBA'); logo = logo.crop(logo.getbbox())
iso = Image.open(SP + '/reel/ov/isotipo-negativo.png').convert('RGBA'); iso = iso.crop(iso.getbbox()); iso_s = iso.resize((int(iso.width * 64 / iso.height), 64))
def badge(t1, t2):
    s = 300; im = Image.new('RGBA', (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, s - 1, s - 1], fill=CHISPA + (255,)); d.ellipse([14, 14, s - 15, s - 15], outline=GRAF + (255,), width=5)
    fs = 150
    while BC8(fs).getlength(t1) > 230: fs -= 6
    f2s = 44
    while BC7(f2s).getlength(t2) > 220: f2s -= 2
    d.text((s / 2, s / 2 - 22), t1, font=BC8(fs), fill=GRAF, anchor='mm'); d.text((s / 2, s / 2 + 70), t2, font=BC7(f2s), fill=GRAF, anchor='mm')
    return im
BADGE = badge(*C['badge'])
def check_pill(txt):
    f = BC8(66); w = int(f.getlength(txt)) + 150; h = 110; im = rrect(w, h, 55, VERDE + (255,)); d = ImageDraw.Draw(im)
    d.ellipse([18, 18, 92, 92], fill=BLANCO); d.line([36, 56, 50, 72], fill=VERDE, width=10); d.line([50, 72, 76, 40], fill=VERDE, width=10)
    d.text((112, h / 2), txt, font=f, fill=BLANCO, anchor='lm'); return im
PILL = check_pill(U(C['pill']))
def msg_button():
    f = BC8(72); txt = U('Escríbenos por mensaje'); w = int(f.getlength(txt)) + 170; h = 124
    im = rrect(w, h, 62, CHISPA + (255,)); d = ImageDraw.Draw(im)
    d.ellipse([22, 18, 110, 106], fill=GRAF); d.polygon([(34, 92), (28, 114), (54, 100)], fill=GRAF)
    for x in [46, 66, 86]: d.ellipse([x - 6, 56, x + 6, 68], fill=CHISPA)
    d.text((128, h / 2), txt, font=f, fill=GRAF, anchor='lm'); return im
MSG = msg_button()
def ptag(p):
    w, h = 520, 230; im = Image.new('RGBA', (w + 80, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(40, 0), (w + 80, 0), (w + 40, h), (0, h)], fill=CHISPA + (255,))
    d.text(((w + 80) / 2, 62), 'PRECIO', font=BC8(34), fill=GRAF, anchor='mm')
    d.text(((w + 80) / 2, 150), f'{p}$', font=AX(150 if p < 100 else 128), fill=BLANCO, anchor='mm')
    return im
PTAG = ptag(C['price'])

# fondo del cierre: acero con franjas y el producto recortado
def end_bg():
    bg = Image.new('RGBA', (W, H), ACERO + (255,)); d = ImageDraw.Draw(bg)
    d.polygon([(860, 0), (1080, 0), (1080, H), (700, H)], fill=(23, 63, 71, 255))
    d.polygon([(1010, 0), (1046, 0), (926, H), (890, H)], fill=CHISPA + (255,))
    d.rectangle([W // 2 - 70, 540, W // 2 + 70, 548], fill=CHISPA + (255,))
    for y in range(0, H, 54): d.line([(0, y), (W, y)], fill=(28, 66, 74, 255), width=1)
    p = Image.open(REPO + 'productos-estudio/' + C['prod'] + '.png').convert('RGBA')
    p.thumbnail((880, 600)); sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    cx, cy = W // 2, 900
    ds.ellipse([cx - p.width * 0.42, cy + p.height / 2 - 30, cx + p.width * 0.42, cy + p.height / 2 + 30], fill=(0, 0, 0, 120))
    sh = sh.filter(__import__('PIL.ImageFilter', fromlist=['x']).GaussianBlur(22)); bg.alpha_composite(sh)
    bg.alpha_composite(p, (int(cx - p.width / 2), int(cy - p.height / 2)))
    return bg, p.height
ENDBG, PH = end_bg()

def paste(base, im, x, y, scale=1.0, alpha=1.0, rot=0.0):
    if alpha <= 0 or scale <= 0.01: return
    if scale != 1.0 or rot:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
        if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alpha < 1: a = im.getchannel('A').point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    base.alpha_composite(im, (int(x - im.width / 2), int(y - im.height / 2)))

# subtítulos por palabra (desde la toma 2 hasta el cierre)
def disp(w):
    k = w.strip(',.:?¿').lower(); t = FIX.get(k, w.strip(',.:'))
    return U(t)
cap = [(disp(w), w, s, e) for w, s, e in words if T1 - 0.05 <= s < T_END - 0.05]
groups = []; cur = []
for x in cap:
    cur.append(x)
    if len(cur) >= 3 or x[1][-1] in ',.:?':
        groups.append(cur); cur = []
if cur: groups.append(cur)
CF = BC8(78)
def caption(base, t):
    for g in groups:
        if g[0][2] - 0.05 <= t <= g[-1][3] + 0.12:
            toks = [x[0].rstrip('?') for x in g]; widths = [CF.getlength(x) for x in toks]; gap = 22
            w = int(sum(widths) + gap * (len(toks) - 1)) + 60; h = 110; pill = rrect(w, h, 14, ACERO + (230,)); d = ImageDraw.Draw(pill); x = 30
            for (tok, _, s, e), wi in zip(g, widths):
                d.text((x, h / 2), tok.rstrip('?'), font=CF, fill=CHISPA if s - 0.03 <= t <= e + 0.08 else BLANCO, anchor='lm'); x += wi + gap
            k = clamp((t - (g[0][2] - 0.05)) / 0.12); paste(base, pill, W / 2, 1420 + (1 - ease_out(k)) * 30, 1.0, k)
            return

def frame(i):
    t = i / FPS
    if t < T_END:
        for a, b, fr in shots:
            if a <= t < b: img = fr[min(len(fr) - 1, int((t - a) * FPS))]; ts = t - a; dur = b - a; break
        s = 1.0 + 0.045 * (ts / dur)
        if a > 0 and ts < 0.2: s += 0.10 * (1 - ease_out(ts / 0.2))
        base = Image.fromarray(grade(zoomed(img, s))).convert('RGBA')
        if a > 0 and ts < 0.07: base = Image.blend(base, Image.new('RGBA', (W, H), (255, 255, 255, 255)), 0.45 * (1 - ts / 0.07))
    else:
        ts = t - T_END; base = ENDBG.copy()
    if t < T1:   # gancho
        k = ease_out(clamp((t - 0.05) / 0.3)); paste(base, BLK_HOOK, 40 + BLK_HOOK.width / 2 - (1 - k) * (BLK_HOOK.width + 60), 200 + BLK_HOOK.height / 2)
    if T1 <= t < T_END: paste(base, iso_s, W - 40 - iso_s.width / 2, 170, 1.0, clamp((t - T1) / 0.3) * 0.95)
    if T1 <= t < T2:   # título y dato
        sc = 0.82; k = back(clamp((t - T1 - 0.1) / 0.35))
        paste(base, BLK_T, W - 40 - BLK_T.width * sc / 2 + (1 - clamp(k)) * (BLK_T.width + 60), 260 + BLK_T.height * sc / 2, sc)
        tb = T1 + 0.9
        if t >= tb: k = clamp((t - tb) / 0.3); paste(base, BADGE, 220, 1130, back(k) * 0.9, clamp(k * 2), rot=-6)
    if T2 <= t < T_END:
        tp = T2 + 0.35
        if t >= tp: k = clamp((t - tp) / 0.28); paste(base, PILL, W / 2, 1200, back(k), clamp(k * 2))
    if t >= T_END:   # cierre
        ts = t - T_END
        k2 = back(clamp((ts - 0.05) / 0.4)); paste(base, logo, W / 2, 210, 0.75 * clamp(k2), clamp(k2 * 2))
        if ts > 0.2:
            k3 = ease_out(clamp((ts - 0.2) / 0.3)); fs = fit_size(C['name'], 92, 1000); f = BC8(fs)
            im = Image.new('RGBA', (1040, 220), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
            d.text((520, 55), U(C['name'][0]), font=f, fill=BLANCO, anchor='mm'); d.text((520, 155), U(C['name'][1]), font=f, fill=CHISPA, anchor='mm')
            paste(base, im, W / 2, 420 + (1 - k3) * 30, 1.0, k3)
        if ts > 0.5: k6 = back(clamp((ts - 0.5) / 0.35)); paste(base, PTAG, W / 2 + 220, 900 + PH / 2 - 10, k6 * 0.82, clamp(k6 * 2), rot=-4)
        tm = wt('escríbenos') - 0.1
        if t >= tm:
            k4 = clamp((t - tm) / 0.3); pulse = 1 + 0.035 * math.sin((t - tm) * 2 * math.pi * 1.6) * clamp((t - tm - 0.3) / 0.2)
            paste(base, MSG, W / 2, 1390, back(k4) * pulse, clamp(k4 * 2))
            k5 = ease_out(clamp((t - tm - 0.2) / 0.3)); im = Image.new('RGBA', (1000, 130), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
            d.text((500, 30), '@piezaclave.valencia', font=B6(46), fill=BLANCO, anchor='mm')
            d.text((500, 92), U('Lun a sáb 8 a. m. – 5 p. m. · Entregas en Valencia'), font=B6(28), fill=LINEA, anchor='mm')
            paste(base, im, W / 2, 1530 + (1 - k5) * 20, 1.0, k5)
    if T1 <= t < T_END: caption(base, t)
    return np.asarray(base.convert('RGB'))

if os.environ.get('PREVIEW'):
    for x in os.environ['PREVIEW'].split(','):
        Image.fromarray(frame(int(float(x) * FPS))).save(f'prev_{KEY}_{x}.jpg', quality=80)
    print('T1', T1, 'T2', T2, 'T_END', T_END, 'DUR', DUR); sys.exit()
os.makedirs('out', exist_ok=True); tmp = f'tmp_{KEY}.mp4'
p = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)): p.stdin.write(frame(i).tobytes())
p.stdin.close(); p.wait()
A = SP + '/reel/audio/'
ev = [('whoosh', T1 - 0.15, 5), ('whoosh', T2 - 0.15, 4), ('whoosh', T_END - 0.15, 5), ('pop', T1 + 0.9, 3), ('pop', T2 + 0.35, 3),
      ('pop', T_END + 0.5, 4), ('pop', wt('escríbenos') - 0.1, 4)]
inp = ['-i', tmp, '-i', f'vo/{KEY}.mp3', '-i', A + C['music'] + '.mp3']; fl = []; mix = ['[vo]', '[mus]']
for j, (nm, at, db) in enumerate(ev):
    inp += ['-i', A + nm + '.mp3']; ms = int(max(0, at) * 1000)
    fl.append(f'[{j+3}:a]adelay={ms}|{ms},volume={db}dB[e{j}]'); mix.append(f'[e{j}]')
fc = (f'[1:a]apad=whole_dur={DUR},volume=2.0,asplit=2[vo][vosc];'
      f'[2:a]atrim=0:{DUR},afade=t=out:st={DUR-0.9}:d=0.9,volume=0.9[m0];'
      f'[m0][vosc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[mus];' + ';'.join(fl) + ';'
      + ''.join(mix) + f'amix=inputs={len(mix)}:duration=longest:normalize=0,atrim=0:{DUR},alimiter=limit=0.95[a]')
subprocess.run(['ffmpeg', '-y', '-v', 'error', *inp, '-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
                '-movflags', '+faststart', f'out/reel-{KEY}.mp4'], check=True)
os.remove(tmp); print('ok', KEY, round(DUR, 2))
