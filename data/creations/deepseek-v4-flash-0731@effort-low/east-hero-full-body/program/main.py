from pixelbench_api import *

W = H = 256
c = new_canvas(W, H, name="east-hero")

OUT = (24, 24, 32)          # dark outline
SKIN  = (231, 199, 168)
SKIN2 = (207, 165, 128)      # shadowed skin
SKIN3 = (184, 142, 106)
HAIR  = (36, 36, 46)
HAIRH = (58, 58, 70)
ROBE  = (44, 50, 70)         # dark navy robe
ROBEH = (88, 100, 128)
ROBEM = (58, 66, 92)
ROBED = (30, 33, 48)
SASH  = (150, 46, 54)
SASHH = (196, 96, 96)
SASHD = (108, 30, 40)
TAN   = (208, 166, 110)      # bamboo hat
TANL  = (230, 196, 148)
TAND  = (168, 128, 82)
BLADE = (200, 210, 220)
BLADEH= (228, 236, 242)
BLADED= (142, 154, 168)
GOLD  = (198, 158, 92)
GOLDD = (148, 112, 60)
MIST  = (228, 236, 240)

def shade_poly(pts, fill, out=OUT, f=0.90):
    c.poly(pts, out, fill=True)
    n = len(pts)
    cx = sum(p[0] for p in pts) / n
    cy = sum(p[1] for p in pts) / n
    ip = [(cx + (x - cx) * f, cy + (y - cy) * f) for (x, y) in pts]
    c.poly(ip, fill, fill=True)

def shade_ellipse(x, y, rx, ry, fill, out=OUT, f=1.0):
    c.ellipse(x, y, rx + 1, ry + 1, out, fill=True)
    c.ellipse(x, y, rx, ry, fill, fill=True)

# ---------- background: misty mountains ----------
bands = [
    (0, 55, (226, 231, 235)),
    (55, 112, (211, 220, 226)),
    (112, 165, (197, 208, 215)),
    (165, 205, (183, 196, 205)),
    (205, 256, (172, 187, 196)),
]
for y0, y1, col in bands:
    c.rect(0, y0, W, y1 - y0, col)

# distant mountain ridges
c.poly([(0, 158), (34, 112), (72, 96), (112, 128), (152, 98),
        (198, 122), (255, 148), (255, 256), (0, 256)], (176, 192, 202), fill=True)
c.poly([(0, 172), (52, 132), (106, 160), (150, 132), (204, 160),
        (232, 148), (255, 168), (255, 256), (0, 256)], (150, 168, 182), fill=True)
c.poly([(10, 200), (80, 168), (132, 200), (196, 170), (255, 200),
        (255, 256), (0, 256)], (122, 142, 158), fill=True)

# mist ribbons across mountains
for (y, w, col) in [(150, 10, (218, 228, 233)), (176, 14, (228, 236, 240)),
                    (206, 16, (236, 242, 245)), (222, 20, (244, 248, 250))]:
    c.rect(0, y, W, w, col)

# ---------- back hair (flowing) ----------
bhair = [(108, 78), (96, 96), (84, 122), (74, 156), (70, 190), (82, 216),
         (98, 196), (110, 168), (116, 150), (126, 196), (136, 220), (150, 200),
         (158, 172), (166, 150), (157, 106), (146, 84), (140, 74), (126, 70), (116, 72)]
c.poly(bhair, HAIR, fill=True)

# ---------- long flowing robe (torso + skirt) ----------
robe_pts = [
    (86, 102), (100, 88), (126, 82), (152, 88), (166, 102),   # shoulders
    (178, 132), (196, 170), (204, 216), (206, 232), (170, 234),
    (82, 234), (48, 232), (54, 216), (74, 170), (84, 132),
]
shade_poly(robe_pts, ROBE, f=0.93)
# inner robe shading (chest highlight)
shade_poly([(104, 106), (122, 92), (132, 92), (148, 104), (152, 132),
           (146, 158), (130, 170), (122, 170), (106, 158), (100, 132)], ROBEM, f=0.90)
# broad skirt shadow near ground
c.poly([(58, 214), (70, 200), (130, 196), (182, 200), (200, 214),
        (204, 232), (170, 234), (84, 234), (52, 232)], ROBED, fill=True)

# ---------- sword (straight jian), point resting on ground at right ----------
bx = 190                       # blade x
c.poly([(bx - 3, 130), (bx + 3, 130), (bx + 2, 216), (bx, 226), (bx - 2, 216)], BLADE, fill=True)
c.line(bx - 1, 132, bx, 224, BLADEH)
c.poly([(bx - 3, 130), (bx + 3, 130), (bx + 2, 138), (bx - 2, 138)], BLADED, fill=True)
# guard
shade_poly([(bx - 11, 120), (bx + 11, 120), (bx + 13, 129), (bx - 13, 129)], GOLD, f=0.55)
# handle
c.poly([(bx - 3, 104), (bx + 3, 104), (bx + 3, 121), (bx - 3, 121)],
       (190, 170, 120), fill=True)
