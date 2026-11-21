import math

c = new_canvas(128, 128, background=None, name="motorcycle")

# ---------------- palette ----------------
TIRE   = '#141419'
TIRE2  = '#22222a'
RIMBED = '#2e2e37'
BLACK  = '#0e0e13'
BODY   = '#26262e'
DGRAY  = '#3c3c46'
DGRAY2 = '#54545f'
SILVER = '#b6bac2'
SILVD  = '#82868f'
SILVD2 = '#5c6068'
HILITE = '#e4e8ee'
WHITE  = '#f2f4f8'
HUB    = '#8d929b'
RED    = '#d1202c'


# ---------------- helpers ----------------
def tline(x0, y0, x1, y1, colour, w=3):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    half = (w - 1) / 2.0
    for i in range(w):
        t = i - half
        c.line(int(round(x0 + nx * t)), int(round(y0 + ny * t)),
               int(round(x1 + nx * t)), int(round(y1 + ny * t)), colour)


def arc_band(cx, cy, r, a0, a1, colour, thick=3, steps=110):
    offs = [o - (thick - 1) / 2.0 for o in range(thick)]
    for i in range(steps + 1):
        a = math.radians(a0 + (a1 - a0) * i / steps)
        ca, sa = math.cos(a), math.sin(a)
        for o in offs:
            c.set(int(round(cx + (r + o) * ca)), int(round(cy + (r + o) * sa)), colour)


def wheel(cx, cy):
    c.circle(cx, cy, 17, TIRE)
    c.circle(cx, cy, 13, TIRE2)
    c.circle(cx, cy, 11, RIMBED)
    c.circle(cx, cy, 11, SILVER, fill=False)
    for k in range(5):
        a = math.radians(-90 + k * 72)
        tline(cx + 3 * math.cos(a), cy + 3 * math.sin(a),
              cx + 11 * math.cos(a), cy + 11 * math.sin(a), WHITE, 2)
    c.circle(cx, cy, 4, HUB)
    c.circle(cx, cy, 1, SILVD2)


# ============ 1. wheels ============
wheel(30, 84)
wheel(98, 84)

# ============ 2. front fender ============
arc_band(98, 84, 19, -145, -55, DGRAY, 3)

# ============ 3. exhaust ============
tline(76, 88, 84, 94, SILVD, 3)
tline(84, 94, 60, 96, SILVD, 3)
tline(58, 92, 44, 66, SILVER, 6)
c.circle(44, 66, 3, DGRAY)
c.circle(44, 66, 1, BLACK)

# ============ 4. swingarm ============
tline(30, 84, 60, 80, SILVER, 4)

# ============ 5. fork ============
tline(98, 84, 91, 44, SILVER, 4)
tline(99, 83, 92, 43, SILVD, 1)

# ============ 6. engine ============
c.poly([(58, 74), (76, 74), (81, 82), (79, 92), (62, 92), (56, 84)], DGRAY)
c.rect(70, 76, 10, 7, DGRAY2)
c.circle(68, 82, 9, SILVER)
c.circle(68, 82, 6, SILVD)
c.circle(68, 82, 2, SILVD2)
for k in range(3):
    a = math.radians(-150 + k * 60)
    c.set(int(round(68 + 7.5 * math.cos(a))), int(round(82 + 7.5 * math.sin(a))), HILITE)

# ============ 7. body core (upswept tail + mid) ============
c.poly([(84, 58), (80, 54), (76, 52), (64, 53), (50, 52), (32, 47), (20, 44), (17, 44),
        (17, 52), (24, 54), (40, 59), (52, 66), (58, 74), (76, 74), (82, 76)], DGRAY)

# ============ 8. frame spar ============
tline(88, 62, 66, 76, SILVER, 3)

# ============ 9. tail light + tail stripe ============
c.rect(17, 46, 3, 6, RED)
c.set(18, 48, HILITE)
tline(22, 46, 50, 54, RED, 3)

# ============ 10. seat ============
c.poly([(38, 49), (58, 48), (62, 51), (60, 56), (44, 56), (36, 52)], BLACK)

# ============ 11. windscreen (before fairing: fairing hides its base) ============
c.poly([(99, 50), (108, 52), (98, 33), (90, 32)], BLACK)
tline(97, 44, 91, 33, HILITE, 1)

# ============ 12. triple clamp ============
c.rect(84, 42, 10, 4, SILVER)
c.set(85, 43, HILITE)

# ============ 13. fairing ============
c.poly([(78, 58), (81, 52), (90, 50), (100, 49), (108, 51), (114, 55), (116, 59),
        (113, 63), (104, 65), (94, 65), (85, 63), (79, 61)], DGRAY)
tline(80, 61, 100, 62, BODY, 3)
tline(100, 62, 110, 61, BODY, 3)
tline(84, 55, 102, 53, RED, 3)
tline(102, 53, 112, 56, RED, 3)
tline(88, 51, 104, 50, HILITE, 1)
tline(109, 52, 114, 56, HILITE, 1)

# ============ 14. tank (over the fairing's rear) ============
c.poly([(82, 50), (78, 44), (68, 42), (60, 45), (56, 51), (58, 58), (64, 62),
        (72, 61), (78, 56)], BODY)
tline(60, 46, 74, 44, HILITE, 1)

# ============ 15. handlebar grip ============
tline(87, 43, 76, 41, BLACK, 2)

# ============ 16. margins / cleanup ============
c.clear(0, 0, 16, 128)
c.clear(0, 0, 128, 28)
c.clear(118, 0, 10, 128)
c.clear(0, 104, 128, 24)

print(c.stats_text())
print("bbox:", c.stats()['bbox'])
finish(c)
