import math

W, H = 64, 64
c = new_canvas(W, H)

# Distant hill crest (top of the view, where the village sits)
crest = c.color((86, 94, 52), "crest")
c.rect(0, 0, W, H, crest, fill=True)
c.rect(0, 0, W, 2, c.color((56, 62, 34), "crest_top"), fill=True)

# Terrace contour bands: top = distant/pale, bottom = near/rich amber.
bases = [8, 13, 18, 23, 28, 33, 37, 41, 45, 49, 53, 58, 64]
phase = 0.5

def S(x):
    v = (math.sin(0.115 * x + phase)
         + 0.55 * math.sin(0.26 * x + 1.2 + 1.4 * phase)
         + 0.25 * math.sin(0.34 * x + 0.6 + 0.6 * phase))
    return v / 1.8

def amp(b):
    return 1.6 + 0.38 * b

def by(b, x):
    return bases[b] + amp(b) * S(x)

def ry(v):
    return max(0, min(H - 1, int(round(v))))

def mix(c1, c2, t):
    return tuple(int(c1[i] * (1 - t) + c2[i] * t + 0.5) for i in range(3))

terrace_rgb = [
    (239, 227, 163),
    (234, 212, 146),
    (228, 196, 125),
    (221, 179, 104),
    (214, 162, 83),
    (207, 145, 67),
    (199, 129, 53),
    (191, 114, 44),
    (181, 99, 36),
    (171, 84, 29),
    (159, 70, 23),
    (146, 58, 18),
]

# Fill each terrace band, then add dotted crop rows inside it.
for i in range(12):
    base = terrace_rgb[i]
    col = c.color(base, f"t{i}")
    hi = c.color(mix(base, (255, 242, 190), 0.45), f"t{i}_hi")
    sh = c.color(mix(base, (70, 40, 12), 0.35), f"t{i}_sh")

    top, bot = i, i + 1
    pts = []
    for x in range(W):
        pts.append((x, ry(by(top, x))))
    for x in range(W - 1, -1, -1):
        pts.append((x, ry(by(bot, x) + 1)))
    c.poly(pts, col, fill=True)

    for frac, tcol in ((0.30, hi), (0.66, sh)):
        for x in range(0, W, 3):
            y = ry(by(top, x) + frac * (by(bot, x) - by(top, x)))
            c.set(x, y, tcol)

# Ridge lines (the narrow dikes between paddies).
ridge = c.color((64, 36, 13), "ridge")
for b in range(0, 12):
    for x in range(W):
        y = ry(by(b, x))
        c.set(x, y, ridge)

# Simple distant village houses on the crest.
def house(x, y, w=3, h=3, orient='h'):
    roof = c.color((158, 86, 48), "roof")
    roof_hi = c.color((198, 120, 70), "roof_hi")
    roof_dk = c.color((92, 48, 26), "roof_dk")
    c.rect(x, y, w, h, roof, fill=True)
    c.rect(x, y, w, h, roof_dk, fill=False)
    if orient == 'h':
        c.line(x + 1, y + h // 2, x + w - 2, y + h // 2, roof_dk)
        c.line(x, y, x + w - 1, y, roof_hi)
    else:
        c.line(x + w // 2, y + 1, x + w // 2, y + h - 2, roof_dk)
        c.line(x, y, x, y + h - 1, roof_hi)

houses = [
    (5, 3, 3, 3, 'h'),
    (12, 5, 2, 2, 'v'),
    (17, 2, 2, 2, 'h'),
    (26, 4, 2, 2, 'v'),
    (35, 2, 3, 3, 'v'),
    (42, 5, 2, 2, 'h'),
    (50, 2, 2, 2, 'v'),
    (56, 4, 2, 2, 'h'),
]
for hx, hy, hw, hh, o in houses:
    house(hx, hy, hw, hh, o)

tree_col = c.color((58, 76, 40), "tree")
tree_hi = c.color((88, 104, 60), "tree_hi")
for tx, ty in [(10, 2), (24, 3), (33, 2), (47, 3), (57, 2)]:
    c.rect(tx, ty, 2, 2, tree_col, fill=True)
    c.set(tx, ty, tree_hi)

# Two tiny farmers standing on ridge lines.
hat_col = c.color((234, 206, 128), "hat")
skin_col = c.color((210, 164, 112), "skin")
dark_col = c.color((56, 32, 14), "farmer_dark")

def farmer(fx, fy, body_rgb, tool=None):
    bcol = c.color(body_rgb)
    c.set(fx - 1, fy - 3, hat_col); c.set(fx, fy - 3, hat_col)
    c.set(fx - 1, fy - 2, hat_col); c.set(fx, fy - 2, skin_col)
    c.set(fx - 1, fy - 1, bcol); c.set(fx, fy - 1, bcol)
    c.set(fx - 1, fy, dark_col); c.set(fx, fy, dark_col)
    if tool == 'sickle':
        t = c.color((140, 96, 40), "tool")
        c.set(fx + 1, fy - 2, t); c.set(fx + 2, fy - 2, t)
    elif tool == 'basket':
        t = c.color((232, 198, 90), "basket")
        c.set(fx + 1, fy - 2, t); c.set(fx + 1, fy - 1, t)

farmer(16, 34, (104, 66, 36), tool='sickle')
farmer(46, 47, (70, 84, 104), tool='basket')

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 15)))
print(c.matrix_text(region=(0, 26, 63, 52)))
finish(c)
