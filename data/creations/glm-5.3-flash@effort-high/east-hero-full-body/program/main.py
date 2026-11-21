from pixelbench_api import *

W = H = 256
OUTLINE = "#171521"

# ---------------- background: misty mountains ----------------
bg = new_canvas(W, H, name="bg")

sky = ["#b2c4d0", "#bac9d4", "#c2ced7", "#cad4d9", "#d2dad c"]
sky = ["#b2c4d0", "#bac9d4", "#c2ced7", "#cad4d9", "#d2dadc",
       "#dae0e0", "#e0e6e4", "#e6eae7", "#ebeee9", "#eff1ec"]
step = 200 // len(sky)
for i, col in enumerate(sky):
    bg.rect(0, i * step, W, step + 1, col)
bg.rect(0, 196, W, 20, "#eff1ec")

# mountain ridges (far to near)
bg.poly([(0, 152), (28, 122), (58, 142), (92, 106), (128, 140), (162, 114),
         (198, 142), (228, 120), (255, 144), (255, 256), (0, 256)], "#93a7b4")
bg.poly([(0, 178), (42, 152), (82, 174), (122, 150), (162, 172), (206, 152),
         (255, 174), (255, 256), (0, 256)], "#7b90a0")
bg.poly([(0, 204), (52, 184), (102, 200), (152, 182), (212, 200),
         (255, 188), (255, 256), (0, 256)], "#61768a")

# tiny distant pagoda on the far ridge
pg = "#8296a4"
bg.rect(193, 139, 14, 5, pg)
bg.rect(191, 135, 18, 3, pg)
bg.rect(196, 130, 8, 5, pg)
bg.rect(194, 126, 12, 3, pg)
bg.line(200, 120, 200, 126, pg)

# mist bands drifting across the ranges
bg.rect(0, 130, W, 4, "#cfdadd")
bg.rect(0, 146, W, 8, "#d7e0e2")
bg.rect(0, 168, W, 6, "#dde4e5")
bg.rect(0, 190, W, 10, "#e3e9e9")
bg.ellipse(60, 208, 46, 7, "#dde4e5")
bg.ellipse(190, 204, 52, 8, "#dde4e5")
bg.ellipse(128, 197, 62, 6, "#e3e9e9")

# ground plane
bg.rect(0, 212, W, 44, "#c7cfd1")
bg.rect(0, 212, W, 3, "#d6dcdd")
bg.rect(0, 228, W, 2, "#bcc5c7")
bg.rect(0, 240, W, 2, "#bcc5c7")
bg.poly([(30, 236), (44, 230), (58, 238), (52, 246), (34, 246)], "#a3adb0")
bg.poly([(196, 232), (210, 228), (222, 236), (214, 244), (198, 242)], "#a3adb0")
bg.ellipse(130, 247, 42, 6, "#aeb7ba")   # cast shadow

# ---------------- character ----------------
ch = new_canvas(W, H, name="hero")

ROBE   = "#2b2938"
ROBE_D = "#1e1c28"
ROBE_L = "#3a3850"
ROBE_R = "#454360"
HAIR   = "#241c28"
HAIR_L = "#3a3040"
SKIN   = "#d8b090"
SKIN_D = "#a8826a"
HAT    = "#c2a066"
HAT_D  = "#a8874a"
HAT_U  = "#8a6c3e"
SASH   = "#8e3038"
SASH_D = "#6b2229"
SASH_L = "#a84a4a"
BLADE  = "#b9c6cf"
BLADE_D= "#8494a0"
BLADE_L= "#d5dee3"
STEEL  = "#4a5560"
GRIP   = "#3a2c22"

# back hair mass (behind the robe)
ch.rect(112, 88, 44, 30, HAIR)

# robe body with flowing jagged hem
ch.poly([(100, 108), (168, 106), (175, 120), (164, 150), (177, 196), (187, 226),
         (178, 233), (168, 227), (157, 239), (145, 231), (133, 243), (121, 233),
         (109, 241), (99, 229), (90, 223), (95, 192), (104, 150), (96, 120)], ROBE)

# robe folds
ch.line(118, 150, 112, 225, ROBE_L)
ch.line(136, 152, 134, 232, ROBE_L)
ch.line(152, 150, 158, 220, ROBE_L)
ch.line(126, 150, 122, 228, ROBE_D)
ch.line(145, 152, 148, 226, ROBE_D)
# rim light along the left edge
ch.line(98, 118, 103, 148, ROBE_R)
ch.line(103, 150, 97, 190, ROBE_R)
ch.line(97, 192, 92, 220, ROBE_R)
# shadow down the right side
ch.line(171, 116, 179, 190, ROBE_D)
ch.line(179, 192, 184, 222, ROBE_D)

# collar (V overlap, three-quarter)
ch.poly([(124, 116), (140, 114), (134, 140), (128, 140)], ROBE_L)
ch.line(116, 110, 132, 142, "#1a1824")
ch.line(150, 108, 134, 142, "#1a1824")

