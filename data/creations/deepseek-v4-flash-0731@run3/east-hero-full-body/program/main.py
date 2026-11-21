from pixelbench_api import new_canvas, flatten, finish, save

W = H = 256


def lerp_hex(h1, h2, t):
    def ch(i):
        a = int(h1[i:i + 2], 16)
        b = int(h2[i:i + 2], 16)
        return round(a + (b - a) * t)
    return "#%02x%02x%02x" % (ch(1), ch(3), ch(5))


bg = new_canvas(W, H, name="bg")
mist = new_canvas(W, H, name="mist")
mistf = new_canvas(W, H, name="mistf")
hero = new_canvas(W, H, name="hero")


def C(name, h):
    bg.color(h, name)


sky_top = "#eaf1f7"
sky_bot = "#9fb9cc"
for i in range(16):
    C("sky%02d" % i, lerp_hex(sky_top, sky_bot, i / 15))
C("moon", "#f7f9fb")
C("glow", "#dbe7ef")
C("mfar", "#b3c9d8")
C("mfarD", "#86a1b7")
C("mmid", "#8da9bf")
C("mmidD", "#63809a")
C("mnear", "#67849c")
C("mnearD", "#455f75")
C("msil", "#47596b")
C("msilD", "#27333f")
C("gndA", "#5d6a77")
C("gndB", "#47535f")
C("gndC", "#313c47")
C("gndD", "#1f2831")
C("mist1", (236, 243, 249, 96))
C("mist2", (227, 236, 244, 74))
C("mist3", (221, 232, 241, 88))
C("hatA", "#b98951")
C("hatB", "#9c6f3f")
C("hatC", "#7a542c")
C("hatD", "#57391d")
C("hatE", "#362308")
C("skin", "#d8b290")
C("skinS", "#b58f6c")
C("skinD", "#8a6748")
C("hair", "#16120f")
C("hairH", "#33261c")
C("robe0", "#212b38")
C("robe1", "#2f3b4a")
C("robe2", "#425463")
C("robe3", "#5a6f85")
C("robeS", "#10161f")
C("robeL", "#71879c")
C("inner", "#415363")
C("sash", "#b33b2c")
C("sashD", "#8d2b20")
C("sashL", "#d85f47")
C("sashG", "#d9b566")
C("sashGD", "#9b7d40")
C("stL", "#dfe7ee")
C("stM", "#a9bdcc")
C("stD", "#70889d")
C("stX", "#3d5063")
C("boot", "#2a211b")
C("bootS", "#42352a")
C("ink", "#0a0d11")

# ---------------- background ----------------
for i in range(16):
    bg.rect(0, i * 16, 256, 16, "sky%02d" % i)

bg.ellipse(196, 46, 30, 30, "glow")
bg.circle(196, 46, 15, "moon")


def ridge(cv, pts, fill, ln):
    cv.poly(pts + [(256, 256), (0, 256)], fill)
    cv.poly(pts, ln, fill=False)


far = [(0, 122), (30, 100), (54, 114), (84, 96), (112, 109), (138, 91), (164, 105), (190, 89), (216, 103), (240, 96), (255, 109)]
mid = [(0, 154), (28, 137), (60, 149), (92, 132), (124, 145), (156, 128), (188, 141), (220, 131), (244, 143), (256, 137)]
near = [(0, 184), (36, 167), (76, 179), (116, 163), (158, 177), (198, 161), (232, 173), (256, 165)]
sil = [(118, 198), (150, 173), (186, 185), (222, 172), (256, 177)]

ridge(bg, far, "mfar", "mfarD")
ridge(bg, mid, "mmid", "mmidD")
ridge(bg, near, "mnear", "mnearD")
ridge(bg, sil, "msil", "msilD")

# stone ground
bg.ellipse(128, 214, 104, 30, "gndB")
bg.ellipse(128, 224, 92, 22, "gndC")
for (sx, sy, srx, sry, sc) in [(70, 206, 22, 8, "gndD"), (170, 202, 26, 9, "gndD"), (200, 220, 20, 8, "gndA"), (110, 234, 30, 10, "gndA"), (48, 222, 18, 7, "gndD")]:
    bg.ellipse(sx, sy, srx, sry, sc)

