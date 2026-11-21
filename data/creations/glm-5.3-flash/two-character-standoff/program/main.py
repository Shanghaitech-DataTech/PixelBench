# -*- coding: utf-8 -*-
# two-character-standoff : 128x128 pixel art, red knight vs green rogue
try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 128
OUTLINE = "#15101c"
DEBUG = False


# ---------------- helpers ----------------
def row_of(segs, width):
    buf = ['.'] * width
    for col, s in segs:
        for i, ch in enumerate(s):
            j = col + i
            if 0 <= j < width:
                buf[j] = ch
    return ''.join(buf)


def build(rows, width, legend, name):
    cv = new_canvas(width, len(rows), name=name)
    for y, r in enumerate(rows):
        assert len(r) == width, "%s row %d: len=%d != %d" % (name, y, len(r), width)
        for x, ch in enumerate(r):
            if ch != '.':
                cv.set(x, y, legend[ch])
    return cv


def rim(cv, dx, dy, colour):
    """1px moonlight rim on the side of the sprite facing the moon."""
    w, h, data = cv.to_rgba()
    hits = []
    for y in range(h):
        base = y * w
        for x in range(w):
            if data[4 * (base + x) + 3] == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and data[4 * (ny * w + nx) + 3] == 0:
                hits.append((x, y))
    for x, y in hits:
        cv.set(x, y, colour)
    return cv


# ---------------- palettes ----------------
KLEG = {
    'R': '#c0392f', 'r': '#7e2420', 'L': '#e8664e', 'H': '#ffd9a0',
    'C': '#8e2430', 'c': '#5c1622', 'G': '#e0b054', 'g': '#9a7430',
    'S': '#b9c6d4', 's': '#6d7a8c', 'W': '#eef4f8', 'E': '#ffd25e',
    'K': '#15101c', 'B': '#5a3a28',
}
RLEG = {
    'g': '#3f8f52', 'd': '#1e4d36', 'K': '#15101c',
    'B': '#5a3a28', 'b': '#3a2418', 'T': '#d8a878', 'M': '#c8d4dc',
    'E': '#a8ff9e', 'G': '#e0b054', 'Y': '#c05038',
}

