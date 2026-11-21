import math

W = H = 256
c = new_canvas(W, H, background="#0a0810", name="output")

# ---------------- palette ----------------
# dark hall
c.color("#0a0810", "bg0")
c.color("#120f1c", "bg1")
c.color("#1a1526", "bg2")
c.color("#241d33", "bg3")
c.color("#2e2540", "bg4")

# stone
c.color("#2b2a33", "st_dark")
c.color("#3c3a47", "st_mid")
c.color("#4e4c5b", "st_lite")
c.color("#64627235", "st_hi")

# brass
c.color("#1c1408", "br_out")
c.color("#3a2a10", "br_sh2")
c.color("#5b4418", "br_sh1")
c.color("#8a6a24", "br_mid")
c.color("#b08a32", "br_lit")
c.color("#d8b14a", "br_hi")
c.color("#f3dd93", "br_gl")

# copper / alt metal
c.color("#2a1208", "cu_out")
c.color("#6b2f14", "cu_sh")
c.color("#9c4a1e", "cu_mid")
c.color("#c8732f", "cu_lit")
c.color("#e8a357", "cu_hi")

# rune / glow cyan
c.color("#07343c", "gl_dk")
c.color("#0d6b78", "gl_md")
c.color("#19b4c4", "gl_lt")
c.color("#8df2fb", "gl_hi")
c.color("#e8ffff", "gl_wt")

# core gold-white
c.color("#6b3a07", "co_dk")
c.color("#c47a12", "co_md")
c.color("#f0b53a", "co_lt")
c.color("#ffe79a", "co_hi")
c.color("#fffbe8", "co_wt")

# crystal purple
c.color("#2a1140", "px_dk")
c.color("#5a2a85", "px_md")
c.color("#8f52c9", "px_lt")
c.color("#c9a6f2", "px_hi")

# crystal green
c.color("#0d3320", "gr_dk")
c.color("#1d6b3e", "gr_md")
c.color("#3fae6a", "gr_lt")
c.color("#a6f0c0", "gr_hi")

# crystal red
c.color("#3d0f14", "rd_dk")
c.color("#8a2028", "rd_md")
c.color("#c8424a", "rd_lt")
c.color("#f59a9a", "rd_hi")

OUT = "br_out"

# ---------------- helpers ----------------
def ring(cx, cy, r, col, squash=1.0):
    """1px thick ellipse outline"""
    c.ellipse(cx, cy, r, max(1, int(round(r * squash))), col, fill=False)

def ell_band(cx, cy, rx, ry, thick, cols):
    """concentric ellipse outlines from outside in, cols listed outer->inner"""
    for i, col in enumerate(cols):
        c.ellipse(cx, cy, rx - i, max(1, ry - i), col, fill=False)

def arc_pts(cx, cy, rx, ry, a0, a1, n=240):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    return pts

def draw_arc(cx, cy, rx, ry, a0, a1, col, n=360):
    prev = None
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        x = int(round(cx + rx * math.cos(a)))
        y = int(round(cy + ry * math.sin(a)))
        if (x, y) != prev:
            c.set(x, y, col)
            prev = (x, y)


# =========================================================
# 1. DARK HALL BACKGROUND
# =========================================================
# vertical gradient-ish bands
for y in range(0, H):
    t = y / H
    if y < 40:
        col = "bg0"
    elif y < 90:
        col = "bg1"
    elif y < 150:
        col = "bg1"
    elif y < 200:
        col = "bg0"
    else:
        col = "bg0"
    c.rect(0, y, W, 1, col)

# distant arches / columns of the hall
for px in (16, 50, 206, 240):
    c.rect(px - 10, 20, 20, 190, "bg2")
    c.rect(px - 10, 20, 2, 190, "bg3")
    c.rect(px + 8, 20, 2, 190, "bg0")
    # fluting
    for k in range(-6, 8, 4):
        c.rect(px + k, 28, 1, 180, "bg3")
    # capital
    c.rect(px - 13, 20, 26, 7, "bg3")
    c.rect(px - 13, 20, 26, 1, "bg4")

# arch openings between columns
c.path("M 56 210 L 56 96 A 36 42 0 0 1 128 96 L 128 210 Z", "bg0")
c.path("M 128 210 L 128 96 A 36 42 0 0 1 200 96 L 200 210 Z", "bg0")
c.path("M 58 208 L 58 98 A 34 40 0 0 1 126 98 L 126 208 Z", "bg2", fill=False)
c.path("M 130 208 L 130 98 A 34 40 0 0 1 198 98 L 198 208 Z", "bg2", fill=False)

