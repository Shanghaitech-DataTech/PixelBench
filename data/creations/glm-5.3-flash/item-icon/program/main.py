import math

c = new_canvas(32, 32, background=None, name="compass_icon")

# ---------------- palette ----------------
OUT  = c.color("#1b1108", name="outline")
RING = c.color("#2a1a0a", name="inner_ring")
HL   = c.color("#fff3bd", name="gold_highlight")
G1   = c.color("#ffe08a", name="gold_light")
G2   = c.color("#e6ae3c", name="gold")
G3   = c.color("#b57c1e", name="gold_shade")
G4   = c.color("#7c5210", name="gold_deep")
F1   = c.color("#46321a", name="face")
F2   = c.color("#2f2110", name="face_shade")
SCR  = c.color("#6a5133", name="scribe")
C1   = c.color("#bfeaff", name="crystal_light")
C2   = c.color("#59b7f2", name="crystal")
C3   = c.color("#2a6cb4", name="crystal_shade")
C4   = c.color("#143a66", name="crystal_deep")
W    = c.color("#ffffff", name="sparkle")

CX, CY = 15.5, 15.5
LX, LY = -0.7071, -0.7071          # light from top-left


def bezel_tone(d, b):
    if b > 0.80:                    # specular glint, upper-left arc
        return HL
    if b > 0.30:
        return G1
    if b > -0.15:
        return G2
    if b > -0.65:
        return G3
    if b < -0.88 and d > 10.8:      # faint rim light, lower-right edge
        return G3
    return G4


def shade(x, y):
    dx, dy = x - CX, y - CY
    d = math.hypot(dx, dy)
    if d > 14.0:
        return None
    if d > 12.0:                    # thick dark outline
        return OUT
    if d > 9.0:                     # golden bezel
        return bezel_tone(d, (dx * LX + dy * LY) / d)
    if d > 8.0:                     # recessed groove
        return RING
    b = (dx * LX + dy * LY) / d     # dial face
    return F1 if b > -0.35 else F2


for y in range(32):
    for x in range(32):
        col = shade(x, y)
        if col is not None:
            c.set(x, y, col)

# ---------------- needle (4 arms, lit from top-left) ----------------
c.set(15, 8, G1); c.set(16, 8, G1)
for y in range(9, 13):
    c.set(15, y, G1); c.set(16, y, G2)
for y in range(19, 23):
    c.set(15, y, G2); c.set(16, y, G3)
c.set(15, 23, G3); c.set(16, 23, G3)
c.set(8, 15, G1); c.set(8, 16, G2)
for x in range(9, 13):
    c.set(x, 15, G1); c.set(x, 16, G2)
c.set(23, 15, G2); c.set(23, 16, G3)
for x in range(19, 23):
    c.set(x, 15, G2); c.set(x, 16, G3)

# ---------------- engraved scribed ring on the dial ----------------
for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        d = math.hypot(dx, dy)
        if 6.0 <= d < 7.0 and c.get(x, y) in (F1, F2):
            c.set(x, y, SCR)

# ---------------- gold mount + dark seat holding the crystal ----------------
for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        d = math.hypot(dx, dy)
        if 3.3 <= d < 4.4 and c.get(x, y) in (F1, F2):
            b = (dx * LX + dy * LY) / d
            c.set(x, y, G3 if b > 0.15 else G4)
        elif 2.6 <= d < 3.3 and c.get(x, y) in (F1, F2):
            c.set(x, y, RING)

# ---------------- blue crystal centre ----------------
crystal = {
    (15, 13): C2, (16, 13): C2,
    (14, 14): W,  (15, 14): C2, (16, 14): C2, (17, 14): C3,
    (13, 15): C1, (14, 15): C1, (15, 15): C2, (16, 15): C3, (17, 15): C3, (18, 15): C4,
    (13, 16): C2, (14, 16): C2, (15, 16): C3, (16, 16): C3, (17, 16): C4, (18, 16): C4,
    (14, 17): C3, (15, 17): C3, (16, 17): C4, (17, 17): C4,
    (15, 18): C4, (16, 18): C4,
}
for (x, y), col in crystal.items():
    c.set(x, y, col)

# ---------------- diagonal degree ticks ----------------
for (x, y) in [(21, 10), (20, 11), (11, 10), (10, 11),
               (21, 20), (20, 21), (10, 21), (11, 20)]:
    c.set(x, y, G2)

# ---------------- final checks ----------------
print(c.stats_text())
print({k: v for k, v in c.stats().items() if k != "top_colors"})
assert c.stats()["colors_used"] <= 86
print(c.matrix_text(region=(10, 9, 21, 22)))

view(c)
finish(c)
