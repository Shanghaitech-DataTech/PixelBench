import math
from pixelbench_api import new_canvas, finish

W = H = 256

# ---------------- palette ----------------
OUT      = (22, 14, 20)
SKIN     = (233, 195, 157)
SKIN_SH  = (203, 158, 118)
SKIN_DK  = (176, 130, 94)
HAIR     = (18, 13, 18)
HAIR_HI  = (72, 64, 76)
ROBE     = (38, 44, 57)
ROBE_DK  = (25, 29, 39)
ROBE_HI  = (64, 73, 90)
BAM      = (193, 160, 101)
BAM_HI   = (226, 196, 142)
BAM_DK   = (158, 123, 73)
BAM_DK2  = (118, 88, 50)
CROWN    = (142, 109, 64)
SASH     = (182, 66, 58)
SASH_DK  = (126, 42, 40)
SASH_HI  = (212, 98, 78)
GOLD     = (199, 159, 84)
BLADE    = (152, 164, 178)
BLADE_HI = (230, 238, 246)
BLADE_DK = (86, 97, 113)
GRIP     = (86, 60, 36)
LIP      = (150, 90, 80)

# ---------------- background ----------------
bg = new_canvas(W, H)

# sky gradient
for i in range(18):
    t = i / 17
    col = (int(243 - t * 34), int(246 - t * 40), int(250 - t * 42))
    bg.rect(0, i * 14, W, 14, col)

# pale moon
bg.circle(206, 94, 26, (238, 242, 248))
bg.circle(206, 94, 30, (222, 230, 238), fill=False)
bg.circle(206, 94, 34, (210, 220, 232), fill=False)

# birds
bg.poly([(232, 58), (238, 52), (244, 58)], (122, 136, 152), fill=False)
bg.poly([(216, 44), (221, 39), (226, 44)], (150, 162, 176), fill=False)
bg.poly([(120, 54), (126, 48), (132, 54)], (122, 136, 152), fill=False)

def arcpts(cx, cy, rx, ry, t0, t1, n=56):
    pts = []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n
        pts.append((cx + rx * math.cos(t), cy + ry * math.sin(t)))
    return pts

def ridge(fn, col):
    pts = [(0, fn(0))]
    for x in range(4, W + 1, 4):
        pts.append((x, fn(x)))
    pts += [(W, H), (0, H)]
    bg.poly(pts, col)

far  = lambda x: 118 + 15 * math.sin(x * 0.045) + 9 * math.sin(x * 0.016 + 1.2)
mid  = lambda x: 160 + 22 * math.sin(x * 0.03 + 0.8) + 9 * math.sin(x * 0.05 + 0.1)
near = lambda x: 168 + 26 * math.sin(x * 0.02 + 2.3) + 10 * math.sin(x * 0.05 + 0.3)
mistA = lambda x: 150 + 6 * math.sin(x * 0.055 + 0.5)
mistB = lambda x: 178 + 7 * math.sin(x * 0.045 + 2.0)
mistC = lambda x: 204 + 6 * math.sin(x * 0.04 + 1.2)
gnd  = lambda x: 226 + 5 * math.sin(x * 0.05 + 1.1)

ridge(far, (176, 189, 203))
ridge(mistA, (208, 218, 229))
ridge(mid, (150, 166, 184))
ridge(mistB, (190, 203, 217))
ridge(near, (124, 141, 161))

# pines on mid ridge
for (px, py, pc) in [(46, 164, (110, 124, 144)), (196, 146, (110, 124, 144)), (222, 150, (110, 124, 144))]:
    bg.poly([(px, py), (px - 5, py + 10), (px + 5, py + 10)], pc)
    bg.poly([(px, py + 4), (px - 6, py + 15), (px + 6, py + 15)], pc)
ridge(mistC, (200, 212, 226))

# pines on near ridge
for (px, py, pc) in [(30, 182, (74, 90, 112)), (232, 160, (74, 90, 112)), (18, 168, (74, 90, 112))]:
    bg.poly([(px, py), (px - 5, py + 10), (px + 5, py + 10)], pc)
    bg.poly([(px, py + 4), (px - 6, py + 15), (px + 6, py + 15)], pc)

ridge(gnd, (216, 228, 240))
# footing shadow
bg.ellipse(134, 240, 66, 11, (140, 154, 172))

# ---------------- character layer ----------------
fg = new_canvas(W, H)

# hair flying behind
fg.poly([(98, 106), (82, 116), (72, 134), (68, 150), (76, 152), (84, 136), (94, 122)], HAIR)
fg.poly([(156, 108), (170, 118), (178, 132), (182, 144), (176, 148), (170, 134), (162, 120)], HAIR)

