# 64x64 harvest rice terraces
result = new_canvas(64, 64, background="#182f2b", name="rice-terraces-harvest")

# Palette
sky = "#91a77a"
mist = "#718b6b"
mount_far = "#405f52"
mount_mid = "#315047"
mount_near = "#243f38"
forest = "#1b352f"
forest_hi = "#42654f"
roof_dark = "#4a2922"
roof_red = "#8d4329"
roof_hi = "#c06b35"
wall = "#d5b66a"
wall_shade = "#957d4b"
path_light = "#d5b865"
ridge_dark = "#5b4b27"
ridge_mid = "#7b642f"
ridge_hi = "#b18d3d"
gold_dark = "#9b7625"
gold = "#c99c2f"
gold_hi = "#edc34f"
straw = "#f4d76a"
amber = "#d67f22"
water = "#597b68"
water_hi = "#83a079"
shadow = "#273b31"
skin = "#b86d3b"
shirt1 = "#4f7f78"
shirt2 = "#a8472c"
hat = "#e6c56b"
white = "#f0dfaa"

# Hazy sky strips and distant mountain contours
result.rect(0, 0, 64, 10, sky)
result.rect(0, 8, 64, 4, mist)
result.poly([(0,8),(7,4),(13,8),(20,3),(28,9),(36,5),(44,9),(53,2),(64,8),(64,15),(0,15)], mount_far)
result.poly([(0,12),(8,8),(16,12),(24,7),(32,13),(41,8),(49,12),(57,7),(64,11),(64,18),(0,18)], mount_mid)
result.poly([(0,16),(6,12),(13,15),(20,11),(27,16),(35,12),(44,15),(51,10),(58,14),(64,12),(64,22),(0,22)], mount_near)
# Mountain texture
result.line(2,13,8,9,forest_hi); result.line(9,14,15,11,forest_hi)
result.line(22,13,25,10,forest_hi); result.line(39,13,44,10,forest_hi)
result.line(52,12,57,9,forest_hi)
result.rect(0,17,64,4,forest)
for x,y in [(2,15),(5,14),(11,16),(17,14),(29,15),(33,14),(47,15),(55,14),(61,15)]:
    result.poly([(x,y+3),(x+2,y),(x+4,y+3)], forest_hi)

