import math
from pixelbench_api import *

W = H = 32
work = new_canvas(W, H, background=None, name="work")
c = work

# ---------------- palette (warm, muted) ----------------
WHI = c.color("#FCF8EF")
WLT = c.color("#F2E9D9")
WMD = c.color("#E4D6C0")
WSH = c.color("#CDBAA2")
WDP = c.color("#B29C84")
PNK = c.color("#F3D0C7")
PNI = c.color("#DFA9A1")
PND = c.color("#BE8880")
EYE = c.color("#4A3A33")
HOF = c.color("#7E6A59")

# ---------------- helpers ----------------
def new_mask():
    return [[False] * W for _ in range(H)]

def add_ellipse(m, cx, cy, rx, ry=None):
    if ry is None:
        ry = rx
    for y in range(H):
        for x in range(W):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
                m[y][x] = True

def mask_copy(m):
    return [[m[y][x] for x in range(W)] for y in range(H)]

def cleanup(m, maxn=3):
    """drop specks, fill pinholes"""
    n = mask_copy(m)
    for y in range(H):
        for x in range(W):
            cnt = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < W and 0 <= yy < H and m[yy][xx]:
                        cnt += 1
            if m[y][x] and cnt <= maxn:
                n[y][x] = False
            elif (not m[y][x]) and cnt >= 6:
                n[y][x] = True
    return n

def fill(m, col):
    for y in range(H):
        for x in range(W):
            if m[y][x]:
                c.set(x, y, col)

