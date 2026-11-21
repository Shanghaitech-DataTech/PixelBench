import math
import random

W = H = 128

# ---------------------------------------------------------------- palette
SKY = ["#150b26", "#1d1032", "#26163f", "#301c4b", "#3a2358", "#452a64"]
SKY_BANDS = [(0, 14), (14, 28), (28, 42), (42, 56), (56, 70), (70, 84)]

STAR_A, STAR_B = "#d6c8ee", "#9a88bc"
MOON, MOON_D, MOON_E = "#f8f0d6", "#e4d7b4", "#cdbd9b"

FAR_TREE, NEAR_TREE = "#241a38", "#1a132c"
GROUND_F, GROUND_N = "#2b2134", "#221a2b"
MOSS_D, MOSS_L = "#2f3a2c", "#3d4a33"

ROOF_L, ROOF_R, ROOF_D = "#2f3b2a", "#44563a", "#212a1e"
MOSS_R1, MOSS_R2 = "#55703f", "#6b8a4a"
WOOD, WOOD_D, WOOD_L = "#4a3a2e", "#3a2d24", "#5d4a39"
STONE, STONE_D, STONE_L = "#4a4654", "#383544", "#5c5868"
WARM, WARM_C, WARM_E = "#ff9f3c", "#ffe7a6", "#c76a26"
FRAME = "#241a16"
DOOR, DOOR_L = "#3a2a22", "#52392a"
SMOKE_A, SMOKE_B = "#4b3f60", "#5e5174"

SLAB, SLAB_L, SLAB_D = "#59545f", "#6d6773", "#413e4b"
ROPE = "#8a8270"

BARK, BARK_L, BARK_D = "#2c2030", "#3e2f3c", "#1d1422"
LEAF = ["#4a1b26", "#5c2430", "#3a2340", "#4a3024", "#6b2f33", "#2a1a2a"]
LEAF_HI = "#82413f"

FOG1, FOG2, FOG3 = "#6d5c8a", "#8c7cab", "#a99ac4"
FOG_WARM = "#c98a52"
FIRE_A, FIRE_B = "#ffd27a", "#c9913f"

rnd = random.Random(7)

c = new_canvas(W, H, name="cottage")
fog = new_canvas(W, H, name="fog")


# ---------------------------------------------------------------- helpers
def inb(x, y):
    return 0 <= x < W and 0 <= y < H


def wisp(layer, cx, cy, rx, ry, col, strength=0.6, parity=True):
    """Soft patchy mist cloud: density falls off to the edges."""
    for y in range(int(cy - ry), int(cy + ry) + 1):
        for x in range(int(cx - rx), int(cx + rx) + 1):
            if not inb(x, y):
                continue
            d = ((x - cx) / float(rx)) ** 2 + ((y - cy) / float(ry)) ** 2
            if d > 1.0:
                continue
            p = (1.0 - d) * strength
            if parity and (x + y * 2) % 3 == 0:
                p *= 0.3
            if rnd.random() < p:
                layer.set(x, y, col)


def halo(layer, cx, cy, r0, r1, col, strength=0.55):
    for y in range(cy - r1, cy + r1 + 1):
        for x in range(cx - r1, cx + r1 + 1):
            if not inb(x, y):
                continue
            d = math.hypot(x - cx, y - cy)
            if r0 <= d <= r1:
                p = (r1 - d) / float(r1 - r0)
                if (x + y) % 2 == 0 and rnd.random() < p * strength:
                    layer.set(x, y, col)


def blob(cv, cx, cy, rx, ry, cols, n, r_choices=(1, 1, 2), avoid=None):
    for _ in range(n):
        a = rnd.random() * math.tau
        rr = math.sqrt(rnd.random())
        x = int(round(cx + math.cos(a) * rx * rr))
        y = int(round(cy + math.sin(a) * ry * rr))
        if avoid is not None:
            ax, ay, ar = avoid
            if math.hypot(x - ax, y - ay) < ar:
                continue
        cv.circle(x, y, rnd.choice(r_choices), rnd.choice(cols))


