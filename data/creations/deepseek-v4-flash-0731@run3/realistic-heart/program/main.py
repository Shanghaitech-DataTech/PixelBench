import math
from collections import deque
from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="realistic_heart")

def clamp(v, lo, hi):
    if v < lo: return lo
    if v > hi: return hi
    return v

def ell(x, y, cx, cy, a, b):
    dx = (x - cx) / a
    dy = (y - cy) / b
    return dx * dx + dy * dy <= 1.0

def dseg(px, py, ax, ay, bx, by):
    vx = bx - ax; vy = by - ay
    wx = px - ax; wy = py - ay
    L2 = vx * vx + vy * vy
    if L2 == 0:
        return math.hypot(px - ax, py - ay)
    t = clamp((wx * vx + wy * vy) / L2, 0.0, 1.0)
    return math.hypot(px - (ax + t * vx), py - (ay + t * vy))

AORTA = [(25,21),(23,15),(19,11),(13,9),(8,12)]
PULM  = [(35,21),(37,17),(39,13),(41,10),(43,9)]
# coronary surface vessels: faint dark lines over the lobes
CORON_L = [(18,20),(15,25),(12,31),(10,37)]
CORON_R = [(33,21),(37,26),(41,31),(43,36)]
GROOVES = [(16,36),(23,32),(30,31),(37,32),(44,36)]
TIPLINE = [(26,33),(25,41),(24,48),(23,55),(24,59)]

def dvessel(x, y):
    best = 1e9
    for pts in (AORTA, PULM):
        for i in range(len(pts) - 1):
            d = dseg(x, y, pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1])
            if d < best: best = d
    return best

def in_vessel(x, y):
    return dvessel(x, y) <= 2.3

def in_body(x, y):
    if ell(x, y, 20, 30, 13, 10.5): return True
    if ell(x, y, 36, 29, 13.5, 11): return True
    if ell(x, y, 28, 40, 16, 15): return True
    if ell(x, y, 24, 52, 9.5, 10): return True
    if ell(x, y, 34, 43, 9.5, 9): return True
    if ell(x, y, 28, 24, 13, 6.2): return True
    return False

def inside(x, y):
    return in_body(x, y) or in_vessel(x, y)

mask = [[inside(x, y) for x in range(W)] for y in range(H)]
dist = [[-1] * W for _ in range(H)]
dq = deque()
for y in range(H):
    for x in range(W):
        if not mask[y][x]:
            continue
        bnd = False
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= W or ny >= H or not mask[ny][nx]:
                bnd = True
        if bnd:
            dist[y][x] = 0
            dq.append((x, y))
while dq:
    x, y = dq.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and mask[ny][nx] and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            dq.append((nx, ny))

def noise(x, y):
    h = (x * 374761393 + y * 668265263) & 0xffffffff
    h = ((h ^ (h >> 13)) * 1274126177) & 0xffffffff
    return (h & 0xffff) / 65535.0

def shade(x, y):
    d = dist[y][x]
    light = 0.52 + 0.42 * clamp(((34 - x) + (34 - y)) / 44.0, 0.0, 1.0)
    if in_vessel(x, y):
        tc = clamp(1.0 - dvessel(x, y) / 2.3, 0.0, 1.0)
        s = clamp((0.07 + 0.60 * tc) * light, 0.0, 1.0)
    else:
        s = clamp(0.12 + 0.80 * min(d / 11.0, 1.0), 0.0, 1.0) * light
        if y <= 32:
            s = clamp(s + 0.05, 0.0, 1.0)
        for i in range(len(GROOVES) - 1):
            if dseg(x, y, GROOVES[i][0], GROOVES[i][1], GROOVES[i+1][0], GROOVES[i+1][1]) < 1.1 and d > 1:
                s *= 0.74
        for i in range(len(TIPLINE) - 1):
            if dseg(x, y, TIPLINE[i][0], TIPLINE[i][1], TIPLINE[i+1][0], TIPLINE[i+1][1]) < 1.2 and d > 1:
                s *= 0.82
        for pts in (CORON_L, CORON_R):
            for i in range(len(pts) - 1):
                if dseg(x, y, pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1]) < 1.0 and d > 1:
                    s *= 0.82
        if ell(x, y, 34, 31, 4.5, 3.2):
            s = max(s, 0.66)
        if ell(x, y, 36, 33, 2.2, 1.8):
            s = max(s, 0.85)
    s = clamp(s + (noise(x, y) - 0.5) * 0.045, 0.0, 1.0)
    return s

STOPS = [(0.0,(30,4,9)),(0.16,(62,10,17)),(0.34,(104,16,24)),(0.52,(148,26,32)),
        (0.68,(186,42,44)),(0.82,(218,66,58)),(0.93,(242,106,90)),(1.0,(250,146,124))]
def sample_rgb(s):
    s = clamp(s, 0.0, 1.0)
    for i in range(len(STOPS) - 1):
        u0,(r0,g0,b0) = STOPS[i]
        u1,(r1,g1,b1) = STOPS[i+1]
        if s <= u1:
            u = 0.0 if u1 == u0 else (s - u0) / (u1 - u0)
            return (int(r0 + (r1 - r0) * u), int(g0 + (g1 - g0) * u), int(b0 + (b1 - b0) * u))
    return STOPS[-1][1]

NS = 48
pal = [sample_rgb(i / (NS - 1.0)) for i in range(NS)]
idx = [c.color(col) for col in pal]

def center_shadow(x, y):
    if y < 24 or y > 40:
        return 1.0
    vc = math.exp(-((x - 28.5) ** 2) / (2 * 4.5 ** 2))
    vb = math.exp(-((y - 33) ** 2) / (2 * 8.0 ** 2))
    f = 1.0 - 0.30 * vc * vb
    if y < 29:
        f = 1.0 - 0.14 * vc
    return f

for y in range(H):
    for x in range(W):
        if mask[y][x]:
            s = shade(x, y) * center_shadow(x, y)
            c.set(x, y, idx[round(clamp(s, 0.0, 1.0) * (NS - 1))])

print(c.stats_text())

chars = " .:-=+*#%@"
print("ASCII shade map:")
for y in range(H):
    line = ""
    for x in range(W):
        if not mask[y][x]:
            line += " "
        else:
            s = shade(x, y)
            line += chars[min(9, int(s * 10))]
    print(line)

finish(c)