# ---------------- mist ----------------
mist.ellipse(128, 98, 127, 20, "mist1")
mist.ellipse(128, 134, 127, 24, "mist2")
mist.ellipse(128, 170, 127, 26, "mist1")

# ---------------- hero ----------------
# boots
hero.ellipse(112, 226, 13, 9, "boot")
hero.ellipse(140, 226, 13, 9, "boot")
hero.ellipse(112, 230, 11, 6, "bootS")
hero.ellipse(140, 230, 11, 6, "bootS")

# back hair mass
hero.poly([(96, 82), (86, 98), (76, 130), (70, 160), (76, 180), (88, 170), (86, 140), (94, 114), (102, 98)], "hair")
hero.poly([(158, 82), (168, 98), (178, 128), (184, 158), (178, 178), (166, 168), (168, 140), (160, 114), (152, 98)], "hair")

# robe
hero.poly([
    (96, 116), (90, 130), (84, 150), (78, 174), (74, 196), (72, 212), (82, 226), (92, 222),
    (100, 230), (110, 236), (122, 238), (134, 236), (146, 230), (156, 224), (166, 228),
    (176, 214), (172, 194), (168, 172), (162, 150), (158, 130), (154, 116)
], "robe0")

# shoulder caps
hero.ellipse(98, 122, 14, 8, "robe1")
hero.ellipse(154, 122, 14, 8, "robe1")

# inner chest
hero.poly([(112, 120), (138, 120), (134, 148), (120, 152), (112, 142)], "robe3")
hero.path("M110,118 L124,124 L120,146", "robeS", fill=False)
hero.path("M140,118 L126,124 L128,146", "robeS", fill=False)
hero.path("M146,122 L166,140", "robeS", fill=False)
hero.path("M104,122 L84,140", "robeS", fill=False)

# hanging right sleeve
hero.poly([(152, 122), (166, 132), (176, 152), (180, 172), (172, 184), (162, 180), (160, 158), (156, 136), (150, 126)], "robe1")
hero.ellipse(168, 174, 10, 8, "inner")

# sash
hero.poly([(92, 150), (160, 150), (162, 164), (94, 164)], "sash")
hero.poly([(92, 150), (160, 150), (162, 154), (94, 154)], "sashL")
hero.ellipse(150, 158, 12, 9, "sashD")
hero.poly([(150, 154), (158, 158), (153, 192), (147, 190)], "sashD")
hero.poly([(182, 176), (172, 158), (176, 186), (188, 196), (184, 194)], "sashD")
hero.poly([(147, 186), (153, 188), (150, 200), (144, 198)], "sash")
hero.path("M176,180 Q162,172 170,160", "sash", fill=False)

# sword (in front of body, left side)
hero.poly([(80, 168), (90, 171), (88, 226), (82, 227)], "stM")
hero.line(83, 172, 84, 224, "stL")
hero.line(80, 169, 82, 226, "stD")
hero.rect(66, 164, 30, 7, "sashG")
hero.rect(66, 164, 30, 2, "sashGD")
hero.poly([(66, 164), (70, 164), (70, 162), (69, 160), (67, 162)], "sashGD")
hero.poly([(92, 164), (96, 164), (95, 160), (93, 162)], "sashGD")
hero.rect(78, 148, 10, 15, "stX")
hero.line(79, 150, 81, 162, "sashG")
hero.line(85, 150, 87, 162, "sashG")
hero.circle(82, 146, 5, "sashG")

# left sleeve (arm resting on sword)
hero.poly([(96, 118), (82, 130), (74, 146), (72, 160), (80, 164), (86, 154), (90, 140), (94, 128)], "robe1")

# hand on pommel
hero.circle(81, 151, 7, "skin")
hero.circle(78, 153, 3, "skinS")

# collar / neck
hero.poly([(114, 108), (120, 104), (130, 104), (136, 108), (134, 122), (126, 124), (116, 122)], "skinS")
hero.poly([(112, 116), (124, 120), (120, 134), (108, 128)], "inner")
hero.line(116, 108, 130, 108, "skinD")

