# 64x64 sunken shipwreck pixel art
result = new_canvas(64, 64, background="#123d52", name="sunken_shipwreck")

# Palette
water0 = "#123d52"
water1 = "#164b60"
water2 = "#1b596d"
water3 = "#21697a"
water4 = "#2b7885"
ray = "#3f8790"
deep = "#0b2d3d"
ink = "#102a32"
wood0 = "#2b2928"
wood1 = "#46362d"
wood2 = "#664936"
wood3 = "#866247"
wood4 = "#a17a55"
rust = "#8f5337"
rust2 = "#ba7047"
sand0 = "#a6835b"
sand1 = "#c09c68"
sand2 = "#d0b579"
sand3 = "#e0ca8b"
coral0 = "#a94e4f"
coral1 = "#d36a59"
plant0 = "#32654f"
plant1 = "#4b8060"
fish0 = "#80b9af"
fish1 = "#b7d2b9"
fish2 = "#dfd59c"

# Layered water bands
result.rect(0, 0, 64, 9, water3)
result.rect(0, 9, 64, 10, water2)
result.rect(0, 19, 64, 13, water1)
result.rect(0, 32, 64, 20, water0)
# Surface shimmer and descending light shafts
result.rect(2, 3, 13, 2, water4)
result.rect(20, 2, 17, 2, water4)
result.rect(43, 4, 12, 2, water4)
result.rect(8, 7, 9, 1, ray)
result.rect(31, 7, 14, 1, ray)
result.poly([(8,8),(15,8),(24,42),(20,42)], "#2b6c78")
result.poly([(39,8),(44,8),(39,35),(36,35)], "#286776")
# Water texture specks
for x,y,c in [(3,14,water3),(12,17,water3),(24,12,water3),(35,16,water3),(50,12,water3),(58,18,water3),(5,25,water2),(18,28,water2),(28,23,water2),(45,27,water2),(57,24,water2),(2,36,water1),(31,36,water1),(60,33,water1)]:
    result.rect(x,y,3 if x%2 else 2,1,c)

# Distant bubbles
for x,y in [(8,20),(11,16),(49,20),(53,16),(55,12),(24,31)]:
    result.set(x,y,ray)
result.rect(9,22,2,2,water3)
result.set(9,22,ray)

# School of fish, all facing left
fish = [
    (43,16,fish1),(51,20,fish0),(37,22,fish2),(53,27,fish1),
    (46,29,fish0),(31,17,fish0),(54,12,fish2)
]
for x,y,c in fish:
    result.poly([(x,y+1),(x+3,y-1),(x+7,y),(x+9,y-2),(x+9,y+3),(x+7,y+1),(x+3,y+3)], c)
    result.set(x+2,y, "#d8e2c8")
    result.set(x+1,y+1, ink)

# Broken mast behind the hull
result.line(25,12,31,39,ink)
result.line(26,12,32,39,wood3)
result.line(27,13,33,39,wood1)
result.line(26,17,40,20,wood2)
result.line(27,18,39,21,wood4)
result.line(29,28,17,25,wood2)
result.line(29,29,17,26,wood4)
# Tattered sail scraps and rope
result.poly([(29,20),(38,22),(34,29),(31,27)], "#53756d")
result.poly([(28,19),(33,21),(30,24)], "#749183")
result.line(39,21,45,36,"#203a3c")
result.line(18,26,11,36,"#203a3c")

# Main wreck silhouette: raised stern left, bow buried right
result.poly([(7,31),(15,29),(20,32),(48,35),(57,39),(54,48),(45,53),(20,51),(11,45)], ink)
# Outer hull timber mass
result.poly([(9,32),(16,31),(21,34),(48,37),(55,40),(52,47),(44,50),(20,48),(13,44)], wood1)
# Upper corroded rim
result.poly([(10,31),(16,29),(20,32),(48,35),(56,39),(54,41),(47,39),(19,35),(13,34),(10,36)], wood3)
result.line(14,34,47,39,wood4)
result.line(16,36,52,41,rust2)
# Stern cabin remains
result.rect(10,27,10,5,ink)
result.rect(11,26,8,5,wood2)
result.rect(12,27,3,3,deep)
result.rect(17,27,2,3,wood4)
result.rect(9,25,11,2,wood0)
result.rect(11,24,8,1,wood4)
# Broken stern posts
result.rect(8,27,2,10,wood2)
result.rect(8,26,2,2,wood4)
result.rect(20,29,2,6,wood1)
result.set(20,28,wood4)

