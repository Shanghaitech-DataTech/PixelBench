import math
from math import cos, sin, radians, pi, hypot

W, H = 256, 256
CX, CY = 128, 100

# ---------- palette ----------
PAL = {
    'bg0':  '#05040a', 'bg1':  '#08070f', 'bg2':  '#0c0a14', 'bg3':  '#100d1a',
    'bg4':  '#151020', 'bg5':  '#191326', 'bg6':  '#161020', 'bg7':  '#110c18',
    'bg8':  '#0c0810', 'bg9':  '#08050b',
    'hall_dark':  '#0a0710', 'hall_mid':  '#140e1c', 'hall_light': '#241a30',
    'aura0': '#160e16', 'aura1': '#1f121e', 'aura2': '#291624', 'aura3': '#351a26',
    'stone_dark':  '#221b26', 'stone_mid':  '#392f40', 'stone_light': '#504458',
    'stone_hi':    '#6e607a',
    'floor':  '#0b080e', 'shadow': '#060409',
    'brass_dark':  '#2e1f0e', 'brass_mid':  '#6a4a1a', 'brass_light': '#a6782c',
    'brass_bright': '#d9a441', 'brass_hi': '#f2cd72', 'brass_shadow': '#1c1207',
    'outline': '#0c0704',
    'rune_cyan':   '#55e8e0', 'rune_amber': '#ffb63d', 'rune_violet': '#d86af0',
    'rune_blue':   '#5a9cff', 'rune_green': '#6aff9a', 'rune_pink': '#ff6aa0',
    'crystal_cyan':  '#5ad4e8', 'crystal_cyan_dark':  '#2a6a7c', 'crystal_cyan_hi':  '#b8f4ff',
    'crystal_violet':'#a86ae8', 'crystal_violet_dark':'#4a2a78', 'crystal_violet_hi':'#dcc0ff',
    'crystal_amber': '#ffb84a', 'crystal_amber_dark': '#8a4a12', 'crystal_amber_hi': '#ffe2a0',
    'crystal_green': '#6ae88a', 'crystal_green_dark': '#2a6a3a', 'crystal_green_hi': '#c8ffd8',
    'core_deep':  '#7a2408', 'core_orange': '#c8400e', 'core_amber': '#f28c1e',
    'core_yellow':'#ffd24a', 'core_white': '#fff6d8',
    'steel_dark': '#1c1c26', 'steel_mid': '#3a3a4a', 'steel_light': '#6a6a82',
}

c_bg = new_canvas(W, H, name='bg')
for name, hexv in PAL.items():
    c_bg.color(hexv, name)

# ---------- helpers ----------
def thick_line(c, x0, y0, x1, y1, color, w=3):
    dx = x1 - x0
    dy = y1 - y0
    L = hypot(dx, dy)
    if L == 0:
        c.set(round(x0), round(y0), color)
        return
    px = -dy / L
    py = dx / L
    for i in range(w):
        off = i - (w - 1) / 2.0
        c.line(round(x0 + px * off), round(y0 + py * off),
               round(x1 + px * off), round(y1 + py * off), color)

def pol(r, deg):
    a = radians(deg)
    return (CX + r * cos(a), CY + r * sin(a))

# ---------- rune glyphs ----------
RUNE_PLUS = [(-1,0),(0,-1),(0,0),(0,1),(1,0)]
RUNE_DIAG = [(-1,-1),(0,0),(1,1)]
RUNE_TRI  = [(0,-1),(0,0),(-1,1),(0,1),(1,1)]
RUNE_L    = [(0,-1),(0,0),(0,1),(1,1)]
RUNE_H    = [(-1,-1),(1,-1),(-1,0),(1,0),(-1,1),(1,1)]
RUNE_X    = [(-1,-1),(1,-1),(0,0),(-1,1),(1,1)]
RUNES = [RUNE_PLUS, RUNE_DIAG, RUNE_TRI, RUNE_L, RUNE_H, RUNE_X]
RUNE_COLORS = ['rune_cyan', 'rune_amber', 'rune_violet', 'rune_blue', 'rune_green', 'rune_pink']

def draw_rune(c, x, y, pattern, color, outline='outline'):
    pts = set()
    for dx, dy in pattern:
        pts.add((x + dx, y + dy))
    neigh = set()
    for px, py in pts:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                q = (px + dx, py + dy)
                if q not in pts:
                    neigh.add(q)
    for q in neigh:
        c.set(q[0], q[1], outline)
    for p in pts:
        c.set(p[0], p[1], color)

