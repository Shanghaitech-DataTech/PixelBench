import math
from pixelbench_api import new_canvas, finish

TWO_PI = 6.283185307179586
c = new_canvas(256, 256, name="arcane-instrument-giant")

PAL = {
    'bg0': (4, 5, 10), 'bg1': (10, 12, 19), 'bg2': (15, 18, 27), 'bg3': (21, 24, 35),
    'std': (27, 29, 37), 'stl': (38, 41, 52), 'sth': (58, 63, 80),
    'ink': (12, 8, 4), 'bronze': (52, 36, 14), 'bd': (78, 56, 20), 'brass': (122, 90, 36),
    'bl': (172, 134, 64), 'bh': (226, 186, 110), 'gold': (255, 224, 140),
    'copper': (162, 94, 44), 'sd': (58, 60, 72), 'st': (106, 112, 128), 'sl': (166, 176, 192),
    'ws': (88, 72, 50), 'wsh': (124, 100, 66), 'wsl': (158, 132, 90),
    'cd': (16, 34, 84), 'cm': (38, 78, 156), 'cl': (98, 152, 228), 'ch': (164, 218, 255),
    'cw': (230, 250, 255),
    'rd': (0, 116, 140), 'rn': (0, 198, 220), 'rh': (132, 255, 250),
    'mg': (178, 74, 228), 'mh': (244, 150, 255),
    'k0': (118, 46, 14), 'k1': (186, 86, 20), 'k2': (244, 142, 32),
    'k3': (255, 200, 94), 'k4': (255, 242, 182), 'k5': (255, 255, 248),
    'amb': (32, 21, 12), 'amb2': (50, 32, 16),
}
for k, v in PAL.items():
    c.color(v, k)


def earc(cx, cy, rx, ry, a0, a1, color, angle=0.0):
    steps = max(150, int(6.3 * max(rx, ry)))
    ca = math.cos(angle)
    sa = math.sin(angle)
    for i in range(steps + 1):
        a = a0 + (a1 - a0) * i / steps
        ex = rx * math.cos(a)
        ey = ry * math.sin(a)
        c.set(int(cx + ex * ca - ey * sa), int(cy + ex * sa + ey * ca), color)


def eout(cx, cy, rx, ry, color, angle=0.0):
    earc(cx, cy, rx, ry, 0.0, TWO_PI, color, angle)


def ring_tube(cx, cy, rx, ry, thick, ramp, angle=0.0, out='ink'):
    steps = max(240, int(6.3 * max(rx, ry)))
    ca = math.cos(angle)
    sa = math.sin(angle)
    n = len(ramp)
    for i in range(steps):
        a = TWO_PI * i / steps
        ex = rx * math.cos(a)
        ey = ry * math.sin(a)
        xi = int(round(cx + ex * ca - ey * sa))
        yi = int(round(cy + ex * sa + ey * ca))
        b = 0.5 - 0.36 * math.sin(a) - 0.14 * math.cos(a)
        idx = max(0, min(n - 1, int(b * n)))
        c.circle(xi, yi, thick, out)
        c.circle(xi, yi, thick - 1, ramp[idx])


def engrave(cx, cy, r, dark='bd', hi='bh'):
    eout(cx, cy, r, r, dark)
    eout(cx, cy - 1, r - 1, r - 1, hi)


GLYPHS = [
    ["101", "111", "101", "111", "101"],
    ["011", "101", "111", "101", "110"],
    ["111", "001", "010", "100", "111"],
    ["101", "010", "111", "010", "101"],
    ["111", "001", "111", "001", "111"],
    ["010", "111", "101", "111", "010"],
    ["111", "101", "111", "101", "111"],
    ["001", "010", "100", "010", "001"],
]


def glyph(x, y, g, col='rn', hi='rh'):
    dots = GLYPHS[g % len(GLYPHS)]
    for i, row in enumerate(dots):
        for j, ch in enumerate(row):
            if ch == '1':
                c.set(x - 1 + j, y - 2 + i, col)
    for j, ch in enumerate(GLYPHS[g % len(GLYPHS)][0]):
        if ch == '1':
            c.set(x - 1 + j, y - 2, hi)


def crystal(x, y, r):
    c.circle(x, y, r + 1, 'ink')
    c.circle(x, y, r, 'cd')
    c.circle(x + 2, y + 2, max(1, int(r * 0.8)), 'cm')
    c.circle(x - 1, y - 2, max(1, int(r * 0.55)), 'cl')
    c.circle(x - 2, y - 3, max(1, int(r * 0.34)), 'ch')
    c.circle(x - 3, y - 4, max(1, int(r * 0.16)), 'cw')
    c.set(x - 3 - int(r * 0.35), y - 4 - int(r * 0.4), 'cw')


