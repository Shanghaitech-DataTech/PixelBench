import math

W = H = 64
c = new_canvas(W, H, name="tavern")

# ---------------------------------------------------------------- palette ---
INK       = "#120b0a"
INK_SOFT  = "#241610"

CEIL      = "#291a14"
CEIL_BEAM = "#3b261c"
CEIL_DK   = "#1b110d"

WALL_A    = "#453129"
WALL_B    = "#3d2a23"
WALL_SEAM = "#2d1d17"

FLOOR_A   = "#4b3320"
FLOOR_B   = "#402a19"
FLOOR_SEAM= "#291909"

WOOD      = "#6b4423"
WOOD_LT   = "#8a5a2b"
WOOD_HI   = "#b8793a"
WOOD_DK   = "#4a2d17"
WOOD_XDK  = "#33200f"
TRIM      = "#a9713a"

CAB_BACK  = "#21140e"
SHELF     = "#7a4f28"
SHELF_DK  = "#3d2513"

B_GREEN   = "#3f7a3a"; B_GREEN_HI = "#63a94f"
B_AMBER   = "#b5651d"; B_AMBER_HI = "#e5953a"
B_BLUE    = "#3a6ea5"; B_BLUE_HI  = "#6fa8d8"
B_RED     = "#93362f"; B_RED_HI   = "#c25a45"
B_CLEAR   = "#9db8bc"; B_CLEAR_HI = "#dcebef"
B_DARK    = "#4a3a2a"; B_DARK_HI  = "#6d5a42"
CORK      = "#c9a06a"
LABEL     = "#ddcfa9"

GLASS     = "#b3c9cd"
GLASS_HI  = "#eef6f7"
BEER      = "#d1922a"
BEER_HI   = "#efbf58"
FOAM      = "#f4e7c8"
BREAD     = "#c9873c"
CHEESE    = "#e6c257"

NIGHT     = "#151e39"
NIGHT_LT  = "#233159"
NIGHT_XD  = "#0c1226"
MOON      = "#e9eef6"
MOON_DIM  = "#8b9ac0"
STAR      = "#cfd8ee"
LITWIN    = "#e0a53a"

METAL     = "#8a7a5a"
METAL_HI  = "#c9b48a"
METAL_DK  = "#4a3f2c"

LAMP_SH   = "#a8652a"
LAMP_SH_D = "#6d3f1c"
LAMP_SH_HI= "#d38d3e"
GLOW_HOT  = "#fff2c0"
GLOW_MID  = "#f0bf55"
GLOW_DIM  = "#a8762f"

HAZE_DIM  = "#6d5a4e"
HAZE_MID  = "#8d7867"
HAZE_LT   = "#b39d89"

COOL      = "#5b6b8c"

BAYER = [
    [0, 8, 2, 10],
    [12, 4, 14, 6],
    [3, 11, 1, 9],
    [15, 7, 13, 5],
]

def dith(x, y, s):
    return BAYER[y & 3][x & 3] < s * 16

# ---------------------------------------------------------------- ceiling ---
c.rect(0, 0, 64, 6, CEIL)
c.rect(0, 0, 64, 1, CEIL_DK)
c.rect(0, 2, 64, 2, CEIL_BEAM)
c.rect(0, 4, 64, 1, CEIL_DK)
c.line(0, 5, 63, 5, INK_SOFT)
for x in (7, 23, 39, 55):
    c.rect(x, 2, 1, 2, CEIL_DK)

# ------------------------------------------------------------------- wall ---
c.rect(0, 6, 64, 42, WALL_A)
for i, x in enumerate(range(0, 64, 8)):
    c.rect(x, 6, 8, 42, WALL_A if i % 2 == 0 else WALL_B)
    c.rect(x, 6, 1, 42, WALL_SEAM)
# knots and grain
for (kx, ky) in [(12, 12), (36, 9), (52, 34), (18, 40), (60, 42), (44, 14)]:
    c.set(kx, ky, WALL_SEAM)
    c.set(kx + 1, ky, INK_SOFT)

