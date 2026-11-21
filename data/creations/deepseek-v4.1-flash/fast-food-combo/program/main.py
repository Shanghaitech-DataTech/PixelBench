# ============================================================
#  fast-food-combo  --  64x64 pixel art
#  45-degree top-down view of a fast food combo on a tray
# ============================================================

# ---------------- palette ----------------
INK   = "#241309"
BG1   = "#1d1411"
BG2   = "#2b1f18"
DARK0 = "#120806"

TRAY_RIM   = "#c99b6b"
TRAY_RIM_L = "#e2b787"
TRAY_RIM_D = "#a87a4e"
TRAY_SURF  = "#9d7248"
TRAY_SURF2 = "#88603a"
TRAY_EDGE  = "#6d4a2d"
TRAY_EDGE_L= "#8d6540"
TRAY_EDGE_D= "#3f2818"

SH1 = "#7d5a3a"

BUN_L  = "#f6cd86"
BUN_LL = "#ffe0aa"
BUN    = "#e0a44e"
BUN_D  = "#bf7f2d"
BUN_DD = "#96601e"
SEED   = "#fff6d8"

LET_L = "#96e057"
LET   = "#6bc23c"
LET_D = "#478a24"

CHE_L = "#ffe27a"
CHE   = "#f7c53a"
CHE_D = "#dc9e20"

PAT   = "#7a4426"
PAT_L = "#9a633b"
PAT_D = "#4e2713"

BOTB   = "#dda55a"
BOTB_L = "#f0be7c"
BOTB_D = "#b57c35"

FRY_L  = "#ffe98f"
FRY    = "#f7c846"
FRY_D  = "#d29a1f"
FRY_DD = "#a87716"

CART   = "#e0402f"
CART_L = "#f26a55"
CART_D = "#a8241a"
CART_DD= "#7a1610"

CUP_W  = "#f4f1ea"
CUP_WL = "#fdfbf6"
CUP_W2 = "#ded9cf"
CUP_R  = "#dd3a2e"
CUP_RD = "#a8231a"
CUP_RL = "#f0685a"
CREAM  = "#f6e9c0"

COLA  = "#3a1a10"
COLA_L= "#5c2f1c"
ICE   = "#cfe9f0"
ICE_L = "#f1fbff"
ICE_D = "#9dc6d3"

STRAW = "#e6392e"
STRW  = "#f7f3ea"

NUG   = "#e3a63c"
NUG_L = "#f8cd72"
NUG_D = "#b3781f"

KETCH   = "#c62a1c"
KETCH_L = "#e8564a"
RANCH   = "#f3ecd6"
RANCH_L = "#fffbe9"


def rrect(c, x0, y0, x1, y1, r, col):
    c.poly([(x0 + r, y0), (x1 - r, y0), (x1, y0 + r), (x1, y1 - r),
            (x1 - r, y1), (x0 + r, y1), (x0, y1 - r), (x0, y0 + r)],
           col, fill=True)


# ================= BACKGROUND =================
main = new_canvas(64, 64, name="bg")
main.rect(0, 0, 64, 64, BG1)
main.ellipse(32, 30, 30, 24, BG2)
main.ellipse(32, 57, 30, 5, DARK0)

# ================= TRAY =================
tray = new_canvas(64, 64, name="tray")

rrect(tray, 1, 50, 62, 60, 5, TRAY_EDGE)        # front wall (thickness)
rrect(tray, 1, 6, 62, 55, 4, TRAY_RIM)          # top face rim
rrect(tray, 4, 9, 59, 53, 3, TRAY_SURF)         # recessed surface
tray.rect(5, 10, 54, 1, TRAY_SURF2)             # recess back shadow
tray.line(7, 7, 56, 7, TRAY_RIM_L)              # rim highlight top
tray.line(2, 12, 2, 49, TRAY_RIM_L)             # rim highlight left
tray.line(7, 54, 56, 54, TRAY_RIM_D)            # rim shade bottom
tray.rect(5, 51, 54, 2, TRAY_SURF2)             # recess front shade
tray.line(5, 56, 58, 56, TRAY_EDGE_L)           # wall top light
tray.line(4, 59, 59, 59, TRAY_EDGE_D)           # wall bottom dark

