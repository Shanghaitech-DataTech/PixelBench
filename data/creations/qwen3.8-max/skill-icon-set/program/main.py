import numpy as np

# ---------------------------------------------------------------- palette
INK      = "#101420"          # unified dark outline

FIRE_OUT = ["#8c2211", "#cf3a15", "#f2691d", "#fb9a22"]   # outer flames
FIRE_IN  = ["#ef6118", "#fb9a22", "#fdd84a", "#fff3b0"]   # inner core
FIRE_HOT = "#fffbe0"

ICE_RIM  = ["#2b6091", "#4d92c4", "#9fd9f2"]              # shield rim
ICE_FLD  = ["#2f6fa8", "#4b95cd", "#7cc4ea", "#c3ecfb"]   # shield field
ICE_WHITE = "#f2feff"

HRT      = ["#8e1330", "#c81f42", "#ef4463", "#ff92a6"]   # heart
HRT_GLOS = "#ffd9e0"
CROSS    = "#ffffff"
CROSS_SH = "#7d1029"

CLD      = ["#39415f", "#545e80", "#767f9f", "#9aa2bd"]   # storm cloud
BOLT     = ["#cf7a08", "#f9a90f", "#fcd329", "#fff3a8"]   # lightning
SPARK    = "#fff6c8"

# ---------------------------------------------------------------- helpers
def arr(c):
    w, h, rgba = c.to_rgba()
    return np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(h, w, 4).copy()

def vis(c):
    return arr(c)[:, :, 3] > 0

def paint(c, mask, colour):
    ys, xs = np.nonzero(mask)
    for x, y in zip(xs.tolist(), ys.tolist()):
        c.set(int(x), int(y), colour)

def mask_of(c, colour):
    w, h, rgba = c.to_rgba()
    a = np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(h, w, 4)
    r = int(colour[1:3], 16); g = int(colour[3:5], 16); b = int(colour[5:7], 16)
    return (a[:, :, 0] == r) & (a[:, :, 1] == g) & (a[:, :, 2] == b) & (a[:, :, 3] > 0)

def levels_from(t, lo, hi, n):
    u = np.clip((t - lo) / (hi - lo + 1e-9), 0.0, 1.0)
    return np.clip(np.floor(u * n).astype(int), 0, n - 1)

def sphere_levels(c, cx, cy, R, light=(-0.50, -0.62, 0.61), lo=0.10, hi=0.95, n=4):
    a = arr(c); h, w = a.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    dx = (xx - cx) / float(R); dy = (yy - cy) / float(R)
    r2 = np.clip(dx * dx + dy * dy, 0.0, 1.0)
    dz = np.sqrt(np.clip(1.0 - r2, 0.0, 1.0))
    L = np.array(light, dtype=float); L = L / np.linalg.norm(L)
    inten = dx * L[0] + dy * L[1] + dz * L[2]
    return levels_from(inten, lo, hi, n)

def dir_levels(c, toward=(-0.62, -0.78), lo=0.12, hi=0.88, n=4):
    v = vis(c); ys, xs = np.nonzero(v)
    p = xs * toward[0] + ys * toward[1]
    mn, mx = p.min(), p.max()
    h, w = v.shape
    yy, xx = np.mgrid[0:h, 0:w]
    P = xx * toward[0] + yy * toward[1]
    t = (P - mn) / (mx - mn + 1e-9)
    return levels_from(t, lo, hi, n)

def apply_ramp(c, levels, ramp, only=None):
    v = vis(c)
    if only is not None:
        v = v & only
    h, w = v.shape
    for k, col in enumerate(ramp):
        paint(c, v & (levels == k), col)

def outline_all(c, colour):
    a = arr(c)
    v = a[:, :, 3] > 0
    h, w = v.shape
    pad = np.zeros((h + 2, w + 2), dtype=bool)
    pad[1:-1, 1:-1] = v
    interior = (pad[0:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, 0:-2] & pad[1:-1, 2:])
    paint(c, v & ~interior, colour)