# ------------------------------------------------------------------ floor ---
c.rect(0, 48, 64, 16, FLOOR_A)
c.rect(0, 48, 64, 1, INK_SOFT)
c.rect(0, 49, 64, 3, FLOOR_B)
c.rect(0, 52, 64, 1, FLOOR_SEAM)
c.rect(0, 53, 64, 4, FLOOR_A)
c.rect(0, 57, 64, 1, FLOOR_SEAM)
c.rect(0, 58, 64, 4, FLOOR_B)
c.rect(0, 62, 64, 1, FLOOR_SEAM)
c.rect(0, 63, 64, 1, FLOOR_A)
for (jx, jy) in [(9, 50), (33, 50), (55, 50), (18, 55), (44, 55), (7, 60), (29, 60), (52, 60)]:
    c.rect(jx, jy, 1, 3 if jy < 57 else 2, FLOOR_SEAM)

# ----------------------------------------------------------------- window ---
c.rect(43, 4, 20, 25, INK)
c.rect(44, 5, 18, 23, WOOD_DK)
c.rect(45, 6, 16, 21, WOOD)
c.rect(47, 8, 13, 17, NIGHT)
c.rect(47, 8, 13, 4, NIGHT_XD)
c.rect(47, 21, 13, 4, NIGHT_LT)
# moon + halo
c.circle(50, 12, 2, MOON)
c.set(48, 11, MOON_DIM); c.set(52, 13, MOON_DIM)
for y in range(8, 18):
    for x in range(47, 56):
        d = math.hypot(x - 50, y - 12)
        if 2.5 < d < 4.2 and dith(x, y, 0.28 * (1 - (d - 2.5) / 1.7)):
            c.set(x, y, MOON_DIM)
# stars
for (sx, sy) in [(56, 9), (58, 13), (55, 17), (48, 19), (57, 20), (49, 9)]:
    c.set(sx, sy, STAR)
# distant roofs
c.poly([(47, 24), (47, 21), (50, 19), (53, 21), (53, 24)], NIGHT_XD, fill=True)
c.poly([(53, 24), (53, 20), (56, 18), (60, 20), (60, 24)], NIGHT_XD, fill=True)
c.set(51, 21, LITWIN); c.set(57, 20, LITWIN)
# mullions
c.rect(53, 8, 1, 17, WOOD_DK)
c.rect(47, 16, 13, 1, WOOD_DK)
c.rect(47, 8, 1, 17, INK_SOFT)
# sill
c.rect(42, 27, 22, 2, WOOD)
c.rect(42, 27, 22, 1, WOOD_LT)
c.rect(42, 29, 22, 1, INK)

# --------------------------------------------------- back bar (bottles) ----
c.rect(0, 6, 33, 26, INK)
c.rect(1, 7, 31, 24, CAB_BACK)
c.rect(1, 7, 31, 2, WOOD)
c.rect(1, 7, 31, 1, WOOD_LT)
c.rect(1, 9, 2, 22, WOOD_DK)
c.rect(30, 9, 2, 22, WOOD_DK)
c.rect(2, 9, 1, 22, WOOD)
c.rect(30, 9, 1, 22, WOOD)

def board(y):
    c.rect(1, y, 31, 1, SHELF)
    c.rect(3, y, 27, 1, SHELF)
    c.line(3, y, 29, y, TRIM)
    c.rect(1, y + 1, 31, 1, SHELF_DK)

board(15)
board(23)
board(29)

