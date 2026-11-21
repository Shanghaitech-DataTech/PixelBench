import math

c = new_canvas(64, 64, background="#1b2530", name="result")

# ---------------- palette ----------------
CEIL      = "#26313d"
TUBE      = "#f4fbff"
TUBE_G    = "#8198a9"

WALL_A    = "#dbe6ed"
WALL_B    = "#cedbe4"
WALL_C    = "#c1d0da"
WALL_D    = "#b3c3cf"
BASEBD    = "#93a4b1"
BASEBD_H  = "#aabac5"

FLOOR     = "#93a3af"
POOL_1    = "#9aa9b5"
POOL_2    = "#a1b0bc"
GROUT     = "#85949f"
SHADOW    = "#7b8b98"
SHADOW2   = "#8292a0"

M_OUT     = "#4d5e6c"
M_BODY    = "#dce5eb"
M_BODY2   = "#e4ebf0"
M_HI      = "#f1f7fa"
SPEC      = "#fbfdff"
M_SH      = "#b7c4ce"
M_BASE    = "#a5b3be"
M_PANEL   = "#aab8c3"
M_PANEL_D = "#98a7b3"
M_DISP    = "#1e2f3c"

RIM       = "#eaf3f7"
GASKET    = "#7e8f9d"
GLASS     = "#16222c"
GLASS_2   = "#4a7089"
GLINT     = "#ddf0f8"
LED       = "#6bd6c3"
LED2      = "#f2f8fa"

CLOCK_RIM = "#3a4a5b"
CLOCK_F   = "#f4fafc"
CLOCK_T   = "#8d9ca9"
CLOCK_H   = "#28333e"
CLOCK_S   = "#cf5548"

TBL_TOP   = "#dde5ea"
TBL_HI    = "#f0f6f9"
TBL_EDGE  = "#aab8c2"
TBL_LEG   = "#8b98a2"
TBL_LEG_D = "#74818b"

TOWEL_W   = "#f2f7fa"
TOWEL_B   = "#bcd8e8"
TOWEL_G   = "#d6e3ea"

BSK_L     = "#cd8450"
BSK_M     = "#b06a37"
BSK_D     = "#894d22"
BSK_HOLE  = "#5d3113"
BSK_HI    = "#e2a06a"

LIGHT_SPANS = [(5, 26), (37, 58)]


# ---------------- helpers ----------------
def glass_door(cx, cy, r):
    c.circle(cx, cy, r, RIM)
    c.circle(cx, cy, r - 1, GASKET)
    c.circle(cx, cy, r - 2, GLASS)
    if r >= 5:
        rr = r - 3
        for ang in range(184, 282, 6):
            a = math.radians(ang)
            px = int(round(cx + rr * math.cos(a)))
            py = int(round(cy + rr * math.sin(a)))
            c.set(px, py, GLASS_2)
        c.set(cx - 2, cy - 2, GLINT)
        c.set(cx - 1, cy - 3, GLINT)
    else:
        c.set(cx - 1, cy - 1, GLASS_2)
        c.set(cx, cy, "#20313f")


def washer(x, y, w, h, dr, panel_h, door_cy, body=M_BODY, led=LED):
    c.rect(x, y, w, h, M_OUT)
    c.rect(x + 1, y + 1, w - 2, h - 2, body)
    c.rect(x + 1, y + 1, w - 2, 1, M_HI)
    c.rect(x + 1, y + 1, 1, h - 2, M_HI)
    c.rect(x + w - 2, y + 1, 1, h - 2, M_SH)
    c.rect(x + 1, y + h - 2, w - 2, 1, M_BASE)
    # control panel
    c.rect(x + 2, y + 2, w - 4, panel_h, M_PANEL)
    panel_bot = y + 1 + panel_h
    if w >= 16:
        c.rect(x + 4, y + 2, 5, 2, M_DISP)
        c.set(x + 5, y + 2, led)
        c.set(x + 8, y + 2, GLINT)
        c.circle(x + 13, y + 3, 1, "#cfdae2")
        c.set(x + 13, y + 2, "#8b9aa6")
        c.rect(x + 2, panel_bot, w - 4, 1, M_PANEL_D)
        c.set(x + 16, panel_bot, led)
    else:
        c.rect(x + 3, y + 2, 3, 1, M_DISP)
        c.set(x + 4, y + 2, led)
        c.set(x + w - 4, y + 2, LED2)
        c.rect(x + 2, panel_bot, w - 4, 1, M_PANEL_D)
    cx = x + w // 2
    glass_door(cx, door_cy, dr)
    # specular streak on top edge where the tubes shine
    for (a, b) in LIGHT_SPANS:
        lo = max(a, x + 1)
        hi = min(b, x + w - 2)
        if lo <= hi:
            c.rect(lo, y + 1, hi - lo + 1, 1, SPEC)


# ================= ceiling =================
c.rect(0, 0, 64, 3, CEIL)
c.rect(5, 1, 22, 1, TUBE)
c.rect(37, 1, 22, 1, TUBE)
c.rect(5, 2, 22, 1, TUBE_G)
c.rect(37, 2, 22, 1, TUBE_G)
c.rect(0, 2, 5, 1, "#2e3b48")
c.rect(27, 2, 10, 1, "#2e3b48")
c.rect(59, 2, 5, 1, "#2e3b48")