def lick(c, tipx, tipy, bx, by, hw, colour, bend=0):
    my = (by + tipy) // 2
    d = ("M%d,%d Q%d,%d %d,%d Q%d,%d %d,%d Z"
         % (bx - hw, by, bx - hw + bend, my, tipx, tipy,
            bx + hw + bend, my, bx + hw, by))
    c.path(d, colour, fill=True)

# ---------------------------------------------------------------- fireball
def draw_fire():
    c = new_canvas(32, 32, name="fire")
    flat = "#c0301a"
    # flame licks rising from the core
    lick(c, 16, 1, 15, 13, 5, flat, bend=-2)      # tall centre tongue
    lick(c, 7, 5, 9, 15, 4, flat, bend=-3)        # left tongue
    lick(c, 25, 6, 23, 15, 3, flat, bend=3)       # right tongue
    lick(c, 28, 11, 26, 19, 3, flat, bend=2)      # small right lick
    lick(c, 4, 12, 6, 20, 3, flat, bend=-2)       # small left lick
    c.circle(16, 18, 10, flat)                    # core
    lv = sphere_levels(c, 16, 18, 11.0, light=(-0.25, -0.85, 0.46),
                       lo=-0.55, hi=0.90, n=4)
    apply_ramp(c, lv, FIRE_OUT)
    # inner incandescent core
    inner = new_canvas(32, 32, name="fire_inner")
    inner.circle(15, 17, 6, flat)
    lv2 = sphere_levels(inner, 15, 17, 7.0, light=(-0.45, -0.66, 0.60),
                        lo=0.05, hi=0.90, n=4)
    apply_ramp(inner, lv2, FIRE_IN)
    c.blit(inner, 0, 0)
    # white hot heart + specular
    c.circle(13, 15, 2, FIRE_HOT)
    c.set(11, 13, "#ffffff")
    c.set(12, 13, "#ffffff")
    # embers
    for (x, y, col) in [(4, 3, "#fba919"), (5, 3, "#fba919"), (4, 4, "#fba919"),
                        (28, 2, "#fb9a22"), (29, 2, "#fb9a22"),
                        (2, 24, "#cf3a15"), (2, 25, "#cf3a15"), (3, 25, "#cf3a15"),
                        (29, 24, "#fba919"), (29, 25, "#fba919")]:
        c.set(x, y, col)
    return c

# ---------------------------------------------------------------- ice shield
SHIELD_OUT = "M5,4 Q16,1 27,4 L27,17 Q27,24 16,30 Q5,24 5,17 Z"
SHIELD_IN  = "M8,7 Q16,4 24,7 L24,16 Q24,22 16,27 Q8,22 8,16 Z"

def draw_ice():
    c = new_canvas(32, 32, name="ice")
    c.path(SHIELD_OUT, "#4d92c4", fill=True)
    c.path(SHIELD_IN, "#4b95cd", fill=True)
    rim = mask_of(c, "#4d92c4")
    fld = mask_of(c, "#4b95cd")
    lv = dir_levels(c, toward=(-0.60, -0.80), lo=0.10, hi=0.90, n=3)
    apply_ramp(c, lv, ICE_RIM, only=rim)
    lv2 = sphere_levels(c, 15, 13, 15.0, light=(-0.48, -0.62, 0.62),
                        lo=0.05, hi=0.92, n=4)
    apply_ramp(c, lv2, ICE_FLD, only=fld)
    # glassy streaks lower-right
    for k in range(5):
        c.set(19 + k, 24 - k, ICE_FLD[3])
    for k in range(3):
        c.set(21 + k, 24 - k, ICE_FLD[2])
    # snowflake emblem
    cx, cy = 16, 15
    c.line(cx, cy - 6, cx, cy + 6, ICE_WHITE)
    c.line(cx - 5, cy - 3, cx + 5, cy + 3, ICE_WHITE)
    c.line(cx - 5, cy + 3, cx + 5, cy - 3, ICE_WHITE)
    for (sx, sy) in [(0, -1), (0, 1)]:
        bx, by = cx + sx * 4, cy + sy * 4
        c.set(bx - 1, by + sy * 0, ICE_WHITE); c.set(bx + 1, by + sy * 0, ICE_WHITE)
        c.set(bx - 1, by - sy * 1, ICE_WHITE); c.set(bx + 1, by - sy * 1, ICE_WHITE)
    c.set(cx - 3, cy - 3, ICE_WHITE); c.set(cx + 3, cy + 3, ICE_WHITE)
    c.set(cx - 3, cy + 3, ICE_WHITE); c.set(cx + 3, cy - 3, ICE_WHITE)
    c.set(cx, cy, "#ffffff")
    return c

