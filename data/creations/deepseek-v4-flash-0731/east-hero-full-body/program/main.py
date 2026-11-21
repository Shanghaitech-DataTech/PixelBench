from pixelbench_api import *

W = H = 256
OUT = "#0c0b12"

# ------------------------------------------------------------------ background
bg = new_canvas(W, H, name="bg")
sky = ["#f1ecf5", "#e8e1f0", "#dcd3e8", "#cfc4de", "#c1b5d2", "#b3a6c6", "#a598ba", "#978bab"]
for i, col in enumerate(sky):
    bg.rect(0, i * 20, W, 20, col)
bg.rect(0, 160, W, 96, "#897da0")
bg.circle(80, 62, 26, "#f6efe0")
bg.circle(80, 62, 26, "#7a6f92", fill=False)
bg.line(56, 76, 62, 70, "#6f6588")
bg.line(62, 70, 68, 76, "#6f6588")
bg.line(72, 64, 77, 59, "#6f6588")
bg.line(77, 59, 82, 64, "#6f6588")

far = new_canvas(W, H, name="far")
far.poly([(0, 120), (30, 94), (56, 116), (88, 88), (114, 112), (142, 92), (170, 116), (198, 86), (226, 110), (255, 98), (255, 255), (0, 255)], "#9a90ba")

m1 = new_canvas(W, H, name="m1")
m1.rect(0, 116, W, 58, (228, 224, 240, 120))

mid = new_canvas(W, H, name="mid")
mid.poly([(0, 142), (22, 118), (50, 138), (80, 110), (108, 132), (136, 114), (164, 136), (194, 106), (222, 132), (255, 118), (255, 255), (0, 255)], "#7c74a0")

m2 = new_canvas(W, H, name="m2")
m2.rect(0, 164, W, 44, (226, 222, 238, 110))

near = new_canvas(W, H, name="near")
near.poly([(0, 166), (26, 144), (58, 160), (92, 140), (128, 158), (164, 136), (200, 154), (232, 142), (255, 156), (255, 255), (0, 255)], "#5e5880")

ground = new_canvas(W, H, name="ground")
ground.ellipse(128, 234, 92, 12, (26, 22, 40, 110))

# ------------------------------------------------------------------ character
char = new_canvas(W, H, name="char")

hair = "#151221"
face_c = "#7a5a3e"; face_d = "#5d4230"; face_l = "#937054"
robe = "#262c40"; rd = "#191e2f"; rl = "#37405e"; rf = "#454f6e"; inner = "#3f4a68"
sash = "#9c3b35"; sd = "#6d2320"
gold = "#c99b4e"; gd = "#96692c"
steel = "#aeb6c6"; stl = "#d5dae6"
tassel = "#a03a30"
shoe = "#14161f"

# hair behind head
char.poly([(64, 88), (188, 88), (196, 116), (190, 148), (172, 176), (150, 192), (126, 196), (100, 192), (76, 174), (62, 146), (58, 116)], hair)
char.poly([(64, 88), (188, 88), (196, 116), (190, 148), (172, 176), (150, 192), (126, 196), (100, 192), (76, 174), (62, 146), (58, 116)], OUT, fill=False)

# neck
char.rect(116, 118, 26, 26, face_d)

# face: lower half peeks below the tilted brim
char.poly([(102, 106), (140, 104), (148, 118), (140, 142), (122, 150), (98, 130)], face_c)
char.poly([(102, 106), (140, 104), (148, 118), (140, 142), (122, 150), (98, 130)], OUT, fill=False)
char.poly([(104, 114), (138, 110), (144, 120), (136, 134), (116, 132), (104, 124)], face_d)
char.line(112, 136, 126, 136, "#382720")
char.line(120, 144, 132, 142, face_l)

# hat: wide bamboo conical hat tilted down covering the upper face
bm = "#b5813f"; bd = "#8a5c2e"; bl = "#d8a96e"; rim = "#6e4522"; bh = "#e8c78f"
char.poly([(58, 92), (198, 92), (128, 22)], bm)
char.line(128, 24, 72, 88, bd)
char.line(128, 24, 96, 90, bd)
char.line(128, 24, 160, 90, "#9a6a38")
char.line(128, 24, 186, 86, bd)
char.line(128, 24, 128, 68, bd)
char.ellipse(128, 110, 64, 15, bl)
char.ellipse(128, 110, 64, 15, rim, fill=False)
char.ellipse(128, 102, 56, 9, bh, fill=False)
char.ellipse(128, 116, 58, 9, bm, fill=False)
char.poly([(58, 92), (198, 92), (128, 22)], OUT, fill=False)
# hair wisps escaping under the brim, framing the face
char.poly([(64, 100), (56, 110), (60, 118), (70, 108)], hair)
char.poly([(190, 100), (202, 110), (198, 118), (186, 108)], hair)

