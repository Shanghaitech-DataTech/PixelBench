from pixelbench_api import *

# ---------------- palette ----------------
OUT   = "#20130a"   # universal dark outline
TRAY_E = "#b3a691"   # tray rim
TRAY_M = "#dcd4c2"   # tray surface
TRAY_H = "#e9e2d1"   # tray top bevel
SHAD  = "#a4987d"   # drop shadow

# burger
BBUN  = "#d99c45"; BBUN_D = "#b57c2e"
PAT   = "#7a4422"; PAT_D = "#522c12"; PAT_L = "#96582c"
CH    = "#f6c63c"; CH_D  = "#cf911d"; CH_L = "#f9d96a"
LET   = "#63a63c"; LET_D = "#3c7a22"; LET_L = "#85c655"
BUN   = "#e2ab55"; BUN_D = "#c78d3c"; BUN_L = "#f4cf82"
SES   = "#faedc5"

# fries + carton
CART  = "#d63a2c"; CART_D = "#9c2118"; CART_L = "#ec5a46"
WHT   = "#f6f0e2"
FRY   = "#f0b63e"; FRY_L = "#fbd973"; FRY_D = "#c98e1f"

# cola
COLA  = "#5c2210"; COLA_L = "#7e3518"
ICE   = "#dff0f6"; ICE_D  = "#a9c6d2"
STRAW = "#f4f1e9"; STRAW_R = "#d63a2c"

# nuggets
NUG   = "#e9a63c"; NUG_L = "#f7c964"; NUG_D = "#c18326"

# sauce cups
SAU   = "#f2e8d4"; SAU_D = "#b3a482"
KET   = "#cf2e1e"; KET_L = "#ef6a3a"; KET_D = "#8f1a10"
MUS   = "#f2c23a"; MUS_D = "#d09a18"

# ---------------- helpers ----------------
def fry(fx, fy, h):
    c.rect(fx, fy, 4, h, OUT)
    c.rect(fx + 1, fy + 1, 2, h - 1, FRY)
    c.rect(fx + 1, fy + 1, 1, h - 2, FRY_L)

def sauce(x, y, dip, dipd):
    c.ellipse(x + 3, y + 1, 3, 2, OUT)          # rim outline
    c.rect(x, y + 2, 7, 6, OUT)                # body outline
    c.ellipse(x + 3, y + 1, 2, 1, SAU)          # rim shell
    c.rect(x + 1, y + 2, 5, 5, SAU)            # body
    c.ellipse(x + 3, y + 2, 2, 1, dip)          # dip
    c.rect(x + 2, y + 3, 1, 1, dipd)           # dip depth
    c.rect(x + 2, y + 1, 1, 1, dipd)           # dip shine

def nug(cx, cy):
    c.ellipse(cx, cy, 5, 4, OUT)
    c.ellipse(cx, cy, 4, 3, NUG)
    c.ellipse(cx - 1, cy - 1, 2, 2, NUG_L)
    c.ellipse(cx + 1, cy + 1, 2, 1, NUG)
    c.ellipse(cx + 1, cy - 1, 1, 1, NUG_L)
    c.ellipse(cx - 2, cy + 2, 2, 1, NUG)

# ---------------- canvas ----------------
c = new_canvas(64, 64)

# ---------- tray ----------
c.rect(0, 0, 64, 64, TRAY_E)
c.rect(2, 2, 60, 60, TRAY_M)
c.rect(3, 2, 58, 1, TRAY_H)
c.rect(3, 60, 58, 1, TRAY_E)

# ---------- drop shadows ----------
c.ellipse(17, 22, 16, 8, SHAD)   # burger
c.ellipse(37, 11, 5, 4, SHAD)    # sauce A
c.ellipse(51, 18, 11, 9, SHAD)   # carton
c.ellipse(37, 26, 5, 4, SHAD)    # sauce B
c.ellipse(52, 47, 11, 9, SHAD)   # cup
c.ellipse(16, 50, 15, 10, SHAD)  # nuggets

# ---------- burger (x 1..33, y 1..25) ----------
# bottom bun
c.ellipse(17, 21, 15, 4, OUT)
c.ellipse(17, 21, 14, 3, BBUN)
# patty
c.ellipse(17, 18, 13, 3, OUT)
c.ellipse(17, 18, 12, 2, PAT)
# melted cheese runs down the front
for (dx, hh) in [(8, 3), (14, 4), (20, 4), (25, 3)]:
    c.rect(dx, 16, 3, hh, OUT)
    c.rect(dx + 1, 16, 1, hh - 1, CH)
    c.rect(dx + 1, 18, 1, 1, CH_D)