def bottle(x, top, h, w, col, hi):
    bot = top + h - 1
    nw = 1 if w <= 3 else 2
    nx = x + (w - nw) // 2
    c.rect(x, top + 3, w, h - 3, col)
    c.rect(nx, top + 1, nw, 2, col)
    c.rect(nx, top, nw, 1, CORK)
    c.rect(x, top + 3, 1, h - 3, hi)
    if h > 5:
        c.rect(x + w - 1, top + 4, 1, h - 5, INK_SOFT)
    else:
        c.set(x + w - 1, top + 3, INK_SOFT)
    c.rect(x, bot, w, 1, INK_SOFT)
    if h >= 6 and w >= 3:
        c.rect(x + 1, top + 5, w - 2, 2, LABEL)

GREEN = (B_GREEN, B_GREEN_HI); AMBER = (B_AMBER, B_AMBER_HI)
BLUE = (B_BLUE, B_BLUE_HI); RED = (B_RED, B_RED_HI)
CLEAR = (B_CLEAR, B_CLEAR_HI); DARK = (B_DARK, B_DARK_HI)

rowA = [(3, 6, 3, GREEN), (7, 5, 2, AMBER), (10, 6, 3, BLUE), (14, 4, 2, CLEAR),
        (17, 6, 3, RED), (21, 5, 2, DARK), (24, 6, 3, AMBER), (28, 5, 2, GREEN)]
for (x, h, w, col) in rowA:
    bottle(x, 15 - h, h, w, col[0], col[1])

rowB = [(3, 5, 2, RED), (6, 6, 3, AMBER), (10, 4, 2, GREEN), (13, 5, 3, CLEAR),
        (17, 6, 2, BLUE), (20, 4, 3, DARK), (24, 5, 2, AMBER), (27, 6, 3, GREEN)]
for (x, h, w, col) in rowB:
    bottle(x, 23 - h, h, w, col[0], col[1])

# bottom compartment: mugs + glasses + jug
def tiny_mug(x, bot, col, hi):
    c.rect(x, bot - 3, 3, 4, col)
    c.rect(x, bot - 3, 1, 4, hi)
    c.rect(x + 3, bot - 2, 1, 2, col)
    c.rect(x, bot, 3, 1, INK_SOFT)

def tiny_glass(x, bot):
    c.rect(x, bot - 2, 2, 3, GLASS)
    c.set(x, bot - 2, GLASS_HI)
    c.rect(x, bot, 2, 1, INK_SOFT)

tiny_mug(3, 28, WOOD_LT, TRIM)
tiny_glass(8, 28)
tiny_mug(11, 28, WOOD, WOOD_LT)
tiny_glass(16, 28)
c.rect(19, 25, 4, 4, B_CLEAR); c.rect(19, 25, 1, 4, B_CLEAR_HI)
c.rect(20, 24, 2, 1, B_CLEAR); c.rect(19, 28, 4, 1, INK_SOFT)
tiny_mug(25, 28, METAL_DK, METAL)

# -------------------------------------------------------------- barrels ---
def barrel(cx, top, bot, hw):
    n = bot - top
    for y in range(top, bot + 1):
        t = (y - top) / max(1, n)
        w = int(round(hw + math.sin(t * math.pi) * 1.7))
        x0 = max(0, cx - w); x1 = min(W - 1, cx + w)
        c.line(x0, y, x1, y, WOOD)
        c.line(x0 + 1, y, min(x0 + 2, x1), y, WOOD_LT)
        c.set(x0, y, INK)
        if x1 < W - 1:
            c.set(x1, y, INK)
            c.set(x1 - 1, y, WOOD_XDK)
    # lid
    lx0 = max(0, cx - hw + 1); lx1 = min(W - 1, cx + hw - 1)
    c.line(lx0, top, lx1, top, INK)
    c.line(lx0, top + 1, lx1, top + 1, WOOD_DK)
    # staves
    for sx in (cx - 3, cx + 1, cx + 4):
        for y in range(top + 2, bot):
            if dith(sx, y, 0.5):
                c.set(sx, y, WOOD_XDK)
    # hoops
    for hy in (top + 4, bot - 5):
        w1 = int(round(hw + math.sin(((hy - top) / n) * math.pi) * 1.7))
        w2 = int(round(hw + math.sin(((hy + 1 - top) / n) * math.pi) * 1.7))
        a1 = max(0, cx - w1 + 1); b1 = min(W - 1, cx + w1 - 1)
        a2 = max(0, cx - w2 + 1); b2 = min(W - 1, cx + w2 - 1)
        c.line(a1, hy, b1, hy, METAL_DK)
        c.line(a2, hy + 1, b2, hy + 1, METAL)
        c.line(a2, hy + 1, min(cx - 2, b2), hy + 1, METAL_HI)