# sash + knot + trailing ends
ch.poly([(101, 146), (166, 143), (167, 157), (102, 160)], SASH)
ch.poly([(102, 155), (167, 152), (167, 157), (102, 160)], SASH_D)
ch.line(102, 147, 166, 144, SASH_L)
ch.rect(100, 148, 8, 10, SASH_D)
ch.rect(101, 149, 6, 4, SASH_L)
ch.poly([(108, 158), (118, 157), (128, 196), (117, 201)], SASH)
ch.line(112, 162, 122, 196, SASH_D)
ch.poly([(122, 158), (132, 157), (144, 206), (132, 210)], "#7a2830")

# left sleeve (viewer left) reaching down to the sword grip
ch.poly([(100, 110), (114, 114), (106, 148), (100, 166), (86, 162), (92, 136)], ROBE)
ch.line(88, 162, 100, 166, "#1a1824")
ch.line(104, 120, 98, 150, ROBE_D)

# right sleeve bent back, wide and flowing
ch.poly([(164, 108), (176, 114), (184, 138), (181, 162), (192, 184), (180, 192),
         (168, 166), (163, 138)], ROBE)
ch.line(181, 163, 191, 184, "#1a1824")
ch.line(170, 120, 178, 150, ROBE_D)
ch.circle(176, 165, 3, SKIN)          # relaxed hand at sleeve mouth

# ---- jian sword, point down, hand resting on the grip ----
ch.poly([(91, 176), (96, 176), (96, 236), (93, 243), (91, 236)], BLADE)
ch.line(95, 178, 95, 235, BLADE_D)
ch.line(93, 178, 93, 234, BLADE_L)
ch.rect(86, 172, 17, 4, STEEL)
ch.rect(86, 172, 17, 1, "#6a7884")
ch.rect(91, 158, 5, 15, GRIP)
for wy in (161, 164, 167, 170):
    ch.line(91, wy, 95, wy, "#241a14")
ch.circle(93, 156, 3, "#5a4a34")
ch.circle(92, 155, 1, "#8a7452")

# hand wrapping the grip
ch.circle(94, 164, 5, SKIN)
ch.line(90, 162, 98, 162, SKIN_D)
ch.line(90, 166, 98, 166, SKIN_D)
ch.circle(90, 160, 2, SKIN)

# ---- head: neck, shadowed face under the hat ----
ch.rect(126, 100, 12, 10, SKIN)
ch.line(126, 104, 137, 104, SKIN_D)
ch.poly([(118, 96), (148, 94), (142, 104), (124, 106)], SKIN)   # lower face / chin
ch.poly([(112, 86), (152, 84), (150, 96), (114, 98)], "#2a2028")  # brim shadow
ch.line(130, 101, 138, 100, SKIN_D)                              # mouth hint

# loose hair strands over the shoulders
ch.poly([(110, 84), (102, 98), (96, 122), (100, 146), (106, 142), (102, 120),
         (112, 98), (116, 88)], HAIR)
ch.poly([(152, 84), (162, 96), (170, 120), (166, 150), (159, 144), (163, 120),
         (150, 98), (146, 88)], HAIR)
ch.line(104, 100, 100, 130, HAIR_L)
ch.line(164, 100, 168, 132, HAIR_L)

# ---- wide conical douli hat, tilted down ----
ch.poly([(130, 26), (68, 86), (106, 91), (150, 89), (194, 80)], HAT)
ch.poly([(68, 86), (106, 91), (150, 89), (194, 80), (193, 85), (150, 94),
         (106, 96), (68, 91)], HAT_U)
ch.line(130, 28, 100, 88, HAT_D)
ch.line(130, 28, 130, 89, HAT_D)
ch.line(130, 28, 160, 86, HAT_D)
ch.line(130, 28, 78, 86, "#9a7c48")
ch.circle(130, 25, 2, "#9a7c48")
ch.line(68, 86, 106, 91, "#d8bc84")

ch.outline(OUTLINE)

# ---------------- foreground mist + drifting leaves ----------------
m = new_canvas(W, H, name="mist")
m.rect(0, 218, W, 38, (226, 234, 236, 150))
m.ellipse(50, 214, 44, 8, (228, 236, 238, 130))
m.ellipse(200, 210, 50, 9, (228, 236, 238, 130))
m.ellipse(128, 224, 70, 8, (232, 240, 242, 110))
m.ellipse(140, 186, 40, 5, (230, 238, 240, 90))
for (lx, ly) in ((70, 120), (182, 92), (212, 152), (88, 172), (160, 60)):
    m.rect(lx, ly, 2, 2, (201, 168, 106, 210))
    m.rect(lx + 2, ly + 1, 1, 1, (201, 168, 106, 160))

result = flatten([bg, ch, m], name="result")
print(result.stats_text())
finish(result)
