from pixelbench_api import *

# 64x64 rainy-night convenience store scene
c = new_canvas(64, 64, background="#07131f", name="convenience-store-rainy-night")

# Palette
sky = "#0b1b2d"
sky2 = "#102941"
cloud = "#18364d"
outline = "#050b13"
wall = "#253749"
wall_hi = "#365166"
trim = "#8da9b5"
cyan = "#76cbd0"
rain = "#79a9c4"
rain_hi = "#b0d5de"
cream = "#ffe69a"
light = "#fff3bd"
yellow = "#ffc857"
orange = "#e58b3f"
red = "#b74645"
glass = "#3d7182"
glass_dark = "#244f65"
road = "#101d2a"
road2 = "#152b3a"
puddle = "#285268"
reflect = "#6ca7aa"
white = "#dce9e8"
black = "#081018"
green = "#32746d"
coat = "#d1a43c"
coat_hi = "#f0cb59"
skin = "#b97853"

# Background night sky and distant block silhouettes
c.rect(0, 0, 64, 29, sky)
c.rect(0, 7, 64, 5, sky2)
c.rect(0, 10, 64, 2, cloud)
c.rect(0, 24, 8, 19, "#0a1724")
c.rect(2, 27, 3, 2, "#1b3a4d")

# Store building shadow and body
c.rect(7, 13, 52, 38, outline)
c.rect(8, 14, 50, 35, wall)
c.rect(9, 15, 48, 6, cream)
c.rect(10, 16, 46, 4, light)
# Plain abstract sign marks, no logo/brand
c.rect(14, 17, 12, 1, yellow)
c.rect(29, 17, 9, 1, cyan)
c.rect(41, 17, 10, 1, red)

# Awning / canopy
c.rect(7, 21, 52, 3, outline)
c.rect(8, 21, 50, 2, white)
for x in range(9, 58, 8):
    c.rect(x, 21, 4, 2, red)
c.set(8, 23, wall_hi); c.set(57, 23, wall_hi)

# Warm interior window field
c.rect(10, 25, 46, 22, trim)
c.rect(11, 26, 44, 20, cream)
# glass panes with warm interior
c.rect(12, 27, 13, 18, "#e9c96e")
c.rect(27, 27, 13, 18, "#f5d77f")
c.rect(42, 27, 12, 18, "#e7c66c")
# pane shadows / night reflections
c.rect(12, 27, 13, 3, "#b7c798")
c.rect(27, 27, 13, 3, "#b7cfad")
c.rect(42, 27, 12, 3, "#a9c19d")
c.line(13, 29, 13, 43, glass)
c.line(24, 29, 24, 44, glass_dark)
c.line(28, 29, 28, 44, glass)
c.line(39, 29, 39, 44, glass_dark)
c.line(43, 29, 43, 44, glass)
c.line(53, 29, 53, 44, glass_dark)

# Shelving and colorful products visible through left window
c.rect(14, 32, 9, 1, "#725744")
c.rect(14, 38, 9, 1, "#725744")
for x, col in [(15, red), (17, green), (19, yellow), (21, cyan)]:
    c.rect(x, 30, 1, 2, col)
for x, col in [(14, orange), (16, red), (18, cyan), (20, green), (22, white)]:
    c.rect(x, 35, 2, 3, col)
for x, col in [(15, yellow), (18, green), (21, red)]:
    c.rect(x, 40, 1, 4, col)

# Counter and register behind central glass
c.rect(30, 36, 9, 2, "#79614a")
c.rect(32, 33, 5, 3, glass_dark)
c.rect(33, 33, 3, 1, cyan)
c.rect(29, 38, 10, 5, "#9b784e")
c.rect(30, 39, 8, 1, yellow)

# Door frame, handle, and open dark wedge
c.rect(40, 25, 2, 23, outline)
c.rect(54, 25, 2, 23, outline)
c.rect(42, 26, 12, 20, "#b8d08f")
c.poly([(48, 27), (54, 27), (54, 45), (50, 43)], glass_dark)
c.line(49, 29, 49, 42, trim)
c.rect(50, 35, 1, 4, light)
c.set(51, 36, outline)

# Lower wall base and sidewalk
c.rect(7, 47, 52, 3, outline)
c.rect(8, 47, 50, 2, wall_hi)
c.rect(0, 50, 64, 14, road)
c.rect(0, 50, 64, 2, road2)
c.line(0, 52, 63, 52, "#263b47")