barrel(59, 31, 48, 5)
barrel(53, 35, 57, 7)

# ---------------------------------------------------------------- counter ---
c.rect(0, 32, 46, 1, INK_SOFT)
c.rect(0, 33, 46, 5, WALL_SEAM)
for y in range(33, 38):
    for x in range(0, 46):
        if dith(x, y, 0.35):
            c.set(x, y, WALL_B)

c.rect(0, 38, 46, 1, WOOD_HI)
c.rect(0, 39, 46, 1, WOOD_LT)
c.rect(0, 40, 46, 1, WOOD)
c.rect(0, 41, 46, 1, WOOD_XDK)
c.rect(46, 38, 1, 4, INK)
c.rect(0, 42, 46, 11, WOOD)
for x in range(0, 46, 6):
    c.rect(x, 42, 1, 11, WOOD_XDK)
for px in (2, 16, 30):
    c.rect(px, 44, 12, 7, INK_SOFT)
    c.rect(px + 1, 45, 10, 5, WOOD_DK)
    c.line(px + 1, 45, px + 10, 45, WOOD_XDK)
    c.line(px + 1, 49, px + 10, 49, WOOD)
c.rect(43, 42, 3, 11, WOOD_DK)
c.rect(45, 42, 1, 11, INK)
# warm lamplight falling on the counter front
for lx in (14, 38):
    for y in range(42, 53):
        for x in range(lx - 9, lx + 10):
            if 0 <= x < 46:
                d = math.hypot((x - lx) / 9.0, (y - 41) / 12.0)
                if d < 1 and dith(x, y, 0.45 * (1 - d) ** 1.4):
                    c.set(x, y, WOOD_LT)
# foot rail
c.rect(0, 53, 46, 1, METAL_HI)
c.rect(0, 54, 46, 1, METAL)
c.rect(0, 55, 46, 1, METAL_DK)
for bx in (5, 21, 37):
    c.rect(bx, 52, 2, 4, METAL_DK)
c.rect(0, 56, 46, 1, INK_SOFT)

# --------------------------------------------------------- counter top items
def tankard(x, y, w, h):
    c.rect(x, y, w, h, WOOD_LT)
    c.rect(x, y, 1, h, TRIM)
    c.rect(x + w - 1, y, 1, h, WOOD_DK)
    c.rect(x, y, w, 1, METAL_HI)
    c.rect(x, y + h - 2, w, 1, METAL_DK)
    c.rect(x + w, y + 1, 1, h - 3, METAL_DK)
    c.rect(x + w + 1, y + 2, 1, h - 5, METAL_DK)
    c.rect(x, y + h - 1, w, 1, INK_SOFT)

tankard(4, 32, 5, 6)

# beer glass
c.rect(11, 33, 3, 5, BEER)
c.rect(11, 33, 1, 5, BEER_HI)
c.rect(11, 33, 3, 1, FOAM)
c.set(11, 32, FOAM); c.set(13, 32, FOAM)
c.rect(13, 34, 1, 4, GLASS)
c.rect(11, 37, 3, 1, INK_SOFT)

# plate with bread and cheese
c.rect(16, 36, 7, 1, GLASS)
c.rect(16, 37, 7, 1, INK_SOFT)
c.rect(17, 34, 4, 2, BREAD)
c.rect(17, 34, 4, 1, CHEESE)
c.set(20, 35, BREAD)
c.rect(21, 35, 2, 1, CHEESE)

