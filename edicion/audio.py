"""Sound design: ambient pad + booms/riser/whooshes/pulse over the clips' own ambience. Writes audio.wav (stereo 48k)."""
import json, subprocess, os, sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

D = os.path.dirname(os.path.abspath(__file__))
SR = 48000
U = sys.argv[1]
A, B = f'{U}/bc491b1d-VID_20261107_130350606.mp4', f'{U}/19ce2278-VID_20261107_1304297302.mp4'
cj = json.load(open(f'{D}/cuts.json'))
cuts, T = cj['cuts'], cj['T']
N = int(T * SR) + 1
t = np.arange(N) / SR
rng = np.random.default_rng(3)
bounds = [0] + cuts + [T]

def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
def rms(x): return np.sqrt(np.mean(x ** 2) + 1e-12)
def at(x, sec, sig):
    i = int(sec * SR); n = min(len(sig), N - i)
    if n > 0: x[i:i + n] += sig[:n]

# ---- ambience from the original clips (real time, short crossfades) ----
def grab(src, ss, d):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(ss), '-t', str(d + 0.05), '-i', src, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)
amb = np.zeros(N)
plan = [(A, 0.6, False), (A, 6.2, False), (A, 4.0, True), (B, 3.0, True), (B, 0.0, False)]
for (src, ss, dreamy), a, b in zip(plan, bounds[:-1], bounds[1:]):
    x = hp(grab(src, ss, b - a), 90)
    if dreamy: x = lp(x, 1100, 4)                       # muffled under the slow-motion parts
    x = x / rms(x) * 0.035
    f = int(0.03 * SR); env = np.ones(len(x)); env[:f] = np.linspace(0, 1, f); env[-f:] = np.linspace(1, 0, f)
    at(amb, a, x * env)

# ---- pad: Am | Fmaj7 | C | G, band-limited detuned saws ----
def saw(f, dur):
    tt = np.arange(int(dur * SR)) / SR
    y = np.zeros_like(tt)
    for det in (-0.004, 0, 0.0045):
        ph = rng.uniform(0, 2 * np.pi)
        for n in range(1, 16):
            y += np.sin(2 * np.pi * n * f * (1 + det) * tt + ph * n) / n
    return y
chords = [(0.0, [110, 130.81, 164.81, 220]), (3.4, [87.31, 110, 130.81, 164.81]),
          (cuts[2], [65.41, 130.81, 164.81, 196]), (10.2, [98, 123.47, 146.83, 196])]
pad = np.zeros(N)
for k, (st, notes) in enumerate(chords):
    en = chords[k + 1][0] if k + 1 < len(chords) else T + 1.5
    dur = en - st + 0.8
    y = sum(saw(f, dur) for f in notes)
    e = np.minimum(1, np.arange(len(y)) / (0.7 * SR)) * np.clip((len(y) - np.arange(len(y))) / (0.8 * SR), 0, 1)
    at(pad, st, y * e)
dark, bright = lp(pad, 700, 4), lp(pad, 1900, 4)
mix = np.clip((t - cuts[2] + 0.2) / 0.6, 0, 1)        # filter opens at the main transition
pad = (dark * (1 - mix) + bright * mix)
pad = pad / rms(pad) * 0.05
sub = np.sin(2 * np.pi * 55 * t) * 0.06 * np.clip((t - cuts[2]) / 0.3, 0, 1)
sub[t >= 10.2] = 0; sub += np.sin(2 * np.pi * 49 * t) * 0.06 * (t >= 10.2)

# ---- hits ----
def boom(dur=2.0, f0=58, f1=30, tau=0.8):
    tt = np.arange(int(dur * SR)) / SR
    f = f1 + (f0 - f1) * np.exp(-tt / 0.25)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / tau)
    y += lp(rng.normal(0, 1, len(tt)), 180) * np.exp(-tt / 0.15) * 0.6
    return y
def kick():
    tt = np.arange(int(0.45 * SR)) / SR
    f = 45 + 110 * np.exp(-tt / 0.03)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.16) + hp(rng.normal(0, 1, len(tt)), 3000) * np.exp(-tt / 0.004) * 0.3
def sweep_noise(dur, f0, f1, rise, fall):
    n = int(dur * SR); x = rng.normal(0, 1, n); y = np.zeros(n); blk = 512
    for i in range(0, n, blk):                          # time-varying band-pass, block-wise
        u = i / n; fc = f0 * (f1 / f0) ** u
        y[i:i + blk] = bp(x[max(0, i - 4096):i + blk], fc * 0.6, min(fc * 1.6, SR / 2 - 100))[-len(y[i:i + blk]):]
    tt = np.arange(n) / SR
    env = np.where(tt < rise, (tt / rise) ** 2, np.exp(-(tt - rise) / fall))
    return y * env
fx = np.zeros(N)
at(fx, 0.35, boom() * 0.55)
at(fx, cuts[0], kick() * 0.35)                          # punch cut
w = sweep_noise(0.5, 3000, 600, 0.3, 0.08); at(fx, cuts[1] - 0.3, w / rms(w) * 0.03)
r = sweep_noise(1.6, 250, 7000, 1.55, 0.03); at(fx, cuts[2] - 1.55, r / rms(r) * 0.04)   # riser into the big transition
at(fx, cuts[2], boom(2.6, 62, 28, 1.1) * 0.8)
w = sweep_noise(0.6, 2500, 400, 0.32, 0.1); at(fx, cuts[3] - 0.32, w / rms(w) * 0.05)    # whip
beat = 60 / 80
for k in range(1, 12):
    s = cuts[2] + k * beat
    if s < T - 1.0: at(fx, s, kick() * (0.22 if abs(s - cuts[3]) > 0.2 else 0.4))

# ---- reverb send + stereo ----
def ir(seed):
    g = np.random.default_rng(seed); tt = np.arange(int(2.4 * SR)) / SR
    return lp(g.normal(0, 1, len(tt)), 5000) * np.exp(-tt / 0.7) * 0.012
send = pad + fx * 0.6
L = pad * 0.8 + fx + sub + amb + fftconvolve(send, ir(1))[:N]
R = pad * 0.8 + fx + sub + amb + fftconvolve(send, ir(2))[:N]
out = np.stack([L, R], 1)
out *= np.minimum(1, t / 0.3)[:, None] * np.clip((T - t) / 1.4, 0, 1)[:, None]
out = out / np.max(np.abs(out)) * 0.89
wavfile.write(f'{D}/audio.wav', SR, out.astype(np.float32))
print('audio ok', out.shape, 'peak', np.max(np.abs(out)))
