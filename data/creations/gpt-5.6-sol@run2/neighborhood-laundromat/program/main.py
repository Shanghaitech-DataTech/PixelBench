from pixelbench_api import *

# Neighborhood laundromat interior, 64x64.
c = new_canvas(64, 64, background="#142331", name="neighborhood-laundromat")

# Palette
ceiling = "#243746"
ceiling_hi = "#314a5b"
light = "#e7fbff"
light_glow = "#bce7ee"
wall = "#a9c5ca"
wall_hi = "#c9dde0"
tile_line = "#789ca5"
ink = "#172632"
ink2 = "#253d4c"
metal_dark = "#526d77"
metal = "#88a4aa"
metal_hi = "#d6e5e6"
white = "#edf5f3"
teal = "#3db4b2"
teal_hi = "#72d8d1"
blue = "#417b9b"
glass = "#183849"
glass_mid = "#28596c"
glass_hi = "#78cbd0"
red = "#e05b61"
yellow = "#f2c66d"
floor = "#53727c"
floor_hi = "#6e9098"
floor_dark = "#36545f"
basket = "#e2a657"
basket_hi = "#ffd07c"
cloth1 = "#e76575"
cloth2 = "#65c7bd"
cloth3 = "#f4e2a4"

# Ceiling and cool fluorescent fixtures.
c.rect(0, 0, 64, 11, ceiling)
c.rect(0, 9, 64, 2, ceiling_hi)
c.rect(5, 2, 20, 2, light_glow)
c.rect(7, 3, 16, 2, light)
c.rect(33, 2, 20, 2, light_glow)
c.rect(35, 3, 16, 2, light)
c.set(6, 5, "#7faab4").set(52, 5, "#7faab4")

# Upper wall, tiled backsplash, sign and clock.
c.rect(0, 11, 64, 6, wall)
c.rect(0, 11, 64, 1, wall_hi)
for x in range(0, 64, 8):
    c.line(x, 12, x, 16, tile_line)
c.line(0, 16, 63, 16, tile_line)
# Soap dispenser / simple neighborhood detail.
c.rect(3, 12, 18, 4, ink2)
c.text(5, 12, "WASH", light, spacing=0, font="5x7")
# Crop text deliberately into compact sign height; repaint lower wall edge.
c.rect(3, 16, 18, 1, tile_line)
# Clock
c.circle(53, 11, 5, ink)
c.circle(53, 11, 4, white)
c.set(53, 7, ink2).set(57, 11, ink2).set(53, 15, ink2).set(49, 11, ink2)
c.line(53, 11, 53, 8, ink)
c.line(53, 11, 56, 12, ink)
c.set(53, 11, red)

# Machine bank backing and base.
c.rect(1, 17, 62, 35, ink)
c.rect(2, 18, 60, 33, metal_dark)
c.rect(1, 50, 62, 3, ink2)
c.rect(3, 50, 58, 1, metal_hi)

# Five distinct stacked machine columns.
xs = [3, 15, 27, 39, 51]
for i, x in enumerate(xs):
    # Dark separator channel and top machine body.
    c.rect(x, 18, 10, 15, metal)
    c.rect(x + 1, 19, 8, 2, metal_hi)
    c.set(x + 1, 20, teal if i % 2 == 0 else blue)
    c.set(x + 7, 20, red if i == 3 else ink2)
    c.set(x + 8, 20, yellow)
    # Top door: black gasket, steel rim, deep glass.
    c.circle(x + 5, 26, 5, ink)
    c.circle(x + 5, 26, 4, metal_hi)
    c.circle(x + 5, 26, 3, glass)
    c.set(x + 3, 24, glass_hi)
    c.set(x + 4, 24, glass_mid)
    c.set(x + 7, 27, glass_mid)
    # Lower machine.
    c.rect(x, 34, 10, 16, metal)
    c.rect(x + 1, 35, 8, 2, metal_hi)
    c.set(x + 1, 36, blue if i % 2 == 0 else teal)
    c.set(x + 7, 36, red if i == 1 else ink2)
    c.set(x + 8, 36, yellow)
    c.circle(x + 5, 43, 5, ink)
    c.circle(x + 5, 43, 4, metal_hi)
    c.circle(x + 5, 43, 3, glass)
    c.set(x + 3, 41, glass_hi)
    c.set(x + 4, 41, glass_mid)
    c.set(x + 7, 44, glass_mid)
    # Individual dark side and bottom gaps.
    c.rect(x + 10, 18, 2, 32, ink)
    c.rect(x, 32, 10, 2, ink2)
    c.set(x + 1, 49, ceiling_hi)

# Floor with perspective tile lines.
c.rect(0, 53, 64, 11, floor)
c.line(0, 53, 63, 53, floor_hi)
c.line(0, 59, 63, 59, floor_dark)
c.line(11, 53, 7, 63, floor_dark)
c.line(24, 53, 22, 63, floor_dark)
c.line(38, 53, 40, 63, floor_dark)
c.line(53, 53, 59, 63, floor_dark)
c.line(0, 54, 63, 54, "#7899a0")

# Folding table at right foreground, with folded laundry.
c.rect(40, 52, 23, 3, ink)
c.rect(41, 51, 22, 3, metal_hi)
c.rect(42, 50, 10, 2, cloth2)
c.rect(43, 48, 9, 2, cloth3)
c.rect(45, 46, 7, 2, cloth1)
c.set(46, 46, "#ff9aa2").set(49, 48, white)
# Table legs and cross brace.
c.rect(43, 54, 2, 10, metal_dark)
c.rect(59, 54, 2, 10, metal_dark)
c.line(44, 57, 59, 62, metal_dark)
c.line(60, 57, 45, 62, metal_dark)
c.set(43, 63, ink).set(44, 63, ink).set(59, 63, ink).set(60, 63, ink)

# Laundry basket in left foreground: rim, woven slats, handles, clothes.
c.rect(2, 53, 17, 3, ink)
c.rect(3, 52, 15, 3, basket_hi)
c.rect(5, 50, 4, 3, cloth1)
c.rect(8, 49, 5, 4, cloth2)
c.rect(12, 51, 4, 2, cloth3)
c.rect(4, 55, 13, 8, basket)
c.poly([(3, 55), (18, 55), (16, 63), (5, 63)], basket)
c.line(3, 55, 5, 63, ink2)
c.line(18, 55, 16, 63, ink2)
c.line(5, 58, 17, 58, basket_hi)
c.line(5, 61, 16, 61, basket_hi)
for x in (7, 10, 13, 16):
    c.line(x, 56, x - 1, 62, "#b8783c")
# Basket handle arcs in blocky pixel form.
c.line(5, 52, 6, 49, ink2)
c.line(6, 49, 14, 49, ink2)
c.line(14, 49, 16, 52, ink2)
c.set(7, 50, basket_hi).set(14, 51, basket_hi)

# A few crisp specular pixels unify the cool fluorescent ambience.
c.set(0, 17, light_glow).set(63, 17, light_glow)
c.set(23, 55, floor_hi).set(35, 57, floor_hi).set(29, 61, floor_hi)

view(c, scale=8, margin=0)
finish(c)
