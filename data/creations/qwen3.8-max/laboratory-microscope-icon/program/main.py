"""Laboratory microscope icon - 32x32, three-quarter view, transparent background."""

try:
    from pixelbench_api import new_canvas, view, save, finish
except Exception:  # already preloaded in the main program
    pass

SIZE = 32

# ---------------------------------------------------------------- palette ----
COL = {
    'K': '#131b25',   # outline
    'D': '#2d4157',   # dark shade
    'M': '#56708a',   # mid tone
    'L': '#8ea6bd',   # light
    'H': '#d8e7f5',   # highlight
    'W': '#f3f9fd',   # glass slide white
    'C': '#5ecfe6',   # lens / specimen cyan
    'G': '#e9bb3d',   # objective band (gold)
    'R': '#cf5a44',   # objective band (red)
}

# ------------------------------------------------------------- span map ------
# each row: list of (x0, x1, colour-char), painted in order (later wins)
EYE = [(12, 12, 'K'), (13, 13, 'H'), (14, 15, 'L'), (16, 16, 'M'), (17, 17, 'D'), (18, 18, 'K')]
TUBE = [(12, 12, 'K'), (13, 13, 'H'), (14, 15, 'L'), (16, 16, 'M'), (17, 17, 'D'), (18, 18, 'K')]
PILL = [(23, 23, 'K'), (24, 24, 'L'), (25, 25, 'M'), (26, 26, 'K')]

ROWS = [
    # y0
    [],
    # y1  eyepiece crown
    [(13, 17, 'K')],
    # y2  eyepiece barrel
    EYE,
    # y3
    EYE,
    # y4  barrel shade
    [(12, 12, 'K'), (13, 13, 'L'), (14, 15, 'M'), (16, 17, 'D'), (18, 18, 'K')],
    # y5  head top edge
    [(11, 19, 'K')],
    # y6  head + arm shoulder
    [(10, 10, 'K'), (11, 11, 'H'), (12, 14, 'L'), (15, 17, 'M'), (18, 19, 'D'), (20, 20, 'K'),
     (21, 21, 'K'), (22, 22, 'M'), (23, 23, 'K')],
    # y7  body tube + arm
    TUBE + [(21, 21, 'K'), (22, 22, 'L'), (23, 23, 'M'), (24, 24, 'K')],
    # y8
    TUBE + [(22, 22, 'K'), (23, 23, 'L'), (24, 24, 'M'), (25, 25, 'K')],
    # y9
    TUBE + PILL,
    # y10
    TUBE + PILL,
    # y11 tube bottom shade
    [(12, 12, 'K'), (13, 13, 'L'), (14, 15, 'M'), (16, 17, 'D'), (18, 18, 'K')] + PILL,
    # y12 nosepiece top
    [(9, 9, 'K'), (10, 10, 'L'), (11, 16, 'M'), (17, 19, 'D'), (20, 20, 'K')] + PILL,
    # y13 nosepiece underside
    [(9, 9, 'K'), (10, 10, 'M'), (11, 19, 'D'), (20, 20, 'K')] + PILL,
    # y14 objectives: short (left) + main (centre)
    [(9, 9, 'K'), (10, 10, 'L'), (11, 11, 'M'), (12, 12, 'D'),
     (13, 13, 'K'), (14, 14, 'L'), (15, 15, 'M'), (16, 16, 'K')] + PILL,
    # y15 colour bands
    [(9, 9, 'K'), (10, 12, 'R'),
     (13, 13, 'K'), (14, 15, 'G'), (16, 16, 'K')] + PILL + [(23, 25, 'K')],
    # y16 short objective tip / main barrel + focus knob
    [(10, 10, 'K'), (11, 11, 'C'), (12, 12, 'K'),
     (13, 13, 'K'), (14, 14, 'L'), (15, 15, 'M'), (16, 16, 'K')] + PILL +
    [(22, 22, 'K'), (23, 23, 'H'), (24, 24, 'M'), (25, 25, 'D'), (26, 26, 'K')],
    # y17
    [(13, 13, 'K'), (14, 14, 'L'), (15, 15, 'M'), (16, 16, 'K')] + PILL +
    [(22, 22, 'K'), (23, 23, 'L'), (24, 24, 'M'), (25, 25, 'D'), (26, 26, 'K')],
    # y18
    [(13, 13, 'K'), (14, 14, 'L'), (15, 15, 'M'), (16, 16, 'K')] + PILL +
    [(22, 22, 'K'), (23, 23, 'M'), (24, 25, 'D'), (26, 26, 'K')],
    # y19 main objective lens tip
    [(14, 14, 'K'), (15, 15, 'C'), (16, 16, 'K')] + PILL + [(23, 25, 'K')],
    # y20 stage back edge
    [(8, 22, 'K')] + PILL,
    # y21 stage top face + glass slide with specimen
    [(7, 7, 'K'), (8, 11, 'H'), (12, 13, 'W'), (14, 15, 'C'), (16, 18, 'W'), (19, 21, 'H'),
     (22, 22, 'M')] + PILL,
    # y22 stage top face front + slide
    [(6, 6, 'K'), (7, 10, 'L'), (11, 17, 'W'), (18, 21, 'L'), (22, 22, 'M')] + PILL,
    # y23 stage front face
    [(6, 6, 'K'), (7, 19, 'M'), (20, 22, 'D')] + PILL,
    # y24 stage bottom edge
    [(7, 7, 'K'), (8, 21, 'D'), (22, 22, 'K')] + PILL,
    # y25 under-stage condenser + pillar
    [(14, 14, 'K'), (15, 15, 'D'), (16, 16, 'K')] + PILL,
    # y26 base top face
    [(11, 11, 'K'), (12, 24, 'L'), (25, 25, 'M'), (26, 26, 'K')],
    # y27
    [(9, 9, 'K'), (10, 12, 'H'), (13, 23, 'L'), (24, 25, 'M'), (26, 26, 'D'), (27, 27, 'K')],
    # y28 base front face
    [(8, 8, 'K'), (9, 23, 'M'), (24, 26, 'D'), (27, 27, 'K')],
    # y29
    [(7, 7, 'K'), (8, 22, 'M'), (23, 26, 'D'), (27, 27, 'K')],
    # y30 foot
    [(8, 8, 'K'), (9, 25, 'D'), (26, 26, 'K')],
    # y31
    [],
]

assert len(ROWS) == SIZE, len(ROWS)

grid = [['.'] * SIZE for _ in range(SIZE)]
for y, spans in enumerate(ROWS):
    for x0, x1, ch in spans:
        for x in range(x0, x1 + 1):
            grid[y][x] = ch

print('    ' + ''.join(str(x % 10) for x in range(SIZE)))
for y, r in enumerate(grid):
    print('%3d %s' % (y, ''.join(r)))

c = new_canvas(SIZE, SIZE, name="microscope")
for y, r in enumerate(grid):
    for x, ch in enumerate(r):
        if ch != '.':
            c.set(x, y, COL[ch])

print(c.stats_text())
p = view(c)
print('view:', p)
save("microscope", c)
finish(c)
