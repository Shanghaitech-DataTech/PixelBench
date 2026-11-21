W = 128
H = 128
HORIZON = 66
CEIL_END = 16
POOL_BOTTOM = 116

bg = new_canvas(W, H, background=None, name="bg")

def reg(name, rgb):
    return bg.color(rgb, name=name)

# ---- palette -------------------------------------------------------------
reg('white',       (255, 255, 255))
reg('cloud',       (240, 247, 253))
reg('wall_light',  (219, 234, 249))
reg('wall_mid',    (202, 224, 245))
reg('wall_dark',   (178, 208, 236))
reg('line',        (146, 186, 220))
reg('line_dark',   (120, 164, 202))
reg('ceil',        (228, 239, 249))
reg('ceil_dark',   (202, 219, 234))
reg('light',       (255, 255, 246))
reg('light_glow',  (236, 246, 255))
reg('floor_light', (204, 233, 248))
reg('floor_mid',   (180, 217, 240))
reg('floor_dark',  (156, 200, 232))
reg('floor_line',  (126, 172, 210))
reg('water',       (150, 205, 235, 110))
reg('water_light', (214, 242, 252, 200))
reg('water_deep',  (110, 175, 215, 150))
reg('slide',       (247, 251, 253))
reg('slide_shade', (212, 226, 240))
reg('slide_dark',  (178, 200, 222))
reg('ring',        (250, 214, 60))
reg('ring_shade',  (228, 178, 38))
reg('ring_hi',     (255, 242, 150))
reg('skin',        (244, 206, 176))
reg('skin_shade',  (226, 184, 152))
reg('hair',        (96, 68, 54))
reg('hair_hi',     (134, 100, 80))
reg('suit',        (226, 112, 142))
reg('suit_shade',  (200, 88, 122))
reg('foam',        (238, 248, 252))
reg('shadow',      (112, 152, 198, 120))

# ---- ceiling -------------------------------------------------------------
bg.rect(0, 0, W, CEIL_END, 'ceil', fill=True)
for (lx, lw) in [(14, 14), (40, 14), (74, 14), (100, 14)]:
    bg.rect(lx - 2, 2, lw + 4, 10, 'light_glow', fill=True)
    bg.rect(lx, 4, lw, 6, 'light', fill=True)
bg.line(0, CEIL_END - 1, W - 1, CEIL_END - 1, 'ceil_dark')

# ---- far wall ------------------------------------------------------------
bg.rect(0, CEIL_END, W, HORIZON - CEIL_END, 'wall_light', fill=True)
for r in range(6):
    for cc in range(16):
        x = cc * 8
        y = CEIL_END + r * 8
        bg.rect(x, y, 8, 8, 'wall_light' if (r + cc) % 2 == 0 else 'wall_mid', fill=True)
for r in range(7):
    y = CEIL_END + r * 8
    bg.line(0, y, W - 1, y, 'line')
for cc in range(17):
    x = min(cc * 8, 127)
    bg.line(x, CEIL_END, x, HORIZON - 1, 'line')
bg.line(0, HORIZON - 1, W - 1, HORIZON - 1, 'line_dark')

# ---- tiled columns -------------------------------------------------------
cols = [(10, 22), (44, 56), (72, 84), (106, 118)]
for (x0, x1) in cols:
    bg.rect(x0, CEIL_END, x1 - x0, HORIZON - CEIL_END, 'cloud', fill=True)
    bg.rect(x0, CEIL_END, 3, HORIZON - CEIL_END, 'white', fill=True)
    bg.rect(x1 - 3, CEIL_END, 3, HORIZON - CEIL_END, 'wall_dark', fill=True)
    for r in range(1, 6):
        y = CEIL_END + r * 8
        bg.line(x0 + 2, y, x1 - 4, y, 'line')
    bg.rect(x0 - 1, CEIL_END - 1, x1 - x0 + 2, 3, 'ceil_dark', fill=True)
    bg.rect(x0 - 1, HORIZON - 3, x1 - x0 + 2, 3, 'wall_dark', fill=True)

