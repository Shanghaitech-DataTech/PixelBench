import math, random

random.seed(11)

W = H = 64
c = new_canvas(W, H, background=None, name="explosion_2frames")

WHITE = (255, 255, 255)
YB    = (255, 246, 96)
Y1    = (255, 224, 40)
Y2    = (255, 200, 16)
O1    = (255, 160, 24)
O2    = (255, 116, 8)
R1    = (232, 64, 0)
R2    = (178, 34, 0)


def spike(cx, cy, ang, tip_r, base_r, hw, col, xmin, xmax):
    a = math.radians(ang)
    pts = []
    for (r, off) in ((tip_r, 0.0), (base_r, -hw), (base_r, hw)):
        x = min(max(cx + r * math.cos(a + math.radians(off)), xmin), xmax)
        y = min(max(cy + r * math.sin(a + math.radians(off)), 0), 63)
        pts.append((round(x), round(y)))
    c.poly(pts, col, fill=True)


def spark(cx, cy, ang, r1, r2, col, xmin, xmax):
    a = math.radians(ang)
    pts = []
    for r in (r1, r2):
        x = min(max(cx + r * math.cos(a), xmin), xmax)
        y = min(max(cy + r * math.sin(a), 0), 63)
        pts.append((round(x), round(y)))
    c.line(pts[0][0], pts[0][1], pts[1][0], pts[1][1], col)


def dot(cx, cy, ang, r, col, xmin, xmax):
    a = math.radians(ang)
    x = min(max(cx + r * math.cos(a), xmin), xmax)
    y = min(max(cy + r * math.sin(a), 0), 63)
    c.set(round(x), round(y), col)


# ---------------- Frame 1 (left half): bright yellow fireball at center ----------------
cx1, cy1 = 16, 32
c.circle(cx1, cy1, 14, R1)
c.circle(cx1, cy1, 11, O2)
c.circle(cx1, cy1, 8, O1)
c.circle(cx1, cy1, 6, Y1)
c.circle(cx1, cy1, 4, YB)
c.circle(cx1, cy1, 2, WHITE)

# flame tongues
for i, ang in enumerate([0, 45, 90, 135, 180, 225, 270, 315]):
    spike(cx1, cy1, ang, 16, 9, 22, Y1 if i % 2 == 0 else O1, 0, 31)
for i, ang in enumerate([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]):
    spike(cx1, cy1, ang, 14, 11, 14, O2 if i % 2 else Y2, 0, 31)

# little drifting sparks around the fireball
for _ in range(10):
    spark(cx1, cy1, random.uniform(0, 360), random.uniform(13, 15), random.uniform(15, 18),
          random.choice([YB, Y1, O1, WHITE]), 0, 31)

# ---------------- Frame 2 (right half): expanding orange-red blast with sparks ----------------
cx2, cy2 = 48, 32
c.circle(cx2, cy2, 15, R2)
c.circle(cx2, cy2, 12, R1)
c.circle(cx2, cy2, 9, O2)
c.circle(cx2, cy2, 6, O1)
c.circle(cx2, cy2, 4, Y1)
c.circle(cx2, cy2, 2, YB)

# ragged expanding tongues
for i, ang in enumerate([0, 40, 80, 120, 160, 200, 240, 280, 320]):
    spike(cx2, cy2, ang, 19, 10, 26, R1 if i % 2 == 0 else O2, 32, 63)

# partial shockwave ring segments
for a0 in range(0, 360, 45):
    spark(cx2, cy2, a0, 16, 18, O2, 32, 63)
    spark(cx2, cy2, a0 + 22, 18, 20, R2, 32, 63)

# radiating sparks
for _ in range(22):
    ang = random.uniform(0, 360)
    spark(cx2, cy2, ang, random.uniform(13, 16), random.uniform(16, 21),
          random.choice([WHITE, YB, Y1, O1]), 32, 63)

for _ in range(14):
    dot(cx2, cy2, random.uniform(0, 360), random.uniform(14, 22),
        random.choice([YB, O1, WHITE, Y1]), 32, 63)

print(c.stats_text())
result = c
finish(result)
