from pixelbench_api import *

W = H = 128

# Palette
sky0 = "#241c3d"
sky1 = "#44305a"
sky2 = "#7b3f63"
sky3 = "#c45b5d"
sky4 = "#ef8754"
sky5 = "#f6b45c"
sun_hi = "#ffd77a"
sun = "#ffad4a"
cloud_dark = "#30213f"
cloud_mid = "#613752"
cloud_lit = "#d66a5d"
cloud_glow = "#f29a62"
sea_dark = "#17243b"
sea = "#263b54"
sea_mid = "#3f5c6b"
sea_glow = "#d97857"
ink = "#131525"
rock = "#1a1a2a"
rock_mid = "#2b2838"
rock_hi = "#45404b"
castle = "#222033"
castle_mid = "#343044"
castle_hi = "#57505c"
window = "#ffc45a"
gold_dark = "#7d3f30"
gold = "#f39a49"
gold_hi = "#ffd77b"
foam = "#9aa7a2"

# Base sky bands
bg = new_canvas(W, H, sky0, name="sunset sky")
bg.rect(0, 20, W, 15, sky1)
bg.rect(0, 35, W, 17, sky2)
bg.rect(0, 52, W, 15, sky3)
bg.rect(0, 67, W, 19, sky4)
bg.rect(0, 80, W, 8, sky5)
# Mild stepped dithering to integrate the bands
bg.dither(0, 30, W, 9, [sky1, sky2], pattern="bayer4")
bg.dither(0, 47, W, 9, [sky2, sky3], pattern="checker")
bg.dither(0, 63, W, 8, [sky3, sky4], pattern="bayer4")

# Huge sun on the left, half sinking into the sea
bg.circle(38, 66, 22, sun)
bg.circle(38, 64, 17, sun_hi)
# Pixel cutouts give the disc a deliberately blocky rim
bg.rect(18, 49, 3, 5, sky3)
bg.rect(55, 50, 3, 4, sky3)
bg.rect(15, 60, 2, 9, sky4)
bg.rect(59, 60, 2, 8, sky4)

# Layered clouds
clouds = new_canvas(W, H, None, name="clouds")
clouds.poly([(0,29),(8,29),(8,26),(19,26),(19,28),(29,28),(29,32),(39,32),(39,36),(0,36)], cloud_dark)
clouds.rect(2,29,24,2,cloud_mid)
clouds.poly([(63,27),(70,27),(70,24),(81,24),(81,21),(91,21),(91,24),(101,24),(101,28),(114,28),(114,32),(128,32),(128,37),(61,37)], cloud_dark)
clouds.rect(70,28,42,3,cloud_mid)
clouds.rect(84,24,15,2,cloud_mid)
clouds.poly([(0,43),(14,43),(14,40),(26,40),(26,42),(36,42),(36,46),(49,46),(49,50),(0,50)], cloud_mid)
clouds.rect(4,44,28,2,cloud_lit)
clouds.poly([(82,45),(94,45),(94,42),(107,42),(107,44),(117,44),(117,48),(128,48),(128,53),(79,53)], cloud_mid)
clouds.rect(88,47,33,2,cloud_lit)
# Thin glowing strips across sunset
clouds.rect(0,74,16,2,cloud_lit)
clouds.rect(5,76,27,2,cloud_glow)
clouds.rect(53,72,24,2,cloud_lit)
clouds.rect(59,74,13,2,cloud_glow)
clouds.rect(96,66,32,2,cloud_lit)
clouds.rect(108,68,20,2,cloud_glow)

# Ocean and sunset reflection
sea_layer = new_canvas(W, H, None, name="sea")
sea_layer.rect(0,86,W,42,sea_dark)
sea_layer.rect(0,88,W,3,sea)
sea_layer.rect(0,94,W,2,sea_mid)
sea_layer.rect(0,103,W,2,sea)
sea_layer.rect(0,112,W,2,sea_mid)
sea_layer.rect(0,123,W,2,sea)
# Sun reflection broken into horizontal streaks
for x,y,w in [(24,87,29),(19,90,39),(27,93,24),(17,97,43),(25,101,29),(30,106,20),(34,111,12)]:
    sea_layer.rect(x,y,w,1,sea_glow)
for x,y,w in [(5,91,14),(66,91,19),(91,98,20),(3,106,23),(72,109,17),(98,118,24),(43,119,20)]:
    sea_layer.rect(x,y,w,1,sea_mid)

