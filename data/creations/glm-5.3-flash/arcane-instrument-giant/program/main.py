# arcane-instrument-giant : 256x256 pixel art
# A massive brass astrolabe-orrery floating over a stone pedestal in a dark hall.
from pixelbench_api import *
import math, random

random.seed(11)
W = H = 256
CX, CY = 128, 112            # instrument centre
c = new_canvas(W, H, background='#07060d', name='arcane-instrument-giant')

# ---------------------------------------------------------------- palette
PAL = [
    ('void', '#07060d'), ('hall_dark', '#0d0b18'), ('hall_mid', '#151226'),
    ('hall_hi', '#221c3a'), ('arch', '#2b2447'), ('arch_hi', '#3a3159'),
    ('floor_dark', '#100d1c'), ('floor_mid', '#1a1630'), ('floor_hi', '#2a2444'),
    ('floor_lit', '#3a3258'),
    ('stone_dark', '#2e2a3e'), ('stone_mid', '#454055'), ('stone_hi', '#6a6377'),
    ('stone_lit', '#8d8496'),
    ('iron_dark', '#1c1a26'), ('iron_mid', '#343140'),
    ('brass_dark', '#3a2a12'), ('brass_deep', '#5a3f16'), ('brass_mid', '#8a6420'),
    ('brass', '#c49432'), ('brass_hi', '#f0c860'), ('brass_spec', '#fff3c0'),
    ('copper', '#a45f2a'), ('copper_hi', '#d18a4a'),
    ('crystal_dk', '#123a44'), ('crystal', '#3fa8b8'), ('crystal_hi', '#8ff0f2'),
    ('crystal_sp', '#e8ffff'),
    ('violet_dk', '#2c1a4a'), ('violet', '#7a4fd0'), ('violet_hi', '#b48aff'),
    ('rune_dim', '#8a6a2a'), ('rune', '#ffd870'), ('rune_hot', '#fff6d8'),
    ('core_deep', '#8a3a10'), ('core', '#ffb028'), ('core_hi', '#ffe08a'),
    ('core_sp', '#ffffff'),
    ('glow_warm', '#4a2c10'), ('glow_cool', '#16283e'),
    ('shadow', '#050409'),
]
P = {}
for _n, _h in PAL:
    P[_n] = c.color(_h, name=_n)

BR_RAMP = ['brass_dark', 'brass_deep', 'brass_mid', 'brass', 'brass_hi', 'brass_spec']

# ---------------------------------------------------------------- helpers
def safe_set(x, y, col):
    if 0 <= x < W and 0 <= y < H:
        c.set(int(round(x)), int(round(y)), col)

def safe_line(x0, y0, x1, y1, col):
    x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        safe_set(x0, y0, col)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def disc(cx, cy, r, col):
    r2 = r * r
    for y in range(int(cy) - r, int(cy) + r + 1):
        for x in range(int(cx) - r, int(cx) + r + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r2:
                safe_set(x, y, col)

def ring_pts(r, n=360):
    return [(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n))
            for i in range(n)]

def engrave_circle(r, col, cx=CX, cy=CY):
    for x, y in ring_pts(r, max(24, int(2 * math.pi * r))):
        safe_set(cx + x, cy + y, col)

def radial_ticks(r0, r1, n, col, a0=0.0, a1=360.0):
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / float(n))
        safe_line(CX + r0 * math.cos(a), CY + r0 * math.sin(a),
                  CX + r1 * math.cos(a), CY + r1 * math.sin(a), col)

def ring_point(rx, ry, rot_deg, t_deg, cx=CX, cy=CY):
    a = math.radians(t_deg)
    ex, ey = rx * math.cos(a), ry * math.sin(a)
    ang = math.radians(rot_deg)
    ca, sa = math.cos(ang), math.sin(ang)
    return (cx + ex * ca - ey * sa, cy + ex * sa + ey * ca)

