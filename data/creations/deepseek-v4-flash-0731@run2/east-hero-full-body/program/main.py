import math
from pixelbench_api import *

W, H = 256, 256
c = new_canvas(W, H, name="hero")
fig = new_canvas(W, H, name="figure")

def C(hexs):
    return c.color(hexs)

INK     = C("#17181e")
HAIR    = C("#0c0d11")
SKIN    = C("#f0c79f")
SKIN_S  = C("#d7aa7f")
HAT_L   = C("#e6cd8e")
HAT     = C("#c9a963")
HAT_D   = C("#9d813f")
HAT_E   = C("#6f5a2c")
ROBE    = C("#2b303b")
ROBE_D  = C("#1f232c")
ROBE2   = C("#363d4c")
ROBE3   = C("#495267")
SASH    = C("#8e2f2f")
SASH_D  = C("#6b2222")
SASH_L  = C("#c24e4e")
BLADE   = C("#e9edf5")
BLADE2  = C("#bac3d4")
BLADE_D = C("#8791a6")
GOLD    = C("#d8b458")
GRIP    = C("#5d4e33")
MOON    = C("#f7f1de")
MOON_D  = C("#e2d6b8")
M_FAR   = C("#c8d3de")
M_MID   = C("#a9b8c8")
M_NEAR  = C("#8ba0b4")
M_DK    = C("#6b7f95")
MIST1   = C("#ebeeea")
MIST2   = C("#e0e6e2")
BOOT    = C("#343a45")
BIRD    = C("#64748c")

def rot_pts(cx, cy, rx, ry, ang, n=90):
    a = math.radians(ang)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x = rx * math.cos(t)
        y = ry * math.sin(t)
        pts.append((round(cx + x * math.cos(a) - y * math.sin(a)),
                    round(cy + x * math.sin(a) + y * math.cos(a))))
    return pts

# ---------------- background ----------------
top = (229, 235, 243)
bot = (243, 216, 184)
steps = 16
for i in range(steps):
    y0 = round(206 * i / steps)
    y1 = round(206 * (i + 1) / steps)
    f = (i + 0.5) / steps
    col = tuple(round(top[k] + (bot[k] - top[k]) * f) for k in range(3))
    c.rect(0, y0, W, y1 - y0, col)

c.rect(0, 206, W, 50, M_DK)
c.circle(190, 58, 22, MOON)
c.circle(190, 58, 22, MOON_D, fill=False)

# faint cloud streaks
c.rect(30, 116, 58, 3, "#dfe6ee")
c.rect(72, 126, 34, 2, "#e8edf2")
c.rect(160, 130, 44, 2, "#e5eaf0")

# mountains
c.poly([(0, 158), (40, 128), (86, 146), (132, 116), (180, 140), (232, 122), (255, 146), (255, 214), (0, 214)], M_FAR)
c.poly([(0, 180), (56, 150), (104, 170), (152, 142), (204, 168), (255, 156), (255, 226), (0, 226)], M_MID)
c.poly([(0, 200), (66, 172), (122, 192), (176, 166), (226, 190), (255, 182), (255, 240), (0, 240)], M_NEAR)
c.poly([(0, 214), (48, 208), (96, 216), (150, 210), (204, 218), (255, 212), (255, 236), (0, 236)], MIST1)
c.poly([(0, 224), (64, 218), (120, 226), (176, 220), (232, 228), (255, 222), (255, 242), (0, 242)], MIST2)

# birds
c.line(58, 100, 66, 106, BIRD)
c.line(66, 106, 74, 100, BIRD)
c.line(92, 88, 100, 94, BIRD)
c.line(100, 94, 108, 87, BIRD)
c.line(36, 122, 42, 127, BIRD)
c.line(42, 127, 48, 121, BIRD)

# ground shadow for the figure
c.ellipse(128, 234, 58, 8, "#5c6d80")

# ---------------- figure ----------------
# long hair flowing behind (back layer)
fig.poly([(112, 74), (150, 78), (160, 106), (162, 136), (154, 172), (140, 192), (124, 194), (110, 170), (104, 134), (100, 100)], HAIR)

# neck and lower face
fig.rect(121, 98, 18, 16, SKIN_S)
fig.poly([(112, 72), (144, 74), (150, 88), (147, 104), (133, 115), (117, 109), (108, 92)], SKIN)
fig.poly([(112, 100), (117, 112), (126, 115), (128, 104)], SKIN_S)
fig.line(119, 103, 133, 104, INK)   # mouth
fig.line(115, 93, 113, 99, SKIN_S)   # nose hint
fig.line(118, 96, 122, 95, HAIR)    # hair fringe over forehead

