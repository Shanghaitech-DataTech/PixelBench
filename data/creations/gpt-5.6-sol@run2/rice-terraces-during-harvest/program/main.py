# 64x64 golden rice terraces during harvest
result = new_canvas(64, 64, background="#9fc5aa", name="rice-terraces-harvest")

# Restrained harvest palette.
sky = "#9fc5aa"
haze = "#75958a"
far_mtn = "#496f68"
near_mtn = "#315952"
dark = "#203f3c"
water = "#477a72"
water_hi = "#73a39a"
ridge_dark = "#594b2a"
ridge = "#806637"
ridge_hi = "#b08a3f"
gold_dark = "#a8792f"
gold = "#d3a63b"
gold_hi = "#f0cb58"
straw = "#ffe078"
soil = "#6b5230"
roof = "#713f2b"
roof_hi = "#a65c37"
wall = "#d6bd7a"
cloth_red = "#a63d32"
cloth_blue = "#315e73"
skin = "#bd7745"
hat = "#e6bd5b"

# Distant mountain layers, kept narrow so terraces dominate.
result.poly([(0,15),(0,9),(7,6),(13,9),(20,3),(29,10),(37,5),(46,11),(54,6),(63,9),(63,20)], haze)
result.poly([(0,18),(0,13),(9,9),(16,14),(24,7),(31,14),(39,10),(47,15),(56,9),(63,13),(63,22)], far_mtn)
result.poly([(0,22),(0,17),(8,13),(15,18),(23,12),(31,18),(40,14),(48,19),(56,14),(63,17),(63,24)], near_mtn)
# Sparse mountain contour highlights.
result.line(2,15,8,12,water_hi).line(8,12,14,16,water_hi)
result.line(24,13,28,10,water_hi).line(28,10,33,15,water_hi)
result.line(49,17,56,12,water_hi).line(56,12,61,16,water_hi)

