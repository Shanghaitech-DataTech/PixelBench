import math

W = H = 128
c = new_canvas(W, H, background="#eaf3f9", name="poolcore")

# ---------------- palette ----------------
P = {
    "white":      "#ffffff",
    "glow":       "#f8fcff",
    "tile_w":     "#f1f7fb",
    "tile_w2":    "#e6eff6",
    "tile_b":     "#cde2ef",
    "grid":       "#b6d3e4",
    "grid_d":     "#9dc3da",
    "ceil":       "#edf4f9",
    "ceil_s":     "#dde9f2",
    "wallL":      "#e2edf5",
    "wallR":      "#eaf2f8",
    "back":       "#edf4f9",
    "deck":       "#e3eef5",
    "deck_s":     "#d2e3ee",
    "w1":         "#c4e5f3",
    "w2":         "#a8d8ee",
    "w3":         "#8ac7e5",
    "w4":         "#6fb5da",
    "w5":         "#58a4cd",
    "rip":        "#ddf2fb",
    "rip2":       "#f0fbff",
    "under":      "#93c9e3",
    "sl_w":       "#fbfeff",
    "sl_s":       "#d8e8f2",
    "sl_d":       "#9cc0d7",
    "sl_e":       "#7ba2bd",
    "sl_u":       "#8bb0c9",
    "shade":      "#d6e4ee",
    "y1":         "#fff0a2",
    "y2":         "#f8d94c",
    "y3":         "#dca92b",
    "hair":       "#5b4331",
    "hair_d":     "#3c2c20",
    "skin":       "#f0c49c",
    "skin_s":     "#d7a177",
}
for k, v in P.items():
    c.color(v, k)

VX, VY = 64.0, 52.0
BT, BB = 30, 63          # back wall top / bottom
BL, BR = 34, 93          # back wall left / right


def lerp(a, b, t):
    return a + (b - a) * t


# ---------------- big planes ----------------
c.poly([(0, 0), (127, 0), (BR, BT), (BL, BT)], "ceil")                 # ceiling
c.poly([(0, 0), (BL, BT), (BL, BB), (0, 127)], "wallL")                # left wall
c.poly([(127, 0), (BR, BT), (BR, BB), (127, 127)], "wallR")            # right wall
c.poly([(0, 127), (BL, BB), (BR, BB), (127, 127)], "deck")             # floor
c.rect(BL, BT, BR - BL + 1, BB - BT + 1, "back")                       # back wall


# ---------------- side walls : mosaic grid ----------------
def wall(mir):
    def X(x):
        return 127 - x if mir else x
    dist = 63.5 if mir else 64.0
    base = "wallR" if mir else "wallL"
    # tile blocks (sparse pale-blue mosaic accents)
    xs = [0, 7, 14, 20, 25, 29, 32, 34]
    y0s = list(range(-30, 150, 12))
    for i in range(len(xs) - 1):
        for j in range(len(y0s) - 1):
            if (i + j) % 3:
                continue
            for xv in range(xs[i], xs[i + 1] + 1):
                tt = xv / dist
                ya = lerp(y0s[j], VY, tt)
                yb = lerp(y0s[j + 1], VY, tt)
                top = 30 * xv / 34.0
                bot = 127 - 64 * xv / 34.0
                for y in range(int(max(ya, top)), int(min(yb, bot)) + 1):
                    c.set(X(xv), y, "tile_b")
    # vertical grout lines
    for xv in xs:
        top = 30 * xv / 34.0
        bot = 127 - 64 * xv / 34.0
        for y in range(int(math.ceil(top)), int(bot) + 1):
            c.set(X(xv), y, "grid")
    # grout lines running to the vanishing point
    for y0 in y0s:
        for xv in range(0, 35):
            tt = xv / dist
            y = lerp(y0, VY, tt)
            top = 30 * xv / 34.0
            bot = 127 - 64 * xv / 34.0
            if top <= y <= bot:
                c.set(X(xv), int(round(y)), "grid")


wall(False)
wall(True)


# ---------------- ceiling grid + fluorescent lights ----------------
def ceil_span(y):
    t = (BT - y) / float(BT)
    return 34 - 34 * t, 93 + 34 * t


for xb in range(-40, 170, 14):
    for y in range(0, BT + 1):
        xl, xr = ceil_span(y)
        x = VX + (xb - VX) * (y - VY) / (0 - VY)
        if xl <= x <= xr:
            c.set(int(round(x)), y, "ceil_s")
for y in [29, 26, 22, 16, 8, 0]:
    xl, xr = ceil_span(y)
    for x in range(int(xl), int(xr) + 1):
        c.set(x, y, "ceil_s")