# Umbrella rack beside store
c.rect(8, 39, 6, 2, trim)
c.rect(9, 41, 5, 8, glass_dark)
c.rect(8, 48, 7, 2, outline)
c.line(10, 39, 9, 31, red)
c.path("M9 31 Q11 28 13 31 Q11 30 9 31", red, fill=False)
c.line(12, 39, 13, 33, cyan)
c.path("M11 33 Q13 30 15 33", cyan, fill=False)
c.line(13, 39, 15, 35, yellow)

# Bicycle parked in foreground, outlined for readability
c.circle(19, 51, 6, "#03080d", fill=False)
c.circle(34, 51, 6, "#03080d", fill=False)
c.circle(19, 51, 5, rain_hi, fill=False)
c.circle(34, 51, 5, rain_hi, fill=False)
c.line(19, 51, 25, 43, wall_hi)
c.line(25, 43, 30, 51, wall_hi)
c.line(30, 51, 19, 51, wall_hi)
c.line(25, 43, 27, 51, cyan)
c.line(27, 51, 34, 51, cyan)
c.line(25, 43, 32, 43, wall_hi)
c.line(32, 43, 34, 51, wall_hi)
c.rect(22, 42, 5, 1, black)
c.line(31, 43, 33, 41, trim)
c.line(33, 41, 36, 41, trim)
c.circle(27, 51, 1, yellow)

# Person in yellow raincoat stepping into doorway
# rear leg and boot
c.line(45, 48, 43, 54, outline)
c.line(49, 48, 51, 54, outline)
c.rect(41, 53, 5, 3, black)
c.rect(50, 53, 5, 3, black)
c.line(41, 56, 45, 56, rain_hi)
c.line(51, 56, 55, 56, rain_hi)
# coat silhouette and body
c.poly([(44, 37), (49, 35), (53, 38), (52, 48), (49, 51), (43, 49), (42, 42)], outline)
c.poly([(45, 38), (49, 36), (52, 39), (51, 47), (48, 49), (44, 48), (43, 42)], coat)
c.line(47, 39, 46, 47, coat_hi)
c.line(50, 39, 51, 46, orange)
# head and hood
c.circle(48, 33, 4, outline)
c.circle(48, 33, 3, coat_hi)
c.rect(47, 32, 3, 3, skin)
c.set(50, 33, black)
# arm reaching toward door
c.line(51, 39, 55, 37, outline)
c.line(51, 40, 55, 38, coat)
c.set(55, 37, skin)

# Reflective puddles and broken neon/warm reflections
c.ellipse(31, 59, 24, 3, puddle)
c.ellipse(31, 59, 18, 2, glass_dark)
c.line(10, 57, 23, 57, reflect)
c.line(16, 60, 37, 60, "#4d7d85")
c.line(24, 62, 47, 62, "#335e70")
c.line(43, 56, 57, 56, "#9e7c4c")
c.line(47, 58, 55, 58, yellow)
c.line(12, 55, 18, 55, cyan)
c.line(29, 54, 37, 54, red)
c.rect(20, 53, 2, 5, "#73989a")
c.rect(34, 54, 2, 5, "#9a6d50")
c.rect(52, 52, 2, 4, "#d0a74f")
# Dark breaks through reflections
c.rect(3, 59, 9, 1, road)
c.rect(38, 60, 8, 1, road)
c.rect(56, 58, 7, 1, road)

# Rain streaks, varied lengths and depths
for x, y, length in [(3,3,4),(10,1,3),(17,6,4),(24,2,5),(31,8,3),(39,1,4),(47,5,5),(55,2,3),(61,8,4),
                     (5,17,4),(13,12,3),(21,18,4),(29,13,4),(37,16,3),(46,12,4),(62,18,5),
                     (2,33,4),(16,25,3),(60,28,4),(4,45,3),(61,43,4)]:
    c.line(x, y, x-1, y+length, rain)
for x, y in [(7,5),(27,10),(43,7),(58,14),(2,22),(61,23)]:
    c.line(x, y, x-1, y+2, rain_hi)

# Rain splashes on road
for x, y in [(7,55),(14,62),(40,56),(59,61)]:
    c.line(x-2, y, x+2, y, rain)
    c.set(x, y-1, rain_hi)

# Roof edge highlights and small structural pixels
c.line(8, 14, 57, 14, wall_hi)
c.rect(56, 25, 2, 22, "#172b39")
c.set(9, 49, trim); c.set(57, 49, trim)

view(c, scale=8, margin=0)
finish(c)
