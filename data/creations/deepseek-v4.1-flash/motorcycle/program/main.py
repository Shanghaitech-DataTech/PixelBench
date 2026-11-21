import math

W = H = 128
c = new_canvas(W, H, name="motorcycle")

COLS = [
    ("tire",      '#15171a'),
    ("tire_lo",   '#090a0b'),
    ("tire_hi",   '#2a2e33'),
    ("rim",       '#787d84'),
    ("rim_lo",    '#4a4e54'),
    ("spoke",     '#eef1f4'),
    ("silver",    '#b6bbc1'),
    ("silver_hi", '#dfe4e9'),
    ("silver_lo", '#81868d'),
    ("body",      '#1a1c1f'),
    ("body_hi",   '#2c3036'),
    ("fair",      '#3b4046'),
    ("fair_hi",   '#4d535a'),
    ("fair_lo",   '#272b30'),
    ("red",       '#c8202b'),
    ("red_hi",    '#e8454f'),
    ("red_lo",    '#8b1119'),
    ("glass",     '#1c2229'),
    ("glass_hi",  '#39424c'),
    ("engine",    '#9aa0a7'),
    ("engine_hi", '#c7cdd3'),
    ("engine_lo", '#6c7279'),
]
for n, hx in COLS:
    c.color(hx, name=n)


def P(pts, col):
    c.poly([(float(x), float(y)) for x, y in pts], col)


def thick(p0, p1, w, col, cap=False):
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L * w / 2.0, dx / L * w / 2.0
    c.poly([(x0 + nx, y0 + ny), (x1 + nx, y1 + ny),
            (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)], col)
    if cap:
        c.circle(int(round(x0)), int(round(y0)), max(1, int(w / 2)), col)
        c.circle(int(round(x1)), int(round(y1)), max(1, int(w / 2)), col)


def arc_band(cx, cy, r_in, r_out, a0, a1, col):
    A0, A1 = math.radians(a0), math.radians(a1)
    p0o = (cx + r_out * math.cos(A0), cy + r_out * math.sin(A0))
    p1o = (cx + r_out * math.cos(A1), cy + r_out * math.sin(A1))
    p1i = (cx + r_in * math.cos(A1), cy + r_in * math.sin(A1))
    p0i = (cx + r_in * math.cos(A0), cy + r_in * math.sin(A0))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 1 if a1 > a0 else 0
    d = ("M %.2f %.2f A %.2f %.2f 0 %d %d %.2f %.2f L %.2f %.2f "
         "A %.2f %.2f 0 %d %d %.2f %.2f Z" % (
             p0o[0], p0o[1], r_out, r_out, large, sweep, p1o[0], p1o[1],
             p1i[0], p1i[1], r_in, r_in, large, 1 - sweep, p0i[0], p0i[1]))
    c.path(d, col)


def wheel(cx, cy, R, rimR):
    d = ("M %d %d A %d %d 0 1 0 %d %d A %d %d 0 1 0 %d %d Z "
         "M %d %d A %d %d 0 1 0 %d %d A %d %d 0 1 0 %d %d Z") % (
             cx - R, cy, R, R, cx + R, cy, R, R, cx - R, cy,
             cx - rimR, cy, rimR, rimR, cx + rimR, cy, rimR, rimR, cx - rimR, cy)
    c.path(d, 'tire')
    c.circle(cx, cy, R, 'tire_lo', fill=False)
    arc_band(cx, cy, R - 3, R - 1, 192, 302, 'tire_hi')
    arc_band(cx, cy, R - 0.6, R + 0.9, 192, 302, 'tire_lo')
    for i in range(5):
        a = math.radians(-90 + i * 72)
        x0 = cx + math.cos(a) * 3.6
        y0 = cy + math.sin(a) * 3.6
        x1 = cx + math.cos(a) * (rimR - 0.4)
        y1 = cy + math.sin(a) * (rimR - 0.4)
        thick((x0, y0), (x1, y1), 1.9, 'spoke')
    arc_band(cx, cy, rimR - 1.0, rimR + 0.9, 0, 360, 'silver_lo')
    arc_band(cx, cy, rimR - 0.9, rimR + 0.2, 0, 360, 'rim')
    c.circle(cx, cy, 4, 'rim')
    c.circle(cx, cy, 4, 'rim_lo', fill=False)
    c.set(cx, cy, 'silver_hi')


