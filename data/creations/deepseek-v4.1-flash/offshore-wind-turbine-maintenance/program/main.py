import math
from pixelbench_api import *

c = new_canvas(64, 64, background="#0d2447", name="result")


def dash(x, y, n, col):
    c.line(x, y, x + n - 1, y, col)


# ============================== SKY ==============================
SKY = ["#0d2447", "#123058", "#193e6d", "#234f85", "#2f6299", "#4478ab", "#5c98c4"]
BANDS = [(0, 5), (5, 11), (11, 17), (17, 23), (23, 29), (29, 34), (34, 38)]
for i, (y0, y1) in enumerate(BANDS):
    c.rect(0, y0, 64, y1 - y0, SKY[i])
for i in range(len(BANDS) - 1):
    yb = BANDS[i][1]
    c.dither(0, yb - 1, 64, 2, [SKY[i], SKY[i + 1]], pattern="checker")

# horizon haze
c.rect(0, 37, 64, 1, "#a9d3e4")

# ============================== SEA ==============================
SEA = [("#1f7a9c", 38, 43), ("#1a6a8a", 43, 49), ("#155877", 49, 56), ("#104861", 56, 64)]
for col, y0, y1 in SEA:
    c.rect(0, y0, 64, y1 - y0, col)
for i in range(len(SEA) - 1):
    yb = SEA[i][2]
    c.dither(0, yb - 1, 64, 2, [SEA[i][0], SEA[i + 1][0]], pattern="checker")

CF = "#46aecd"
CM = "#3ba2c0"
CN = "#2f93b1"
FOAM = "#c9ecf7"

WAVES = [
    (3, 40, 3, CF), (12, 41, 2, CF), (21, 39, 2, CF), (31, 41, 3, CF),
    (42, 40, 2, CF), (50, 41, 3, CF), (58, 39, 2, CF), (24, 42, 2, CF),
    (46, 42, 2, CF), (7, 39, 2, CF), (36, 39, 3, CF), (61, 41, 2, CF),
    (5, 45, 3, CM), (16, 44, 4, CM), (26, 46, 3, CM), (37, 45, 3, CM),
    (47, 44, 4, CM), (56, 46, 3, CM), (2, 47, 3, CM), (33, 47, 4, CM),
    (9, 44, 3, CM), (21, 43, 2, CM), (42, 46, 3, CM), (60, 44, 3, CM),
    (1, 50, 4, CN), (12, 51, 3, CN), (22, 50, 4, CN), (34, 51, 3, CN),
    (44, 50, 4, CN), (55, 51, 3, CN), (8, 53, 4, CN), (28, 53, 4, CN),
    (49, 53, 3, CN), (6, 49, 3, CN), (19, 49, 4, CN), (39, 49, 3, CN),
    (58, 49, 4, CN), (16, 52, 3, CN), (41, 53, 3, CN), (61, 52, 3, CN),
    (2, 57, 6, CN), (13, 58, 5, CN), (25, 57, 6, CN), (37, 58, 5, CN),
    (49, 57, 6, CN), (59, 58, 4, CN), (19, 56, 4, CN), (32, 56, 5, CN),
    (44, 56, 3, CN), (8, 62, 7, CN), (21, 61, 6, CN), (33, 62, 7, CN),
    (45, 61, 6, CN), (56, 62, 5, CN), (14, 61, 4, CN), (27, 60, 4, CN),
    (50, 60, 5, CN), (2, 60, 5, CN),
]
for x, y, n, col in WAVES:
    dash(x, y, n, col)

# foreground swell: crest with a shaded trough under it
SW_CREST = "#3fa6c2"
SW_TROUGH = "#0c3448"
for x, y, n in [(3, 59, 7), (17, 60, 6), (30, 59, 7), (44, 60, 6), (55, 59, 5)]:
    dash(x, y, n, SW_CREST)
    dash(x + 1, y + 1, n - 2, SW_TROUGH)
    c.set(x + 1, y, FOAM)

for x, y in [(6, 58), (14, 58), (26, 57), (39, 58), (50, 57), (9, 62), (34, 62),
             (46, 61), (57, 62), (23, 50), (45, 50), (11, 45), (30, 45), (52, 45),
             (18, 54), (36, 55), (60, 56)]:
    c.set(x, y, FOAM)

# ============================== DISTANT TURBINES ==============================
DT = "#4a7899"
DTH = "#6f9cbb"


def distant_turbine(hx, hy, blen):
    base_y = 37
    c.rect(hx, hy + 1, 2, base_y - hy, DT)
    c.line(hx, hy + 1, hx, base_y - 1, DTH)
    c.rect(hx - 1, hy - 1, 4, 2, DT)
    c.set(hx, hy - 1, DTH)
    for ang in (60, 180, 300):
        a = math.radians(ang)
        x1 = int(round(hx + 0.5 + blen * math.cos(a)))
        y1 = int(round(hy - 0.5 - blen * math.sin(a)))
        c.line(hx, hy, x1, y1, DT)


