from pixelbench_api import *

output = input_canvas.copy(name="output")

# Reuse the sprite's dark outline and midtone, and add two cohesive chocolate tones.
outline = output.color("#5e363e", name="melt_outline")
shadow = output.color("#754033", name="melt_shadow")
chocolate = output.color("#94524c", name="melt_chocolate")
highlight = output.color("#ad6250", name="melt_highlight")
shine = output.color("#c8785d", name="melt_shine")

# Irregular melted skirt hanging from the bottom of the scoop.
output.poly([
    (17, 31), (34, 31), (34, 35), (33, 35), (33, 39),
    (32, 40), (30, 40), (29, 39), (29, 36),
    (28, 36), (28, 43), (27, 43), (27, 47), (26, 49),
    (24, 49), (23, 48), (23, 44), (22, 44), (22, 38),
    (21, 38), (21, 41), (20, 43), (18, 43), (17, 41)
], outline)

# Chocolate body, leaving the dark silhouette visible as a one-pixel rim.
output.poly([
    (18, 32), (33, 32), (33, 35), (32, 35), (32, 38),
    (31, 39), (30, 38), (30, 35),
    (27, 35), (27, 42), (26, 42), (26, 47), (25, 48),
    (24, 47), (24, 43), (23, 43), (23, 37),
    (21, 37), (21, 40), (20, 42), (19, 41), (19, 36), (18, 36)
], chocolate)

# Shadow under the scoop and along the left sides of the viscous drips.
output.rect(18, 32, 15, 2, shadow)
output.rect(19, 34, 2, 6, shadow)
output.set(20, 40, shadow)
output.rect(23, 35, 2, 9, shadow)
output.rect(24, 44, 1, 3, shadow)
output.rect(30, 34, 1, 4, shadow)

# Small warm reflections make the coating look wet and actively melting.
output.rect(25, 34, 3, 2, highlight)
output.rect(26, 36, 1, 6, highlight)
output.set(25, 42, highlight)
output.rect(31, 34, 1, 3, highlight)
output.set(26, 34, shine)

view(output, scale=8, margin=0)
finish(output)