# wine glass
c.poly([(25, 33), (28, 33), (27, 36), (26, 36)], GLASS, fill=True)
c.rect(26, 34, 2, 2, B_RED)
c.rect(26, 36, 1, 1, GLASS)
c.rect(25, 37, 3, 1, GLASS)
c.set(25, 33, GLASS_HI)

# candle
c.rect(32, 35, 3, 3, METAL_DK)
c.rect(32, 35, 3, 1, METAL)
c.rect(33, 31, 1, 4, FOAM)
c.set(33, 30, GLOW_HOT)
c.set(33, 29, GLOW_MID)

# tall mug with foam
c.rect(38, 31, 5, 7, GLASS)
c.rect(38, 32, 5, 6, BEER)
c.rect(38, 31, 5, 1, FOAM)
c.rect(38, 32, 1, 6, BEER_HI)
c.rect(42, 32, 1, 5, GLASS)
c.rect(43, 33, 1, 3, GLASS)
c.rect(38, 37, 5, 1, INK_SOFT)

# ------------------------------------------------------------------ stools ---
def stool(cx):
    c.ellipse(cx, 60, 7, 2, INK_SOFT)
    c.line(cx - 1, 49, cx - 6, 59, WOOD_XDK)
    c.line(cx - 2, 49, cx - 7, 59, WOOD_XDK)
    c.line(cx + 1, 49, cx + 6, 59, WOOD_XDK)
    c.line(cx + 2, 49, cx + 7, 59, WOOD_XDK)
    c.line(cx - 5, 56, cx + 5, 56, METAL_DK)
    c.line(cx - 5, 55, cx + 5, 55, METAL)
    c.rect(cx - 1, 48, 3, 9, WOOD_DK)
    c.rect(cx - 1, 48, 1, 9, WOOD)
    c.ellipse(cx, 46, 7, 3, INK)
    c.ellipse(cx, 46, 6, 2, WOOD_DK)
    c.ellipse(cx, 45, 6, 2, WOOD_LT)
    c.ellipse(cx, 45, 4, 1, TRIM)

stool(9)
stool(25)
stool(41)

# ------------------------------------------------------------------- lamps ---
def lamp(cx):
    c.rect(cx, 0, 1, 8, INK_SOFT)
    c.rect(cx - 1, 0, 1, 8, WOOD_XDK)
    c.poly([(cx - 2, 8), (cx + 2, 8), (cx + 6, 14), (cx - 6, 14)], LAMP_SH, fill=True)
    c.line(cx - 2, 9, cx - 5, 13, LAMP_SH_HI)
    c.line(cx - 1, 9, cx - 3, 13, LAMP_SH_HI)
    c.line(cx + 2, 9, cx + 5, 13, LAMP_SH_D)
    c.rect(cx - 6, 14, 13, 1, LAMP_SH_D)
    c.rect(cx - 4, 15, 9, 1, GLOW_MID)
    c.rect(cx - 2, 15, 5, 2, GLOW_HOT)
    c.rect(cx - 1, 17, 3, 1, FOAM)

# ------------------------------------------------------------- light pools --
def pool(cx, cy, rx, ry, inten, col):
    for y in range(max(0, cy - ry), min(H, cy + ry + 1)):
        for x in range(max(0, cx - rx), min(W, cx + rx + 1)):
            d = math.hypot((x - cx) / rx, (y - cy) / ry)
            if d > 1:
                continue
            s = inten * (1 - d) ** 1.6
            if dith(x, y, s):
                c.set(x, y, col)

pool(14, 45, 8, 4, 0.18, WOOD_LT)
pool(38, 45, 8, 4, 0.18, WOOD_LT)
pool(53, 42, 7, 4, 0.14, WOOD_LT)

