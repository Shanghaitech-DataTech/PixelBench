import random
from pixelbench_api import new_canvas, finish

W = H = 256
rng = random.Random(2024)
c = new_canvas(W, H, name="ancient_dragon_battle")

OUT = "#0d0912"

# ---- palette ----
SKY = ["#350f45", "#481448", "#5a1a4a", "#6c2049", "#7d2647", "#8f2d44",
       "#a03540", "#b13d3b", "#c24636", "#d25030", "#e05a2b", "#ea6528"]
G_DARK = "#d15a3a"
G_MID = "#ea7a38"
G_LIT = "#f7a03a"
SUN = "#ffd25e"
SUNC = "#ffe98a"
CLOUD_A = "#5c1c4a"
CLOUD_B = "#6a2148"
CLOUD_C = "#7c2848"
CLOUD_D = "#a03050"
MT1 = "#3a1d46"
MT2 = "#2c1538"
HILL = "#231030"
GROUND = "#180d20"
GROUND2 = "#110a18"
STONE = "#403048"
STONE_L = "#54405e"
STONE_D = "#2a1e34"
WOOD = "#542e1c"
WOOD_L = "#6e3c24"
WOOD_D = "#2a1810"
FIRE_R = "#d84a16"
FIRE_O = "#f07a1c"
FIRE_Y = "#ffb82e"
FIRE_W = "#ffe066"
WIN_F = "#ff6a1c"
SMOKE = ["#6a4e58", "#543e4c", "#3f2f3e", "#2c2030"]
ARM = "#5e5870"
HELM = "#c8c2d0"
SPEAR = "#b08a44"
TIP = "#f0ecef"
SH_D = "#6a2028"
SH_L = "#a8383c"
FLAG = "#8a1e26"
DR_BODY = "#341d4e"
DR_BODY_L = "#6a3a72"
DR_MEM = "#7a4a78"
DR_MEM_F = "#5c3360"
DR_JAW = "#231240"
HORN = "#6e5a44"
EYE = "#ffb42e"
BR_O = "#e86a14"
BR_Y = "#ff9c28"
BR_C = "#ffd44a"
ARROW = "#a57a3c"
ARROW_H = "#e8d8c0"
SOL = "#332450"
SOL2 = "#1e1430"
SHAFT = "#8a6a38"
EMB = ["#ff8c1a", "#ffb02e", "#ffd64a", "#ff5e14"]
POLE = "#3a2a20"
GATE = "#160d18"
BARS = "#3a2c34"
EDGE = "#0c0712"