# ---- pool bottom (seen through clear water) ------------------------------
floor = new_canvas(W, H, background=None, name="floor")
D = POOL_BOTTOM - HORIZON
ys = [HORIZON]
for k in range(1, 8):
    ys.append(HORIZON + int(D * ((k / 7.0) ** 1.6)))
for i in range(len(ys) - 1):
    y0 = ys[i]
    y1 = ys[i + 1]
    col = 'floor_light' if i % 2 == 0 else 'floor_mid'
    floor.rect(0, y0, W, y1 - y0, col, fill=True)
for y in ys[1:-1]:
    floor.line(0, y, W - 1, y, 'floor_line')

xs116 = [-24, 0, 16, 32, 48, 64, 80, 96, 112, 128, 152]
for x116 in xs116:
    floor.line(64, HORIZON, x116, POOL_BOTTOM, 'floor_line')

# ---- water ---------------------------------------------------------------
water = new_canvas(W, H, background=None, name="water")
water.rect(0, HORIZON, W, POOL_BOTTOM - HORIZON, 'water', fill=True)
water.line(0, HORIZON, W - 1, HORIZON, 'water_light')

for y in [70, 75, 82, 89, 97, 105, 112]:
    x = 0
    while x < W:
        ln = 6 + ((x // 16) % 3) * 3
        water.line(x, y, min(x + ln, W - 1), y, 'water_light')
        x += ln + 7 + ((x // 29) % 3) * 4
for y in [72, 84, 96, 108]:
    x = 4
    while x < W:
        ln = 4 + ((x // 20) % 2) * 3
        water.line(x, y + 1, min(x + ln, W - 1), y + 1, 'water_deep')
        x += ln + 10

# reflections of lights and columns on the water
for lx in [21, 47, 81, 107, 16, 50, 78, 112]:
    for yy in range(HORIZON + 2, 112, 8):
        off = ((yy // 8) % 3) - 1
        water.line(lx + off, yy, lx + off, yy + 3, 'water_light')

# ---- water slide ---------------------------------------------------------
def bezier_pts(p0, p1, p2, p3, n=60):
    out = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt ** 3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t ** 3 * p3[0]
        y = mt ** 3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t ** 3 * p3[1]
        out.append((x, y))
    return out

def draw_tube(c, pts, r, base, light, shade):
    for x, y in pts:
        c.circle(int(round(x)), int(round(y)), r, base, fill=True)
    for x, y in pts:
        c.circle(int(round(x)), int(round(y)) + r - 2, r - 3, shade, fill=True)
    for x, y in pts:
        c.circle(int(round(x)), int(round(y)) - r + 2, r - 4, light, fill=True)

p0 = (110, 26)
p1 = (78, 16)
p2 = (66, 52)
p3 = (90, 86)
pts = bezier_pts(p0, p1, p2, p3, 60)

slide_full = new_canvas(W, H, background=None, name="slide_full")
slide_full.ellipse(int(p0[0]), int(p0[1]), 8, 10, 'slide_dark', fill=True)
draw_tube(slide_full, pts, 7, 'slide', 'white', 'slide_shade')

entry_y = 80
entry = min(pts, key=lambda p: abs(p[1] - entry_y))
pts_above = [p for p in pts if p[1] <= entry_y + 2]
slide_above = new_canvas(W, H, background=None, name="slide_above")
draw_tube(slide_above, pts_above, 7, 'slide', 'white', 'slide_shade')

# ---- foreground deck -----------------------------------------------------
deck = new_canvas(W, H, background=None, name="deck")
deck.rect(0, POOL_BOTTOM, W, H - POOL_BOTTOM, 'floor_light', fill=True)
deck.rect(0, POOL_BOTTOM, W, 4, 'floor_mid', fill=True)
deck.rect(0, POOL_BOTTOM - 2, W, 2, 'cloud', fill=True)
deck.line(0, POOL_BOTTOM, W - 1, POOL_BOTTOM, 'line_dark')
for y in [120, 124]:
    deck.line(0, y, W - 1, y, 'floor_line')
for x116 in xs116:
    x127 = 64 + int(round((x116 - 64) * (H - 1 - HORIZON) / (POOL_BOTTOM - HORIZON)))
    deck.line(x116, POOL_BOTTOM, x127, H - 1, 'floor_line')

# ---- girl in swim ring ---------------------------------------------------
girl = new_canvas(W, H, background=None, name="girl")
girl.ellipse(64, 99, 28, 7, 'shadow', fill=True)

# swim ring (donut)
girl.ellipse(64, 93, 22, 9, 'ring', fill=True)
girl.ellipse(64, 88, 17, 4, 'ring_hi', fill=True)
girl.ellipse(64, 97, 20, 5, 'ring_shade', fill=True)
girl.ellipse(64, 92, 12, 5, 'skin', fill=True)

# torso / back
girl.ellipse(64, 82, 11, 7, 'skin', fill=True)
girl.rect(54, 85, 20, 7, 'suit', fill=True)
girl.line(54, 85, 74, 85, 'suit_shade')
girl.line(57, 79, 55, 85, 'suit')
girl.line(71, 79, 73, 85, 'suit')

# arms resting on the ring
def arm(c, pts):
    for (x, y) in pts:
        c.circle(int(x), int(y), 3, 'skin', fill=True)
    for (x, y) in pts:
        c.circle(int(x), int(y) + 1, 2, 'skin_shade', fill=True)

arm(girl, [(55, 82), (48, 86), (44, 90)])
arm(girl, [(73, 82), (80, 86), (84, 90)])

# hair (seen from behind)
girl.ellipse(64, 68, 7, 10, 'hair', fill=True)
girl.ellipse(62, 65, 2, 3, 'hair_hi', fill=True)

# ---- foam / splashes -----------------------------------------------------
foam = new_canvas(W, H, background=None, name="foam")
foam.ellipse(64, 100, 27, 6, 'foam', fill=False)
foam.line(40, 102, 48, 102, 'foam')
foam.line(80, 102, 88, 102, 'foam')

ex = int(round(entry[0]))
ey = int(round(entry[1]))
foam.ellipse(ex, ey, 11, 5, 'foam', fill=True)
foam.ellipse(ex + 4, ey - 2, 6, 3, 'foam', fill=True)
for dx in [-14, -8, -2, 4, 10]:
    foam.line(ex + dx, ey + 4, ex + dx + 4, ey + 4, 'foam')

# ---- composite -----------------------------------------------------------
result = flatten([bg, floor, slide_full, water, deck, slide_above, girl, foam], name="result")

print(result.stats_text())

NAME_CHAR = {
    'white': 'W', 'cloud': 'w', 'wall_light': 'a', 'wall_mid': 'b', 'wall_dark': 'd',
    'line': 'l', 'line_dark': 'L', 'ceil': 'c', 'ceil_dark': 'C', 'light': '*',
    'light_glow': 'g', 'floor_light': 'f', 'floor_mid': 'F', 'floor_dark': 'D',
    'floor_line': 'l', 'water': '~', 'water_light': 'r', 'water_deep': 'v',
    'slide': 'S', 'slide_shade': 's', 'slide_dark': 'd', 'ring': 'Y',
    'ring_shade': 'y', 'ring_hi': 'H', 'skin': 'k', 'skin_shade': 'h',
    'hair': 'n', 'hair_hi': 'N', 'suit': 'p', 'suit_shade': 'P', 'foam': 'o',
    'shadow': 'x',
}

def preview(c, block=4):
    for y in range(0, H, block):
        row = []
        for x in range(0, W, block):
            idx = c.get(min(x + block // 2, W - 1), min(y + block // 2, H - 1))
            if idx is None:
                row.append('.')
            else:
                nm = c.color_name(idx)
                row.append(NAME_CHAR.get(nm, '~'))
        print(''.join(row))

print('--- preview ---')
preview(result, 4)

save("poolcore-water-slide", result)
finish(result)
