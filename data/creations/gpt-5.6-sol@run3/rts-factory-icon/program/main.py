# 32x32 RTS factory building icon
result = new_canvas(32, 32, background=None, name="rts_factory")

# Palette
outline = result.color("#20252b", "outline")
deep = result.color("#303841", "deep_shadow")
brick_dark = result.color("#7b3832", "brick_dark")
brick = result.color("#a94d3e", "brick")
brick_light = result.color("#c5664e", "brick_light")
mortar = result.color("#d98664", "mortar")
roof_dark = result.color("#3d4850", "roof_dark")
roof = result.color("#58656a", "roof")
metal = result.color("#77858a", "metal")
metal_light = result.color("#a9b1aa", "metal_light")
window = result.color("#65a3a0", "window")
window_light = result.color("#9bc5b8", "window_light")
warning = result.color("#d39a3e", "warning")

# Chimney, behind the main building
result.rect(21, 2, 6, 3, outline)
result.rect(22, 5, 5, 11, outline)
result.rect(22, 5, 4, 10, brick_dark)
result.rect(23, 6, 3, 2, brick_light)
result.rect(23, 10, 3, 2, brick)
result.rect(21, 2, 5, 2, deep)
result.rect(22, 2, 4, 1, metal)

# Main clean silhouette and flat roof
result.rect(3, 12, 25, 17, outline)
result.rect(2, 10, 27, 4, outline)
result.rect(3, 10, 25, 2, roof)
result.rect(4, 10, 23, 1, metal_light)
result.rect(4, 14, 23, 14, brick)
result.rect(4, 14, 23, 2, brick_light)
result.rect(4, 26, 23, 2, brick_dark)

# Rooftop vent unit
result.rect(6, 7, 9, 3, outline)
result.rect(7, 6, 7, 1, outline)
result.rect(7, 7, 7, 2, metal)
result.rect(8, 7, 5, 1, metal_light)
result.set(8, 8, deep)
result.set(10, 8, deep)
result.set(12, 8, deep)

# Brick bonds, sparse and readable
result.line(5, 17, 9, 17, mortar)
result.line(12, 17, 16, 17, mortar)
result.line(19, 17, 25, 17, mortar)
result.line(4, 21, 7, 21, brick_dark)
result.line(10, 21, 14, 21, brick_dark)
result.line(17, 21, 21, 21, brick_dark)
result.line(24, 21, 26, 21, brick_dark)
result.set(10, 16, brick_dark)
result.set(18, 16, brick_dark)
result.set(8, 20, mortar)
result.set(15, 20, mortar)
result.set(22, 20, mortar)
result.set(11, 25, mortar)
result.set(19, 25, mortar)

# Left service door
result.rect(6, 19, 7, 9, outline)
result.rect(7, 20, 5, 8, deep)
result.rect(8, 21, 3, 1, metal)
result.rect(8, 23, 3, 1, metal)
result.rect(8, 26, 3, 2, roof_dark)
result.set(11, 24, warning)

# Twin front vents/windows
for x in (16, 22):
    result.rect(x, 18, 4, 6, outline)
    result.rect(x + 1, 19, 2, 4, window)
    result.set(x + 1, 19, window_light)
    result.set(x + 1, 21, deep)
    result.set(x + 2, 21, deep)

# Base / foundation and small side pipe
result.rect(2, 28, 27, 2, outline)
result.rect(4, 28, 23, 1, roof_dark)
result.rect(27, 18, 2, 8, outline)
result.rect(27, 19, 1, 6, metal)
result.rect(28, 24, 2, 2, outline)
result.set(28, 24, metal_light)

# A few hard highlights for RTS readability
result.set(4, 15, mortar)
result.set(5, 15, brick_light)
result.set(26, 15, brick_dark)
result.set(3, 11, metal_light)

view(result, scale=16, margin=0)
finish(result)
