from pixelbench_api import *

c = input_canvas
W, H = 256, 128
out = c.copy(name='output')

# --- Demonic recolour of every original palette entry ---
demonic = {
    0: None,
    1:  (26, 10, 20, 255),
    2:  (42, 13, 28, 255),
    3:  (58, 18, 34, 255),
    4:  (88, 22, 38, 255),
    5:  (134, 34, 46, 255),
    6:  (11, 6, 8, 255),
    7:  (106, 36, 48, 255),
    8:  (92, 34, 50, 255),
    9:  (110, 37, 52, 255),
    10: (154, 138, 144, 255),
    11: (176, 72, 88, 255),
    12: (90, 26, 38, 255),
    13: (60, 24, 56, 255),
    14: (38, 10, 22, 255),
    15: (192, 48, 64, 255),
    16: (176, 40, 56, 255),
    17: (16, 8, 16, 255),
    18: (30, 17, 24, 255),
    19: (224, 160, 48, 255),
    20: (72, 30, 58, 255),
    21: (122, 42, 56, 255),
    22: (72, 30, 46, 255),
    23: (136, 48, 62, 255),
    24: (24, 12, 26, 255),
    25: (38, 18, 30, 255),
    26: (154, 58, 70, 255),
    27: (160, 58, 72, 255),
    28: (90, 36, 38, 255),
    29: (56, 20, 48, 255),
    30: (106, 40, 50, 255),
    31: (216, 154, 40, 255),
    32: (122, 40, 68, 255),
    33: (40, 24, 32, 255),
    34: (144, 48, 68, 255),
    35: (14, 7, 18, 255),
    36: (140, 46, 60, 255),
    37: (162, 72, 82, 255),
    38: (124, 40, 56, 255),
    39: (192, 96, 82, 255),
    40: (92, 26, 38, 255),
    41: (110, 34, 50, 255),
    42: (116, 38, 54, 255),
    43: (120, 40, 56, 255),
    44: (208, 64, 98, 255),
    45: (74, 30, 50, 255),
    46: (68, 26, 44, 255),
    47: (152, 52, 62, 255),
    48: (60, 22, 36, 255),
    49: (42, 16, 34, 255),
    50: (52, 20, 36, 255),
    51: (144, 32, 46, 255),
    52: (92, 32, 50, 255),
    53: (30, 10, 22, 255),
    54: (20, 12, 18, 255),
    55: (14, 8, 16, 255),
    56: (30, 13, 24, 255),
    57: (110, 74, 48, 255),
    58: (42, 26, 32, 255),
    59: (42, 20, 50, 255),
    60: (92, 58, 40, 255),
    61: (28, 16, 24, 255),
    62: (86, 32, 50, 255),
    63: (74, 44, 36, 255),
    64: (102, 46, 58, 255),
    65: (102, 30, 46, 255),
    66: (78, 30, 44, 255),
    67: (94, 32, 46, 255),
    68: (26, 12, 32, 255),
    69: (64, 28, 46, 255),
    70: (20, 10, 24, 255),
    71: (44, 18, 34, 255),
    72: (32, 14, 24, 255),
    73: (192, 88, 88, 255),
}

newidx = {}
for k, v in demonic.items():
    newidx[k] = 0 if v is None else out.color(v, name='dm%d' % k)

for y in range(H):
    for x in range(W):
        i = out.get(x, y)
        out.set(x, y, newidx.get(i, i))

# --- Palette for the new elements ---
wall     = out.color('#1a0d14', 'wall')
wall_mid = out.color('#2a1620', 'wall_mid')
wall_hi  = out.color('#3a1e2c', 'wall_hi')
roof     = out.color('#0d0609', 'roof')
roof_hi  = out.color('#1c0d14', 'roof_hi')
window   = out.color('#ff4a2a', 'window')
window_hi= out.color('#ffb020', 'window_hi')
moon_glow= out.color('#4a0e16', 'moon_glow')
moon     = out.color('#c01828', 'moon')
moon_dark= out.color('#8a0e18', 'moon_dark')
moon_hi  = out.color('#e83848', 'moon_hi')
banner   = out.color('#c01828', 'banner')
chain    = out.color('#0d0609', 'chain')

# --- Hanging blood moon, behind the castle ---
out.circle(106, 20, 20, moon_glow)
out.line(106, 0, 106, 3, chain)
out.line(104, 0, 108, 0, chain)
out.circle(106, 20, 16, moon)
out.circle(100, 16, 3, moon_dark)
out.circle(114, 26, 2, moon_dark)
out.circle(104, 30, 2, moon_dark)
out.circle(98, 26, 2, moon_dark)
out.circle(101, 14, 2, moon_hi)

# --- Demon King's castle: main wall over the old "City of Hope" text ---
out.rect(4, 34, 252, 66, wall)
out.rect(4, 34, 252, 1, wall_hi)
for x in range(4, 254, 10):
    out.rect(x, 30, 6, 4, wall_mid)
for yy in (44, 54, 64, 74, 84, 94):
    out.rect(4, yy, 252, 1, wall_mid)

# Towers
out.rect(18, 20, 26, 80, wall_mid)
out.rect(66, 14, 30, 86, wall_mid)
out.rect(118, 8, 44, 92, wall_mid)
out.rect(186, 16, 28, 84, wall_mid)
out.rect(224, 22, 22, 78, wall_mid)

out.rect(18, 20, 4, 80, wall_hi)
out.rect(66, 14, 4, 86, wall_hi)
out.rect(118, 8, 5, 92, wall_hi)
out.rect(186, 16, 4, 84, wall_hi)
out.rect(224, 22, 4, 78, wall_hi)

# Spiked roofs
out.poly([(16, 20), (31, 1), (46, 20)], roof)
out.poly([(64, 14), (81, 0), (98, 14)], roof)
out.poly([(116, 8), (140, 0), (164, 8)], roof)
out.poly([(184, 16), (200, 1), (216, 16)], roof)
out.poly([(222, 22), (235, 5), (246, 22)], roof)

out.line(31, 1, 18, 19, roof_hi)
out.line(81, 0, 66, 13, roof_hi)
out.line(140, 0, 118, 7, roof_hi)
out.line(200, 1, 186, 15, roof_hi)
out.line(235, 5, 224, 21, roof_hi)

# Windows
for cx, ys in [(31, (42, 56, 70)), (81, (38, 52, 66)),
               (200, (44, 58, 72)), (235, (48, 62))]:
    for yy in ys:
        out.rect(cx - 1, yy, 3, 9, window)

# Great arched window on the keep
out.rect(132, 40, 16, 28, window)
out.circle(140, 40, 8, window)
out.rect(136, 44, 8, 20, window_hi)
out.circle(140, 44, 4, window_hi)
out.line(140, 40, 140, 67, wall)
out.line(132, 50, 147, 50, wall)
out.line(132, 60, 147, 60, wall)

for x, yy in [(52, 60), (100, 58), (172, 62), (212, 64),
              (60, 84), (150, 86), (200, 84)]:
    out.rect(x, yy, 4, 7, window)

# Banners
out.rect(31, 20, 5, 14, banner)
out.poly([(31, 34), (36, 34), (33, 40)], banner)
out.rect(140, 8, 6, 16, banner)
out.poly([(140, 24), (146, 24), (143, 30)], banner)
out.rect(200, 16, 5, 12, banner)
out.poly([(200, 28), (205, 28), (202, 34)], banner)

# Red mist at the castle base
out.rect(0, 100, 256, 3, moon_glow)

print(out.stats_text())
finish(out)
