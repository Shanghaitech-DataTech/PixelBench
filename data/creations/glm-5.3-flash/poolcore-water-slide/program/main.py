import math

c = new_canvas(128, 128, background="#c3e4f0", name="poolcore")

NAMES = {
    "ceil_base": "#7e97a6", "ceil_dark": "#6d8595", "ceil_light": "#94adbc",
    "light_white": "#f7fdff", "light_glow": "#dceef8",
    "wall_base": "#e4f1f7", "wall_grid": "#c6dfe9", "wall_blue": "#b7dae9",
    "wall_blue2": "#9dcbe0", "band": "#8fb9cd", "band_grid": "#7ea9bf",
    "col_light": "#eff7fb", "col_mid": "#d4e8f1", "col_dark": "#b2cfdc",
    "deck_base": "#d9ebf3", "deck_grid": "#b9d6e4", "deck_dark": "#a5c6d8",
    "coping": "#f6fbfd", "coping_dark": "#9ec0d1",
    "wat1": "#c3e4f0", "wat2": "#b1d9ea", "wat3": "#9ecde1",
    "ripple_lt": "#e4f5fb", "ripple_dk": "#88bdd7",
    "slide_body": "#f4f9fc", "slide_hi": "#ffffff", "slide_sh": "#cfe2ec",
    "slide_edge": "#9cbccf", "slide_chan": "#dcebf3",
    "slide_sub": "#cfe7f1", "slide_sub2": "#bfe0ee", "slide_sub3": "#b4d5e4",
    "slide_sub4": "#9cc3d4", "slide_sub5": "#c2dfec",
    "opening": "#33566b", "opening2": "#26455a",
    "ring_y": "#ffd23f", "ring_dk": "#e3a81c", "ring_hi": "#fff0a0",
    "ring_edge": "#c78d12", "skin": "#f3cba4", "skin_sh": "#dba87f",
    "hair": "#4a3126", "hair_hi": "#6d4a34", "suit": "#3f6fa8",
    "refl": "#739cb2",
}
P = {k: c.color(v, name=k) for k, v in NAMES.items()}


def col(n):
    return P[n]


# ----------------------------- ceiling -----------------------------
c.rect(0, 0, 128, 12, col("ceil_base"))
for y in (4, 8):
    c.line(0, y, 127, y, col("ceil_dark"))
for x in range(0, 128, 8):
    c.line(x, 0, x, 11, col("ceil_dark"))
for lx in (14, 52, 90):
    c.rect(lx - 2, 0, 28, 12, col("ceil_light"))
    c.rect(lx - 1, 1, 26, 9, col("ceil_dark"))
    c.rect(lx, 2, 24, 7, col("light_white"))
    c.rect(lx, 7, 24, 2, col("light_glow"))
c.line(0, 11, 127, 11, col("ceil_dark"))

