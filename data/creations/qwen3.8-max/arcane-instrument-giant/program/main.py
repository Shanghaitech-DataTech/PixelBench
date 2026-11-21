import math
from pixelbench_api import new_canvas, flatten, view, save, finish, np

W = H = 256
CX, CY = 128, 86
TAU = math.pi * 2

# ------------------------------------------------------------------ palettes
BRASS = ["#201504", "#3a2809", "#573d11", "#775719", "#987223", "#b98f31",
         "#d6ae45", "#eecf68", "#fbe9a4", "#fff8d8"]
COPP = ["#261005", "#401c09", "#5e2c11", "#7e3e18", "#9d5423", "#bb7134",
        "#d69152", "#eeb479", "#ffd9a8"]
STEEL = ["#0d0d14", "#181822", "#252531", "#343444", "#45455a", "#595972",
         "#71718c", "#8b8ba6", "#ababc4", "#cfd0e2"]
CRYST = ["#061420", "#0c2740", "#123c5e", "#1a577e", "#24779e", "#359bbd",
         "#57bed6", "#8adff0", "#c4f4ff", "#eefdff"]
CORE = ["#421003", "#701d04", "#9c3206", "#c2520c", "#e27616", "#f99c26",
        "#ffc24c", "#ffdf85", "#fff3c0", "#ffffff"]
RUNEC = ["#0a3325", "#116049", "#1d9470", "#37c99a", "#74eec6", "#b6ffe6"]
STONE = ["#07060c", "#0c0a14", "#12101d", "#191628", "#211d34", "#2b2543",
         "#372f55", "#463c6b", "#584c85"]

bg = new_canvas(W, H, name="bg")
mach = new_canvas(W, H, name="mach")
halo = new_canvas(W, H, name="halo")
fg = new_canvas(W, H, name="fg")


def R(hexes):
    return [bg.color(h) for h in hexes]


BI, CI, SI, XI, OI, GI, TI = R(BRASS), R(COPP), R(STEEL), R(CRYST), R(CORE), R(RUNEC), R(STONE)
DARKO = bg.color("#07050d")


def pick(ramp, t):
    n = len(ramp)
    i = int(round(t * (n - 1)))
    if i < 0:
        i = 0
    if i > n - 1:
        i = n - 1
    return ramp[i]


def px(cv, x, y, col):
    if 0 <= x < W and 0 <= y < H:
        cv.set(x, y, col)


def line_px(cv, x0, y0, x1, y1, col):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    dx = abs(x1 - x0); dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        px(cv, x0, y0, col)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy; x0 += sx
        if e2 <= dx:
            err += dx; y0 += sy


def disc(cv, cx, cy, r, col):
    cx = int(round(cx)); cy = int(round(cy))
    r2 = r * r
    for y in range(int(cy - r) - 1, int(cy + r) + 2):
        dy = y - cy
        for x in range(int(cx - r) - 1, int(cx + r) + 2):
            dx = x - cx
            if dx * dx + dy * dy <= r2:
                px(cv, x, y, col)


def glow_ellipse(cv, cx, cy, rx, ry, bands):
    x0 = max(0, int(cx - rx)); x1 = min(W - 1, int(cx + rx))
    y0 = max(0, int(cy - ry)); y1 = min(H - 1, int(cy + ry))
    for y in range(y0, y1 + 1):
        dy = (y - cy) / ry
        for x in range(x0, x1 + 1):
            dx = (x - cx) / rx
            d = math.sqrt(dx * dx + dy * dy)
            if d > 1.0:
                continue
            for frac, col in bands:
                if d <= frac:
                    cv.set(x, y, col)
                    break


