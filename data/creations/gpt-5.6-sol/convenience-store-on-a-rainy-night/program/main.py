from pixelbench_api import *

# 64x64 rainy-night convenience store scene.
c = new_canvas(64, 64, background="#081422", name="convenience_store_rain")

# Palette
sky = "#081422"
sky2 = "#0d2030"
cloud = "#142d3b"
ink = "#071018"
outline = "#101820"
wall = "#243642"
wall_hi = "#3f5360"
roof = "#121e28"
red = "#d94b4d"
red_dark = "#812f39"
cream = "#ffe7a3"
light = "#fff3bd"
yellow = "#ffc95b"
window = "#d9f2c7"
window2 = "#9fd4bd"
teal = "#4f9c9b"
blue = "#367493"
rain = "#77b6c9"
rain_hi = "#b0d8da"
road = "#0b1b26"
road2 = "#102b38"
puddle = "#1c4654"
reflect = "#d7bd74"
white = "#e8f4e6"
coat = "#d7a43b"
coat_dark = "#8e682c"
skin = "#d99a6c"
metal = "#8ca5aa"
green = "#609b63"

# Rainy sky, distant blocks and wires.
c.rect(0, 0, 64, 14, sky)
c.rect(0, 7, 64, 7, sky2)
c.rect(0, 9, 15, 5, cloud)
c.rect(18, 6, 21, 8, cloud)
c.rect(43, 8, 21, 6, cloud)
c.line(0, 10, 63, 4, "#18313d")
c.line(0, 11, 63, 5, "#0a1720")
# Distant building edge and lit windows.
c.rect(0, 13, 9, 28, "#0c1d29")
c.rect(2, 18, 3, 4, "#32505a")
c.rect(2, 27, 3, 5, "#263f4a")
c.rect(6, 16, 2, 7, "#182f3b")

# Store building shell and roof.
c.rect(8, 13, 55, 3, ink)
c.rect(9, 16, 53, 31, wall)
c.rect(7, 15, 56, 3, roof)
c.rect(9, 18, 53, 2, wall_hi)
# Bright fascia, deliberately generic with simple decorative marks.
c.rect(10, 17, 51, 8, cream)
c.rect(10, 17, 51, 2, red)
c.rect(10, 23, 51, 2, red_dark)
c.rect(13, 20, 4, 2, red)
c.rect(19, 20, 2, 2, teal)
c.rect(23, 20, 3, 2, red)
c.rect(47, 20, 10, 2, yellow)

# Window bays, frames and warm interior.
c.rect(10, 25, 50, 22, outline)
c.rect(12, 27, 14, 17, light)
c.rect(28, 27, 14, 17, window)
c.rect(44, 27, 14, 20, "#bce4c1")
# Golden light fall at base.
c.rect(11, 42, 47, 3, yellow)
c.rect(12, 45, 46, 2, "#b47e37")
# Window mullions and sill.
for x in (26, 42, 58):
    c.rect(x, 25, 2, 22, outline)
c.rect(10, 44, 50, 2, outline)

# Interior shelves and products seen through glass.
c.rect(13, 30, 11, 2, "#bb6a45")
c.rect(13, 36, 11, 2, "#6e8e77")
c.rect(14, 28, 2, 2, red)
c.rect(18, 28, 3, 2, green)
c.rect(22, 28, 2, 2, blue)
for x, col, h in [(14, red, 3), (17, teal, 4), (20, yellow, 3), (23, green, 4)]:
    c.rect(x, 33, 2, h, col)
for x, col, h in [(30, red, 4), (33, yellow, 3), (36, blue, 4), (39, green, 3)]:
    c.rect(x, 34, 2, h, col)
c.rect(29, 32, 12, 2, "#466e69")
c.rect(29, 39, 12, 2, "#72977b")
# Ceiling lamps and glass shine.
c.rect(16, 27, 7, 1, white)
c.rect(31, 27, 8, 1, white)
c.line(13, 28, 13, 38, "#fff7d1")
c.line(30, 28, 30, 34, "#f1ffe0")
c.line(32, 28, 29, 36, "#d7f1d2")

# Door details at right.
c.rect(44, 27, 14, 20, "#31515a")
c.rect(46, 29, 10, 16, window2)
c.rect(46, 29, 10, 2, "#e4f7cb")
c.rect(44, 27, 2, 20, ink)
c.rect(56, 27, 2, 20, ink)
c.rect(53, 36, 2, 1, yellow)
c.rect(47, 32, 5, 3, white)
c.rect(48, 33, 3, 1, red)
# Door opening, dark wedge behind entering person.
c.poly([(44, 28), (48, 30), (48, 46), (44, 46)], "#183139")
c.line(45, 29, 45, 45, "#527879")

# Side wall and drainpipe.
c.rect(60, 20, 3, 29, "#152630")
c.rect(61, 22, 1, 26, metal)
c.rect(60, 48, 4, 2, ink)

