DARK = "#2b1a10"

T_RIM = "#8a5a2e"
T_TOP = "#ad7340"
T_LITE = "#c08a53"
T_GRAIN = "#935c2c"
FRUIT_O = "#4a2c1a"

CH_B = "#8a5729"
CH_S = "#9f6836"
CH_H = "#b8814c"

MAT_D = "#8f4635"
MAT_L = "#bd6b52"

CERAM = "#efe6d2"
CERAM_D = "#d5c7aa"


def rr(c, x, y, w, h, col):
    """Rect with 1px clipped corners."""
    c.rect(x + 1, y, w - 2, h, col)
    c.rect(x, y + 1, w, h - 2, col)
    return c


c = new_canvas(64, 64, name="dining-table")

# ---- table top (17..46 both axes) ----
rr(c, 17, 17, 30, 30, T_RIM)
rr(c, 19, 19, 26, 26, T_TOP)
# plank seams and grain
for gy in (25, 32, 39):
    c.line(19, gy, 44, gy, T_RIM)
for gy in (22, 29, 36, 43):
    c.line(21, gy, 42, gy, T_GRAIN)
# soft light along upper-left of the top
c.line(20, 20, 43, 20, T_LITE)
c.line(20, 21, 20, 43, T_LITE)

# ---- placemats ----
c.rect(27, 20, 10, 4, MAT_D)
c.rect(28, 21, 8, 2, MAT_L)
c.rect(27, 40, 10, 4, MAT_D)
c.rect(28, 41, 8, 2, MAT_L)
c.rect(20, 27, 4, 10, MAT_D)
c.rect(21, 28, 2, 8, MAT_L)
c.rect(40, 27, 4, 10, MAT_D)
c.rect(41, 28, 2, 8, MAT_L)

# ---- fruit bowl ----
c.circle(31, 31, 7, DARK)
c.circle(31, 31, 6, CERAM_D)
c.circle(31, 31, 5, CERAM)

def fruit(x, y, body, hi):
    rr(c, x, y, 4, 4, body)
    c.set(x + 1, y + 1, hi)

fruit(27, 27, "#c33a2b", "#e0675a")   # apple
fruit(32, 27, "#e3862a", "#f3a94f")   # orange
fruit(27, 32, "#7b4a8a", "#9d6aa8")   # plum
fruit(32, 32, "#7fa83c", "#a3c75c")   # green pear
c.set(28, 26, "#4f7a28")              # leaf on the apple
c.set(29, 26, "#4f7a28")

# ---- chairs ----
# top
rr(c, 25, 1, 14, 4, CH_B)
c.line(26, 2, 37, 2, CH_H)
c.line(26, 5, 37, 5, DARK)
rr(c, 26, 6, 12, 10, CH_S)
rr(c, 28, 8, 8, 6, CH_H)
# bottom
rr(c, 25, 59, 14, 4, CH_B)
c.line(26, 61, 37, 61, CH_H)
c.line(26, 58, 37, 58, DARK)
rr(c, 26, 48, 12, 10, CH_S)
rr(c, 28, 50, 8, 6, CH_H)
# left
rr(c, 1, 25, 4, 14, CH_B)
c.line(2, 26, 2, 37, CH_H)
c.line(5, 26, 5, 37, DARK)
rr(c, 6, 26, 10, 12, CH_S)
rr(c, 8, 28, 6, 8, CH_H)
# right
rr(c, 59, 25, 4, 14, CH_B)
c.line(61, 26, 61, 37, CH_H)
c.line(58, 26, 58, 37, DARK)
rr(c, 48, 26, 10, 12, CH_S)
rr(c, 50, 28, 6, 8, CH_H)

c.outline(DARK)

view(c)
print(c.stats_text())
finish(c)
