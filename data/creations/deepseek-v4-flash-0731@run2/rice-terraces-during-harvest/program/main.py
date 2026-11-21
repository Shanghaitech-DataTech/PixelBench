from pixelbench_api import new_canvas, finish
import math, random

W = H = 64
c = new_canvas(W, H, background="#f8eed2")
rng = random.Random(20240917)

# ---- terrace colour gradient: pale hazy gold (high/distant) -> deep gold (near) ----
stops = [
    (247, 236, 198),
    (240, 221, 160),
    (231, 204, 128),
    (220, 185, 100),
    (207, 165, 77),
    (193, 145, 59),
    (177, 124, 46),
    (160, 104, 36),
    (141, 86, 28),
    (121, 69, 22),
    (100, 55, 17),
]

def _lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))

def level_rgb(k):
    t = k / 28.0
    pos = t * (len(stops) - 1)
    i = min(int(pos), len(stops) - 2)
    return "#%02x%02x%02x" % _lerp(stops[i], stops[i + 1], pos - i)

RIDGE = "#4a2e11"
RIDGE2 = "#3a2310"

def height(x, y):
    dx = x - 29.0
    dy = (y - 7.5) * 1.6
    wob = 6.0 * math.sin(x * 0.26 + y * 0.34) + 4.5 * math.sin(x * 0.16 - y * 0.20 + 2.0)
    return math.hypot(dx, dy) + wob

band = 3.3
for y in range(H):
    for x in range(W):
        h = height(x, y)
        k = max(0, int(h / band))
        f = h / band - int(h / band)
        col = RIDGE if f < 0.16 else level_rgb(k)
        c.set(x, y, col)

# ---- light mist over the highest (top) terraces ----
for y in range(0, 6):
    for x in range(0, W):
        if rng.random() < 0.35:
            c.set(x, y, "#f9f2da")

# ---- stubble / textured crop sprinkle ----
for y in range(H):
    for x in range(W):
        if rng.random() < 0.045:
            c.set(x, y, "#eeda98" if rng.random() < 0.5 else "#7a521f")

# ---- small piles of cut stalks (harvest bundles) ----
for _ in range(28):
    x = rng.randrange(3, W - 3)
    y = rng.randrange(10, H - 3)
    c.rect(x, y, 2, 2, "#e9d590")
    c.rect(x + 1, y + 1, 2, 1, "#8a5d22")

# ---- one small irrigation pond ----
c.circle(20, 25, 3, "#a9c6c0")
c.circle(20, 25, 2, "#c3dbd2")
c.set(19, 24, "#dcece3")
c.circle(20, 25, 3, "#6f938c", fill=False)

# ---- distant village houses ----
def house(x, y, roof):
    c.rect(x + 1, y + 1, 4, 3, "#3b2410")   # shadow
    c.rect(x, y, 4, 3, roof)
    c.line(x + 1, y + 1, x + 2, y + 1, "#5e321e")

hl = [
    (26, 10, "#a05a3c"),
    (33, 9, "#8f8a7c"),
    (40, 11, "#a05a3c"),
    (29, 13, "#a05a3c"),
    (36, 13, "#a05a3c"),
    (32, 16, "#97704f"),
]
for hx, hy, roof in hl:
    house(hx, hy, roof)

# ---- trees tucked around the village ----
for tx, ty in [(24, 12), (43, 9), (28, 15), (38, 16), (35, 18)]:
    c.circle(tx, ty, 2, "#41603a")
    c.circle(tx, ty + 1, 2, "#2f4929")

# ---- two farmers carrying harvest on narrow ridges ----
def farmer(fx, fy):
    c.rect(fx - 3, fy, 7, 3, RIDGE2)                 # ridge they stand on
    c.line(fx - 3, fy + 1, fx + 3, fy + 1, "#261a0d")  # bamboo pole
    c.rect(fx - 3, fy, 2, 2, "#33240f")               # load (left)
    c.rect(fx + 2, fy, 2, 2, "#33240f")               # load (right)
    c.rect(fx - 1, fy, 3, 2, "#5a452c")               # body
    c.rect(fx - 1, fy - 1, 3, 1, "#f2e2b4")           # conical hat

farmer(17, 39)
farmer(45, 51)

# ---- distant birds ----
for bx, by in [(12, 3), (8, 5), (16, 4)]:
    c.set(bx, by, "#8f8571")
    c.set(bx + 1, by + 1, "#8f8571")

print(c.stats_text())
finish(c)