# ---------------- wheels ----------------
RX, RY, RR = 29, 90, 18
FX, FY, FR = 98, 90, 18
wheel(RX, RY, RR, 11)
wheel(FX, FY, FR, 11)

# front fender (mostly under the fairing)
arc_band(FX, FY, 19.8, 23.6, 250, 352, 'fair')
arc_band(FX, FY, 20.4, 22.0, 256, 346, 'fair_hi')
arc_band(FX, FY, 22.2, 23.6, 250, 352, 'fair_lo')

# ---------------- swingarm / shock / hugger ----------------
thick((56, 85), (RX, RY), 6, 'silver_lo')
thick((56, 83), (RX, RY - 2), 1.6, 'silver')
thick((43, 59), (34, 73), 4, 'silver_lo')
for k in range(4):
    t = (k + 0.5) / 4.0
    x = 43 + (34 - 43) * t
    y = 59 + (73 - 59) * t
    c.line(int(x) - 2, int(y), int(x) + 2, int(y), 'silver')
arc_band(RX, RY, 19.5, 23, 210, 293, 'fair_lo')
arc_band(RX, RY, 22.2, 23.2, 210, 293, 'body_hi')

# ---------------- front fork ----------------
thick((93, 52), (98, 90), 5, 'silver')
thick((94, 54), (99, 88), 1.4, 'silver_hi')
thick((92, 52), (97, 90), 1.2, 'silver_lo')

# ---------------- engine block ----------------
P([(44, 52), (78, 50), (83, 76), (76, 93), (56, 95), (44, 88), (41, 68)], 'fair_lo')
P([(48, 86), (77, 85), (77, 94), (57, 96), (46, 93)], 'body')
for i in range(4):
    c.line(46, 63 + i * 3, 64, 60 + i * 3, 'body_hi')

# ---------------- frame ----------------
thick((75, 58), (71, 61), 5, 'silver')
thick((71, 61), (53, 80), 5, 'silver')
thick((75, 57), (71, 60), 1.5, 'silver_hi')
thick((71, 59), (53, 78), 1.5, 'silver_hi')
thick((74, 64), (60, 73), 2.6, 'silver_lo')
c.circle(53, 80, 4, 'silver_lo')
c.circle(53, 80, 4, 'silver', fill=False)
c.set(53, 80, 'silver_hi')

# ---------------- exhaust ----------------
thick((74, 91), (58, 88), 6, 'silver_lo')
thick((58, 88), (40, 71), 8, 'silver_lo')
thick((57, 86), (41, 70), 3, 'silver')
c.circle(40, 71, 4, 'silver_lo')
c.circle(40, 71, 3, 'silver')
c.set(40, 71, 'silver_hi')

# ---------------- round engine cover ----------------
c.circle(60, 76, 9, 'engine')
c.circle(60, 76, 9, 'engine_lo', fill=False)
arc_band(60, 76, 5.6, 8.3, 195, 320, 'engine_hi')
c.circle(60, 76, 5, 'engine')
c.circle(60, 76, 5, 'engine_lo', fill=False)
for i in range(6):
    a = math.radians(i * 60 + 30)
    c.set(int(round(60 + math.cos(a) * 7)), int(round(76 + math.sin(a) * 7)), 'engine_lo')
c.set(60, 76, 'silver_hi')