# Tiny village in the distance.
def house(x, y, w=5):
    result.rect(x+1,y+2,w-2,3,wall)
    result.poly([(x,y+2),(x+w//2,y),(x+w,y+2)],roof)
    result.line(x+1,y+2,x+w-1,y+2,roof_hi)
    result.set(x+w//2,y+4,dark)

house(6,15,6)
house(15,17,5)
house(43,16,6)
house(53,17,5)
result.set(11,14,"#d9d1a2").set(48,14,"#d9d1a2")

# Deep base beneath all terraces.
result.rect(0,21,64,43,dark)

# Terraced paddies: broad, nested contour ribbons from back to front.
# Upper cool paddy.
result.poly([(0,22),(10,20),(23,21),(34,19),(48,21),(63,19),(63,25),(49,27),(36,25),(23,27),(10,25),(0,28)], water)
result.poly([(0,22),(11,21),(23,22),(35,20),(48,22),(63,20),(63,22),(49,24),(36,22),(23,24),(10,23),(0,25)], gold_dark)
result.line(0,27,10,24,ridge_hi).line(10,24,23,26,ridge_hi).line(23,26,36,24,ridge_hi).line(36,24,49,26,ridge_hi).line(49,26,63,24,ridge_hi)

# Left-reaching second contour.
result.poly([(0,29),(10,26),(23,28),(36,26),(49,28),(63,25),(63,32),(51,35),(38,32),(25,35),(12,31),(0,35)], gold)
result.poly([(0,29),(11,27),(23,29),(36,27),(49,29),(63,26),(63,29),(51,32),(38,30),(25,32),(12,29),(0,32)], gold_hi)
result.line(0,35,12,31,ridge).line(12,31,25,35,ridge).line(25,35,38,32,ridge).line(38,32,51,35,ridge).line(51,35,63,32,ridge)
result.line(0,34,12,30,ridge_hi).line(12,30,25,34,ridge_hi).line(25,34,38,31,ridge_hi).line(38,31,51,34,ridge_hi).line(51,34,63,31,ridge_hi)

# Third band curls around the center slope.
result.poly([(0,37),(12,33),(25,37),(38,34),(51,37),(63,34),(63,42),(52,45),(39,41),(27,45),(14,40),(0,45)], gold_dark)
result.poly([(0,37),(12,34),(25,38),(38,35),(51,38),(63,35),(63,39),(52,42),(39,39),(27,42),(14,38),(0,42)], gold)
result.poly([(2,37),(12,35),(24,38),(14,37)], gold_hi)
result.poly([(29,39),(38,36),(49,38),(39,38)], gold_hi)
result.line(0,45,14,40,ridge_dark).line(14,40,27,45,ridge_dark).line(27,45,39,41,ridge_dark).line(39,41,52,45,ridge_dark).line(52,45,63,42,ridge_dark)
result.line(0,43,14,39,ridge_hi).line(14,39,27,44,ridge_hi).line(27,44,39,40,ridge_hi).line(39,40,52,44,ridge_hi).line(52,44,63,41,ridge_hi)

# Fourth contour, wider and brighter foreground.
result.poly([(0,47),(14,42),(27,47),(40,43),(53,47),(63,44),(63,53),(53,56),(41,51),(28,56),(15,50),(0,56)], soil)
result.poly([(0,47),(14,43),(27,48),(40,44),(53,48),(63,45),(63,50),(53,53),(41,49),(28,53),(15,48),(0,53)], gold)
result.poly([(0,47),(14,44),(25,48),(15,46),(4,49)], gold_hi)
result.poly([(31,48),(40,45),(52,48),(41,47)], gold_hi)
result.line(0,55,15,50,ridge_dark).line(15,50,28,56,ridge_dark).line(28,56,41,51,ridge_dark).line(41,51,53,56,ridge_dark).line(53,56,63,53,ridge_dark)
result.line(0,53,15,49,ridge_hi).line(15,49,28,55,ridge_hi).line(28,55,41,50,ridge_hi).line(41,50,53,55,ridge_hi).line(53,55,63,52,ridge_hi)

# Lowest terrace reaches off canvas and anchors the scene.
result.poly([(0,57),(15,52),(29,58),(42,53),(54,58),(63,55),(63,64),(0,64)], gold_dark)
result.poly([(0,57),(15,53),(29,59),(42,54),(54,59),(63,56),(63,62),(55,64),(7,64),(0,62)], gold)
result.poly([(0,58),(15,54),(27,59),(16,57),(4,60)], gold_hi)
result.poly([(34,58),(42,55),(54,60),(43,58)], gold_hi)
result.line(0,62,7,63,ridge).line(29,63,42,58,ridge).line(42,58,54,63,ridge).line(54,63,63,60,ridge)
result.line(29,62,42,57,ridge_hi).line(42,57,54,62,ridge_hi).line(54,62,63,59,ridge_hi)

# Harvest stubble: short directional clusters following each contour.
stubble = [
 (3,30),(7,29),(16,31),(20,32),(30,30),(34,29),(43,31),(47,32),(57,29),(60,28),
 (4,39),(8,38),(17,36),(22,39),(31,38),(35,37),(44,38),(48,40),(57,38),(61,37),
 (4,49),(9,47),(18,46),(23,49),(32,50),(36,47),(45,47),(49,50),(58,48),(61,47),
 (5,59),(10,57),(19,57),(24,60),(34,58),(38,57),(47,59),(51,61),(59,58)
]
for x,y in stubble:
    result.line(x,y,x+1,y-2,straw)
    result.set(x+2,y,gold_dark)

# Small cut-rice sheaves.
for x,y in [(10,33),(33,33),(57,40),(8,51),(35,52),(20,61)]:
    result.set(x,y,straw).set(x+1,y-1,straw).set(x+2,y,straw)
    result.line(x,y+1,x+2,y+1,ridge_dark)

# Two farmers standing on narrow ridges, with broad hats and tools.
def farmer(x,y,shirt,flip=False):
    # y is hat row; compact 3x6 silhouette.
    result.line(x-2,y,x+2,y,hat)
    result.line(x-1,y-1,x+1,y-1,hat)
    result.set(x,y+1,skin)
    result.rect(x-1,y+2,3,2,shirt)
    result.set(x-1,y+4,dark).set(x+1,y+4,dark)
    result.set(x-1,y+5,dark).set(x+1,y+5,dark)
    if flip:
        result.line(x-2,y+2,x-4,y+5,ridge_dark)
    else:
        result.line(x+2,y+2,x+4,y+5,ridge_dark)

farmer(18,34,cloth_red,False)
farmer(46,45,cloth_blue,True)

# Foreground edge accents and a few reflective irrigation pixels.
result.line(1,54,6,52,water_hi)
result.line(56,54,62,52,water_hi)
result.set(24,26,water_hi).set(25,26,water_hi).set(39,32,water_hi)

view(result, scale=8, margin=0)
finish(result)