def draw_sphere(c, x, y, r, body, dark, hi):
    c.circle(round(x), round(y), r + 1, 'outline', fill=False)
    c.circle(round(x), round(y), r, body, fill=True)
    ox = max(1, r // 3)
    oy = max(1, r // 3)
    c.circle(round(x + ox), round(y + oy), max(1, r - 2), dark, fill=True)
    c.circle(round(x - ox), round(y - oy), max(1, r // 4), hi, fill=True)

def draw_gear(c, x, y, r, n, color, hub, hi):
    for i in range(n):
        a = 2 * pi * i / n
        for rr in (r + 1, r + 2):
            tx = round(x + cos(a) * rr)
            ty = round(y + sin(a) * rr)
            c.set(tx, ty, color)
    c.circle(round(x), round(y), r, color, fill=True)
    c.circle(round(x), round(y), r, 'outline', fill=False)
    c.circle(round(x), round(y), max(2, r - 3), hub, fill=True)
    c.circle(round(x), round(y), 1, hi, fill=True)

def draw_dial(c, x, y, r, face, rim, tick):
    c.circle(x, y, r + 1, 'outline', fill=False)
    c.circle(x, y, r, face, fill=True)
    c.circle(x, y, r, rim, fill=False)
    c.circle(x, y, max(1, r - 3), 'outline', fill=False)
    for deg in range(0, 360, 45):
        a = radians(deg)
        c.line(round(x + cos(a) * max(1, r - 4)), round(y + sin(a) * max(1, r - 4)),
               round(x + cos(a) * (r - 1)), round(y + sin(a) * (r - 1)), tick)
    c.line(x, y, round(x + cos(radians(210)) * max(1, r - 5)),
           round(y + sin(radians(210)) * max(1, r - 5)), 'core_yellow')

# ---------- background ----------
band = 26
for i in range(10):
    bh = min(band, H - i * band)
    if bh > 0:
        c_bg.rect(0, i * band, W, bh, f'bg{i}')

# hall pillars
c_bg.rect(0, 0, 22, H, 'hall_dark')
c_bg.rect(234, 0, 22, H, 'hall_dark')
c_bg.rect(22, 0, 2, H, 'hall_light')
c_bg.rect(232, 0, 2, H, 'hall_light')
c_bg.rect(4, 0, 2, H, 'hall_mid')
c_bg.rect(238, 0, 2, H, 'hall_mid')

# aura behind orrery
for r, col in [(95, 'aura0'), (85, 'aura1'), (75, 'aura2'), (65, 'aura3')]:
    c_bg.circle(CX, CY, r, col, fill=True)

# floating magical glints
glints = [
    (30, 60, 'rune_cyan'), (220, 70, 'rune_amber'), (42, 152, 'rune_violet'),
    (212, 150, 'rune_blue'), (58, 28, 'rune_amber'), (194, 40, 'rune_cyan'),
    (90, 18, 'rune_pink'), (172, 24, 'rune_green'), (52, 100, 'rune_green'),
    (208, 108, 'rune_pink'), (34, 192, 'brass_hi'), (222, 196, 'brass_hi'),
]
for gx, gy, col in glints:
    c_bg.set(gx, gy, col)

# floor + pedestal shadow
c_bg.rect(0, 244, W, 12, 'floor')
c_bg.ellipse(CX, 250, 92, 9, 'shadow', fill=True)

# stone pedestal
c_bg.rect(40, 244, 176, 12, 'stone_dark')
c_bg.rect(40, 244, 176, 12, 'outline', fill=False)
c_bg.rect(48, 236, 160, 8, 'stone_mid')
c_bg.rect(48, 236, 160, 8, 'outline', fill=False)
c_bg.poly([(70, 204), (186, 204), (200, 236), (56, 236)], 'stone_mid')
c_bg.poly([(70, 204), (186, 204), (200, 236), (56, 236)], 'outline', fill=False)
c_bg.rect(62, 196, 132, 8, 'stone_light')
c_bg.rect(62, 196, 132, 8, 'outline', fill=False)
# pedestal highlights
c_bg.line(73, 206, 59, 234, 'stone_hi')
c_bg.line(75, 206, 64, 232, 'stone_light')
c_bg.line(64, 198, 66, 234, 'stone_hi')
c_bg.line(50, 238, 44, 250, 'stone_hi')
c_bg.line(42, 246, 44, 253, 'stone_hi')

# carved runes on pillar
for k, (rx, ry) in enumerate([(100, 214), (122, 222), (140, 222), (158, 214)]):
    draw_rune(c_bg, rx, ry, RUNES[(k + 2) % len(RUNES)], 'stone_hi', outline='stone_dark')

# ---------- spokes ----------
c_spokes = new_canvas(W, H, name='spokes')
for deg in range(0, 360, 45):
    x0, y0 = pol(14, deg)
    x1, y1 = pol(90, deg)
    thick_line(c_spokes, x0, y0, x1, y1, 'brass_dark', 3)
    thick_line(c_spokes, x0, y0, x1, y1, 'brass_light', 1)
for deg in range(22, 360, 45):
    x0, y0 = pol(20, deg)
    x1, y1 = pol(88, deg)
    thick_line(c_spokes, x0, y0, x1, y1, 'brass_shadow', 1)

# ---------- rings ----------
c_rings = new_canvas(W, H, name='rings')
rings = [
    (88, 6, 'brass_mid'),
    (76, 5, 'brass_light'),
    (64, 5, 'brass_mid'),
    (52, 5, 'brass_light'),
    (40, 4, 'brass_mid'),
    (28, 4, 'brass_bright'),
]
for idx, (r, w, fill) in enumerate(rings):
    # annulus
    c_rings.circle(CX, CY, r, fill, fill=True)
    c_rings.circle(CX, CY, r - w, None, fill=True)
    # edges
    c_rings.circle(CX, CY, r, 'outline', fill=False)
    c_rings.circle(CX, CY, r - w, 'outline', fill=False)
    # highlight
    c_rings.circle(CX, CY, r - 1, 'brass_hi', fill=False)
    # engraved midline
    mid = r - w // 2
    c_rings.circle(CX, CY, mid, 'brass_shadow', fill=False)
    # radial engraved ticks
    step = 20 if r > 50 else 30
    for deg in range(0, 360, step):
        a = radians(deg)
        c_rings.line(round(CX + cos(a) * (r - w + 1)), round(CY + sin(a) * (r - w + 1)),
                     round(CX + cos(a) * (r - 1)), round(CY + sin(a) * (r - 1)), 'brass_shadow')

# inner core ring
c_rings.circle(CX, CY, 24, 'brass_hi', fill=False)

# runes along rings
ring_mids = [r - w // 2 for r, w, _ in rings]
rune_angles = [
    [15, 90, 165, 240, 315],
    [45, 135, 225, 315],
    [20, 110, 200, 290],
    [0, 90, 180, 270],
    [60, 150, 240, 330],
    [30, 150, 270],
]
ri = 0
for ring_idx, angles in enumerate(rune_angles):
    mid = ring_mids[ring_idx]
    for angle in angles:
        x, y = pol(mid, angle)
        pat = RUNES[ri % len(RUNES)]
        col = RUNE_COLORS[(ri + ring_idx) % len(RUNE_COLORS)]
        draw_rune(c_rings, round(x), round(y), pat, col)
        ri += 1

# ---------- details ----------
c_details = new_canvas(W, H, name='details')

# bold dark outer outline around instrument
c_details.circle(CX, CY, 89, 'outline', fill=False)
c_details.circle(CX, CY, 90, 'outline', fill=False)

# orbiting crystal spheres
spheres = [
    (85, 20, 6, 'crystal_cyan', 'crystal_cyan_dark', 'crystal_cyan_hi'),
    (74, 120, 5, 'crystal_violet', 'crystal_violet_dark', 'crystal_violet_hi'),
    (62, 210, 6, 'crystal_amber', 'crystal_amber_dark', 'crystal_amber_hi'),
    (50, 300, 5, 'crystal_green', 'crystal_green_dark', 'crystal_green_hi'),
    (38, 60, 4, 'crystal_violet', 'crystal_violet_dark', 'crystal_violet_hi'),
    (85, 200, 5, 'crystal_amber', 'crystal_amber_dark', 'crystal_amber_hi'),
]
for mid, ang, r, body, dark, hi in spheres:
    x, y = pol(mid, ang)
    draw_sphere(c_details, x, y, r, body, dark, hi)

# gears
gears = [
    (85, 135, 8, 10, 'brass_mid', 'brass_dark', 'brass_hi'),
    (74, 315, 7, 8, 'steel_mid', 'steel_dark', 'steel_light'),
    (62, 0, 7, 10, 'brass_light', 'brass_dark', 'brass_hi'),
    (50, 225, 6, 8, 'steel_light', 'steel_dark', 'steel_mid'),
    (85, 90, 8, 10, 'brass_mid', 'brass_dark', 'brass_hi'),
]
for mid, ang, r, n, col, hub, hi in gears:
    x, y = pol(mid, ang)
    draw_gear(c_details, x, y, r, n, col, hub, hi)

# alchemical dials
draw_dial(c_details, 128, 168, 9, 'brass_dark', 'brass_light', 'brass_hi')
draw_dial(c_details, 128, 32, 7, 'steel_dark', 'steel_light', 'steel_light')

# central radiant core
core = [(22, 'core_deep'), (18, 'core_orange'), (14, 'core_amber'), (10, 'core_yellow'), (6, 'core_white')]
for r, col in core:
    c_details.circle(CX, CY, r, col, fill=True)
for deg in range(0, 360, 15):
    a = radians(deg)
    c_details.line(round(CX + cos(a) * 10), round(CY + sin(a) * 10),
                   round(CX + cos(a) * 20), round(CY + sin(a) * 20), 'core_yellow')
c_details.circle(CX, CY, 23, 'outline', fill=False)

# ---------- compose ----------
result = flatten([c_bg, c_spokes, c_rings, c_details], name='result')
print(result.stats_text())
print('colors used:', len(result.palette()))
finish(result)