# wide bamboo hat (douli), tilted down
fig.poly(rot_pts(128, 78, 48, 16, -8), HAT_E)
fig.poly(rot_pts(128, 71, 46, 15, -8), HAT)
fig.poly(rot_pts(126, 65, 42, 13, -8), HAT_L)
# weave marks on the brim
fig.line(128, 58, 84, 74, HAT_D)
fig.line(128, 58, 172, 74, HAT_D)
fig.line(104, 56, 86, 70, HAT_D)
fig.line(126, 54, 88, 64, HAT_D)
fig.line(150, 54, 170, 64, HAT_D)
# cone
fig.poly([(128, 24), (152, 64), (106, 64)], HAT)
fig.poly([(128, 24), (106, 64), (121, 62)], HAT_L)
fig.poly([(128, 24), (152, 64), (139, 60)], HAT)
fig.line(110, 62, 146, 62, HAT_D)
fig.poly([(128, 24), (106, 64), (152, 64)], INK, fill=False)
fig.poly(rot_pts(128, 74, 47, 15.5, -8), INK, fill=False)

# flowing long robe
fig.poly([(98, 110), (120, 106), (154, 106), (162, 120), (166, 152), (168, 190), (164, 224), (150, 232), (134, 226), (116, 233), (98, 228), (86, 214), (82, 168), (90, 132)], ROBE)
fig.poly([(90, 132), (84, 170), (88, 210), (96, 222), (92, 182), (98, 142)], ROBE3)
fig.line(120, 114, 114, 224, ROBE_D)
fig.line(133, 116, 127, 228, ROBE_D)
fig.line(146, 118, 142, 230, ROBE_D)
fig.poly([(146, 110), (160, 118), (164, 142), (156, 152), (146, 136), (140, 116)], ROBE2)

# crossed collar
fig.line(126, 102, 100, 112, INK)
fig.line(126, 102, 156, 110, INK)
fig.line(127, 103, 101, 113, ROBE3)

# loose hair: bangs under the brim, strands falling beside the face
fig.poly([(114, 86), (130, 84), (144, 88), (143, 96), (136, 99), (122, 97), (116, 92)], HAIR)
fig.poly([(146, 90), (158, 100), (164, 124), (162, 148), (156, 162), (148, 156), (152, 126), (146, 106)], HAIR)
fig.poly([(106, 92), (100, 114), (96, 140), (101, 152), (107, 142), (108, 118)], HAIR)
fig.poly([(150, 84), (158, 98), (163, 122), (161, 148), (155, 160), (150, 150), (152, 124)], HAIR)
fig.path("M 140 122 C 152 132, 156 150, 152 172 C 149 184, 145 192, 140 198", HAIR)

# straight jian sword, hand resting on the hilt, blade slanting down
fig.poly([(150, 149), (161, 152), (160, 247), (149, 245)], INK)   # blade dark edge
fig.poly([(151, 150), (159, 152), (157, 246), (150, 245)], BLADE)
fig.line(154, 152, 153, 245, BLADE2)
fig.poly([(137, 147), (160, 144), (163, 150), (139, 152)], GOLD)  # guard
fig.rect(146, 128, 8, 16, GRIP)
fig.line(147, 132, 153, 133, INK)
fig.line(147, 137, 153, 138, INK)
fig.line(147, 142, 153, 143, INK)
fig.circle(150, 126, 3, GOLD)   # pommel
# hand resting on the hilt/guard
fig.ellipse(150, 148, 8, 10, SKIN)
fig.ellipse(147, 146, 6, 8, SKIN_S)
fig.line(144, 149, 156, 147, INK)

# sash with knot and flowing ribbons (kept left of the blade)
fig.poly([(98, 148), (148, 144), (152, 166), (100, 172)], SASH)
fig.poly([(126, 146), (148, 144), (144, 164), (124, 166)], SASH_D)
fig.line(104, 152, 146, 149, SASH_L)
fig.poly([(112, 168), (126, 166), (122, 202), (110, 200)], SASH_D)
fig.poly([(120, 170), (134, 168), (130, 206), (118, 204)], SASH)
fig.poly([(126, 168), (142, 166), (138, 172), (124, 174)], SASH_D)

# boots
fig.poly([(96, 228), (114, 230), (114, 242), (96, 241)], BOOT)
fig.poly([(140, 232), (158, 230), (161, 243), (140, 244)], BOOT)
c.poly([(240, 198), (255, 194), (255, 214)], M_DK)
c.poly([(24, 212), (54, 206), (70, 218), (38, 222)], M_NEAR)

# dark outline around the whole figure
fig.outline(INK)
c.blit(fig, 0, 0)

# foreground mist across the feet
c.poly([(0, 228), (52, 222), (104, 230), (158, 224), (210, 232), (255, 226), (255, 246), (0, 246)], MIST1)
c.poly([(0, 236), (60, 232), (120, 238), (182, 233), (240, 240), (255, 237), (255, 248), (0, 248)], MIST2)

print(c.stats_text())
finish(c)