c.ellipse(17, 14, 14, 4, OUT)
c.ellipse(17, 14, 13, 3, CH)
c.rect(5, 15, 6, 1, CH_L)
c.rect(15, 15, 4, 1, CH_L)
c.rect(22, 16, 3, 1, CH_L)
# lettuce frill
c.ellipse(17, 11, 15, 4, OUT)
c.ellipse(17, 11, 14, 3, LET)
c.rect(6, 13, 4, 1, LET_L)
c.rect(12, 12, 3, 1, LET_L)
c.rect(19, 13, 3, 1, LET_L)
c.rect(25, 12, 3, 1, LET_L)
c.rect(9, 14, 2, 1, LET_L)
# top bun + sesame
c.ellipse(17, 7, 16, 6, OUT)
c.ellipse(17, 7, 15, 5, BUN)
c.ellipse(14, 5, 8, 3, BUN_L)
c.ellipse(20, 9, 9, 2, BUN_D)
for (sx, sy) in [(7, 3), (13, 3), (19, 3), (25, 3), (10, 4), (16, 4), (22, 4),
                (6, 5), (13, 5), (19, 5), (25, 5), (9, 6), (15, 6), (21, 6)]:
    c.rect(sx, sy, 2, 2, SES)

# ---------- sauce cup A (ketchup) ----------
sauce(34, 8, KET, KET_D)
c.rect(35, 9, 1, 1, KET_L)

# ---------- fries carton ----------
# opening interior (painted before fries + wall so fries sink in)
c.ellipse(52, 9, 10, 3, OUT)
c.ellipse(52, 9, 9, 2, CART_D)
# golden fries
for (fx, fy, h) in [(43, 2, 10), (46, 3, 9), (49, 2, 10), (52, 3, 10),
                   (55, 2, 9), (58, 3, 10), (44, 5, 8), (48, 4, 9),
                   (51, 5, 8), (54, 4, 9), (57, 5, 8), (60, 4, 9),
                   (46, 6, 7)]:
    fry(fx, fy, h)
# carton wall
c.rect(42, 10, 20, 16, OUT)
c.rect(43, 11, 18, 15, CART)
c.rect(43, 12, 1, 3, CART_L)
c.rect(45, 11, 1, 2, CART_L)
# white band + red stripes
c.rect(44, 13, 14, 4, WHT)
c.rect(46, 14, 2, 3, CART)
c.rect(51, 14, 2, 3, CART)
c.rect(55, 14, 2, 3, CART)
c.rect(43, 13, 1, 4, CART_L)

# ---------- sauce cup B (mustard) ----------
sauce(34, 22, MUS, MUS_D)
c.rect(35, 22, 1, 2, MUS)
c.rect(35, 21, 2, 1, MUS)

# ---------- cola cup + straw ----------
c.rect(42, 43, 20, 16, OUT)
c.rect(43, 44, 18, 14, CUP if False else "#d63a2c")
c.rect(43, 45, 1, 3, "#ec5a46")
c.ellipse(52, 41, 10, 3, OUT)
c.ellipse(52, 41, 9, 2, COLA)
c.ellipse(50, 41, 4, 1, COLA_L)
c.rect(44, 40, 4, 4, ICE_D)
c.rect(45, 41, 3, 2, ICE)
c.rect(50, 41, 4, 4, ICE_D)
c.rect(51, 42, 3, 2, ICE)
c.rect(56, 39, 4, 4, ICE_D)
c.rect(57, 40, 2, 2, ICE)
# cup band + logo
c.rect(45, 46, 14, 4, WHT)
c.rect(47, 47, 10, 2, CART)
c.rect(48, 48, 8, 1, WHT)
# straw (over cola, rising to upper-right then bending)
for dx in (0, 1, 2):
    c.line(48 + dx, 42, 56 + dx, 32, STRAW)
    c.line(56 + dx, 32, 58 + dx, 30, STRAW)
    c.line(58 + dx, 30, 56 + dx, 28, STRAW)
c.line(50, 40, 52, 38, STRAW_R)
c.line(52, 36, 54, 34, STRAW_R)
c.line(55, 32, 57, 31, STRAW_R)

# ---------- nuggets ----------
nug(8, 42)
nug(20, 40)
nug(25, 49)
nug(14, 52)
nug(6, 55)
c.rect(21, 38, 1, 1, NUG_D)
c.rect(22, 39, 1, 1, NUG_D)

# ---------- ketchup splat ----------
c.circle(28, 41, 2, KET)
c.circle(25, 43, 1, KET)
c.circle(29, 42, 1, KET)
c.rect(27, 40, 1, 1, KET_L)

print(c.stats_text())
print("palette size:", len(c.palette()))

finish(c)