# face
hero.poly([(108, 90), (114, 84), (124, 82), (134, 84), (140, 92), (138, 102), (130, 110), (120, 112), (112, 104)], "skin")
hero.ellipse(124, 88, 17, 8, "skinS")
hero.line(126, 104, 130, 108, "skinD")
hero.rect(120, 108, 10, 2, "skinD")
hero.poly([(104, 84), (96, 92), (98, 104), (108, 98)], "hair")
hero.poly([(146, 84), (152, 92), (150, 102), (142, 96)], "hair")
hero.poly([(96, 100), (80, 112), (70, 130), (74, 134), (88, 118), (100, 106)], "hair")

# cone of hat
hero.poly([(122, 38), (86, 56), (68, 74), (86, 80), (104, 68), (122, 64), (140, 68), (162, 80), (178, 74), (158, 56)], "hatA")
hero.line(122, 40, 88, 72, "hatC")
hero.line(122, 40, 104, 62, "hatC")
hero.line(122, 40, 122, 58, "hatC")
hero.line(122, 40, 152, 62, "hatC")
hero.line(122, 40, 170, 72, "hatC")

# brim (tilted down conical hat)
hero.ellipse(124, 84, 58, 15, "hatC")
hero.ellipse(124, 73, 58, 14, "hatB")
hero.ellipse(124, 78, 52, 10, "hatD")
hero.ellipse(124, 84, 20, 8, "skinS")   # under-brim shadow falling on face
hero.line(66, 76, 182, 76, "hatE")
hero.line(84, 70, 164, 70, "hatE")

# fabric flow lines
hero.path("M120,152 Q112,182 114,214", "robeS", fill=False)
hero.path("M132,152 Q140,184 136,216", "robeS", fill=False)
hero.path("M106,150 Q96,188 94,222", "robe2", fill=False)
hero.path("M146,150 Q156,186 152,220", "robe2", fill=False)
hero.path("M126,156 Q126,196 124,226", "robeS", fill=False)
hero.path("M96,220 Q124,230 156,220", "robeS", fill=False)
# highlight folds
hero.path("M92,132 Q86,160 84,188", "robeL", fill=False)
hero.path("M158,132 Q166,158 166,182", "robeL", fill=False)
hero.path("M100,122 Q96,132 104,142", "robeL", fill=False)
hero.path("M126,140 Q128,166 128,196", "robeL", fill=False)
# hat inner shading and highlight
hero.path("M96,54 Q108,46 120,44", "hatC", fill=False)
hero.path("M150,54 Q160,48 166,58", "hatB", fill=False)
hero.path("M76,70 Q92,62 108,60", "hatD", fill=False)
hero.line(88, 71, 96, 84, "hatD")
hero.line(160, 71, 152, 84, "hatD")

# dark ink outline around the figure
hero.outline("ink")

# ---------------- foreground mist ----------------
mistf.ellipse(128, 224, 127, 34, "mist3")
mistf.ellipse(160, 238, 110, 26, "mist2")
mistf.ellipse(60, 242, 86, 24, "mist3")
mistf.path("M0,196 Q50,206 96,200", "mist2", fill=False)
mistf.path("M120,240 Q170,248 250,242", "mist3", fill=False)

# ---------------- composite ----------------
result = flatten([bg, mist, hero, mistf], name="result")

print(result.stats_text())
print("visible colors:", result.stats()["colors_used"])

save("east-hero", result)

# quick region checks
probes = [
    (122, 42, "hat cone top"), (122, 66, "cone mid"), (122, 80, "brim inner"),
    (150, 92, "brim right"), (124, 106, "face"), (124, 126, "chest"),
    (100, 130, "left shoulder"), (150, 230, "robe hem"), (82, 170, "sword blade"),
    (82, 150, "hand/pommel"), (82, 200, "sword lower"), (66, 164, "sword guard"),
    (150, 158, "sash knot"), (120, 150, "sash"), (70, 170, "hair left"),
    (180, 165, "sash tail"), (122, 96, "under brim"), (196, 46, "moon"),
    (30, 100, "far ridge"), (120, 200, "robe center"), (112, 228, "boot"),
    (140, 120, "robe shoulder"),
]
print()
for (x, y, label) in probes:
    idx = result.get(x, y)
    print("%-16s (%d,%d) idx=%d %s" % (label, x, y, idx, result.color_name(idx)))

finish(result)