def gear(x, y, r, teeth, body='brass', rim='bd'):
    c.circle(x, y, r + 2, 'ink')
    for i in range(teeth):
        a = TWO_PI * i / teeth
        px = int(round(x + (r + 1) * math.cos(a)))
        py = int(round(y + (r + 1) * math.sin(a)))
        c.circle(px, py, 2, body)
    c.circle(x, y, r, body)
    c.circle(x, y, r - 2, rim)
    for i in range(5):
        a = TWO_PI * i / 5
        x0 = int(round(x + (r - 3) * math.cos(a)))
        y0 = int(round(y + (r - 3) * math.sin(a)))
        c.line(x, y, x0, y0, rim)
    c.circle(x, y, max(1, int(r * 0.42)), 'ink')
    c.circle(x, y, max(1, int(r * 0.38)), 'st')
    c.circle(x, y, max(1, int(r * 0.14)), 'ink')


def dial(x, y, r):
    c.circle(x, y, r + 1, 'ink')
    c.circle(x, y, r, 'bh')
    for i in range(20):
        a = TWO_PI * i / 20
        x1 = int(round(x + (r - 1) * math.cos(a)))
        y1 = int(round(y + (r - 1) * math.sin(a)))
        c.set(x1, y1, 'ink')
    for i in range(10):
        a = TWO_PI * i / 10
        x1 = int(round(x + (r - 4) * math.cos(a)))
        y1 = int(round(y + (r - 4) * math.sin(a)))
        c.set(x1, y1, 'bd')
    na = -0.5
    c.line(x, y, int(round(x + (r) * math.cos(na))), int(round(y + (r) * math.sin(na))), 'ink')
    c.circle(x, y, 3, 'st')
    c.circle(x, y, 1, 'ink')


# ----------------------------------------------------------------------
# BACKGROUND HALL
# ----------------------------------------------------------------------
c.rect(0, 0, 256, 256, 'bg0')
c.circle(128, 112, 118, 'bg1')
c.circle(128, 108, 94, 'bg2')
c.circle(128, 104, 72, 'bg3')

# columns
for sx in (12, 220):
    c.rect(sx, 0, 24, 256, 'std')
    c.rect(sx, 2, 1, 256, 'stl')
    c.rect(sx + 22, 0, 2, 256, 'stl')
    for yy in range(0, 234, 20):
        c.rect(sx + 4, yy, 18, 1, 'bg0')
# arch
earc(128, 44, 120, 96, math.pi, TWO_PI, 'std')
earc(128, 44, 116, 88, math.pi, TWO_PI, 'stl')
earc(128, 44, 113, 84, math.pi, TWO_PI, 'st')
# floor
c.rect(0, 246, 256, 10, 'bg2')
c.rect(0, 246, 256, 1, 'stl')
for i in range(9):
    c.rect(4 + i * 32, 246, 1, 10, 'std')
# light pool on floor
c.ellipse(128, 250, 120, 16, 'amb')
c.ellipse(128, 252, 88, 11, 'amb2')

# ----------------------------------------------------------------------
# PEDESTAL
# ----------------------------------------------------------------------
c.rect(86, 220, 84, 20, 'std')
c.rect(86, 220, 84, 20, 'ink', fill=False)
c.rect(78, 238, 100, 8, 'std')
c.rect(78, 238, 100, 8, 'ink', fill=False)
c.rect(70, 244, 116, 12, 'st')
c.rect(70, 244, 116, 12, 'ink', fill=False)
c.rect(70, 244, 116, 1, 'sl')
c.rect(96, 210, 64, 3, 'ink')
c.rect(96, 226, 64, 2, 'stl')
c.ellipse(128, 214, 74, 11, 'ink')
c.ellipse(128, 212, 70, 9, 'ws')
c.ellipse(128, 210, 62, 7, 'wsh')
c.ellipse(128, 208, 50, 5, 'ink')
c.ellipse(128, 207, 42, 4, 'wsl')
glyph(128, 208, 2, 'bd', 'bh')
c.ellipse(128, 206, 34, 3, 'bg0')

# energy column between instrument and pedestal
for yy in range(148, 208, 6):
    w = 5 + (yy - 148) // 12
    c.rect(128 - w, yy, 2 * w, 5, 'amb2')
c.rect(123, 148, 10, 54, 'amb2')
c.rect(125, 154, 6, 44, 'k0')
c.rect(126, 160, 4, 34, 'k1')

# rays from core (behind)
for i in range(18):
    a = TWO_PI * i / 18
    c.line(128, 106, int(128 + 116 * math.cos(a)), int(106 + 116 * math.sin(a)), 'k0')
    c.line(128, 106, int(128 + 86 * math.cos(a)), int(106 + 86 * math.sin(a)), 'k1')
c.circle(128, 106, 30, 'k0')
c.circle(128, 106, 22, 'k1')

# ----------------------------------------------------------------------
# BACK RINGS
# ----------------------------------------------------------------------
BRASS_RAMP = ['bronze', 'bd', 'brass', 'bl', 'bh']
BRIGHT = ['bronze', 'brass', 'bl', 'bh', 'gold']

ring_tube(128, 102, 92, 34, 5, BRASS_RAMP, 0.62)
ring_tube(128, 100, 60, 21, 4, BRASS_RAMP, -0.35)

