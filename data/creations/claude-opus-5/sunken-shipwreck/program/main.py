import math

c = new_canvas(64, 64, name="output")

# ---------------- water gradient ----------------
water = ["#2e7f96", "#2a7690", "#266d89", "#226482", "#1e5b7b",
         "#1a5274", "#17496d", "#154367", "#123c60", "#103659"]
for i, col in enumerate(water):
    c.rect(0, i * 6, 64, 7, col)
c.rect(0, 58, 64, 6, water[-1])

# soften the band edges with a checker blend
for i in range(1, len(water)):
    c.dither(0, i * 6 - 1, 64, 2, [water[i - 1], water[i]], pattern="bayer4")

shaft = "#3f95a8"
for x0, length in ((6, 30), (23, 34), (42, 28), (55, 22)):
    for i in range(length):
        x = x0 + i // 3
        c.set(x, i, shaft)
        if i < length // 2:
            c.set(x + 1, i, shaft)

# ---------------- palette ----------------
sand = "#c9b183"
sand_d = "#ab9263"
sand_s = "#e2d0a7"
sand_sh = "#8d7750"

wood = "#6b4a30"
wood_m = "#5a3d27"
wood_d = "#42291a"
wood_l = "#8a6440"
dark = "#1d1511"
rust = "#59795f"
rust_d = "#3d5a49"


def sand_top(x):
    return 48 - 2.0 * math.sin(x / 9.0) - 1.2 * math.sin(x / 3.5 + 1.0)


for x in range(64):
    t = int(round(sand_top(x)))
    c.rect(x, t, 1, 64 - t, sand)
    c.set(x, t, sand_s)

# ---------------- shipwreck hull ----------------
X0, X1 = 9, 56


def hull_edges(x):
    t = (x - X0) / float(X1 - X0)
    top = 45.0 - 16.0 * t
    bot = 54.0 - 10.0 * t
    if t > 0.70:
        f = ((t - 0.70) / 0.30) ** 1.4
        bot = bot - (bot - (top + 1.0)) * f
    return top, bot


