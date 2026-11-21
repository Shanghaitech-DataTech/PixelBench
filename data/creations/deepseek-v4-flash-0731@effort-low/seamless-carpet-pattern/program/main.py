from pixelbench_api import *

W = H = 32

# Warm palette
BG_D     = "#69201c"   # deep woven red (dark thread)
BG_L     = "#7c291f"   # woven red (light thread)
GOLD     = "#e2a63b"   # main diamond
GOLDD    = "#b97f1c"   # dark gold edge / accents
CREAM    = "#f6dda4"
CENTER  = "#8f1420"   # deep red center
OUTLINE = "#44130f"   # near black outline

def woven_bg(x, y):
    # diagonal 2px thread weave of two warm reds
    return BG_L if (((x >> 1) + (y >> 1)) & 1) else BG_D

def flower(x, y):
    ex = ((x + 8) // 16) * 16
    ey = ((y + 8) // 16) * 16
    gx = abs(x - ex)
    gy = abs(y - ey)
    fd = gx + gy
    # diagonal + cardinal petals radiate from each grid intersection
    if gx == gy and gx <= 4:
        return CREAM
    if (gx == 0 and gy <= 5) or (gy == 0 and gx <= 5):
        return CREAM
    if fd <= 2:
        return CREAM
    return None

def compute(x, y):
    ux = x % 16
    uy = y % 16
    d = abs(ux - 8) + abs(uy - 8)

    # lozenge diamond: centre -> inner ring -> heart -> gold body -> outline
    if d == 0:
        return CENTER
    if d <= 3:
        return CREAM          # cream heart
    if d <= 5:
        return GOLD           # gold lozenge body
    if d == 6:
        return GOLDD          # dark-gold outline of the lozenge

    # floral rosette petals (corners of each 16-cell)
    f = flower(x, y)
    if f is not None:
        return f

    return woven_bg(x, y)

c = new_canvas(W, H)
for y in range(H):
    for x in range(W):
        c.set(x, y, compute(x, y))

print(c.stats_text())
save("carpet", c)
print(c.matrix_text(region=(0, 0, 31, 31), indices=False))

finish(c)