# ---------------------------------------------------------------- sky
for col, (y0, y1) in zip(SKY, SKY_BANDS):
    c.rect(0, y0, W, y1 - y0, col)
for i in range(1, len(SKY)):
    y = SKY_BANDS[i][0]
    c.dither(0, y - 2, W, 4, [SKY[i - 1], SKY[i]], pattern="bayer4")
c.rect(0, 84, W, 6, SKY[5])
c.dither(0, 82, W, 5, [SKY[4], SKY[5]], pattern="bayer4")

# stars
MX, MY, MR = 98, 22, 9
for _ in range(70):
    x = rnd.randrange(W)
    y = rnd.randrange(72)
    if math.hypot(x - MX, y - MY) < MR + 12:
        continue
    c.set(x, y, STAR_A if rnd.random() < 0.4 else STAR_B)

# moon halo (on fog layer so it dithers into the sky)
halo(fog, MX, MY, MR + 1, MR + 14, FOG1, 0.30)
halo(fog, MX, MY, MR + 1, MR + 8, FOG2, 0.40)
halo(fog, MX, MY, MR + 1, MR + 4, FOG3, 0.55)

# moon
c.circle(MX, MY, MR, MOON)
c.circle(MX + 3, MY + 3, 2, MOON_D)
c.circle(MX - 4, MY - 2, 1, MOON_D)
c.circle(MX + 1, MY - 5, 1, MOON_E)
c.circle(MX - 2, MY + 5, 1, MOON_E)
c.set(MX + 5, MY - 2, MOON_D)