# ------------------------------------------------------------------ ring engine
def ering(cv, cx, cy, Rr, w, sx=1.0, sy=1.0, rot=0.0, ramp=BI, half=None,
          light=-1.9, tube=True, spec=True, edge=True, lum=1.0, a0=None,
          a1=None, grooves=0):
    ca, sa = math.cos(rot), math.sin(rot)
    a = (Rr + w) * sx; b = (Rr + w) * sy
    hw = math.sqrt((a * ca) ** 2 + (b * sa) ** 2) + 1.5
    hh = math.sqrt((a * sa) ** 2 + (b * ca) ** 2) + 1.5
    x0 = max(0, int(cx - hw)); x1 = min(W - 1, int(cx + hw))
    y0 = max(0, int(cy - hh)); y1 = min(H - 1, int(cy + hh))
    n = len(ramp)
    for y in range(y0, y1 + 1):
        dy = y - cy
        for x in range(x0, x1 + 1):
            dx = x - cx
            lx = dx * ca + dy * sa
            ly = -dx * sa + dy * ca
            u = lx / sx; v = ly / sy
            r = math.sqrt(u * u + v * v)
            d = r - Rr
            if d < -w or d > w:
                continue
            if half == "near" and v < 0:
                continue
            if half == "far" and v > 0:
                continue
            if a0 is not None:
                aa = math.atan2(dy, dx) % TAU
                if not (a0 <= aa <= a1):
                    continue
            t = (d + w) / (2.0 * w)
            th = math.atan2(dy, dx)
            diff = 0.5 + 0.5 * math.cos(th - light)
            tb = math.sin(math.pi * t)
            L = 0.10 + 0.58 * diff * (0.42 + 0.58 * tb)
            if spec:
                s = max(0.0, math.cos(th - light))
                L += 0.40 * (s ** 9) * (0.3 + 0.7 * tb)
            if edge and (t < 0.09 or t > 0.91):
                L *= 0.40
            if grooves:
                gt = t * grooves
                if abs(gt - round(gt)) < 0.16:
                    L *= 0.45
            cv.set(x, y, pick(ramp, L * lum))


def gear(cv, cx, cy, Rr, teeth, th_h, hub, ramp=BI, rot=0.0, spokes=0,
         light=-1.9, lum=1.0):
    rad = Rr + th_h + 1
    x0 = max(0, int(cx - rad)); x1 = min(W - 1, int(cx + rad))
    y0 = max(0, int(cy - rad)); y1 = min(H - 1, int(cy + rad))
    n = len(ramp)
    for y in range(y0, y1 + 1):
        dy = y - cy
        for x in range(x0, x1 + 1):
            dx = x - cx
            r = math.sqrt(dx * dx + dy * dy)
            if r > Rr + th_h or r < hub:
                continue
            th = math.atan2(dy, dx)
            k = int(((th + rot) % TAU) / TAU * teeth)
            outer = Rr + (th_h if k % 2 == 0 else 0)
            if r > outer:
                continue
            if spokes and hub + 1.5 < r < Rr - 2.5:
                seg = (((th + rot) % TAU) / TAU * spokes) % 1.0
                if 0.26 < seg < 0.74:
                    continue
            diff = 0.5 + 0.5 * math.cos(th - light)
            L = 0.12 + 0.50 * diff
            if r > Rr - 1.2:
                L += 0.22
            if r < hub + 1.6:
                L += 0.16
            if r > outer - 0.6:
                L += 0.12
            cv.set(x, y, pick(ramp, L * lum))


def orb(cv, cx, cy, r, ramp=XI, outline=True, lx=-0.45, ly=-0.62):
    cx = int(round(cx)); cy = int(round(cy))
    if outline:
        disc(cv, cx, cy, r + 1.2, DARKO)
    lz = 0.64
    ln = math.sqrt(lx * lx + ly * ly + lz * lz)
    lx /= ln; ly /= ln; lz /= ln
    for y in range(int(cy - r) - 1, int(cy + r) + 2):
        dy = (y - cy) / r
        for x in range(int(cx - r) - 1, int(cx + r) + 2):
            dx = (x - cx) / r
            d2 = dx * dx + dy * dy
            if d2 > 1.0:
                continue
            z = math.sqrt(1.0 - d2)
            diff = dx * lx + dy * ly + z * lz
            L = 0.06 + 0.80 * max(0.0, diff)
            d = math.sqrt(d2)
            if d > 0.70:
                L += 0.34 * ((d - 0.70) / 0.30) ** 1.6
            sd = math.sqrt((dx - lx * 0.55) ** 2 + (dy - ly * 0.55) ** 2)
            if sd < 0.30:
                L += 0.55 * (1 - sd / 0.30)
            cv.set(x, y, pick(ramp, L))


def runes_glyph(cv, gx, gy, g, ramp=GI, bright=4):
    for j, row in enumerate(g):
        for i, ch in enumerate(row):
            if ch == '1':
                px(cv, gx + i, gy + j, ramp[bright])


