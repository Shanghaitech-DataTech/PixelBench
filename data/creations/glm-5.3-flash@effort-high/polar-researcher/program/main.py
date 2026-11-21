# Polar researcher sprite, 48x48, transparent background
from pixelbench_api import *  # noqa

W = H = 48

# ---------- palette ----------
OUT      = '#1d2130'   # dark outline
PARKA    = '#d95b2e'
PARKA_HI = '#f08050'
PARKA_SH = '#9c3c1d'
FUR      = '#e8dab6'
FUR_SH   = '#c3ac82'
SKIN     = '#f0c49c'
SKIN_SH  = '#cf9a70'
FRAME    = '#262b38'
LENS     = '#a9d9ef'
LENS_HI  = '#eaf7fd'
PANTS    = '#33405c'
PANTS_SH = '#232c42'
BOOT     = '#3c2b1f'
BOOT_HI  = '#5c4330'
SNOW     = '#eef4f9'
CASE     = '#a3b6c0'
CASE_HI  = '#cddae1'
CASE_SH  = '#6f8290'
HANDLE   = '#49545f'
MITT     = '#8e3b3b'
MITT_HI  = '#b05a55'
SCARF    = '#2f8f83'
SCARF_SH = '#1f6a61'
WIND     = '#cfe9f5'
WIND2    = '#9fd0e8'

# ---------- layers ----------
wind = new_canvas(W, H, name='wind')
char = new_canvas(W, H, name='researcher')

# ---------- wind streaks (behind, trailing right) ----------
def streak(c, x0, x1, y, col, gaps=()):
    for x in range(x0, x1 + 1):
        if x not in gaps:
            c.set(x, y, col)

streak(wind, 33, 45, 7, WIND, gaps={39})
streak(wind, 37, 46, 11, WIND2, gaps={42})
streak(wind, 34, 44, 16, WIND, gaps={40, 41})
streak(wind, 38, 47, 22, WIND2, gaps={44})
streak(wind, 35, 46, 27, WIND, gaps={41})
streak(wind, 37, 47, 33, WIND2, gaps={43})
streak(wind, 33, 43, 38, WIND, gaps={38})
streak(wind, 30, 40, 43, WIND2, gaps={35})
# snow flecks whipped up
for (x, y) in [(31, 9), (44, 14), (36, 20), (46, 25), (34, 30), (45, 36), (28, 41), (42, 45)]:
    wind.set(x, y, SNOW)

# ---------- character ----------
# hood (back of head)
char.ellipse(20, 13, 7, 7, PARKA)
char.rect(22, 12, 6, 10, PARKA)          # hood neck into shoulders
# fur trim ring + face
char.ellipse(17, 13, 5, 5, FUR)
char.ellipse(17, 13, 4, 4, SKIN)
char.set(14, 16, SKIN_SH)                # chin shade
# goggles
char.rect(13, 11, 9, 4, FRAME)
char.rect(14, 12, 7, 2, LENS)
char.set(15, 12, LENS_HI)
char.set(16, 12, LENS_HI)
char.set(19, 13, '#7fb8d4')              # lens lower shade
# scarf trailing in the wind
char.line(23, 18, 30, 15, SCARF)
char.line(23, 19, 30, 16, SCARF)
char.line(30, 15, 34, 13, SCARF)
char.line(30, 16, 34, 14, SCARF_SH)
char.line(34, 13, 37, 12, SCARF)
char.line(34, 14, 37, 13, SCARF_SH)

# torso (leaning forward-left)
char.poly([(14, 21), (30, 19), (34, 32), (20, 34)], PARKA)
# highlight along the windward (left) side
char.poly([(15, 22), (20, 21), (23, 33), (20, 34)], PARKA_HI)
# shade along the leeward (right) side
char.poly([(28, 20), (30, 19), (34, 32), (31, 32)], PARKA_SH)
# hem
char.line(20, 33, 34, 31, PARKA_SH)
char.line(20, 34, 34, 32, OUT)

# front arm reaching forward-down toward the case
char.line(17, 23, 12, 29, PARKA)
char.line(18, 24, 13, 30, PARKA)
char.line(16, 22, 11, 28, PARKA_HI)
# back arm bent at the side
char.line(28, 22, 31, 26, PARKA)
char.line(29, 23, 32, 27, PARKA_SH)
# mittens
char.ellipse(10, 30, 2, 2, MITT)
char.set(9, 29, MITT_HI)
char.ellipse(31, 28, 2, 2, MITT)
char.set(30, 27, MITT_HI)

# sample case (held low, in front)
char.rect(3, 30, 12, 8, CASE)
char.line(3, 31, 14, 31, CASE_HI)
char.line(3, 37, 14, 37, CASE_SH)
char.line(14, 31, 14, 37, CASE_SH)
# handle
char.line(7, 28, 10, 28, HANDLE)
char.set(7, 29, HANDLE)
char.set(10, 29, HANDLE)
# latches + stripe
char.set(5, 33, HANDLE)
char.set(12, 33, HANDLE)
char.line(4, 35, 13, 35, SCARF_SH)

# legs: front braced forward, rear trailing back (filled, thick)
char.poly([(21, 31), (26, 32), (21, 42), (16, 42)], PANTS)
char.poly([(21, 31), (24, 32), (19, 42), (16, 42)], PANTS_SH)
char.poly([(28, 31), (32, 32), (38, 41), (34, 42)], PANTS)
char.poly([(28, 31), (30, 32), (36, 41), (34, 42)], PANTS_SH)

# boots
char.rect(11, 41, 8, 5, BOOT)
char.line(11, 42, 18, 42, BOOT_HI)
char.line(11, 45, 18, 45, OUT)
char.rect(32, 41, 8, 5, BOOT)
char.line(32, 42, 39, 42, BOOT_HI)
char.line(32, 45, 39, 45, OUT)
# snow kicked up behind the rear boot
char.set(41, 42, SNOW)
char.set(42, 41, SNOW)
char.set(10, 41, SNOW)

# ---------- outline the character for readability ----------
char.outline(OUT)

# ---------- composite ----------
result = flatten([wind, char], name='polar-researcher')
print(result.stats_text())
print(result.matrix_text())
save('polar-researcher', result, indexed=True)
finish(result)