def shaded_annulus(r0, r1, ramp, rim_light=None):
    for y in range(CY - r1, CY + r1 + 1):
        for x in range(CX - r1, CX + r1 + 1):
            dx, dy = x - CX, y - CY
            d2 = dx * dx + dy * dy
            if d2 < r0 * r0 or d2 > r1 * r1:
                continue
            L = 1.0 - (math.sqrt(d2) - r0) / max(1e-6, (r1 - r0))
            if rim_light is not None:
                a = math.degrees(math.atan2(dy, dx)) % 360
                dd = abs((a - rim_light + 180) % 360 - 180)
                if dd < 80:
                    L += 0.4 * (1 - dd / 80.0)
            L = max(0.0, min(0.999, L))
            safe_set(x, y, P[ramp[int(L * len(ramp))]])

def tilted_band(rx, ry, ang_deg, w, ramp, dim_back=0.55):
    """Tilted elliptical band; inner edge lit, outer edge darkest."""
    ang = math.radians(ang_deg)
    ca, sa = math.cos(ang), math.sin(ang)
    n = max(160, int(2 * math.pi * max(rx, ry) * 2))
    for i in range(n):
        a = 2 * math.pi * i / n
        ex, ey = rx * math.cos(a), ry * math.sin(a)
        gx, gy = math.cos(a) / max(rx, 1e-6), math.sin(a) / max(ry, 1e-6)
        gl = math.hypot(gx, gy) or 1.0
        gx, gy = gx / gl, gy / gl
        L0 = 1.0 if math.sin(a) >= 0 else dim_back
        for t in range(w):
            L = max(0.0, min(0.999, L0 * (1.0 - t / float(max(1, w - 1)))))
            px = CX + (ex + gx * t) * ca - (ey + gy * t) * sa
            py = CY + (ex + gx * t) * sa + (ey + gy * t) * ca
            safe_set(px, py, P[ramp[int(L * len(ramp))]])

def ring_ticks(rx, ry, rot, n, col, a0=0.0, a1=360.0):
    for i in range(n):
        t = a0 + (a1 - a0) * i / float(n)
        x0, y0 = ring_point(rx - 1, ry - 1, rot, t)
        x1, y1 = ring_point(rx + 2, ry + 2, rot, t)
        safe_line(x0, y0, x1, y1, col)

RUNE_GLYPHS = [
    (' # ', '# #', ' # ', '# #', ' # '),
    ('#  ', '#  ', '###', '  #', '  #'),
    ('###', '  #', ' # ', '#  ', '###'),
    (' # ', '###', ' # ', ' # ', ' # '),
    ('#  ', '## ', '# #', ' ##', '  #'),
    (' # ', '# #', '# #', '# #', '###'),
    ('  #', ' ##', '# #', '## ', '#  '),
    ('# #', '# #', ' # ', '# #', '# #'),
]

def draw_rune(x, y, idx, col):
    g = RUNE_GLYPHS[idx % len(RUNE_GLYPHS)]
    for j, row in enumerate(g):
        for i, ch in enumerate(row):
            if ch == '#':
                safe_set(x + i, y + j, col)

def gear(cx, cy, r, teeth, body, dark, hi, rot=0.0, hub=2):
    for i in range(teeth):
        a = math.radians(rot + 360.0 * i / teeth)
        for t in (r + 2, r + 3):
            safe_set(cx + t * math.cos(a), cy + t * math.sin(a), P['shadow'])
    disc(cx, cy, r, P[body])
    for y in range(-r, r + 1):
        for x in range(-r, r + 1):
            if x * x + y * y <= r * r:
                if x + y < -r * 0.4:
                    safe_set(cx + x, cy + y, P[hi])
                elif x + y > r * 0.5:
                    safe_set(cx + x, cy + y, P[dark])
    for i in range(teeth):
        a = math.radians(rot + 360.0 * i / teeth)
        for t in (r + 1, r + 2):
            safe_set(cx + t * math.cos(a), cy + t * math.sin(a), P[body])
    for i in range(4):
        a = math.radians(rot + 90 * i + 45)
        for t in range(hub + 2, r - 1):
            for w in (-1, 0, 1):
                safe_set(cx + t * math.cos(a) - w * math.sin(a),
                         cy + t * math.sin(a) + w * math.cos(a), P[dark])
    disc(cx, cy, hub, P[dark])
    safe_set(cx, cy, P[hi])