# back hair masses beside head
fg.poly([(108, 102), (96, 112), (86, 132), (80, 158), (76, 180), (85, 190), (94, 180), (96, 152), (99, 130), (106, 114)], HAIR)
fg.poly([(152, 102), (164, 112), (170, 132), (174, 158), (177, 178), (170, 186), (161, 176), (159, 152), (154, 126), (146, 110)], HAIR)
# hair wisps in front of shoulders
fg.poly([(112, 108), (104, 122), (100, 138), (98, 150), (104, 148), (106, 128), (114, 116)], HAIR)
fg.poly([(150, 110), (158, 122), (162, 136), (158, 144), (153, 132), (147, 116)], HAIR)

# torso / robe
fg.poly([(96, 130), (114, 122), (150, 122), (168, 130), (176, 146), (184, 168), (192, 194), (194, 214),
         (186, 232), (172, 227), (158, 236), (144, 229), (130, 237), (116, 231), (102, 236), (86, 229),
         (80, 212), (84, 182), (90, 154)], ROBE)

# flutter pieces at hem
fg.poly([(82, 210), (64, 216), (58, 226), (70, 232), (84, 224)], ROBE_DK)
fg.poly([(198, 214), (210, 218), (208, 228), (196, 222)], ROBE_DK)
fg.poly([(80, 214), (66, 220), (62, 230), (74, 232), (84, 226)], ROBE_HI)

# boots
fg.poly([(106, 226), (120, 228), (118, 240), (104, 238)], ROBE_DK)
fg.poly([(142, 228), (156, 228), (154, 240), (142, 240)], ROBE_DK)

# right hand (resting on the sword)
fg.poly([(147, 138), (157, 134), (166, 134), (170, 139), (168, 148), (160, 153), (149, 151), (144, 146)], SKIN)
fg.line(147, 140, 160, 138, SKIN_DK)
fg.line(146, 146, 160, 144, SKIN_DK)
fg.line(149, 150, 160, 148, SKIN_DK)
fg.line(163, 141, 165, 147, SKIN_DK)

# blade, guard, handle (drawn above the hand so the grip passes through it)
fg.path("M 150,152 C 160,145 165,140 170,126", SKIN_DK, fill=False)  # arm slit hint
fg.poly([(156, 148), (168, 150), (162, 240), (152, 238)], BLADE)
fg.line(155, 150, 152, 238, BLADE_DK)
fg.line(167, 150, 162, 240, BLADE_DK)
fg.line(160, 152, 157, 238, BLADE_HI)
fg.rect(147, 147, 22, 5, GOLD)
fg.rect(147, 147, 22, 2, (160, 122, 58))
fg.ellipse(148, 143, 4, 8, GRIP)
fg.ellipse(148, 145, 2, 4, (120, 84, 48))
fg.circle(159, 139, 3, (150, 116, 60))
fg.poly([(158, 140), (161, 141), (160, 147), (157, 147)], SKIN_DK)
fg.circle(160, 143, 2, SKIN)

# right sleeve (arm toward sword)
fg.poly([(164, 126), (176, 134), (182, 150), (178, 164), (168, 166), (160, 158), (156, 142), (158, 130)], ROBE)
fg.line(168, 132, 172, 150, OUT)

# wrist cuff covering forearm join
fg.poly([(140, 140), (172, 136), (176, 144), (172, 154), (166, 156), (138, 150)], ROBE_DK)
fg.line(142, 143, 168, 141, ROBE_HI)

# left hanging sleeve
fg.poly([(94, 126), (84, 136), (78, 162), (74, 190), (72, 212), (80, 224), (90, 214), (90, 184), (96, 158), (98, 140)], ROBE)
fg.ellipse(84, 214, 11, 7, ROBE_DK)
fg.ellipse(84, 217, 8, 5, ROBE_DK)
fg.circle(83, 218, 6, SKIN_SH)
fg.line(80, 216, 86, 216, SKIN_DK)

# belt / sash
fg.poly([(94, 156), (174, 154), (176, 164), (170, 170), (96, 172), (92, 164)], SASH_DK)
fg.poly([(96, 156), (172, 154), (174, 161), (98, 163)], SASH)
fg.circle(101, 164, 7, SASH)
fg.circle(101, 162, 5, SASH_HI)
fg.poly([(98, 160), (108, 162), (106, 186), (100, 200), (96, 207), (92, 194), (94, 174)], SASH_DK)
fg.poly([(176, 158), (198, 150), (216, 136), (230, 124), (233, 130), (218, 144), (198, 158)], SASH)
fg.poly([(180, 166), (200, 170), (214, 162), (224, 154), (222, 160), (206, 170)], SASH_HI)