# ---------------- tail ----------------
P([(52, 46), (30, 38), (15, 36), (17, 49), (34, 60), (54, 62)], 'body')
P([(15, 37), (20, 38), (21, 48), (17, 49)], 'red')
P([(16, 38), (19, 37), (19, 40), (16, 42)], 'red_hi')
thick((23, 40), (50, 47), 1.6, 'red_lo')
c.path("M 16 38 L 30 40 L 51 47", 'body_hi', fill=False)
c.path("M 25 45 C 36 47 46 51 52 55", 'body_hi', fill=False)

# ---------------- seat ----------------
c.path("M 48 45 C 56 49 62 50 68 46 C 71 44 73 43 76 41 L 76 58 "
       "C 66 62 52 62 47 59 Z", 'body')
c.path("M 50 47 C 57 51 63 51 68 47", 'body_hi', fill=False)

# ---------------- tank ----------------
c.path("M 66 52 C 70 44 78 40 86 40 L 94 42 C 98 44 100 47 98 50 "
       "C 90 56 74 58 68 57 Z", 'body')
c.path("M 70 48 C 77 42 84 40 91 41", 'body_hi', fill=False)
P([(73, 45), (85, 41), (86, 45), (75, 49)], 'red_lo')

# ---------------- fairing ----------------
c.path("M 80 51 C 90 46 99 45 105 45 C 110 48 114 55 114 62 "
       "C 114 69 108 76 99 80 C 89 85 78 86 72 83 "
       "C 66 80 66 71 69 63 C 72 56 76 53 80 51 Z", 'fair')
c.path("M 82 52 C 91 47 99 47 104 47", 'fair_hi', fill=False)
c.path("M 71 82 C 79 85 89 84 98 79", 'fair_lo', fill=False)
c.path("M 107 47 C 111 51 113 57 113 62", 'fair_hi', fill=False)
c.path("M 72 83 C 79 86 89 85 98 80 C 96 85 85 89 77 88 C 72 87 70 86 72 83 Z", 'fair_lo')
c.path("M 70 68 C 78 72 88 72 97 68", 'fair_lo', fill=False)
c.path("M 74 62 C 84 59 96 61 106 68", 'fair_hi', fill=False)

# red accents on fairing
P([(101, 47), (111, 59), (107, 68), (97, 53)], 'red')
P([(102, 49), (109, 58), (107, 62), (100, 52)], 'red_hi')
thick((83, 80), (100, 75), 2, 'red_lo')
P([(107, 50), (113, 57), (113, 64), (109, 58)], 'silver_hi')

# ---------------- windscreen ----------------
P([(110, 48), (100, 45), (95, 30), (105, 33)], 'glass')
c.line(109, 46, 105, 34, 'glass_hi')
c.line(99, 44, 96, 32, 'glass_hi')


def dump(x0=0, y0=0, x1=W - 1, y1=H - 1, step=2):
    pal = c.palette()
    idxmap = {}
    syms = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    out = []
    hdr = "    "
    for x in range(x0, x1 + 1, step * 2):
        hdr += str((x // 10) % 10)
    out.append(hdr)
    hdr2 = "    "
    for x in range(x0, x1 + 1, step * 2):
        hdr2 += str(x % 10)
    out.append(hdr2)
    for y in range(y0, y1 + 1, step):
        row = []
        for x in range(x0, x1 + 1, step):
            i = c.get(x, y)
            if pal[i]['rgba'][3] == 0:
                row.append('.')
            else:
                if i not in idxmap:
                    idxmap[i] = syms[len(idxmap) % len(syms)]
                row.append(idxmap[i])
        out.append("%3d %s" % (y, ''.join(row)))
    print('\n'.join(out))
    print('legend:')
    for i, s in idxmap.items():
        print('  ', s, tuple(pal[i]['rgba']), pal[i]['name'])


print(c.stats_text())
dump(step=2)
print('---- nose 1:1 ----')
dump(88, 26, 120, 62, 1)
finish(c)
