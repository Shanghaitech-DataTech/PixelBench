from pixelbench_api import *
from collections import Counter

output = input_canvas.copy(name="output")
W, H = 250, 147
pal0 = output.palette()

# ---------- helpers ----------
def lerp(a, b, t): return a + (b - a) * t

def lerp3(c1, c2, t):
    return tuple(int(round(lerp(c1[k], c2[k], t))) for k in range(3))

def ramps_stops(t, stops):
    # stops: list of (pos, colour); t in [0,1]
    t = min(1.0, max(0.0, t))
    for k in range(len(stops) - 1):
        p0, c0 = stops[k]
        p1, c1 = stops[k + 1]
        if t <= p1:
            u = 0.0 if p1 == p0 else (t - p0) / (p1 - p0)
            return lerp3(c0, c1, u)
    return stops[-1][1]

def hexc(rgb): return '#%02x%02x%02x' % rgb

LUM = {}
for e in pal0:
    r, g, b, a = e['rgba']
    LUM[e['index']] = 0.299*r + 0.587*g + 0.114*b

# ---------- classify input pixels ----------
def base_cls(i):
    r, g, b, a = pal0[i]['rgba']
    L = LUM[i]
    mx, mn = max(r, g, b), min(r, g, b)
    if L < 55:
        return 'F' if b < r - 6 else 'M'
    if mx - mn < 35 and L > 180:
        return 'O'                      # moon -> sky
    if r - b > 45:
        return 'A'                      # snow / warm cloud
    if L >= 100:
        return 'S'
    return 'M'

clsmap = [[base_cls(output.get(x, y)) for x in range(W)] for y in range(H)]

# moon mask -> force to sky (O occurs only in the moon disc)
for y in range(H):
    for x in range(W):
        if clsmap[y][x] == 'O':
            clsmap[y][x] = 'S'

# ---------- sky/ground horizon per column (solid run of M/F/A) ----------
def solid(c): return c in ('M', 'F', 'A')

gy = []
for x in range(W):
    g = 120
    run = 0
    for y in range(0, 120):
        if solid(clsmap[y][x]):
            run += 1
            if run >= 6:
                g = y - 5
                break
        else:
            run = 0
    gy.append(g)
mode_gy = Counter(gy).most_common(1)[0][0]
gy = [v if abs(v - mode_gy) <= 12 else mode_gy for v in gy]
# clamp spikes: horizon never sits below the neighbourhood minimum
gy = [min(gy[max(0, x-8):min(W, x+9)]) for x in range(W)]

# ---------- forest top line ----------
ftop = []
for x in range(W):
    f = 130
    run = 0
    for y in range(0, H):
        if clsmap[y][x] == 'F':
            run += 1
            if run >= 5:
                f = y - 4
                break
        else:
            run = 0
    ftop.append(f)

# ---------- region assignment ----------
# region: S sky (y < gy), M mountain (gy..ftop-1), F forest (>= ftop)
# note: snow/cloud 'A' keeps accent region; sky-coloured haze below gy -> HM (haze-mountain)
regions = []
for y in range(H):
    row = []
    for x in range(W):
        c = clsmap[y][x]
        if c == 'A':
            row.append('A')
        elif y < gy[x]:
            row.append('S')
        elif y < ftop[x]:
            row.append('M' if c in ('M', 'F') else 'HM')
        else:
            row.append('F')
    regions.append(row)

# ---------- per-region luminance min/max ----------
def lum_range(pred):
    vals = [LUM[output.get(x, y)] for y in range(H) for x in range(W) if pred(x, y)]
    return (min(vals), max(vals)) if vals else (0.0, 1.0)

lo_sky, hi_sky   = lum_range(lambda x, y: regions[y][x] == 'S')
lo_acc, hi_acc   = lum_range(lambda x, y: regions[y][x] == 'A')
lo_mt,  hi_mt    = lum_range(lambda x, y: regions[y][x] == 'M')
lo_hm,  hi_hm    = lum_range(lambda x, y: regions[y][x] == 'HM')
lo_fo,  hi_fo    = lum_range(lambda x, y: regions[y][x] == 'F')

SKY = [(0.0, (36, 100, 214)), (0.55, (104, 168, 240)), (1.0, (198, 232, 252))]
ACC = [(0.0, (226, 236, 250)), (0.5, (244, 249, 254)), (1.0, (255, 255, 255))]
MTN = [(0.0, (52, 68, 122)), (0.45, (92, 112, 162)), (1.0, (150, 170, 212))]
HZE = [(0.0, (160, 186, 226)), (1.0, (196, 220, 244))]
FOR = [(0.0, (14, 34, 20)), (0.5, (40, 88, 44)), (1.0, (140, 194, 84))]

def norm(L, lo, hi):
    return 0.0 if hi <= lo else (L - lo) / (hi - lo)

# ---------- repaint ----------
for y in range(H):
    for x in range(W):
        i = output.get(x, y)
        L = LUM[i]
        rg = regions[y][x]
        if rg == 'S':
            output.set(x, y, ramps_stops(norm(L, lo_sky, hi_sky), SKY))
        elif rg == 'A':
            output.set(x, y, ramps_stops(norm(L, lo_acc, hi_acc), ACC))
        elif rg == 'M':
            output.set(x, y, ramps_stops(norm(L, lo_mt, hi_mt), MTN))
        elif rg == 'HM':
            output.set(x, y, ramps_stops(norm(L, lo_hm, hi_hm), HZE))
        else:
            output.set(x, y, ramps_stops(norm(L, lo_fo, hi_fo), FOR))

# ---------- smooth noon sky gradient above the horizon ----------
pal = output.palette()
def skyish_idx(i):
    r, g, b, a = pal[i]['rgba']
    return b > r + 25 and b > 120

ZEN, HOR = (36, 100, 214), (198, 232, 252)
for x in range(W):
    g = gy[x]
    for y in range(0, g):
        if skyish_idx(output.get(x, y)):
            t = (y / max(1.0, g - 1.0)) ** 0.92
            output.set(x, y, lerp3(ZEN, HOR, t))

# ---------- cleanup: erase isolated sky specks (leftover moon halo pixels) ----------
pal = output.palette()
for y in range(1, 109):
    for x in range(1, W - 1):
        i = output.get(x, y)
        if not skyish_idx(i):
            nb = [output.get(x-1, y), output.get(x+1, y), output.get(x, y-1), output.get(x, y+1)]
            if all(skyish_idx(j) for j in nb):
                output.set(x, y, output.get(x - 1, y))

view(output, scale=3)
finish(output)
