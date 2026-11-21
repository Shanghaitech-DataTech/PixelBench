from pixelbench_api import *
import random

C = new_canvas(64, 64, name="store")

# ---------- palette ----------
SKY = C.color("#0e1424")
SKY_T = C.color("#0a0f1d")
LB  = C.color("#171c2c")
LBW  = C.color("#202744")
ROOF = C.color("#201a12")
WALL = C.color("#3a2c1e")
SIGN_BG = C.color("#10141f")
SIGN_BR = C.color("#414a68")
SIGN_T = C.color("#ffd452")
AWN_R = C.color("#c2352e")
AWN_W = C.color("#e8e2d6")
AWN_D = C.color("#7e2622")
FRAME = C.color("#221c15")
W_LG = C.color("#ffd880")
W_BR = C.color("#ffe9ab")
TUBE = C.color("#fff2bf")
SHELF = C.color("#9c6a34")
SHELF_D = C.color("#7a4c22")
P_R = C.color("#c9543f")
P_O = C.color("#d87f33")
P_G = C.color("#4e8a4e")
P_B = C.color("#3f6fa8")
DOOR = C.color("#f2ca80")
DGL = C.color("#ffe3a0")
DP = C.color("#4a3020")
HDL = C.color("#e2d8c8")
MAT = C.color("#3a342c")
GND = C.color("#232833")
GND_D = C.color("#171b25")
SPL = C.color("#4a3e2c")
PD = C.color("#141b29")
PD_S = C.color("#2c3f66")
PD_W = C.color("#ffc96f")
PD_B = C.color("#ffe6a8")
BIKE = C.color("#1e3c49")
BDK = C.color("#0e141c")
BLI = C.color("#9db6c0")
BM = C.color("#3f9fb0")
UM0 = C.color("#d9483f")
UM1 = C.color("#52a254")
UM2 = C.color("#3f7fd9")
RACK = C.color("#15181f")
CT = C.color("#f2c44a")
PDK = C.color("#14161c")
LMP = C.color("#1a1e28")
LG = C.color("#ffc77e")
POOL = C.color((255, 196, 120, 60))

# ---------- night sky ----------
C.rect(0, 0, 64, 16, SKY)
C.rect(0, 0, 64, 5, SKY_T)
C.rect(0, 8, 2, 38, LB)
C.rect(0, 12, 2, 2, LBW)
C.rect(0, 18, 2, 2, LBW)

# ---------- store wall ----------
C.rect(2, 15, 61, 1, ROOF)
C.rect(2, 16, 61, 31, WALL)

# ---------- glowing sign ----------
C.rect(11, 16, 43, 10, SIGN_BG)
C.rect(11, 16, 43, 10, SIGN_BR, fill=False)
C.text(21, 18, "STORE", SIGN_T)

# ---------- awning ----------
for i, x in enumerate(range(2, 62, 4)):
    C.rect(x, 26, 4, 5, AWN_R if i % 2 == 0 else AWN_W)
C.rect(2, 31, 60, 1, AWN_D)

# ---------- left window ----------
C.rect(4, 32, 18, 13, W_LG)
C.rect(4, 32, 18, 2, W_BR)
C.rect(5, 32, 16, 1, TUBE)
C.rect(4, 32, 18, 13, FRAME, fill=False)
C.rect(13, 32, 1, 13, FRAME)
C.rect(5, 37, 16, 1, SHELF)
C.rect(5, 41, 16, 1, SHELF)
C.rect(5, 41, 16, 1, SHELF_D)
C.rect(6, 34, 3, 2, P_O)
C.rect(10, 33, 2, 2, P_R)
C.rect(15, 34, 2, 2, P_G)
C.rect(17, 33, 2, 2, P_B)
C.rect(6, 38, 2, 2, P_G)
C.rect(9, 39, 2, 2, P_R)
C.rect(15, 38, 3, 2, P_O)
C.rect(18, 39, 2, 2, P_B)

# ---------- door ----------
C.rect(24, 28, 12, 19, FRAME)
C.rect(25, 29, 10, 16, DGL)
C.rect(25, 29, 10, 2, DOOR)
C.rect(25, 29, 10, 16, FRAME, fill=False)
C.rect(26, 41, 8, 4, DP)
C.rect(33, 34, 2, 5, HDL)
C.rect(24, 46, 12, 1, MAT)