for x in range(X0, X1 + 1):
    ft, fb = hull_edges(x)
    top, bot = int(round(ft)), int(round(fb))
    for y in range(top, bot + 1):
        d = y - top
        if d == 0:
            col = wood_l                      # gunwale / deck edge
        elif d % 4 == 1:
            col = wood_d                      # plank seam
        elif y >= bot - 1:
            col = wood_d                      # shaded belly
        else:
            col = wood if (d // 4) % 2 == 0 else wood_m
        c.set(x, y, col)

# prow stem post
c.line(55, 27, 56, 33, wood_l)
c.set(54, 28, wood_d)

# broken deck gap near the stern: snapped planks
c.path("M14 44 C 19 41 24 45 20 48 C 15 50 11 47 14 44 Z", dark)
for i in range(4):
    bx = 13 + i * 3
    ty, by = hull_edges(bx)
    c.line(bx, int(ty) + 1, bx, int(ty) + 6 - i, wood_m)
    c.set(bx, int(ty) + 1, wood_l)

# exposed ribs rising out of the hole
for rx, ry in ((16, 40), (19, 39), (22, 41)):
    c.line(rx, ry, rx, ry + 5, wood_d)
    c.set(rx, ry, wood_m)

# algae / corrosion patches on the hull
c.path("M30 43 C 35 41 40 44 36 47 C 31 49 27 46 30 43 Z", rust)
c.path("M44 36 C 48 34 51 37 48 39 C 44 41 41 38 44 36 Z", rust)
c.set(34, 42, rust_d)
c.set(46, 38, rust_d)
c.set(26, 48, rust_d)
c.set(50, 34, rust_d)

# ---------------- broken mast and rigging ----------------
c.line(34, 37, 26, 13, wood_m)
c.line(35, 37, 27, 13, wood)
c.set(26, 12, wood_d)
c.set(25, 14, wood_d)
# spar
c.line(22, 20, 34, 24, wood_m)
c.set(22, 20, wood_d)
c.set(34, 24, wood_d)
# tattered sail hanging from the spar, torn lower edge
sail = "#9fae9f"
sail_d = "#76867a"
c.path("M24 21 C 28 22 31 26 30 30 L28 28 L27 30 L26 27 L25 29 L24 21 Z", sail)
c.path("M26 22 C 28 24 29 27 29 29", sail_d, fill=False)
c.set(30, 29, sail_d)
# rigging lines
c.line(26, 15, 21, 21, "#2c3a42")
c.line(28, 18, 36, 33, "#2c3a42")

# ---------------- sand burying the hull ----------------
for x in range(64):
    t = sand_top(x) + 5 + 1.6 * math.sin(x / 5.0 + 2.0)
    if X0 - 2 <= x <= X1:
        ft, fb = hull_edges(x)
        bury = fb - 3.0 + 3.0 * ((x - X0) / float(X1 - X0))
        t = max(t, min(bury, 56))
    t = int(round(min(t, 57)))
    c.rect(x, t, 1, 64 - t, sand_d)
    c.set(x, t, sand)

# ---------------- coral and seaweed ----------------
grn = "#3f8f52"
grn_l = "#58ad66"
cor = "#d4705f"
cor_l = "#ea9a82"
cor2 = "#9a66a8"
cor2_d = "#75497f"

c.path("M6 58 C 2 51 10 47 5 41 C 2 36 8 33 6 29", grn, fill=False)
c.path("M9 59 C 6 53 12 49 9 44 C 7 40 11 37 10 34", grn_l, fill=False)
c.path("M60 59 C 63 52 56 48 61 43 C 63 39 59 36 60 32", grn, fill=False)
c.path("M57 60 C 54 55 59 51 56 46 C 54 43 57 40 57 37", grn_l, fill=False)
c.path("M30 62 C 28 57 33 54 31 50", grn, fill=False)

# branching coral right of the bow
c.line(50, 56, 50, 47, cor)
c.line(50, 51, 47, 47, cor)
c.line(50, 50, 53, 45, cor)
c.set(47, 46, cor_l)
c.set(53, 44, cor_l)
c.set(50, 46, cor_l)
# purple fan coral at the left
c.path("M17 61 C 13 56 18 52 22 57 Z", cor2)
c.line(19, 61, 19, 58, cor2_d)
c.set(16, 58, cor2_d)
# small coral nubs
c.set(38, 58, cor)
c.set(39, 57, cor_l)
c.set(43, 60, cor2)

for px, py in ((26, 59), (35, 61), (12, 62), (45, 57), (62, 62), (22, 63), (54, 61)):
    c.set(px, py, sand_sh)

# scattered debris planks half-buried in the sand
c.line(2, 57, 7, 56, wood_m)
c.set(3, 58, wood_d)
c.line(33, 56, 38, 55, wood_m)
c.set(35, 55, wood_l)
c.set(36, 56, wood_d)
c.line(56, 58, 60, 57, wood_m)
c.set(58, 58, wood_d)

# sand ripples and a soft shadow pooling under the hull
c.path("M2 60 C 10 58 18 61 26 59", sand_sh, fill=False)
c.path("M36 62 C 44 60 52 63 61 61", sand_sh, fill=False)
for x in range(X0, X1 - 1):
    t = sand_top(x) + 5 + 1.6 * math.sin(x / 5.0 + 2.0)
    ft, fbt = hull_edges(x)
    bury = fbt - 3.0 + 3.0 * ((x - X0) / float(X1 - X0))
    y = int(round(min(max(t, min(bury, 56)), 57)))
    c.set(x, y + 1, sand_sh)
    if x % 3 == 0:
        c.set(x, y + 2, sand_sh)

# ---------------- school of fish ----------------
fb = "#f0b23f"
fb_d = "#c8862a"
fw = "#e8e3c8"
fw_d = "#b3ae95"
feye = "#1b2430"


def fish(x, y, body, tail):
    c.set(x + 1, y, body)
    c.set(x + 2, y, body)
    c.line(x, y + 1, x + 3, y + 1, body)
    c.set(x + 1, y + 2, body)
    c.set(x + 2, y + 2, body)
    c.set(x + 4, y, tail)
    c.set(x + 4, y + 2, tail)
    c.set(x + 4, y + 1, body)
    c.set(x + 1, y + 1, feye)


def fry(x, y, body):
    c.line(x, y, x + 2, y, body)
    c.set(x + 3, y - 1, body)
    c.set(x + 3, y + 1, body)


# a cohesive shoal drifting past the wreck, all facing right
school = [(4, 23), (10, 20), (10, 26), (16, 17), (16, 23), (22, 14),
          (22, 20), (28, 11), (34, 8), (40, 11), (40, 17), (46, 14),
          (46, 20), (52, 17), (52, 23), (58, 20)]
for i, (fx, fy) in enumerate(school):
    if i % 5 == 3:
        fish(fx, fy, fw, fw_d)
    else:
        fish(fx, fy, fb, fb_d)

# strays
for fx, fy in ((6, 8), (56, 7),):
    fish(fx, fy, fb, fb_d)
for fx, fy in ((14, 33), (50, 38), (28, 4)):
    fry(fx, fy, fw)

for bx, by in ((21, 41), (23, 37), (59, 29), (60, 26), (12, 38), (4, 31)):
    c.set(bx, by, "#8fd0dc")

print(len([p for p in c.palette()]))

view(c)
finish(c)
