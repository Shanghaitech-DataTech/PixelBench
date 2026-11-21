W = H = 64
VPX, VPY = 36, 27          # vanishing point
BL, BR = -24, 94           # asphalt edges at the bottom row
DY = 5                     # how far the sprite is pushed down the road

sprite = input_canvas.copy(name="sprite")
sprite.fill_at(0, 0, None)          # drop the white background


def road_t(y):
    return (y - VPY) / float(64 - VPY)


def left_x(y):
    return VPX + (BL - VPX) * road_t(y)


def right_x(y):
    return VPX + (BR - VPX) * road_t(y)


c = new_canvas(W, H, name="output")

# ---------------- sky ----------------
for col, y0, h in [("#4fa3dd", 0, 6), ("#68b6e7", 6, 6), ("#8acbee", 12, 6),
                   ("#aadcf4", 18, 5), ("#cfeaf8", 23, 4)]:
    c.rect(0, y0, W, h, col)

c.ellipse(12, 8, 6, 2, "#ffffff")
c.ellipse(16, 7, 4, 2, "#ffffff")
c.ellipse(8, 9, 3, 1, "#ffffff")
c.ellipse(12, 10, 6, 1, "#dcecf7")
c.ellipse(46, 13, 7, 2, "#ffffff")
c.ellipse(51, 12, 4, 1, "#ffffff")
c.ellipse(46, 14, 6, 1, "#dcecf7")

# ---------------- distant hills ----------------
c.path("M 0 27 L 0 22 Q 8 16 18 22 Q 26 26 31 24 L 63 24 L 63 27 Z", "#8fb0cf")
c.path("M 30 27 L 30 23 Q 42 15 54 22 Q 60 25 63 23 L 63 27 Z", "#7fa3c4")

# ---------------- fields ----------------
c.rect(0, 27, W, H - 27, "#64a847")
for y0, h, col in [(27, 1, "#4e8c3a"), (28, 1, "#6cb04e"), (29, 2, "#5c9c41"),
                   (31, 2, "#6cb04e"), (33, 3, "#5a9a3f"), (36, 3, "#6fb551"),
                   (39, 4, "#58973d"), (43, 5, "#6fb551"), (48, 6, "#55923a"),
                   (54, 10, "#6bb14d")]:
    c.rect(0, y0, W, h, col)

# soft distant tree line hugging the horizon, irregular crowns
heights = [2, 3, 2, 3, 4, 3, 2, 3, 3, 4, 2, 3, 4, 3, 2, 3, 3, 2, 4, 3, 2, 3]
x = 0
for i, hh in enumerate(heights):
    wd = 3 if hh >= 3 else 2
    c.rect(x, 28 - hh, wd, hh, "#3a7a3a")
    if hh >= 3:
        c.set(x + wd // 2, 27 - hh, "#3a7a3a")
        c.rect(x + wd - 1, 29 - hh, 1, hh - 1, "#2f6b33")
    x += wd
    if x >= W:
        break
c.rect(0, 27, W, 1, "#2f6b33")

# ---------------- road ----------------
dirt = "#b79b63"
dirt_d = "#9c8a62"
asph = "#5f6268"
asph_d = "#565a60"
asph_l = "#6b6e74"

c.poly([(VPX, VPY), (BR + 8, 63), (BL - 8, 63)], dirt)
c.poly([(VPX, VPY), (BR, 63), (BL, 63)], asph)

# worn wheel tracks and patchy tarmac
for y in range(VPY, H):
    lx, rx = left_x(y), right_x(y)
    cx, half = (lx + rx) / 2.0, (rx - lx) / 2.0
    tw = max(1, int(round(half * 0.22)))
    for sgn in (-1, 1):
        tx = int(round(cx + sgn * half * 0.52))
        c.rect(tx - tw // 2, y, tw, 1, asph_d)
    if y % 7 == 0:
        c.rect(int(lx) + 1, y, max(1, int(rx - lx) - 1), 1, asph_l)

# crumbling asphalt edges
for y in range(VPY + 2, H):
    lx, rx = int(round(left_x(y))), int(round(right_x(y)))
    def put(px, py, col):
        if 0 <= px < W and 0 <= py < H:
            c.set(px, py, col)
    if y % 3 == 0:
        put(lx, y, dirt)
        put(rx, y, dirt)
    if y % 5 == 0:
        put(lx + 1, y, dirt_d)
        put(rx - 1, y, dirt_d)

# dashed centre line
y = VPY + 2
while y < H:
    t = road_t(y)
    dash = max(1, int(round(1 + 5 * t)))
    gap = max(1, int(round(1 + 4 * t)))
    wid = max(1, int(round(1 + 2.2 * t)))
    for yy in range(y, min(H, y + dash)):
        cx = (left_x(yy) + right_x(yy)) / 2.0
        c.rect(int(round(cx - (wid - 1) / 2.0)), yy, wid, 1, "#e9e2c4")
    y += dash + gap

# ---------------- roadside detail ----------------
def bush(cx, cy, r, dark, light):
    c.ellipse(cx, cy, r, max(1, r - 1), dark)
    c.ellipse(cx - 1, cy - 1, max(1, r - 2), max(1, r - 2), light)

# telegraph poles receding along the left verge
tops = []
for py in (47, 42, 38, 35, 32, 30, 29):
    t = road_t(py)
    px = int(round(left_x(py))) - max(1, int(round(4 * t)))
    ph = max(2, int(round(15 * t)))
    if px < 0:
        continue
    c.rect(px, py - ph, 1, ph, "#6b4a2c")
    if t > 0.45:
        c.set(px, py - ph, "#8a6338")
        c.rect(px - 1, py - ph + 1, 3, 1, "#6b4a2c")
    tops.append((px, py - ph))
for (x0, y0), (x1, y1) in zip(tops, tops[1:]):
    c.line(x0, y0 + 1, x1, y1 + 1, "#3c3230")

# verge planting
bush(61, 59, 5, "#2d6b2f", "#46913c")
bush(3, 57, 4, "#2d6b2f", "#46913c")
bush(55, 36, 2, "#2f6e31", "#45903b")
bush(7, 34, 2, "#2f6e31", "#45903b")
c.rect(58, 31, 1, 5, "#5a3f25")
bush(58, 30, 3, "#2a6530", "#3f8a3a")

for fx, fy in ((9, 52), (13, 60), (59, 50), (2, 46), (52, 32), (62, 43)):
    if 0 <= fx < W and 0 <= fy < H:
        c.set(fx, fy, "#f2e55a")

# ---------------- contact shadow under the bike ----------------
by = 47 + DY                       # ground row of the wheels
c.ellipse(13, by + 1, 9, 2, "#43464b")
c.ellipse(50, by + 1, 9, 2, "#43464b")
c.rect(18, by, 30, 3, "#43464b")
c.ellipse(13, by + 3, 10, 1, "#4c4f55")
c.ellipse(50, by + 3, 10, 1, "#4c4f55")
c.rect(20, by + 3, 26, 1, "#4c4f55")

# ---------------- the motorcycle ----------------
c.blit(sprite, 0, DY)

result = c
view(result)
save("motorcycle_road", result)
finish(result)