# ----------------------------- back wall -----------------------------
c.rect(0, 12, 128, 36, col("wall_base"))
for ty in range(12, 48, 4):
    for tx in range(0, 128, 4):
        r = ((tx // 4) * 7 + (ty // 4) * 13) % 11
        if r == 3:
            c.rect(tx, ty, 4, 4, col("wall_blue"))
        elif r == 7:
            c.rect(tx, ty, 4, 4, col("wall_blue2"))
for y in range(12, 48, 4):
    c.line(0, y, 127, y, col("wall_grid"))
for x in range(0, 128, 4):
    c.line(x, 12, x, 47, col("wall_grid"))
c.rect(0, 40, 128, 8, col("band"))
for y in range(40, 48, 4):
    c.line(0, y, 127, y, col("band_grid"))
for x in range(0, 128, 4):
    c.line(x, 40, x, 47, col("band_grid"))

# doorway
c.rect(30, 26, 14, 22, col("opening2"))
c.rect(29, 25, 16, 1, col("opening"))
c.rect(29, 26, 1, 22, col("opening"))
c.rect(43, 26, 1, 22, col("opening"))
c.rect(30, 26, 14, 1, col("opening"))

# sign
c.rect(63, 14, 28, 13, col("opening"))
c.rect(65, 16, 24, 9, col("opening2"))
c.text(66, 17, "POOL", col("coping"), font="5x7")

# slide opening in wall
c.rect(114, 12, 14, 12, col("opening2"))
c.rect(115, 12, 13, 11, col("opening"))
c.rect(114, 12, 1, 12, col("opening"))
c.rect(114, 23, 14, 1, col("opening"))


# ----------------------------- deck -----------------------------
c.rect(0, 48, 128, 12, col("deck_base"))
c.line(0, 48, 127, 48, col("deck_dark"))
for y in (51, 54, 57):
    c.line(0, y, 127, y, col("deck_grid"))
for xb in range(0, 129, 16):
    xf = 64 + (xb - 64) * 1.5
    c.line(xb, 49, int(round(xf)), 59, col("deck_grid"))

# ----------------------------- columns -----------------------------
def draw_column(cx, top_y, bot_y, w=10):
    x0 = cx - w // 2
    c.rect(x0, top_y, w, bot_y - top_y, col("col_mid"))
    c.rect(x0 + 1, top_y, 2, bot_y - top_y, col("col_light"))
    c.rect(x0 + w - 3, top_y, 2, bot_y - top_y, col("col_dark"))
    c.line(x0, top_y, x0, bot_y - 1, col("col_dark"))
    c.line(x0 + w - 1, top_y, x0 + w - 1, bot_y - 1, col("col_dark"))
    for y in range(top_y + 3, bot_y - 2, 4):
        c.line(x0 + 1, y, x0 + w - 2, y, col("col_dark"))
    c.rect(x0 - 1, top_y, w + 2, 3, col("col_light"))
    c.line(x0 - 1, top_y, x0 + w, top_y, col("col_dark"))
    c.line(x0 - 1, top_y + 2, x0 + w, top_y + 2, col("col_dark"))
    c.rect(x0 - 1, bot_y - 3, w + 2, 3, col("col_light"))
    c.line(x0 - 1, bot_y - 3, x0 + w, bot_y - 3, col("col_dark"))
    c.line(x0 - 1, bot_y - 1, x0 + w, bot_y - 1, col("col_dark"))


draw_column(20, 12, 61)
draw_column(58, 12, 61)
draw_column(100, 24, 61)

# ----------------------------- copings -----------------------------
c.rect(0, 60, 128, 3, col("coping"))
c.line(0, 62, 127, 62, col("coping_dark"))
c.rect(0, 118, 128, 3, col("coping"))
c.line(0, 120, 127, 120, col("coping_dark"))
c.rect(0, 121, 128, 7, col("deck_base"))
c.line(0, 121, 127, 121, col("deck_dark"))
c.line(0, 124, 127, 124, col("deck_grid"))
for xb in range(-24, 153, 24):
    xf = 64 + (xb - 64) * 1.45
    c.line(xb, 122, int(round(xf)), 127, col("deck_grid"))

# ----------------------------- water -----------------------------
c.rect(0, 63, 128, 55, col("wat1"))
for x in range(128):
    yb = 78 + int(round(1.8 * math.sin(2 * math.pi * x / 26.0)))
    c.line(x, yb, x, 97, col("wat2"))
    yb2 = 98 + int(round(1.8 * math.sin(2 * math.pi * x / 22.0 + 2.0)))
    c.line(x, yb2, x, 117, col("wat3"))
c.line(0, 63, 127, 63, col("ripple_dk"))


# ----------------------------- reflections -----------------------------
def vstreak(cx, y0, y1, colour, width=2, amp=1.4, period=7.0, phase=0.0, duty=2, of=3):
    for y in range(y0, y1 + 1):
        if (y % of) >= duty:
            continue
        x = cx + int(round(amp * math.sin(2 * math.pi * y / period + phase)))
        for dx in range(width):
            c.set(x + dx, y, colour)


vstreak(19, 64, 92, col("col_mid"), 3, 1.6, 8.0, 0.4)
vstreak(22, 64, 88, col("col_dark"), 1, 1.6, 8.0, 0.4)
vstreak(57, 64, 86, col("col_mid"), 3, 1.4, 7.0, 2.1)
vstreak(60, 64, 82, col("col_dark"), 1, 1.4, 7.0, 2.1)
vstreak(99, 64, 90, col("col_mid"), 3, 1.6, 8.0, 5.0)
vstreak(102, 64, 86, col("col_dark"), 1, 1.6, 8.0, 5.0)
for lx, ph in ((25, 0.9), (63, 2.6), (101, 4.2)):
    vstreak(lx, 64, 80, col("light_white"), 2, 1.2, 6.0, ph, duty=1, of=2)

# girl + ring reflection (broken by ripples later)
for dy, w2, cl in ((2, 10, "ring_y"), (3, 8, "ring_dk"), (5, 9, "ring_y"),
                   (7, 7, "ring_dk"), (9, 8, "ring_y"), (11, 5, "ring_dk")):
    y = 99 + dy
    x = 64 + int(round(1.6 * math.sin(y / 2.7)))
    c.rect(x - w2 // 2, y, w2, 1, col(cl))
c.rect(62, 100, 4, 1, col("hair"))
c.rect(63, 102, 3, 1, col("skin_sh"))
# doorway reflection
c.rect(7, 64, 13, 7, col("refl"))
for yy in range(64, 71):
    xoff = int(round(1.5 * math.sin(yy / 2.2)))
    c.rect(7 + xoff, yy, 11, 1, col("opening2"))
vstreak(12, 71, 82, col("refl"), 1, 1.2, 7.0, 0.5, duty=1, of=3)
# ladder reflection (below the ladder rails)
vstreak(35, 78, 92, col("refl"), 1, 1.2, 6.0, 0.0, duty=1, of=3)
vstreak(40, 78, 92, col("refl"), 1, 1.2, 6.0, 0.6, duty=1, of=3)


# ----------------------------- ripple lines -----------------------------
def wavy_h(y0, x0, x1, colour, period=11.0, amp=1.0, phase=0.0, duty=None, skip=5):
    for x in range(x0, x1 + 1):
        if duty is not None and (x % skip) >= duty:
            continue
        y = y0 + int(round(amp * math.sin(2 * math.pi * x / period + phase)))
        if 64 <= y <= 117:
            c.set(x, y, colour)


wavy_h(67, 0, 127, col("ripple_lt"), 11, 1, 0.3)
wavy_h(71, 0, 127, col("ripple_dk"), 13, 1, 1.8, duty=3)
wavy_h(75, 0, 127, col("ripple_lt"), 9, 1, 4.0)
wavy_h(80, 0, 127, col("ripple_lt"), 12, 1, 2.2)
wavy_h(85, 0, 127, col("ripple_dk"), 10, 1, 0.7, duty=3)
wavy_h(90, 0, 127, col("ripple_lt"), 14, 1, 3.1)
wavy_h(95, 0, 127, col("ripple_lt"), 11, 1, 5.0, duty=3)
wavy_h(101, 0, 127, col("ripple_lt"), 13, 1, 1.4)
wavy_h(107, 0, 127, col("ripple_dk"), 12, 1, 2.9, duty=3)
wavy_h(112, 0, 127, col("ripple_lt"), 15, 1, 0.2)

# ----------------------------- pool ladder -----------------------------
c.line(35, 62, 35, 76, col("slide_edge"))
c.line(40, 62, 40, 76, col("slide_edge"))
for ry in range(63, 76, 3):
    c.line(36, ry, 39, ry, col("slide_edge"))
c.set(34, 62, col("slide_hi"))
c.set(41, 62, col("slide_hi"))
c.rect(34, 74, 2, 2, col("slide_edge"))
c.rect(40, 74, 2, 2, col("slide_edge"))
wavy_h(70, 32, 44, col("ripple_lt"), 8, 1, 1.0, duty=4)


# ----------------------------- slide geometry -----------------------------
def sample_seg(seg, n=36, skip_first=False):
    p0, p1, p2, p3 = seg
    out = []
    for i in range(n + 1):
        if skip_first and i == 0:
            continue
        t = i / n
        mt = 1 - t
        x = mt ** 3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t ** 3 * p3[0]
        y = mt ** 3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t ** 3 * p3[1]
        dx = 3 * mt * mt * (p1[0] - p0[0]) + 6 * mt * t * (p2[0] - p1[0]) + 3 * t * t * (p3[0] - p2[0])
        dy = 3 * mt * mt * (p1[1] - p0[1]) + 6 * mt * t * (p2[1] - p1[1]) + 3 * t * t * (p3[1] - p2[1])
        out.append((x, y, dx, dy))
    return out


SA = ((127, 18), (106, 18), (94, 23), (90, 34))
SB = ((90, 34), (86, 46), (92, 54), (78, 66))
S = sample_seg(SA) + sample_seg(SB, skip_first=True)

top_pts, bot_pts, inn_hi, inn_sh, mid_pts = [], [], [], [], []
for (x, y, dx, dy) in S:
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    top_pts.append((x + nx * 3.5, y + ny * 3.5))
    bot_pts.append((x - nx * 3.5, y - ny * 3.5))
    inn_hi.append((x + nx * 1.8, y + ny * 1.8))
    inn_sh.append((x - nx * 1.8, y - ny * 1.8))
    mid_pts.append((x, y))

# slide reflection on the water (dashed, squashed mirror)
for i, (x, y, dx, dy) in enumerate(S):
    if y >= 61:
        continue
    yi = int(round(63 + (63 - y) * 0.55))
    if not (64 <= yi <= 116) or i % 3 == 2:
        continue
    xi = int(round(x + 1.6 * math.sin(yi / 2.8)))
    cl = col("slide_body") if i % 2 == 0 else col("slide_sh")
    for dx2 in range(3):
        c.set(xi - 1 + dx2, yi, cl)


def stroke(pts, colour, width=1):
    for (x, y) in pts:
        xi, yi = int(round(x)), int(round(y))
        for dx in range(width):
            c.set(xi + dx, yi, colour)


# ----------------------------- the slide -----------------------------
c.poly([(int(round(x)), int(round(y))) for (x, y) in top_pts + bot_pts[::-1]],
       col("slide_body"), fill=True)
for i in range(4, len(S) - 2, 6):
    c.line(int(round(top_pts[i][0])), int(round(top_pts[i][1])),
           int(round(bot_pts[i][0])), int(round(bot_pts[i][1])), col("slide_sh"))
stroke(mid_pts, col("slide_chan"), 2)
stroke(inn_sh, col("slide_sh"))
stroke(inn_hi, col("slide_hi"))
stroke(top_pts, col("slide_edge"))
stroke(bot_pts, col("slide_edge"))

# submerged part shifts blue (crystal clear water)
sub_map = {P["slide_body"]: P["slide_sub"], P["slide_hi"]: P["slide_sub2"],
           P["slide_sh"]: P["slide_sub3"], P["slide_edge"]: P["slide_sub4"],
           P["slide_chan"]: P["slide_sub5"]}
for y in range(64, 76):
    for x in range(66, 100):
        idx = c.get(x, y)
        if idx in sub_map:
            c.set(x, y, sub_map[idx])
wavy_h(68, 70, 92, col("ripple_lt"), 9, 1, 1.0)
wavy_h(72, 70, 92, col("ripple_dk"), 11, 1, 2.0, duty=3)

# splash where the slide meets the water
c.rect(79, 63, 6, 3, col("slide_hi"))
c.set(78, 62, col("slide_edge"))
c.set(82, 61, col("slide_edge"))
c.set(85, 62, col("slide_edge"))
c.set(77, 64, col("slide_hi"))
c.set(86, 64, col("slide_hi"))


# ----------------------------- ripple arcs -----------------------------
def arc_ellipse(cx, cy, rx, ry, colour, a0=-20, a1=200, step=4, dash=3):
    i = 0
    for adeg in range(a0, a1 + 1, step):
        i += 1
        if i % dash == 0:
            continue
        ar = math.radians(adeg)
        x = int(round(cx + rx * math.cos(ar)))
        y = int(round(cy + ry * math.sin(ar)))
        if 64 <= y <= 117 and 0 <= x <= 127:
            c.set(x, y, colour)


arc_ellipse(81, 66, 6, 2.6, col("ripple_lt"), -180, 179, 4, 4)
arc_ellipse(81, 66, 10, 4, col("ripple_dk"), -180, 179, 4, 4)
arc_ellipse(81, 66, 14, 5.5, col("ripple_lt"), -180, 179, 4, 4)
arc_ellipse(81, 66, 18, 7, col("ripple_lt"), -180, 179, 4, 6)

# ----------------------------- girl in the ring -----------------------------
CX, CY = 64, 93


def ring_half(a0, a1, colour):
    for adeg in range(a0, a1 + 1, 2):
        ar = math.radians(adeg)
        ox, oy = CX + 9 * math.cos(ar), CY + 5 * math.sin(ar)
        ix, iy = CX + 5 * math.cos(ar), CY + 2 * math.sin(ar)
        c.line(int(round(ix)), int(round(iy)), int(round(ox)), int(round(oy)), colour)


def ring_arc(a0, a1, rx, ry, colour):
    for adeg in range(a0, a1 + 1, 3):
        ar = math.radians(adeg)
        c.set(int(round(CX + rx * math.cos(ar))), int(round(CY + ry * math.sin(ar))), colour)


ring_half(180, 360, col("ring_y"))
ring_arc(180, 360, 9, 5, col("ring_edge"))
ring_arc(180, 360, 5, 2, col("ring_dk"))
for adeg in range(205, 336, 10):
    ar = math.radians(adeg)
    c.set(int(round(CX + 9 * math.cos(ar))), int(round(CY + 5 * math.sin(ar))), col("ring_hi"))

# girl seen from behind
c.circle(64, 84, 3, col("hair"))
c.rect(62, 87, 5, 2, col("hair"))
c.rect(60, 89, 9, 3, col("skin"))
c.rect(60, 90, 9, 1, col("suit"))
c.rect(62, 92, 5, 1, col("skin_sh"))
c.set(62, 82, col("hair_hi"))
c.set(63, 81, col("hair_hi"))
c.rect(57, 90, 2, 2, col("skin"))
c.rect(69, 90, 2, 2, col("skin"))

ring_half(0, 180, col("ring_y"))
ring_arc(0, 180, 9, 5, col("ring_edge"))
ring_arc(0, 180, 5, 2, col("ring_dk"))

# expanding rings around her
arc_ellipse(64, 94, 12, 6, col("ripple_lt"), -20, 200, 4, 4)
arc_ellipse(64, 94, 16, 8, col("ripple_lt"), -20, 200, 4, 5)
arc_ellipse(64, 94, 20, 10, col("ripple_dk"), -20, 200, 4, 7)

# caustic sparkles
for (sx, sy) in ((30, 72), (45, 77), (90, 84), (110, 96), (20, 100),
                 (52, 110), (100, 112), (38, 92), (118, 74), (8, 86)):
    c.set(sx, sy, col("ripple_lt"))

# soft vignette in the corners
c.dither(0, 0, 24, 5, [col("ceil_base"), col("ceil_dark")], pattern="bayer4")
c.dither(104, 0, 24, 5, [col("ceil_base"), col("ceil_dark")], pattern="bayer4")

print(c.stats_text())
print(c.matrix_text(region=(44, 74, 92, 106)))
finish(c)
