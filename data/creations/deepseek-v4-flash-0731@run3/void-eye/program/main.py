from pixelbench_api import *

c = new_canvas(64, 64, name="void-eye")

def col(spec):
    return c.color(spec)

body_base = col("#2a0e4f")
body_shade = col("#17052e")
body_hi = col("#6d28d9")
iris_deep = col("#4c1d95")
iris_mid = col("#7c3aed")
iris_dark = col("#2e1065")
pupil = col("#f5e9ff")
pupil_glow = col((216, 180, 254, 150))
aura = col((139, 92, 246, 60))
mote = col((196, 181, 253, 130))
shadow_soft = col((10, 3, 20, 55))
shadow_core = col((8, 2, 16, 105))

# faint aura halo behind the eye
c.ellipse(32, 27, 22, 21, aura)

# soft floating shadow
c.ellipse(32, 55, 19, 5, shadow_soft)
c.ellipse(32, 56, 12, 3, shadow_core)

# body (the great eyeball)
c.ellipse(32, 26, 20, 18, body_base)
c.ellipse(32, 38, 17, 9, body_shade)
c.circle(23, 15, 4, body_hi)
c.circle(20, 19, 3, body_hi)
c.circle(18, 23, 2, body_hi)

# tentacles
def tentacle(pts, base_r):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        r = max(1, round(base_r - (base_r - 1) * i / max(1, n - 1)))
        c.circle(x, y, r, body_base)
    x, y = pts[-1]
    c.circle(x, y, 1, body_shade)

# bottom tentacles
tentacle([(17,42),(14,46),(12,50),(11,52)], 4)
tentacle([(24,44),(22,47),(20,50),(19,52)], 4)
tentacle([(32,44),(32,48),(32,51),(32,52)], 4)
tentacle([(40,44),(42,47),(44,50),(45,52)], 4)
tentacle([(47,42),(50,46),(52,50),(53,52)], 4)

# side tentacles
tentacle([(13,30),(10,34),(8,38),(7,41)], 3)
tentacle([(51,30),(54,34),(56,38),(57,41)], 3)

# dark rim for a readable silhouette
c.outline(col("#1a0533"))

# iris
c.circle(32, 28, 11, iris_deep)
c.circle(32, 28, 8, iris_mid)
c.circle(32, 28, 6, iris_dark)

# faintly glowing pupil
c.circle(32, 28, 5, pupil_glow)
c.circle(32, 28, 2, pupil)

# wet glint
c.set(28, 23, pupil)
c.set(29, 23, pupil)
c.set(28, 24, pupil)

# floating motes
for mx, my in [(15, 13), (47, 15), (50, 34), (9, 36)]:
    c.circle(mx, my, 1, mote)

print(c.stats_text())
print(c.matrix_text(region=(6, 4, 58, 58)))
finish(c)