# ---------------------------------------------------------------- healing
HEART = ("M16,28 C16,28 4,20 4,13 C4,8 8,5 12,5 C14,5 16,7 16,9 "
         "C16,7 18,5 20,5 C24,5 28,8 28,13 C28,20 16,28 16,28 Z")

def draw_heal():
    c = new_canvas(32, 32, name="heal")
    c.path(HEART, "#c81f42", fill=True)
    lv = sphere_levels(c, 13, 12, 15.0, light=(-0.46, -0.66, 0.59),
                       lo=0.05, hi=0.90, n=4)
    apply_ramp(c, lv, HRT)
    # gloss on the upper-left lobe
    c.path("M7,12 Q7,8 11,7", HRT_GLOS, fill=False)
    c.set(6, 13, HRT_GLOS)
    # cross emblem with an inner shadow
    sh = new_canvas(32, 32, name="heal_x")
    sh.rect(15, 10, 3, 12, CROSS_SH)
    sh.rect(11, 14, 11, 3, CROSS_SH)
    c.blit(sh, 1, 1)
    cr = new_canvas(32, 32, name="heal_x2")
    cr.rect(15, 10, 3, 12, CROSS)
    cr.rect(11, 14, 11, 3, CROSS)
    c.blit(cr, 0, 0)
    # glints
    for (x, y) in [(4, 3), (28, 4), (27, 26)]:
        c.set(x, y, SPARK); c.set(x + 1, y, "#ffffff")
        c.set(x, y + 1, "#ffffff"); c.set(x + 1, y + 1, SPARK)
    return c

# ---------------------------------------------------------------- lightning
BOLT_PTS = [(20, 8), (10, 20), (16, 20), (9, 30), (24, 15), (17, 15), (26, 8)]

def draw_bolt():
    c = new_canvas(32, 32, name="bolt")
    # bolt first so the cloud overlaps its top
    b = new_canvas(32, 32, name="bolt_b")
    b.poly(BOLT_PTS, "#f9a90f", fill=True)
    lv = dir_levels(b, toward=(-0.80, -0.60), lo=0.10, hi=0.90, n=4)
    apply_ramp(b, lv, BOLT)
    c.blit(b, 0, 0)
    # storm cloud
    cl = new_canvas(32, 32, name="bolt_c")
    cl.circle(8, 8, 4, "#545e80")
    cl.circle(16, 6, 5, "#545e80")
    cl.circle(24, 8, 4, "#545e80")
    cl.rect(4, 9, 25, 4, "#545e80")
    lv = sphere_levels(cl, 11, 3, 20.0, light=(-0.44, -0.70, 0.56),
                       lo=0.05, hi=0.92, n=4)
    apply_ramp(cl, lv, CLD)
    c.blit(cl, 0, 0)
    # sparks
    for (x, y) in [(4, 20), (27, 22), (6, 27)]:
        c.set(x, y, SPARK)
        c.set(x - 1, y, "#fcd329"); c.set(x + 1, y, "#fcd329")
        c.set(x, y - 1, "#fcd329"); c.set(x, y + 1, "#fcd329")
    return c

# ---------------------------------------------------------------- assemble
result = new_canvas(64, 64, name="result")
result.blit(draw_fire(), 0, 0)
result.blit(draw_ice(), 32, 0)
result.blit(draw_heal(), 0, 32)
result.blit(draw_bolt(), 32, 32)
outline_all(result, INK)

print(result.stats_text())
save("skill_icons", result, indexed=True)
p = view(result, scale=8, margin=0)
print("view:", p)
finish(result)
