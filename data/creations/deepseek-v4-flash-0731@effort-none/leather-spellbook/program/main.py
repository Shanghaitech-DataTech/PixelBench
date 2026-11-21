from pixelbench_api import *

c = new_canvas(32, 32)

DARK = "#1c1208"       # outline
LEATHER_DARK = "#3e2a15"
LEATHER = "#6b4423"
LEATHER_LIGHT = "#8a5a2e"
GOLD = "#d4af37"
GOLD_D = "#8c7018"

# Cover silhouette x=7..25, y=5..27
c.rect(7, 5, 19, 23, DARK)

# Spine
c.rect(9, 6, 3, 21, LEATHER_DARK)

# Cover with shading
c.rect(12, 6, 12, 21, LEATHER)
c.rect(12, 6, 5, 21, LEATHER_DARK)
c.rect(20, 6, 4, 21, LEATHER_LIGHT)

# Gold trim border
c.rect(12, 6, 12, 1, GOLD)
c.rect(12, 26, 12, 1, GOLD)
c.rect(12, 6, 1, 21, GOLD)
c.rect(23, 6, 1, 21, GOLD)

# Spine gold bands
for yy in (8, 12, 16, 20, 24):
    c.rect(9, yy, 3, 1, GOLD)

# Gold corner brackets
def bracket(x, y, vflip, hflip):
    c.rect(x, y, 3, 3, GOLD)
    c.set(x + (0 if not hflip else 2), y + (0 if not vflip else 2), GOLD_D)

bracket(12, 6, False, False)
bracket(21, 6, False, True)
bracket(12, 24, True, False)
bracket(21, 24, True, True)

# Central diamond emblem
c.poly([(17, 12), (20, 15), (17, 18), (14, 15)], GOLD)
c.rect(16, 14, 3, 3, GOLD_D)

finish(c)