def crystal_ball(cx, cy, r, dark, base, lit, sp):
    for y in range(int(cy) - r, int(cy) + r + 1):
        for x in range(int(cx) - r, int(cx) + r + 1):
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            if d2 <= r * r:
                dl = math.hypot(x - cx + r * 0.45, y - cy + r * 0.45) / max(1e-6, r)
                safe_set(x, y, lit if dl < 0.5 else (base if dl < 0.92 else dark))
    for i in range(-r + 1, r):
        safe_set(cx + i, cy, dark)
    sx, sy = cx - max(1, int(r * 0.45)), cy - max(1, int(r * 0.45))
    safe_set(sx, sy, sp)
    if r >= 4:
        safe_set(sx + 1, sy, sp)
        safe_set(sx, sy + 1, sp)
    for x, y in ring_pts(r, max(20, int(2 * math.pi * r))):
        safe_set(cx + x, cy + y, P['iron_dark'])

def dial(x, y, r, ring, face, needle, ang):
    disc(x, y, r, P[ring])
    disc(x, y, r - 1, P[face])
    for i in range(8):
        a = 2 * math.pi * i / 8
        safe_set(x + (r - 2) * math.cos(a), y + (r - 2) * math.sin(a), P[ring])
    safe_line(x, y, x + (r - 2) * math.cos(ang), y + (r - 2) * math.sin(ang), P[needle])
    safe_set(x, y, P['brass_hi'])

print('setup ok')

# ================================================================ HALL
FLOOR_Y = 226

