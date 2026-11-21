import math

c = new_canvas(64, 64, background="#141019", name="output")

# --- palette ---
BG1 = "#1d1726"
BG2 = "#272033"
SHD = "#0d0a12"

P0 = "#1c1006"
P1 = "#2b1a09"
P2 = "#3d2710"
G1 = "#5a3a16"
G2 = "#7d5420"
G3 = "#a3722c"
G4 = "#c6943c"
G5 = "#e0b455"
G6 = "#f3d481"
G7 = "#fff0bf"

S1 = "#3c3f4a"
S2 = "#5d616e"
S3 = "#8a8f9c"
S4 = "#c8ccd6"
D1 = "#a89c86"
D2 = "#cfc4ae"
D3 = "#f7f2e4"
DK = "#8d8371"
TICK = "#6b6253"
INK = "#1b1510"
RUBY = "#9a2f3a"

CX, CY, R = 38, 32, 20

c.ellipse(30, 34, 34, 30, BG1)
c.ellipse(30, 34, 24, 21, BG2)
c.ellipse(34, 56, 26, 5, SHD)

# ---------------- open lid (left) ----------------
c.ellipse(13, 30, 9, 19, G1)
c.ellipse(13, 30, 8, 18, G3)
c.ellipse(13, 30, 7, 16, G2)
c.ellipse(13, 30, 5, 13, G3)
c.ellipse(13, 30, 5, 13, G1, fill=False)
c.ellipse(13, 30, 3, 8, G1, fill=False)
c.path("M 11 19 Q 8 30 11 41", G7, fill=False)
c.path("M 12 21 Q 9.5 30 12 39", G6, fill=False)
c.path("M 14 23 Q 12 30 14 37", G5, fill=False)
c.path("M 18 23 Q 20 31 18 39", G1, fill=False)
c.path("M 6 25 Q 5 30 6 35", G6, fill=False)

c.rect(20, 29, 4, 6, G2)
c.rect(20, 30, 4, 2, G5)
c.set(22, 34, P0)
c.set(21, 35, P1)

# ---------------- case body ----------------
c.circle(CX, CY, R, G1)
c.circle(CX, CY, R - 1, G3)
c.circle(CX, CY, R - 2, G2)
c.circle(CX, CY, R - 3, G4)
c.circle(CX, CY, R - 4, G1)
c.circle(CX, CY, R - 5, P0)
c.path("M 24 19 A 19 19 0 0 1 47 14", G7, fill=False)
c.path("M 21 24 A 18 18 0 0 1 32 14", G6, fill=False)
c.path("M 51 44 A 19 19 0 0 1 32 51", P0, fill=False)
c.path("M 54 38 A 18 18 0 0 1 47 49", G1, fill=False)
c.path("M 24 44 A 18 18 0 0 0 32 50", G2, fill=False)

# movement baseplate
c.circle(CX, CY, 15, P1)
c.circle(CX, CY, 15, P0, fill=False)

# brass top bridge plate: solid, shaped, lit from the upper left
c.path("M 25 26 Q 27 19 34 18 L 45 19 Q 51 22 51 28 "
       "Q 46 24 40 25 Q 32 25 25 26 Z", G3)
c.path("M 26 25 Q 28 20 34 19 L 44 20 Q 49 23 50 27", G5, fill=False)
c.path("M 25 26 Q 27 19 34 18 L 44 19", G6, fill=False)
c.path("M 25 26 Q 32 25 40 25 Q 46 24 51 28", G1, fill=False)
c.path("M 26 27 Q 33 26 40 26 Q 46 25 50 29", P0, fill=False)
c.set(27, 24, G7)
c.set(33, 19, G7)
c.set(50, 27, G2)
# engraved screw holes along the bridge
c.set(30, 22, P1)
c.set(47, 24, P1)


def pt(cx, cy, r, a):
    return int(round(cx + math.cos(a) * r)), int(round(cy + math.sin(a) * r))