# ---------------------------------------------------------------- forest
def conifer(cv, x, base, h, col):
    cv.poly([(x - h // 3 - 2, base), (x, base - h), (x + h // 3 + 2, base)], col)
    cv.rect(x - 1, base - 2, 2, 4, col)


x = -4
while x < W + 6:
    conifer(c, x, 90, rnd.randrange(16, 30), FAR_TREE)
    x += rnd.randrange(7, 12)
x = -6
while x < W + 8:
    conifer(c, x, 97, rnd.randrange(20, 34), NEAR_TREE)
    x += rnd.randrange(9, 15)

# ---------------------------------------------------------------- ground
c.rect(0, 92, W, H - 92, GROUND_F)
c.rect(0, 110, W, H - 110, GROUND_N)
c.dither(0, 106, W, 6, [GROUND_F, GROUND_N], pattern="bayer4")
for _ in range(120):
    x = rnd.randrange(W)
    y = rnd.randrange(94, H)
    col = MOSS_D if rnd.random() < 0.65 else MOSS_L
    c.set(x, y, col)
    if rnd.random() < 0.4:
        c.set(x, y - 1, col)

# ---------------------------------------------------------------- cottage
# walls
c.rect(30, 72, 48, 16, WOOD)
for x in range(31, 78, 5):
    c.line(x, 72, x, 87, WOOD_D)
c.rect(30, 87, 48, 1, WOOD_L)
c.rect(30, 88, 48, 14, STONE)
for y in range(88, 102, 4):
    c.line(30, y, 77, y, STONE_D)
for _ in range(60):
    x = rnd.randrange(30, 78)
    y = rnd.randrange(88, 102)
    c.set(x, y, STONE_L if rnd.random() < 0.5 else STONE_D)
c.line(30, 101, 77, 101, STONE_D)

# warm glow bleeding onto the wall around each window (under the frames)
for (gx, gy, grx, gry) in [(40, 80, 9, 7), (67, 80, 9, 7), (38, 94, 7, 6)]:
    wisp(c, gx, gy, grx, gry, WARM_E, 0.26)

# windows (wood storey)
for wx in (35, 62):
    c.rect(wx, 75, 10, 9, FRAME)
    c.rect(wx + 1, 76, 8, 7, WARM)
    c.rect(wx + 2, 77, 6, 5, WARM_C)
    c.rect(wx + 3, 78, 3, 2, "#fff6d8")
    c.line(wx + 5, 76, wx + 5, 82, FRAME)
    c.line(wx + 1, 79, wx + 8, 79, FRAME)
    c.rect(wx - 1, 84, 12, 1, WOOD_D)
    c.set(wx - 1, 83, WOOD_L)
    c.set(wx + 10, 83, WOOD_L)

# stone window
c.rect(34, 91, 8, 7, FRAME)
c.rect(35, 92, 6, 5, WARM)
c.rect(36, 93, 4, 3, WARM_C)
c.set(37, 94, "#fff6d8")
c.line(38, 92, 38, 96, FRAME)

# door
c.rect(49, 88, 12, 14, FRAME)
c.path("M50 102 L50 93 Q56 86 61 93 L61 102 Z", DOOR)
for x in range(51, 61, 3):
    c.line(x, 90, x, 101, DOOR_L)
c.rect(50, 100, 11, 1, WARM_E)
c.set(59, 96, WARM_C)

# roof (steep; eaves at y=72 so the wooden storey stays visible)
RSL = 36.0 / 34.0
c.poly([(54, 38), (18, 72), (90, 72)], ROOF_L)
c.poly([(54, 38), (54, 72), (90, 72)], ROOF_R)
for y in range(42, 73, 3):
    half = int((y - 38) * RSL)
    c.line(54 - half, y, 54 + half, y, ROOF_D)
c.line(54, 38, 18, 72, ROOF_D)
c.line(54, 38, 90, 72, ROOF_D)
c.rect(18, 72, 73, 2, ROOF_D)
c.line(17, 73, 91, 73, WOOD_D)
blob(c, 28, 66, 9, 4, [MOSS_R1, MOSS_R2], 26, (1, 1))
blob(c, 80, 65, 9, 4, [MOSS_R1, MOSS_R2], 22, (1, 1))
blob(c, 54, 46, 6, 4, [MOSS_R1], 10, (1,))
for _ in range(40):
    y = rnd.randrange(42, 72)
    half = int((y - 38) * RSL) - 1
    if half < 1:
        continue
    x = rnd.randrange(54 - half, 54 + half + 1)
    c.set(x, y, MOSS_R1 if rnd.random() < 0.6 else MOSS_R2)

# gable window in the roof face
c.rect(49, 56, 11, 11, WOOD_D)
c.circle(54, 61, 4, FRAME)
c.circle(54, 61, 3, WARM)
c.circle(54, 61, 2, WARM_C)
c.set(54, 61, MOON)
c.line(50, 61, 58, 61, FRAME)
c.line(54, 57, 54, 65, FRAME)

# chimney
c.rect(68, 46, 9, 16, STONE)
c.rect(67, 44, 11, 3, STONE_L)
for y in range(48, 62, 3):
    c.line(68, y, 76, y, STONE_D)

# smoke
# smoke: broken puffs rising and drifting left
for (sx, sy, sr, sc, sp) in [(72, 40, 3, SMOKE_A, 0.7), (71, 35, 3, SMOKE_A, 0.6),
                             (73, 30, 4, SMOKE_B, 0.5), (70, 24, 4, SMOKE_A, 0.45),
                             (74, 18, 5, SMOKE_B, 0.35), (70, 11, 5, SMOKE_A, 0.28),
                             (75, 5, 6, SMOKE_B, 0.2)]:
    for y in range(sy - sr, sy + sr + 1):
        for x in range(sx - sr - 1, sx + sr + 2):
            if not inb(x, y):
                continue
            d = math.hypot((x - sx) / float(sr + 1), (y - sy) / float(sr))
            if d <= 1.0 and rnd.random() < sp * (1.0 - d * 0.6):
                c.set(x, y, sc)

# ---------------------------------------------------------------- well
c.rect(89, 85, 4, 20, WOOD)
c.rect(108, 85, 4, 20, WOOD)
c.line(89, 85, 92, 104, WOOD_D)
c.line(108, 85, 111, 104, WOOD_D)
c.rect(87, 82, 27, 4, WOOD_L)
c.rect(86, 81, 29, 2, WOOD_D)
c.rect(93, 88, 15, 5, WOOD_L)
c.rect(93, 88, 15, 1, WOOD_D)
c.rect(93, 92, 15, 1, WOOD_D)
c.line(108, 90, 112, 93, WOOD_D)
c.line(100, 93, 100, 101, ROPE)
c.rect(98, 101, 5, 4, WOOD_D)
c.rect(98, 101, 5, 1, ROPE)
c.ellipse(100, 106, 13, 5, STONE)
c.ellipse(100, 105, 10, 3, "#140e1c")
c.rect(88, 106, 25, 7, STONE)
c.ellipse(100, 113, 12, 3, STONE_D)
for _ in range(40):
    x = rnd.randrange(88, 113)
    y = rnd.randrange(103, 115)
    c.set(x, y, STONE_L if rnd.random() < 0.45 else STONE_D)
c.line(88, 106, 88, 112, STONE_D)
c.line(112, 106, 112, 112, STONE_D)

# ---------------------------------------------------------------- rim light
RIM = "#8f84ad"
# moon sits upper-right, so light catches right-facing edges
for y in range(39, 73):
    x = 54 + int((y - 38) * RSL)
    if rnd.random() < 0.8:
        c.set(x, y, RIM)
    if rnd.random() < 0.35:
        c.set(x - 1, y, RIM)
c.line(77, 44, 77, 47, RIM)
c.line(77, 47, 77, 60, "#6d6485")
c.line(112, 82, 114, 83, RIM)
c.line(110, 85, 110, 95, "#6d6485")
for y in range(106, 113):
    if rnd.random() < 0.7:
        c.set(111 + (y > 110), y, "#6d6485")
c.line(76, 88, 76, 100, "#6d6485")

# warm glow bleeding onto the wall around each window

# ---------------------------------------------------------------- path
slabs = [(55, 104, 5, 2), (56, 108, 6, 2), (54, 112, 7, 3), (57, 117, 8, 3),
         (54, 122, 9, 3), (58, 127, 10, 3)]
for (sx, sy, rx, ry) in slabs:
    c.ellipse(sx, sy, rx, ry, SLAB_D)
    c.ellipse(sx, sy, rx - 1, ry, SLAB)
    c.ellipse(sx - 1, sy - 1, rx - 2, max(1, ry - 1), SLAB_L)
    c.ellipse(sx, sy + 1, rx - 2, max(1, ry - 2), SLAB)
# light spill from door onto path: soft fan narrowing with distance
for i, (sy, hw, pr) in enumerate([(102, 7, 0.85), (103, 8, 0.8), (104, 9, 0.7),
                                  (105, 10, 0.6), (106, 11, 0.5), (107, 12, 0.4),
                                  (108, 13, 0.3), (109, 14, 0.22),
                                  (110, 15, 0.16), (111, 16, 0.1)]):
    for x in range(55 - hw, 55 + hw + 1):
        if not inb(x, sy):
            continue
        edge = 1.0 - abs(x - 55) / float(hw + 1)
        if rnd.random() < pr * edge:
            c.set(x, sy, WARM_E if rnd.random() < 0.75 else WARM)


# warm bounce from the cottage onto the near side of the well
for (gx, gy, grx, gry) in [(90, 108, 6, 4), (92, 89, 5, 3)]:
    wisp(c, gx, gy, grx, gry, WARM_E, 0.22)
c.line(89, 86, 89, 96, WARM_E)
c.set(93, 88, WARM_E)

# ---------------------------------------------------------------- big trees
def branch(cv, d, col, col2=None):
    cv.path(d, col, fill=False)
    if col2:
        cv.path(d, col2, fill=False)


# left tree
c.path("M0 128 C6 104 -2 88 8 70 C13 58 8 48 16 38 L28 42 C22 52 24 62 20 74 "
       "C14 94 20 112 18 128 Z", BARK)
c.path("M16 38 C10 48 15 58 10 70 C2 88 9 104 3 128", BARK_D, fill=False)
c.path("M26 44 C22 54 24 64 20 76", BARK_L, fill=False)
branch(c, "M14 48 C26 44 34 36 40 24", BARK)
branch(c, "M14 49 C26 45 34 37 40 25", BARK_D)
branch(c, "M12 60 C24 58 30 50 38 44", BARK)
branch(c, "M16 40 C8 30 10 18 4 10", BARK)
branch(c, "M17 41 C9 31 11 19 5 11", BARK_D)

# right tree
c.path("M127 128 C120 106 128 90 118 74 C112 62 120 52 112 42 L100 46 "
       "C108 56 104 66 110 78 C118 96 112 112 114 128 Z", BARK)
c.path("M112 42 C119 52 112 62 118 74 C127 90 121 106 126 128", BARK_D, fill=False)
c.path("M102 48 C108 58 104 68 110 80", BARK_L, fill=False)
branch(c, "M114 52 C102 48 94 40 86 30", BARK)
branch(c, "M114 53 C102 49 94 41 86 31", BARK_D)
branch(c, "M116 64 C106 62 100 56 92 50", BARK)
branch(c, "M112 44 C120 32 118 20 124 12", BARK)

# canopies
MOON_CLEAR = (MX, MY, MR + 4)
blob(c, 14, 12, 26, 16, LEAF, 150)
blob(c, 40, 4, 18, 9, LEAF, 60)
blob(c, 4, 34, 10, 12, LEAF, 45)
blob(c, 118, 20, 20, 20, LEAF, 130, avoid=MOON_CLEAR)
blob(c, 86, 6, 16, 8, LEAF, 55, avoid=MOON_CLEAR)
for _ in range(60):
    if rnd.random() < 0.5:
        x, y = rnd.randrange(0, 46), rnd.randrange(0, 26)
    else:
        x, y = rnd.randrange(100, 128), rnd.randrange(4, 40)
        if math.hypot(x - MX, y - MY) < MR + 4:
            continue
    c.set(x, y, LEAF_HI)

# ---------------------------------------------------------------- fog
for (fx, fy, frx, fry, fcol, fs) in [
    # low band hugging the treeline behind the cottage
    (8, 90, 26, 5, FOG1, 0.55), (120, 90, 26, 5, FOG1, 0.55),
    (54, 90, 40, 3, FOG1, 0.30),
    # ground drifts to the sides
    (12, 101, 22, 5, FOG2, 0.45), (116, 102, 22, 5, FOG2, 0.40),
    (10, 93, 10, 3, FOG3, 0.40), (118, 93, 10, 3, FOG3, 0.35),
    # faint veil over the foreground earth
    (40, 118, 30, 6, FOG1, 0.22), (96, 120, 28, 6, FOG1, 0.20),
]:
    wisp(fog, fx, fy, frx, fry, fcol, fs)
wisp(fog, 40, 83, 8, 5, FOG_WARM, 0.30)
wisp(fog, 67, 83, 8, 5, FOG_WARM, 0.30)

result = flatten([c, fog], name="result")

# fireflies
for (fx, fy) in [(26, 86), (84, 92), (70, 110), (46, 66), (96, 80), (20, 104),
                 (110, 98), (60, 120), (34, 112)]:
    result.set(fx, fy, FIRE_A)
    result.set(fx + 1, fy, FIRE_B)
    result.set(fx, fy + 1, FIRE_B)

print(result.stats_text())
view(result)
finish(result)
