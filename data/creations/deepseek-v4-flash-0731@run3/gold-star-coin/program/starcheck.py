import math
from pixelbench_api import new_canvas

star = new_canvas(16, 16)
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
    star.poly([outer[i], inner[i], outer[(i + 1) % 5]], "#9c7416")
star.poly(inner, "#9c7416")
print(star.matrix_text())
