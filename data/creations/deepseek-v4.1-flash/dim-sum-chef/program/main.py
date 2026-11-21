from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="result")


def R(x0, y0, x1, y1, col):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, col)


SKIN      = c.color('#f4c9a4', 'skin')
SKIN_SH   = c.color('#d9a077', 'skin_sh')
BLUSH     = c.color('#eda98c', 'blush')
HAIR      = c.color('#33241c', 'hair')
EYE       = c.color('#241a14', 'eye')
MOUTH     = c.color('#b4694f', 'mouth')
HAT       = c.color('#fdfbf6', 'hat')
HAT_SH    = c.color('#dcd8cb', 'hat_sh')
JACKET    = c.color('#d3e2ee', 'jacket')
JACKET_SH = c.color('#a3b9c9', 'jacket_sh')
APRON     = c.color('#f5e3b4', 'apron')
APRON_SH  = c.color('#d3b57e', 'apron_sh')
DUST      = c.color('#ffffff', 'dust')
DUST_SH   = c.color('#cfc7b2', 'dust_sh')
BAM       = c.color('#d98b36', 'bamboo')
BAM_L     = c.color('#f5c47e', 'bamboo_light')
BAM_D     = c.color('#a06428', 'bamboo_dark')
BUN       = c.color('#fffaf0', 'bun')
BUN_SH    = c.color('#e3d0aa', 'bun_sh')
SHOE      = c.color('#4a3a30', 'shoe')

# ---------------- hat ----------------
R(12, 0, 19, 0, HAT)
R(10, 1, 21, 1, HAT)
R(9, 2, 22, 3, HAT)
R(10, 4, 21, 5, HAT)
R(10, 6, 21, 6, HAT_SH)

# ---------------- head ----------------
R(10, 8, 21, 13, SKIN)
R(11, 14, 20, 14, SKIN)
R(13, 15, 18, 15, SKIN)
R(10, 7, 21, 7, HAIR)
R(10, 8, 10, 9, HAIR)
R(21, 8, 21, 9, HAIR)
R(9, 11, 9, 12, SKIN)
R(22, 11, 22, 12, SKIN)
R(13, 10, 14, 11, EYE)
R(17, 10, 18, 11, EYE)
c.set(15, 12, SKIN_SH)
R(15, 13, 16, 13, MOUTH)
R(11, 12, 12, 12, BLUSH)
R(19, 12, 20, 12, BLUSH)

# ---------------- body ----------------
R(9, 16, 22, 16, JACKET)
R(9, 17, 22, 25, JACKET)
R(10, 26, 21, 27, JACKET)
R(9, 17, 9, 25, JACKET_SH)
R(22, 17, 22, 25, JACKET_SH)
R(15, 16, 16, 16, SKIN)

# ---------------- apron ----------------
R(11, 17, 20, 28, APRON)
R(12, 16, 13, 16, APRON)
R(18, 16, 19, 16, APRON)
R(11, 17, 11, 28, APRON_SH)
R(20, 17, 20, 28, APRON_SH)
R(12, 28, 19, 28, APRON_SH)

# ---------------- arms ----------------
R(8, 17, 10, 21, JACKET)
R(21, 17, 23, 21, JACKET)
R(8, 17, 8, 21, JACKET_SH)
R(23, 17, 23, 21, JACKET_SH)

# ---------------- steamer ----------------
R(10, 20, 21, 20, BAM_L)
R(9, 21, 22, 21, BAM)
R(9, 22, 22, 22, BAM_D)
R(11, 23, 20, 23, BAM)
R(11, 24, 20, 24, BAM_D)

# ---------------- buns ----------------
for cx in (12, 16, 20):
    c.set(cx, 17, BUN)
    R(cx - 1, 18, cx + 1, 18, BUN)
    R(cx - 2, 19, cx + 2, 19, BUN)
    c.set(cx, 18, BUN_SH)
c.set(14, 19, BUN_SH)
c.set(18, 19, BUN_SH)
c.set(10, 19, BUN_SH)
c.set(22, 19, BUN_SH)

# ---------------- hands ----------------
R(9, 21, 10, 23, SKIN)
R(21, 21, 22, 23, SKIN)
c.set(9, 21, SKIN_SH)
c.set(22, 21, SKIN_SH)
c.set(9, 23, SKIN_SH)
c.set(22, 23, SKIN_SH)

# ---------------- flour dust ----------------
for (x, y) in [(13, 25), (18, 25), (15, 26), (12, 27), (19, 27), (16, 28)]:
    c.set(x, y, DUST)
for (x, y) in [(14, 26), (17, 27), (9, 18), (22, 19)]:
    c.set(x, y, DUST_SH)

# ---------------- shoes ----------------
R(12, 29, 14, 31, SHOE)
R(17, 29, 19, 31, SHOE)
R(11, 30, 14, 31, SHOE)
R(17, 30, 20, 31, SHOE)

print(c.stats_text())
lines = c.matrix_text().splitlines()
for y, ln in enumerate(lines[1:33]):
    s = ln.strip()
    print(f'{y:2d} {len(s):2d} {s}')

save("dim_sum_chef", c)
finish(c)