def gear(cx, cy, r, teeth, phase, spokes, body=G4, rim=G3, lit=G7):
    c.circle(cx, cy, r + 2, P0)
    for i in range(teeth):
        a = phase + 2.0 * math.pi * i / teeth
        hot = math.cos(a + 2.3) > 0.0
        col = lit if hot else rim
        tx, ty = pt(cx, cy, r + 1, a)
        c.rect(tx - 1, ty - 1, 2, 2, col)
    c.circle(cx, cy, r, G1)
    c.circle(cx, cy, r - 1, body)
    c.circle(cx, cy, r - 3, P0)
    for i in range(spokes):
        a = phase + 2.0 * math.pi * i / spokes
        c.line(cx, cy, *pt(cx, cy, r - 2, a), body)
    for k in range(8):
        a = math.radians(170 + k * 13)
        c.set(*pt(cx, cy, r - 1, a), G6)
    for k in range(6):
        a = math.radians(-10 + k * 13)
        c.set(*pt(cx, cy, r - 1, a), G2)
    c.circle(cx, cy, 1, G5)
    c.set(cx, cy, INK)


# ---- gear train in the lower band ----
gear(29, 38, 6, 10, 0.10, 4)
gear(42, 39, 5, 9, 0.32, 4, body=G5, rim=G4)
gear(50, 31, 3, 7, 0.20, 3, body=G5, rim=G4)
gear(26, 27, 3, 7, 0.45, 3, body=G4, rim=G3)

# steel balance wheel mounted on the bridge, right of centre
c.circle(45, 23, 3, S1)
c.circle(45, 23, 3, S2, fill=False)
c.circle(45, 23, 1, S3, fill=False)
c.set(43, 21, S4)
c.set(44, 21, S4)
c.set(47, 25, S1)
c.set(45, 23, S4)

# screws + jewels
for (sx, sy) in [(31, 22), (36, 45), (48, 42)]:
    c.circle(sx, sy, 1, S2)
    c.set(sx, sy - 1, S4)
    c.set(sx, sy, S1)
c.set(36, 35, RUBY)
c.set(47, 36, RUBY)
c.set(30, 31, RUBY)

# ---------------- chapter ring ----------------
ring = new_canvas(64, 64, name="ring")
ring.circle(CX, CY, 15, D2)
ring.circle(CX, CY, 13, None)
for i in range(60):
    a = -math.pi / 2 + 2.0 * math.pi * i / 60
    if i % 5 == 0:
        x0, y0 = pt(CX, CY, 13.2, a)
        x1, y1 = pt(CX, CY, 14.6, a)
        ring.line(x0, y0, x1, y1, INK)
    else:
        ring.set(*pt(CX, CY, 14.3, a), TICK)
ring.circle(CX, CY, 15, D1, fill=False)
ring.path("M 24 20 A 16 16 0 0 1 46 15", D3, fill=False)
ring.path("M 51 45 A 16 16 0 0 1 33 51", DK, fill=False)
c.blit(ring, 0, 0)

# ---------------- hands ----------------
c.line(CX, CY, CX - 7, CY - 6, INK)
c.line(CX - 1, CY - 1, CX - 7, CY - 7, INK)
c.line(CX - 1, CY, CX - 6, CY - 6, S4)
c.line(CX, CY, CX + 5, CY - 10, INK)
c.line(CX + 1, CY, CX + 6, CY - 10, INK)
c.line(CX + 1, CY - 1, CX + 5, CY - 9, S4)
c.circle(CX, CY, 1, G6)
c.set(CX, CY, G7)

# ---------------- crown, bow, chain ----------------
c.rect(36, 9, 4, 4, G3)
c.rect(36, 9, 4, 1, G6)
c.set(39, 11, G2)
c.set(39, 12, G1)
c.ellipse(38, 6, 3, 3, G4, fill=False)
c.set(36, 4, G7)
c.set(37, 3, G6)
c.set(40, 8, G1)

LINKS = [(43, 4), (47, 2), (51, 3), (55, 5), (58, 8), (60, 12), (62, 17), (63, 22)]
for n, (lx, ly) in enumerate(LINKS):
    if n % 2 == 0:
        c.ellipse(lx, ly, 2, 1, G3, fill=False)
        c.set(lx - 1, ly - 1, G6)
    else:
        c.ellipse(lx, ly, 1, 2, G4, fill=False)
        c.set(lx - 1, ly - 1, G5)

print(c.stats_text())

# ---------------- final light/contrast pass ----------------
# shadow cast by the bezel onto the lower-right of the movement
for k in range(16):
    a = math.radians(-40 + k * 7)
    c.set(*pt(CX, CY, 13.0, a), P0)
# raking highlight glint on the bezel top-left and case edge
c.set(27, 17, G7)
c.set(28, 16, G7)
c.set(24, 21, G7)
# darker underside of the case
c.path("M 30 51 A 19 19 0 0 0 45 48", P0, fill=False)

view(c)
finish(c)