# ================= wall =================
c.rect(0, 3, 64, 16, WALL_C)
c.rect(0, 3, 64, 2, WALL_A)
c.rect(0, 5, 64, 2, WALL_B)
c.rect(0, 15, 64, 2, WALL_D)
c.rect(0, 17, 64, 1, BASEBD_H)
c.rect(0, 18, 64, 1, BASEBD)

# ================= floor =================
c.rect(0, 19, 64, 45, FLOOR)
c.ellipse(32, 58, 26, 13, POOL_1)
c.ellipse(32, 57, 17, 8, POOL_2)
for yy in (23, 27, 32, 38, 45, 53, 62):
    c.rect(0, yy, 64, 1, GROUT)
VPX, VPY = 32, 11
for bx in (-2, 10, 21, 32, 43, 54, 66):
    t = (26 - VPY) / (63 - VPY)
    x0 = VPX + (bx - VPX) * t
    c.line(int(round(x0)), 26, bx, 63, GROUT)

# ================= wall clock =================
c.set(56, 5, CLOCK_RIM)
c.circle(56, 11, 5, CLOCK_RIM)
c.circle(56, 11, 4, CLOCK_F)
c.set(56, 7, CLOCK_T)
c.set(52, 11, CLOCK_T)
c.set(56, 15, CLOCK_T)
c.set(60, 11, CLOCK_T)
c.line(56, 11, 53, 9, CLOCK_H)
c.line(56, 11, 59, 9, CLOCK_H)
c.line(56, 11, 55, 13, CLOCK_S)
c.set(56, 11, CLOCK_H)

# ================= back row of washers =================
for i, mx in enumerate((2, 14, 26, 38)):
    bod = M_BODY if i % 2 == 0 else M_BODY2
    led = LED if i % 2 == 0 else LED2
    washer(mx, 7, 11, 12, 3, 2, 14, body=bod, led=led)
for gx in (13, 25, 37):
    c.rect(gx, 7, 1, 12, SHADOW)

# ================= front row of washers =================
for gx in (21, 42):
    c.rect(gx, 22, 1, 20, SHADOW)
washer(0, 22, 21, 20, 6, 3, 33)
washer(22, 22, 20, 20, 6, 3, 33, body=M_BODY2, led=LED2)
washer(43, 22, 21, 20, 6, 3, 33)
c.rect(0, 42, 64, 1, SHADOW2)
c.rect(0, 43, 64, 1, "#8a99a6")

# ================= folding table =================
c.poly([(7, 46), (23, 46), (27, 51), (3, 51)], TBL_TOP)
c.line(7, 46, 23, 46, TBL_HI)
c.rect(12, 47, 9, 1, TBL_HI)
c.line(3, 51, 27, 51, TBL_EDGE)
c.poly([(3, 51), (27, 51), (27, 53), (3, 53)], TBL_EDGE)
c.line(3, 52, 27, 52, TBL_LEG_D)
c.rect(5, 53, 2, 9, TBL_LEG)
c.rect(6, 53, 1, 9, TBL_LEG_D)
c.rect(24, 53, 2, 9, TBL_LEG)
c.rect(25, 53, 1, 9, TBL_LEG_D)
c.rect(4, 61, 3, 1, SHADOW)
c.rect(23, 61, 3, 1, SHADOW)

# folded towels on the table
c.rect(10, 47, 7, 2, TOWEL_W)
c.rect(10, 45, 7, 2, TOWEL_B)
c.rect(11, 44, 5, 1, TOWEL_G)
c.rect(11, 48, 5, 1, TOWEL_G)
c.set(9, 48, TOWEL_W)
c.set(17, 47, TOWEL_B)
# detergent bottle
c.rect(19, 43, 4, 4, "#e8f0f4")
c.rect(20, 42, 3, 1, "#4a90b8")
c.rect(19, 47, 4, 1, "#b9c8d2")
c.set(22, 45, "#7fb8d8")
c.set(19, 46, "#c9d6de")

# ================= laundry basket =================
c.ellipse(43, 48, 3, 2, TOWEL_W)
c.ellipse(48, 48, 3, 2, TOWEL_B)
c.set(45, 47, TOWEL_G)
c.set(41, 48, "#c9d6de")
c.set(50, 47, TOWEL_W)
# body
c.poly([(38, 51), (53, 51), (50, 62), (41, 62)], BSK_L)
for yy in range(52, 62):
    wl = 38 + (yy - 51) * 3 // 11
    wr = 53 - (yy - 51) * 3 // 11
    for xx in range(wl + 1, wr):
        if (xx - 38) % 3 == 0:
            c.set(xx, yy, BSK_HOLE)
# handle bumps
c.rect(38, 47, 3, 2, BSK_M)
c.rect(49, 47, 3, 2, BSK_M)
c.rect(38, 47, 3, 1, BSK_HI)
c.rect(49, 47, 3, 1, BSK_HI)
# rim
c.rect(37, 49, 17, 2, BSK_M)
c.rect(37, 49, 17, 1, BSK_HI)
c.rect(37, 51, 17, 1, BSK_D)
c.rect(37, 49, 1, 2, BSK_D)
c.rect(53, 49, 1, 2, BSK_D)
# bottom shade
c.rect(41, 61, 9, 1, BSK_D)
c.rect(40, 62, 11, 1, SHADOW)

# ================= dropped sock =================
c.ellipse(31, 55, 2, 1, TOWEL_W)
c.rect(33, 54, 2, 1, TOWEL_B)
c.set(30, 55, "#c9d6de")

print(c.stats_text())
save("laundromat", c)
finish(c)
