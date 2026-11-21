from pixelbench_api import *

# Transparent 32x32 sprite canvas.
result = new_canvas(32, 32, background=None, name="green-pear")

outline = "#173b24"
stem = "#69452d"
dark = "#2f7d3d"
base = "#55ad45"
light = "#82cf55"
highlight = "#b7e66c"

# Stem and leaf, tucked behind the fruit.
result.rect(16, 2, 2, 7, outline)
result.set(18, 2, outline)
result.set(18, 3, stem)
result.rect(16, 3, 1, 5, stem)
result.set(17, 2, stem)

# Leaf outline and fill.
result.set(19, 3, outline)
result.rect(20, 2, 3, 1, outline)
result.rect(19, 4, 5, 2, outline)
result.rect(20, 6, 3, 1, outline)
result.set(23, 3, outline)
result.set(20, 3, dark)
result.rect(21, 3, 2, 2, dark)
result.rect(20, 4, 2, 2, base)
result.set(22, 5, dark)

# Pear body silhouette: inclusive horizontal spans per row.
spans = {
    7:(14,18), 8:(12,20), 9:(11,21), 10:(10,22),
    11:(9,23), 12:(8,24), 13:(7,25), 14:(6,26),
    15:(5,27), 16:(5,27), 17:(4,28), 18:(4,28),
    19:(4,28), 20:(4,28), 21:(4,28), 22:(4,28),
    23:(5,27), 24:(5,27), 25:(6,26), 26:(7,25),
    27:(8,24), 28:(10,22), 29:(13,19)
}
for y, (x0, x1) in spans.items():
    result.rect(x0, y, x1 - x0 + 1, 1, outline)

# Main green fill, leaving the one-pixel dark contour intact.
inner = {
    8:(14,18), 9:(13,19), 10:(12,20), 11:(11,21),
    12:(10,22), 13:(9,23), 14:(8,24), 15:(7,25),
    16:(6,26), 17:(6,26), 18:(5,27), 19:(5,27),
    20:(5,27), 21:(5,27), 22:(5,27), 23:(6,26),
    24:(6,26), 25:(7,25), 26:(8,24), 27:(10,22),
    28:(13,19)
}
for y, (x0, x1) in inner.items():
    result.rect(x0, y, x1 - x0 + 1, 1, base)

# Cool dark-green shading along the lower-right curve.
shadow_spans = {
    12:(21,22), 13:(22,23), 14:(23,24), 15:(24,25),
    16:(25,26), 17:(25,26), 18:(26,27), 19:(26,27),
    20:(25,27), 21:(24,27), 22:(23,27), 23:(22,26),
    24:(20,26), 25:(19,25), 26:(18,24), 27:(17,22),
    28:(16,19)
}
for y, (x0, x1) in shadow_spans.items():
    result.rect(x0, y, x1 - x0 + 1, 1, dark)

# Broad light plane on the upper-left face.
result.rect(11, 11, 5, 1, light)
result.rect(9, 12, 8, 2, light)
result.rect(8, 14, 8, 3, light)
result.rect(7, 17, 7, 3, light)
result.rect(7, 20, 5, 2, light)
result.set(10, 22, light)

# Small hard-edged specular highlight.
result.rect(10, 12, 3, 2, highlight)
result.rect(9, 14, 3, 3, highlight)
result.rect(8, 16, 2, 2, highlight)
result.set(10, 17, highlight)

view(result, scale=16, margin=0)
finish(result)
