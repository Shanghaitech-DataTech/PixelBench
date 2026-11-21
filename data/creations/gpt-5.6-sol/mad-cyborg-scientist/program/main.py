# 64x64 mad cyborg scientist portrait
from pixelbench_api import *

result = new_canvas(64, 64, background="#081317", name="mad-cyborg-scientist")

# Palette
bg = "#081317"; bg2 = "#10282a"; bg3 = "#17413e"
ink = "#11151a"; near = "#20252a"
white = "#e7eee5"; hair_mid = "#aebdb5"; hair_sh = "#637876"
skin = "#d6966e"; skin_hi = "#ffc392"; skin_sh = "#925547"; skin_deep = "#5a3435"
steel = "#718895"; steel_hi = "#b9ccd0"; steel_sh = "#3d515c"; steel_dark = "#263740"
cyan = "#43f6ee"; cyan_hi = "#d4ffff"; red = "#f04452"; red_hi = "#ff9b72"
coat = "#c7c9b7"; coat_hi = "#f1edd8"; coat_sh = "#747c70"
leather = "#704631"; leather_hi = "#aa7047"; gold = "#d7a949"

# Background: hard laboratory pools of light and panel fragments
result.rect(0, 0, 64, 64, bg)
result.poly([(0,0),(28,0),(16,64),(0,64)], "#0d2426")
result.rect(3, 6, 2, 18, bg3); result.rect(6, 8, 1, 13, cyan)
result.rect(52, 2, 9, 2, bg3); result.rect(56, 5, 5, 1, steel_sh)
result.rect(1, 42, 8, 2, bg3); result.rect(2, 46, 5, 1, cyan)
result.set(9,10,cyan); result.set(11,6,red); result.set(53,12,cyan)
# Backlight halo
result.poly([(15,7),(24,2),(43,3),(53,14),(51,37),(43,49),(15,45),(8,26)], "#18383a")
result.dither(11, 11, 41, 34, ["#18383a", "#20484a"], pattern="checker")

# Torso silhouette and dirty lab coat
result.poly([(17,38),(9,46),(5,64),(57,64),(54,48),(45,39)], ink)
result.poly([(18,39),(11,46),(8,64),(29,64),(30,47)], coat_sh)
result.poly([(17,40),(12,48),(11,62),(20,62),(25,44)], coat)
result.poly([(45,39),(53,47),(56,64),(36,64),(34,46)], coat)
result.poly([(45,42),(50,49),(53,62),(45,62),(38,45)], coat_hi)
# torn lapels
result.poly([(23,39),(29,46),(26,57),(18,43)], coat_hi)
result.poly([(39,39),(32,47),(37,56),(47,43)], coat_sh)
result.line(14,52,20,50,skin_deep); result.set(16,53,skin_deep)
result.line(46,55,51,57,hair_sh); result.set(48,52,leather)

# Leather apron and straps
result.poly([(24,43),(40,43),(45,64),(19,64)], leather)
result.rect(25,46,14,18,"#5a392d")
result.line(20,42,27,48,leather_hi); result.line(44,42,38,48,leather_hi)
result.rect(17,57,29,4, ink); result.rect(18,58,27,2, leather_hi)
# Belt buckle, pouches, tools
result.rect(29,57,7,5, gold); result.rect(31,58,3,3,ink)
result.rect(20,60,7,4, leather); result.rect(38,60,7,4, leather)
result.rect(47,54,2,9,steel_hi); result.rect(49,52,2,11,steel_sh); result.set(48,53,red)
result.line(15,58,14,63,steel_hi); result.line(16,58,18,63,gold)

# Neck
result.poly([(24,33),(41,33),(42,44),(22,44)], skin_sh)
result.rect(27,34,10,10,skin); result.rect(27,39,10,3,skin_hi)
result.poly([(37,33),(43,34),(40,44),(35,44)], steel_dark)
result.rect(38,37,4,3,steel); result.set(39,38,cyan)

# Head base: human left and machine right
result.poly([(18,11),(25,6),(38,6),(47,13),(48,25),(43,36),(35,41),(24,38),(17,29),(15,18)], ink)
result.poly([(18,13),(24,8),(32,8),(34,36),(29,39),(23,35),(18,28),(17,18)], skin)
# Human face strong lit plane / shadow
result.poly([(19,13),(26,9),(31,11),(31,29),(27,28),(25,35),(20,29),(18,20)], skin_hi)
result.poly([(17,21),(22,22),(23,31),(29,36),(24,36),(18,29)], skin_sh)
result.poly([(25,12),(32,10),(33,20),(29,24),(27,19)], "#e7a775")
# ear
result.rect(15,21,4,8,skin_sh); result.rect(16,23,2,4,skin_hi); result.set(16,26,skin_deep)

# Robotic skull half and plate geometry
result.poly([(33,8),(41,8),(47,14),(48,25),(43,35),(35,39),(32,34),(33,22)], steel_dark)
result.poly([(35,9),(41,10),(46,15),(44,20),(35,19)], steel)
result.poly([(37,10),(41,11),(44,14),(43,16),(36,15)], steel_hi)
result.poly([(34,21),(47,20),(46,28),(41,34),(34,34)], steel_sh)
result.poly([(36,23),(45,22),(44,27),(39,29),(35,27)], steel)
result.line(34,17,37,20,ink); result.line(43,16,47,18,ink)
result.line(39,9,39,13,steel_dark); result.set(40,12,gold)
# cheek vent and jaw seams
result.rect(39,29,6,2,steel_dark)
result.set(40,30,steel_hi); result.set(42,30,steel_hi); result.set(44,30,steel_hi)
result.line(34,32,38,36,steel_hi); result.line(38,36,43,33,ink)
result.rect(43,24,3,3,near); result.set(44,25,red)

