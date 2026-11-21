from pixelbench_api import *

c = new_canvas(64, 64, name="result")

# ---- palette ----
OUT = c.color("#241a12", "outline")
TRAY = c.color("#d8c6a4", "tray")
TRAY_EDGE = c.color("#b89a72", "tray_edge")
TRAY_LIGHT = c.color("#eee0c4", "tray_light")
SHADOW = c.color("#a98b63", "shadow")

BUN = c.color("#e8a54a", "bun")
BUN_LIGHT = c.color("#f7cf7e", "bun_light")
BUN_SHADOW = c.color("#b5793a", "bun_shadow")
SESAME = c.color("#f7e8c0", "sesame")
CHEESE = c.color("#f7c542", "cheese")
CHEESE_DARK = c.color("#d9a028", "cheese_dark")
LETTUCE = c.color("#6db83e", "lettuce")
LETTUCE_DARK = c.color("#4d8a2a", "lettuce_dark")
PATTY = c.color("#7a4a2b", "patty")
PATTY_DARK = c.color("#5a3420", "patty_dark")

FRY = c.color("#f2c14e", "fry")
FRY_LIGHT = c.color("#f9dc7a", "fry_light")
FRY_DARK = c.color("#c68a2a", "fry_dark")
CARTON_RED = c.color("#d0342c", "carton_red")
CARTON_DARK = c.color("#a02420", "carton_dark")
CARTON_LIGHT = c.color("#e8504a", "carton_light")
CARTON_IN = c.color("#3a0c08", "carton_in")
WHITE = c.color("#f4ecd8", "white")

NUGGET = c.color("#d59a4a", "nugget")
NUGGET_LIGHT = c.color("#e8b870", "nugget_light")
NUGGET_DARK = c.color("#b07634", "nugget_dark")
NUGGET_CRUMB = c.color("#f0d0a0", "nugget_crumb")

COLA = c.color("#3a1f10", "cola")
COLA_LIGHT = c.color("#5a3820", "cola_light")
ICE = c.color("#a8d8e8", "ice")
ICE_DARK = c.color("#6fb0c8", "ice_dark")
CUP = c.color("#e8e0d0", "cup")
CUP_DARK = c.color("#b8a888", "cup_dark")
STRAW = c.color("#e04040", "straw")
STRAW_DARK = c.color("#a02828", "straw_dark")
STRAW_WHITE = c.color("#f0d8d8", "straw_white")

SAUCE_CUP = c.color("#e8e4dc", "sauce_cup")
SAUCE_CUP_DARK = c.color("#b0a898", "sauce_cup_dark")
KETCHUP = c.color("#c83a28", "ketchup")
BBQ = c.color("#6b3a1a", "bbq")


def rrect(cv, x0, y0, x1, y1, r, col, fill=True):
    d = (f"M {x0+r} {y0} "
         f"L {x1-r} {y0} "
         f"Q {x1} {y0} {x1} {y0+r} "
         f"L {x1} {y1-r} "
         f"Q {x1} {y1} {x1-r} {y1} "
         f"L {x0+r} {y1} "
         f"Q {x0} {y1} {x0} {y1-r} "
         f"L {x0} {y0+r} "
         f"Q {x0} {y0} {x0+r} {y0} Z")
    cv.path(d, col, fill=fill)


# ---- tray ----
rrect(c, 1, 1, 62, 62, 9, OUT)
rrect(c, 2, 2, 61, 61, 8, TRAY)
rrect(c, 4, 4, 59, 59, 6, TRAY_EDGE, fill=False)


# ---- cheeseburger ----
def burger(cv, cx, cy):
    cv.ellipse(cx + 2, cy + 2, 13, 13, SHADOW)
    cv.ellipse(cx, cy, 13, 13, OUT)
    cv.ellipse(cx, cy + 1, 11, 11, PATTY)
    cv.ellipse(cx, cy, 10, 10, CHEESE)
    cv.ellipse(cx, cy - 1, 9, 9, LETTUCE)
    cv.ellipse(cx, cy - 4, 12, 9, BUN)
    # bun shading
    cv.ellipse(cx - 3, cy - 6, 3, 2, BUN_LIGHT)
    cv.ellipse(cx - 3, cy + 2, 3, 2, BUN_SHADOW)
    # sesame seeds
    seeds = [(cx - 5, cy - 6), (cx, cy - 7), (cx + 5, cy - 6), (cx - 3, cy - 4),
             (cx + 2, cy - 4), (cx - 6, cy - 3), (cx + 6, cy - 2), (cx - 1, cy - 2)]
    for sx, sy in seeds:
        cv.set(sx, sy, SESAME)
    # melted cheese drips over the patty
    cv.set(cx - 6, cy + 11, CHEESE)
    cv.set(cx - 2, cy + 12, CHEESE)
    cv.set(cx + 3, cy + 11, CHEESE)
    cv.set(cx - 2, cy + 13, CHEESE_DARK)


