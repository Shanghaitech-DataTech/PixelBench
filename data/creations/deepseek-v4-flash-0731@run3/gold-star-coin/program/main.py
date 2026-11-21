import math
from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16)

RIM = "#8a6420"    # outer rim, dark bronze-gold
GOLD = "#ecc431"   # coin face
STAR = "#9c7416"   # star emblem, darker gold
SHINE = "#f9dd6a"  # small highlight

# Coin body: rim ring + face
c.circle(7, 7, 7, RIM)
c.circle(7, 7, 6, GOLD)

# Five-pointed star in the middle, built as 5 petals + centre pentagon
# so the even-odd fill yields a solid star.
cx, cy = 7.5, 7.5
R, r = 5.0, 2.3
outer = []
inner = []
for i in range(5):
    a = -math.pi / 2 + i * 2 * math.pi / 5
    outer.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for i in range(5):
    a = -math.pi / 2 + math.pi / 5 + i * 2 * math.pi / 5
    inner.append((cx + r * math.cos(a), cy + r * math.sin(a)))

for i in range(5):
    c.poly([outer[i], inner[i], outer[(i + 1) % 5]], STAR)
c.poly(inner, STAR)

# Small highlight on the upper-left of the face
c.circle(6, 5, 1, SHINE)

print(c.stats_text())
print(c.matrix_text())

finish(c)
