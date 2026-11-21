import math
from pixelbench_api import *

c = new_canvas(64, 64)

# Palette
skin = c.color("#ffe0c2")
skin_sh = c.color("#dca37a")
skin_dk = c.color("#b57b54")

hair_dk = c.color("#183d22")
hair_md = c.color("#256636")
hair_lt = c.color("#3cb059")
hair_hi = c.color("#7ee898")

cloth_dk = c.color("#3b6e40")
cloth_md = c.color("#5da864")
cloth_lt = c.color("#8ce695")
cloth_hi = c.color("#b3f0b9")

leather_dk = c.color("#3d2210")
leather_md = c.color("#6b3f1e")
leather_lt = c.color("#9e6437")

gold_dk = c.color("#b57c14")
gold_md = c.color("#f0b82b")
gold_lt = c.color("#fae575")

wood_dk = c.color("#4a3219")
wood_md = c.color("#785632")
wood_lt = c.color("#a67d51")

steel_dk = c.color("#4a4f54")
steel_md = c.color("#828a91")
steel_lt = c.color("#c4ccd4")

white = c.color("#ffffff")
black = c.color("#111111")
eye_color = c.color("#1e90ff")
eye_color_dk = c.color("#104e8b")

# Back Hair
c.poly([(22, 16), (36, 16), (40, 25), (41, 40), (36, 48), (30, 48), (25, 40)], hair_dk)
c.poly([(23, 18), (35, 18), (39, 25), (40, 40), (35, 47), (30, 47), (26, 40)], hair_md)

# Bow on back
c.line(20, 45, 45, 15, steel_md) # Bow string
c.path("M 20 45 Q 30 25 45 15", wood_md, fill=False)
c.path("M 19 45 Q 29 25 44 15", wood_dk, fill=False)
c.path("M 21 45 Q 31 25 46 15", wood_lt, fill=False)

# Quiver
c.poly([(35, 14), (43, 16), (39, 36), (31, 34)], leather_dk)
c.poly([(35, 14), (42, 16), (38, 35), (31, 34)], leather_md)
c.line(35, 15, 41, 16, leather_lt)

# Arrows
for i in range(3):
    ox = 37 + i*2
    oy = 10 + i
    c.line(ox, oy, ox-3, oy+8, wood_lt)
    c.set(ox-1, oy+1, white)
    c.set(ox+1, oy+2, white)
    c.set(ox, oy+2, steel_md)

# Back Arm (Image Right)
c.poly([(32, 24), (37, 28), (36, 36), (33, 34)], skin_sh)
c.poly([(32, 24), (38, 28), (36, 32), (32, 29)], cloth_dk)
c.poly([(34, 31), (37, 33), (36, 37), (33, 35)], leather_dk) # Bracer
c.poly([(34, 31), (36, 33), (35, 36), (33, 35)], leather_md)

# Back Leg (Image Right)
c.rect(29, 38, 5, 10, skin_sh)
c.rect(29, 46, 6, 12, leather_dk)
c.rect(30, 46, 4, 12, leather_md)
c.line(30, 46, 34, 46, leather_lt)

# Torso
c.poly([(25, 24), (32, 23), (34, 30), (34, 38), (26, 38), (24, 30)], cloth_md)
c.poly([(25, 24), (31, 23), (33, 30), (33, 38), (27, 38), (25, 30)], cloth_lt)
c.poly([(26, 25), (30, 24), (32, 30), (32, 37), (28, 37), (26, 30)], cloth_hi)

# Belt
c.rect(24, 36, 11, 3, leather_dk)
c.rect(24, 36, 10, 2, leather_md)
c.rect(26, 35, 4, 4, gold_md)
c.rect(27, 36, 2, 2, gold_lt)

# Neck / Collar
c.poly([(25, 24), (32, 23), (29, 27)], cloth_dk) # Collar opening
c.poly([(26, 22), (31, 21), (29, 26)], skin_sh) # Neck
c.poly([(26, 22), (30, 22), (28, 25)], skin)

# Front Leg (Image Left)
c.rect(24, 38, 5, 10, skin)
c.rect(23, 46, 6, 12, leather_dk)
c.rect(24, 46, 4, 12, leather_md)
c.line(24, 46, 28, 46, leather_lt)

# Front Arm (Image Left)
c.poly([(25, 24), (20, 30), (22, 36), (25, 32)], skin)
c.poly([(25, 24), (19, 30), (22, 31), (26, 27)], cloth_md)
c.poly([(25, 24), (20, 30), (22, 30), (26, 26)], cloth_lt)
c.poly([(20, 31), (23, 37), (25, 35), (22, 30)], leather_dk) # Bracer
c.poly([(21, 31), (23, 36), (24, 35), (22, 31)], leather_md)

# Head
c.ellipse(27, 16, 7, 7, skin_sh)
c.ellipse(26, 16, 7, 7, skin)
c.poly([(22, 18), (26, 24), (30, 22), (31, 17)], skin)

# Ears
# Right ear (image left)
c.poly([(22, 18), (14, 16), (18, 21)], skin_sh)
c.poly([(22, 18), (15, 17), (19, 20)], skin)
# Left ear (image right)
c.poly([(31, 17), (40, 14), (33, 20)], skin_sh)
c.poly([(31, 17), (38, 15), (32, 19)], skin_dk)

# Face
c.set(23, 17, eye_color_dk)
c.set(24, 17, eye_color)
c.set(24, 16, black)
c.set(23, 16, white)

c.set(27, 17, eye_color_dk)
c.set(28, 17, eye_color)
c.set(28, 16, black)
c.set(27, 16, white)

# Nose
c.set(24, 20, skin_sh)
c.set(23, 20, skin_dk)

# Mouth
c.set(25, 22, skin_dk)
c.set(26, 22, skin_dk)

# Hair (Front and sides)
# Top volume
c.ellipse(27, 11, 8, 7, hair_dk)
c.ellipse(26, 11, 8, 7, hair_md)
c.ellipse(26, 10, 7, 6, hair_lt)
c.ellipse(25, 10, 6, 5, hair_hi)

# Bangs - fixed to not cover eyes
c.poly([(20, 13), (28, 11), (35, 13), (34, 14), (31, 13), (28, 14), (24, 13), (21, 14)], hair_md)
c.poly([(21, 13), (28, 12), (34, 13), (33, 14), (31, 13), (28, 14), (24, 13), (22, 14)], hair_lt)

# Side locks
c.path("M 32,14 Q 36,21 34,31 Q 32,21 31,16 Z", hair_md)
c.path("M 33,15 Q 35,21 33,29 Q 32,21 32,16 Z", hair_lt)

c.path("M 21,14 Q 17,21 19,31 Q 21,21 22,16 Z", hair_md)
c.path("M 22,15 Q 18,21 20,29 Q 21,21 22,16 Z", hair_lt)

finish(c)