# Distant village houses clustered along upper ridge
def house(x,y,w=6):
    result.rect(x+1,y+3,w-2,4,wall_shade)
    result.rect(x+2,y+3,w-3,3,wall)
    result.poly([(x,y+3),(x+w//2,y),(x+w,y+3)], roof_dark)
    result.line(x+1,y+2,x+w-1,y+2,roof_red)
    result.set(x+w//2,y+5,roof_dark)

house(5,12,7); house(14,14,6); house(24,12,8); house(36,14,6); house(45,11,8); house(55,14,7)
result.set(28,13,roof_hi); result.set(49,12,roof_hi); result.set(8,13,roof_hi)
# Tiny smoke
result.set(28,9,"#809582"); result.set(29,8,"#809582")

# Terrace field base
result.rect(0,20,64,44,gold_dark)

# Layered paddies, their curved contours widen toward foreground
result.path("M0 20 C12 17 21 18 31 21 C42 24 54 19 64 18 L64 25 C52 25 45 29 33 26 C20 22 11 23 0 27 Z", gold)
result.path("M0 28 C12 23 23 25 33 28 C45 32 54 26 64 26 L64 34 C51 31 45 37 31 34 C20 30 10 31 0 36 Z", gold_hi)
result.path("M0 38 C10 31 20 34 30 37 C42 42 53 34 64 36 L64 45 C51 40 43 47 29 44 C17 39 9 42 0 47 Z", gold)
result.path("M0 49 C11 40 19 44 30 48 C43 53 53 43 64 47 L64 57 C53 51 45 59 30 55 C18 50 10 53 0 59 Z", gold_hi)
result.path("M0 60 C10 51 19 55 29 59 C37 62 46 61 54 57 C58 55 61 56 64 58 L64 64 L0 64 Z", amber)

# Dark retaining walls and highlighted ridge tops
contours = [
    ("M0 26 C12 21 21 22 32 25 C43 29 54 23 64 23", ridge_dark),
    ("M0 35 C11 28 22 30 32 33 C44 38 54 31 64 32", ridge_dark),
    ("M0 46 C10 37 19 40 30 43 C43 49 53 39 64 43", ridge_dark),
    ("M0 58 C10 48 19 51 30 54 C43 60 53 49 64 54", ridge_dark),
]
for d,c in contours:
    result.path(d,c,fill=False)
# Pixel-thick shadow offsets and sunlit ridge fragments
result.path("M0 27 C12 22 21 23 32 26 C43 30 54 24 64 24", ridge_mid, fill=False)
result.path("M0 36 C11 29 22 31 32 34 C44 39 54 32 64 33", ridge_mid, fill=False)
result.path("M0 47 C10 38 19 41 30 44 C43 50 53 40 64 44", ridge_mid, fill=False)
result.path("M0 59 C10 49 19 52 30 55 C43 61 53 50 64 55", ridge_mid, fill=False)
result.line(2,25,12,22,ridge_hi); result.line(17,22,26,24,ridge_hi)
result.line(4,33,13,30,ridge_hi); result.line(38,35,48,34,ridge_hi)
result.line(3,44,12,40,ridge_hi); result.line(46,44,55,41,ridge_hi)
result.line(3,56,13,51,ridge_hi); result.line(36,57,46,55,ridge_hi)

# Narrow irrigation water glimpses
result.path("M52 25 C57 23 60 23 64 23 L64 25 C60 25 56 26 52 27 Z", water)
result.line(56,24,62,24,water_hi)
result.path("M49 34 C55 31 59 31 64 32 L64 33 C59 32 55 34 49 35 Z", water)
result.path("M52 44 C57 41 61 42 64 43 L64 44 C60 43 57 45 52 46 Z", water)

# Rice-row texture: short staggered strokes following each terrace
for x,y in [(3,22),(8,21),(14,21),(20,22),(27,23),(36,25),(42,26),(50,24),(58,22),
            (3,31),(8,29),(15,28),(21,29),(27,31),(35,33),(42,34),(50,31),(58,29),
            (3,41),(9,38),(15,37),(22,38),(28,41),(36,43),(44,43),(51,39),(59,39),
            (3,53),(9,49),(16,47),(23,49),(29,51),(37,54),(44,54),(52,50),(59,50),
            (4,62),(11,57),(18,56),(25,58),(33,61),(47,60),(56,57)]:
    result.line(x,y,x+1,y-2,straw)
    result.set(x+2,y-1,gold_dark)
# Harvested patch hatch marks
for x in range(1,28,4):
    result.line(x,62,x+3,59,"#f1b83f")

# Farmer 1 on middle ridge: conical hat, teal shirt, legs and carrying pole
result.line(18,34,25,31,shadow)
result.set(18,35,shadow); result.set(23,35,shadow)
result.rect(20,32,3,4,shirt1)
result.set(20,36,ridge_dark); result.set(22,36,ridge_dark)
result.set(21,31,skin)
result.poly([(18,31),(21,29),(24,31)],hat)
result.line(17,33,25,33,roof_dark)
result.set(17,34,amber); result.set(25,34,amber)

# Farmer 2 on foreground ridge: red shirt with basket
result.set(46,45,shadow); result.set(49,45,shadow)
result.rect(46,42,3,4,shirt2)
result.set(46,46,ridge_dark); result.set(48,46,ridge_dark)
result.set(47,41,skin)
result.poly([(44,41),(47,39),(50,41)],hat)
result.rect(50,42,3,3,amber)
result.set(51,41,ridge_dark)
result.line(48,43,51,42,skin)

# Foreground edge plants and bright grain heads
for x in [1,7,13,21,39,45,53,60]:
    result.line(x,63,x,59,ridge_dark)
    result.set(x-1,59,straw); result.set(x+1,60,straw)

# Tied harvest sheaves on the lower banks
for x,y in [(9,55),(32,57),(57,51)]:
    result.line(x,y,x-2,y-4,straw)
    result.line(x,y,x,y-5,straw)
    result.line(x,y,x+2,y-4,straw)
    result.line(x-2,y-2,x+2,y-2,ridge_dark)

# Sparse glints and contour accents
for x,y in [(31,21),(34,22),(6,28),(11,27),(39,29),(44,28),(18,34),(26,36),(55,36),(61,37),(13,45),(20,45),(34,47),(58,48),(31,57),(41,59)]:
    result.set(x,y,white)

view(result, scale=8, margin=0)
finish(result)
