output = input_canvas.copy(name="output")

# Saturated potion palette, retaining the source liquid's value structure.
dark = output.color("#4c1678", name="potion_dark")
mid_dark = output.color("#7026a8", name="potion_mid_dark")
base = output.color("#9846d6", name="potion_base")
light = output.color("#c070f2", name="potion_light")
glow = output.color("#e3b0ff", name="potion_glow")
shadow = output.color("#32104f", name="potion_shadow")

# Replace only the original water colours, preserving the bottle pixel-for-pixel.
liquid_map = {
    5: dark,    # dark water surface
    6: base,    # main water body
    7: light,
    8: light,
    10: mid_dark,
}
for y in range(64):
    for x in range(64):
        source_colour = input_canvas.get(x, y)
        if source_colour in liquid_map:
            output.set(x, y, liquid_map[source_colour])

# Churning surface: bright foam caps and dark gaps, aligned to the source's 2px grid.
output.rect(12, 26, 6, 2, mid_dark)
output.rect(18, 26, 4, 2, light)
output.rect(22, 26, 8, 2, base)
output.rect(30, 26, 4, 2, glow)
output.rect(34, 26, 6, 2, light)
output.rect(40, 26, 6, 2, mid_dark)
output.rect(16, 28, 4, 2, light)
output.rect(28, 28, 4, 2, mid_dark)
output.rect(38, 28, 4, 2, glow)

# Pixel bubble rings beneath the surface.
def bubble(x, y, size, rim=light, shine=glow):
    output.rect(x + 2, y, size - 4, 2, rim)
    output.rect(x, y + 2, 2, size - 4, rim)
    output.rect(x + size - 2, y + 2, 2, size - 4, mid_dark)
    output.rect(x + 2, y + size - 2, size - 4, 2, mid_dark)
    output.rect(x + 2, y + 2, 2, 2, shine)

bubble(14, 38, 8)
bubble(30, 44, 10)
bubble(40, 34, 6)
bubble(20, 52, 6)

# Small suspended bubbles and glints give the liquid an active magical sparkle.
output.rect(24, 34, 4, 4, mid_dark)
output.rect(24, 34, 2, 2, glow)
output.rect(44, 48, 4, 4, light)
output.rect(44, 48, 2, 2, glow)
output.rect(12, 48, 2, 2, glow)
output.rect(36, 56, 2, 2, glow)

# Bubbles rising through the clear chamber above the potion.
output.rect(22, 20, 4, 4, light)
output.rect(24, 20, 2, 2, glow)
output.rect(28, 14, 2, 2, glow)
output.rect(34, 18, 4, 4, mid_dark)
output.rect(34, 18, 2, 2, light)

view(output, scale=8, margin=0)
finish(output)