distant_turbine(9, 21, 5)
distant_turbine(54, 23, 4)

# ============================== MAIN TOWER ==============================
TOWER = {
    27: "#dfe8ec", 28: "#c3d0d8", 29: "#a9b8c2", 30: "#a9b8c2",
    31: "#93a3ae", 32: "#93a3ae", 33: "#7b8b97", 34: "#7b8b97",
    35: "#63737f", 36: "#4e5e6a",
}
TOWER_DK = {
    27: "#c9d5db", 28: "#adbbc4", 29: "#94a3ad", 30: "#94a3ad",
    31: "#7e8e99", 32: "#7e8e99", 33: "#687884", 34: "#687884",
    35: "#53636f", 36: "#42525e",
}
for x, col in TOWER.items():
    c.line(x, 0, x, 27, col)
# bolted flange joints
for x, col in TOWER_DK.items():
    c.set(x, 7, col)
    c.set(x, 20, col)

# ============================== PLATFORM DECK ==============================
DECK_L, DECK_R = 19, 45
c.rect(DECK_L, 28, DECK_R - DECK_L + 1, 1, "#d3dde2")
c.rect(DECK_L, 29, DECK_R - DECK_L + 1, 1, "#a9b8c2")
c.rect(DECK_L, 30, DECK_R - DECK_L + 1, 2, "#7f8f9a")
c.rect(DECK_L, 32, DECK_R - DECK_L + 1, 1, "#4f5f6b")

for x in range(21, 45, 5):
    c.rect(x, 30, 2, 2, "#d9a43a")

# ============================== TRANSITION PIECE ==============================
# submerged jacket (seen through the water)
c.poly([(23, 33), (41, 33), (38, 42), (26, 42)], "#3a5464")
c.line(28, 39, 28, 42, "#31495a")
c.line(36, 39, 36, 42, "#31495a")
# above water
c.poly([(23, 33), (41, 33), (40, 38), (24, 38)], "#6b7b87")
c.line(23, 33, 41, 33, "#8b99a2")
c.line(27, 34, 27, 37, "#5a6a76")
c.line(36, 34, 36, 37, "#5a6a76")
c.line(24, 34, 30, 37, "#83919a")
c.line(40, 34, 34, 37, "#83919a")

# ============================== RAILING ==============================
YEL = "#e6b23c"
YELD = "#b9882a"
for x0, x1 in [(DECK_L, 26), (37, DECK_R)]:
    c.line(x0, 22, x1, 22, YEL)
    c.line(x0, 25, x1, 25, YEL)
    mid = (x0 + x1) // 2
    for pxx in (x0, mid, x1):
        c.line(pxx, 22, pxx, 27, YELD)
    c.line(x0, 23, x1, 23, YELD)

# ============================== LADDER ==============================
LAD = "#3a4750"
LAD_HI = "#5c6b76"
c.line(28, 0, 28, 27, LAD)
c.line(34, 0, 34, 27, LAD)
for y in range(1, 28, 3):
    c.line(28, y, 34, y, LAD)
    c.set(29, y, LAD_HI)

# ============================== TECHNICIAN ==============================
HELM = "#f6cf46"
HELM_HI = "#ffe98f"
HELM_DK = "#c9a02c"
SKIN = "#cf9463"
VEST = "#e8622a"
VEST_D = "#b8431a"
STRIPE = "#f0e6c0"
PANTS = "#2e3a4a"
DARK = "#222b38"

c.rect(29, 11, 5, 1, HELM)          # hard hat crown
c.set(30, 11, HELM_HI)
c.set(31, 11, HELM_HI)
c.rect(28, 12, 7, 1, HELM_DK)       # helmet brim
c.rect(30, 13, 3, 1, SKIN)          # head / neck
c.set(28, 13, DARK)                 # gloves gripping the rung
c.set(34, 13, DARK)
c.rect(29, 14, 5, 4, VEST)          # hi-vis vest
c.rect(28, 14, 1, 3, VEST)          # sleeves
c.rect(34, 14, 1, 3, VEST)
c.rect(29, 15, 5, 1, STRIPE)        # reflective band
c.rect(29, 17, 5, 1, VEST_D)
c.rect(29, 18, 5, 1, DARK)          # belt
c.rect(29, 19, 2, 2, PANTS)         # left leg
c.rect(32, 19, 2, 1, PANTS)         # right leg
c.set(33, 20, PANTS)
c.rect(29, 21, 2, 1, DARK)          # boots
c.set(33, 21, DARK)

# ============================== WATERLINE FOAM ==============================
for x, y, n, col in [
    (23, 38, 3, FOAM), (36, 38, 3, FOAM),
    (20, 39, 3, "#8fc8dc"), (41, 39, 3, "#8fc8dc"),
    (28, 40, 2, FOAM), (33, 40, 2, FOAM),
]:
    dash(x, y, n, col)

save("offshore_wind_turbine_maintenance", c)
print(c.stats_text())
finish(c)