def dist_field(m):
    outs = [(x, y) for y in range(H) for x in range(W) if not m[y][x]]
    d = [[0.0] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if m[y][x]:
                d[y][x] = min(math.hypot(x - ox, y - oy) for ox, oy in outs)
    return d

def blur(d, times=2):
    cur = d
    for _ in range(times):
        nxt = [[0.0] * W for _ in range(H)]
        for y in range(H):
            for x in range(W):
                s = 0.0
                n = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < W and 0 <= yy < H:
                            s += cur[yy][xx]
                            n += 1
                nxt[y][x] = s / n
        cur = nxt
    return cur

LX, LY = -0.52, -0.85
NORM = (WHI, WLT, WMD, WSH)

def rim_paint(mask, tones=NORM, b=3, lit=2.1, sh1=1.05, sh2=2.1):
    """gentle rim shading from the silhouette's own distance field"""
    d = dist_field(mask)
    bb = blur(d, b)
    for y in range(H):
        for x in range(W):
            if not mask[y][x]:
                continue
            gx = (bb[y][min(W - 1, x + 1)] - bb[y][max(0, x - 1)]) / 2.0
            gy = (bb[min(H - 1, y + 1)][x] - bb[max(0, y - 1)][x]) / 2.0
            mag = math.hypot(gx, gy)
            if mag < 1e-9:
                nx, ny = 0.0, -1.0
            else:
                nx, ny = -gx / mag, -gy / mag
            lam = nx * LX + ny * LY
            dd = d[y][x]
            if lam > 0.10 and dd < lit:
                col = tones[0]
            elif lam < -0.12 and dd < sh1:
                col = tones[3]
            elif lam < -0.12 and dd < sh2:
                col = tones[2]
            else:
                col = tones[1]
            c.set(x, y, col)

# ================= body silhouette (fluffy scallops) =================
BCX, BCY, BRX, BRY = 19.3, 14.2, 8.4, 5.35
pts = []
for i in range(1441):
    t = 2 * math.pi * i / 1440
    pts.append((BCX + BRX * math.cos(t), BCY + BRY * math.sin(t)))
acc, next_s, STEP = 0.0, 0.0, 3.4
BUMPS = []
for i in range(1, len(pts)):
    x, y = pts[i]
    px, py = pts[i - 1]
    acc += math.hypot(x - px, y - py)
    if acc >= next_s:
        BUMPS.append((x, y, 1.8))
        next_s = acc + STEP

body = new_mask()
add_ellipse(body, BCX, BCY, BRX, BRY)
add_ellipse(body, 11.0, 19.6, 2.6)      # chest, bridges head to legs
for cx, cy, r in BUMPS:
    add_ellipse(body, cx, cy, r)
body = cleanup(body, 3)

# ================= head silhouette =================
head = new_mask()
add_ellipse(head, 6.0, 16.4, 4.5, 4.5)
for cx, cy, r in [(4.4, 12.6, 1.7), (7.6, 12.4, 1.7), (9.0, 14.6, 1.5)]:
    add_ellipse(head, cx, cy, r)

near_legs = [(11, 13), (21, 23)]
far_legs = [(14, 15), (24, 25)]

# ================= wool shading =================
rim_paint(body, b=3, lit=2.1, sh1=1.05, sh2=2.1)
rim_paint(head, b=3, lit=1.9, sh1=1.05, sh2=2.0)

# contact shadow on the body beside the head
for y in range(H):
    for x in range(W):
        if body[y][x] and not head[y][x]:
            near = False
            for dy in (-2, -1, 0, 1, 2):
                for dx in (-2, -1, 0, 1, 2):
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < W and 0 <= yy < H and head[yy][xx]:
                        near = True
            if near:
                c.set(x, y, WMD)

# wool creases
for grp in ([(16, 12), (17, 12), (18, 12)], [(22, 11), (23, 11)],
            [(13, 16), (14, 16)]):
    for (x, y) in grp:
        if body[y][x] and not head[y][x]:
            c.set(x, y, WMD)

# ================= legs =================
for (x0, x1) in far_legs:
    for x in range(x0, x1 + 1):
        for y in range(18, 28):
            if not body[y][x] and not head[y][x]:
                c.set(x, y, WSH if y < 26 else WDP)
for (x0, x1) in near_legs:
    for x in range(x0, x1 + 1):
        for y in range(18, 28):
            if not body[y][x] and not head[y][x]:
                col = WLT if x < x1 else WMD
                if y >= 26:
                    col = HOF
                c.set(x, y, col)

# ================= ear (pale pink, tilted up-left) =================
ear = new_mask()
for cx, cy, r in [(6.2, 13.0, 1.6), (5.2, 11.8, 1.4),
                  (4.4, 10.6, 1.1), (3.8, 9.6, 0.8)]:
    add_ellipse(ear, cx, cy, r)
fill(ear, PNK)
ear_in = new_mask()
for cx, cy, r in [(5.8, 12.5, 0.9), (5.0, 11.5, 0.8),
                  (4.4, 10.5, 0.7), (3.9, 9.8, 0.5)]:
    add_ellipse(ear_in, cx, cy, r)
fill(ear_in, PNI)

# ================= muzzle =================
muz = new_mask()
add_ellipse(muz, 3.4, 18.6, 2.2, 1.7)
fill(muz, PNK)
for (x, y) in [(4, 20), (3, 20), (5, 19), (4, 19)]:
    if muz[y][x]:
        c.set(x, y, PNI)

# ================= face =================
for x, y in [(4, 15), (5, 15), (4, 16), (5, 16)]:
    c.set(x, y, EYE)
c.set(3, 18, PND)

# ================= centre on the canvas =================
bb = work.stats()["bbox"]
x0, y0, x1, y1 = bb
sw, sh = x1 - x0 + 1, y1 - y0 + 1
dx = int(round((W - sw) / 2.0)) - x0
dy = int(round((H - sh) / 2.0)) - y0
result = new_canvas(W, H, background=None, name="sheep")
result.blit(work, dx, dy)

# drop any isolated single pixels left by the rounding at part joins
for _ in range(3):
    kill = []
    for y in range(H):
        for x in range(W):
            if result.get(x, y) != 0:
                cnt = 0
                for dy_ in (-1, 0, 1):
                    for dx_ in (-1, 0, 1):
                        if dx_ == 0 and dy_ == 0:
                            continue
                        xx, yy = x + dx_, y + dy_
                        if 0 <= xx < W and 0 <= yy < H and result.get(xx, yy) != 0:
                            cnt += 1
                if cnt <= 1:
                    kill.append((x, y))
    if not kill:
        break
    for (x, y) in kill:
        result.set(x, y, None)

print("shift", dx, dy, "sprite", sw, sh)

print(result.stats_text())
print(result.matrix_text())

# --- hygiene checks ---
ruler = "".join(str(x % 10) for x in range(W))
print("     " + ruler)
for y in range(H):
    row = "".join("." if result.get(x, y) == 0 else "#" for x in range(W))
    print("%3d  %s" % (y, row))

specks = []
for y in range(H):
    for x in range(W):
        if result.get(x, y) != 0:
            cnt = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < W and 0 <= yy < H and result.get(xx, yy) != 0:
                        cnt += 1
            if cnt <= 2:
                specks.append((x, y))
print("specks:", specks)
print("colours:", len(result.palette()))
save("farm-sheep", result)
finish(result)
