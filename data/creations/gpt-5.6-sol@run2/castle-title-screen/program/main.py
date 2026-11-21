from pixelbench_api import *

# 128x128 fantasy RPG title-screen scene
result = new_canvas(128, 128, background="#211a35", name="castle-title-screen")

# Compact hand-picked palette
sky0 = "#352449"; sky1 = "#513052"; sky2 = "#754052"; sky3 = "#a95750"
sky4 = "#d46b4c"; sky5 = "#ef8d4b"; sky6 = "#f6b65b"
sun0 = "#ffd777"; sun1 = "#ffbd55"; sun2 = "#ee8143"
cloud0 = "#31283f"; cloud1 = "#493249"; cloud2 = "#754354"; cloud3 = "#a85a59"; cloud4 = "#d47a63"
sea0 = "#242940"; sea1 = "#2d3650"; sea2 = "#3b4660"; sea3 = "#59627a"; sea4 = "#a66b66"; foam = "#d8a782"
ink = "#171827"; rock0 = "#1c1c2d"; rock1 = "#27253a"; rock2 = "#343047"; rock3 = "#464057"
stone0 = "#252536"; stone1 = "#343246"; stone2 = "#4b4351"; stone3 = "#66515a"; stone4 = "#8a625e"
light0 = "#f2a452"; light1 = "#ffd079"; flag = "#b94345"; flag_hi = "#e0644d"

# Layered sunset sky, horizontal bands with deliberate pixel steps
result.rect(0, 0, 128, 15, sky0)
result.rect(0, 15, 128, 13, sky1)
result.rect(0, 28, 128, 14, sky2)
result.rect(0, 42, 128, 13, sky3)
result.rect(0, 55, 128, 11, sky4)
result.rect(0, 66, 128, 10, sky5)
# subtle broken sky bands
result.rect(0, 14, 41, 2, "#40294b").rect(75, 15, 53, 2, "#40294b")
result.rect(0, 27, 29, 2, "#60364f").rect(83, 27, 45, 2, "#60364f")
result.rect(42, 41, 86, 2, "#914b52")
result.rect(71, 54, 57, 2, "#c45e4d")

# Huge orange setting sun behind clouds
result.circle(94, 39, 23, sun2)
result.circle(94, 37, 20, sun1)
result.circle(91, 33, 15, sun0)
# pixel-notch the disc for a raster silhouette
result.rect(75, 21, 4, 4, sky2).rect(111, 22, 4, 5, sky2)
result.rect(114, 49, 3, 4, sky3).rect(73, 46, 3, 5, sky3)

# Distant upper clouds
result.poly([(0,20),(7,20),(7,17),(17,17),(17,15),(28,15),(28,17),(36,17),(36,20),(48,20),(48,24),(0,24)], cloud1)
result.rect(0, 23, 39, 3, cloud2)
result.poly([(79,10),(89,10),(89,8),(101,8),(101,10),(111,10),(111,13),(124,13),(124,16),(78,16)], cloud0)
result.rect(88, 16, 40, 2, cloud1)
# warm mid-cloud crossing sun
result.poly([(59,44),(66,44),(66,41),(75,41),(75,38),(85,38),(85,40),(96,40),(96,43),(106,43),(106,46),(122,46),(122,50),(58,50)], cloud2)
result.rect(67, 50, 55, 3, cloud3)
result.rect(83, 53, 30, 2, cloud4)
result.rect(106, 48, 22, 5, cloud2)
# right wispy cloud
result.poly([(96,61),(102,61),(102,58),(111,58),(111,56),(120,56),(120,58),(128,58),(128,65),(96,65)], cloud3)
result.rect(105,65,23,2, cloud4)

# Ocean base and horizon glow
result.rect(0, 74, 128, 54, sea0)
result.rect(0, 74, 128, 3, "#8f5a60")
result.rect(0, 77, 128, 5, sea3)
result.rect(0, 82, 128, 7, sea2)
result.rect(0, 89, 128, 39, sea1)
# sun reflection: broken horizontal gold fragments
for x,y,w,c in [
    (78,76,33,foam),(84,80,22,"#c98a70"),(71,84,38,"#bd7d69"),(86,88,17,foam),
    (76,92,29,"#9b6865"),(90,97,12,"#b57b6c"),(80,102,23,"#7c5961")]:
    result.rect(x,y,w,2,c)
# wave streaks
for x,y,w,c in [
    (4,80,22,sea4),(34,78,18,"#7e5961"),(113,81,15,"#85606a"),
    (8,87,16,sea3),(31,91,22,sea3),(107,91,18,sea3),(57,95,16,sea3),
    (4,101,27,"#3f4c66"),(35,106,24,"#253047"),(105,104,19,"#46516a"),
    (16,113,18,"#526078"),(63,112,22,"#3f4b64"),(94,118,28,"#263349")]:
    result.rect(x,y,w,2,c)
# tiny foam caps
result.rect(18,86,6,1,foam).rect(15,87,3,1,foam)
result.rect(111,89,8,1,"#8290a0").rect(108,90,4,1,"#8290a0")
result.rect(48,99,7,1,"#78849a").rect(45,100,4,1,"#78849a")

