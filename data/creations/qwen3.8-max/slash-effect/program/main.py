import math

TAU = math.pi * 2
W = H = 48

c = new_canvas(W, H, name="result")

# ---------------------------------------------------------------- palette
# opaque ramp (shared by both arcs, outside -> inside)
RAMP = [(0.12, "#4a7ad0"), (0.28, "#7fa8f2"), (0.42, "#c3dcff"),
        (0.75, "#ffffff"), (0.88, "#eaf4ff"), (1.01, "#9cc3ff")]
WHITE = "#ffffff"
GLOW1 = "#7fa8f246"
GLOW2 = "#6f9cec26"
GLOW3 = "#5b87d812"


def ramp(v):
    for th, col in RAMP:
        if v <= th:
            return col
    return RAMP[-1][1]


# ---------------------------------------------------------------- geometry
def arc_params(p1, p2, bulge):
    x1, y1 = p1
    x2, y2 = p2
    vx, vy = x2 - x1, y2 - y1
    L = math.hypot(vx, vy)
    ux, uy = vx / L, vy / L
    nx, ny = -uy, ux
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    b = float(bulge)
    s = (b * b - L * L / 4.0) / (2.0 * b)
    cx, cy = mx + s * nx, my + s * ny
    R = abs(b - s)
    a0 = math.atan2(y1 - cy, x1 - cx)
    a1 = math.atan2(y2 - cy, x2 - cx)
    am = math.atan2(my + b * ny - cy, mx + b * nx - cx)
    half = (am - a0 + math.pi) % TAU - math.pi
    return cx, cy, R, a0, a0 + 2.0 * half


def pt_on(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))


def draw_band(cv, prm, ox, oy, box, thickf, colorf, glowf=None, only=None):
    cx, cy, R, a0, a1 = prm
    span = a1 - a0
    x0, y0, x1, y1 = box
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            dx, dy = (x - ox) + 0.5 - cx, (y - oy) + 0.5 - cy
            d = math.hypot(dx, dy)
            a = math.atan2(dy, dx)
            u = ((a - a0) % TAU) / span if span > 0 else ((a0 - a) % TAU) / (-span)
            if u < 0.0 or u > 1.0:
                continue
            t = thickf(u)
            if t <= 0.05:
                continue
            off = d - R
            if abs(off) <= t / 2.0:
                if only == "glow":
                    continue
                col = colorf(u, 0.5 + off / t, x - ox, y - oy)
                if col:
                    cv.set(x, y, col)
            elif glowf is not None and only != "band":
                col = glowf(u, abs(off) - t / 2.0)
                if col:
                    cv.set(x, y, col)


def glow(u, g, lo, hi):
    if u < lo or u > hi:
        return None
    if g <= 0.9:
        return GLOW1
    if g <= 1.9:
        return GLOW2
    if g <= 3.0:
        return GLOW3
    return None


# ================================================================ FRAME 1
OX1, OY1 = 0, 0
f1 = arc_params((7, 31), (17, 16), -3.0)


def f1_thick(u):
    return 4.1 * math.sin(math.pi * u) ** 0.55 * (0.7 + 0.3 * u)


draw_band(c, f1, OX1, OY1, (0, 0, 23, 47), f1_thick, lambda u, v: None,
          glowf=lambda u, g: glow(u, g, 0.12, 0.95), only="glow")
draw_band(c, f1, OX1, OY1, (0, 0, 23, 47), f1_thick, lambda u, v, lx, ly: ramp(v),
          only="band")

for (sx, sy, col) in [(19, 13, WHITE), (20, 16, "#dcecff"), (16, 11, "#eaf4ff"),
                      (21, 12, "#9cc3ff96"), (5, 34, "#9cc3ff78"),
                      (4, 32, "#7fa8f246")]:
    c.set(OX1 + sx, OY1 + sy, col)

# ================================================================ FRAME 2
OX2, OY2 = 24, 0
f2 = arc_params((6, 37), (20, 7), -5.0)
cx2, cy2, R2, a0_2, a1_2 = f2
span2 = a1_2 - a0_2


def f2_thick(u):
    return 7.2 * math.sin(math.pi * u ** 0.85) ** 0.5 * (0.55 + 0.45 * u)