# light panels (back to front, growing)
panels = [(29, 1, 0.34), (26, 1, 0.31), (22, 2, 0.28), (16, 2, 0.25), (8, 3, 0.22), (1, 3, 0.19)]
for (y, th, frac) in panels:
    xl, xr = ceil_span(y)
    span = xr - xl
    a, b = int(xl + span * frac), int(xr - span * frac)
    for yy in range(y - th, y + 1):
        if 0 <= yy <= BT:
            for x in range(a, b + 1):
                c.set(x, yy, "white")
    for yy in (y - th - 1, y + 1):
        if 0 <= yy <= BT:
            for x in range(a - 1, b + 2):
                c.set(x, yy, "glow")


# ---------------- back wall mosaic ----------------
xs = list(range(BL, BR + 2, 6))
ys = list(range(BT, BB + 2, 6))
for i in range(len(xs) - 1):
    for j in range(len(ys) - 1):
        if (i + j) % 3 == 0:
            c.rect(xs[i], ys[j], min(xs[i + 1], BR + 1) - xs[i],
                   min(ys[j + 1], BB + 1) - ys[j], "tile_b")
        elif (i * 2 + j) % 5 == 0:
            c.rect(xs[i], ys[j], min(xs[i + 1], BR + 1) - xs[i],
                   min(ys[j + 1], BB + 1) - ys[j], "tile_w2")
for x in xs:
    if x <= BR:
        c.line(x, BT, x, BB, "grid")
for y in ys:
    if y <= BB:
        c.line(BL, y, BR, y, "grid")
c.line(BL, BB, BR, BB, "grid_d")
c.line(BL, BB - 1, BR, BB - 1, "tile_w")


# ---------------- floor grid (deck) ----------------
def floor_span(y):
    t = (y - BB) / float(127 - BB)
    return 34 - 34 * t, 93 + 34 * t


for xb in range(-60, 190, 13):
    for y in range(BB, 128):
        xl, xr = floor_span(y)
        x = VX + (xb - VX) * (y - VY) / (127.0 - VY)
        if xl <= x <= xr:
            c.set(int(round(x)), y, "deck_s")
fy = BB + 1.0
step = 1.3
while fy < 128:
    y = int(fy)
    xl, xr = floor_span(y)
    for x in range(int(xl), int(xr) + 1):
        c.set(x, y, "deck_s")
    fy += step
    step *= 1.33