# ---- french fries in red carton ----
def fries(cv):
    # carton body
    cv.poly([(39, 10), (54, 10), (51, 36), (43, 36)], SHADOW)
    cv.poly([(37, 8), (52, 8), (49, 34), (41, 34)], OUT)
    cv.poly([(38, 9), (51, 9), (48, 33), (42, 33)], CARTON_RED)
    cv.poly([(38, 9), (51, 9), (49, 15), (41, 15)], CARTON_IN)
    # side shading
    cv.line(39, 10, 39, 32, CARTON_LIGHT)
    cv.line(50, 10, 47, 32, CARTON_DARK)
    # small white stripe on the carton front
    cv.poly([(39, 20), (50, 19), (49, 21), (40, 22)], WHITE)
    # golden fries
    sticks = [(40, 4, 2, FRY), (42, 3, 2, FRY_LIGHT), (44, 5, 2, FRY),
              (46, 2, 2, FRY), (48, 4, 2, FRY_DARK), (50, 6, 2, FRY)]
    for x, top, w, col in sticks:
        cv.rect(x, top, w, 16 - top, col)
    cv.line(41, 5, 41, 14, FRY_LIGHT)
    cv.line(43, 6, 43, 13, FRY)
    cv.line(45, 4, 45, 15, FRY_LIGHT)
    cv.line(47, 5, 47, 14, FRY)
    cv.line(49, 7, 49, 13, FRY_DARK)


# ---- chicken nuggets ----
def nugget(cv, cx, cy, rx, ry):
    cv.ellipse(cx + 1, cy + 1, rx + 1, ry + 1, SHADOW)
    cv.ellipse(cx, cy, rx + 1, ry + 1, OUT)
    cv.ellipse(cx, cy, rx, ry, NUGGET)
    cv.set(cx - 2, cy - 1, NUGGET_LIGHT)
    cv.set(cx + 1, cy - 2, NUGGET_LIGHT)
    cv.set(cx + 2, cy + 1, NUGGET_DARK)
    cv.set(cx - 1, cy + 1, NUGGET_DARK)
    cv.set(cx + 1, cy, NUGGET_CRUMB)


# ---- cola cup with ice and straw ----
def drink(cv, cx, cy, r):
    cv.circle(cx + 2, cy + 2, r + 1, SHADOW)
    cv.circle(cx, cy, r + 1, OUT)
    cv.circle(cx, cy, r, CUP)
    cv.circle(cx, cy, r - 1, COLA)
    # ice cubes
    ice = [(cx - 4, cy - 3), (cx - 1, cy - 5), (cx + 3, cy - 4),
           (cx - 3, cy + 2), (cx + 2, cy + 3), (cx + 5, cy + 1)]
    for ix, iy in ice:
        cv.rect(ix, iy, 2, 2, ICE)
        cv.set(ix, iy + 1, ICE_DARK)
    cv.rect(cx - 6, cy + 3, 2, 2, ICE)
    cv.set(cx - 6, cy + 4, ICE_DARK)
    # cola surface highlight
    cv.circle(cx - 3, cy - 6, 1, COLA_LIGHT)
    # straw seen from above
    cv.circle(cx + 5, cy - 5, 1, STRAW)
    cv.set(cx + 5, cy - 5, STRAW_DARK)
    cv.set(cx + 4, cy - 5, STRAW_WHITE)


# ---- dipping sauce cups ----
def sauce(cv, cx, cy, col):
    cv.circle(cx + 1, cy + 1, 4, SHADOW)
    cv.circle(cx, cy, 4, OUT)
    cv.circle(cx, cy, 3, SAUCE_CUP)
    cv.circle(cx, cy, 2, col)
    cv.set(cx - 2, cy - 2, WHITE)
    cv.set(cx + 2, cy + 2, SAUCE_CUP_DARK)


# ---- assemble ----
burger(c, 20, 20)
fries(c)
nugget(c, 15, 44, 4, 3)
nugget(c, 23, 44, 4, 3)
nugget(c, 19, 50, 5, 3)
drink(c, 48, 47, 10)
sauce(c, 33, 39, KETCHUP)
sauce(c, 33, 47, BBQ)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