# gown
char.poly([(84, 146), (96, 142), (122, 146), (146, 144), (168, 148), (182, 174), (190, 204), (188, 232), (64, 232), (76, 202), (88, 178), (78, 154)], robe)
char.poly([(84, 146), (96, 142), (122, 146), (146, 144), (168, 148), (182, 174), (190, 204), (188, 232), (64, 232), (76, 202), (88, 178), (78, 154)], OUT, fill=False)
# collar lapels
char.poly([(94, 146), (120, 150), (114, 182), (96, 174)], rl)
char.poly([(134, 148), (160, 146), (166, 174), (148, 180)], rl)
char.poly([(116, 152), (142, 150), (136, 184), (122, 184)], inner)
char.poly([(116, 152), (142, 150), (136, 184), (122, 184)], OUT, fill=False)

# robe folds
char.line(96, 186, 90, 228, rd)
char.line(110, 188, 104, 230, rd)
char.line(126, 190, 122, 230, rd)
char.line(146, 190, 152, 226, rd)
char.line(162, 188, 170, 224, rd)
char.line(178, 186, 184, 218, rd)
char.line(86, 170, 80, 216, rf)
char.line(156, 170, 162, 210, rf)

# hem flutters
char.poly([(56, 224), (66, 232), (58, 240)], robe)
char.poly([(188, 230), (200, 226), (196, 240)], robe)

# sash
char.poly([(88, 174), (170, 178), (168, 190), (86, 186)], sash)
char.rect(116, 172, 26, 28, sd)
char.circle(112, 182, 7, sd)
char.circle(136, 184, 7, sd)
char.rect(108, 178, 40, 16, sash)
char.poly([(120, 196), (140, 196), (136, 230), (124, 226)], sd)
char.poly([(128, 196), (146, 196), (152, 224), (138, 220)], sash)
char.poly([(108, 178), (148, 180), (146, 190), (110, 188)], OUT, fill=False)

# left sleeve
char.poly([(82, 148), (114, 154), (120, 198), (104, 212), (74, 206), (64, 180)], rd)
char.poly([(82, 148), (114, 154), (120, 198), (104, 212), (74, 206), (64, 180)], OUT, fill=False)
char.line(92, 154, 106, 200, rf)
char.line(80, 162, 90, 198, rd)

# right sleeve toward sword
char.poly([(166, 150), (190, 160), (186, 184), (168, 188), (156, 176)], rl)
char.poly([(166, 150), (190, 160), (186, 184), (168, 188), (156, 176)], OUT, fill=False)
char.line(172, 158, 182, 178, rf)

# boots
char.poly([(80, 228), (104, 226), (106, 244), (90, 250), (78, 246)], shoe)
char.poly([(80, 228), (104, 226), (106, 244), (90, 250), (78, 246)], OUT, fill=False)
char.poly([(148, 226), (176, 228), (186, 244), (170, 250), (148, 248)], shoe)
char.poly([(148, 226), (176, 228), (186, 244), (170, 250), (148, 248)], OUT, fill=False)

# jian sword, point down, hand resting on it
char.circle(151, 162, 4, gold)
char.circle(151, 162, 4, gd, fill=False)
char.rect(149, 164, 7, 18, "#3a3126")
char.rect(151, 166, 3, 15, "#4d4234")
char.rect(143, 162, 20, 22, face_d)
char.rect(143, 162, 20, 22, OUT, fill=False)
char.line(145, 168, 161, 168, OUT)
char.line(145, 174, 161, 174, OUT)
char.line(145, 180, 161, 180, OUT)
char.rect(137, 182, 28, 4, gold)
char.rect(137, 182, 28, 4, gd, fill=False)
char.rect(149, 186, 8, 56, steel)
char.rect(151, 188, 3, 53, stl)
char.poly([(149, 242), (157, 242), (153, 249)], steel)
char.poly([(153, 242), (157, 242), (153, 248)], stl)
char.poly([(149, 242), (157, 242), (153, 249)], OUT, fill=False)
# tassel overlain on blade
char.poly([(152, 154), (160, 156), (157, 206), (150, 210), (147, 200), (150, 156)], tassel)
char.poly([(152, 154), (160, 156), (157, 206), (150, 210), (147, 200), (150, 156)], OUT, fill=False)
char.line(152, 156, 151, 206, "#7c2a24")
char.circle(154, 210, 5, tassel)

front = new_canvas(W, H, name="front")
front.rect(0, 226, W, 30, (244, 243, 249, 120))
front.rect(0, 242, W, 14, (250, 249, 252, 175))

# ------------------------------------------------------------------ combine
result = flatten([bg, far, m1, mid, m2, near, ground, char, front], name="result")

print(result.stats_text())
print("colors used:", result.stats()["colors_used"])

finish(result)
