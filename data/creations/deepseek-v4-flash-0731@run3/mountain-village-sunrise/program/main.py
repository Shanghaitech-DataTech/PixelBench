import math
import random

random.seed(11)
W = H = 128
c = new_canvas(W, H)

def C(spec, name=None):
    return c.color(spec, name)

# ------------------------------------------------------------------
# SKY bands (sunrise)
# ------------------------------------------------------------------
sky_bands = [
    (0, 15, (36, 32, 66)),    # deep purple top
    (16, 31, (88, 56, 96)),   # rose purple
    (32, 47, (156, 88, 100)), # warm rose
    (48, 59, (220, 140, 96)), # orange
    (60, 63, (244, 168, 110)),# bright horizon
]
for (y0, y1, col) in sky_bands:
    c.rect(0, y0, 128, y1 - y0 + 1, C(col))

# cloud streaks
cloud1 = C((228, 160, 120))
cloud2 = C((242, 186, 144))
for (sx, sy, ln, col) in [
    (16, 19, 9, cloud1), (34, 15, 7, cloud1), (88, 20, 11, cloud1),
    (24, 33, 6, cloud2), (78, 29, 8, cloud2),
]:
    for i in range(ln):
        c.set(sx + i, sy, col)

# ------------------------------------------------------------------
# SUN glow + disc (focal point, low centre)
# ------------------------------------------------------------------
sun_glow = C((232, 134, 88))
sun_halo = C((250, 168, 104))
sun_disc = C((252, 192, 110))
sun_core = C((255, 242, 200))
c.circle(64, 36, 19, sun_glow)
c.circle(64, 36, 13, sun_glow)
c.circle(64, 36, 10, sun_halo, fill=False)
c.circle(64, 36, 8, sun_disc)
c.circle(64, 36, 3, sun_core)

# birds
birdcol = C((34, 30, 46))
def bird(x, y):
    c.set(x, y, birdcol)
    c.set(x - 1, y + 1, birdcol)
    c.set(x + 1, y + 1, birdcol)
bird(34, 26)
bird(42, 22)
bird(92, 21)

# ------------------------------------------------------------------
# MOUNTAINS (two hazy ridges + near foothill)
# ------------------------------------------------------------------
def ridge(points, base, color):
    c.poly([(0, base)] + points + [(127, base)], C(color))

# far ridge (light hazy purple)
ridge([(10, 42), (20, 50), (32, 36), (44, 46), (56, 38), (64, 34),
       (74, 44), (86, 36), (98, 46), (110, 40), (120, 50)], 64, (132, 94, 130))
# mid ridge (deeper purple)
ridge([(12, 50), (26, 60), (40, 48), (54, 58), (64, 56), (76, 58),
       (90, 46), (104, 58), (116, 50)], 64, (92, 66, 104))
# near foothill ridge
ridge([(16, 56), (32, 62), (50, 58), (70, 60), (88, 56), (108, 62), (120, 58)],
      64, (70, 56, 84))

# ------------------------------------------------------------------
# GROUND bands
# ------------------------------------------------------------------
meadow = C((110, 116, 86))   # far meadow y64..77
lawn = C((90, 102, 64))      # mid lawn    y78..105
front = C((58, 70, 46))      # foreground y106..127
grass_lo = C((46, 58, 38))
grass_hi = C((70, 82, 54))
c.rect(0, 64, 128, 14, meadow)
c.rect(0, 78, 128, 28, lawn)
c.rect(0, 106, 128, 22, front)

for _ in range(260):
    gx = random.randint(0, 127)
    gy = random.randint(106, 127)
    c.set(gx, gy, grass_lo if random.random() < 0.55 else grass_hi)
for _ in range(120):
    c.set(random.randint(0, 127), random.randint(80, 104), grass_lo)

# ------------------------------------------------------------------
# PINE TREES
# ------------------------------------------------------------------
def pine(cx, tip, basew, step, tier_h, col, trunkcol):
    cc = C(col)
    for i in range(3):
        y0 = tip + step * i
        y1 = y0 + tier_h
        halfw = basew + i * (basew - 1)
        c.poly([(cx, y0), (cx - halfw, y1), (cx + halfw, y1)], cc)
    c.rect(cx - 2, tip + 2 * step + tier_h - 2, 4, 8, C(trunkcol))

