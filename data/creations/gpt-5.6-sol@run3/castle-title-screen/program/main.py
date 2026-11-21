from pixelbench_api import *

# 128x128 fantasy RPG title screen
result = new_canvas(128, 128, background="#141326", name="castle-title-screen")

# Tight dusk palette
ink = "#141326"
deep = "#201a32"
plum = "#35213b"
cloud_dark = "#51304b"
cloud_mid = "#75405a"
rose = "#a95761"
coral = "#d66b62"
orange = "#ee8a55"
gold = "#f5b55f"
sun = "#ffd277"
pale = "#ffe09a"
sea_dark = "#1c2940"
sea = "#29415a"
sea_mid = "#3b6070"
foam = "#6f9290"
rock = "#171827"
rock_mid = "#28263a"
rock_hi = "#474053"
castle_dark = "#262033"
castle = "#3a3042"
castle_hi = "#594456"
window = "#ffc76b"
flag = "#9f3f51"
title_shadow = "#4a253b"
title = "#f5c977"
title_hi = "#fff0ad"

# Sunset bands
result.rect(0, 0, 128, 18, deep)
result.rect(0, 18, 128, 13, plum)
result.rect(0, 31, 128, 13, cloud_mid)
result.rect(0, 44, 128, 14, rose)
result.rect(0, 58, 128, 14, coral)
result.rect(0, 72, 128, 12, orange)
result.rect(0, 84, 128, 12, gold)

# Pixel-banded transition texture
for x, y, w, col in [
    (0,17,32,plum),(42,17,23,plum),(82,17,46,plum),
    (9,29,38,cloud_mid),(63,29,29,cloud_mid),(103,29,25,cloud_mid),
    (0,42,22,rose),(31,42,46,rose),(90,42,38,rose),
    (6,56,45,coral),(70,56,31,coral),(109,56,19,coral),
    (0,70,31,orange),(47,70,42,orange),(103,70,25,orange),
]: result.rect(x,y,w,3,col)

# Huge setting sun, partly obscured by castle and horizon
result.circle(76, 58, 25, sun)
result.rect(56, 38, 41, 4, pale)
result.rect(52, 47, 49, 13, pale)
result.rect(54, 60, 45, 8, sun)
# Sun pixel glints
result.rect(58, 45, 5, 2, "#fff0b0")
result.rect(89, 51, 7, 2, "#fff0b0")

# Layered clouds: long, stepped horizontal masses
result.poly([(0,24),(8,24),(8,21),(21,21),(21,24),(37,24),(37,28),(50,28),(50,33),(0,33)], cloud_dark)
result.rect(0,31,43,3, cloud_mid)
result.rect(10,27,31,3, cloud_mid)
result.poly([(70,19),(82,19),(82,16),(99,16),(99,20),(115,20),(115,23),(128,23),(128,30),(75,30),(75,27),(65,27)], cloud_dark)
result.rect(84,24,44,3, cloud_mid)
result.rect(99,29,29,2, rose)
result.poly([(0,46),(13,46),(13,43),(28,43),(28,46),(42,46),(42,50),(52,50),(52,54),(0,54)], "#63384f")
result.rect(0,52,35,3, rose)
result.poly([(93,36),(106,36),(106,33),(119,33),(119,36),(128,36),(128,43),(88,43),(88,40),(78,40),(78,37)], "#63384f")
result.rect(100,42,28,3, rose)
# Thin bright cloud ribbons
result.rect(5,66,26,2, gold)
result.rect(0,68,18,2, orange)
result.rect(101,63,27,2, gold)
result.rect(110,66,18,2, orange)

# Sea and horizon
result.rect(0,88,128,40, sea_dark)
result.rect(0,88,128,3, sea_mid)
result.rect(0,92,128,5, sea)
result.rect(0,100,128,2, "#24384f")
# Horizontal sea reflections
for x,y,w,c in [
    (4,94,18,foam),(28,95,12,sea_mid),(49,92,19,foam),(76,94,9,sea_mid),(95,92,24,foam),
    (0,103,14,sea_mid),(19,106,26,foam),(51,102,10,sea_mid),(70,107,20,foam),(101,103,27,sea_mid),
    (8,113,15,foam),(30,111,12,sea_mid),(56,115,28,sea_mid),(91,112,13,foam),(112,116,16,sea_mid)
]: result.rect(x,y,w,1,c)

# Distant rock stack at right
result.poly([(112,81),(118,78),(123,80),(126,77),(128,78),(128,104),(115,103),(116,96),(111,93)], deep)
result.rect(119,84,9,12, castle_dark)
result.set(121,82, castle_hi)