# Human eye, brow and wrinkles
result.line(20,17,29,15,skin_deep); result.line(21,16,29,14,ink)
result.rect(21,18,8,3,white); result.rect(25,18,3,3,ink); result.set(26,18,cyan_hi)
result.line(20,22,28,23,skin_sh); result.line(19,25,23,24,skin_sh)
# Cyborg glowing eye in black socket
result.poly([(34,16),(38,13),(44,15),(45,19),(41,22),(35,20)], ink)
result.rect(37,16,6,4,cyan); result.rect(39,15,3,6,cyan)
result.rect(39,16,2,3,cyan_hi); result.set(43,18,"#159d9f")
result.set(34,17,cyan); result.set(45,18,cyan)
# Nose, split bridge
result.line(30,20,28,28,skin_sh); result.line(28,28,32,29,skin_deep)
result.line(32,19,32,29,steel_hi); result.set(30,27,skin_hi)

# Maniacal grin: wide black cavity, bright uneven teeth
result.poly([(21,29),(27,31),(34,30),(41,28),(39,35),(33,38),(26,35)], skin_deep)
result.poly([(22,30),(28,32),(34,31),(40,29),(38,34),(32,37),(26,34)], ink)
result.poly([(23,30),(28,32),(34,32),(39,30),(37,33),(31,35),(26,33)], white)
result.line(28,31,28,34,skin_deep); result.line(33,31,33,35,skin_deep); result.line(37,30,37,33,steel_dark)
result.set(24,30,red_hi); result.line(27,36,35,38,skin_deep)

# Messy white hair silhouette and locks
result.poly([(15,16),(10,13),(15,10),(12,6),(20,7),(21,2),(26,6),(30,1),(33,6),(39,2),(40,7),(47,5),(44,11),(50,12),(45,15),(39,10),(31,9),(24,10),(18,18)], ink)
result.poly([(16,14),(12,12),(18,9),(15,6),(22,8),(22,3),(27,7),(31,2),(32,8),(38,4),(37,9),(44,7),(41,12),(47,12),(43,15),(36,10),(28,9),(21,11)], white)
result.poly([(14,12),(20,9),(24,10),(18,16)], hair_mid)
result.poly([(23,8),(27,5),(28,10)], hair_sh)
result.poly([(32,7),(38,4),(36,10)], hair_mid)
result.poly([(38,9),(44,8),(41,14)], hair_sh)
result.line(18,10,22,8,cyan_hi); result.set(14,13,hair_sh)
# loose side wisps
result.line(14,14,10,19,hair_mid); result.line(12,18,14,23,white)
result.line(45,10,49,15,hair_mid); result.line(48,14,47,19,white)

# Brain electrode plugs and wires
result.rect(20,5,3,4,steel_dark); result.rect(21,4,2,3,steel_hi); result.set(22,5,red)
result.rect(34,5,3,4,steel_dark); result.rect(35,4,2,3,steel_hi); result.set(35,5,cyan)
result.line(21,4,17,1,red); result.line(17,1,12,3,red)
result.line(36,4,41,1,cyan); result.line(41,1,46,3,cyan)
result.set(12,3,red_hi); result.set(46,3,cyan_hi)

# Raised exposed robotic arm on right, behind hand but in front of torso
result.poly([(47,42),(51,35),(56,36),(59,45),(58,57),(52,58)], ink)
result.poly([(49,42),(52,36),(55,37),(57,45),(56,54),(53,56),(50,50)], steel_sh)
result.poly([(52,38),(54,38),(55,47),(53,48)], steel_hi)
result.rect(50,44,7,4,steel); result.rect(51,45,5,2,steel_hi)
result.set(52,46,cyan); result.set(56,43,red)
# cable bundles along arm
result.line(49,40,47,48,red); result.line(51,39,49,51,cyan)
result.line(57,40,60,49,gold); result.line(58,48,57,55,ink)
# Prosthetic hand near face, claw-like fingers
result.poly([(49,34),(48,28),(50,24),(53,25),(53,32),(55,25),(58,24),(58,33),(60,28),(62,29),(60,38),(56,41),(51,39)], ink)
result.poly([(50,34),(50,28),(51,25),(52,26),(52,34),(54,36),(55,27),(57,25),(57,35),(58,37),(59,30),(61,30),(59,37),(56,39),(52,38)], steel)
result.rect(52,34,6,5,steel_hi); result.rect(53,36,4,3,steel_sh)
result.set(55,37,cyan); result.set(59,31,red)
# finger joints
result.set(51,29,steel_hi); result.set(56,29,steel_hi); result.set(60,32,steel_hi)
# dangling hand cables
result.line(58,39,61,44,red); result.line(56,39,59,46,cyan); result.set(61,45,red_hi)

# Foreground contrast chips / coat grime
result.set(9,61,coat_hi); result.set(12,56,near); result.set(44,48,skin_deep)
result.rect(6,63,52,1,ink)

view(result, scale=8, margin=0)
finish(result)
