import numpy as np
from collections import deque

try:
    from pixelbench_api import new_canvas, finish
except Exception:
    pass

W = H = 64

BODY = (200, 30, 30)
AORTA = (220, 120, 100)
VEIN = (70, 100, 150)

# ---- region mask -----------------------------------------------------------
mask = new_canvas(W, H, name="mask")
mask.path(
    "M 20 57 C 14 50 12 40 14 32 C 16 24 22 20 30 20 "
    "C 38 20 46 24 50 32 C 54 40 50 48 44 53 C 38 58 28 60 20 57 Z",
    BODY,
)


def tube(pts, r, col):
    for x, y in pts:
        mask.circle(x, y, r, col)


# aorta: ascends, arches over to the right, descends behind
tube([(33, 26), (32, 21), (31, 16), (32, 12), (36, 9), (41, 10), (44, 14), (45, 19), (46, 23)], 3, AORTA)
# pulmonary trunk
tube([(28, 26), (26, 21), (24, 16), (23, 12), (22, 9)], 2, VEIN)
# superior vena cava
tube([(18, 28), (17, 23), (16, 18), (16, 13), (15, 8)], 2, VEIN)

w, h, data = mask.to_rgba()
raw = data if isinstance(data, np.ndarray) else np.frombuffer(data, dtype=np.uint8).reshape(h, w, 4)
alpha = raw[:, :, 3] > 0


def near(px, ref):
    return (int(px[0]) - ref[0]) ** 2 + (int(px[1]) - ref[1]) ** 2 + (int(px[2]) - ref[2]) ** 2


region = np.zeros((H, W), dtype=np.uint8)  # 0 none, 1 body, 2 aorta, 3 vein
for y in range(H):
    for x in range(W):
        if alpha[y, x]:
            px = raw[y, x, :3]
            d = [near(px, BODY), near(px, AORTA), near(px, VEIN)]
            region[y, x] = 1 + int(np.argmin(d))

# distance to the nearest transparent pixel (BFS)
INF = 999
dist = np.full((H, W), INF, dtype=int)
dq = deque()
for y in range(H):
    for x in range(W):
        if not alpha[y, x]:
            dist[y, x] = 0
            dq.append((x, y))
while dq:
    x, y = dq.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and dist[ny, nx] > dist[y, x] + 1:
            dist[ny, nx] = dist[y, x] + 1
            dq.append((nx, ny))

# ---- shading ---------------------------------------------------------------
RED = ["#2b0708", "#4a0d10", "#661316", "#831b1b", "#9c2422",
       "#b52f2a", "#cc4438", "#dd5f4c", "#ea7c62", "#f29a7c"]
ART = ["#4a120c", "#641c12", "#7e2a18", "#983c22",
       "#b05232", "#c66a46", "#d9845e", "#e8a078"]
VEN = ["#101c2e", "#182a44", "#22395a", "#2e4a72",
       "#3c5d8a", "#4c72a2", "#6088ba", "#78a0d0"]
LIGHT = {1: ((22, 26), 27), 2: ((33, 12), 18), 3: ((18, 10), 14)}
BAYER = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16.0

c = new_canvas(W, H, name="heart")
for y in range(H):
    for x in range(W):
        r = region[y, x]
        if r == 0:
            continue
        ramp = (None, RED, ART, VEN)[r]
        n = len(ramp)
        (lx, ly), lr = LIGHT[r]
        d = dist[y, x]
        dd = ((x - lx) ** 2 + (y - ly) ** 2) ** 0.5
        hl = max(0.0, 1.0 - dd / lr)
        depth = min(d, 8) / 8.0
        b = 0.14 + 0.34 * depth + 0.62 * (hl ** 1.35)
        if d <= 1:
            b = 0.02
        elif d == 2:
            b = min(b, 0.20)
        b = min(max(b, 0.0), 0.999)
        t = b * (n - 1)
        i = int(t + BAYER[y % 4, x % 4])
        i = max(0, min(n - 1, i))
        c.set(x, y, ramp[i])

# ---- epicardial fat --------------------------------------------------------
YEL = ["#5f4118", "#7c5a20", "#9a732c", "#b58a3c", "#cba452", "#dcbc6e"]


def fat(cx, cy, rx, ry):
    for y in range(max(0, cy - ry), min(H, cy + ry + 1)):
        for x in range(max(0, cx - rx), min(W, cx + rx + 1)):
            if region[y, x] != 1:
                continue
            e = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
            if e > 1.0:
                continue
            dd = ((x - 22) ** 2 + (y - 26) ** 2) ** 0.5
            hl = max(0.0, 1.0 - dd / 30.0)
            b = 0.30 + 0.62 * hl - 0.35 * max(0.0, e - 0.55) / 0.45
            i = int(round(b * (len(YEL) - 1)))
            c.set(x, y, YEL[max(0, min(len(YEL) - 1, i))])


fat(31, 27, 4, 5)
fat(44, 35, 4, 4)
fat(25, 48, 3, 5)
fat(19, 33, 2, 3)

# ---- interventricular groove + coronary vessels ----------------------------
c.path("M 31 27 C 30 33 29 38 27 44 C 26 48 24 51 22 54", "#36080a", fill=False)
ART_COL = "#eda184"
c.path("M 33 28 C 31 34 30 40 29 46 C 28 50 27 52 26 55", ART_COL, fill=False)
c.path("M 31 34 L 36 37", ART_COL, fill=False)
c.path("M 29 41 L 34 44", ART_COL, fill=False)
c.path("M 28 47 L 32 50", ART_COL, fill=False)
c.path("M 40 29 C 43 31 45 35 45 40 C 45 44 43 47 40 50", ART_COL, fill=False)
c.path("M 44 33 L 39 35", ART_COL, fill=False)
c.path("M 45 39 L 40 41", ART_COL, fill=False)
# cardiac vein, running beside the artery in the groove
VEIN_COL = "#3c5d8a"
c.path("M 30 28 C 29 34 28 40 26 46 C 25 50 24 52 23 55", VEIN_COL, fill=False)
# shadow creases where the great vessels root into the muscle
c.path("M 29 24 C 30 27 32 29 35 30", "#4a0d10", fill=False)
c.path("M 37 25 C 37 28 39 30 42 31", "#4a0d10", fill=False)
c.path("M 20 31 C 22 33 24 34 26 34", "#4a0d10", fill=False)

# ---- vessel lumina (cut ends) ----------------------------------------------
c.ellipse(22, 9, 2, 1, "#0d1a2c")
c.ellipse(15, 8, 2, 1, "#0d1a2c")

# ---- speculars -------------------------------------------------------------
for x, y, col in [(24, 29, "#f7b39a"), (25, 28, "#f7b39a"), (23, 31, "#f7b39a"),
                  (32, 11, "#f2c2a8"), (33, 10, "#f2c2a8"),
                  (15, 11, "#a8c8e8"), (16, 10, "#a8c8e8")]:
    c.set(x, y, col)

print(c.stats_text())
finish(c)