# trailing wash: broad faint sweep hugging the arc (motion blur)
wash = (cx2, cy2, R2 + 0.5, a0_2 - 0.24 * span2, a1_2)


def wash_thick(u):
    return 11.0 * math.sin(math.pi * min(1.0, u * 1.05)) ** 0.7


def wash_col(u, v, lx, ly):
    if ly > 44:
        return None
    core = 1.0 - abs(v - 0.5) * 2.0
    if core > 0.45 and ly <= 40:
        return GLOW2
    return GLOW3


draw_band(c, wash, OX2, OY2, (24, 0, 47, 47), wash_thick, wash_col)

# trailing streaks: thin echoes curling back out of the tail
for (dr, th, body, tip, back) in [(2.0, 3.0, "#9cc3ff96", "#9cc3ff4c", 0.20),
                                  (3.8, 2.2, "#7fa8f278", "#7fa8f23a", 0.28),
                                  (5.6, 1.6, "#6f9cec46", "#6f9cec1e", 0.36)]:
    echo = (cx2, cy2, R2 - dr, a0_2 - back * span2, a0_2 + 0.45 * span2)

    def mk(th=th):
        return lambda u: th * math.sin(math.pi * u) ** 0.6

    def colf(u, v, lx, ly, body=body, tip=tip):
        if ly > 43:
            return None
        if ly > 40:
            return tip
        return body if 0.18 < u < 0.82 else tip

    draw_band(c, echo, OX2, OY2, (24, 0, 47, 47), mk(), colf)

# main arc: glow then band
draw_band(c, f2, OX2, OY2, (24, 0, 47, 47), f2_thick, lambda u, v: None,
          glowf=lambda u, g: glow(u, g, 0.05, 1.0), only="glow")
draw_band(c, f2, OX2, OY2, (24, 0, 47, 47), f2_thick, lambda u, v, lx, ly: ramp(v),
          only="band")

# hot core highlight along the leading half
hi = (cx2, cy2, R2 + 1.2, a0_2 + 0.42 * span2, a1_2 - 0.02 * span2)
draw_band(c, hi, OX2, OY2, (24, 0, 47, 47),
          lambda u: 2.2 * math.sin(math.pi * u) ** 0.5,
          lambda u, v, lx, ly: WHITE)

# comet streak continuing off the tail tip
tx, ty = pt_on(cx2, cy2, R2, a0_2)
tang = math.atan2(ty - (cy2 + R2 * math.sin(a0_2 - 0.01)),
                  tx - (cx2 + R2 * math.cos(a0_2 - 0.01)))
ba = tang + math.pi
AL = [255, 220, 170, 120, 80]
steps = 11
for i in range(steps):
    f = i / float(steps - 1)
    sx = tx + math.cos(ba) * (8.0 * f) - 3.5 * f * f
    sy = ty + math.sin(ba) * (8.0 * f) - 2.0 * f * f + 0.4 * f
    w = 2.8 * (1.0 - f) + 0.5
    binv = min(4, int(f * 5))
    ahex = "" if AL[binv] == 255 else "%02x" % AL[binv]
    for j in range(-3, 4):
        off = j * 0.5
        if abs(off) > w / 2.0:
            continue
        px = int(round(sx + math.cos(ba + math.pi / 2) * off))
        py = int(round(sy + math.sin(ba + math.pi / 2) * off))
        if 0 <= px < 24 and 0 <= py < 48:
            base = WHITE if abs(off) < w / 4.0 else "#b9d6ff"
            c.set(OX2 + px, OY2 + py, base + ahex)

for (sx, sy, col) in [(20, 4, WHITE), (21, 8, "#eaf4ff"), (17, 3, "#dcecff"),
                      (20, 2, "#9cc3ff96"), (15, 5, "#9cc3ff78"),
                      (19, 11, "#7fa8f246"), (21, 5, "#7fa8f23a")]:
    c.set(OX2 + sx, OY2 + sy, col)

# ---------------------------------------------------------------- output
print(c.stats_text())
bg = new_canvas(W, H, background="#2a2f3a", name="bg")
prev = flatten([bg, c], name="prev")
view(prev, scale=8, margin=1)
view(c, scale=8, margin=1)
save("slash_effect", c, indexed=True)
finish(c)
