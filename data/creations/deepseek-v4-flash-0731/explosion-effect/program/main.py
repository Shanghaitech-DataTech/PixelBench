import math
import random

from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="explosion")

# ---- palette (small, well under the 86-colour limit) ----
WHITE = "#fff6d8"
YBRIGHT = "#ffe040"
YELLOW = "#ffc020"
ORANGE = "#ff8a10"
ORRED = "#ff5a10"
RED = "#e03010"
DRED = "#a01808"

CX = CY = 32


def star_poly(cx, cy, r_out, r_in, n, rot):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = rot + math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


# ---- outer expanding blast: spiky multi-coloured fireball ----
c.poly(star_poly(CX, CY, 23, 19, 8, math.pi / 8), DRED)
c.poly(star_poly(CX, CY, 19, 16, 8, math.pi / 8), RED)

# flame lobes on each spike tip for a rougher blast edge
for i in range(8):
    a = math.pi / 8 + math.pi * i / 4
    x = CX + 15 * math.cos(a)
    y = CY + 15 * math.sin(a)
    c.circle(int(round(x)), int(round(y)), 4, ORRED)

c.circle(CX, CY, 14, ORRED)
c.circle(CX, CY, 11, ORANGE)
c.circle(CX, CY, 8, YELLOW)

# ---- bright yellow fireball at centre ----
c.circle(CX, CY, 6, YBRIGHT)
c.circle(CX, CY, 3, WHITE)

# ---- sparks flying outward ----
rng = random.Random(7)
spark_cols = [WHITE, YBRIGHT, YELLOW, ORANGE]
for i in range(26):
    a = rng.uniform(0, 2 * math.pi)
    r = rng.uniform(20, 30)
    x = CX + r * math.cos(a)
    y = CY + r * math.sin(a)
    col = spark_cols[i % len(spark_cols)]
    # short radial streak + bright head
    dx = math.cos(a)
    dy = math.sin(a)
    x2 = x + 2 * dx
    y2 = y + 2 * dy
    c.line(int(round(x)), int(round(y)), int(round(x2)), int(round(y2)), ORRED)
    c.set(int(round(x)), int(round(y)), col)

# a second smaller batch of embers closer in
for i in range(10):
    a = rng.uniform(0, 2 * math.pi)
    r = rng.uniform(15, 20)
    x = int(round(CX + r * math.cos(a)))
    y = int(round(CY + r * math.sin(a)))
    c.set(x, y, ORANGE if i % 2 else YELLOW)

# ---- shockwave ring racing outward (broken into segments, like a blast front) ----
rng2 = random.Random(21)
segments = 28
ring_r = 28.5
for i in range(segments):
    if rng2.random() < 0.30:
        continue  # leave a gap so it reads as a wave front, not a solid circle
    a0 = 2 * math.pi * i / segments
    a1 = 2 * math.pi * (i + 1) / segments
    n = 3
    prev = None
    for k in range(n + 1):
        a = a0 + (a1 - a0) * k / n
        x = CX + ring_r * math.cos(a)
        y = CY + ring_r * math.sin(a)
        p = (int(round(x)), int(round(y)))
        if prev is not None:
            c.line(prev[0], prev[1], p[0], p[1], YBRIGHT)
        prev = p

# far dark-red embers just behind the shockwave
for i in range(12):
    a = rng2.uniform(0, 2 * math.pi)
    r = rng2.uniform(24, 27)
    x = int(round(CX + r * math.cos(a)))
    y = int(round(CY + r * math.sin(a)))
    c.set(x, y, DRED if i % 2 else RED)

print(c.stats_text())
print(c.matrix_text(region=(22, 22, 41, 41)))
print(c.matrix_text(region=(22, 1, 41, 8)))
print(c.matrix_text(region=(1, 28, 8, 39)))

finish(c)