# Distant cliff, castle, towers, bridge-like wall
fort = new_canvas(W, H, None, name="castle and cliff")
# Cliff mass
fort.poly([(61,92),(68,85),(75,82),(83,80),(90,83),(97,82),(104,87),(111,89),(116,96),(128,99),(128,128),(49,128),(53,117),(57,108)], rock)
fort.poly([(77,91),(88,86),(98,88),(106,95),(95,96),(89,102),(75,101)], rock_mid)
fort.poly([(105,98),(128,101),(128,111),(116,108)], rock_mid)
fort.poly([(61,101),(70,96),(73,105),(65,114),(57,117)], rock_hi)
fort.poly([(91,109),(109,105),(119,110),(108,117),(88,119)], rock_mid)
# Castle foundation and walls
fort.rect(74,69,38,18,castle)
fort.rect(71,66,44,5,castle)
# Battlements along wall
for x in range(72,115,7):
    fort.rect(x,62,4,7,castle)
fort.rect(74,70,38,3,castle_mid)
fort.rect(79,76,28,11,castle_mid)
# Left tower
fort.rect(69,47,17,31,castle)
fort.rect(67,44,21,6,castle)
for x in (67,75,84):
    fort.rect(x,40,5,7,castle)
fort.rect(72,51,11,24,castle_mid)
fort.rect(69,51,3,24,castle_hi)
# Right tall tower
fort.rect(99,40,18,43,castle)
fort.rect(97,37,22,6,castle)
for x in (97,105,114):
    fort.rect(x,33,5,7,castle)
fort.rect(102,44,12,35,castle_mid)
fort.rect(99,44,3,33,castle_hi)
# Small central keep / peaked roof
fort.rect(87,55,13,25,castle)
fort.poly([(85,56),(93,48),(102,56)],castle)
fort.rect(90,57,7,20,castle_mid)
# Gate and windows
fort.rect(89,72,8,15,ink)
fort.circle(93,73,4,ink)
for x,y in [(75,55),(80,55),(104,48),(110,48),(104,60),(110,60),(91,60),(80,66)]:
    fort.rect(x,y,2,4,window)
    fort.set(x,y,gold_hi)
# Stone edge pixels
fort.rect(75,73,2,8,castle_hi)
fort.rect(108,74,2,8,castle_hi)
fort.rect(83,70,2,3,castle_hi)
# Flag poles and flags
fort.rect(76,27,1,15,ink)
fort.poly([(77,28),(89,31),(77,35)],gold)
fort.rect(106,18,1,17,ink)
fort.poly([(107,19),(121,23),(107,27)],gold_hi)
fort.rect(107,25,10,2,gold)

# Foreground rocks frame the image and add depth
front = new_canvas(W,H,None,name="foreground rocks")
front.poly([(0,101),(7,97),(14,99),(21,95),(28,101),(35,103),(39,111),(48,115),(53,128),(0,128)],ink)
front.poly([(0,108),(8,103),(18,106),(24,112),(32,115),(34,128),(0,128)],rock)
front.poly([(5,105),(14,101),(20,104),(12,108)],rock_hi)
front.poly([(18,111),(26,108),(34,113),(28,117)],rock_mid)
front.poly([(107,114),(113,108),(119,109),(123,103),(128,102),(128,128),(99,128)],ink)
front.poly([(112,117),(120,111),(128,111),(128,128),(106,128)],rock)
front.poly([(119,112),(125,107),(128,108),(128,115)],rock_hi)
# Foam lines against rocks
front.rect(35,115,13,1,foam)
front.rect(39,117,17,1,sea_mid)
front.rect(93,119,14,1,foam)
front.rect(87,121,18,1,sea_mid)

scene = flatten([bg, clouds, sea_layer, fort, front], name="castle-title-screen")

# Title is built at native bitmap size, then doubled for a crisp logo.
title_src = new_canvas(58, 9, None, name="title source")
title_src.text(1,1,"TIDEKEEP",gold_dark,font="5x7")
title_src.text(0,0,"TIDEKEEP",gold_hi,font="5x7")
title_big = title_src.select(0,0,58,9).resize(116,18).preview()
scene.blit(title_big,6,5)
# Small centered subtitle and ornamental rules
scene.text(26,25,"CROWN OF TIDES",gold_hi,font="5x7")
scene.rect(13,28,10,1,gold)
scene.rect(105,28,10,1,gold)
scene.set(11,28,gold_hi)
scene.set(116,28,gold_hi)

# Fine cinematic edge framing
scene.rect(0,0,128,2,ink)
scene.rect(0,126,128,2,ink)
scene.rect(0,2,2,124,ink)
scene.rect(126,2,2,124,ink)

view(scene, scale=4, margin=0)
finish(scene)
