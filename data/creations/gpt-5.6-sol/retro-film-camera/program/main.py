from pixelbench_api import new_canvas, view, finish

# 32x32 retro film camera item sprite on transparency.
c = new_canvas(32, 32, background=None, name="retro_film_camera")

# Palette
outline = "#211a1b"
deep = "#332326"
shadow = "#4a2c25"
leather_dark = "#603829"
leather = "#845039"
leather_light = "#a66b48"
leather_hi = "#c1865a"
metal_dark = "#5b6263"
metal = "#858b88"
metal_light = "#b9b9ad"
metal_hi = "#ded9c8"
black = "#17191c"
lens_dark = "#24313a"
lens_mid = "#31505c"
lens_blue = "#467484"
lens_glint = "#9cc0b6"
cream = "#e8dfc5"
red = "#b74336"

# Camera silhouette, including viewfinder and top controls.
c.rect(5, 8, 22, 19, outline)
c.rect(7, 6, 7, 3, outline)
c.rect(8, 5, 5, 1, outline)
c.rect(19, 6, 6, 3, outline)
c.rect(21, 5, 3, 1, outline)
c.rect(25, 10, 3, 14, outline)
c.rect(4, 12, 2, 12, outline)

# Main leather body.
c.rect(6, 13, 20, 12, leather)
c.rect(6, 21, 20, 4, leather_dark)
c.rect(7, 14, 18, 2, leather_light)
c.rect(7, 16, 2, 5, leather_dark)
c.rect(23, 16, 2, 7, shadow)
c.rect(7, 24, 18, 1, shadow)

# Fine leather texture, sparse and readable.
for x, y, col in [
    (7,17,leather_hi),(10,15,leather_hi),(21,14,leather_hi),(24,18,leather_light),
    (8,22,shadow),(10,23,leather_light),(12,17,shadow),(20,17,leather_dark),
    (22,23,leather_light),(24,21,leather_dark),(7,19,leather_light),(18,24,leather_light),
    (11,21,leather_dark),(15,15,leather_hi),(19,22,shadow)
]:
    c.set(x, y, col)

# Metal top plate.
c.rect(6, 9, 20, 4, metal_dark)
c.rect(7, 9, 18, 3, metal)
c.rect(8, 9, 16, 1, metal_light)
c.rect(7, 12, 18, 1, shadow)
c.set(7, 10, metal_hi)
c.set(24, 11, metal_dark)

# Raised viewfinder housing.
c.rect(8, 6, 5, 3, metal_dark)
c.rect(9, 6, 4, 2, metal_light)
c.rect(10, 6, 3, 1, metal_hi)
c.rect(9, 8, 4, 1, deep)

# Film advance dial and shutter button.
c.rect(19, 7, 6, 2, metal_dark)
c.rect(20, 6, 4, 2, metal)
c.rect(21, 6, 3, 1, metal_light)
c.rect(22, 5, 2, 1, outline)
c.set(22, 5, red)
c.set(23, 5, metal_hi)

# Small front details: meter window and badge.
c.rect(7, 10, 4, 2, outline)
c.rect(8, 10, 2, 1, lens_blue)
c.set(8, 10, lens_glint)
c.rect(22, 10, 2, 2, outline)
c.set(22, 10, cream)

# Lens mount, chunky concentric pixel rings.
c.rect(10, 14, 12, 10, outline)
c.rect(9, 16, 14, 6, outline)
c.rect(11, 13, 10, 12, outline)
c.rect(10, 15, 12, 8, metal_dark)
c.rect(12, 14, 8, 10, metal_dark)
c.rect(11, 16, 10, 6, metal)
c.rect(13, 15, 6, 8, metal)

# Dark lens glass.
c.rect(12, 17, 8, 4, black)
c.rect(14, 16, 4, 6, black)
c.rect(13, 17, 6, 5, lens_dark)
c.rect(12, 18, 8, 3, lens_dark)
c.rect(14, 17, 4, 4, lens_mid)
c.rect(15, 18, 3, 3, lens_blue)

# Glass reflection and aperture depth.
c.set(14, 17, lens_glint)
c.set(15, 17, "#6f9aa0")
c.set(14, 18, "#588391")
c.set(18, 20, black)
c.set(17, 21, black)
c.set(16, 20, "#24414c")
c.set(15, 18, "#79a5a5")

# Ring highlights/shadows to define cylindrical depth.
c.line(11, 15, 13, 14, metal_light)
c.set(10, 17, metal_light)
c.set(10, 18, metal_hi)
c.set(11, 22, metal_light)
c.line(19, 15, 21, 17, deep)
c.set(21, 20, deep)
c.set(20, 22, deep)
c.set(13, 23, metal_dark)

# Side strap lug and base feet.
c.rect(26, 13, 2, 7, outline)
c.rect(26, 14, 1, 4, metal)
c.set(27, 19, deep)
c.rect(7, 26, 4, 1, outline)
c.rect(21, 26, 4, 1, outline)
c.set(8, 25, metal_dark)
c.set(23, 25, metal_dark)

# Outer silhouette accents and tiny worn edge highlights.
c.set(5, 13, metal_dark)
c.set(5, 14, leather_light)
c.set(26, 11, metal_dark)
c.set(6, 24, shadow)
c.set(25, 24, shadow)
c.set(8, 13, leather_hi)
c.set(24, 13, leather_light)

view(c, scale=16, margin=1, edges="all")
finish(c)