# Hull plank bands
result.line(13,39,50,44,wood3)
result.line(14,42,48,47,wood2)
result.line(18,46,43,49,wood4)
# Dark plank separation pixel steps
result.line(20,36,18,47,wood0)
result.line(29,37,28,49,wood0)
result.line(39,39,38,50,wood0)
result.line(48,40,45,49,wood0)
# Corrosion and missing holes
result.rect(22,38,4,3,deep)
result.set(21,39,deep)
result.rect(34,41,5,3,deep)
result.set(39,42,deep)
result.rect(45,43,3,3,deep)
result.rect(16,42,3,2,ink)
# Rusty chipped highlights
for x,y in [(14,37),(19,35),(27,41),(31,38),(41,41),(50,42),(23,45),(35,47),(12,40)]:
    result.rect(x,y,2,1,rust)
for x,y in [(17,38),(30,43),(42,45),(51,40)]:
    result.set(x,y,rust2)
# Exposed ribs rising from hull
for x,h in [(23,6),(29,7),(35,6),(42,5)]:
    result.line(x,38,x-1,38-h,ink)
    result.line(x+1,38,x,38-h,wood3)
    result.set(x,38-h,wood4)

# Sand seabed behind and over the wreck
result.poly([(0,50),(8,48),(16,50),(24,49),(32,52),(42,50),(51,48),(63,50),(63,63),(0,63)], sand1)
result.poly([(0,55),(12,52),(22,55),(34,53),(46,55),(56,51),(63,53),(63,63),(0,63)], sand2)
result.poly([(0,60),(15,57),(28,59),(41,57),(53,59),(63,56),(63,63),(0,63)], sand3)
# Burial mounds at hull base
result.poly([(11,50),(19,47),(29,51),(37,54),(15,55)], sand0)
result.poly([(39,52),(50,47),(61,50),(63,55),(45,56)], sand1)
result.line(16,52,30,54,sand2)
result.line(45,54,58,52,sand3)
# Sand texture
for x,y,c in [(2,54,sand3),(8,58,sand0),(18,57,sand1),(25,61,sand0),(34,56,sand0),(42,60,sand1),(52,57,sand0),(59,61,sand1),(5,62,sand1),(31,58,sand3)]:
    result.rect(x,y,3,1,c)

# Left branching coral
result.rect(4,47,2,11,coral0)
result.rect(6,50,2,9,coral1)
result.line(5,51,2,47,coral1)
result.line(5,53,1,53,coral0)
result.line(7,53,10,48,coral1)
result.rect(1,46,2,3,coral0)
result.rect(9,46,2,3,coral0)
# Right coral fan
result.line(55,55,55,45,coral0)
result.line(56,54,60,48,coral1)
result.line(55,51,52,47,coral1)
result.line(58,52,62,51,coral0)
result.rect(51,45,2,3,coral0)
result.rect(59,46,2,3,coral0)

# Seaweed accents with blocky bends
result.line(13,60,12,51,plant0)
result.line(12,54,10,51,plant1)
result.line(13,57,16,53,plant1)
result.line(46,61,47,53,plant0)
result.line(47,56,44,52,plant1)
result.line(48,58,51,54,plant1)
result.line(61,61,60,55,plant0)
# Small stones and foreground shadow flecks
result.rect(20,59,4,2,sand0)
result.rect(21,58,2,1,wood2)
result.rect(37,61,5,2,sand0)
result.rect(38,60,3,1,wood1)
result.rect(27,55,2,1,wood2)

view(result, scale=8, margin=0)
finish(result)