shade_poly([(bx - 4, 100), (bx + 4, 100), (bx + 4, 104), (bx - 4, 104)], GOLD, f=0.4)
c.poly([(bx - 3, 100), (bx + 3, 100), (bx + 3, 121), (bx - 3, 121)], OUT, fill=True)
c.rect(bx - 1, 102, 2, 18, (210, 196, 160))

# ---------- sleeves / arms ----------
# right sleeve (toward sword) with flowing wide cuff
rarm = [(164, 100), (182, 112), (196, 124), (192, 140), (180, 138), (170, 126)]
shade_poly(rarm, ROBEH, f=0.88)
# right hand gripping handle
shade_ellipse(186, 112, 7, 8, SKIN)
# left arm folded, sleeve hanging at left side
larm = [(90, 104), (76, 116), (66, 132), (58, 150), (70, 156), (84, 142), (92, 126)]
shade_poly(larm, ROBEH, f=0.88)
# left hand tucked
shade_ellipse(74, 150, 7, 9, SKIN)

# ---------- sash ----------
shade_poly([(86, 132), (168, 132), (172, 148), (84, 148)], SASH, f=0.90)
# sash knot
shade_rect = shade_ellipse(126, 140, 12, 10, SASHH)
shade_ellipse(126, 140, 12, 10, SASHH)
# trailing sash tails flowing to the left
c.poly([(88, 144), (70, 158), (52, 188), (44, 208), (56, 190), (74, 166), (90, 152)], SASH, fill=True)
c.poly([(40, 200), (30, 210), (38, 216), (50, 198), (46, 196)], SASH, fill=True)
shade_poly([(126, 150), (118, 178), (110, 204), (100, 222), (112, 196), (122, 170), (130, 152)], SASHD, f=0.88)

# flowing robe folds
folds = [
    ("M 96 150 C 92 178 78 206 66 230", ROBED),
    ("M 110 152 C 108 184 104 212 100 232", ROBED),
    ("M 132 152 C 134 184 138 214 142 232", ROBED),
    ("M 150 150 C 156 180 164 206 178 230", ROBED),
    ("M 88 100 C 94 112 98 124 92 140", ROBEH),
    ("M 112 96 C 108 116 110 130 106 142", ROBEH),
    ("M 142 98 C 146 116 144 130 150 142", ROBEH),
]
for d, col in folds:
    c.path(d, col, fill=False)

# ---------- neck ----------
shade_poly([(118, 108), (138, 108), (136, 120), (120, 120)], SKIN, f=0.6)
shade_poly([(118, 108), (138, 108), (136, 120), (120, 120)], SKIN2, f=0.55)

# ---------- face (lower half visible under hat) ----------
face = [(112, 92), (124, 84), (134, 92), (136, 112), (128, 122), (118, 122), (112, 112)]
shade_poly(face, SKIN, f=0.9)
# shadow cast by broad brim (hidden eyes, dark band)
c.poly([(112, 90), (134, 90), (136, 100), (130, 96), (124, 100), (118, 96), (112, 100)], SKIN2, fill=True)
# nose hint
c.line(120, 96, 119, 110, SKIN3)
c.line(121, 108, 118, 112, SKIN3)
# mouth
c.line(114, 116, 126, 115, (120, 92, 76))
# chin shadow
c.line(116, 119, 128, 119, SKIN2)

# ---------- front hair framing face ----------
c.poly([(110, 88), (106, 104), (104, 120), (100, 108), (106, 92), (114, 82)], HAIR, fill=True)
c.poly([(136, 88), (142, 106), (144, 122), (140, 108), (132, 90)], HAIR, fill=True)

# ---------- wide bamboo conical hat (douli) ----------
# crown cone
crown = [(94, 58), (100, 44), (112, 34), (126, 30), (140, 34), (152, 44), (158, 58),
         (150, 52), (140, 46), (126, 43), (112, 46), (102, 52)]
c.poly(crown, TAND, fill=True)
shade_poly([(96, 57), (102, 45), (114, 35), (126, 31), (138, 35), (150, 45), (156, 57)], TAN, f=0.88)
# cone ridges (radiating weave lines)
for a in [(100,50),(110,44),(126,41),(142,44),(152,50)]:
    pass
c.line(110, 46, 118, 60, TANL)
c.line(126, 42, 126, 60, TANL)
c.line(142, 46, 134, 60, TANL)
c.line(150, 52, 146, 62, TANL)
# wide brim
shade_ellipse(126, 60, 60, 15, TAN, f=0.94)
shade_ellipse(126, 62, 52, 11, TANL, f=0.94)
# brim underside shadow
c.poly([(70, 62), (182, 62), (180, 70), (70, 70)], OUT, fill=True)
c.poly([(72, 63), (180, 63), (176, 69), (74, 69)], (150, 116, 74), fill=True)
# tie ribbon under hat
c.line(126, 66, 126, 84, TAND)

# ---------- re-trace decisive dark outlines ----------
for p in [robe_pts]:
    c.poly(p, OUT, fill=False)

# floor mist / ground shadow
c.poly([(40, 222), (96, 216), (150, 216), (210, 222), (214, 240), (34, 240)], (196, 208, 214), fill=True)
# faint hero shadow drift
c.ellipse(126, 236, 70, 8, (158, 172, 182), fill=True)

finish(c)
print(c.stats_text())
