# Mountain village at sunrise, 128x128 pixel art
result = new_canvas(128, 128, background="#f3a65d", name="mountain-village-sunrise")

# Compact sunrise palette
sky_top = "#5b557f"
sky_mid = "#a76375"
sky_warm = "#df7d63"
sky_gold = "#f3a65d"
sun_edge = "#ffd477"
sun_core = "#ffe9a3"
cloud = "#d88978"
far_mtn = "#6c6680"
far_light = "#8b7180"
mid_mtn = "#48556b"
mid_light = "#687184"
snow = "#c5b9b3"
snow_hi = "#ead4bd"
forest_far = "#344a50"
forest = "#203d3b"
pine_dark = "#162f30"
ground_far = "#41534a"
ground = "#31483e"
ground_dark = "#253a35"
frost = "#879080"
wood_dark = "#4a3029"
wood = "#714434"
wood_light = "#966048"
roof_dark = "#392c2d"
roof = "#59383a"
roof_snow = "#b6aaa0"
stone_dark = "#5b5854"
stone = "#81786d"
stone_light = "#a99a86"
window = "#ffca62"
window_hi = "#fff0a0"
smoke_dark = "#8f7780"
smoke_light = "#b68a86"

# Sky bands
result.rect(0, 0, 128, 15, sky_top)
result.rect(0, 15, 128, 13, sky_mid)
result.rect(0, 28, 128, 15, sky_warm)
result.rect(0, 43, 128, 25, sky_gold)
# Stepped horizon glow
result.rect(42, 35, 45, 15, "#f8b866")
result.rect(50, 29, 29, 19, "#fac474")
# Sparse sky dithering
for y in range(12, 44):
    for x in range((y * 3) % 7, 128, 8):
        if (x + y) % 3 == 0:
            result.set(x, y, sky_mid if y < 27 else sky_warm)
# Thin blocky clouds
result.rect(5, 25, 20, 2, cloud)
result.rect(10, 23, 11, 2, cloud)
result.rect(102, 32, 20, 2, "#d98b74")
result.rect(108, 30, 10, 2, "#d98b74")

# Sunrise disc, partially hidden by the mountains
result.circle(64, 39, 12, sun_edge)
result.circle(64, 38, 8, sun_core)
result.rect(55, 47, 19, 3, sun_edge)

# Distant mountain range
result.poly([(0,55),(12,45),(21,51),(34,35),(49,52),(61,38),(76,51),(91,33),(108,51),(119,42),(127,49),(127,73),(0,73)], far_mtn)
# Warm-facing facets
result.poly([(8,51),(12,45),(21,51),(15,50)], far_light)
result.poly([(25,46),(34,35),(49,52),(36,45)], far_light)
result.poly([(78,48),(91,33),(91,51)], far_light)
result.poly([(109,50),(119,42),(127,49),(127,55)], far_light)
# Snow caps
result.poly([(24,45),(34,35),(44,46),(38,43),(35,47),(32,42),(29,47)], snow_hi)
result.poly([(82,44),(91,33),(101,45),(96,43),(92,46),(89,41),(86,45)], snow)
result.poly([(56,44),(61,38),(68,46),(63,44),(60,47)], snow)

# Midground mountains and lit faces
result.poly([(0,62),(17,48),(31,63),(48,49),(63,67),(81,46),(99,62),(114,52),(127,63),(127,83),(0,83)], mid_mtn)
result.poly([(17,48),(31,63),(20,58)], mid_light)
result.poly([(48,49),(63,67),(50,59)], mid_light)
result.poly([(81,46),(99,62),(84,57)], mid_light)
result.poly([(114,52),(127,63),(117,59)], mid_light)
result.poly([(40,56),(48,49),(55,58),(50,55),(47,59),(45,54)], snow)
result.poly([(72,55),(81,46),(90,57),(84,54),(81,58),(78,52)], snow_hi)

# Distant pine belt
result.rect(0, 72, 128, 18, forest_far)
def tiny_pine(x, y, h, col):
    result.rect(x, y + h - 4, 2, 4, col)
    result.poly([(x+1,y),(x-3,y+7),(x,y+6),(x-5,y+12),(x+7,y+12),(x+2,y+6),(x+5,y+7)], col)
for x, h in [(2,14),(10,18),(19,13),(27,17),(36,12),(43,18),(53,14),(62,17),(72,13),(80,18),(91,15),(101,19),(111,14),(121,18),(126,13)]:
    tiny_pine(x, 75-h, h, forest)

# Village ground
result.poly([(0,82),(20,78),(39,84),(62,78),(84,84),(105,77),(127,81),(127,128),(0,128)], ground_far)
result.poly([(0,94),(22,88),(43,93),(66,87),(89,94),(108,88),(127,92),(127,128),(0,128)], ground)
result.poly([(0,111),(23,103),(49,108),(70,102),(96,109),(127,101),(127,128),(0,128)], ground_dark)
# Frost/sunlit grass clusters
for x,y in [(4,91),(13,99),(29,89),(38,101),(88,89),(101,100),(114,91),(119,110),(8,119),(35,116),(90,119)]:
    result.line(x,y,x+5,y-2,frost)
    result.set(x+2,y-3,frost)