# back orbit crystals
for (px, py, pr) in [(62, 74, 12), (194, 70, 10), (188, 140, 11), (66, 136, 10)]:
    crystal(px, py, pr)
small_orb = [(128, 52, 6), (52, 106, 7), (204, 106, 6), (128, 160, 6)]
for (px, py, pr) in small_orb:
    crystal(px, py, pr)

gear(128, 128, 26, 13, 'bd')
gear(104, 66, 11, 9, 'brass')
gear(150, 136, 10, 8, 'copper')

# spokes
for i in range(6):
    a = TWO_PI * i / 6
    c.line(int(128 + 22 * math.cos(a)), int(106 + 22 * math.sin(a)),
          int(128 + 62 * math.cos(a)), int(106 + 62 * math.sin(a)), 'bd')
    c.line(int(128 + 16 * math.cos(a)) + 1, int(106 + 16 * math.sin(a)) + 1,
          int(128 + 60 * math.cos(a)) + 1, int(106 + 60 * math.sin(a)) + 1, 'bl')

# ----------------------------------------------------------------------
# OUTER FRONT RING
# ----------------------------------------------------------------------
ring_tube(128, 106, 99, 99, 3, BRIGHT)
# ticks
for i in range(72):
    a = TWO_PI * i / 72
    c.set(int(128 + 96 * math.cos(a)), int(106 + 96 * math.sin(a)), 'bd')
for i in range(12):
    a = TWO_PI * i / 12
    c.set(int(128 + 100 * math.cos(a)), int(106 + 100 * math.sin(a)), 'bh')
engrave(128, 106, 90)
engrave(128, 106, 84)

# outer-zone gears bridging rings
gear(150, 152, 9, 8, 'copper')
gear(104, 58, 9, 8, 'brass')
gear(60, 126, 8, 8, 'bronze')
gear(196, 128, 8, 8, 'copper')

# ----------------------------------------------------------------------
# MAIN FRONT RING + ENGRAVING + RUNES
# ----------------------------------------------------------------------
ring_tube(128, 106, 78, 78, 5, BRASS_RAMP)
# ticks
for i in range(48):
    a = TWO_PI * i / 48
    c.set(int(128 + 72 * math.cos(a)), int(106 + 72 * math.sin(a)), 'bd')
for i in range(12):
    a = TWO_PI * i / 12
    c.set(int(128 + 75 * math.cos(a)), int(106 + 75 * math.sin(a)), 'bh')
engrave(128, 106, 68)
engrave(128, 106, 56)
ring_tube(128, 106, 34, 34, 2, BRIGHT)
earc(128, 106, 60, 60, 0.0, TWO_PI, 'rd')
eout(128, 105, 58, 58, 'rh')

# runes on main ring
for i, a in enumerate([20, 62, 104, 146, 188, 230, 272, 314]):
    px = int(128 + 62 * math.cos(math.radians(a)))
    py = int(106 + 62 * math.sin(math.radians(a)))
    c.circle(px, py, 4, 'rd')
    glyph(px, py, i, 'rn', 'rh')
# runes on outer ring
for i, a in enumerate([0, 45, 90, 135, 180, 225, 270, 315]):
    px = int(128 + 87 * math.cos(math.radians(a)))
    py = int(106 + 87 * math.sin(math.radians(a)))
    c.circle(px, py, 4, 'rd')
    glyph(px, py, (i + 4), 'rn', 'rh')

# side dials and small gears
dial(128, 44, 10)
dial(128, 168, 9)
dial(58, 62, 7)
dial(198, 152, 7)
dial(58, 150, 7)
dial(198, 60, 7)

# front crossing ring
ring_tube(128, 104, 86, 26, 5, BRASS_RAMP, -0.5)
eout(128, 100, 74, 18, 'bd', -0.5)
eout(128, 99, 70, 14, 'bh', -0.5)

# ----------------------------------------------------------------------
# CORE
# ----------------------------------------------------------------------
c.circle(128, 106, 18, 'k2')
c.circle(128, 106, 12, 'k3')
c.circle(128, 106, 7, 'k4')
c.circle(128, 106, 4, 'k5')
c.circle(128, 106, 2, 'k5')

# radiance sparkles
for i in range(14):
    a = TWO_PI * i / 14
    c.line(128, 106, int(128 + 40 * math.cos(a)), int(106 + 40 * math.sin(a)), 'k3')
    c.line(128, 106, int(128 + 30 * math.cos(a)), int(106 + 30 * math.sin(a)), 'k4')
c.set(127, 105, 'k5')
c.set(129, 107, 'k5')

# floating motes
for i in range(40):
    a = i * 1.93
    r = 30 + (i * 17) % 96
    px = int(128 + r * math.cos(a))
    py = int(106 + r * math.sin(a))
    if i % 3 == 0:
        c.set(px, py, 'amb2')
    else:
        c.set(px, py, 'k0')

# ----------------------------------------------------------------------
print(c.stats_text())
finish(c)