def radial_glow(cx, cy, r, inten=1.0):
    for y in range(max(0, int(cy - r)), min(H, int(cy + r) + 1)):
        for x in range(max(0, int(cx - r)), min(W, int(cx + r) + 1)):
            d = math.hypot(x - cx, (y - cy) * 1.12)
            if d > r:
                continue
            s = inten * (1 - d / r) ** 2.6
            if s >= 0.85:
                c.set(x, y, GLOW_HOT); continue
            if s >= 0.4:
                col, s2 = GLOW_HOT, 0.4
            elif s >= 0.22:
                col, s2 = GLOW_MID, 0.28
            elif s >= 0.11:
                col, s2 = GLOW_MID, 0.14
            elif s >= 0.05:
                col, s2 = GLOW_DIM, 0.10
            else:
                continue
            if dith(x, y, s2):
                c.set(x, y, col)

radial_glow(14, 16, 9, 1.0)
radial_glow(38, 16, 9, 1.0)
radial_glow(14, 21, 17, 0.32)
radial_glow(38, 21, 17, 0.32)
radial_glow(33, 30, 5, 0.8)

# redraw lamps on top of their glow so shades stay crisp
lamp(14)
lamp(38)

# moonlight cool spill: wall strip under the sill + rim on barrel left edge
for x in range(44, 64):
    if dith(x, 30, 0.35):
        c.set(x, 30, COOL)
for y in range(36, 46):
    if dith(46, y, 0.5):
        c.set(46, y, COOL)

# ------------------------------------------------------------------ smoke ---
sm = new_canvas(W, H, name="smoke_mask")
MA = "#ff00ff"
MB = "#00ff00"

def smoke_col(x0, y0, y1, amp, phase, r0, r1, col, steps=26):
    for i in range(steps + 1):
        t = i / steps
        y = y0 + (y1 - y0) * t
        x = x0 + amp * math.sin(t * math.pi * 1.8 + phase) * (0.35 + t)
        r = r0 + (r1 - r0) * t
        sm.ellipse(int(round(x)), int(round(y)), max(1, int(round(r))),
                   max(1, int(round(r * 0.62))), col)

# wide soft body
smoke_col(15, 18, 4, 4.0, 0.4, 1.6, 3.2, MA)
smoke_col(37, 18, 5, 3.6, 2.2, 1.6, 3.2, MA)
smoke_col(33, 30, 16, 2.4, 1.2, 1.0, 2.6, MA)
smoke_col(52, 34, 20, 2.6, 3.0, 1.2, 2.8, MA)
for i in range(10):
    t = i / 9
    sm.ellipse(int(8 + t * 48), int(11 + 3 * math.sin(t * 4)), 4, 1, MA)
# bright cores
smoke_col(33, 30, 18, 2.4, 1.2, 0.6, 1.2, MB)
smoke_col(52, 34, 22, 2.6, 3.0, 0.6, 1.2, MB)
smoke_col(15, 19, 8, 4.0, 0.4, 0.7, 1.3, MB)
smoke_col(37, 19, 9, 3.6, 2.2, 0.7, 1.3, MB)

ia = sm.color(MA)
ib = sm.color(MB)
for y in range(H):
    for x in range(W):
        v = sm.get(x, y)
        if v == ib:
            col, s = HAZE_LT, 0.30
        elif v == ia:
            col, s = HAZE_MID, 0.16
        else:
            continue
        if dith(x, y, s):
            c.set(x, y, col)

# broad low haze band
for y in range(22, 38):
    for x in range(0, 64):
        s = 0.10 * math.exp(-((y - 30) ** 2) / 40.0)
        if dith(x, y, s):
            c.set(x, y, HAZE_DIM)

# --------------------------------------------------------------- vignette ---
for y in range(H):
    for x in range(W):
        d = math.hypot((x - 31.5) / 34.0, (y - 30.5) / 33.0)
        s = max(0.0, (d - 0.80)) * 1.1
        if s > 0 and dith(x, y, min(0.55, s)):
            c.set(x, y, INK)

print(c.stats_text())
view(c)
save("tavern", c, indexed=True)
finish(c)
