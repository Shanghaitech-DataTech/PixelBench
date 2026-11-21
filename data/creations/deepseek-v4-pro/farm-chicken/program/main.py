from pixelbench_api import *

c = new_canvas(32, 32, name="chicken")

# Warm muted palette
cream = c.color((245, 236, 220), "cream")
cream_dark = c.color((222, 204, 176), "cream_dark")
wing = c.color((208, 182, 148), "wing")
beak = c.color((227, 142, 56), "beak")
leg = c.color((211, 126, 44), "leg")
leg_dark = c.color((188, 108, 38), "leg_dark")
comb = c.color((190, 68, 56), "comb")
wattle = c.color((181, 60, 50), "wattle")
eye = c.color((66, 44, 32), "eye")
outline = c.color((92, 62, 44), "outline")
glint = c.color((255, 250, 240), "glint")

# Plump body (flattened top and bottom so the silhouette outline stays clean)
c.ellipse(16, 17, 9, 7, cream)
c.rect(13, 10, 7, 3, cream)
c.rect(13, 22, 7, 3, cream)

# Tail feathers (overlapping the body so they read as attached)
c.poly([(22, 11), (28, 10), (29, 15), (26, 18), (23, 16)], cream)

# Head
c.circle(10, 9, 4, cream)

# Comb (drawn before the outline so it keeps a dark edge)
c.poly([(6, 7), (6, 4), (7, 3), (8, 4), (9, 3), (10, 4), (11, 3), (12, 4), (13, 4), (13, 7)], comb)

# Wing
c.ellipse(18, 18, 5, 4, wing)

# Belly shading
c.ellipse(16, 22, 4, 1, cream_dark)

# Eye with a tiny glint
c.rect(8, 8, 2, 2, eye)
c.set(8, 8, glint)

# Clean silhouette outline around the main body/head/tail
c.outline(outline)

# Wattle (drawn after the outline so it stays a solid red shape)
c.ellipse(7, 13, 1, 2, wattle)

# Beak (solid orange, more readable than an outlined sliver)
c.poly([(6, 8), (3, 11), (6, 13)], beak)

# Legs and feet (drawn after the outline so they stay orange)
c.rect(20, 24, 2, 4, leg_dark)   # far leg
c.rect(14, 24, 2, 4, leg)        # near leg
c.rect(19, 27, 4, 2, leg_dark)   # far foot
c.rect(12, 27, 4, 2, leg)        # near foot

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