# Far cliff carrying the castle
result.poly([(0,60),(10,59),(18,62),(27,63),(36,66),(46,68),(55,73),(63,76),(67,82),(62,88),(55,91),(48,96),(41,99),(30,99),(24,103),(14,102),(0,106)], rock0)
result.poly([(0,69),(12,67),(23,70),(33,73),(43,77),(52,79),(60,84),(53,88),(46,88),(40,94),(28,94),(21,98),(10,96),(0,99)], rock1)
result.poly([(0,72),(13,71),(23,74),(29,76),(17,77),(9,81),(0,80)], rock2)
result.rect(28,79,18,3, rock2).rect(22,83,15,3, rock3)
result.rect(44,86,11,3, rock2).rect(14,91,15,3, rock2)

# Castle main mass, perched over cliff
result.rect(18,43,41,28, stone0)
result.rect(22,39,33,31, stone1)
# battlements main keep
for x in (22,30,42,50):
    result.rect(x,35,6,7,stone0)
result.rect(22,40,34,7,stone1)
# central raised hall and roof ridge
result.rect(32,30,14,12,stone0)
result.poly([(30,31),(39,24),(48,31)], ink)
result.poly([(33,31),(39,27),(45,31)], stone3)
result.rect(35,31,9,12,stone2)
# left tower
result.rect(10,28,16,39,stone0)
result.rect(12,27,13,40,stone1)
result.rect(9,24,18,6,stone0)
for x in (9,16,23):
    result.rect(x,20,5,7,stone0)
result.rect(12,29,3,34,stone2)
# right tower, taller/narrower
result.rect(52,24,17,49,stone0)
result.rect(55,22,12,49,stone1)
result.rect(51,20,18,6,stone0)
for x in (51,58,65):
    result.rect(x,16,5,7,stone0)
result.rect(55,26,3,39,stone2)
# masonry warm edge catching sunset
result.rect(25,45,2,21,stone3).rect(47,45,2,20,stone2)
result.rect(66,27,2,39,stone3).rect(13,31,2,28,stone3)
result.rect(27,48,18,2,stone2).rect(30,59,19,2,stone2)
result.rect(18,53,6,2,stone3).rect(51,37,7,2,stone3)
result.rect(35,35,8,2,stone4)
# brick accents
for x,y,w in [(17,34,6),(28,43,7),(38,52,8),(50,57,6),(16,61,7),(57,31,7),(56,48,8),(27,65,9)]:
    result.rect(x,y,w,2,stone2)

# Windows: warm magical points and dark arrow slits
for x,y in [(17,36),(58,30),(58,43),(38,37),(27,54)]:
    result.rect(x,y,3,5,light0)
    result.set(x+1,y,light1)
for x,y in [(17,48),(17,57),(61,55),(44,44),(34,55)]:
    result.rect(x,y,2,5,ink)
# arched gate
result.rect(35,62,8,10,ink)
result.circle(39,62,4,ink)
result.rect(38,64,1,8,stone3)

# Two flagpoles and windblown flags
result.rect(17,8,1,13,ink)
result.poly([(18,9),(33,12),(29,16),(18,14)], flag)
result.rect(19,10,9,2,flag_hi).set(30,12,flag_hi)
result.rect(60,5,1,12,ink)
result.poly([(61,6),(75,9),(71,13),(61,11)], flag)
result.rect(62,7,8,2,flag_hi).set(72,9,flag_hi)
# pole caps
result.rect(16,7,3,2,light1).rect(59,4,3,2,light1)

# Foreground framing rocks, deep and chunky
result.poly([(0,95),(8,91),(16,94),(22,101),(28,103),(31,112),(40,116),(44,128),(0,128)], ink)
result.poly([(0,102),(8,98),(15,101),(18,109),(27,112),(30,128),(0,128)], rock1)
result.poly([(0,111),(10,108),(18,114),(21,128),(0,128)], rock2)
result.poly([(128,97),(121,94),(113,96),(108,103),(99,105),(96,113),(89,118),(86,128),(128,128)], ink)
result.poly([(128,105),(119,100),(113,103),(109,111),(101,114),(97,128),(128,128)], rock1)
result.poly([(128,114),(120,110),(113,115),(109,128),(128,128)], rock2)
# central low crags create cinematic lower frame
result.poly([(24,128),(31,119),(39,117),(48,121),(55,118),(63,122),(70,120),(78,123),(84,128)], rock0)
result.poly([(32,128),(40,121),(48,124),(55,122),(63,126),(72,123),(80,128)], rock2)
# edge highlights on rocks
result.line(4,102,11,99,rock3).line(11,99,17,104,rock3)
result.line(109,109,114,102,rock3).line(114,102,121,100,rock3)
result.rect(8,113,8,2,rock3).rect(113,116,10,2,rock3)
result.rect(38,122,8,2,rock3).rect(69,124,7,2,rock3)

# A few airborne birds for scale
result.line(83,29,86,27,cloud0).line(86,27,89,29,cloud0)
result.line(116,35,119,33,cloud1).line(119,33,122,35,cloud1)

view(result, scale=4, margin=0)
finish(result)