green_big = (30, 54, 38)
green_mid = (36, 60, 42)
green_sm = (26, 48, 34)
trunk = (58, 44, 32)
pine(20, 52, 5, 8, 9, green_big, trunk)
pine(104, 50, 5, 8, 9, green_big, trunk)
pine(30, 72, 4, 6, 7, green_mid, trunk)
pine(98, 70, 4, 6, 7, green_mid, trunk)
pine(116, 90, 3, 5, 6, green_sm, trunk)
pine(10, 94, 3, 5, 6, green_sm, trunk)

# ------------------------------------------------------------------
# VILLAGE (three wooden houses, village at centre)
# ------------------------------------------------------------------
wood = C((112, 78, 52))
woodd = C((96, 64, 42))
roof = C((150, 78, 64))
roofl = C((182, 110, 82))
dk = C((56, 38, 30))
lit = C((255, 214, 130))
brick = C((122, 96, 88))
brickd = C((100, 78, 72))

# main house (cx=64) -- focal
c.rect(53, 82, 22, 15, wood)
c.rect(53, 87, 22, 1, woodd)
c.rect(53, 92, 22, 1, woodd)
c.poly([(50, 84), (64, 73), (78, 84)], roof)
c.line(50, 85, 78, 85, roofl)
c.rect(58, 86, 3, 3, lit)
c.rect(66, 86, 3, 3, lit)
c.rect(61, 91, 5, 5, dk)
c.rect(65, 93, 1, 2, lit)
c.rect(68, 75, 4, 8, brick)
c.rect(67, 74, 6, 1, brickd)

# left house (cx=42)
c.rect(35, 84, 14, 11, wood)
c.rect(35, 89, 14, 1, woodd)
c.poly([(33, 86), (42, 76), (51, 86)], roof)
c.line(33, 87, 51, 87, roofl)
c.rect(36, 86, 2, 2, lit)
c.rect(39, 89, 4, 5, dk)
c.rect(37, 78, 3, 6, brick)
c.rect(36, 77, 5, 1, brickd)

# right house (cx=86)
c.rect(79, 85, 13, 10, wood)
c.rect(79, 90, 13, 1, woodd)
c.poly([(77, 87), (86, 77), (95, 87)], roof)
c.line(77, 88, 95, 88, roofl)
c.rect(80, 86, 2, 2, lit)
c.rect(83, 89, 4, 5, dk)
c.rect(88, 79, 3, 6, brick)
c.rect(87, 78, 5, 1, brickd)

# smoke plumes (three thin streams, drifting right)
def puff(x, y, r, col):
    c.circle(x, y, r, C(col))

smoke_a = (198, 198, 198)
smoke_b = (218, 218, 218)
smoke_c = (236, 236, 236)
for (x, y, r, col) in [
    (70, 71, 2, smoke_a), (72, 67, 2, smoke_b), (74, 63, 2, smoke_c),
    (77, 59, 2, smoke_b), (80, 55, 1, smoke_c), (83, 51, 1, smoke_c),
    (37, 76, 2, smoke_a), (35, 72, 2, smoke_b), (33, 68, 2, smoke_c),
    (31, 64, 1, smoke_b),
    (89, 77, 2, smoke_a), (91, 73, 2, smoke_b), (93, 69, 2, smoke_c),
    (95, 65, 1, smoke_c), (97, 61, 1, smoke_c),
]:
    puff(x, y, r, col)

# ------------------------------------------------------------------
# STONE PATH (winding from foreground to the main door)
# ------------------------------------------------------------------
grey_a = C((140, 140, 144))
grey_b = C((118, 118, 124))
grey_c = C((164, 164, 166))
for yy in range(98, 128, 3):
    t = (yy - 98) / 29.0
    x0 = 64 + 3 * math.sin(t * math.pi)
    if yy > 115:
        n, offs = 3, [-4, 1, 6]
    elif yy > 106:
        n, offs = 2, [-3, 3]
    else:
        n, offs = 1, [0]
    for k in range(n):
        sx = max(1, min(126, x0 + offs[k] + random.randint(-1, 1)))
        sy = min(126, yy + random.randint(-1, 1))
        ci = C(random.choice((grey_a, grey_b, grey_c)))
        c.ellipse(sx, sy, random.randint(2, 4), random.randint(1, 2), ci)

# bushes
bush = C((58, 72, 46))
for (bx, by, brx, bry) in [(14, 110, 6, 3), (46, 112, 5, 3), (76, 113, 6, 3),
                          (112, 110, 6, 3), (8, 120, 5, 3), (120, 120, 5, 3)]:
    c.ellipse(bx, by, brx, bry, bush)

# ------------------------------------------------------------------
print(c.stats_text())
finish(c)