RUNES = [
    ["11111", "...1.", "..1..", ".1...", "11111"],
    ["1...1", ".1.1.", "..1..", ".1.1.", "1...1"],
    ["11111", "1....", "1111.", "1....", "11111"],
    ["..1..", ".111.", "1.1.1", "..1..", ".1.1."],
    ["1...1", "1...1", ".1.1.", "..1..", "..1.."],
    ["11111", "..1..", "..1..", "..1..", "11111"],
    [".111.", "1...1", "1.1.1", "1...1", ".111."],
    ["1....", "1111.", "1...1", "1...1", "11111"],
    ["..1..", ".1.1.", "1...1", "11111", "..1.."],
    ["1.1.1", "1.1.1", "11111", ".1.1.", ".1.1."],
    ["11111", "1...1", "1.1.1", "1...1", "11111"],
    [".1.1.", "1.1.1", "..1..", "1.1.1", ".1.1."],
]

# ================================================================== BACKGROUND
bg.rect(0, 0, W, H, STONE[1])
for y in range(0, 158):
    bg.rect(0, y, W, 1, pick(TI, 0.10 + 0.30 * (y / 158.0)))
for by in range(0, 158, 26):
    line_px(bg, 0, by, W - 1, by, STONE[0])
    line_px(bg, 0, by + 1, W - 1, by + 1, STONE[3])
    off = 0 if (by // 26) % 2 == 0 else 32
    for bx in range(off, W, 64):
        line_px(bg, bx, by, bx, min(by + 25, 157), STONE[0])
        line_px(bg, bx + 1, by, bx + 1, min(by + 25, 157), STONE[3])

# great carved medallion niche behind the instrument
mcx, mcy = 128, 92
for y in range(0, 210):
    dy = y - mcy
    for x in range(0, W):
        dx = x - mcx
        r = math.sqrt(dx * dx + dy * dy)
        if r > 124:
            continue
        th = math.atan2(dy, dx)
        if r < 96:
            L = 0.04 + 0.18 * (r / 96.0)
            col = pick(TI, L)
            if r > 92:
                col = STONE[0]
        elif r < 112:
            seg = int(((th + 0.13) % TAU) / TAU * 24)
            base = 0.26 + 0.32 * (0.5 + 0.5 * math.cos(th + 1.2))
            if seg % 2 == 0:
                base += 0.05
            col = pick(TI, base)
            loc = (r - 96) / 16.0
            if loc < 0.08 or loc > 0.92:
                col = STONE[0]
            elif loc < 0.18:
                col = pick(TI, base + 0.18)
            ang = ((th % TAU) / TAU * 24) % 1.0
            if ang < 0.045:
                col = STONE[0]
        else:
            loc = (r - 112) / 12.0
            col = pick(TI, 0.34 - 0.24 * loc)
            if loc > 0.86:
                col = STONE[0]
        bg.set(x, y, col)

for k in range(12):
    a = k / 12.0 * TAU - math.pi / 2
    gx = int(round(mcx + 104 * math.cos(a))) - 2
    gy = int(round(mcy + 104 * math.sin(a))) - 2
    runes_glyph(bg, gx, gy, RUNES[k], TI, 6)

# side pilasters
for x0, x1 in ((0, 20), (236, 255)):
    for x in range(x0, x1 + 1):
        t = (x - x0) / float(x1 - x0)
        col = pick(TI, 0.12 + 0.46 * math.sin(math.pi * t) ** 0.7)
        line_px(bg, x, 0, x, 158, col)
    line_px(bg, x0, 0, x0, 158, STONE[0])
    line_px(bg, x1, 0, x1, 158, STONE[0])
    for fl in range(x0 + 3, x1 - 1, 5):
        line_px(bg, fl, 6, fl, 150, STONE[0])
        line_px(bg, fl + 1, 6, fl + 1, 150, pick(TI, 0.46))
    bg.rect(x0, 140, x1 - x0 + 1, 4, pick(TI, 0.44))
    bg.rect(x0, 144, x1 - x0 + 1, 2, STONE[0])
    bg.rect(max(0, x0 - 2), 146, min(W, x1 + 3) - max(0, x0 - 2), 12, pick(TI, 0.34))
    line_px(bg, max(0, x0 - 2), 146, min(255, x1 + 2), 146, pick(TI, 0.60))

# ------------------------------------------------------------- floor
HOR = 158
for y in range(HOR, H):
    t = (y - HOR) / float(H - HOR)
    bg.rect(0, y, W, 1, pick(TI, 0.07 + 0.26 * t))
for k in range(-7, 8):
    line_px(bg, 128 + k * 7, HOR, 128 + k * 130, H - 1, STONE[0])
for i, y in enumerate([163, 170, 180, 194, 213, 238]):
    line_px(bg, 0, y, W - 1, y, STONE[0])
    line_px(bg, 0, y + 1, W - 1, y + 1, pick(TI, 0.22))

# ------------------------------------------------------------- pedestal
PED_TOP = 178


def stone_block(x0, y0, x1, y1, base, lit, warm=0.0):
    for y in range(y0, y1 + 1):
        t = (y - y0) / float(max(1, y1 - y0))
        for x in range(x0, x1 + 1):
            u = (x - x0) / float(max(1, x1 - x0))
            L = base + lit * (1.0 - t) ** 1.3 * (0.35 + 0.65 * math.sin(math.pi * u) ** 0.5)
            if x == x0 or x == x1:
                L *= 0.55
            px(bg, x, y, pick(TI, L))
    line_px(bg, x0, y0, x1, y0, pick(TI, base + lit + 0.16))
    line_px(bg, x0, y1, x1, y1, STONE[0])


stone_block(70, PED_TOP, 186, PED_TOP + 8, 0.30, 0.62)
stone_block(82, PED_TOP + 9, 174, PED_TOP + 16, 0.22, 0.36)
stone_block(78, PED_TOP + 17, 178, PED_TOP + 46, 0.18, 0.26)
stone_block(64, PED_TOP + 47, 192, PED_TOP + 56, 0.20, 0.24)
stone_block(54, PED_TOP + 57, 202, PED_TOP + 70, 0.15, 0.18)
for xx in range(70, 187):
    px(bg, xx, PED_TOP, pick(OI, 0.32))
    px(bg, xx, PED_TOP + 1, pick(TI, 0.74))
for xx in range(64, 193):
    if xx % 5 < 3:
        px(bg, xx, PED_TOP + 47, pick(OI, 0.16))
for (px0, px1) in ((86, 120), (136, 170)):
    bg.rect(px0, PED_TOP + 22, px1 - px0 + 1, 20, STONE[0])
    bg.rect(px0 + 1, PED_TOP + 23, px1 - px0 - 1, 18, pick(TI, 0.20))
    line_px(bg, px0 + 1, PED_TOP + 23, px1 - 1, PED_TOP + 23, pick(TI, 0.36))
    runes_glyph(bg, px0 + 13, PED_TOP + 29, RUNES[(px0 // 3) % 12], GI, 2)
runes_glyph(bg, 125, PED_TOP + 11, RUNES[3], GI, 3)
# inscribed summoning circle on the pedestal top
for k in range(64):
    a = k / 64.0 * TAU
    px(bg, int(round(128 + 44 * math.cos(a))), int(round(PED_TOP + 4 + 3 * math.sin(a))), pick(TI, 0.62))
    px(bg, int(round(128 + 30 * math.cos(a))), int(round(PED_TOP + 4 + 2 * math.sin(a))), pick(TI, 0.50))
for k in range(6):
    a = k / 6.0 * TAU
    px(bg, int(round(128 + 37 * math.cos(a))), int(round(PED_TOP + 4 + 2.5 * math.sin(a))), pick(GI, 0.4))

# ================================================================== HALO / LIGHT
bands_c = [(0.30, bg.color("#4fb6d82e")), (0.55, bg.color("#2f86aa24")),
           (0.78, bg.color("#1d5f7e18")), (1.0, bg.color("#123c5210"))]
bands_w = [(0.28, bg.color("#ffc06030")), (0.55, bg.color("#e08a2822")),
           (0.80, bg.color("#a85c1814")), (1.0, bg.color("#6a3a100c"))]
glow_ellipse(halo, 128, 92, 126, 122, bands_c)
glow_ellipse(halo, 128, 90, 74, 72, bands_w)
glow_ellipse(halo, 30, 96, 30, 34, bands_w)
glow_ellipse(halo, 226, 96, 30, 34, bands_w)
glow_ellipse(halo, 128, 202, 100, 34,
             [(0.25, bg.color("#7fe0ff26")), (0.5, bg.color("#3f96c01a")),
              (0.75, bg.color("#26648812")), (1.0, bg.color("#153c560a"))])
glow_ellipse(halo, 128, 182, 66, 14,
             [(0.5, bg.color("#bfeeff30")), (1.0, bg.color("#5aa8c818"))])
glow_ellipse(halo, 128, 232, 76, 22,
             [(0.4, bg.color("#c2520c1c")), (1.0, bg.color("#701d040e"))])

# ================================================================== INSTRUMENT
LIGHT = -1.95

# polar axis rod (behind everything)
for x in range(125, 132):
    t = (x - 125) / 6.0
    line_px(mach, x, 10, x, 164, pick(BI, 0.10 + 0.75 * math.sin(math.pi * t)))
disc(mach, 128, 8, 5, pick(BI, 0.30))
orb(mach, 128, 8, 5, BI, outline=False, lx=-0.4, ly=-0.7)
line_px(mach, 128, 1, 128, 4, pick(BI, 0.75))
disc(mach, 128, 166, 6, pick(BI, 0.25))
orb(mach, 128, 165, 6, BI, outline=False, lx=-0.4, ly=-0.7)

# --- back halves of the tilted great rings
ering(mach, CX, CY, 70, 2.6, sx=0.30, sy=1.0, rot=0.22, ramp=BI, half="far", lum=0.72)
ering(mach, CX, CY, 62, 2.4, sx=1.0, sy=0.30, rot=-0.18, ramp=CI, half="far", lum=0.72)
ering(mach, CX, CY, 52, 2.2, sx=0.62, sy=1.0, rot=-0.35, ramp=BI, half="far", lum=0.78)

# --- gear train (behind the great limb)
gear(mach, 86, 150, 12, 12, 3, 4, BI, rot=0.12, spokes=5)
gear(mach, 128, 158, 15, 14, 3, 4, CI, rot=0.05, spokes=6)
gear(mach, 170, 150, 12, 12, 3, 4, BI, rot=0.30, spokes=5)
gear(mach, 58, 136, 7, 7, 2, 2, SI, rot=0.4, spokes=0)
gear(mach, 198, 136, 7, 7, 2, 2, SI, rot=0.2, spokes=0)
for (gx, gy, gr) in ((86, 150, 3), (128, 158, 3), (170, 150, 3), (58, 136, 2), (198, 136, 2)):
    disc(mach, gx, gy, gr, pick(SI, 0.25))
    px(mach, gx, gy, pick(SI, 0.70))
    px(mach, gx - 1, gy - 1, pick(SI, 0.50))
ering(mach, 128, 150, 46, 3.0, sx=1.0, sy=0.24, rot=0.0, ramp=CI, half="near")

# --- outer case ring (the great engraved limb)
ering(mach, CX, CY, 78, 4.6, ramp=BI, grooves=3)
for k in range(72):
    a = k / 72.0 * TAU
    r0 = 74.0 if k % 6 else 72.0
    x1 = CX + 82 * math.cos(a); y1 = CY + 82 * math.sin(a)
    x0 = CX + r0 * math.cos(a); y0 = CY + r0 * math.sin(a)
    line_px(mach, x0, y0, x1, y1, pick(BI, 0.06) if k % 6 else pick(BI, 0.30))
for k in range(12):
    a = k / 12.0 * TAU + 0.26
    xr = CX + 78 * math.cos(a); yr = CY + 78 * math.sin(a)
    disc(mach, xr, yr, 1.6, pick(BI, 0.85))
    px(mach, int(xr), int(yr), pick(BI, 0.98))
# struts linking the ecliptic band to the limb (lower half)
for k in range(9):
    a = math.pi * (0.58 + 0.84 * k / 8.0)
    line_px(mach, CX + 70 * math.cos(a), CY + 70 * math.sin(a),
            CX + 73.8 * math.cos(a), CY + 73.8 * math.sin(a), pick(BI, 0.28))
    line_px(mach, CX + 70 * math.cos(a) + 1, CY + 70 * math.sin(a),
            CX + 73.8 * math.cos(a) + 1, CY + 73.8 * math.sin(a), pick(BI, 0.60))

# --- ecliptic band with runes
ering(mach, CX, CY, 64, 6.2, ramp=BI, light=-1.95)
ering(mach, CX, CY, 64, 6.2, ramp=CI, a0=math.pi * 0.15, a1=math.pi * 0.85, lum=0.85)
for k in range(48):
    a = k / 48.0 * TAU
    long_ = (k % 4 == 0)
    r0 = 58.6 if long_ else 60.6
    line_px(mach, CX + r0 * math.cos(a), CY + r0 * math.sin(a),
            CX + 69.4 * math.cos(a), CY + 69.4 * math.sin(a),
            pick(BI, 0.05) if long_ else pick(BI, 0.16))
for k in range(12):
    a = k / 12.0 * TAU - math.pi / 2 + math.pi / 12
    gx = int(round(CX + 64 * math.cos(a))) - 2
    gy = int(round(CY + 64 * math.sin(a))) - 2
    runes_glyph(mach, gx, gy, RUNES[k], GI, 3)

# --- inner armillary rings (back halves)
ering(mach, CX, CY, 46, 2.4, sx=1.0, sy=0.34, rot=0.30, ramp=BI, half="far")
ering(mach, CX, CY, 40, 2.0, sx=0.34, sy=1.0, rot=-0.30, ramp=CI, half="far")

# --- orbit arms + spheres (back)
ORB_BACK = [(0.55, 30, 5.0), (2.35, 44, 4.2), (3.75, 36, 3.6)]
for a, rad, rr in ORB_BACK:
    ox = CX + rad * math.cos(a); oy = CY + rad * 0.62 * math.sin(a)
    line_px(mach, CX, CY, int(ox), int(oy), pick(BI, 0.22))
    line_px(mach, CX, CY + 1, int(ox), int(oy) + 1, pick(BI, 0.45))
    orb(mach, ox, oy, rr, XI)

# --- alchemical dials
def dial(cx, cy, r):
    disc(mach, cx, cy, r + 2, DARKO)
    ering(mach, cx, cy, r, 2.2, ramp=BI)
    for k in range(8):
        a = k / 8.0 * TAU + 0.39
        px(mach, int(round(cx + r * math.cos(a))), int(round(cy + r * math.sin(a))), pick(BI, 0.9))
    disc(mach, cx, cy, r - 2.4, pick(SI, 0.20))
    for k in range(16):
        a = k / 16.0 * TAU
        rr0 = r - 3.0 if k % 4 == 0 else r - 4.2
        line_px(mach, cx + rr0 * math.cos(a), cy + rr0 * math.sin(a),
                cx + (r - 2.6) * math.cos(a), cy + (r - 2.6) * math.sin(a),
                pick(BI, 0.72 if k % 4 == 0 else 0.45))
    for k in range(4):
        a = (k + 0.5) / 4.0 * TAU
        px(mach, int(cx + (r - 5) * math.cos(a)), int(cy + (r - 5) * math.sin(a)), GI[4])
    pa = -0.7
    line_px(mach, cx, cy, int(cx + (r - 4) * math.cos(pa)), int(cy + (r - 4) * math.sin(pa)), CORE[8])
    line_px(mach, cx, cy, int(cx + 3 * math.cos(pa + math.pi)), int(cy + 3 * math.sin(pa + math.pi)), pick(BI, 0.6))
    disc(mach, cx, cy, 1.6, pick(BI, 0.9))
    for j in range(-r + 3, 0):
        for i in range(-r + 3, r - 2):
            if i * i + j * j < (r - 3) ** 2 and (i + j) % 7 == 0:
                px(mach, cx + i, cy + j, pick(XI, 0.55))


dial(76, 122, 14)
dial(180, 122, 14)
line_px(mach, 62, 106, 70, 114, pick(BI, 0.5))
line_px(mach, 63, 106, 71, 114, pick(BI, 0.3))
line_px(mach, 194, 106, 186, 114, pick(BI, 0.5))
line_px(mach, 193, 106, 185, 114, pick(BI, 0.3))

# --- central radiant core
disc(mach, CX, CY, 21, DARKO)
ering(mach, CX, CY, 19, 2.4, ramp=SI)
for k in range(8):
    a = k / 8.0 * TAU + 0.2
    line_px(mach, CX + 15 * math.cos(a), CY + 15 * math.sin(a),
            CX + 19 * math.cos(a), CY + 19 * math.sin(a), pick(BI, 0.6))
orb(mach, CX, CY, 14, OI, outline=False, lx=-0.3, ly=-0.45)
disc(mach, CX, CY, 6, OI[9])
disc(mach, CX - 2, CY - 3, 3, OI[9])
for a in (0.0, math.pi / 3, 2 * math.pi / 3):
    x1 = CX + 17 * math.cos(a); y1 = CY + 17 * math.sin(a)
    x0 = CX - 17 * math.cos(a); y0 = CY - 17 * math.sin(a)
    line_px(mach, x0, y0, x1, y1, pick(BI, 0.30))
    line_px(mach, x0, y0 - 1, x1, y1 - 1, pick(BI, 0.62))
ering(mach, CX, CY, 17, 1.3, sx=1.0, sy=0.36, rot=0.5, ramp=BI, half="near")

# --- front halves of the tilted great rings
ering(mach, CX, CY, 70, 2.6, sx=0.30, sy=1.0, rot=0.22, ramp=BI, half="near")
ering(mach, CX, CY, 62, 2.4, sx=1.0, sy=0.30, rot=-0.18, ramp=CI, half="near")
ering(mach, CX, CY, 52, 2.2, sx=0.62, sy=1.0, rot=-0.35, ramp=BI, half="near")
ering(mach, CX, CY, 46, 2.4, sx=1.0, sy=0.34, rot=0.30, ramp=BI, half="near")
ering(mach, CX, CY, 40, 2.0, sx=0.34, sy=1.0, rot=-0.30, ramp=CI, half="near")

# --- orbit arms + spheres (front)
ORB_FRONT = [(1.30, 40, 6.0), (2.85, 54, 5.0), (4.35, 30, 4.0),
             (5.60, 48, 3.6), (0.05, 24, 3.2)]
for a, rad, rr in ORB_FRONT:
    ox = CX + rad * math.cos(a); oy = CY + rad * 0.62 * math.sin(a)
    line_px(mach, CX, CY, int(ox), int(oy), pick(BI, 0.30))
    line_px(mach, CX, CY - 1, int(ox), int(oy) - 1, pick(BI, 0.58))
    disc(mach, int(ox), int(oy), 2, pick(BI, 0.5))
    orb(mach, ox, oy, rr, XI)

# --- hanging crystal pendulums from the limb
for a in (2.35, 2.75, 0.45, 0.85):
    x0 = CX + 78 * math.cos(a); y0 = CY + 78 * math.sin(a)
    ln = 8 + int(6 * abs(math.cos(a * 2)))
    line_px(mach, x0, y0, x0, y0 + ln, pick(BI, 0.45))
    orb(mach, x0, y0 + ln + 3, 3.2, XI)

# --- wall torches (brackets + flames)
for tx in (30, 226):
    sgn = 1 if tx < 128 else -1
    line_px(mach, tx - 6 * sgn, 102, tx, 98, pick(CI, 0.45))
    line_px(mach, tx - 6 * sgn, 103, tx, 99, pick(CI, 0.25))
    disc(mach, tx, 96, 3, pick(CI, 0.55))
    orb(mach, tx, 92, 3, OI, outline=False, lx=-0.2, ly=-0.8)
    px(mach, tx, 88, OI[8])
    px(mach, tx - 1, 89, OI[6])
    px(mach, tx + 1, 89, OI[6])

# ================================================================== OUTLINE
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
dil = new_canvas(W, H, name="dil")
for dx, dy in DIRS:
    t = mach.copy()
    t.shift(dx, dy, fill=None)
    dil.blit(t, 0, 0)
_ww, _hh, _buf = dil.to_rgba()
_arr = np.frombuffer(_buf, np.uint8).reshape(_hh, _ww, 4)
_ys, _xs = np.nonzero(_arr[:, :, 3] > 0)
for x, y in zip(_xs.tolist(), _ys.tolist()):
    dil.set(x, y, DARKO)

# ================================================================== FOREGROUND GLOW
for k in range(12):
    a = k / 12.0 * TAU - math.pi / 2 + math.pi / 12
    gx = int(round(CX + 64 * math.cos(a))) - 2
    gy = int(round(CY + 64 * math.sin(a))) - 2
    glow_ellipse(fg, gx + 2, gy + 2, 6, 6,
                 [(0.4, bg.color("#7dffd446")), (1.0, bg.color("#2fa87a1c"))])
    runes_glyph(fg, gx, gy, RUNES[k], GI, 5)

glow_ellipse(fg, CX, CY, 46, 46,
             [(0.16, bg.color("#fff3c0a0")), (0.30, bg.color("#ffc24c60")),
              (0.52, bg.color("#f08a1e34")), (0.78, bg.color("#c2520c1c")),
              (1.0, bg.color("#701d040e"))])
for k in range(12):
    a = k / 12.0 * TAU
    ln = 42 if k % 3 == 0 else 26
    for i in range(16, ln):
        t = 1.0 - (i - 16) / float(ln - 16)
        col = pick(OI, 0.30 + 0.62 * t)
        x = int(round(CX + i * math.cos(a))); y = int(round(CY + i * math.sin(a)))
        px(fg, x, y, col)
        if k % 3 == 0:
            px(fg, x + 1, y, pick(OI, 0.25 + 0.4 * t))

for a, rad, rr in ORB_FRONT:
    ox = CX + rad * math.cos(a); oy = CY + rad * 0.62 * math.sin(a)
    glow_ellipse(fg, ox, oy, rr * 3.2, rr * 3.2,
                 [(0.32, bg.color("#c4f4ff50")), (0.6, bg.color("#57bed62c")),
                  (1.0, bg.color("#24779e14"))])
for a, rad, rr in ORB_BACK:
    ox = CX + rad * math.cos(a); oy = CY + rad * 0.62 * math.sin(a)
    glow_ellipse(fg, ox, oy, rr * 2.6, rr * 2.6,
                 [(0.4, bg.color("#8adff03c")), (1.0, bg.color("#24779e18"))])
for (dx0, dy0) in ((76, 122), (180, 122)):
    glow_ellipse(fg, dx0, dy0, 12, 12,
                 [(0.5, bg.color("#ffc24c22")), (1.0, bg.color("#f08a1e10"))])
for tx in (30, 226):
    glow_ellipse(fg, tx, 92, 16, 20,
                 [(0.3, bg.color("#ffc24c50")), (0.6, bg.color("#e2761628")),
                  (1.0, bg.color("#9c320612"))])
# levitation magic between instrument and pedestal
glow_ellipse(fg, 128, 176, 34, 9,
             [(0.22, bg.color("#c4f4ff80")), (0.45, bg.color("#8adff050")),
              (0.70, bg.color("#37c99a2c")), (1.0, bg.color("#1d7a5a14"))])
for k in range(9):
    a = math.pi + k / 8.0 * math.pi
    rx = 128 + 40 * math.cos(a) * 0.9
    ry = 174 + 8 * math.sin(a)
    px(fg, int(rx), int(ry), pick(XI, 0.85))
    px(fg, int(rx), int(ry) - 1, pick(GI, 0.7))
seed = 7
for i in range(90):
    seed = (seed * 1103515245 + 12345) % 2147483648
    mx = (seed >> 8) % 256
    seed = (seed * 1103515245 + 12345) % 2147483648
    my = (seed >> 8) % 256
    d = math.hypot(mx - 128, my - 92)
    if d < 40 or d > 130 or my > 172:
        continue
    px(fg, mx, my, pick(XI, 0.55 + 0.4 * ((i % 5) / 4.0)))

# ================================================================== COMPOSITE
comp = flatten([bg, halo, dil, mach, fg], name="comp")


# ================================================================== QUANTIZE
def quantize(cv, k):
    w, h, buf = cv.to_rgba()
    a = np.frombuffer(buf, np.uint8).reshape(h, w, 4)
    vis = a[:, :, 3] > 0
    u, inv, cnt = np.unique(a[vis], axis=0, return_inverse=True, return_counts=True)
    groups = [np.arange(len(u))]
    while len(groups) < k:
        best = -1; bs = -1.0
        for bi, ix in enumerate(groups):
            if len(ix) < 2:
                continue
            cc = u[ix][:, :3].astype(np.int64)
            rng = cc.max(0) - cc.min(0)
            score = int(rng.max()) * int(cnt[ix].sum())
            if score > bs:
                bs = score; best = bi
        if best < 0:
            break
        ix = groups.pop(best)
        cc = u[ix][:, :3].astype(np.int64)
        rng = cc.max(0) - cc.min(0)
        ax = int(rng.argmax())
        order = np.argsort(cc[:, ax], kind="stable")
        ixo = ix[order]
        csum = np.cumsum(cnt[ixo])
        mid = int(np.searchsorted(csum, csum[-1] / 2))
        mid = min(max(mid, 1), len(ixo) - 1)
        groups.append(ixo[:mid]); groups.append(ixo[mid:])
    lut = np.zeros((len(u), 4), np.uint8)
    pal = []
    for ix in groups:
        mean = (u[ix].astype(np.float64) * cnt[ix][:, None]).sum(0) / cnt[ix].sum()
        q = np.clip(np.round(mean), 0, 255).astype(np.uint8)
        lut[ix] = q
        pal.append(tuple(int(v) for v in q))
    newc = lut[inv]
    res = new_canvas(w, h, name="result")
    for c in pal:
        res.color(c)
    ys, xs = np.nonzero(vis)
    xl = xs.tolist(); yl = ys.tolist()
    flat = newc.reshape(-1, 4).tolist()
    for i in range(len(xl)):
        res.set(xl[i], yl[i], tuple(flat[yl[i] * w + xl[i]]))
    return res


out = quantize(comp, 134)
print(out.stats_text())
save("arcane_instrument", out)
print(view(out))
finish(out)