# food shadows
tray.ellipse(16, 42, 12, 3, SH1)
tray.ellipse(38, 34, 9, 3, SH1)
tray.ellipse(51, 49, 8, 3, SH1)
tray.ellipse(14, 49, 8, 3, SH1)
tray.ellipse(34, 51, 9, 2, SH1)
# stray sesame seeds on the tray
for sx, sy in [(34, 37), (36, 38), (32, 39), (45, 21)]:
    tray.set(sx, sy, SEED)
tray.outline(INK)

# ================= FRIES =================
f = new_canvas(64, 64, name="fries")
# loose fry lying on the tray
f.rect(28, 35, 6, 2, FRY)
f.rect(28, 35, 6, 1, FRY_L)
f.set(33, 36, FRY_D)

# carton opening (dark inside)
f.ellipse(38, 21, 10, 4, CART_DD)
# dark gaps between the fries
for gx in (32, 36, 40, 44):
    f.rect(gx, 11, 1, 11, CART_DD)
# fries
sticks = [(29, 16), (33, 11), (37, 13), (41, 9), (45, 14)]
for sx, sy in sticks:
    h = 23 - sy
    f.rect(sx, sy, 3, h, FRY)
    f.rect(sx, sy, 1, h, FRY_L)
    f.rect(sx + 2, sy + 1, 1, h - 1, FRY_D)
    f.set(sx + 2, sy, FRY_DD)
# carton front face
f.poly([(30, 21), (47, 21), (45, 34), (32, 34)], CART, fill=True)
f.poly([(31, 22), (33, 22), (34, 33), (33, 33)], CART_L, fill=True)
f.poly([(43, 22), (47, 22), (45, 34), (43, 34)], CART_D, fill=True)
f.line(33, 33, 44, 33, CART_DD)                 # bottom dark
f.line(33, 22, 42, 22, CART_L)                  # rim light
# emblem
f.line(36, 30, 38, 26, CREAM)
f.line(38, 26, 40, 30, CREAM)
f.outline(INK)

# ================= COLA =================
k = new_canvas(64, 64, name="cola")
# cup body (tapered)
k.poly([(44, 29), (58, 29), (56, 48), (46, 48)], CUP_W, fill=True)
k.poly([(45, 30), (48, 30), (48, 47), (47, 47)], CUP_WL, fill=True)     # left shine
k.poly([(47, 44), (56, 44), (56, 48), (46, 48)], CUP_W2, fill=True)     # bottom shade
# red band
k.poly([(45, 33), (57, 33), (57, 39), (45, 39)], CUP_R, fill=True)
k.poly([(54, 33), (57, 33), (57, 39), (54, 39)], CUP_RD, fill=True)
k.rect(46, 34, 1, 4, CUP_RL)
k.rect(47, 34, 7, 1, "#f9efe0")
# rim (flat oval)
rrect(k, 43, 24, 59, 31, 3, CUP_W2)
rrect(k, 45, 26, 57, 29, 2, COLA)
k.rect(44, 25, 4, 1, CUP_WL)                    # rim highlight
k.set(43, 28, CUP_WL)
# cola surface
k.rect(46, 29, 10, 1, COLA_L)
# ice
for cx, cy in [(46, 26), (50, 27), (54, 26)]:
    k.rect(cx, cy, 2, 2, ICE_L)
    k.set(cx + 1, cy + 1, ICE)
    k.set(cx, cy + 1, ICE_D)
# straw
for i in range(4):
    k.line(51 + i, 29, 55 + i, 15, STRAW)
k.line(52, 25, 55, 25, STRW)
k.line(53, 22, 56, 22, STRW)
k.line(54, 19, 57, 19, STRW)
k.outline(INK)

# ================= BURGER =================
b = new_canvas(64, 64, name="burger")
BUN_ROWS = [(11, 2), (12, 4), (13, 6), (14, 8), (15, 9), (16, 10), (17, 11),
            (18, 11), (19, 12), (20, 12), (21, 12), (22, 12), (23, 11),
            (24, 11), (25, 10), (26, 10)]
for y, hw in BUN_ROWS:
    if y <= 15:
        col = BUN_L
    elif y <= 21:
        col = BUN
    elif y <= 24:
        col = BUN_D
    else:
        col = BUN_DD
    b.rect(16 - hw, y, 2 * hw + 1, 1, col)