# long sash flowing left
fg.poly([(90, 156), (70, 164), (58, 178), (54, 194), (62, 196), (70, 182), (84, 172)], SASH_DK)
fg.poly([(90, 160), (74, 168), (66, 180), (72, 186), (82, 174), (92, 168)], SASH_HI)

# blade sparkle
fg.circle(161, 182, 2, BLADE_HI)
fg.line(157, 182, 165, 182, BLADE_HI)
fg.line(161, 178, 161, 186, BLADE_HI)

# robe folds
fg.line(104, 150, 96, 220, ROBE_DK)
fg.line(112, 172, 108, 228, ROBE_DK)
fg.line(124, 176, 120, 232, ROBE_DK)
fg.line(140, 174, 140, 234, ROBE_DK)
fg.line(160, 172, 164, 230, ROBE_DK)
fg.line(116, 162, 112, 214, ROBE_HI)
fg.line(96, 130, 92, 150, ROBE_HI)
fg.line(168, 132, 172, 150, OUT)

# neck + collar
# face (lower half; brim will cover the top)
fg.poly([(116, 106), (146, 108), (151, 120), (145, 136), (132, 141), (116, 137), (110, 125)], SKIN)
fg.poly([(118, 108), (144, 110), (142, 121), (119, 119)], SKIN_SH)
fg.line(123, 129, 136, 129, LIP)
# chin contour
fg.line(116, 134, 122, 138, SKIN_DK)
fg.line(146, 132, 140, 139, SKIN_DK)

# neck
fg.poly([(119, 130), (145, 130), (143, 152), (121, 152)], SKIN_SH)
fg.poly([(119, 130), (145, 130), (143, 152), (121, 152)], OUT, fill=False)
fg.line(122, 132, 128, 152, OUT)
fg.line(142, 132, 136, 152, OUT)

# deep shadow under the hat brim
fg.poly([(112, 120), (150, 122), (146, 127), (114, 125)], SKIN_DK)
fg.poly([(118, 106), (144, 108), (142, 112), (120, 110)], SKIN_DK)

# loose strands framing the face (drawn over brim)
fg.poly([(112, 108), (104, 118), (100, 132), (97, 145), (103, 143), (106, 126), (113, 115)], HAIR)
fg.poly([(112, 83), (104, 96), (100, 112), (98, 126), (103, 124), (105, 104), (113, 90)], HAIR)
fg.poly([(150, 110), (157, 120), (160, 132), (156, 139), (152, 127), (147, 116)], HAIR_HI)
fg.poly([(150, 84), (158, 96), (162, 112), (158, 121), (153, 111), (148, 94)], HAIR_HI)
fg.poly([(124, 79), (130, 89), (126, 93), (120, 85)], HAIR_HI)

# hat
fg.ellipse(132, 100, 61, 18, OUT)
fg.ellipse(132, 100, 59, 16, BAM)
fg.poly(arcpts(132, 100, 57, 14, 0, math.pi), BAM_DK)
fg.path("M 74,100 A 58,15 0 0 0 190,100", BAM_HI, fill=False)
fg.line(114, 82, 86, 88, BAM_DK2)
fg.line(148, 82, 172, 88, BAM_DK2)
fg.line(106, 94, 82, 106, BAM_DK2)
fg.line(156, 94, 180, 106, BAM_DK2)
# dome (toplight: upper half bright bowl, lower half shaded)
fg.poly(arcpts(132, 88, 30, 25, 0, math.pi), BAM_HI)
fg.poly(arcpts(132, 88, 30, 25, math.pi, 2 * math.pi), BAM_DK)
fg.ellipse(132, 88, 30, 25, OUT, fill=False)
# shading arcs
fg.path("M 103,90 A 29,24 0 0 0 161,90", BAM_DK2, fill=False)
fg.line(112, 64, 152, 66, BAM_HI)
fg.line(103, 73, 161, 75, BAM_DK2)
# band
fg.ellipse(132, 96, 31, 9, OUT, fill=False)
fg.rect(101, 92, 62, 7, BAM_DK)
fg.line(101, 98, 163, 98, BAM_HI)

# dark silhouette outline
fg.outline(OUT)
fg.outline(OUT)

# composite character over background
bg.blit(fg, 0, 0)

# foreground mist at the feet
bg.poly([(40, 226), (70, 222), (96, 228), (92, 240), (122, 234), (120, 246), (58, 246), (28, 242)], (226, 233, 241))
bg.poly([(150, 230), (192, 226), (224, 232), (216, 244), (242, 238), (238, 248), (150, 248)], (232, 238, 244))
bg.poly([(102, 236), (134, 232), (142, 244), (98, 244)], (220, 228, 237))
bg.poly([(158, 236), (188, 232), (196, 244), (154, 244)], (222, 230, 239))

print(bg.stats_text())

finish(bg)