# Cliff silhouette beneath castle
result.poly([(15,75),(25,70),(36,71),(43,74),(48,78),(59,79),(66,84),(69,91),(66,98),(58,102),(50,109),(39,111),(31,117),(17,119),(0,116),(0,89),(8,84)], rock)
result.poly([(0,87),(13,79),(22,77),(31,78),(38,82),(48,83),(57,89),(62,96),(52,96),(45,101),(34,102),(25,108),(12,106),(0,109)], rock_mid)
# Cliff strata and lit edges
result.poly([(3,84),(14,77),(29,75),(39,80),(31,81),(25,84),(17,82),(10,89)], rock_hi)
result.rect(7,91,16,2, "#353044")
result.poly([(31,87),(44,85),(55,90),(58,94),(48,92),(42,96),(34,94)], "#373143")
result.rect(17,101,14,2, "#3d3548")
result.rect(2,109,21,2, deep)

# Castle main keep on cliff
result.rect(25,49,35,28, castle_dark)
result.rect(28,53,29,23, castle)
# Battlements
for x in [24,31,39,47,55]:
    result.rect(x,45,6,7, castle_dark)
    result.rect(x+2,47,4,5, castle)
result.rect(24,51,37,4, castle)
# Left tower
result.rect(17,35,14,39, castle_dark)
result.rect(20,39,10,35, castle)
for x in [16,22,28]: result.rect(x,31,5,8, castle_dark)
result.rect(16,37,17,4, castle)
# Right tall tower
result.rect(51,29,15,50, castle_dark)
result.rect(54,34,10,43, castle)
for x in [50,56,63]: result.rect(x,25,5,9, castle_dark)
result.rect(50,32,18,4, castle)
# Roof/stone highlights
result.rect(21,42,2,28, castle_hi)
result.rect(55,37,2,36, castle_hi)
result.rect(30,56,2,18, castle_hi)
result.rect(37,57,15,2, castle_hi)
result.rect(26,67,28,2, "#463749")
# Gate and windows
result.poly([(37,67),(41,63),(45,67),(45,77),(37,77)], deep)
for x,y in [(23,46),(23,57),(57,41),(57,53),(57,64),(34,59),(48,59)]:
    result.rect(x,y,2,4, window)
    result.set(x+1,y, pale)
# Tiny stone marks
for x,y,w in [(27,58,4),(46,54,5),(33,63,3),(25,72,5),(49,72,4),(59,48,4),(18,51,3)]:
    result.rect(x,y,w,1,castle_hi)

# Flagpoles and two windblown flags
result.rect(23,17,1,15, ink)
result.poly([(24,18),(38,21),(31,25),(24,24)], flag)
result.rect(23,18,8,1, coral)
result.rect(58,10,1,16, ink)
result.poly([(59,11),(77,14),(70,18),(59,17)], flag)
result.rect(59,11,10,1, coral)

# Foreground rocks frame the lower edge
result.poly([(0,105),(7,102),(15,105),(20,114),(27,117),(31,128),(0,128)], ink)
result.poly([(0,112),(7,108),(13,111),(16,119),(23,122),(23,128),(0,128)], rock_mid)
result.poly([(128,100),(120,98),(115,103),(112,111),(105,115),(100,128),(128,128)], ink)
result.poly([(128,108),(121,104),(117,109),(116,117),(108,121),(108,128),(128,128)], rock_mid)
result.poly([(34,121),(44,117),(53,120),(61,118),(69,122),(79,119),(90,122),(99,128),(28,128)], rock)
result.rect(45,124,17,2,rock_hi)
result.rect(76,123,11,2,rock_hi)
result.rect(4,111,7,2,rock_hi)
result.rect(119,109,9,2,rock_hi)

# Whitecaps around the cliff base
result.rect(28,110,12,2,foam)
result.rect(34,108,15,2,"#91aaa1")
result.rect(42,106,9,1,pale)
result.rect(52,104,11,2,foam)
result.rect(17,116,10,1,foam)

# RPG title lockup in the open sky, outlined for contrast against the sun
for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
    result.text(75+dx,68+dy,"SUNFALL",title_shadow,font="5x7",spacing=1)
result.text(75,68,"SUNFALL",title_hi,font="5x7",spacing=1)
result.rect(78,76,35,1,title_shadow)
result.rect(83,77,25,1,title)
for dx, dy in [(-1,0),(1,0),(0,1)]:
    result.text(84+dx,80+dy,"KEEP",title_shadow,font="5x7",spacing=1)
result.text(84,80,"KEEP",title,font="5x7",spacing=1)
result.rect(80,89,33,1,title_shadow)

# Sparse birds for depth
result.line(8,59,11,57,deep); result.line(11,57,14,59,deep)
result.line(106,51,109,49,deep); result.line(109,49,112,51,deep)

view(result, scale=4, margin=0)
finish(result)
