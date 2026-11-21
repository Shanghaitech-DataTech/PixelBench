from pixelbench_api import new_canvas, view, finish

# 32x32 RTS factory icon: compact, blocky, and readable at native size.
c = new_canvas(32, 32, background=None, name="rts_factory")

# Palette
outline = "#202833"
deep = "#303b45"
shadow = "#4a4240"
brick = "#a6533e"
brick_dark = "#7d3d36"
brick_light = "#c56b4c"
mortar = "#d58a61"
roof = "#53616a"
roof_hi = "#71808a"
metal = "#9aa5a3"
metal_hi = "#c4c9bd"
window = "#263f4b"
glow = "#e1a451"
smoke = "#8b9999"

# Ground shadow, with a deliberately squared pixel-art edge.
c.rect(3, 28, 27, 2, outline)
c.rect(6, 30, 21, 1, deep)

# Main brick building silhouette.
c.rect(4, 14, 24, 15, outline)
c.rect(6, 16, 20, 12, brick)

# Brick wall shading and corner piers.
c.rect(6, 16, 3, 12, brick_dark)
c.rect(23, 16, 3, 12, brick_dark)
c.rect(9, 17, 14, 2, brick_light)
c.rect(9, 26, 14, 2, brick_dark)

# Flat roof cap, with a strong clean silhouette.
c.rect(3, 12, 26, 3, outline)
c.rect(5, 11, 22, 2, roof)
c.rect(7, 10, 18, 1, roof_hi)
c.rect(5, 13, 22, 1, roof_hi)

# Chimney stack rising above the roof.
c.rect(21, 4, 7, 9, outline)
c.rect(23, 5, 4, 7, brick_dark)
c.rect(24, 6, 3, 6, brick)
c.rect(20, 3, 9, 2, outline)
c.rect(22, 3, 6, 1, brick_light)
# Chimney lip and small inset highlight.
c.rect(22, 9, 5, 1, brick_light)

# Stepped smoke puffs, kept sparse so the icon remains a building icon.
c.rect(23, 1, 3, 2, smoke)
c.rect(21, 0, 3, 2, smoke)
c.rect(25, 0, 2, 1, smoke)

# Roof vents / skylights.
c.rect(8, 7, 5, 4, outline)
c.rect(9, 8, 3, 2, metal)
c.rect(9, 8, 3, 1, metal_hi)
c.rect(14, 8, 5, 3, outline)
c.rect(15, 9, 3, 1, metal)
# Vent slats.
c.rect(9, 10, 3, 1, deep)
c.rect(15, 10, 3, 1, deep)

# Brick courses and varied block seams.
c.rect(9, 20, 14, 1, brick_dark)
c.rect(9, 24, 14, 1, brick_dark)
c.rect(12, 17, 1, 3, mortar)
c.rect(19, 17, 1, 3, mortar)
c.rect(10, 21, 1, 3, mortar)
c.rect(16, 21, 1, 3, mortar)
c.rect(22, 21, 1, 3, mortar)
c.rect(13, 25, 1, 3, mortar)
c.rect(19, 25, 1, 3, mortar)

# Front loading door with inset frame.
c.rect(12, 19, 9, 10, outline)
c.rect(14, 21, 5, 8, deep)
c.rect(15, 22, 3, 7, window)
c.rect(15, 22, 3, 1, roof_hi)
c.rect(18, 25, 1, 1, glow)
# Door lintel and side bolts.
c.rect(13, 20, 7, 1, metal)
c.rect(13, 21, 1, 7, roof_hi)
c.rect(20, 21, 1, 7, brick_dark)

# Small side windows and warm industrial lights.
c.rect(7, 20, 3, 4, outline)
c.rect(8, 21, 1, 2, window)
c.rect(9, 21, 1, 2, glow)
c.rect(22, 20, 3, 4, outline)
c.rect(23, 21, 1, 2, glow)
c.rect(24, 21, 1, 2, window)

# Base trim and tiny corner bolts.
c.rect(5, 27, 22, 2, outline)
c.rect(7, 27, 18, 1, brick_light)
c.rect(8, 28, 3, 1, metal)
c.rect(21, 28, 3, 1, metal)
c.set(5, 16, metal_hi)
c.set(26, 16, metal_hi)

view(c, scale=16)
finish(c)
