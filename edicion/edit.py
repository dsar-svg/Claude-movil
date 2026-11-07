"""Cinematic vertical edit: grade, transitions, text. Usage: edit.py OUT.mp4 [--stills]"""
import sys, json, subprocess, math, os
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
FONT = '/usr/share/fonts/opentype/inter/'
STILLS = '--stills' in sys.argv
rng = np.random.default_rng(7)

# segment: file, push-in zoom (start, end)
SEGS = [('s1', 1.00, 1.03), ('s2', 1.02, 1.00), ('s3', 1.00, 1.05), ('s4', 1.00, 1.03), ('s5', 1.00, 1.04)]

def read(name):
    cap = cv2.VideoCapture(f'{D}/seg/{name}.mp4')
    fr = []
    while True:
        ok, f = cap.read()
        if not ok: break
        fr.append(f)
    return fr

ease = lambda t: t * t * (3 - 2 * t)
ein = lambda t: t ** 3          # accelerate into a cut
eout = lambda t: 1 - (1 - t) ** 3  # decelerate out of a cut

def warp(img, s, dx=0.0, dy=0.0):
    M = np.float32([[s, 0, (1 - s) * W / 2 + dx], [0, s, (1 - s) * H / 2 + dy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

def zoom_blur(img, s, amt, n=10):
    acc = np.zeros_like(img, np.float32)
    for k in range(n):
        acc += warp(img, s * (1 + amt * k / (n - 1))).astype(np.float32)
    return acc / n

def whip(img, dx, blur):
    out = warp(img, 1.0, dx)
    L = int(blur) | 1
    if L > 1:
        out = cv2.filter2D(out, -1, np.full((1, L), 1.0 / L, np.float32))
    return out

# ---------- grade ----------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / math.sqrt(2)
GRAD = np.clip(0.90 + 0.10 * (yy / (H * 0.55)), 0, 1)[..., None]  # graduated ND: darker, moodier sky
VIG = GRAD * (1 - 0.22 * np.clip(r - 0.25, 0, 1) ** 1.6 / 0.75 ** 1.6)[..., None].astype(np.float32)
GRAIN = [cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 0.7) for _ in range(12)]

def tone(x):
    x = np.clip(x, 0, 1)
    s = x * x * (3 - 2 * x)
    x = x + 0.20 * (s - x)                                   # S-curve contrast
    k = 0.72
    hi = k + (1 - k) * np.tanh((x - k) / (1 - k)) * 0.80     # soft highlight shoulder (blown sky -> creamy)
    x = np.where(x > k, hi, x)
    return 0.02 + x * (0.97 - 0.02)                        # lifted blacks, rolled whites

LUT = tone(np.arange(256, dtype=np.float32) / 255)

def grade(bgr, warm=1.0):
    f = cv2.LUT(bgr, (LUT * 255).astype(np.uint8)).astype(np.float32) / 255  # BGR
    Y = (0.0722 * f[..., 0] + 0.7152 * f[..., 1] + 0.2126 * f[..., 2])[..., None]
    f = Y + (f - Y) * 0.92                                   # desaturate
    sh = (1 - Y) ** 2.2
    mid = 4 * Y * (1 - Y)
    hi = Y ** 3
    f += sh * np.float32([0.02, 0.008, -0.012])              # teal shadows (BGR)
    f += mid * np.float32([-0.015, 0.0, 0.018]) * warm        # warm mids / skin
    f += hi * np.float32([0.01, 0.004, -0.005])               # cool highlights
    f *= VIG
    return f

# ---------- text ----------
def text_layer(txt, font, size, tracking, alpha, cy, cx=None, align='c', color=(240, 236, 228)):
    ft = ImageFont.truetype(FONT + font, size)
    widths = [ft.getlength(ch) for ch in txt]
    total = sum(widths) + tracking * (len(txt) - 1)
    img = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(img)
    x = (W - total) / 2 if align == 'c' else (cx if align == 'l' else cx - total)
    for ch, w in zip(txt, widths):
        d.text((x, cy), ch, font=ft, fill=int(255 * alpha), anchor='lm')
        x += w + tracking
    a = np.asarray(img, np.float32)[..., None] / 255
    return a, np.float32(color[::-1]) / 255

def over(f, layer):
    a, c = layer
    return f * (1 - a) + c * a

BAR = 150
TY = H * 0.27
SHADE = np.exp(-(((yy - TY - 40) / 230) ** 2))[..., None].astype(np.float32)
def bars(f, t, T):
    f[:BAR] = 0; f[H - BAR:] = 0
    k = min(1, max(0, (t - 0.6) / 0.6)) * min(1, max(0, (T - 0.5 - t) / 0.5))
    if k > 0:
        f = over(f, text_layer('07.11.26', 'Inter-Regular.otf', 26, 6, 0.65 * k, H - BAR / 2, 60, 'l'))
        f = over(f, text_layer('13:03', 'Inter-Regular.otf', 26, 6, 0.65 * k, H - BAR / 2, W - 60, 'r'))
        f = over(f, text_layer('— DÍAS GRISES —', 'Inter-Light.otf', 22, 9, 0.5 * k, BAR / 2))
    return f

def title(f, t):
    t0, t1 = 0.45, 2.75
    if not (t0 < t < t1): return f
    u = (t - t0) / (t1 - t0)
    a = min(1, u / 0.25) * min(1, (1 - u) / 0.25)
    f = f * (1 - 0.38 * ease(a) * SHADE)                      # soft dark wash so light text reads over the sky
    f = over(f, text_layer('DÍAS GRISES', 'InterDisplay-ExtraLight.otf', 78, 18 + 22 * ease(u), 0.95 * ease(a), TY))
    return over(f, text_layer('un sábado cualquiera', 'Inter-LightItalic.otf', 32, 3, 0.8 * ease(a), TY + 80))

# ---------- assemble ----------
segs = [(n, z0, z1, read(n)) for n, z0, z1 in SEGS]
lens = [len(s[3]) for s in segs]
starts = np.cumsum([0] + lens[:-1])
T = sum(lens) / FPS
json.dump({'cuts': [int(s) / FPS for s in starts[1:]], 'T': T}, open(f'{D}/cuts.json', 'w'))
print('frames', lens, 'T', T)

def frame(si, i):
    n, z0, z1, fr = segs[si]
    N = len(fr)
    u = i / max(1, N - 1)
    img = fr[i]
    s = z0 + (z1 - z0) * ease(u)
    e_ = N - 1 - i
    # transitions (by boundary): 0 s1->s2 punch, 1 s2->s3 light zoom blur, 2 s3->s4 big zoom blur, 3 s4->s5 whip
    flash = 0.0
    if si == 2 and e_ < 5:
        k = ein(1 - e_ / 5); img = zoom_blur(img, s * (1 + 0.20 * k), 0.10 * k, 6)
    elif si == 3 and i < 6:
        k = 1 - eout(i / 6); img = zoom_blur(img, s * (1 + 0.20 * k), 0.10 * k, 6)
    else:
        img = warp(img, s)
    if img.dtype != np.uint8:
        img = np.clip(img, 0, 255).astype(np.uint8)
    f = grade(img, warm=1.2 if si < 3 else 0.9)
    if flash: f = f + (1 - f) * flash
    t = (starts[si] + i) / FPS
    fade = min(1, t / 0.3) * min(1, max(0, (T - t) / 0.6))
    return np.clip(f * ease(fade) * 255, 0, 255).astype(np.uint8)

out = sys.argv[1]
if STILLS:
    picks = [(0, 30), (1, 20), (2, 40), (2, 72), (3, 2), (3, 60), (4, 40)]
    ims = [cv2.resize(frame(a, b), (270, 480), interpolation=cv2.INTER_AREA) for a, b in picks]
    cv2.imwrite(out, np.hstack(ims)); sys.exit()

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-preset', 'slow', '-crf', '9', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
for si in range(len(segs)):
    for i in range(lens[si]):
        enc.stdin.write(frame(si, i).tobytes())
    print('seg', si, 'done', flush=True)
enc.stdin.close(); enc.wait()
