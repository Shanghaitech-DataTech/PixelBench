c = input_canvas.copy(name='output')
W, H = 256, 128

# ============ 1. Global palette remap: cold blue day -> blood night ============
remap = {
    1: '#1a0a14', 2: '#240d18', 3: '#3a0f1e', 4: '#551422', 5: '#8b2028',
    6: '#050208', 7: '#6b1822', 8: '#551420', 9: '#7e1c26', 10: '#c8a898',
    11: '#ff6a4a', 12: '#e0c0b0', 13: '#2a0c1a', 14: '#1a0812', 15: '#ff5030',
    16: '#ff4428', 17: '#0a0408', 18: '#140a0c', 19: '#ffd040', 20: '#3a1028',
    21: '#982830', 22: '#40141e', 23: '#b84048', 24: '#170810', 25: '#241018',
    26: '#a06048', 27: '#b03838', 28: '#c84028', 29: '#341022', 30: '#683828',
    31: '#ffd870', 32: '#983030', 33: '#2a1218', 34: '#b84048', 35: '#10060c',
    36: '#b04048', 37: '#8c2830', 38: '#882830', 39: '#d89068', 40: '#ff5838',
    41: '#903030', 42: '#a03838', 43: '#a03838', 44: '#ff3020', 45: '#48141e',
    46: '#3c121c', 47: '#b84848', 48: '#44141e', 49: '#200c14', 50: '#28101a',
    51: '#ff4028', 52: '#501822', 53: '#100610', 54: '#120710', 55: '#0c050a',
    56: '#1a0a14', 57: '#3a1420', 58: '#241018', 59: '#30101c', 60: '#2a0c14',
    61: '#1c0c12', 62: '#5c1822', 63: '#301818', 64: '#602028', 65: '#681c26',
    66: '#48141e', 67: '#581824', 68: '#160812', 69: '#38121c', 70: '#120710',
    71: '#24101a', 72: '#180a12', 73: '#d0b090',
}
idx_map = {}
for old_idx in sorted(remap.keys()):
    idx_map[old_idx] = c.color(remap[old_idx])
for y in range(H):
    for x in range(W):
        old = c.get(x, y)
        if old in idx_map:
            c.set(x, y, idx_map[old])

# ============ 2. Hanging blood moon ============
MCX, MCY, MR = 128, 29, 26
c.circle(MCX, MCY, 29, c.color('#241018'))
c.circle(MCX, MCY, 27, c.color('#301622'))
MOON_MID    = c.color('#b8322a')
MOON_HI     = c.color('#cc4430')
MOON_CORE   = c.color('#e05a38')
MOON_BRIGHT = c.color('#ee7244')
MOON_DARK   = c.color('#94241e')
c.circle(MCX, MCY, MR, MOON_MID)
c.circle(MCX - 5, MCY - 5, 18, MOON_HI)
c.circle(MCX - 9, MCY - 9, 12, MOON_CORE)
c.circle(MCX - 12, MCY - 12, 6, MOON_BRIGHT)
for ccx, ccy, cr in [(118, 23, 5), (140, 33, 4), (142, 21, 3),
                     (110, 33, 3), (132, 15, 3), (146, 39, 3)]:
    c.circle(ccx, ccy, cr, MOON_DARK)

# ============ 3. Demon King's castle silhouette ============
SIL = c.color('#0a0508')
# base wall + battlements
c.rect(70, 88, 116, 15, SIL)
for bx in range(72, 184, 6):
    c.rect(bx, 85, 3, 3, SIL)
# flank towers with conical roofs and spires
c.rect(88, 62, 18, 41, SIL)
c.poly([(97, 46), (88, 62), (106, 62)], SIL, fill=True)
c.rect(96, 40, 2, 7, SIL)
c.rect(150, 62, 18, 41, SIL)
c.poly([(159, 46), (150, 62), (168, 62)], SIL, fill=True)
c.rect(158, 40, 2, 7, SIL)
# central keep + tall spire with war banner
c.rect(110, 55, 36, 48, SIL)
c.poly([(128, 22), (114, 55), (142, 55)], SIL, fill=True)
c.rect(127, 16, 2, 7, SIL)
c.poly([(129, 17), (135, 19), (129, 21)], c.color('#8c1a24'), fill=True)
# outer corner towers
c.rect(64, 80, 14, 23, SIL)
c.poly([(71, 68), (64, 80), (78, 80)], SIL, fill=True)
c.rect(70, 62, 2, 7, SIL)
c.rect(178, 80, 14, 23, SIL)
c.poly([(185, 68), (178, 80), (192, 80)], SIL, fill=True)
c.rect(184, 62, 2, 7, SIL)

# ============ 4. Hell-lit windows and portal ============
WIN      = c.color('#ff3020')
WIN_CORE = c.color('#ff7040')
for wx, wy in [(120, 62), (132, 62), (120, 74), (132, 74), (120, 86), (132, 86)]:
    c.rect(wx, wy, 4, 6, WIN); c.rect(wx + 1, wy + 1, 2, 3, WIN_CORE)
for wx, wy in [(94, 70), (94, 82), (156, 70), (156, 82)]:
    c.rect(wx, wy, 4, 6, WIN); c.rect(wx + 1, wy + 1, 2, 3, WIN_CORE)
for wx, wy in [(68, 86), (184, 86)]:
    c.rect(wx, wy, 4, 5, WIN); c.rect(wx + 1, wy + 1, 2, 2, WIN_CORE)
c.rect(123, 92, 10, 11, WIN)
c.rect(125, 94, 6, 6, WIN_CORE)

# ============ 5. Blood reflections in the water ============
REFL = c.color('#0d060a')
for i, (rx, rw) in enumerate([(76, 104), (86, 84), (96, 64), (106, 44)]):
    c.rect(rx, 104 + i * 3, rw, 1, REFL)
for i in range(8):
    ry = 104 + i * 3
    rw = max(4, 22 - i * 2)
    rx = 128 - rw // 2
    c.rect(rx, ry, rw, 1, c.color('#7e1c26') if i % 2 == 0 else c.color('#4a141e'))

# ============ 6. Bats circling the spire ============
BAT = c.color('#0a0508')
for bx, by in [(92, 20), (168, 16), (102, 44), (155, 50), (80, 32), (176, 34), (60, 22)]:
    c.rect(bx - 3, by - 1, 2, 2, BAT)
    c.rect(bx + 2, by - 1, 2, 2, BAT)
    c.rect(bx - 1, by, 3, 2, BAT)

# ============ 7. Drifting embers ============
for ex, ey in [(40, 12), (58, 40), (30, 52), (200, 18), (220, 44), (236, 30),
               (74, 8), (186, 10), (210, 60), (36, 70), (224, 72), (96, 12)]:
    c.set(ex, ey, c.color('#ff5030'))
for ex, ey in [(48, 26), (192, 52), (244, 14), (66, 56), (204, 34)]:
    c.set(ex, ey, c.color('#c84028'))

print(c.stats_text())
finish(c)