# ================= SKY =================
n = len(SKY)
for y in range(154):
    c.line(0, y, 255, y, SKY[min(n - 1, y * n // 154)])

# sun + glow
c.circle(192, 130, 50, G_DARK)
c.circle(192, 130, 36, G_MID)
c.circle(192, 130, 24, G_LIT)
c.circle(192, 130, 17, SUN)
c.circle(192, 130, 12, SUNC)

# clouds
clouds = [(58, 38, 30, 5, CLOUD_A), (120, 26, 44, 6, CLOUD_B), (176, 44, 34, 5, CLOUD_C),
          (36, 62, 26, 5, CLOUD_D), (168, 66, 30, 5, CLOUD_B), (100, 80, 44, 5, CLOUD_D),
          (10, 86, 58, 4, CLOUD_C), (204, 22, 36, 5, CLOUD_A)]
for (cx, cy, rx, ry, cc) in clouds:
    c.ellipse(cx, cy, rx, ry, cc)
# cloud top highlights
c.line(58, 34, 74, 34, CLOUD_D)
c.line(70, 60, 92, 60, CLOUD_A)
c.line(150, 24, 172, 24, CLOUD_A)

# ================= LAND =================
# distant mountains
c.poly([(0, 150), (20, 136), (46, 148), (70, 130), (100, 146), (128, 136),
       (158, 148), (188, 138), (218, 148), (244, 136), (256, 148), (256, 168), (0, 168)], MT1)
c.poly([(0, 158), (30, 146), (58, 156), (90, 144), (120, 156), (152, 148),
       (182, 158), (212, 150), (240, 158), (256, 156), (256, 176), (0, 176)], MT2)
# hill for the castle
c.poly([(56, 160), (84, 150), (118, 146), (156, 146), (196, 152), (224, 162),
       (242, 174), (242, 200), (56, 200)], HILL)
c.rect(0, 196, 256, 60, GROUND)
c.rect(0, 226, 256, 30, GROUND2)

# ================= CASTLE =================
# central donjon
c.rect(112, 80, 36, 120, OUT)
c.rect(114, 82, 32, 116, STONE)
for x in range(114, 146, 8):
    c.rect(x, 74, 4, 8, OUT)
    c.rect(x, 76, 4, 5, STONE)
for wx, wy in [(118, 152), (132, 152), (126, 118)]:
    c.rect(wx, wy, 3, 6, OUT)
    c.rect(wx + 1, wy + 2, 1, 2, WIN_F)
# donjon gate
c.rect(120, 176, 16, 24, OUT)
c.rect(122, 182, 12, 16, GATE)
for gx in range(124, 134, 3):
    c.line(gx, 182, gx, 198, BARS)
# banners on donjon
c.line(112, 54, 112, 80, POLE)
c.poly([(112, 56), (130, 60), (112, 66)], FLAG)
c.line(147, 62, 147, 88, POLE)
c.poly([(147, 64), (131, 68), (147, 74)], FLAG)

# left tower
c.rect(84, 124, 30, 78, OUT)
c.rect(86, 126, 26, 74, STONE)
c.rect(84, 122, 30, 4, STONE_D)
for x in range(86, 110, 8):
    c.rect(x, 116, 4, 8, OUT)
    c.rect(x, 118, 4, 5, STONE)
c.rect(92, 140, 3, 6, OUT)
c.rect(93, 142, 1, 3, WIN_F)
c.rect(96, 162, 4, 14, OUT)
c.rect(97, 164, 2, 10, STONE_D)

# right tower
c.rect(146, 120, 30, 82, OUT)
c.rect(148, 122, 26, 78, STONE)
c.rect(146, 118, 30, 4, STONE_D)
for x in range(148, 172, 8):
    c.rect(x, 112, 4, 8, OUT)
    c.rect(x, 114, 4, 5, STONE)
c.rect(154, 140, 3, 6, OUT)
c.rect(155, 142, 1, 3, WIN_F)
c.rect(158, 164, 4, 14, OUT)
c.rect(159, 166, 2, 10, STONE_D)

# curtain wall between towers
c.rect(86, 148, 84, 54, OUT)
c.rect(88, 150, 80, 50, STONE_L)
for x in range(88, 164, 10):
    c.rect(x, 142, 5, 8, OUT)
    c.rect(x, 144, 5, 5, STONE)
# wall texture lines
for yy in (160, 172, 184):
    c.line(88, yy, 168, yy, STONE_D)
# gangplank from left tower to wall
c.poly([(44, 110), (48, 106), (66, 128), (62, 132)], WOOD)
c.poly([(44, 110), (48, 106), (66, 128), (62, 132)], OUT, fill=False)
# burning flag on wall
c.line(160, 148, 160, 158, POLE)
c.poly([(160, 148), (146, 150), (158, 156)], FLAG)

# ================= FIRE =================
# left tower burns a little
for _ in range(12):
    c.circle(96 + rng.randint(0, 22), 120 - rng.randint(0, 12), rng.randint(1, 3),
            rng.choice([FIRE_O, FIRE_R, FIRE_Y]))
# donjon ablaze
c.ellipse(130, 78, 42, 18, "#c23c16")
for k in range(34):
    fx = 116 + rng.randint(0, 28)
    fy = 80 - rng.randint(2, 24)
    r = rng.randint(2, 5)
    col = FIRE_R if r < 3 else (FIRE_O if r < 4 else FIRE_Y)
    c.circle(fx, fy, r, col)
for _ in range(16):
    c.circle(120 + rng.randint(0, 20), 90 - rng.randint(0, 8), 2, FIRE_W)
# right tower on fire
for k in range(18):
    c.circle(150 + rng.randint(0, 22), 118 - rng.randint(0, 16), rng.randint(1, 4),
            rng.choice([FIRE_R, FIRE_O, FIRE_Y]))

# smoke plumes
for i in range(11):
    sy = 86 - i * 7
    sx = 136 + i * 10 + rng.randint(-3, 3)
    r = 7 + i * 2
    c.circle(sx, sy, r, SMOKE[min(3, i // 3)])
    c.circle(sx - 3 + rng.randint(-2, 2), sy - rng.randint(0, 5), max(2, r - 3),
            SMOKE[min(3, i // 3)])
# extra far smoke drifting right
for k in range(6):
    c.circle(196 + k * 8, 16 + rng.randint(-3, 8), 6 + k, SMOKE[3])

# ================= SIEGE TOWERS =================
# left siege tower
c.rect(10, 108, 34, 108, OUT)
c.rect(12, 110, 30, 104, WOOD_D)
c.rect(12, 110, 30, 5, WOOD)
for yy in range(122, 214, 12):
    c.line(11, yy, 43, yy, WOOD)
c.line(12, 110, 43, 120, WOOD_L)
c.line(12, 208, 43, 198, WOOD_L)
c.circle(18, 214, 6, OUT)
c.circle(18, 214, 5, WOOD_D)
c.set(18, 214, OUT)
c.circle(32, 214, 6, OUT)
c.circle(32, 214, 5, WOOD_D)
c.set(32, 214, OUT)
# knights atop left tower
def knight(cx, ty, arm, shd):
    c.line(cx - 1, ty - 9, cx + 2, ty + 1, SPEAR)
    c.set(cx, ty - 10, TIP)
    c.set(cx + 3, ty, TIP)
    c.rect(cx - 1, ty, 4, 5, OUT)
    c.rect(cx, ty + 1, 2, 3, arm)
    c.set(cx, ty, HELM)
    c.rect(cx - 2, ty + 2, 2, 3, OUT)
    c.rect(cx - 2, ty + 3, 2, 2, shd)

knight(96, 128, ARM, SH_D)
knight(104, 128, ARM, SH_D)
knight(14, 128, SOL, SH_L)
knight(22, 128, SOL, SH_L)
knight(32, 126, SOL2, SH_D)

# right siege tower
c.rect(212, 112, 34, 104, OUT)
c.rect(214, 114, 30, 98, WOOD_D)
c.rect(214, 114, 30, 5, WOOD)
for yy in range(126, 214, 12):
    c.line(213, yy, 245, yy, WOOD)
c.line(214, 114, 245, 124, WOOD_L)
c.circle(220, 214, 6, OUT)
c.circle(220, 214, 5, WOOD_D)
c.set(220, 214, OUT)
c.circle(234, 214, 6, OUT)
c.circle(234, 214, 5, WOOD_D)
c.set(234, 214, OUT)
knight(152, 126, ARM, SH_D)
knight(160, 126, ARM, SH_D)
knight(218, 124, SOL, SH_L)
knight(228, 122, SOL, SH_L)
knight(238, 122, SOL2, SH_D)

# ================= FOREGROUND =================
def soldier(cx, ty, arm, helm, shd, shaftc):
    c.line(cx - 1, ty - 8, cx + 1, ty + 1, shaftc)
    c.set(cx, ty - 8, TIP)
    c.rect(cx - 1, ty, 3, 6, OUT)
    c.rect(cx, ty + 1, 2, 4, arm)
    c.set(cx, ty, helm)
    c.rect(cx - 2, ty + 1, 2, 3, OUT)
    c.rect(cx - 2, ty + 2, 2, 2, shd)

for i in range(16):
    soldier(12 + i * 15, 236, SOL, HELM, SH_L, SHAFT)
for i in range(17):
    soldier(8 + i * 15, 249, SOL2, SOL, SH_D, SHAFT)
# archers loosing arrows
knight(40, 212, ARM, SH_D)
knight(204, 214, ARM, SH_D)

# ================= DRAGON =================
# tail
c.poly([(168, 58), (204, 66), (230, 74), (204, 78), (170, 74)], DR_BODY)
c.poly([(168, 58), (204, 66), (230, 72), (204, 76), (170, 72)], OUT, fill=False)
for (sx, sy) in [(188, 56), (204, 62), (220, 68)]:
    c.poly([(sx, sy), (sx + 2, sy - 6), (sx + 6, sy + 1)], HORN)
# far wing
c.poly([(118, 52), (92, 28), (64, 12), (44, 6), (52, 14), (80, 26), (104, 42)], DR_MEM_F)
c.poly([(118, 52), (92, 28), (64, 12), (44, 6), (52, 14), (80, 26), (104, 42)], OUT, fill=False)
c.line(108, 46, 52, 12, OUT)
c.line(104, 44, 76, 22, OUT)
# body
c.ellipse(140, 64, 34, 15, OUT)
c.ellipse(140, 64, 32, 13, DR_BODY)
c.ellipse(140, 67, 20, 7, DR_BODY_L)
for (sx, sy) in [(126, 50), (134, 46), (148, 48), (160, 52)]:
    c.set(sx, sy, DR_JAW)
# back spikes
for (sx, sy) in [(128, 52), (140, 47), (154, 50), (168, 55)]:
    c.poly([(sx, sy), (sx + 2, sy - 7), (sx + 7, sy + 1)], DR_JAW)
    c.poly([(sx, sy), (sx + 2, sy - 7), (sx + 7, sy + 1)], OUT, fill=False)
# legs
c.poly([(118, 72), (110, 84), (122, 87), (130, 76)], DR_JAW)
c.poly([(118, 72), (110, 84), (122, 87), (130, 76)], OUT, fill=False)
c.poly([(136, 74), (130, 86), (140, 88), (146, 77)], DR_JAW)
c.poly([(136, 74), (130, 86), (140, 88), (146, 77)], OUT, fill=False)
# near wing
c.poly([(126, 58), (100, 34), (64, 18), (34, 10), (24, 18), (46, 30), (80, 42), (108, 52)], DR_MEM)
c.poly([(126, 58), (100, 34), (64, 18), (34, 10), (24, 18), (46, 30), (80, 42), (108, 52)], OUT, fill=False)
c.line(108, 50, 44, 20, OUT)
c.line(102, 48, 72, 30, OUT)
c.line(98, 48, 56, 26, OUT)
# rim light (backlit dragon against sun)
DRIM = "#ffb03e"
DRIM2 = "#ff7a34"
c.line(80, 58, 86, 62, DRIM)
c.line(74, 56, 78, 60, DRIM)
c.line(88, 64, 104, 70, DRIM)
c.line(104, 70, 116, 74, DRIM)
c.line(116, 74, 126, 78, DRIM)
c.line(126, 78, 138, 74, DRIM)
c.line(138, 74, 150, 68, DRIM)
c.line(150, 68, 160, 62, DRIM)
c.line(160, 62, 172, 56, DRIM)
c.line(172, 56, 186, 52, DRIM)
c.line(64, 44, 64, 66, DRIM2)
c.line(74, 42, 74, 64, DRIM2)
c.line(82, 46, 82, 60, DRIM2)
c.set(60, 50, DRIM)
c.set(60, 66, DRIM)
c.set(70, 68, DRIM)
c.set(90, 58, DRIM)
c.set(96, 64, DRIM)
c.line(24, 18, 40, 28, DRIM)
c.line(28, 22, 44, 30, DRIM)
c.set(20, 16, DRIM)
for (gx, gy) in [(30, 14), (40, 22), (52, 30), (62, 36), (72, 42), (82, 46), (92, 50)]:
    c.set(gx, gy, DRIM2)
# breath (under head)
c.poly([(48, 52), (40, 60), (52, 72), (72, 84), (98, 94), (108, 96), (98, 82), (78, 70), (60, 62)], BR_O)
c.poly([(54, 58), (52, 68), (70, 78), (92, 86), (100, 88), (90, 78), (72, 68)], BR_Y)
c.line(62, 66, 84, 80, BR_C)
# head
c.poly([(74, 38), (64, 44), (56, 50), (54, 62), (64, 68), (82, 62), (84, 48)], DR_BODY)
c.poly([(74, 38), (64, 44), (56, 50), (54, 62), (64, 68), (82, 62), (84, 48)], OUT, fill=False)
c.poly([(56, 58), (46, 62), (52, 70), (62, 66)], DR_JAW)
c.poly([(56, 58), (46, 62), (52, 70), (62, 66)], OUT, fill=False)
# horns
c.poly([(62, 40), (56, 24), (70, 36)], HORN)
c.poly([(62, 40), (56, 24), (70, 36)], OUT, fill=False)
c.poly([(72, 42), (76, 30), (82, 42)], HORN)
c.poly([(72, 42), (76, 30), (82, 42)], OUT, fill=False)
# eye
c.set(63, 49, EYE)
c.set(64, 50, EYE)
c.set(63, 48, OUT)
# talon claws
c.line(111, 84, 109, 90, OUT)
c.line(118, 86, 118, 91, OUT)
# wing tip claws
c.line(26, 16, 20, 20, OUT)
c.line(36, 12, 32, 8, OUT)

# ================= ARROWS =================
shots = [(36, 120, 78, 148), (30, 128, 74, 154), (44, 114, 84, 144), (222, 148, 176, 140),
        (214, 142, 168, 136), (228, 154, 180, 148), (60, 196, 96, 178), (196, 192, 158, 176),
        (54, 132, 92, 156), (206, 118, 166, 128), (72, 190, 106, 172), (186, 196, 150, 182)]
for (a0, b0, a1, b1) in shots:
    c.line(a0, b0, a1, b1, ARROW)
    c.set(a1, b1, TIP)
# arrows sticking in wall
for (ax, ay) in [(92, 156), (150, 162), (128, 170)]:
    c.line(ax, ay + 3, ax + 4, ay, ARROW)
    c.set(ax + 2, ay - 1, TIP)

# ================= EMBERS =================
for k in range(190):
    t = rng.uniform(1, 40)
    x = int(116 + rng.uniform(0, 40) + t * rng.uniform(0.5, 1.5))
    y = int(92 - rng.uniform(0, 10) - t * rng.uniform(1.1, 2.4))
    if 0 <= x < 256 and 0 <= y < 256:
        c.set(x, y, rng.choice(EMB))
for k in range(46):
    x = int(118 + rng.uniform(0, 28) + rng.uniform(0, 60))
    y = int(96 - rng.uniform(0, 30))
    if 0 <= x < 256 and 0 <= y < 256:
        c.set(x, y, rng.choice(EMB[:3]))

# bottom shadow edge
c.rect(0, 252, 256, 4, EDGE)

# small birds in sky
for (bx, by) in [(30, 60), (44, 56), (252, 70), (238, 66), (8, 96), (250, 44)]:
    c.line(bx - 3, by, bx + 3, by, DR_JAW)
    c.line(bx - 2, by - 1, bx, by - 1, DR_JAW)
    c.line(bx + 1, by - 1, bx + 3, by - 1, DR_JAW)

# ================= REPORT =================
print(c.stats_text())
print("palette size:", len(c.palette()))

finish(c)
