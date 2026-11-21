import math

pal = input_canvas.palette()
rgba = {e['index']: e['rgba'] for e in pal}

W, H = 256, 128
src = [[rgba[input_canvas.get(x, y)] for x in range(W)] for y in range(H)]

out = input_canvas.copy(name='output')

MX, MY, MR = 128, 25, 21          # blood moon centre / radius


def clamp(v):
    return 0 if v < 0 else (255 if v > 255 else int(v))


def px(c, x, y):
    """live RGBA read: the palette grows while drawing"""
    i = c.get(x, y)
    e = rgba.get(i)
    if e is None:
        e = {p['index']: p['rgba'] for p in c.palette()}[i]
        rgba[i] = e
    return e


def hsh(x, y, s=0):
    n = (x * 374761393 + y * 668265263 + s * 362437) & 0xFFFFFFFF
    n = (n ^ (n >> 13)) * 1274126177 & 0xFFFFFFFF
    return ((n ^ (n >> 16)) & 0xFFFF) / 65535.0


# ---------------------------------------------------------------- masks
def is_stone(r, g, b):
    """warm masonry / rock / road of the original castle"""
    return r > b + 12 and r > 40


stone = [[is_stone(*src[y][x][:3]) for x in range(W)] for y in range(H)]

# ------------------------------------------------- sky / cloud recolour
SKY = [
    (0,   (6, 2, 6)),
    (28,  (22, 6, 13)),
    (58,  (46, 10, 19)),
    (92,  (76, 15, 23)),
    (126, (112, 22, 27)),
    (160, (150, 32, 31)),
    (196, (194, 58, 42)),
    (226, (228, 100, 66)),
    (255, (252, 164, 124)),
]

# dark basalt ramp for the fortress
ROCK = [
    (0,   (10, 6, 10)),
    (40,  (24, 14, 19)),
    (80,  (44, 24, 28)),
    (120, (68, 36, 36)),
    (160, (96, 50, 44)),
    (200, (128, 68, 54)),
    (255, (166, 94, 70)),
]


def ramp(table, l):
    if l <= table[0][0]:
        return table[0][1]
    for i in range(len(table) - 1):
        l0, c0 = table[i]
        l1, c1 = table[i + 1]
        if l0 <= l <= l1:
            t = (l - l0) / (l1 - l0)
            return tuple(c0[k] + (c1[k] - c0[k]) * t for k in range(3))
    return table[-1][1]


for y in range(H):
    for x in range(W):
        r, g, b, a = src[y][x]
        if a == 0:
            continue
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        magic = (g > 175 and b > 150 and r < 160) or (r > 200 and b > 200 and g < 160)
        if stone[y][x]:
            nr, ng, nb = ramp(ROCK, lum)
            if y > 104:                       # the road, left as faint embers
                nr, ng, nb = nr * 1.35 + 14, ng * 1.05 + 4, nb * 0.9 + 4
        elif magic:
            nr, ng, nb = 255, 128, 56        # sigil arcs become hellfire
        else:
            nr, ng, nb = ramp(SKY, lum)
            if b > r + 30 and lum > 150:     # the big cloud banks: lit from the moon
                nr, ng, nb = nr * 1.04 + 12, ng * 0.92, nb * 0.9

        # moon bloom
        d = math.hypot(x - MX, (y - MY) * 1.05)
        gl = max(0.0, 1.0 - d / 108.0) ** 2 * (0.72 if not stone[y][x] else 0.42)
        nr += (214 - nr) * gl
        ng += (48 - ng) * gl
        nb += (42 - nb) * gl

        if y > 72:                            # brooding foreground
            k = 1.0 - 0.26 * ((y - 72) / 56.0)
            nr, ng, nb = nr * k, ng * k, nb * k

        out.set(x, y, (clamp(nr), clamp(ng), clamp(nb), 255))