# ---------- right window ----------
C.rect(39, 32, 20, 13, W_LG)
C.rect(39, 32, 20, 2, W_BR)
C.rect(40, 32, 18, 1, TUBE)
C.rect(39, 32, 20, 13, FRAME, fill=False)
C.rect(48, 32, 1, 13, FRAME)
C.rect(40, 37, 18, 1, SHELF)
C.rect(40, 41, 18, 1, SHELF)
C.rect(40, 41, 18, 1, SHELF_D)
for x in [41, 43, 45, 49, 51, 53, 55, 57]:
    C.rect(x, 34, 1, 2, P_B)
    C.rect(x, 38, 1, 2, P_G)
    C.rect(x, 36, 1, 1, P_R)

# ---------- umbrella rack (wall strip beside door) ----------
C.line(36, 34, 40, 34, CT)
C.rect(36, 34, 5, 1, CT)
C.rect(36, 34, 5, 9, FRAME, fill=False)
for ux, col in [(37, UM0), (38, UM1), (39, UM2)]:
    C.line(ux, 36, ux, 42, col)
    C.set(ux, 35, col)
C.rect(36, 41, 5, 1, RACK)
C.rect(36, 42, 5, 3, RACK)

# ---------- warm pool of light at door ----------
C.ellipse(30, 49, 8, 3, POOL)

# ---------- person in raincoat entering ----------
C.circle(30, 31, 3, CT)
C.rect(27, 34, 7, 8, CT)
C.rect(26, 35, 2, 4, CT)
C.rect(33, 36, 2, 4, CT)
C.rect(27, 42, 3, 4, PDK)
C.rect(31, 42, 3, 4, PDK)
C.set(30, 42, CT)
C.rect(28, 46, 6, 1, PDK)

# ---------- street lamp ----------
C.rect(62, 8, 1, 39, LMP)
C.rect(60, 6, 4, 4, LMP)
C.rect(61, 7, 2, 2, LG)

# ---------- sidewalk & road ----------
C.rect(0, 47, 64, 3, GND_D)
C.rect(7, 47, 50, 2, SPL)
C.rect(0, 50, 64, 14, GND)

# ---------- bicycle parked in front of left window ----------
C.circle(8, 45, 3, BDK)
C.circle(16, 45, 3, BDK)
C.set(8, 45, BLI)
C.set(16, 45, BLI)
C.line(8, 45, 8, 36, BIKE)
C.line(9, 36, 5, 36, BIKE)
C.line(13, 36, 8, 45, BIKE)
C.line(13, 36, 16, 45, BIKE)
C.line(13, 36, 15, 34, BIKE)
C.rect(5, 35, 3, 1, BIKE)
C.line(14, 32, 15, 34, BIKE)
C.rect(13, 30, 3, 2, BDK)
C.set(15, 33, BM)

# ---------- reflective puddles ----------
C.ellipse(13, 57, 10, 3, PD)
C.ellipse(49, 57, 11, 4, PD)
C.ellipse(60, 55, 3, 2, PD)
C.ellipse(13, 55, 7, 1, PD_S)
C.ellipse(49, 55, 8, 1, PD_S)
C.line(6, 56, 20, 56, PD_W)
C.line(10, 54, 15, 54, PD_W)
C.line(8, 58, 18, 58, PD_W)
C.line(42, 55, 55, 55, PD_W)
C.line(46, 58, 53, 58, PD_W)
C.set(7, 57, PD_B)
C.set(17, 58, PD_B)
C.set(44, 56, PD_B)
C.set(54, 57, PD_B)
C.line(60, 52, 60, 57, PD_B)
C.line(59, 54, 59, 56, PD_W)
C.line(29, 53, 31, 55, PD_B)
C.line(28, 56, 32, 56, PD_W)

# ---------- rain layer (blended over whole scene) ----------
R = new_canvas(64, 64)
RAIN = R.color((170, 198, 235, 75))
RAIN2 = R.color((214, 232, 252, 95))
HALO = R.color((255, 207, 140, 80))
R.circle(61, 8, 2, HALO, fill=False)
R.circle(31, 32, 4, HALO, fill=False)
random.seed(42)
for _ in range(60):
    x = random.randrange(0, 62)
    y = random.randrange(0, 14)
    R.line(x, y, x + 1, y + 2, RAIN)
for _ in range(30):
    x = random.randrange(42, 62)
    y = random.randrange(48, 60)
    R.line(x, y, x + 1, y + 2, RAIN)
for x in [5, 9, 12, 16, 21, 27, 32, 42, 46, 50, 55]:
    R.line(x, 33, x, 42, RAIN2)
R.line(31, 28, 31, 34, RAIN2)

final = flatten([C, R], name="final")
print(final.stats_text())
print("palette size:", len(final.palette()))
finish(final)
