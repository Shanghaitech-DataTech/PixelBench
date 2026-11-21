from pixelbench_api import *
from random import Random

W = H = 256
c = new_canvas(W, H, name="main")


def reg(name, rgb):
    return c.color(rgb, name=name)


# ---------------- palette ----------------
SKY = [reg("sky%d" % i, col) for i, col in enumerate([
    (24, 14, 44), (36, 17, 56), (50, 20, 66), (68, 24, 76), (90, 30, 86),
    (114, 38, 92), (140, 46, 94), (166, 56, 92), (194, 70, 88), (218, 90, 80),
    (238, 112, 70), (252, 142, 64), (255, 172, 74), (255, 200, 92),
])]
def skycol(y):
    return SKY[min(13, y * 14 // 181)]

SUN_GLOW = reg("sunglow", (255, 214, 150))
SUN     = reg("sun", (255, 244, 214))
CLOUD_D  = reg("cloud_d", (150, 72, 92))
CLOUD_M  = reg("cloud_m", (198, 112, 102))
CLOUD_L  = reg("cloud_l", (242, 160, 112))
BIRD    = reg("bird", (26, 18, 40))
MTN_F   = reg("mtn_far", (40, 24, 66))
MTN_N   = reg("mtn_near", (58, 38, 86))
GRND_D  = reg("grnd_d", (60, 46, 56))
GRND_N  = reg("grnd_n", (28, 24, 32))
STONE_OUT = reg("stone_out", (20, 16, 22))
STONE    = reg("stone", (66, 60, 68))
STONE_L  = reg("stone_l", (98, 90, 98))
STONE_T  = reg("stone_t", (128, 118, 124))
GATE    = reg("gate", (12, 10, 14))
WIN_GLOW = reg("win_glow", (255, 168, 80))
FIRE_Y  = reg("fire_y", (255, 224, 120))
FIRE_O  = reg("fire_o", (255, 156, 58))
FIRE_R  = reg("fire_r", (214, 66, 38))
FIRE_D  = reg("fire_d", (128, 36, 32))
SMK_D  = reg("smk_d", (24, 20, 26))
SMK    = reg("smk", (46, 40, 48))
SMK_L  = reg("smk_l", (74, 66, 72))
BAN_R  = reg("ban_r", (168, 44, 42))
BAN_D  = reg("ban_d", (84, 26, 30))
WOOD_OUT = reg("wood_out", (38, 27, 22))
WOOD   = reg("wood", (74, 54, 42))
WOOD_L = reg("wood_l", (110, 82, 60))
WOOD_D = reg("wood_d", (52, 38, 30))
SOL_D  = reg("sol_d", (16, 14, 19))
SOL_M  = reg("sol_m", (34, 30, 40))
SOL_H  = reg("sol_h", (52, 46, 58))
SPEAR = reg("spear", (208, 196, 176))
SHIELD = reg("shield", (74, 70, 86))
ARROW = reg("arrow", (26, 22, 28))
EMB_Y = reg("emb_y", (255, 206, 110))
EMB_O = reg("emb_o", (248, 140, 60))
EMB_R = reg("emb_r", (196, 64, 40))
DRG_OUT = reg("drg_out", (8, 6, 10))
DRG_D  = reg("drg_d", (30, 26, 34))
DRG_M  = reg("drg_m", (52, 46, 60))
DRG_B  = reg("drg_b", (92, 84, 100))
WING_D = reg("wing_d", (22, 18, 26))
WING_M = reg("wing_m", (34, 29, 40))
WING_B = reg("wing_b", (56, 50, 64))
HORN  = reg("horn", (150, 138, 118))
DRG_EYE = reg("drg_eye", (255, 216, 90))


# ---------------- helpers ----------------
def teeth(x, y, w):
    k = x
    while k < x + w:
        tw = min(6, x + w - k)
        c.rect(k, y, tw, 6, STONE)
        c.rect(k, y, tw, 6, STONE_OUT, fill=False)
        c.rect(k, y, tw, 1, STONE_T)
        k += 9


def block(x, y, w, h):
    c.rect(x, y, w, h, STONE)
    c.rect(x, y, w, h, STONE_OUT, fill=False)


def defender(bx, by, face):
    c.rect(bx, by, 2, 8, SOL_D)
    c.set(bx, by - 1, SOL_H)
    c.line(bx + 2, by - 8, bx + 2, by - 1, SPEAR)
    c.rect(bx + face * 2, by, 2, 5, SHIELD)


def flames(cx, cy, s):
    c.circle(cx, cy, s, FIRE_D)
    c.circle(cx, cy - 2, s - 1, FIRE_R)
    c.circle(cx, cy - 4, s - 2, FIRE_O)
    c.circle(cx, cy - 5, s - 3, FIRE_Y)


# ---------------- sky ----------------
for y in range(182):
    c.rect(0, y, W, 1, skycol(y))

# sun
c.circle(168, 138, 20, SUN_GLOW)
c.circle(168, 138, 13, SUN)
c.rect(150, 128, 36, 4, CLOUD_D)
c.rect(158, 136, 24, 3, CLOUD_D)


# ---------------- clouds ----------------
def cloud(x0, y0, n, dx):
    for i3 in range(n):
        cx = x0 + i3 * dx
        c.circle(cx, y0 + 5, 9, CLOUD_D)
        c.circle(cx, y0 - 3, 9, CLOUD_M)
        c.circle(cx, y0 - 6, 7, CLOUD_L)


cloud(24, 92, 5, 12)
cloud(116, 78, 4, 13)
cloud(168, 102, 3, 12)
cloud(206, 70, 2, 11)

for (bx, by) in [(120, 52), (128, 48), (136, 52), (150, 70), (158, 66), (206, 58)]:
    c.line(bx, by, bx + 4, by - 2, BIRD)
    c.line(bx + 4, by - 2, bx + 8, by, BIRD)

# ---------------- land ----------------
c.poly([(0, 178), (18, 162), (44, 152), (72, 160), (100, 148), (128, 158),
       (156, 150), (186, 160), (216, 152), (246, 160), (256, 156), (256, 190), (0, 190)], MTN_F)
c.poly([(0, 186), (26, 172), (56, 180), (88, 168), (120, 178), (152, 170),
       (184, 180), (216, 170), (246, 180), (256, 176), (256, 196), (0, 196)], MTN_N)

c.rect(0, 188, 256, 24, GRND_D)
c.rect(0, 212, 256, 44, GRND_N)

# tents on distant plain (behind siege towers)
c.poly([(150, 204), (160, 190), (170, 204)], SOL_D)
c.poly([(176, 206), (184, 194), (192, 206)], SOL_D)
c.poly([(196, 204), (204, 192), (212, 204)], SOL_D)
c.set(196, 193, EMB_O)
c.set(160, 191, EMB_O)

# road / tracks
c.rect(104, 216, 148, 12, SOL_D)
for gx in range(8, 250, 12):
    c.line(gx, 237, gx + 10, 233, SOL_D)
c.line(12, 240, 12, 218, SOL_D)
c.line(12, 224, 20, 216, SOL_D)

# ---------------- castle ----------------
block(16, 148, 120, 62)
teeth(16, 142, 120)
for yy in (156, 168, 180, 192, 202):
    c.rect(18, yy, 116, 1, STONE_L)
c.rect(46, 162, 12, 48, GATE)
c.circle(52, 160, 8, GATE)
c.rect(40, 150, 4, 8, STONE_OUT)
c.rect(60, 156, 4, 8, STONE_OUT)
c.rect(60, 120, 4, 10, STONE_OUT)
c.rect(84, 122, 5, 12, WIN_GLOW)

block(24, 104, 22, 106)
teeth(24, 98, 22)
for yy in (116, 130, 144, 158, 172, 186, 196):
    c.rect(26, yy, 18, 1, STONE_L)
c.rect(38, 132, 4, 10, STONE_OUT)

block(58, 98, 40, 112)
teeth(58, 92, 40)
for yy in (110, 122, 134, 146, 158, 170, 182, 194):
    c.rect(60, yy, 36, 1, STONE_L)
c.rect(66, 130, 4, 10, STONE_OUT)
c.rect(88, 116, 4, 10, STONE_OUT)

block(108, 112, 24, 98)
teeth(108, 106, 24)
for yy in (124, 138, 152, 166, 180, 194):
    c.rect(110, yy, 20, 1, STONE_L)
c.rect(120, 140, 4, 10, STONE_OUT)

# banners
c.line(64, 92, 64, 74, WOOD_OUT)
c.poly([(64, 76), (78, 82), (64, 88)], BAN_R)
c.poly([(64, 76), (78, 82), (64, 88)], BAN_D, fill=False)
c.line(32, 98, 32, 82, WOOD_OUT)
c.poly([(32, 84), (44, 90), (32, 96)], BAN_R)
c.poly([(32, 84), (44, 90), (32, 96)], BAN_D, fill=False)
c.line(214, 128, 214, 112, WOOD_OUT)
c.poly([(214, 114), (226, 119), (214, 124)], BAN_R)
c.poly([(214, 114), (226, 119), (214, 124)], BAN_D, fill=False)

# defenders on castle
defender(36, 136, 1)
defender(52, 136, 1)
defender(98, 136, 1)
defender(122, 136, 1)
defender(28, 96, 1)
defender(40, 96, 1)
defender(64, 90, 1)
defender(78, 90, 1)
defender(90, 90, 1)
defender(112, 104, 1)
defender(122, 104, 1)

# fire on castle
flames(72, 92, 6)
flames(84, 96, 5)
flames(94, 90, 4)
flames(62, 88, 4)
flames(36, 104, 5)
flames(114, 112, 4)

# ---------------- smoke ----------------
for (px, py, pr, pcol) in [
    (74, 88, 9, SMK), (86, 78, 11, SMK), (64, 72, 11, SMK), (96, 66, 10, SMK),
    (78, 58, 10, SMK), (108, 74, 9, SMK), (128, 86, 8, SMK), (58, 62, 9, SMK),
    (56, 50, 8, SMK), (92, 46, 7, SMK), (70, 42, 6, SMK_L), (118, 60, 7, SMK_L),
    (138, 52, 7, SMK), (176, 124, 8, SMK), (188, 110, 9, SMK), (198, 98, 8, SMK),
    (196, 128, 7, SMK),
]:
    c.circle(px, py, pr, pcol)

# ---------------- siege towers ----------------
c.rect(146, 152, 26, 58, WOOD)
c.rect(146, 152, 26, 58, WOOD_OUT, fill=False)
teeth(146, 146, 26)
for yy in range(160, 204, 9):
    c.rect(148, yy, 22, 2, WOOD_OUT)
c.rect(152, 156, 3, 50, WOOD_OUT)
c.rect(163, 156, 3, 50, WOOD_OUT)
c.circle(153, 209, 5, WOOD_D)
c.circle(153, 209, 5, WOOD_OUT, fill=False)
c.circle(165, 209, 5, WOOD_D)
c.circle(165, 209, 5, WOOD_OUT, fill=False)
defender(150, 146, -1)
defender(162, 146, -1)

block(182, 134, 34, 76)  # stone fill covered by wood below
c.rect(182, 134, 34, 76, WOOD)
c.rect(182, 134, 34, 76, WOOD_OUT, fill=False)
teeth(182, 128, 34)
for yy in range(144, 206, 9):
    c.rect(184, yy, 30, 2, WOOD_OUT)
c.rect(186, 138, 3, 68, WOOD_OUT)
c.rect(209, 138, 3, 68, WOOD_OUT)
for yy in range(136, 206, 8):
    c.rect(189, yy, 22, 2, WOOD_OUT)
c.circle(189, 134, 34, SMK)
flames(204, 132, 5)
flames(192, 134, 4)
c.rect(189, 209, 5, 4, WOOD_D)
c.rect(189, 209, 5, 4, WOOD_OUT, fill=False)
c.rect(208, 209, 5, 4, WOOD_D)
c.rect(208, 209, 5, 4, WOOD_OUT, fill=False)
c.rect(132, 137, 50, 5, WOOD_OUT, fill=False)
defender(186, 128, -1)
defender(198, 128, -1)
defender(208, 128, -1)

# wood tower roof slabs
c.rect(146, 146, 26, 5, WOOD_L)
c.rect(146, 146, 26, 5, WOOD_OUT, fill=False)
c.rect(182, 128, 34, 5, WOOD_L)
c.rect(182, 128, 34, 5, WOOD_OUT, fill=False)
c.rect(182, 134, 34, 5, WOOD_L)
c.rect(182, 134, 34, 5, WOOD_OUT, fill=False)
c.rect(146, 152, 26, 5, WOOD_L)
c.rect(146, 152, 26, 5, WOOD_OUT, fill=False)

# ---------------- ground troops ----------------
for sx in range(150, 250, 9):
    defender(sx, 230, -1)
for sx in range(146, 252, 9):
    defender(sx, 240, -1)
for sx in range(72, 108, 9):
    defender(sx, 240, -1)

# ---------------- dragon ----------------
fp = [(88, 56), (124, 18), (156, 30), (134, 50), (102, 56)]
c.poly(fp, WING_D)
c.poly(fp, DRG_OUT, fill=False)
c.line(94, 54, 124, 18, WING_B)
c.line(96, 54, 150, 30, WING_B)

tp = [(128, 62), (166, 86), (180, 98), (158, 104), (118, 90)]
c.poly(tp, DRG_D)
c.poly(tp, DRG_OUT, fill=False)
c.line(126, 60, 134, 52, DRG_M)
c.line(140, 57, 148, 50, DRG_M)
c.line(152, 64, 160, 58, DRG_M)

bp = [(68, 64), (88, 50), (118, 56), (140, 70), (150, 86), (144, 102), (116, 106), (90, 100), (72, 82)]
c.poly(bp, DRG_D)
c.poly(bp, DRG_OUT, fill=False)
c.poly([(86, 84), (108, 94), (128, 90), (134, 78), (112, 70), (92, 70), (82, 78)], DRG_B)

np2 = [(96, 60), (150, 22), (192, 34), (170, 62), (130, 68)]
c.poly(np2, WING_M)
c.poly(np2, DRG_OUT, fill=False)
c.line(100, 60, 150, 22, WING_B)
c.line(104, 60, 172, 42, WING_B)

c.circle(60, 62, 8, DRG_D)
c.circle(60, 62, 8, DRG_OUT, fill=False)
sn = [(64, 55), (42, 59), (44, 70), (62, 67)]
c.poly(sn, DRG_D)
c.poly(sn, DRG_OUT, fill=False)
c.line(58, 55, 51, 45, HORN)
c.line(53, 52, 49, 43, HORN)
c.set(56, 59, DRG_EYE)
c.line(52, 66, 48, 68, DRG_OUT)
c.line(102, 104, 98, 114, DRG_D)
c.line(178, 98, 186, 96, DRG_M)

# dragon fire breath onto the castle
c.poly([(58, 64), (38, 74), (26, 90), (42, 86), (56, 80)], FIRE_R)
c.poly([(50, 72), (36, 80), (32, 88), (42, 84), (50, 80)], FIRE_O)
c.poly([(44, 76), (38, 82), (36, 86), (44, 82), (46, 78)], FIRE_Y)
c.circle(40, 88, 5, FIRE_R)
c.circle(40, 92, 4, FIRE_O)

# ---------------- arrows ----------------
for (ax, ay, adx, ady) in [
    (58, 140, 26, -14), (80, 134, 32, -12), (100, 138, 34, -10), (124, 132, 38, -8),
    (142, 148, 36, -6), (164, 142, 30, -4), (200, 144, -36, 14), (188, 150, -30, 10),
    (172, 152, -26, 16), (118, 120, 40, -6), (156, 116, 30, -16), (92, 124, 32, -16),
    (30, 146, 24, -10), (70, 122, 28, -18),
]:
    c.line(ax, ay, ax + adx, ay + ady, ARROW)

# ---------------- embers ----------------
rng = Random(7)
for _ in range(150):
    ex = rng.randint(16, 244)
    ey = rng.randint(52, 196)
    ec = rng.choice([EMB_R, EMB_O, EMB_Y])
    c.set(ex, ey, ec)
for _ in range(60):
    ex = rng.randint(30, 150)
    ey = rng.randint(70, 170)
    c.set(ex, ey, rng.choice([EMB_Y, EMB_O]))

# foreground rocks
c.circle(20, 236, 5, SOL_D)
c.circle(42, 246, 4, SOL_D)
c.circle(236, 240, 5, SOL_D)
c.circle(8, 248, 4, SOL_D)

print(c.stats_text())
print("colors:", len(c.palette()))

finish(c)