# Stone path behind houses, widening toward viewer
result.poly([(61,82),(70,82),(72,94),(80,106),(91,127),(39,127),(51,108),(58,95)], stone_dark)
result.poly([(63,83),(68,83),(68,94),(75,106),(82,127),(46,127),(55,107),(61,94)], stone)
# Irregular path stones and highlights
stones = [
    (59,96,7,3),(68,99,6,3),(55,105,8,4),(66,107,9,4),(76,113,7,4),
    (49,116,10,4),(62,117,10,4),(73,123,10,4),(46,125,8,3)
]
for x,y,w,h in stones:
    result.rect(x,y,w,h,stone_light)
    result.line(x,y+h,x+w-2,y+h,stone_dark)

# House drawing helper
def house(x, y, w, h, roof_peak, focal=False):
    # shadow and body
    result.rect(x+2, y+2, w, h, wood_dark)
    result.rect(x, y, w, h, wood)
    result.rect(x, y, 3, h, wood_light)
    # horizontal timber courses
    for yy in range(y+5, y+h, 6):
        result.line(x+2, yy, x+w-1, yy, wood_dark)
        for xx in range(x+6, x+w-2, 10):
            result.set(xx, yy-1, wood_light)
    # roof outline and roof
    result.poly([(x-5,y+1),(x+w//2,y-roof_peak-3),(x+w+5,y+1),(x+w+2,y+5),(x-3,y+5)], roof_dark)
    result.poly([(x-3,y),(x+w//2,y-roof_peak),(x+w+3,y),(x+w,y+2),(x,y+2)], roof)
    # snow rim catches sunrise
    result.line(x-2,y-1,x+w//2,y-roof_peak-1,roof_snow)
    result.line(x+w//2,y-roof_peak-1,x+w+3,y-1,roof_snow)
    # door
    dw = 7 if w < 25 else 9
    result.rect(x+w//2-dw//2, y+h-12, dw, 12, wood_dark)
    result.set(x+w//2+2, y+h-6, window)
    # windows
    wy = y+7
    for wx in (x+5, x+w-9):
        result.rect(wx-1, wy-1, 7, 8, wood_dark)
        result.rect(wx, wy, 5, 6, window)
        result.rect(wx+1, wy, 2, 2, window_hi)
        result.line(wx+2,wy,wx+2,wy+5,wood_dark)
        result.line(wx,wy+3,wx+4,wy+3,wood_dark)
    # timber corners
    result.rect(x, y+2, 2, h-2, wood_dark)
    result.rect(x+w-2, y+2, 2, h-2, wood_dark)

# Three houses, central one largest and clearest
house(17, 74, 27, 22, 11)
house(85, 73, 26, 23, 10)
house(48, 65, 34, 29, 14, True)

# Chimneys and drifting smoke (drawn after roofs for crisp silhouettes)
result.rect(29, 61, 5, 12, roof_dark)
result.rect(30, 60, 5, 2, stone_light)
result.rect(96, 60, 5, 12, roof_dark)
result.rect(95, 59, 7, 2, stone_light)
result.rect(70, 47, 6, 15, roof_dark)
result.rect(69, 46, 8, 3, stone_light)
# Pixel-cluster smoke trails
result.rect(72,42,6,4,smoke_dark)
result.rect(75,38,7,5,smoke_dark)
result.rect(79,34,8,5,smoke_light)
result.rect(84,30,7,5,smoke_light)
result.rect(88,27,6,4,smoke_light)
result.rect(31,56,5,4,smoke_dark)
result.rect(34,52,7,5,smoke_light)
result.rect(39,49,6,4,smoke_light)
result.rect(98,55,5,4,smoke_dark)
result.rect(101,51,7,5,smoke_light)
result.rect(106,49,5,3,smoke_light)

# Tall foreground pines frame the village
def pine(x, base, h, col, lit=False):
    trunk_x = x
    result.rect(trunk_x-1, base-h+12, 3, h-10, wood_dark)
    tiers = [(0,7,5),(5,10,8),(11,14,11),(18,17,14),(27,20,17)]
    for off, half, depth in tiers:
        yy = base-h+off
        if yy >= base: continue
        half = min(half, max(5,(base-yy)//2))
        result.poly([(x,yy),(x-half,yy+depth),(x-3,yy+depth-2),(x-half-3,yy+depth+5),(x+half+3,yy+depth+5),(x+3,yy+depth-2),(x+half,yy+depth)], col)
        if lit:
            result.line(x-1,yy+2,x-half+2,yy+depth,sun_edge)

pine(6, 118, 55, pine_dark, True)
pine(120, 117, 58, pine_dark, False)
pine(18, 126, 38, forest, True)
pine(108, 128, 34, forest, False)
# Deep foreground corner shadows
result.poly([(0,113),(8,108),(17,119),(22,128),(0,128)], pine_dark)
result.poly([(128,109),(118,112),(111,128),(128,128)], pine_dark)

# Small central focal accents: doorstep and roof glints
result.rect(59,91,13,3, wood_dark)
result.rect(61,90,9,2, stone_light)
result.set(52,67,sun_core)
result.set(78,67,sun_core)

# Fine grass pixels in foreground
for x,y in [(24,121),(28,112),(32,125),(95,113),(99,123),(15,108),(116,120),(3,126),(87,126)]:
    result.line(x,y,x-1,y-4,forest)
    result.line(x+1,y,x+3,y-3,forest)

view(result, scale=4, margin=0)
finish(result)