# Pavement and curb.
c.rect(0, 47, 64, 6, "#26353a")
c.line(0, 48, 63, 48, "#597077")
c.line(0, 52, 63, 52, "#101b22")
c.rect(0, 53, 64, 11, road)
c.rect(0, 55, 64, 9, road2)
# Pavement seams.
c.line(3, 52, 12, 47, "#18272d")
c.line(26, 52, 29, 47, "#18272d")
c.line(52, 52, 50, 47, "#18272d")

# Light spill and broken reflections.
c.poly([(11, 47), (57, 47), (61, 54), (4, 54)], "#3b4c43")
c.rect(7, 51, 16, 2, "#7b7146")
c.rect(27, 49, 16, 2, "#a38c50")
c.rect(47, 51, 13, 2, "#756743")
c.rect(11, 55, 18, 2, puddle)
c.rect(5, 57, 29, 3, puddle)
c.rect(9, 60, 20, 2, "#173d4b")
c.rect(36, 55, 23, 2, "#1f4e59")
c.rect(32, 58, 28, 3, puddle)
c.rect(39, 61, 17, 2, "#183f4c")
# Store colors reflected in puddles.
c.rect(14, 55, 8, 1, reflect)
c.rect(10, 57, 16, 1, "#9a854d")
c.rect(17, 59, 10, 1, "#615f45")
c.rect(41, 56, 11, 1, "#8d7b4b")
c.rect(36, 58, 8, 1, "#d5a34c")
c.rect(46, 59, 12, 1, "#6e704d")
c.rect(38, 61, 8, 1, "#49675d")

# Umbrella rack outside left window.
c.rect(10, 39, 12, 2, ink)
c.rect(11, 41, 10, 6, "#263943")
c.rect(12, 45, 8, 2, "#101b22")
c.line(13, 32, 13, 44, red)
c.poly([(10, 34), (13, 31), (16, 34)], red, fill=True)
c.line(16, 33, 16, 44, teal)
c.poly([(13, 35), (16, 32), (19, 35)], teal, fill=True)
c.line(19, 34, 19, 44, yellow)
c.poly([(17, 36), (19, 33), (22, 36)], yellow, fill=True)

# Bicycle in foreground: wheels, frame, bars, seat.
c.circle(28, 53, 6, ink, fill=False)
c.circle(47, 53, 6, ink, fill=False)
c.circle(28, 53, 5, metal, fill=False)
c.circle(47, 53, 5, metal, fill=False)
# sparse spokes
for ex, ey in [(28,48),(28,58),(23,53),(33,53)]: c.line(28,53,ex,ey,"#45616a")
for ex, ey in [(47,48),(47,58),(42,53),(52,53)]: c.line(47,53,ex,ey,"#45616a")
# frame triangle and fork
c.line(28, 53, 34, 45, blue)
c.line(34, 45, 40, 53, blue)
c.line(40, 53, 28, 53, blue)
c.line(34, 45, 36, 53, blue)
c.line(36, 53, 47, 53, blue)
c.line(43, 44, 47, 53, metal)
c.line(42, 43, 45, 43, metal)
c.line(43, 43, 43, 46, metal)
c.rect(31, 43, 5, 2, ink)
c.circle(36, 53, 1, yellow)

# Person in hooded yellow raincoat stepping through doorway.
c.circle(47, 33, 3, coat_dark)
c.poly([(44, 35), (49, 34), (52, 43), (49, 47), (43, 47), (42, 41)], coat)
c.rect(45, 34, 4, 2, coat)
c.set(46, 34, skin)
c.line(43, 38, 40, 43, coat_dark)
c.line(50, 38, 53, 41, coat_dark)
c.rect(44, 46, 3, 5, outline)
c.rect(49, 46, 3, 4, outline)
c.rect(43, 50, 4, 2, ink)
c.rect(49, 49, 4, 2, ink)
# wet highlights on coat
c.line(45, 37, 44, 44, "#f0c459")
c.line(48, 36, 50, 42, "#b88631")

# Rain streaks, varied and interrupted around focal silhouettes.
for x, y in [(3,2),(11,5),(28,1),(39,7),(52,2),(61,9),(5,24),(7,34),(24,8),(34,4),(45,9),(56,6),(2,43),(25,25),(39,22),(62,32),(23,46),(56,49),(4,54)]:
    c.line(x, y, x-2, y+5, rain)
for x, y in [(16,3),(33,10),(48,4),(59,16),(6,15),(37,17),(22,13),(63,3)]:
    c.line(x, y, x-1, y+3, rain_hi)
# Rain splashes on street.
c.line(1, 58, 4, 58, rain)
c.set(2,57,rain_hi)
c.line(27, 62, 31, 62, rain)
c.set(29,61,rain_hi)
c.line(58, 54, 62, 54, rain)
c.set(60,53,rain_hi)
c.line(2, 50, 5, 50, rain_hi)

view(c, scale=8, margin=0)
finish(c)
