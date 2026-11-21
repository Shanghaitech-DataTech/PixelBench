from pixelbench_api import *

# ----------------------------------------------------------------------------
# Palette (hex strings register on first use)
# ----------------------------------------------------------------------------
BG       = '#f7f3e8'   # warm paper background
FRAME    = '#cfc7b8'   # chart border
AXIS     = '#4a463f'   # baseline / axis
GRID     = '#e5dfd1'   # light gridlines

APPLE    = '#e23b3b'
APPLE_D  = '#b02828'
BANANA   = '#f2b824'
BANANA_D = '#b8860b'
ORANGE   = '#f28c28'
ORANGE_D = '#c96a10'
LEMON    = '#f8e64a'
LEMON_D  = '#c0a820'
GRAPE    = '#8a4fd0'
GRAPE_D  = '#6a34a8'

LEAF     = '#3faf4f'
BROWN    = '#8a5a20'
WHITE    = '#ffffff'

# ----------------------------------------------------------------------------
# Canvas
# ----------------------------------------------------------------------------
c = new_canvas(128, 64, name='result')
c.rect(0, 0, 128, 64, BG)

# Chart plot area: x 8..120, top y=8, baseline y=48
c.rect(8, 8, 113, 41, FRAME, fill=False)   # thin frame
c.line(8, 48, 120, 48, AXIS)               # baseline

# horizontal gridlines at data values 5 and 10 (scale: 40px for value 14)
c.line(9, 34, 119, 34, GRID)
c.line(9, 19, 119, 19, GRID)

# ----------------------------------------------------------------------------
# Bars
# ----------------------------------------------------------------------------
def bar(cx, h, color, dark):
    x0 = cx - 8
    y1 = 48
    y0 = y1 - h
    c.rect(x0, y0, 16, h, color, fill=True)
    c.rect(x0, y0, 16, h, dark, fill=False)

data = [
    (APPLE,    APPLE_D,  10),   # apple
    (BANANA,   BANANA_D,  5),   # banana
    (ORANGE,   ORANGE_D,  7),   # orange
    (LEMON,    LEMON_D,  14),   # lemon
    (GRAPE,    GRAPE_D,   2),   # grape
]
centers = [20, 42, 64, 86, 108]

for (color, dark, value), cx in zip(data, centers):
    h = round(value * 40 / 14)
    bar(cx, h, color, dark)

# ----------------------------------------------------------------------------
# Mini pixel-art fruit icons (12x12 transparent tiles), drawn below the bars
# ----------------------------------------------------------------------------
def make_apple():
    ic = new_canvas(12, 12)
    ic.circle(6, 7, 4, APPLE, fill=True)
    ic.circle(6, 7, 4, APPLE_D, fill=False)
    ic.ellipse(8, 2, 2, 1, LEAF, fill=True)
    ic.line(6, 1, 6, 3, BROWN)          # stem
    ic.set(4, 5, WHITE)
    ic.set(5, 5, WHITE)
    return ic

def make_banana():
    ic = new_canvas(12, 12)
    ic.circle(6, 6, 5, BANANA, fill=True)
    ic.circle(3, 6, 4, None, fill=True)  # cut the inner arc -> crescent
    ic.set(6, 1, BROWN)                  # tips
    ic.set(6, 11, BROWN)
    return ic

def make_orange():
    ic = new_canvas(12, 12)
    ic.circle(6, 7, 4, ORANGE, fill=True)
    ic.circle(6, 7, 4, ORANGE_D, fill=False)
    ic.ellipse(8, 2, 2, 1, LEAF, fill=True)
    ic.set(4, 5, WHITE)
    ic.set(5, 5, WHITE)
    return ic

def make_lemon():
    ic = new_canvas(12, 12)
    ic.ellipse(6, 7, 5, 3, LEMON, fill=True)
    ic.ellipse(6, 7, 5, 3, LEMON_D, fill=False)
    ic.ellipse(8, 3, 2, 1, LEAF, fill=True)
    ic.set(3, 6, WHITE)
    ic.set(4, 6, WHITE)
    return ic

def make_grape():
    ic = new_canvas(12, 12)
    for (x, y) in [(3, 3), (7, 3), (2, 6), (6, 6), (9, 6), (3, 9), (7, 9)]:
        ic.circle(x, y, 2, GRAPE, fill=True)
    ic.ellipse(6, 1, 1, 1, LEAF, fill=True)
    ic.line(5, 0, 5, 2, BROWN)           # stem
    ic.set(2, 3, WHITE)
    ic.set(6, 3, WHITE)
    return ic

icons = [make_apple(), make_banana(), make_orange(), make_lemon(), make_grape()]
icon_cx = centers
for ic, cx in zip(icons, icon_cx):
    c.blit(ic, cx - 6, 51)

# ----------------------------------------------------------------------------
print(c.stats_text())
finish(c)
