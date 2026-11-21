import random
from pixelbench_api import new_canvas, view, save, finish

W = H = 32
c = new_canvas(W, H, name="camera")

# ---------------- palette ----------------
OUT      = '#17141f'   # dark outline
PLATE_HI = '#e2e7f1'   # top plate highlight
PLATE    = '#b4bdce'   # top plate mid
PLATE_SH = '#7c8699'   # top plate shadow
PLATE_DK = '#525c6e'   # deep metal shade
LEA_HI   = '#71563b'   # leather highlight
LEA      = '#4e3a29'   # leather mid
LEA_DK   = '#33261b'   # leather shadow
METAL    = '#a9b1c1'   # lens barrel ring light
METAL_SH = '#6a7283'   # lens barrel ring shade
BARREL   = '#3b4253'   # inner barrel
GLASS_DK = '#152c40'   # glass edge
GLASS    = '#2a6b8c'   # glass mid
GLASS_LT = '#5cbad6'   # glass highlight
SPEC     = '#eaf9ff'   # specular
RED      = '#c34a3c'   # accent red
BRASS    = '#d8a441'   # accent brass
VWIN     = '#274159'   # viewfinder glass
VWIN_LT  = '#7fb2cc'   # viewfinder glint

# ---------------- body silhouette ----------------
BX0, BY0, BX1, BY1 = 2, 6, 29, 29
c.rect(BX0, BY0, BX1 - BX0 + 1, BY1 - BY0 + 1, OUT)
# interior
c.rect(BX0 + 1, BY0 + 1, BX1 - BX0 - 1, BY1 - BY0 - 1, PLATE)
# rounded corners
for (x, y) in [(BX0, BY0), (BX1, BY0), (BX0, BY1), (BX1, BY1)]:
    c.set(x, y, None)
for (x, y) in [(BX0 + 1, BY0 + 1), (BX1 - 1, BY0 + 1),
               (BX0 + 1, BY1 - 1), (BX1 - 1, BY1 - 1)]:
    c.set(x, y, OUT)

# ---------------- top plate (rows 7..12) ----------------
c.rect(3, 7, 26, 6, PLATE)
c.rect(4, 7, 24, 2, PLATE_HI)      # bright top edge
c.rect(3, 11, 26, 1, PLATE_SH)     # lower shade
c.rect(3, 12, 26, 1, PLATE_DK)     # seam
# vertical form shading
c.rect(27, 7, 2, 6, PLATE_SH)
c.set(28, 7, OUT); c.set(28, 12, OUT)
c.set(3, 7, OUT); c.set(28, 7, OUT)

# ---------------- leatherette body (rows 13..28) ----------------
c.rect(3, 13, 26, 16, LEA)
c.rect(3, 13, 26, 1, LEA_DK)       # shadow under top plate
c.rect(3, 27, 26, 2, LEA_DK)       # base shade
rnd = random.Random(11)
for y in range(14, 27):
    for x in range(3, 29):
        r = rnd.random()
        if r < 0.13:
            c.set(x, y, LEA_HI)
        elif r < 0.28:
            c.set(x, y, LEA_DK)
# side form shading on leather
for y in range(14, 27):
    c.set(28, y, LEA_DK)
    c.set(3, y, LEA_HI if (y % 2 == 0) else LEA)
c.set(3, 28, OUT); c.set(28, 28, OUT)

# ---------------- top-deck accessories ----------------
# rewind knob (left)
c.rect(5, 3, 5, 4, OUT)
c.rect(6, 4, 3, 2, PLATE)
c.set(6, 4, PLATE_HI)
c.set(8, 5, PLATE_SH)
# hot shoe / accessory mount (centre)
c.rect(14, 4, 5, 3, OUT)
c.rect(15, 5, 3, 1, PLATE_DK)
c.set(15, 5, PLATE_SH)
# shutter button (right of centre) - red soft release
c.rect(21, 2, 5, 5, OUT)
c.rect(22, 3, 3, 3, RED)
c.rect(22, 3, 3, 1, '#e06a55')
c.set(23, 5, '#8f332a')
# film advance lever (far right)
c.rect(26, 4, 4, 3, OUT)
c.rect(27, 5, 2, 1, PLATE_SH)

# ---------------- front windows on the top plate ----------------
# viewfinder (right)
c.rect(21, 8, 6, 4, OUT)
c.rect(22, 9, 4, 2, VWIN)
c.set(22, 9, VWIN_LT); c.set(23, 9, VWIN_LT)
# rangefinder window (left)
c.rect(6, 8, 5, 4, OUT)
c.rect(7, 9, 3, 2, VWIN)
c.set(7, 9, VWIN_LT)
# red self-timer lamp
c.rect(12, 9, 3, 3, OUT)
c.set(13, 10, RED)
# tiny brand marks between windows
c.set(17, 10, PLATE_DK); c.set(18, 10, PLATE_DK); c.set(19, 10, PLATE_DK)

# ---------------- strap lugs ----------------
c.rect(3, 15, 2, 3, OUT)
c.set(3, 16, METAL_SH)
c.rect(27, 15, 2, 3, OUT)
c.set(28, 16, METAL_SH)

# ---------------- lens (per-pixel rings) ----------------
import math
LX, LY = 16, 20
for y in range(LY - 8, LY + 9):
    for x in range(LX - 8, LX + 9):
        dx, dy = x - LX, y - LY
        d = math.hypot(dx, dy)
        if d < 3.2:                                   # glass
            col = GLASS_DK
            if math.hypot(dx + 0.9, dy + 0.9) < 2.3:
                col = GLASS
            c.set(x, y, col)
        elif d < 4.2:                                 # inner dark ring
            c.set(x, y, OUT)
        elif d < 5.6:                                 # ridged focus ring
            a = math.degrees(math.atan2(dy, dx)) % 360
            c.set(x, y, PLATE_DK if int(a // 30) % 2 == 0 else BARREL)
        elif d < 6.9:                                 # metal barrel ring
            c.set(x, y, METAL if (dx + dy) < 0 else METAL_SH)
        elif d < 7.9:                                 # dark outline
            c.set(x, y, OUT)
# glass highlights
c.set(14, 18, SPEC)
c.set(15, 18, GLASS_LT); c.set(14, 19, GLASS_LT)
c.set(18, 22, GLASS)
# metal ring specular, upper-left
c.set(12, 15, PLATE_HI); c.set(13, 14, PLATE_HI); c.set(11, 16, PLATE_HI)
# brass aperture glint on the dark crescent
c.set(18, 19, BRASS)

view(c)
save('retro_film_camera', c, indexed=True)
print(c.stats_text())
finish(c)
