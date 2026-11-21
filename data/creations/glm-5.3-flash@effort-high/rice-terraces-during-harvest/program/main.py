import math

W = H = 64
c = new_canvas(W, H, background=None, name="rice-terraces")

P = {}
def reg(name, hexv):
    P[name] = c.color(hexv, name=name)

reg("haze_far", "#A9BFA0")
reg("haze_near", "#8FA982")
reg("forest", "#5C7A48")
reg("tree", "#44603A")
reg("field", "#ADB868")
reg("field_dk", "#96A455")
reg("gold_pale", "#F2DE8A")
reg("gold_light", "#E9C95C")
reg("gold_mid", "#D9AE3F")
reg("gold_deep", "#C08D2C")
reg("gold_dark", "#A67422")
reg("green_gold", "#B4A63E")
reg("bund", "#6E4B23")
reg("bund_dk", "#513617")
reg("roof", "#8E3B2C")
reg("roof_lt", "#A8503C")
reg("roof_dk", "#67291F")
reg("wall", "#D9C49B")
reg("hat", "#EFD983")
reg("body", "#33415E")
reg("body_dk", "#222B42")

def wave(x, base, a1, l1, p1, a2=0.0, l2=1.0, p2=0.0):
    return base + a1*math.sin(2*math.pi*x/l1 + p1) + a2*math.sin(2*math.pi*x/l2 + p2)

fs = [
    lambda x: wave(x, 15, 1.2, 26, 0.3, 0.6, 11, 2.0),
    lambda x: wave(x, 20, 1.4, 23, 1.8, 0.6, 13, 0.5),
    lambda x: wave(x, 25, 1.5, 28, 2.6, 0.7, 12, 1.2),
    lambda x: wave(x, 30, 1.6, 24, 0.9, 0.8, 14, 2.4),
    lambda x: wave(x, 35, 1.8, 27, 1.4, 0.8, 12, 0.2),
    lambda x: wave(x, 40, 2.0, 25, 2.2, 0.9, 15, 1.6),
    lambda x: wave(x, 46, 2.2, 29, 0.6, 1.0, 13, 2.8),
    lambda x: wave(x, 52, 2.4, 26, 1.9, 1.0, 16, 0.8),
    lambda x: wave(x, 58, 2.4, 28, 2.5, 1.0, 14, 1.3),
]
conts = [[max(1, min(63, int(round(f(x))))) for x in range(W)] for f in fs]
conts.append([64] * W)

# ---- terrace bands (top = distant/muted, bottom = near/saturated) ----
bands = [
    ("green_gold", "gold_light", "gold_dark"),
    ("gold_dark",  "gold_mid",   "bund_dk"),
    ("gold_deep",  "gold_mid",   "gold_dark"),
    ("gold_mid",   "gold_pale",  "gold_deep"),
    ("gold_light", "gold_pale",  "gold_mid"),
    ("gold_deep",  "gold_light", "gold_dark"),
    ("gold_mid",   "gold_pale",  "gold_deep"),
    ("gold_light", "gold_pale",  "gold_mid"),
    ("gold_mid",   "gold_light", "gold_dark"),
]
for i in range(len(bands)):
    bcol, lcol, dcol = (P[n] for n in bands[i])
    for x in range(W):
        top = conts[i][x]
        bot = conts[i+1][x]
        h = bot - top - 1
        for y in range(top + 1, bot):
            c.set(x, y, bcol)
        if h > 0:
            # rice rows: stair-stepped dashes following the contour
            ry = top + 1 + ((x // 3 + i) % h)
            c.set(x, ry, lcol)
            # darker speckle (stubble / shadow)
            if (x * 13 + i * 7) % 11 == 0:
                sy = top + 1 + ((x * 5 + i * 3) % h)
                c.set(x, sy, dcol)

# ---- bund lines (terrace walls) ----
for i in range(len(conts) - 1):
    col = P["bund_dk"] if i >= 5 else P["bund"]
    for x in range(W):
        c.set(x, conts[i][x], col)

# ---- distant ridges, forest edge, village fields ----
for x in range(W):
    m1 = 2 + int(round(1.4 * math.sin(x / 8.0 + 1.0)))
    m2 = 5 + int(round(1.6 * math.sin(x / 6.0 + 0.4)))
    m2 = max(m2, m1 + 1)
    for y in range(0, m1 + 1):
        c.set(x, y, P["haze_far"])
    for y in range(m1 + 1, m2 + 1):
        c.set(x, y, P["haze_near"])
    f0 = 7 + (1 if (x * 7) % 5 == 0 else 0)
    for y in range(m2 + 1, f0):
        c.set(x, y, P["forest"])
    for y in range(f0, conts[0][x]):
        c.set(x, y, P["field"])
    # field texture
    if (x * 11) % 4 == 0 and conts[0][x] - f0 > 1:
        c.set(x, f0 + (x % max(1, conts[0][x] - f0)), P["field_dk"])

# forest speckles
for tx, ty in [(1, 6), (5, 7), (12, 6), (17, 7), (26, 6), (30, 7),
               (39, 6), (43, 7), (52, 6), (57, 7), (62, 6)]:
    c.set(tx, ty, P["tree"])

# ---- village houses ----
def house(x, y):
    for xx in range(x, x + 5):
        c.set(xx, y, P["roof"])
    for xx in range(x + 1, x + 4):
        c.set(xx, y + 1, P["roof_lt"])
    for xx in range(x, x + 5):
        c.set(xx, y + 2, P["roof_dk"])
    for xx in range(x + 1, x + 4):
        c.set(xx, y + 3, P["wall"])

house(6, 8)
house(19, 7)
house(33, 9)
house(47, 8)

# trees around the village
for tx, ty in [(3, 10), (14, 10), (27, 10), (41, 10), (55, 10), (61, 9), (25, 12), (44, 12)]:
    c.set(tx, ty, P["tree"])
    c.set(tx + 1, ty, P["tree"])
    c.set(tx, ty + 1, P["tree"])

# ---- farmers on narrow ridges ----
def farmer(cx, cy):
    # widen the bund into a walking ridge
    for xx in range(cx - 3, cx + 4):
        c.set(xx, cy, P["bund_dk"])
        c.set(xx, cy + 1, P["bund"])
    c.set(cx, cy - 3, P["hat"])
    c.set(cx + 1, cy - 3, P["hat"])
    c.set(cx, cy - 2, P["body"])
    c.set(cx + 1, cy - 2, P["body"])
    c.set(cx, cy - 1, P["body_dk"])
    c.set(cx + 1, cy - 1, P["body"])

fa_x, fb_x = 24, 42
farmer(fa_x, conts[5][fa_x])
farmer(fb_x, conts[7][fb_x])

print(c.stats_text())
save("rice-terraces", c)
finish(c)