# ---------------- KNIGHT (40 x 62), facing right ----------------
KN = []
KN.append(row_of([(12, "RRRR")], 40))
KN.append(row_of([(10, "LRRRRRR")], 40))
KN.append(row_of([(8, "LRRRRRRRR")], 40))
KN.append(row_of([(6, "LRRRRRRRRRR")], 40))
KN.append(row_of([(5, "LRRRRRRRRRRR"), (17, "RRGGGGGRR")], 40))
KN.append(row_of([(4, "LRRRRRRRRRRR"), (16, "RRRGGGGGRRRR")], 40))
KN.append(row_of([(4, "LRRRRRRRRRR"), (15, "RRRGGGGGGRRRRR")], 40))
KN.append(row_of([(5, "LRRRRRRRR"), (14, "rRRRRRRRRRRRRRr")], 40))
KN.append(row_of([(6, "LRRRRRRRRRRRRRRRRRRRRRr")], 40))
KN.append(row_of([(7, "LRRRRRRRRRRRRRRKKKKKKr")], 40))
KN.append(row_of([(8, "LRRRRRRRRRRRRRRRKEEKr")], 40))
KN.append(row_of([(9, "LRRRRRRRRRRRRRRKEEKr")], 40))
KN.append(row_of([(15, "rRRRRRRRRKKKKK")], 40))
KN.append(row_of([(16, "rRRRRRRRRRRr")], 40))
KN.append(row_of([(17, "rRRRRRRrrr")], 40))
KN.append(row_of([(19, "ssSSSss")], 40))
KN.append(row_of([(6, "cCCCCcrRRRRRrKKKKKrRRRRRRr")], 40))
KN.append(row_of([(5, "cCCCC"), (10, "rRRRRRRRRr"), (20, "KKKK"), (24, "rRRRRRRRRr")], 40))
KN.append(row_of([(4, "cCCCC"), (9, "rRRRRRRRRRr"), (20, "rRRR"), (24, "rRRRRRRRRRr")], 40))
KN.append(row_of([(3, "cCCCCC"), (9, "rRRRRRRRRRr"), (20, "rGGG"), (24, "rRRRRRRRRRH")], 40))
KN.append(row_of([(2, "cCCCCCC"), (9, "rRRRRRRRRRr"), (20, "GGGG"), (24, "rRRRRRRRRRH")], 40))
KN.append(row_of([(2, "cCCCCCC"), (9, "rRRRRRRRRRr"), (20, "GGGG"), (24, "rRRRRRRRRRH")], 40))
KN.append(row_of([(2, "cCCCCCC"), (9, "rRRRRRRRRr"), (20, "rGGG"), (25, "rRRRRRRRRRH")], 40))
KN.append(row_of([(2, "cCCCCCCC"), (10, "rRRRRRRRRR"), (20, "rRRR"), (24, "rRRRRRRRRr")], 40))
KN.append(row_of([(2, "cCCCCCCCc"), (11, "rRRRRRRr"), (19, "rRRRRRRR"), (27, "rRRRRRH")], 40))
KN.append(row_of([(2, "cCCCCCCCCC"), (12, "rRRr"), (16, "rRRRRRRRRRH"), (28, "rRRRH")], 40))
KN.append(row_of([(2, "cCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (29, "rRRRH")], 40))
KN.append(row_of([(2, "cCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (29, "rRRRRH")], 40))
KN.append(row_of([(1, "cCCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (30, "rRRRH")], 40))
KN.append(row_of([(1, "cCCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (30, "rRRRRH")], 40))
KN.append(row_of([(1, "cCCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (30, "rRRRRH")], 40))
KN.append(row_of([(1, "cCCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (31, "rRRRH")], 40))
KN.append(row_of([(2, "cCCCCCCCCCCc"), (14, "rRRRRRRRRRRRRH"), (31, "GGGG")], 40))
KN.append(row_of([(2, "cCCCCCCCCCCc"), (14, "rRRRRRRRRRRr"), (31, "GGGG")], 40))
KN.append(row_of([(2, "cCCCCCCCCCCc"), (14, "BBBBBBBBBBBBBB"), (31, "BBBB")], 40))
KN.append(row_of([(3, "cCCCCCCCCC"), (14, "rRRRRRRRRRRRRr"), (31, "BBBB")], 40))
KN.append(row_of([(3, "cCCCCCCCCC"), (14, "rRRRRRRRRRRRRr"), (31, "BBBB")], 40))
KN.append(row_of([(3, "cCCCCCCCCC"), (14, "rRRRRRRRRRRRRr"), (30, "GGGGGGGGG")], 40))
KN.append(row_of([(4, "cCCC"), (9, "cCCCC"), (14, "rRRRRRRRRRRRRr"), (33, "WWW")], 40))
KN.append(row_of([(4, "cCCCCCCCCC"), (14, "rRRRRRRRRRRRRr"), (33, "WWW")], 40))
KN.append(row_of([(4, "cC"), (7, "cCCCCCC"), (14, "rRRRRRRRRRRRRr"), (34, "WWW")], 40))
KN.append(row_of([(4, "cCCCCCCCC"), (14, "rRRRRRRRRRRRRr"), (34, "WWW")], 40))
KN.append(row_of([(5, "cC"), (8, "cCCCCC"), (14, "rRRRRRRRRRRRRr"), (34, "WW")], 40))
KN.append(row_of([(6, "cCCCCC"), (14, "rRR"), (18, "rRRRR"), (24, "rRRR"), (35, "WW")], 40))
KN.append(row_of([(16, "rRRRR"), (23, "rRRRH"), (35, "WW")], 40))
KN.append(row_of([(16, "rRRRR"), (23, "rRRRH"), (35, "WW")], 40))
KN.append(row_of([(15, "rRRRr"), (24, "rRRRH"), (35, "WW")], 40))
KN.append(row_of([(15, "rRRRr"), (24, "rRRRH"), (36, "WW")], 40))
KN.append(row_of([(15, "rRRRr"), (24, "rRRRH"), (36, "WW")], 40))
KN.append(row_of([(14, "rRRRr"), (24, "rRRRH"), (36, "WW")], 40))
KN.append(row_of([(14, "rRRRr"), (24, "rRRRH"), (36, "WW")], 40))
KN.append(row_of([(14, "rRRRr"), (24, "rRRRH"), (36, "W")], 40))
KN.append(row_of([(13, "rRRRr"), (25, "rRRRH"), (37, "W")], 40))
KN.append(row_of([(13, "rRRRr"), (25, "rRRRH"), (37, "W")], 40))
KN.append(row_of([(13, "rRRRr"), (25, "rRRRH"), (37, "W")], 40))
KN.append(row_of([(13, "rRRRr"), (25, "rRRRH"), (37, "W")], 40))
KN.append(row_of([(13, "rRRRRR"), (25, "rRRRH"), (37, "W")], 40))
KN.append(row_of([(12, "rRRRRRRR"), (25, "rRRRRRH"), (37, "W")], 40))
KN.append(row_of([(12, "rBBBBBBB"), (25, "rBBBBBH"), (37, "W")], 40))
KN.append(row_of([(12, "rBBBBBBBB"), (25, "rBBBBBBH"), (37, "W")], 40))
KN.append(row_of([(12, "KKKKKKKKK"), (25, "rBBBBBBBB"), (37, "W")], 40))
KN.append(row_of([(25, "KKKKKKKKK"), (37, "W")], 40))

# ---------------- ROGUE (36 x 44), facing left, crouched ----------------
RG = []
# hood + raised dagger
RG.append(row_of([(16, "ddddd"), (33, "MMM")], 36))
RG.append(row_of([(14, "ddgggggdd"), (33, "MMM")], 36))
RG.append(row_of([(12, "ddgggggggggdd"), (32, "MMMM")], 36))
RG.append(row_of([(10, "ddgggggggggggdd"), (32, "MMMM")], 36))
RG.append(row_of([(9, "ddggggggggggggdd"), (31, "ddMMM")], 36))
RG.append(row_of([(8, "ddgggggggggggggdd"), (29, "dggGG")], 36))
RG.append(row_of([(8, "dKKKKKKKggggggggggd"), (28, "dgggggd")], 36))
RG.append(row_of([(8, "dKEEKEEKggggggggggd"), (27, "dgggggd")], 36))
RG.append(row_of([(8, "dKEEKEEKggggggggggd"), (26, "dgggggd")], 36))
RG.append(row_of([(8, "dKKKKKKKgggggggggggd"), (25, "dgggd")], 36))
RG.append(row_of([(9, "dKKKKKggggggggggggd"), (24, "ddd")], 36))
RG.append(row_of([(10, "dggggggggggggggd")], 36))
RG.append(row_of([(11, "dggggggggggggd")], 36))
# shoulders, cloak collar flowing forward
RG.append(row_of([(3, "dgggg"), (7, "ddggggggggggggggdd")], 36))
RG.append(row_of([(1, "dggggg"), (5, "ddggggggggggggggggdd")], 36))
RG.append(row_of([(0, "dggggg"), (4, "ddgggggggggggggggggdd")], 36))
RG.append(row_of([(0, "dgggg"), (4, "dgggggggggggggggggggd")], 36))
RG.append(row_of([(0, "dggg"), (4, "dggggggggggggggggggd")], 36))
# torso, scarf tail behind
RG.append(row_of([(0, "dggg"), (4, "dgggggggggggggggggd"), (22, "ddd")], 36))
RG.append(row_of([(0, "dggg"), (4, "dggggggggggggggggd"), (22, "dgggd")], 36))
RG.append(row_of([(0, "dggg"), (4, "dggggggggggggggggd"), (22, "dgggd")], 36))
RG.append(row_of([(0, "dgg"), (4, "dggggggggggggggggd"), (22, "dggd")], 36))
RG.append(row_of([(1, "TTT"), (4, "dgggggggggggggggd"), (21, "ggd")], 36))
RG.append(row_of([(1, "TTTT"), (5, "dggggggggggggggd"), (20, "dd")], 36))
# hand + vial
RG.append(row_of([(1, "MYYM"), (6, "dggggggggggggd")], 36))
RG.append(row_of([(1, "MYYM"), (6, "dggggggggggd")], 36))
RG.append(row_of([(1, "MMMM"), (6, "dgggggggggd")], 36))
# belt and hips
RG.append(row_of([(5, "bBBBBBBBBBBBBBb")], 36))
RG.append(row_of([(6, "dgggggggggd")], 36))
RG.append(row_of([(5, "ddgggggggggggdd")], 36))
RG.append(row_of([(4, "ddgggggggggggggdd")], 36))
RG.append(row_of([(3, "dgggggggggggggggd")], 36))
RG.append(row_of([(2, "dgggggggggggggggdd")], 36))
# legs in a crouch
RG.append(row_of([(1, "dgggggggg"), (12, "dggggggggg")], 36))
RG.append(row_of([(1, "dggggggg"), (13, "dggggggggg")], 36))
RG.append(row_of([(1, "dggggggg"), (14, "dggggggggg")], 36))
RG.append(row_of([(1, "dgggggg"), (15, "dggggggggg")], 36))
RG.append(row_of([(1, "dggggg"), (16, "dgggggggg")], 36))
RG.append(row_of([(1, "dgggg"), (17, "dgggggggg")], 36))
RG.append(row_of([(1, "dgggg"), (18, "dggggggg")], 36))
RG.append(row_of([(0, "bBBBBBBBBB"), (16, "bBBBBBBBBBB")], 36))
RG.append(row_of([(0, "bBBBBBBBBB"), (16, "bBBBBBBBBBB")], 36))
RG.append(row_of([(0, "bbbbbbbbbb"), (16, "bbbbbbbbbbb")], 36))
RG.append(row_of([(0, "KKKKKKKKKK"), (16, "KKKKKKKKKKK")], 36))

# ---------------- scene ----------------
scene = new_canvas(W, H, background="#0d0b18", name="standoff")

BANDS = [
    (0, 14, "#12112a"),
    (14, 26, "#1d1938"),
    (26, 38, "#2d2250"),
    (38, 50, "#452a5e"),
    (50, 62, "#633463"),
    (62, 74, "#8a4160"),
    (74, 84, "#b5554f"),
    (84, 92, "#dd7a52"),
]
for y0, y1, col in BANDS:
    scene.rect(0, y0, W, y1 - y0, col)
for i in range(len(BANDS) - 1):
    y = BANDS[i][1]
    scene.dither(0, y - 2, W, 4, [BANDS[i][2], BANDS[i + 1][2]], pattern="checker")

# stars in the upper sky
for x, y in [(12, 6), (30, 10), (48, 4), (90, 7), (108, 12), (120, 5), (20, 22),
             (100, 20), (44, 18), (80, 22), (114, 26), (8, 30), (38, 27), (96, 30)]:
    scene.set(x, y, "#e8e4f4")
    if (x + y) % 3 == 0:
        scene.set(x + 1, y, "#b8b2d4")

# clouds / wind streaks
scene.rect(6, 18, 26, 2, "#241f42")
scene.rect(72, 13, 34, 2, "#241f42")
scene.rect(28, 31, 20, 2, "#2b2450")
scene.rect(92, 35, 24, 2, "#2b2450")
scene.rect(2, 44, 18, 2, "#3a2c58")
scene.rect(104, 47, 22, 2, "#3a2c58")
scene.rect(0, 78, 30, 2, "#c96a55")
scene.rect(96, 80, 32, 2, "#c96a55")
scene.rect(18, 85, 26, 2, "#e08a5c")
scene.rect(84, 87, 30, 2, "#e08a5c")

# moon + stepped halo in the gap between the rivals
scene.circle(64, 31, 27, "#332753")
scene.circle(64, 31, 25, "#42305c")
scene.circle(64, 31, 23, "#573a66")
scene.circle(64, 31, 21, "#74486e")
scene.circle(64, 31, 20, "#a06a74")
scene.circle(64, 31, 19, "#f2e6cc")
scene.ellipse(56, 25, 3, 2, "#ddd0b2")
scene.ellipse(71, 36, 4, 3, "#ddd0b2")
scene.ellipse(61, 40, 2, 2, "#ddd0b2")
scene.ellipse(73, 23, 2, 2, "#ddd0b2")
scene.circle(64, 31, 19, "#fffbe8", fill=False)

# horizon glow
scene.ellipse(64, 90, 44, 12, "#e8925c")
scene.ellipse(64, 91, 28, 7, "#ffc07a")

# mountains
scene.poly([(0, 92), (8, 80), (16, 86), (26, 74), (36, 84), (46, 78), (56, 88),
            (66, 80), (76, 88), (86, 76), (96, 86), (106, 78), (116, 88),
            (127, 82), (127, 92), (0, 92)], "#2e2547")
scene.poly([(0, 92), (14, 84), (28, 90), (44, 83), (60, 91), (78, 85), (94, 91),
            (110, 85), (127, 90), (127, 92), (0, 92)], "#221b38")
# ruined pillars on the ridge
scene.rect(22, 76, 3, 12, "#221b38")
scene.rect(99, 79, 3, 10, "#221b38")
scene.rect(24, 74, 7, 2, "#221b38")

# ground
scene.rect(0, 92, W, 36, "#332846")
scene.rect(0, 92, W, 3, "#4a3858")
scene.rect(40, 92, 48, 2, "#6e4a62")
scene.rect(0, 95, W, 5, "#3f3050")
scene.rect(0, 100, W, 8, "#372a48")
scene.rect(0, 108, W, 9, "#2e2340")
scene.rect(0, 117, W, 11, "#271e38")
# paving seams
for x0 in range(0, 128, 16):
    scene.line(x0, 99, min(x0 + 9, 127), 99, "#251c36")
    scene.line(x0 + 5, 106, min(x0 + 14, 127), 106, "#251c36")
    scene.line(x0, 114, min(x0 + 9, 127), 114, "#221a30")
    scene.line(x0 + 8, 122, min(x0 + 17, 127), 122, "#221a30")
for x0, y0 in [(20, 100), (44, 103), (90, 101), (112, 106), (34, 112), (74, 118)]:
    scene.line(x0, y0, x0 - 3, y0 + 6, "#251c36")
# rubble
for x, y, w, h in [(14, 108, 4, 3), (52, 111, 3, 2), (96, 109, 5, 3), (118, 115, 4, 3),
                   (38, 120, 5, 3), (70, 123, 4, 2), (104, 121, 5, 3)]:
    scene.rect(x, y, w, h, "#3d2f4e")
    scene.rect(x, y, w, 1, "#57435f")

# glowing fissure in the gap
fis = [(57, 99), (60, 103), (58, 107), (62, 112), (59, 117), (63, 122), (61, 127)]
for i in range(len(fis) - 1):
    scene.line(fis[i][0], fis[i][1], fis[i + 1][0], fis[i + 1][1], "#1a1226")
    scene.line(fis[i][0] + 1, fis[i][1], fis[i + 1][0] + 1, fis[i + 1][1], "#1a1226")
for i in range(len(fis) - 1):
    scene.line(fis[i][0], fis[i][1], fis[i + 1][0], fis[i + 1][1], "#ff8a4a")
for i in range(0, len(fis), 2):
    scene.set(fis[i][0], fis[i][1], "#ffd25e")
scene.ellipse(61, 108, 9, 7, "#4a2c44")

# contact shadows
scene.ellipse(30, 113, 15, 3, "#1a1426")
scene.ellipse(99, 113, 13, 3, "#1a1426")

# ---------------- characters ----------------
knight = build(KN, 40, KLEG, "knight")
knight.outline(OUTLINE)
rim(knight, 1, 0, "#ffdcac")
scene.blit(knight, 8, 52)

rogue = build(RG, 36, RLEG, "rogue")
rogue.outline(OUTLINE)
rim(rogue, -1, 0, "#cdf0a8")
scene.blit(rogue, 82, 69)

# ---------------- embers in the gap ----------------
embers = [(56, 88), (60, 80), (66, 72), (70, 63), (58, 68), (64, 57), (72, 86),
          (54, 96), (68, 94), (62, 102), (74, 76), (56, 60), (76, 68), (52, 78)]
for i, (x, y) in enumerate(embers):
    scene.set(x, y, "#ffd25e" if i % 2 == 0 else "#ff8a4a")
    if i % 3 == 0:
        scene.set(x, y + 1, "#ff8a4a")

print(scene.stats_text())
save("standoff", scene)
if DEBUG:
    w, h, data = scene.to_rgba()
    px = lambda x, y: (data[4 * (y * w + x)], data[4 * (y * w + x) + 1], data[4 * (y * w + x) + 2])
    print("== COARSE MAP (each char = 4x4 px) ==")
    for by in range(0, h, 4):
        line = []
        for bx in range(0, w, 4):
            rs = gs = bs = br = n = 0
            for y in range(by, min(by + 4, h)):
                for x in range(bx, min(bx + 4, w)):
                    r, g, b = px(x, y)
                    rs += r; gs += g; bs += b; br += max(r, g, b); n += 1
            r, g, b, br = rs // n, gs // n, bs // n, br // n
            if br < 40:
                ch = ' '          # near black
            elif r > g + 30 and r > b + 30:
                ch = 'R'          # red armour
            elif g > r + 20 and g > b + 20:
                ch = 'G'          # green cloak
            elif br > 200:
                ch = '#'          # moon / blade / bright
            elif r > 150 and g > 90 and b < 120:
                ch = 'o'          # warm glow
            elif b >= r:
                ch = '.'          # cool sky / stone
            else:
                ch = ':'
            line.append(ch)
        print(''.join(line))
finish(scene)