def draw_hall():
    for y in range(H):
        if y < 18:
            col = P['void']
        elif y < 56:
            col = P['hall_dark']
        elif y < 150:
            col = P['hall_mid'] if y % 7 else P['hall_dark']
        else:
            col = P['hall_mid']
        c.rect(0, y, W, 1, col)
    for y in range(0, H):
        for x in range(0, W):
            d = math.hypot(x - CX, y - (CY + 2))
            if d < 100:
                if d < 52:
                    c.set(x, y, P['hall_hi'])
                elif d < 78 and (x + 2 * y) % 3 == 0:
                    c.set(x, y, P['hall_hi'])
                elif d < 100 and (x + 3 * y) % 7 == 0:
                    c.set(x, y, P['arch'])
    for y in range(FLOOR_Y, H):
        t = (y - FLOOR_Y) / float(H - 1 - FLOOR_Y)
        col = P['floor_dark'] if t < 0.4 else (P['floor_mid'] if t < 0.8 else P['floor_hi'])
        c.rect(0, y, W, 1, col)
    for k in range(-7, 8):
        safe_line(CX + k * 16, FLOOR_Y, CX + k * 52, H - 1, P['floor_dark'])
    for y in range(FLOOR_Y + 5, H, 8):
        c.line(0, y, W - 1, y, P['floor_dark'])
    for y in range(FLOOR_Y, H):
        for x in range(0, W):
            d = math.hypot(x - CX, (y - FLOOR_Y - 5) * 1.7)
            if d < 66:
                if d < 24:
                    c.set(x, y, P['floor_lit'])
                elif (x + y) % 3 == 0:
                    c.set(x, y, P['floor_hi'])
    def arch(cx0, base_y, w, h):
        c.rect(cx0 - w // 2 - 3, base_y - h, 3, h, P['arch'])
        c.rect(cx0 + w // 2, base_y - h, 3, h, P['arch'])
        for i in range(w + 8):
            x = cx0 - w // 2 - 3 + i
            t = i / float(w + 8)
            yy = base_y - h - int(math.sin(t * math.pi) * 24) - 2
            c.set(x, yy, P['arch_hi'])
            c.set(x, yy + 1, P['arch'])
        c.rect(cx0 - w // 2 - 3, base_y - h - 1, w + 6, 2, P['arch'])
        c.rect(cx0 - w // 2, base_y - h + 4, w, h - 8, P['arch'])
        c.rect(cx0 - w // 2 + 2, base_y - h + 9, w - 4, h - 16, P['arch_hi'])
        c.rect(cx0, base_y - h + 4, 1, h - 8, P['arch'])
        c.line(cx0 - w // 2, base_y - h + 7, cx0 + w // 2, base_y - h + 7, P['arch'])
        for yy in range(base_y - h + 9, base_y - 4, 2):
            c.set(cx0 - 3, yy, P['glow_cool'])
            c.set(cx0 + 3, yy, P['glow_cool'])
    arch(34, 222, 30, 110)
    arch(222, 222, 30, 110)
    arch(128, 208, 46, 134)
    for chx, ln in ((58, 42), (198, 48), (100, 26), (156, 26)):
        for i in range(ln):
            x = chx + (1 if (i // 3) % 2 else 0)
            safe_set(x, i, P['iron_mid'])
            safe_set(x, i + 1, P['iron_dark'])
        ly = ln + 1
        c.rect(chx - 2, ly, 5, 4, P['iron_dark'])
        c.rect(chx - 1, ly + 1, 3, 2, P['rune_dim'])
        c.set(chx, ly + 1, P['rune'])
        safe_set(chx - 1, ly, P['iron_mid'])

def draw_pedestal():
    top = 232
    # floating shadow just under the instrument base
    c.ellipse(CX, top - 4, 30, 5, P['shadow'])
    c.ellipse(CX, top - 3, 22, 3, P['shadow'])
    # cap
    c.rect(88, top, 80, 8, P['stone_mid'])
    c.rect(88, top + 6, 80, 2, P['stone_dark'])
    c.ellipse(CX, top, 40, 5, P['stone_mid'])
    c.ellipse(CX, top - 1, 32, 3, P['stone_hi'])
    c.ellipse(CX, top - 1, 20, 2, P['stone_lit'])
    for i in range(15):
        a = math.pi * (i / 14.0)
        x = int(round(CX + 34 * math.cos(a)))
        y = int(round(top - 3 * math.sin(a)))
        c.set(x, y, P['rune_dim'])
        if i % 3 == 0:
            c.set(x, y - 1, P['rune'])
    # column
    c.rect(96, top + 8, 64, 10, P['stone_dark'])
    for x in range(100, 156, 6):
        c.rect(x, top + 9, 2, 8, P['stone_mid'])
        c.set(x, top + 9, P['stone_hi'])
    # steps
    c.rect(84, top + 18, 88, 6, P['stone_mid'])
    c.rect(84, top + 22, 88, 2, P['stone_dark'])
    c.rect(76, top + 24, 104, 8, P['stone_dark'])
    c.rect(76, top + 30, 104, 2, P['shadow'])
    # side shading + cracks
    c.rect(88, top + 2, 3, 16, P['stone_dark'])
    c.rect(165, top + 2, 3, 16, P['floor_dark'])
    c.line(104, top + 12, 110, top + 20, P['floor_dark'])
    c.line(150, top + 14, 146, top + 22, P['floor_dark'])
    c.line(CX, top + 26, CX + 4, top + 32, P['floor_dark'])
    # rubble
    for rx, ry in ((64, 248), (196, 250), (52, 254), (206, 254), (182, 246)):
        c.set(rx, ry, P['stone_mid'])
        c.set(rx + 1, ry, P['stone_dark'])
        c.set(rx, ry + 1, P['stone_dark'])

draw_hall()
draw_pedestal()
print('hall + pedestal ok')

# ================================================================ INSTRUMENT
def draw_core_glow():
    for y in range(CY - 62, CY + 62):
        for x in range(CX - 62, CX + 62):
            d = math.hypot(x - CX, y - CY)
            if d < 60:
                if d < 30 and (x + y) % 2 == 0:
                    c.set(x, y, P['glow_warm'])
                elif d < 44 and (x + 2 * y) % 5 == 0:
                    c.set(x, y, P['glow_warm'])
                elif d < 60 and (x + 3 * y) % 9 == 0:
                    c.set(x, y, P['glow_cool'])

def draw_back_hardware():
    safe_line(CX, CY - 92, CX, CY + 92, P['brass_dark'])
    for y in range(CY - 88, CY + 89, 6):
        c.rect(CX - 2, y, 5, 3, P['brass_deep'])
    tilted_band(70, 22, -14, 3, ['shadow'] + BR_RAMP[:5], dim_back=0.25)
    tilted_band(56, 16, 10, 3, ['shadow'] + BR_RAMP[:5], dim_back=0.25)
    tilted_band(44, 11, 24, 2, ['shadow'] + BR_RAMP[:5], dim_back=0.25)
    tilted_band(33, 8, -30, 2, ['shadow'] + BR_RAMP[:5], dim_back=0.25)

def draw_meridian():
    engrave_circle(95, P['shadow'])
    engrave_circle(94, P['brass_dark'])
    shaded_annulus(88, 94, BR_RAMP, rim_light=115)
    radial_ticks(89, 93, 72, P['brass_dark'])
    radial_ticks(90, 92, 24, P['brass_deep'])
    engrave_circle(87, P['brass_deep'])
    for i in range(12):
        a = 2 * math.pi * i / 12
        safe_set(CX + 91 * math.cos(a), CY + 91 * math.sin(a), P['brass_spec'])
    c.rect(CX - 4, CY - 101, 9, 6, P['brass_deep'])
    c.rect(CX - 3, CY - 100, 7, 4, P['brass'])
    c.rect(CX - 2, CY - 99, 5, 2, P['brass_spec'])
    c.rect(CX - 4, CY + 95, 9, 6, P['brass_deep'])
    c.rect(CX - 3, CY + 96, 7, 4, P['brass_mid'])
    c.rect(CX - 1, CY - 108, 3, 6, P['brass_deep'])
    disc(CX, CY - 109, 2, P['brass'])
    c.set(CX - 1, CY - 110, P['brass_spec'])
    c.set(CX, CY - 111, P['brass_spec'])

def draw_ecliptics():
    tilted_band(78, 26, -12, 5, BR_RAMP, dim_back=0.3)
    tilted_band(64, 20, 9, 5, BR_RAMP, dim_back=0.3)
    tilted_band(51, 15, 22, 4, BR_RAMP, dim_back=0.3)
    tilted_band(39, 11, -26, 4, BR_RAMP, dim_back=0.3)
    tilted_band(28, 8, 16, 3, BR_RAMP, dim_back=0.3)
    for i in range(14):
        x, y = ring_point(78, 26, -12, 180 * (0.1 + 0.8 * i / 13.0))
        if y > CY + 6:
            draw_rune(x - 1, y - 2, i, P['rune'] if i % 2 else P['rune_dim'])
    for i in range(12):
        x, y = ring_point(64, 20, 9, 30 * i)
        safe_set(x, y, P['brass_hi'] if y >= CY else P['brass_dark'])
        safe_set(x, y + 1, P['brass_dark'])

def draw_horizon():
    for y in range(CY - 104, CY + 105):
        for x in range(CX - 104, CX + 105):
            dx, dy = x - CX, y - CY
            d2 = dx * dx + dy * dy
            if 96 * 96 <= d2 <= 104 * 104:
                a = math.degrees(math.atan2(dy, dx)) % 360
                dd = abs((a - 115 + 180) % 360 - 180)
                if dy > 4:
                    L = 1.0 - (math.sqrt(d2) - 96) / 8.0
                    if dd < 70:
                        L += 0.5 * (1 - dd / 70.0)
                    L = max(0.0, min(0.999, L))
                    c.set(x, y, P[BR_RAMP[int(L * len(BR_RAMP))]])
                elif dy < -4 and (x + y) % 3:
                    c.set(x, y, P['brass_dark'])
    radial_ticks(97, 103, 48, P['brass_dark'], a0=10, a1=170)
    for i in range(16):
        a = math.pi * (0.08 + 0.84 * i / 15.0)
        x = int(round(CX + 100 * math.cos(a)))
        y = int(round(CY + 100 * math.sin(a)))
        if y > CY + 10:
            draw_rune(x - 1, y - 2, i + 2, P['rune_hot'] if i % 3 == 0 else P['rune'])
    engrave_circle(96, P['shadow'])
    engrave_circle(105, P['shadow'])

# crystal spheres: (ring rx, ry, rot, angle_deg, radius, dark, base, lit)
CRYSTALS = [
    (78, 26, -12, 195, 7, 'crystal_dk', 'crystal', 'crystal_hi'),
    (78, 26, -12, 345, 6, 'crystal_dk', 'crystal', 'crystal_hi'),
    (64, 20, 9, 60, 6, 'violet_dk', 'violet', 'violet_hi'),
    (64, 20, 9, 250, 6, 'crystal_dk', 'crystal', 'crystal_hi'),
    (51, 15, 22, 130, 5, 'violet_dk', 'violet', 'violet_hi'),
    (51, 15, 22, 310, 5, 'crystal_dk', 'crystal', 'crystal_hi'),
    (39, 11, -26, 90, 4, 'crystal_dk', 'crystal', 'crystal_hi'),
]

def draw_armature():
    for rx, ry, rot, t, r, dk, base, lit in CRYSTALS:
        mx, my = ring_point(rx, ry, rot, t)
        # mount arm from the ring inward toward the hub
        ix, iy = ring_point(rx * 0.55, ry * 0.55, rot, t)
        safe_line(ix, iy, mx, my, P['brass_dark'])
        safe_line(ix, iy + 1, mx, my + 1, P['brass_mid'])
        # collar on the ring
        disc(mx, my, 2, P['brass_deep'])
        safe_set(mx - 1, my - 1, P['brass_hi'])
        # short stem out to the sphere
        dxn, dyn = (mx - ix), (my - iy)
        dl = math.hypot(dxn, dyn) or 1.0
        sx, sy = mx + dxn / dl * (r + 1), my + dyn / dl * (r + 1)
        safe_line(mx, my, sx, sy, P['brass_mid'])
        crystal_ball(sx, sy, r, P[dk], P[base], P[lit], P['crystal_sp'])
        # halo pixels
        for gx, gy in ((sx - r - 2, sy), (sx + r + 2, sy),
                       (sx, sy - r - 2), (sx, sy + r + 2)):
            safe_set(gx, gy, P['glow_cool'] if base == 'crystal' else P['violet_dk'])

def draw_gearwork():
    gear(44, 208, 9, 12, 'brass_mid', 'brass_dark', 'brass_hi', rot=0, hub=2)
    gear(64, 199, 6, 9, 'copper', 'brass_dark', 'copper_hi', rot=15, hub=1)
    gear(212, 206, 9, 12, 'brass_mid', 'brass_dark', 'brass_hi', rot=8, hub=2)
    gear(192, 197, 6, 9, 'copper', 'brass_dark', 'copper_hi', rot=22, hub=1)
    gear(128, 238, 11, 14, 'brass_deep', 'brass_dark', 'brass', rot=5, hub=3)
    gear(103, 246, 6, 9, 'copper', 'brass_dark', 'copper_hi', rot=30, hub=1)
    gear(153, 247, 5, 8, 'brass_mid', 'brass_dark', 'brass_hi', rot=12, hub=1)
    safe_line(50, 212, 60, 205, P['brass_dark'])
    safe_line(206, 212, 198, 203, P['brass_dark'])
    safe_line(120, 242, 111, 247, P['brass_dark'])
    safe_line(140, 241, 149, 248, P['brass_dark'])
    safe_line(128, 226, 128, 214, P['brass_deep'])
    safe_line(127, 226, 127, 214, P['brass_mid'])

def draw_dialwork():
    dial(96, 238, 6, 'brass_dark', 'brass_deep', 'rune', 2.4)
    dial(160, 238, 6, 'brass_dark', 'brass_deep', 'rune', -0.9)
    dial(128, 252, 5, 'brass_dark', 'brass_deep', 'rune', 1.2)
    for gx, gy in ((85, 236), (171, 236), (114, 254), (144, 254)):
        draw_rune(gx, gy, (gx + gy) % 8, P['rune_dim'])

def draw_core():
    disc(CX, CY, 16, P['core_deep'])
    disc(CX, CY, 13, P['core'])
    disc(CX, CY, 9, P['core_hi'])
    disc(CX, CY, 5, P['core_sp'])
    for a_deg, ln in ((0, 22), (45, 15), (90, 22), (135, 15), (180, 22),
                      (225, 15), (270, 22), (315, 15)):
        a = math.radians(a_deg)
        for t in range(5, ln):
            safe_set(CX + t * math.cos(a), CY + t * math.sin(a),
                     P['core_hi'] if t < ln * 0.55 else P['core'])
    for i in range(12):
        a = 2 * math.pi * i / 12
        x, y = CX + 21 * math.cos(a), CY + 21 * math.sin(a)
        safe_set(x, y, P['rune'])
        if i % 3 == 0:
            safe_set(x, y - 1, P['rune_hot'])
    engrave_circle(23, P['brass_dark'])
    engrave_circle(24, P['shadow'])

def draw_outlines():
    engrave_circle(96, P['shadow'])
    for i in range(240):
        a = 2 * math.pi * i / 240
        x, y = CX + 106 * math.cos(a), CY + 106 * math.sin(a)
        if y > CY + 3 or y < CY - 3:
            safe_set(x, y, P['shadow'])
    # pedestal outline
    c.rect(88, 229, 80, 1, P['shadow'])
    c.rect(87, 230, 1, 10, P['shadow'])
    c.rect(168, 230, 1, 10, P['shadow'])
    c.rect(83, 248, 90, 1, P['shadow'])
    c.rect(75, 254, 106, 1, P['shadow'])
    for gx, gy, gr in ((44, 208, 12), (212, 206, 12), (128, 238, 14)):
        for i in range(48):
            a = 2 * math.pi * i / 48
            safe_set(gx + gr * math.cos(a), gy + gr * math.sin(a), P['shadow'])
    for rx, ry, rot, t, r, *_ in CRYSTALS:
        mx, my = ring_point(rx, ry, rot, t)
        dxn, dyn = (mx - ring_point(rx * 0.55, ry * 0.55, rot, t)[0],
                    my - ring_point(rx * 0.55, ry * 0.55, rot, t)[1])
        dl = math.hypot(dxn, dyn) or 1.0
        sx, sy = mx + dxn / dl * (r + 1), my + dyn / dl * (r + 1)
        rr = r + 1
        for i in range(max(20, int(2 * math.pi * rr))):
            a = 2 * math.pi * i / max(20, int(2 * math.pi * rr))
            safe_set(sx + rr * math.cos(a), sy + rr * math.sin(a), P['shadow'])

def draw_sparkles():
    for sx, sy, k in ((22, 44, 1), (234, 56, 0), (16, 124, 0), (242, 132, 1),
                      (42, 180, 1), (214, 170, 0), (74, 32, 0), (184, 28, 1),
                      (110, 18, 1), (148, 22, 0), (26, 224, 0), (230, 228, 1),
                      (58, 96, 0), (200, 92, 1)):
        col = P['rune_hot'] if k else P['crystal_sp']
        safe_set(sx, sy, col)
        if k:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                safe_set(sx + dx, sy + dy, P['rune_dim'])

draw_core_glow()
draw_back_hardware()
draw_meridian()
draw_ecliptics()
draw_horizon()
draw_armature()
draw_gearwork()
draw_dialwork()
draw_core()
draw_outlines()
draw_sparkles()
print('instrument ok')

# ================================================================ FINISHING
# ground the pedestal with a plinth slab at the frame edge
c.rect(72, 250, 112, 6, P['stone_dark'])
c.rect(72, 254, 112, 2, P['shadow'])
c.rect(76, 250, 104, 1, P['stone_mid'])

# vignette: darken the corners for dramatic lighting
def vignette():
    for y in range(H):
        for x in range(W):
            d = math.hypot((x - CX) / 128.0, (y - 122) / 128.0)
            if d > 0.80:
                if d > 1.0 or (x + y) % 2 == 0:
                    c.set(x, y, P['void'])

vignette()

print('done drawing')
print(c.stats_text())

def overview(step=4):
    lum = {}
    for entry in c.palette():
        r, g, b, a = entry['rgba']
        lum[entry['index']] = (0.3 * r + 0.6 * g + 0.1 * b) / 255.0
    chars = ' .:-=+*#%@'
    out = []
    for y in range(0, H, step):
        out.append(''.join(chars[min(9, int(lum.get(c.get(x, y), 0.0) * 9.99))]
                           for x in range(0, W, step)))
    return '\n'.join(out)

print('=== OVERVIEW (luminance) ===')
print(overview(4))

finish(c)