# floor
c.rect(0, 206, W, 50, "bg1")
c.rect(0, 206, W, 2, "bg2")
for y in range(210, 256, 6):
    c.rect(0, y, W, 1, "bg0")
# perspective floor lines
for x in range(-60, 330, 34):
    c.line(x, 256, 128 + (x - 128) // 6, 207, "bg0")

CX, CY = 128, 104

# =========================================================
# 2. STONE PEDESTAL
# =========================================================
# floor shadow
c.ellipse(CX, 248, 74, 10, "bg0")
c.ellipse(CX, 246, 60, 7, "bg0")

# base plinth
c.rect(76, 236, 104, 14, "st_dark")
c.rect(76, 236, 104, 2, "st_lite")
c.rect(78, 238, 100, 3, "st_mid")
c.rect(76, 248, 104, 2, "bg0")
# shaft (tapered)
for i, y in enumerate(range(214, 236)):
    half = 30 + int(i * 0.8)
    c.rect(CX - half, y, half * 2, 1, "st_dark")
    c.rect(CX - half, y, 5, 1, "st_mid")
    c.rect(CX - half + 5, y, 10, 1, "st_lite")
    c.rect(CX + half - 7, y, 7, 1, "bg2")
# top slab
c.rect(80, 206, 96, 9, "st_mid")
c.rect(80, 206, 96, 2, "st_lite")
c.rect(84, 204, 88, 3, "st_lite")
c.rect(84, 204, 88, 1, "st_hi")
c.rect(80, 213, 96, 2, "st_dark")
# slab edge shading
c.rect(166, 206, 10, 9, "st_dark")
c.rect(160, 204, 12, 3, "st_mid")

# carved band on the shaft
c.rect(96, 220, 64, 8, "bg2")
c.rect(96, 220, 64, 1, "st_dark")
for gx in range(100, 158, 10):
    c.rect(gx, 222, 2, 4, "gl_dk")
    c.rect(gx + 4, 223, 1, 3, "gl_dk")
    c.set(gx + 5, 222, "gl_md")

# chips / texture on plinth
for (tx, ty) in ((84, 243), (112, 241), (140, 245), (166, 242), (98, 247), (152, 240)):
    c.set(tx, ty, "st_mid")
    c.set(tx + 1, ty + 1, "bg0")

# =========================================================
# 3. ORRERY GEOMETRY HELPERS
# =========================================================
def oval_arc(cx, cy, rx, ry, rot, a0, a1, col, step=0.5):
    cr, sr = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    prev = None
    a = a0
    while a <= a1 + 1e-9:
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        px, py = rx * ca, ry * sa
        x = int(round(cx + px * cr - py * sr))
        y = int(round(cy + px * sr + py * cr))
        if (x, y) != prev:
            c.set(x, y, col)
            prev = (x, y)
        a += step

def band_arc(cx, cy, rx, ry, rot, a0, a1, cols, step=0.4):
    for i, col in enumerate(cols):
        oval_arc(cx, cy, rx - i, ry - i, rot, a0, a1, col, step)

def band_full(cx, cy, rx, ry, rot, cols, step=0.3):
    band_arc(cx, cy, rx, ry, rot, 0, 360, cols, step)

def pt(cx, cy, rx, ry, rot, a):
    cr, sr = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
    px, py = rx * ca, ry * sa
    return (int(round(cx + px * cr - py * sr)), int(round(cy + px * sr + py * cr)))

RUNES = [
    ["111", "010", "010"],
    ["101", "111", "101"],
    ["110", "011", "110"],
    ["111", "100", "111"],
    ["010", "111", "010"],
    ["101", "010", "101"],
    ["011", "110", "011"],
    ["100", "111", "001"],
]

def rune(x, y, idx, col):
    pat = RUNES[idx % len(RUNES)]
    for ry_, row in enumerate(pat):
        for rx_, ch in enumerate(row):
            if ch == "1":
                c.set(x + rx_, y + ry_, col)

def gear(gx, gy, r, teeth, body, lite, dark, hub):
    # teeth
    for t in range(teeth):
        a = 2 * math.pi * t / teeth
        tx = int(round(gx + (r + 1.6) * math.cos(a)))
        ty = int(round(gy + (r + 1.6) * math.sin(a)))
        c.rect(tx - 1, ty - 1, 3, 3, dark)
        c.set(tx, ty, body)
    c.circle(gx, gy, r, dark, fill=True)
    c.circle(gx, gy, r - 1, body, fill=True)
    c.circle(gx, gy, r - 2, lite, fill=False)
    # spokes
    for t in range(4):
        a = math.pi / 4 + math.pi / 2 * t
        c.line(gx, gy, int(round(gx + (r - 2) * math.cos(a))),
               int(round(gy + (r - 2) * math.sin(a))), lite)
    c.circle(gx, gy, max(1, r // 3), dark, fill=True)
    c.circle(gx, gy, max(1, r // 3 - 1), hub, fill=True)

def sphere(sx, sy, r, dk, md, lt, hi):
    c.circle(sx, sy, r + 1, OUT, fill=True)
    c.circle(sx, sy, r, dk, fill=True)
    c.circle(sx, sy, r - 1, md, fill=True)
    if r >= 3:
        c.circle(sx - 1, sy - 1, r - 2, lt, fill=True)
    c.circle(sx - max(1, r // 2), sy - max(1, r // 2), max(0, r // 3), hi, fill=True)
    if r >= 4:
        c.set(sx + r - 1, sy + 1, lt)

# orbit ring definitions: rx, ry, rot
ORBITS = [
    (86, 30, -14),
    (72, 52, 20),
    (54, 76, -8),
    (34, 62, 36),
]

# =========================================================
# 4. BACK HALVES OF ORBIT RINGS
# =========================================================
for (rx, ry, rot) in ORBITS:
    band_arc(CX, CY, rx, ry, rot, 180, 360, ["br_sh2", "br_sh1", "br_sh2"])

# =========================================================
# 5. MAIN FRAME RINGS (engraved concentric)
# =========================================================
# outermost heavy ring
band_full(CX, CY, 100, 96, 0, [OUT, "br_sh1", "br_mid", "br_hi", "br_lit", "br_mid", "br_sh1", OUT])
# engraved rune ring
band_full(CX, CY, 90, 86, 0, [OUT, "br_sh1", "br_sh2", "br_sh1", "br_mid", OUT])
# third ring
band_full(CX, CY, 80, 76, 0, [OUT, "br_mid", "br_hi", "br_lit", "br_mid", "br_sh1", OUT])

# runes along the engraved ring
for k in range(28):
    a = 360 * k / 28
    px, py = pt(CX, CY, 88, 84, 0, a)
    rune(px - 1, py - 1, k, "gl_lt")

# tick marks on the outer ring
for k in range(72):
    a = 360 * k / 72
    x0, y0 = pt(CX, CY, 99, 95, 0, a)
    x1, y1 = pt(CX, CY, 95, 91, 0, a)
    c.line(x0, y0, x1, y1, "br_sh2" if k % 6 else "gl_md")

# shadow pass: light from upper-left, so darken lower-right arcs
for (rx, ry) in ((100, 96), (99, 95), (98, 94), (97, 93), (90, 86), (89, 85),
                 (80, 76), (79, 75), (78, 74), (77, 73)):
    oval_arc(CX, CY, rx, ry, 0, 8, 100, "br_sh1", 0.3)
    oval_arc(CX, CY, rx, ry, 0, 30, 78, "br_sh2", 0.3)
# highlight pass upper-left
for (rx, ry) in ((98, 94), (97, 93), (78, 74), (77, 73)):
    oval_arc(CX, CY, rx, ry, 0, 195, 250, "br_gl", 0.3)

# =========================================================
# 6. MOUNTING YOKE / MERIDIAN ARMS
# =========================================================
# two heavy arms rising from the pedestal to the outer ring
c.path("M 100 206 L 112 206 L 120 196 L 112 190 L 96 204 Z", OUT)
c.path("M 101 205 L 111 205 L 118 196 L 112 192 L 98 203 Z", "br_sh1")
c.path("M 103 204 L 110 204 L 116 196 L 112 194 Z", "br_mid")
c.path("M 156 206 L 144 206 L 136 196 L 144 190 L 160 204 Z", OUT)
c.path("M 155 205 L 145 205 L 138 196 L 144 192 L 158 203 Z", "br_sh2")
c.path("M 153 204 L 146 204 L 140 196 L 144 194 Z", "br_sh1")
# collar where arms meet ring
c.rect(118, 192, 20, 10, OUT)
c.rect(119, 193, 18, 8, "br_sh1")
c.rect(120, 194, 16, 3, "br_mid")
c.rect(120, 197, 16, 1, "br_sh2")
for bx in (122, 127, 132):
    c.set(bx, 195, "br_gl")
    c.set(bx, 199, "br_sh2")

# =========================================================
# 7. BACK ORBIT SPHERES (behind the core)
# =========================================================
back_spheres = [
    (0, 212, 5, ("px_dk", "px_md", "px_lt", "px_hi")),
    (1, 250, 4, ("gr_dk", "gr_md", "gr_lt", "gr_hi")),
    (2, 200, 3, ("rd_dk", "rd_md", "rd_lt", "rd_hi")),
]
for (oi, ang, rr, cols) in back_spheres:
    rx, ry, rot = ORBITS[oi]
    sx, sy = pt(CX, CY, rx, ry, rot, ang)
    sphere(sx, sy, rr, *cols)

# =========================================================
# 8. CENTRAL RADIANT CORE
# =========================================================
# glow halo rings (sparse, so the machinery stays readable)
# soft radial glow, circle-clipped, density falls off with radius
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
for yy in range(CY - 40, CY + 41):
    for xx in range(CX - 40, CX + 41):
        d = math.hypot(xx - CX, yy - CY)
        if d > 40 or d < 14:
            continue
        thr = (d - 14) / 26.0 * 16.0
        if BAYER[yy & 3][xx & 3] < thr:
            continue
        c.set(xx, yy, "gl_dk" if d > 24 else "co_dk")
c.circle(CX, CY, 24, "co_dk", fill=False)

# radiant spikes
for k in range(16):
    a = 360 * k / 16
    ln = 34 if k % 2 == 0 else 24
    x1, y1 = pt(CX, CY, ln, ln, 0, a)
    x0, y0 = pt(CX, CY, 12, 12, 0, a)
    c.line(x0, y0, x1, y1, "co_md" if k % 2 == 0 else "co_dk")
for k in range(8):
    a = 360 * k / 8 + 22.5
    x1, y1 = pt(CX, CY, 44, 44, 0, a)
    x0, y0 = pt(CX, CY, 30, 30, 0, a)
    c.line(x0, y0, x1, y1, "gl_md")

# armature cage around the core
c.circle(CX, CY, 20, OUT, fill=False)
c.circle(CX, CY, 19, "br_mid", fill=False)
c.circle(CX, CY, 18, "br_sh1", fill=False)
for k in range(6):
    a = 360 * k / 6 + 15
    x0, y0 = pt(CX, CY, 18, 18, 0, a)
    x1, y1 = pt(CX, CY, 13, 13, 0, a)
    c.line(x0, y0, x1, y1, "br_hi")
    c.set(x0, y0, "br_gl")

# core body
c.circle(CX, CY, 13, "co_dk", fill=True)
c.circle(CX, CY, 11, "co_md", fill=True)
c.circle(CX, CY, 8, "co_lt", fill=True)
c.circle(CX, CY, 5, "co_hi", fill=True)
c.circle(CX, CY, 3, "co_wt", fill=True)
# core facets
for k in range(6):
    a = 360 * k / 6
    x1, y1 = pt(CX, CY, 12, 12, 0, a)
    c.line(CX, CY, x1, y1, "co_hi")

# =========================================================
# 9. FRONT HALVES OF ORBIT RINGS (lit, in front of core)
# =========================================================
for i, (rx, ry, rot) in enumerate(ORBITS):
    cols = ["br_sh1", "br_lit", "br_hi"] if i % 2 == 0 else ["br_sh2", "br_mid", "br_lit"]
    band_arc(CX, CY, rx, ry, rot, 0, 180, cols)
    # graduation marks on the front arcs
    for k in range(24):
        a = 180 * k / 24 + 3.75
        x0, y0 = pt(CX, CY, rx, ry, rot, a)
        c.set(x0, y0, "gl_md" if k % 3 == 0 else "br_sh2")

# rune glyphs riding the front arcs
for i, (rx, ry, rot) in enumerate(ORBITS):
    for k in range(5):
        a = 20 + 140 * k / 4
        px, py = pt(CX, CY, rx - 4, ry - 4, rot, a)
        if math.hypot(px - CX, py - CY) > 22:
            rune(px - 1, py - 1, k + i, "gl_lt")

# =========================================================
# 10. FRONT ORBITING CRYSTAL SPHERES
# =========================================================
front_spheres = [
    (0, 30, 6, ("px_dk", "px_md", "px_lt", "px_hi")),
    (1, 118, 5, ("rd_dk", "rd_md", "rd_lt", "rd_hi")),
    (2, 62, 4, ("gr_dk", "gr_md", "gr_lt", "gr_hi")),
    (3, 150, 4, ("gl_dk", "gl_md", "gl_lt", "gl_wt")),
    (0, 152, 3, ("gr_dk", "gr_md", "gr_lt", "gr_hi")),
    (2, 130, 3, ("px_dk", "px_md", "px_lt", "px_hi")),
]
for (oi, ang, rr, cols) in front_spheres:
    rx, ry, rot = ORBITS[oi]
    sx, sy = pt(CX, CY, rx, ry, rot, ang)
    # faint halo
    c.circle(sx, sy, rr + 3, cols[0], fill=False)
    sphere(sx, sy, rr, *cols)

# small moon on a bracket
rx, ry, rot = ORBITS[1]
mx, my = pt(CX, CY, rx, ry, rot, 118)
c.line(mx + 5, my, mx + 11, my - 4, "br_mid")
sphere(mx + 12, my - 5, 2, "st_dark", "st_mid", "st_lite", "co_hi")

# =========================================================
# 11. GEARS AND MACHINERY ON THE RING FRAME
# =========================================================
gear(CX, CY - 97, 9, 12, "br_mid", "br_hi", "br_sh2", "co_lt")
gear(CX - 12, CY - 88, 5, 9, "cu_mid", "cu_hi", "cu_sh", "co_md")
gear(CX + 13, CY - 87, 6, 10, "cu_mid", "cu_lit", "cu_sh", "gl_lt")
gear(CX - 97, CY + 12, 8, 12, "br_mid", "br_lit", "br_sh2", "gl_lt")
gear(CX + 96, CY - 16, 7, 11, "cu_mid", "cu_hi", "cu_sh", "co_lt")
gear(CX + 92, CY + 34, 5, 9, "br_mid", "br_hi", "br_sh2", "gl_md")
gear(CX - 88, CY - 44, 6, 10, "cu_mid", "cu_lit", "cu_sh", "co_md")
gear(CX - 40, CY + 92, 7, 11, "br_mid", "br_lit", "br_sh2", "co_lt")
gear(CX + 44, CY + 90, 6, 10, "cu_mid", "cu_hi", "cu_sh", "gl_lt")
gear(CX, CY + 100, 5, 9, "br_mid", "br_hi", "br_sh2", "co_hi")

# =========================================================
# 12. ALCHEMICAL DIALS
# =========================================================
def dial(dx, dy, r, face, needle_a, rim="br_hi"):
    c.circle(dx, dy, r + 1, OUT, fill=True)
    c.circle(dx, dy, r, rim, fill=True)
    c.circle(dx, dy, r - 1, "br_sh1", fill=True)
    c.circle(dx, dy, r - 2, face, fill=True)
    for k in range(8):
        a = 360 * k / 8
        px, py = pt(dx, dy, r - 2, r - 2, 0, a)
        c.set(px, py, "br_gl")
    nx, ny = pt(dx, dy, r - 3, r - 3, 0, needle_a)
    c.line(dx, dy, nx, ny, "gl_hi")
    c.set(dx, dy, "co_wt")

dial(CX - 70, CY + 64, 8, "gl_dk", -60)
dial(CX + 68, CY + 62, 7, "px_dk", 200)
dial(CX - 76, CY - 52, 6, "rd_dk", 40)
dial(CX + 74, CY - 56, 6, "gr_dk", 130)
dial(CX - 34, CY - 94, 5, "gl_dk", 250)

# side support struts carrying the dials
c.line(CX - 62, CY + 58, CX - 54, CY + 50, "br_sh1")
c.line(CX + 60, CY + 56, CX + 52, CY + 48, "br_sh1")

# =========================================================
# 13. HANGING CHAINS FROM THE DARKNESS
# =========================================================
for (hx, top) in ((CX - 100, 0), (CX + 100, 0)):
    c.line(hx, top, hx, CY - 12, "bg3")
    for yy in range(top, CY - 12, 4):
        c.set(hx, yy, "st_dark")
        c.set(hx - 1, yy + 2, "bg3")
c.line(CX - 100, CY - 12, CX - 100, CY - 10, "br_sh1")
c.line(CX + 100, CY - 12, CX + 100, CY - 10, "br_sh1")

# =========================================================
# 14. WALL BRAZIERS (dramatic side lighting)
# =========================================================
def brazier(bx, by):
    c.rect(bx - 4, by, 9, 4, "st_dark")
    c.rect(bx - 3, by, 7, 1, "st_mid")
    c.rect(bx - 2, by + 4, 5, 6, "st_dark")
    c.rect(bx - 1, by + 4, 2, 6, "bg3")
    # flame
    c.path("M %d %d Q %d %d %d %d Q %d %d %d %d Z" % (
        bx - 3, by, bx - 4, by - 7, bx, by - 13, bx + 4, by - 7, bx + 3, by), "cu_sh")
    c.path("M %d %d Q %d %d %d %d Q %d %d %d %d Z" % (
        bx - 2, by, bx - 3, by - 6, bx, by - 10, bx + 3, by - 6, bx + 2, by), "cu_lit")
    c.path("M %d %d Q %d %d %d %d Q %d %d %d %d Z" % (
        bx - 1, by, bx - 1, by - 4, bx, by - 7, bx + 1, by - 4, bx + 1, by), "co_hi")
    c.set(bx, by - 4, "co_wt")

brazier(20, 120)
brazier(236, 120)

# =========================================================
# 15. LIGHTING WASH (translucent layer, composited)
# =========================================================
light = new_canvas(W, H, name="light")
BY = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
for yy in range(H):
    for xx in range(W):
        d = math.hypot(xx - CX, (yy - CY) * 1.05)
        if d < 101 or d > 148:
            continue
        t = 1.0 - (d - 101) / 47.0
        t = t * t
        lvl = BY[yy & 3][xx & 3] / 16.0
        if lvl < t * 0.45:
            light.set(xx, yy, "#c0802c30")
        elif lvl < t * 0.8:
            light.set(xx, yy, "#8a5a2018")

# braziers cast their own pools
for (bx, by) in ((20, 116), (236, 116)):
    for yy in range(by - 40, by + 70):
        for xx in range(bx - 30, bx + 32):
            if not (0 <= xx < W and 0 <= yy < H):
                continue
            d = math.hypot(xx - bx, (yy - by) * 0.7)
            if d > 32:
                continue
            t = (1.0 - d / 32.0) ** 2
            if BY[yy & 3][xx & 3] / 16.0 < t * 0.6:
                light.set(xx, yy, "#e0863028")

c2 = flatten([c, light], name="result")

# =========================================================
# 16. FINAL SPECULARS (drawn on the composite, crisp)
# =========================================================
# re-sharpen brass highlights on the upper-left of the big rings
for (rx, ry) in ((98, 94), (97, 93), (78, 74)):
    oval_arc2 = None
for k in range(90):
    a = 196 + k * 0.6
    for (rx, ry) in ((98, 94), (78, 74)):
        px, py = pt(CX, CY, rx, ry, 0, a)
        c2.set(px, py, "br_gl")

# bright rim on the core and its cage
c2.circle(CX, CY, 3, "co_wt", fill=True)
c2.set(CX - 2, CY - 2, "co_wt")

# glow reflection on the pedestal slab
for xx in range(88, 170):
    for yy in range(204, 215):
        if BY[yy & 3][xx & 3] < 5 and abs(xx - CX) < 40:
            c2.set(xx, yy, "co_md" if yy < 208 else "cu_sh")
c2.rect(84, 204, 88, 1, "co_hi")

# darken the hall floor corners so the pedestal reads
for xx in range(W):
    for yy in range(206, H):
        if abs(xx - CX) > 86 and BY[yy & 3][xx & 3] < 9:
            c2.set(xx, yy, "bg0")

# floor glow under the pedestal
for xx in range(60, 198):
    for yy in range(248, 256):
        d = math.hypot((xx - CX) * 0.5, (yy - 250) * 2.2)
        if d < 40 and BY[yy & 3][xx & 3] / 16.0 < (1 - d / 40.0) * 0.5:
            c2.set(xx, yy, "cu_sh")

# sparkles
for (sx, sy) in ((CX - 56, CY - 70), (CX + 62, CY - 40), (CX - 30, CY + 76),
                 (CX + 40, CY + 66), (CX + 20, CY - 82), (CX - 72, CY + 20)):
    c2.set(sx, sy, "gl_wt")
    c2.set(sx - 1, sy, "gl_lt")
    c2.set(sx + 1, sy, "gl_lt")
    c2.set(sx, sy - 1, "gl_lt")
    c2.set(sx, sy + 1, "gl_lt")

print(c2.stats_text())
view(c2)
save("orrery", c2)
finish(c2)