# ---------------- tiled columns ----------------
def column(x0, x1, ytop, ybot):
    c.rect(x0, ytop, x1 - x0 + 1, ybot - ytop + 1, "tile_w")
    c.rect(x1 - 1, ytop, 2, ybot - ytop + 1, "tile_w2")
    c.line(x1, ytop, x1, ybot, "grid_d")
    c.line(x0, ytop, x0, ybot, "grid")
    gy = ytop
    k = 0
    while gy <= ybot:
        c.line(x0, int(gy), x1, int(gy), "grid")
        if k % 2 == 0:
            c.rect(x0 + 1, int(gy) + 1, max(1, (x1 - x0) // 2), 2, "tile_b")
        gy += 5
        k += 1
    for xm in range(x0 + 3, x1, 4):
        c.line(xm, ytop, xm, ybot, "grid")


column(38, 43, BT, 68)
column(84, 89, BT, 68)
column(17, 28, 6, 88)
column(101, 110, 14, 80)


# ---------------- pool water ----------------
def water_span(y):
    if y < 70 or y > 127:
        return None
    t = (y - 70) / 57.0
    return lerp(50, 6, t), lerp(77, 121, t)


bands = ["w1", "w2", "w3", "w4", "w5"]
for y in range(70, 128):
    xl, xr = water_span(y)
    t = (y - 70) / 57.0
    f = (t ** 0.85) * 4.2
    i = int(f)
    frac = f - i
    for x in range(int(math.ceil(xl)), int(xr) + 1):
        col = bands[min(i, 4)]
        if frac > 0.5 and (x + y) % 2 == 0:
            col = bands[min(i + 1, 4)]
        c.set(x, y, col)

# faint tile grid under the water
for xb in range(-50, 180, 15):
    for y in range(70, 128):
        xl, xr = water_span(y)
        x = VX + (xb - VX) * (y - VY) / (127.0 - VY) + 0.9 * math.sin(y / 3.4)
        if xl + 1 <= x <= xr - 1 and (y % 3):
            c.set(int(round(x)), y, "under")

# ripples
ry = 71.0
step = 1.5
k = 0
while ry < 128:
    y = int(ry)
    xl, xr = water_span(y)
    amp = 0.4 + (y - 70) * 0.07
    per = 5.0 + (y - 70) * 0.25
    col = "rip" if k % 2 else "rip2"
    for x in range(int(math.ceil(xl)), int(xr) + 1):
        yy = int(round(y + amp * math.sin(x / per + k * 1.7)))
        if 70 <= yy <= 127:
            sp = water_span(yy)
            if sp and sp[0] <= x <= sp[1]:
                c.set(x, yy, col)
    ry += step
    step *= 1.17
    k += 1

# reflections of the ceiling lights, straight down the middle
for (yy, th, wf) in [(72, 1, 5), (75, 1, 7), (79, 1, 9), (84, 2, 12), (91, 2, 15), (100, 2, 19), (112, 3, 24)]:
    for dy in range(th):
        y = yy + dy
        sp = water_span(y)
        if not sp:
            continue
        cx = VX + 1.0 * math.sin(y / 5.0)
        for x in range(int(cx - wf), int(cx + wf) + 1):
            if sp[0] <= x <= sp[1] and (x + y * 2) % 3:
                c.set(x, y, "rip2" if dy == 0 else "rip")

# column reflections
for cx0 in (40.5, 86.5):
    for y in range(70, 92):
        sp = water_span(y)
        x = cx0 + 0.9 * math.sin(y / 2.6)
        if sp and sp[0] + 1 <= x <= sp[1] - 1 and y % 4 != 3:
            c.set(int(round(x)), y, "rip")

# pool rim / coping
for y in range(70, 128):
    xl, xr = water_span(y)
    for d in (2, 3):
        c.set(int(round(xl)) - d, y, "white")
        c.set(int(round(xr)) + d, y, "white")
    c.set(int(round(xl)) - 1, y, "glow")
    c.set(int(round(xr)) + 1, y, "glow")
    c.set(int(round(xl)), y, "w2")
    c.set(int(round(xr)), y, "w2")
for x in range(47, 81):
    c.set(x, 68, "white")
    c.set(x, 69, "glow")
c.line(50, 70, 77, 70, "w1")


# ---------------- water slide ----------------
def bez(p0, p1, p2, p3, t):
    m = 1 - t
    return (m ** 3 * p0[0] + 3 * m * m * t * p1[0] + 3 * m * t * t * p2[0] + t ** 3 * p3[0],
            m ** 3 * p0[1] + 3 * m * m * t * p1[1] + 3 * m * t * t * p2[1] + t ** 3 * p3[1])


P0, P1, P2, P3 = (103, 24), (124, 46), (113, 79), (79, 91)
N = 90
pts = [bez(P0, P1, P2, P3, i / float(N)) for i in range(N + 1)]
nrm = []
for i in range(N + 1):
    a = pts[max(i - 1, 0)]
    b = pts[min(i + 1, N)]
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy) or 1.0
    nrm.append((-dy / L, dx / L))


def hw(t):
    return 3.0 + 5.4 * t


def ribbon(f_in, f_out, col):
    left = []
    right = []
    for i in range(N + 1):
        t = i / float(N)
        w = hw(t)
        nx, ny = nrm[i]
        x, y = pts[i]
        left.append((x + nx * w * f_in, y + ny * w * f_in))
        right.append((x + nx * w * f_out, y + ny * w * f_out))
    c.poly(left + right[::-1], col)


# supports under the flume
for (sx, y0, y1, wd) in [(120, 54, 72, 2), (115, 70, 80, 2), (104, 82, 90, 2)]:
    c.rect(sx, y0, wd, y1 - y0, "sl_d")
    c.rect(sx, y1 - 2, wd, 2, "sl_e")

ribbon(-1.25, 1.25, "shade")   # soft contact shadow against the wall
ribbon(-1.0, 1.0, "sl_w")      # body of the tube
ribbon(0.00, 1.0, "sl_s")      # shaded outer flank
ribbon(0.48, 1.0, "sl_d")
ribbon(0.82, 1.0, "sl_u")
ribbon(-1.0, -0.66, "glow")    # inner lit lip
ribbon(-0.35, 0.18, "white")   # highlight along the trough

# rims
for i in range(N + 1):
    t = i / float(N)
    w = hw(t)
    nx, ny = nrm[i]
    x, y = pts[i]
    c.set(int(round(x + nx * w)), int(round(y + ny * w)), "sl_e")
    c.set(int(round(x - nx * w)), int(round(y - ny * w)), "sl_d")

# reflection of the slide and its support in the water
for i in range(N + 1):
    t = i / float(N)
    w = hw(t)
    nx, ny = nrm[i]
    x, y = pts[i]
    for e in (-0.6, 0.0, 0.6):
        rx = x + nx * w * e + 0.8 * math.sin(y / 3.0)
        ry = 183 - (y + ny * w * e)
        if ry > 92:
            sp = water_span(int(ry))
            if sp and sp[0] + 1 <= rx <= sp[1] - 1 and int(ry) % 4 != 3:
                c.set(int(round(rx)), int(round(ry)), "rip")

# ribbing across the chute
for i in range(4, N - 2, 7):
    t = i / float(N)
    w = hw(t)
    nx, ny = nrm[i]
    x, y = pts[i]
    c.line(int(round(x - nx * w * 0.95)), int(round(y - ny * w * 0.95)),
           int(round(x + nx * w * 0.95)), int(round(y + ny * w * 0.95)), "sl_s")

# chute mouth at the top
c.ellipse(103, 24, 4, 2, "sl_d")
c.ellipse(103, 23, 4, 2, "sl_s")
c.ellipse(103, 22, 4, 2, "sl_w", fill=False)

# splash where the slide meets the water
c.ellipse(79, 92, 8, 3, "glow", fill=False)
c.ellipse(79, 92, 5, 2, "white")
c.ellipse(79, 95, 9, 3, "rip", fill=False)
for (dx, dy) in [(-11, 93), (-7, 96), (10, 94), (7, 97), (0, 97), (13, 91), (-13, 90)]:
    c.set(79 + dx, dy, "rip2")


# ---------------- girl in the yellow swim ring ----------------
gx, gy = 60, 100
# water disturbance around the ring
c.ellipse(gx, gy + 3, 14, 6, "w5", fill=False)
c.ellipse(gx, gy + 1, 16, 7, "rip", fill=False)
c.ellipse(gx + 1, gy + 5, 11, 3, "w5")

# ring (full donut), then figure, then the near arc back over her
c.ellipse(gx, gy, 11, 6, "y2")
c.ellipse(gx, gy - 1, 11, 5, "y1")
c.ellipse(gx, gy + 3, 11, 3, "y3")
c.ellipse(gx, gy, 5, 3, "skin_s")          # inner hole, in shadow

# torso seen from behind
c.poly([(gx - 5, gy + 1), (gx - 4, gy - 6), (gx - 2, gy - 8),
        (gx + 2, gy - 8), (gx + 4, gy - 6), (gx + 5, gy + 1)], "skin")
c.poly([(gx + 1, gy - 8), (gx + 4, gy - 6), (gx + 5, gy + 1), (gx + 2, gy + 1)], "skin_s")
c.set(gx, gy - 4, "skin_s")
c.set(gx, gy - 2, "skin_s")

# head and hair
c.circle(gx, gy - 11, 3, "hair")
c.ellipse(gx, gy - 9, 4, 3, "hair")
c.ellipse(gx + 2, gy - 9, 2, 3, "hair_d")
c.ellipse(gx, gy - 13, 3, 1, "hair")
c.set(gx - 2, gy - 14, "hair_d")
c.set(gx + 1, gy - 14, "hair_d")
c.set(gx - 3, gy - 7, "hair_d")
c.set(gx + 3, gy - 7, "hair_d")

# near arc of the ring passing in front of her
c.ellipse(gx, gy + 2, 11, 4, "y2")
c.ellipse(gx, gy + 4, 11, 2, "y3")
c.ellipse(gx, gy + 1, 7, 2, "y1", fill=False)

# arms draped over the sides of the ring
c.line(gx - 9, gy - 2, gx - 5, gy - 5, "skin")
c.line(gx + 5, gy - 5, gx + 9, gy - 2, "skin_s")
c.set(gx - 10, gy - 1, "skin_s")
c.set(gx + 10, gy - 1, "skin_s")

# ring highlights and valve
for sx in (-9, -5, 5, 9):
    c.set(gx + sx, gy - 4 + abs(sx) // 7, "y1")
    c.set(gx + sx, gy + 4 - abs(sx) // 7, "y3")
c.set(gx - 7, gy - 3, "white")
c.set(gx - 8, gy - 2, "glow")
c.set(gx + 8, gy + 2, "y3")

# ---------------- pool ladder on the left deck ----------------
c.path("M 31 86 C 31 78 33 76 36 76 C 39 76 40 78 40 84", "sl_e", fill=False)
c.path("M 32 86 C 32 79 34 77 36 77 C 38 77 39 79 39 84", "white", fill=False)
for (ry, rx0, rx1) in [(80, 32, 39), (83, 31, 40)]:
    c.line(rx0, ry, rx1, ry, "sl_d")
c.set(31, 87, "sl_e")
c.set(40, 85, "sl_e")

view(c)
print(c.stats_text())
finish(c)
