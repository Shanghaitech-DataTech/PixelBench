from pixelbench_api import *
import math, random

W = H = 64
c = new_canvas(W, H, name="explosion_2frames")

HOT      = c.color("#FFFBE6")
WHITE    = c.color("#FFFFFF")
YELLOW   = c.color("#FFE600")
BRIGHT   = c.color("#FFC800")
ORANGE   = c.color("#FF8C00")
DEEP_OR  = c.color("#F25C00")
RED      = c.color("#E03000")
DARK_RED = c.color("#A81A00")
MAROON   = c.color("#6E0F00")
SPARK    = c.color("#FFED5A")
AMBER    = c.color("#FFB300")

def spike(cx, cy, ang_deg, r_base, r_tip, hw, color):
    a = math.radians(ang_deg)
    tx = cx + r_tip * math.cos(a)
    ty = cy + r_tip * math.sin(a)
    p = a + math.pi / 2
    p1 = (round(cx + r_base * math.cos(a) + hw * math.cos(p)),
          round(cy + r_base * math.sin(a) + hw * math.sin(p)))
    p2 = (round(cx + r_base * math.cos(a) - hw * math.cos(p)),
          round(cy + r_base * math.sin(a) - hw * math.sin(p)))
    c.poly([(round(tx), round(ty)), p1, p2], color, fill=True)

def scatter(cx, cy, n, rmin, rmax, colors, seed, xmin, xmax):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        ang = rng.uniform(0, 360)
        r = rng.uniform(rmin, rmax)
        x = round(cx + r * math.cos(math.radians(ang)))
        y = round(cy + r * math.sin(math.radians(ang)))
        if x < xmin or x > xmax:
            continue
        out.append((x, y, rng.choice(colors)))
    return out

# ---------------- Frame 1: bright yellow fireball at centre (cell x 0..31) ----------------
fx, fy = 16, 32
c.circle(fx, fy, 11, DARK_RED)
c.circle(fx, fy, 9, RED)
c.circle(fx, fy, 8, DEEP_OR)
c.circle(fx, fy, 6, ORANGE)
c.circle(fx, fy, 4, BRIGHT)
c.circle(fx, fy, 2, YELLOW)
c.set(fx, fy, WHITE)
# spiky flame licks
for i, ang in enumerate(range(0, 360, 30)):
    spike(fx, fy, ang, 7, 13, 2.0, [AMBER, BRIGHT, ORANGE][i % 3])
# hot highlight curls
for (dx, dy, rr, colr) in [(-3, -3, 2, HOT), (3, -2, 2, HOT), (0, -5, 2, BRIGHT)]:
    c.circle(fx + dx, fy + dy, rr, colr)
# stray embers
for (x, y, colr) in scatter(fx, fy, 16, 12, 17, [SPARK, YELLOW, BRIGHT, AMBER], 3, 0, 31):
    c.set(x, y, colr)

# ---------------- Frame 2: expanding orange-red blast with sparks (cell x 32..63) ----------------
bx, by = 47, 32
c.circle(bx, by, 15, MAROON)
c.circle(bx, by, 13, DARK_RED)
c.circle(bx, by, 11, RED)
c.circle(bx, by, 9, DEEP_OR)
c.circle(bx, by, 8, ORANGE)
c.circle(bx, by, 6, YELLOW)
c.circle(bx, by, 4, BRIGHT)
c.circle(bx, by, 2, HOT)
c.set(bx, by, WHITE)
# bumpy blast edge
for i, ang in enumerate(range(0, 360, 15)):
    spike(bx, by, ang, 11, 15, 2.0, [RED, DEEP_OR, ORANGE, AMBER][i % 4])
# longer bursts (avoid crossing into frame 1)
for ang in [0, 40, 80, 100, 140, 220, 260, 300, 320]:
    spike(bx, by, ang, 11, 16, 1.6, AMBER if ang % 80 < 40 else BRIGHT)
# flying sparks
for (x, y, colr) in scatter(bx, by, 52, 15, 24, [SPARK, YELLOW, WHITE, BRIGHT], 11, 32, 63):
    c.set(x, y, colr)
# bright outward streaks
rng2 = random.Random(5)
for _ in range(16):
    ang = rng2.uniform(-85, 85) if rng2.random() < 0.65 else rng2.uniform(95, 265)
    r0 = rng2.uniform(13, 15)
    r1 = rng2.uniform(17, 20)
    a = math.radians(ang)
    x0 = round(bx + r0 * math.cos(a)); y0 = round(by + r0 * math.sin(a))
    x1 = round(bx + r1 * math.cos(a)); y1 = round(by + r1 * math.sin(a))
    if x0 < 32 or x1 < 32 or x0 > 63 or x1 > 63:
        continue
    c.line(x0, y0, x1, y1, rng2.choice([SPARK, YELLOW, BRIGHT]))

print(c.stats_text())
print("--- frame1 ---")
print(c.matrix_text(region=(6, 20, 26, 44), indices=True))
print("--- frame2 ---")
print(c.matrix_text(region=(37, 20, 57, 44), indices=True))
finish(c)
