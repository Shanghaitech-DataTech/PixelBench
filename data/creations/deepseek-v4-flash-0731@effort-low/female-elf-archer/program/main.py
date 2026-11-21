from pixelbench_api import new_canvas, finish
import math

W = H = 64
g = [['.' for _ in range(W)] for _ in range(H)]

def f(x0, y0, x1, y1, ch):
    for y in range(max(0, y0), min(H - 1, y1) + 1):
        for x in range(max(0, x0), min(W - 1, x1) + 1):
            g[y][x] = ch

def p(x, y, ch):
    if 0 <= x < W and 0 <= y < H:
        g[y][x] = ch

# ===== BACK GEAR (drawn behind) =====
# Bow arc on her back, curving visible on upper right
for y in range(6, 42):
    k = (y - 6) / 35.0
    bx = 42 + (16 * math.sin(math.pi * k))
    p(round(bx), y, 'B')
    p(round(bx) + 1, y, 'B')
    p(round(bx), y + 16, 'B')
# bowstring
f(43, 8, 44, 42, 'Q')
# quiver diagonal across back (upper left)
f(27, 22, 31, 46, 'Q')
f(28, 30, 30, 44, 'q')
# arrows sticking up from quiver
for i in range(18):
    p(27 - i, 20 - i, 'A')
    p(31 - i, 20 - i, 'A')
    if i in (14, 15, 16, 17):
        p(27 - i, 20 - i, 'F')
        p(31 - i, 20 - i, 'F')
# arrowheads
p(8, 2, 'X'); p(12, 2, 'X')

# ===== LONG BACK HAIR =====
f(18, 18, 24, 42, 'H')   # left cascade over back
f(38, 20, 43, 44, 'H')
f(18, 38, 29, 44, 'H')

# ===== HEAD =====
# face (three-quarter, facing viewer-right; far=left side shaded)
f(29, 8, 40, 23, 'S')    # face main
f(29, 23, 39, 24, 's')   # chin+neck
f(31, 24, 38, 29, 'S')
f(27, 11, 28, 20, 's')   # far (left) edge shadow
# RIGHT pointed ear (near side), prominent up-right tip
f(42, 9, 46, 19, 'S')
p(44, 6, 'S'); p(43, 7, 'S'); p(45, 7, 'S')   # tip
p(46, 8, 'S'); p(46, 9, 'S'); p(46, 10, 'S')
p(42, 8, 'S')
f(42, 18, 46, 20, 's')   # ear underside
p(45, 12, 's'); p(45, 14, 's'); p(45, 16, 's')  # inner ear shadow

# ===== OUTFIT =====
f(25, 29, 43, 34, 'G')    # shoulders
f(26, 33, 42, 47, 'G')    # torso
f(27, 47, 41, 51, 'G')
# shading on right side of torso
f(34, 34, 42, 46, 'D')
f(35, 34, 41, 47, 'D')
# left back shading
f(26, 34, 29, 47, 'D')
# belt
f(27, 49, 41, 51, 'I')
# neck shade under chin
f(32, 29, 38, 31, 's')

# ===== ARMS =====
# left arm (viewer left) along back/side
f(23, 30, 25, 41, 'G')
f(23, 42, 26, 47, 'S')
# right arm (viewer right) visible
f(43, 31, 46, 42, 'G')
f(43, 42, 47, 48, 'S')
f(44, 45, 47, 48, 's')

# ===== LEGS & BOOTS =====
f(29, 51, 34, 58, 'S')
f(35, 51, 40, 58, 'S')
f(28, 57, 35, 62, 'b')
f(34, 57, 41, 62, 'b')

# ===== FRONT HAIR =====
# hair cap
f(25, 3, 42, 7, 'H')
# side strands framing face (left side back, right side thin by ear)
f(25, 7, 28, 24, 'H')
f(40, 8, 41, 24, 'H')
f(42, 10, 42, 20, 'H')
# outlines of hair cap add coverage
f(26, 4, 27, 7, 'H')
f(41, 4, 42, 6, 'H')
# part line + highlights
f(30, 4, 33, 5, 'L')
f(26, 8, 28, 14, 'L')
f(39, 3, 40, 5, 'L')

# ===== FACE FEATURES (face turned toward viewer-right) =====
f(31, 14, 33, 17, 'E')   # near eye (her right)
f(36, 14, 38, 17, 'E')   # far eye (her left)
p(32, 16, 'W'); p(37, 16, 'W')
f(31, 11, 34, 12, 'h')   # brows
f(36, 11, 38, 12, 'h')
p(35, 16, 'h')           # nose bridge
p(36, 20, 'N'); p(35, 20, 's')
f(34, 21, 38, 22, 'M')
f(32, 23, 36, 24, 's')   # lower lip area
p(32, 19, 'K')

# ground shadow
f(26, 62, 43, 63, 'q')

# ===== palette =====
pal = {
    'O': (40, 36, 54),
    'S': (255, 214, 175),
    's': (226, 186, 148),
    'H': (96, 190, 96),
    'h': (60, 150, 72),
    'L': (152, 228, 132),
    'G': (168, 226, 158),
    'D': (130, 194, 124),
    'B': (152, 96, 56),
    'b': (104, 62, 34),
    'A': (150, 120, 86),
    'F': (226, 92, 72),
    'X': (202, 208, 220),
    'Q': (160, 120, 86),
    'q': (116, 86, 60),
    'E': (52, 92, 150),
    'W': (235, 240, 245),
    'M': (192, 100, 94),
    'N': (224, 178, 136),
    'K': (240, 190, 160),
    'I': (92, 72, 46),
}

import math

c = new_canvas(W, H, background=None, name="female-elf-archer")
for y in range(H):
    for x in range(W):
        ch = g[y][x]
        if ch != '.' and ch in pal:
            c.set(x, y, pal[ch])

c.outline(pal['O'])
print(c.stats_text())
result = c
finish(result)