# ---------------------------------------------------------- blood moon
for y in range(MY - MR - 7, MY + MR + 8):
    if not (0 <= y < H):
        continue
    for x in range(MX - MR - 7, MX + MR + 8):
        if not (0 <= x < W) or stone[y][x]:
            continue
        d = math.hypot(x - MX, y - MY)
        if d <= MR + 0.4:
            t = d / MR
            k = 1.0 - 0.42 * t * t
            base = (214 * k, 46 * k + 8, 38 * k + 10)
            # maria / mottling
            m = hsh(x // 2, y // 2, 3) * 0.55 + hsh(x, y, 9) * 0.25
            if m > 0.52:
                base = (base[0] * 0.80, base[1] * 0.74, base[2] * 0.80)
            if m > 0.72:
                base = (base[0] * 0.86, base[1] * 0.82, base[2] * 0.86)
            if t > 0.90:
                base = (base[0] * 0.74, base[1] * 0.70, base[2] * 0.74)
            out.set(x, y, (clamp(base[0]), clamp(base[1]), clamp(base[2]), 255))
        elif d <= MR + 6.5:
            g = max(0.0, 1.0 - (d - MR) / 6.5) ** 1.7
            r0, g0, b0, _ = px(out, x, y)
            out.set(x, y, (clamp(r0 + (226 - r0) * g * 0.72),
                           clamp(g0 + (56 - g0) * g * 0.72),
                           clamp(b0 + (44 - b0) * g * 0.72), 255))

# a few craters
for cx, cy, cr in [(120, 18, 4), (134, 31, 3), (127, 22, 2), (118, 30, 2), (136, 17, 2)]:
    for y in range(cy - cr, cy + cr + 1):
        for x in range(cx - cr, cx + cr + 1):
            if stone[y][x] or math.hypot(x - cx, y - cy) > cr:
                continue
            r0, g0, b0, _ = px(out, x, y)
            out.set(x, y, (clamp(r0 * 0.80), clamp(g0 * 0.76), clamp(b0 * 0.80), 255))

VOID = (9, 4, 9, 255)
EDGE = (46, 15, 18, 255)
EMBER = (255, 136, 48, 255)
EMBER2 = (255, 206, 110, 255)
BLOOD = (196, 36, 34, 255)

# ------------------------------------------------- demonic horns & spires
# --- great horns sweeping up from behind the fortress shoulders ---
out.path("M110 92 C104 78 97 62 91 44 C99 64 107 80 116 92 Z", VOID)
out.path("M150 92 C156 78 163 62 169 44 C161 64 153 80 144 92 Z", VOID)
out.path("M110 92 C104 78 97 62 91 44", EDGE, fill=False)
out.path("M150 92 C156 78 163 62 169 44", EDGE, fill=False)
for hx, hy in [(91, 44), (92, 46), (169, 44), (168, 46)]:
    out.set(hx, hy, EDGE)


def turret_top(x, y0=46, y1=104):
    for y in range(y0, y1):
        if stone[y][x] and stone[y + 1][x] and stone[y + 2][x]:
            return y
    return None


# --- slender needles grown out of the real turret tops ---
for bx, hgt in [(105, 11), (111, 14), (118, 10), (124, 9),
                (139, 9), (145, 11), (151, 14), (158, 11), (164, 9)]:
    ty = turret_top(bx)
    if ty is None:
        continue
    tip = ty - hgt
    out.poly([(bx - 1, ty + 1), (bx, tip), (bx + 1, ty + 1)], VOID)
    out.set(bx, ty, VOID)
    out.set(bx, tip + 1, EDGE)
    out.set(bx, tip - 1, BLOOD)

# --- the central spire, crowned with three thin needles ---
ty = turret_top(131, 30, 70) or 48
out.line(131, ty + 1, 131, ty - 16, VOID)
out.set(130, ty + 1, VOID)
out.set(132, ty + 1, VOID)
out.set(131, ty - 17, BLOOD)
out.set(131, ty - 18, EMBER)
for dx, hgt in [(-2, 7), (2, 7)]:
    out.line(131 + dx, ty + 3, 131 + dx, ty + 3 - hgt, VOID)
    out.set(131 + dx, ty + 2 - hgt, BLOOD)
out.set(131, ty - 12, EDGE)
out.set(131, ty - 6, EDGE)

# ----------------------------------------------------- glowing windows
for y in range(44, 112):
    for x in range(96, 176):
        if not stone[y][x]:
            continue
        if (x % 4 == 1 and y % 5 == 2) or (x % 7 == 3 and y % 6 == 4):
            r, g, b, _ = src[y][x]
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            if lum < 130:
                out.set(x, y, EMBER if hsh(x, y, 5) > 0.35 else EMBER2)
                if y + 1 < H and stone[y + 1][x] and hsh(x, y, 7) > 0.55:
                    out.set(x, y + 1, BLOOD)

# great gate: a small burning arch at the castle foot
gy = 109
for x in range(123, 140):
    for y in range(gy - 10, gy + 1):
        if stone[y][x]:
            out.set(x, y, (26, 13, 16, 255))
out.path("M127 %d L127 %d Q131 %d 135 %d L135 %d Z" % (gy, gy - 6, gy - 10, gy - 6, gy),
         (104, 20, 18, 255))
out.path("M128 %d L128 %d Q131 %d 134 %d L134 %d Z" % (gy, gy - 5, gy - 9, gy - 5, gy),
         (214, 72, 28, 255))
out.path("M129 %d L129 %d Q131 %d 133 %d L133 %d Z" % (gy, gy - 5, gy - 8, gy - 5, gy),
         (255, 146, 56, 255))
out.set(131, gy - 4, EMBER2)
out.set(131, gy - 3, EMBER2)
# light spilling onto the ground before the gate
for y in range(gy + 1, gy + 5):
    sp = (y - gy)
    for x in range(131 - 2 - sp, 131 + 3 + sp):
        if 0 <= x < W:
            r0, g0, b0, _ = px(out, x, y)
            k = 0.55 - 0.12 * sp
            out.set(x, y, (clamp(r0 + (255 - r0) * k),
                           clamp(g0 + (130 - g0) * k),
                           clamp(b0 + (50 - b0) * k), 255))

# ------------------------------------------------------------- bats
def bat(x, y, s=1):
    if s == 1:
        out.set(x, y, VOID)
        out.set(x - 1, y - 1, VOID)
        out.set(x + 1, y - 1, VOID)
    else:
        out.set(x, y, VOID)
        out.set(x, y - 1, VOID)
        out.line(x - 2, y - 1, x - 1, y, VOID)
        out.line(x + 1, y, x + 2, y - 1, VOID)
        out.set(x - 3, y - 2, VOID)
        out.set(x + 3, y - 2, VOID)


bat(100, 30, 2)
bat(156, 20, 2)
bat(112, 12, 1)
bat(146, 38, 1)
bat(170, 34, 1)
bat(88, 46, 2)

# ------------------------------------------- embers drifting in the air
for i in range(150):
    x = int(hsh(i, 1, 11) * 256)
    y = int(hsh(i, 2, 13) * 110)
    if stone[y][x]:
        continue
    v = hsh(i, 3, 17)
    if v > 0.72:
        out.set(x, y, EMBER2)
    elif v > 0.34:
        out.set(x, y, EMBER)
    else:
        out.set(x, y, BLOOD)

view(out)
finish(out)