# soft highlight on top of the dome
b.rect(13, 12, 5, 1, BUN_LL)
b.rect(12, 13, 8, 1, BUN_LL)
b.rect(13, 14, 6, 1, BUN_LL)
# sesame seeds
for sx, sy in [(8, 17), (12, 16), (17, 15), (21, 16), (25, 19),
               (10, 20), (15, 19), (20, 21), (26, 21), (6, 20), (23, 22),
               (13, 22), (18, 23)]:
    b.set(sx, sy, SEED)
# lettuce
b.rect(6, 23, 3, 1, LET_L)
b.rect(13, 23, 3, 1, LET_L)
b.rect(20, 23, 3, 1, LET_L)
b.set(9, 23, LET)
b.set(24, 23, LET)
b.rect(4, 24, 25, 1, LET_L)                     # x4..28
b.rect(3, 25, 27, 1, LET)                       # x3..29
b.rect(3, 26, 27, 1, LET)
b.rect(4, 27, 25, 1, LET_D)                     # x4..28
b.set(3, 25, LET_D); b.set(29, 26, LET_D)
# cheese band
b.rect(4, 28, 26, 3, CHE)                       # x4..29 y28..30
b.rect(4, 28, 26, 1, CHE_L)
# patty
b.rect(5, 31, 24, 5, PAT)                       # x5..28 y31..35
b.rect(5, 32, 24, 2, PAT_L)
b.rect(5, 35, 24, 1, PAT_D)
for tx, ty in [(8, 33), (13, 33), (18, 34), (23, 32), (11, 35), (21, 34), (16, 33)]:
    b.set(tx, ty, PAT_D)
# cheese drips over the patty
for dx, w, h in [(5, 3, 3), (12, 4, 4), (20, 3, 2), (26, 3, 3)]:
    b.rect(dx, 30, w, h, CHE)
    b.rect(dx, 29 + h, w, 1, CHE_D)
# bottom bun
for y, hw in [(36, 11), (37, 11), (38, 11), (39, 10), (40, 8), (41, 5)]:
    col = BOTB if y <= 39 else BOTB_D
    b.rect(16 - hw, y, 2 * hw + 1, 1, col)
b.rect(7, 37, 6, 1, BOTB_L)                     # shine on the bottom bun
b.outline(INK)

# ================= NUGGETS =================
def make_nugget(x0, y0, x1, y1, name):
    c = new_canvas(64, 64, name=name)
    rrect(c, x0, y0, x1, y1, 2, NUG)
    rrect(c, x0, y0, x1 - 1, y1 - 1, 2, NUG)
    rrect(c, x0 + 1, y0 + 1, x1 - 2, y1 - 2, 2, NUG_L)
    rrect(c, x0 + 1, y1 - 1, x1 - 1, y1, 1, NUG_D)
    c.set(x0 + 3, y0 + 3, NUG_D)
    c.set(x1 - 3, y0 + 2, NUG_D)
    c.set(x0 + 5, y1 - 2, NUG_D)
    c.set(x0 + 2, y0 + 2, NUG_L)
    c.outline(INK)
    return c


n1 = make_nugget(3, 42, 13, 48, "n1")
n2 = make_nugget(13, 44, 23, 50, "n2")
n3 = make_nugget(7, 47, 17, 53, "n3")

# ================= SAUCE CUPS =================
s = new_canvas(64, 64, name="sauce")


def sauce_cup(px, py, hw, col, hi):
    rrect(s, px - hw, py - 1, px + hw, py + 4, 2, CUP_W2)     # body
    rrect(s, px - hw, py - 3, px + hw, py + 1, 2, CUP_W)      # rim
    rrect(s, px - hw + 1, py - 2, px + hw - 1, py, 1, col)    # sauce
    s.rect(px - 2, py - 2, 2, 1, hi)                          # shine


sauce_cup(29, 48, 5, KETCH, KETCH_L)
sauce_cup(39, 49, 4, RANCH, RANCH_L)
s.outline(INK)

# ================= COMPOSITE =================
result = flatten([main, tray, f, k, b, n1, n2, n3, s], name="result")
print(result.stats_text())
print(result.matrix_text())
save("fast_food_combo", result)
finish(result)
