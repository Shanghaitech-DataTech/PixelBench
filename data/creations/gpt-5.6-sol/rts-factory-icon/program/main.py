# 32x32 RTS factory building icon
result = new_canvas(32, 32, background=None, name="rts-factory-icon")

# Restrained industrial palette.
outline = "#202a2c"
deep = "#303a39"
brick_dark = "#713d32"
brick = "#a65743"
brick_light = "#c56c51"
mortar = "#d08a68"
roof_dark = "#465356"
roof = "#657276"
roof_light = "#849195"
metal_dark = "#34464a"
metal = "#5e7478"
metal_light = "#91a5a5"
window = "#23434b"
glass = "#3f7681"
smoke = "#697579aa"

# Soft blocky smoke, detached enough to preserve the chimney silhouette.
result.rect(8, 1, 4, 2, smoke)
result.rect(10, 0, 3, 2, smoke)
result.rect(6, 3, 5, 2, smoke)

# Tall chimney at rear left: dark outline, brick shaft, rim and bands.
result.rect(5, 5, 7, 19, outline)
result.rect(6, 7, 5, 16, brick_dark)
result.rect(7, 7, 3, 16, brick)
result.rect(5, 5, 7, 3, outline)
result.rect(6, 5, 5, 2, roof_dark)
result.rect(7, 6, 3, 1, deep)
result.rect(6, 11, 5, 2, outline)
result.rect(7, 11, 3, 1, mortar)
result.rect(6, 17, 5, 2, outline)
result.rect(7, 17, 3, 1, mortar)
result.rect(7, 8, 1, 3, brick_light)
result.rect(7, 13, 1, 4, brick_light)
result.rect(7, 19, 1, 3, brick_light)

# Main building mass, dark silhouette first.
result.poly([(3,14),(25,14),(29,18),(29,29),(3,29)], outline)

# Flat roof with slight perspective and a bright upper lip.
result.poly([(3,13),(24,13),(29,17),(8,17)], outline)
result.poly([(4,13),(24,13),(27,16),(8,16)], roof)
result.line(5, 13, 23, 13, roof_light)
result.line(8, 16, 27, 16, roof_dark)
result.rect(3, 17, 26, 3, outline)
result.rect(4, 17, 24, 1, roof_light)
result.rect(4, 18, 24, 1, roof_dark)

# Brick walls: brighter front, darker right return.
result.rect(4, 20, 20, 8, brick)
result.poly([(24,20),(28,19),(28,28),(24,28)], brick_dark)
result.rect(4, 27, 24, 2, outline)

# Brick courses and selective highlights, kept sparse for legibility.
result.rect(4, 22, 20, 1, brick_dark)
result.rect(4, 25, 20, 1, brick_dark)
for x in (7, 14, 21):
    result.set(x, 21, brick_light)
for x in (5, 11, 18):
    result.set(x, 24, brick_light)
result.line(5, 20, 22, 20, mortar)

# Large vent bank on facade.
result.rect(6, 20, 8, 7, outline)
result.rect(7, 21, 6, 5, metal_dark)
result.rect(8, 21, 4, 1, metal_light)
for y in (22, 24):
    result.line(8, y, 12, y, metal)
result.set(7, 25, deep)

# Loading/service door with inset blue-grey panels.
result.rect(16, 20, 7, 8, outline)
result.rect(17, 21, 5, 6, window)
result.rect(18, 21, 3, 2, glass)
result.line(17, 24, 21, 24, metal)
result.set(21, 26, metal_light)

# Side-wall louver and roof machinery.
result.rect(25, 21, 3, 5, outline)
result.rect(26, 22, 2, 3, metal)
result.set(27, 22, metal_light)
result.rect(17, 10, 7, 4, outline)
result.rect(18, 9, 5, 1, roof_light)
result.rect(18, 10, 5, 3, metal)
result.line(19, 11, 22, 11, metal_light)
result.set(18, 12, metal_dark)

# Ground contact and tiny corner highlights sharpen the strategy-game read.
result.rect(2, 29, 28, 2, outline)
result.rect(5, 29, 21, 1, deep)
result.set(3, 28, brick_light)
result.set(28, 27, roof_light)

view(result, scale=16, margin=0)
finish(result)
