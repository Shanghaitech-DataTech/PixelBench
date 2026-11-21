from pixelbench_api import *

# Final high-quality flowing fountain
w, h = 64, 92
dy = 16
out = new_canvas(w, h, name="flowing_fountain")
out.blit(input_canvas, 0, dy)

# Registered palette colors
c_deep  = out.color('#13546b', 'water_deep')
c_dark  = out.color('#1d8baa', 'water_dark') # original c5
c_mid   = out.color('#2ec7dc', 'water_mid')  # original c6
c_ice   = out.color('#a6f3ff', 'water_ice')  # light aqua / foam
c_white = out.color('#ffffff', 'water_white')# pure white highlight / foam

# =========================================================================
# 1. TOP SPOUT / JET (y = 2 to 21)
# =========================================================================
# Plume with solid dark cyan / teal outline, vibrant cyan fill, and white highlights

# Apex & Dome (y=2..7):
# y=2 (Apex tip):
out.set(31, 2, c_dark)
out.set(32, 2, c_dark)

# y=3:
out.set(30, 3, c_dark)
out.set(31, 3, c_white)
out.set(32, 3, c_white)
out.set(33, 3, c_dark)

# y=4:
out.set(28, 4, c_dark)
out.set(29, 4, c_mid)
out.set(30, 4, c_ice)
out.set(31, 4, c_white)
out.set(32, 4, c_white)
out.set(33, 4, c_ice)
out.set(34, 4, c_mid)
out.set(35, 4, c_dark)

# y=5:
out.set(26, 5, c_dark)
out.set(27, 5, c_mid)
out.set(28, 5, c_ice)
out.set(29, 5, c_white)
out.set(30, 5, c_white)
out.set(31, 5, c_white)
out.set(32, 5, c_white)
out.set(33, 5, c_white)
out.set(34, 5, c_white)
out.set(35, 5, c_ice)
out.set(36, 5, c_mid)
out.set(37, 5, c_dark)

# y=6:
out.set(25, 6, c_dark)
out.set(26, 6, c_mid)
out.set(27, 6, c_ice)
out.set(28, 6, c_white)
out.set(29, 6, c_ice)
out.set(30, 6, c_white)
out.set(31, 6, c_white)
out.set(32, 6, c_white)
out.set(33, 6, c_white)
out.set(34, 6, c_ice)
out.set(35, 6, c_white)
out.set(36, 6, c_ice)
out.set(37, 6, c_mid)
out.set(38, 6, c_dark)

# y=7:
out.set(24, 7, c_dark)
out.set(25, 7, c_mid)
out.set(26, 7, c_white)
out.set(27, 7, c_ice)
out.set(28, 7, c_mid)
out.set(29, 7, c_dark)
out.set(30, 7, c_mid)
out.set(31, 7, c_white)
out.set(32, 7, c_white)
out.set(33, 7, c_mid)
out.set(34, 7, c_dark)
out.set(35, 7, c_mid)
out.set(36, 7, c_ice)
out.set(37, 7, c_white)
out.set(38, 7, c_mid)
out.set(39, 7, c_dark)

# y=8..15: Left stream (curving down), Center rising column, Right stream (curving down)
for y in range(8, 16):
    # Left falling stream (x=23..27):
    lx = 24 if y in (8, 9) else (23 if y in (10, 11, 12) else 22)
    out.set(lx-1, y, c_dark)
    out.set(lx,   y, c_mid)
    out.set(lx+1, y, c_white if y%2==0 else c_ice)
    out.set(lx+2, y, c_ice if y%2==0 else c_white)
    out.set(lx+3, y, c_mid)
    out.set(lx+4, y, c_dark)
    
    # Center geyser column from nozzle:
    out.set(29, y, c_dark)
    out.set(30, y, c_mid)
    out.set(31, y, c_white)
    out.set(32, y, c_white)
    out.set(33, y, c_mid)
    out.set(34, y, c_dark)
    
    # Right falling stream (x=36..40):
    rx = 36 if y in (8, 9) else (37 if y in (10, 11, 12) else 38)
    out.set(rx-1, y, c_dark)
    out.set(rx,   y, c_mid)
    out.set(rx+1, y, c_ice if y%2==0 else c_white)
    out.set(rx+2, y, c_white if y%2==0 else c_ice)
    out.set(rx+3, y, c_mid)
    out.set(rx+4, y, c_dark)

# y=16..18: Eruption collar over nozzle mouth:
out.rect(29, 16, 6, 2, c_white)
out.set(28, 16, c_dark)
out.set(35, 16, c_dark)
out.set(28, 17, c_mid)
out.set(35, 17, c_mid)

# Water streams entering top bowl (y=16..20):
for y in range(16, 21):
    out.set(21, y, c_dark)
    out.set(22, y, c_mid)
    out.set(23, y, c_white)
    out.set(24, y, c_ice)
    out.set(25, y, c_mid)
    out.set(26, y, c_dark)

    out.set(37, y, c_dark)
    out.set(38, y, c_mid)
    out.set(39, y, c_ice)
    out.set(40, y, c_white)
    out.set(41, y, c_mid)
    out.set(42, y, c_dark)

# Droplets dancing in air:
spray_droplets = [
    (31, 1), (32, 1), (28, 2), (35, 2), (24, 4), (39, 4),
    (22, 6), (41, 6), (20, 9), (43, 9), (19, 13), (44, 13),
    (20, 16), (43, 16), (27, 10), (36, 10), (28, 13), (35, 13)
]
for x, y in spray_droplets:
    out.set(x, y, c_mid if (x+y)%3==0 else c_ice)

# =========================================================================
# 2. TOP BOWL CHURNING & SPLASHES (y = 21..26)
# =========================================================================
# Splash crowns where streams land:
for x in range(21, 27):
    out.set(x, 21, c_white)
    out.set(x, 22, c_ice)
out.set(20, 21, c_mid)
out.set(27, 21, c_mid)

for x in range(37, 43):
    out.set(x, 21, c_white)
    out.set(x, 22, c_ice)
out.set(36, 21, c_mid)
out.set(43, 21, c_mid)

# Churning foam around base of nozzle:
out.rect(29, 22, 6, 1, c_white)
out.rect(28, 23, 8, 1, c_ice)
out.set(27, 24, c_mid)
out.set(36, 24, c_mid)
out.set(28, 24, c_white)
out.set(35, 24, c_white)

# =========================================================================
# 3. CASCADE 1: TOP BOWL TO MIDDLE BOWL (y = 26..35)
# =========================================================================
# Left cascade (x=20..23):
out.rect(20, 26, 4, 1, c_white)
for y in range(27, 33):
    out.set(19, y, c_dark)
    out.set(20, y, c_mid)
    out.set(21, y, c_white)
    out.set(22, y, c_ice if y%2==0 else c_white)
    out.set(23, y, c_mid)
    out.set(24, y, c_dark)
# Impact splash in middle bowl (y=32..34):
out.rect(19, 32, 6, 2, c_white)
out.set(18, 32, c_mid)
out.set(25, 32, c_mid)
out.set(19, 34, c_ice)
out.set(24, 34, c_ice)

# Center cascade over front lip (x=30..33):
out.rect(30, 28, 4, 1, c_white)
for y in range(29, 34):
    out.set(29, y, c_mid)
    out.set(30, y, c_ice)
    out.set(31, y, c_white)
    out.set(32, y, c_white)
    out.set(33, y, c_ice)
    out.set(34, y, c_mid)
# Impact splash:
out.rect(29, 34, 6, 1, c_white)
out.set(28, 34, c_ice)
out.set(35, 34, c_ice)
out.set(30, 35, c_ice)
out.set(31, 35, c_white)
out.set(32, 35, c_white)
out.set(33, 35, c_ice)

# Right cascade (x=40..43):
out.rect(40, 26, 4, 1, c_white)
for y in range(27, 33):
    out.set(39, y, c_dark)
    out.set(40, y, c_mid)
    out.set(41, y, c_ice if y%2==1 else c_white)
    out.set(42, y, c_white)
    out.set(43, y, c_mid)
    out.set(44, y, c_dark)
# Impact splash:
out.rect(39, 32, 6, 2, c_white)
out.set(38, 32, c_mid)
out.set(45, 32, c_mid)
out.set(39, 34, c_ice)
out.set(44, 34, c_ice)

# =========================================================================
# 4. CASCADE 2: MIDDLE BOWL TO BOTTOM BOWL (y = 37..45)
# =========================================================================
# Far-left cascade (x=14..17):
out.rect(14, 37, 4, 1, c_white)
for y in range(38, 43):
    out.set(13, y, c_dark)
    out.set(14, y, c_mid)
    out.set(15, y, c_white)
    out.set(16, y, c_ice if y%2==0 else c_white)
    out.set(17, y, c_mid)
    out.set(18, y, c_dark)
out.rect(13, 42, 6, 2, c_white)
out.set(12, 42, c_mid)
out.set(19, 42, c_mid)
out.set(14, 44, c_ice)
out.set(17, 44, c_ice)

# Mid-left cascade (x=23..26):
out.rect(23, 38, 4, 1, c_white)
for y in range(39, 44):
    out.set(22, y, c_mid)
    out.set(23, y, c_ice)
    out.set(24, y, c_white)
    out.set(25, y, c_white)
    out.set(26, y, c_mid)
out.rect(22, 43, 6, 2, c_white)
out.set(21, 43, c_ice)
out.set(28, 43, c_ice)

# Center cascade (x=30..33):
out.rect(30, 39, 4, 1, c_white)
for y in range(40, 44):
    out.set(29, y, c_mid)
    out.set(30, y, c_ice)
    out.set(31, y, c_white)
    out.set(32, y, c_white)
    out.set(33, y, c_ice)
    out.set(34, y, c_mid)
out.rect(29, 44, 6, 1, c_white)
out.set(28, 44, c_ice)
out.set(35, 44, c_ice)
out.set(30, 45, c_ice)
out.set(31, 45, c_white)
out.set(32, 45, c_white)
out.set(33, 45, c_ice)

# Mid-right cascade (x=37..40):
out.rect(37, 38, 4, 1, c_white)
for y in range(39, 44):
    out.set(37, y, c_mid)
    out.set(38, y, c_white)
    out.set(39, y, c_white)
    out.set(40, y, c_ice)
    out.set(41, y, c_mid)
out.rect(36, 43, 6, 2, c_white)
out.set(35, 43, c_ice)
out.set(42, 43, c_ice)

# Far-right cascade (x=46..49):
out.rect(46, 37, 4, 1, c_white)
for y in range(38, 43):
    out.set(45, y, c_dark)
    out.set(46, y, c_mid)
    out.set(47, y, c_ice if y%2==0 else c_white)
    out.set(48, y, c_white)
    out.set(49, y, c_mid)
    out.set(50, y, c_dark)
out.rect(45, 42, 6, 2, c_white)
out.set(44, 42, c_mid)
out.set(51, 42, c_mid)
out.set(46, 44, c_ice)
out.set(49, 44, c_ice)

# =========================================================================
# 5. CASCADE 3: BOTTOM BOWL TO GROUND BASIN (y = 47..68)
# =========================================================================
# Grand waterfalls cascading down into the basin pool

# 1) Far Left Waterfall (x=13..15):
out.rect(13, 47, 3, 1, c_white)
for y in range(48, 60):
    out.set(11, y, c_dark)
    out.set(12, y, c_mid)
    out.set(13, y, c_white if y%2==0 else c_ice)
    out.set(14, y, c_white)
    out.set(15, y, c_ice if y%2==1 else c_white)
    out.set(16, y, c_mid)
    out.set(17, y, c_dark)
# Splash crown:
out.rect(11, 59, 7, 2, c_white)
out.set(10, 59, c_ice)
out.set(18, 59, c_ice)
out.set(10, 60, c_mid)
out.set(18, 60, c_mid)
out.set(11, 58, c_white)
out.set(17, 58, c_ice)
out.set(12, 61, c_ice)
out.set(13, 61, c_white)
out.set(14, 61, c_white)
out.set(15, 61, c_ice)

# 2) Mid Left Waterfall (x=21..24):
out.rect(21, 48, 4, 1, c_white)
for y in range(49, 63):
    out.set(19, y, c_dark)
    out.set(20, y, c_mid)
    out.set(21, y, c_ice if y%2==1 else c_white)
    out.set(22, y, c_white)
    out.set(23, y, c_white if y%2==0 else c_ice)
    out.set(24, y, c_mid)
    out.set(25, y, c_dark)
# Splash crown:
out.rect(19, 62, 7, 2, c_white)
out.set(18, 62, c_ice)
out.set(26, 62, c_ice)
out.set(18, 63, c_mid)
out.set(26, 63, c_mid)
out.set(19, 61, c_white)
out.set(25, 61, c_ice)
out.set(21, 64, c_ice)
out.set(22, 64, c_white)
out.set(23, 64, c_white)
out.set(24, 64, c_ice)

# 3) Center Waterfall (x=30..33, pouring over pedestal into front basin):
out.rect(30, 49, 4, 1, c_white)
for y in range(50, 65):
    out.set(28, y, c_dark)
    out.set(29, y, c_mid)
    out.set(30, y, c_ice if y%2==0 else c_white)
    out.set(31, y, c_white)
    out.set(32, y, c_white)
    out.set(33, y, c_ice if y%2==1 else c_white)
    out.set(34, y, c_mid)
    out.set(35, y, c_dark)
# Splash crown:
out.rect(28, 64, 8, 2, c_white)
out.set(27, 64, c_ice)
out.set(36, 64, c_ice)
out.set(27, 65, c_mid)
out.set(36, 65, c_mid)
out.set(28, 63, c_white)
out.set(35, 63, c_white)
out.set(29, 66, c_ice)
out.set(30, 66, c_white)
out.set(31, 66, c_white)
out.set(32, 66, c_white)
out.set(33, 66, c_white)
out.set(34, 66, c_ice)

# 4) Mid Right Waterfall (x=39..42):
out.rect(39, 48, 4, 1, c_white)
for y in range(49, 63):
    out.set(38, y, c_dark)
    out.set(39, y, c_mid)
    out.set(40, y, c_ice if y%2==0 else c_white)
    out.set(41, y, c_white)
    out.set(42, y, c_white if y%2==1 else c_ice)
    out.set(43, y, c_mid)
    out.set(44, y, c_dark)
# Splash crown:
out.rect(38, 62, 7, 2, c_white)
out.set(37, 62, c_ice)
out.set(45, 62, c_ice)
out.set(37, 63, c_mid)
out.set(45, 63, c_mid)
out.set(38, 61, c_ice)
out.set(44, 61, c_white)
out.set(39, 64, c_ice)
out.set(40, 64, c_white)
out.set(41, 64, c_white)
out.set(42, 64, c_ice)

# 5) Far Right Waterfall (x=48..50):
out.rect(48, 47, 3, 1, c_white)
for y in range(48, 60):
    out.set(46, y, c_dark)
    out.set(47, y, c_mid)
    out.set(48, y, c_ice if y%2==1 else c_white)
    out.set(49, y, c_white)
    out.set(50, y, c_white if y%2==0 else c_ice)
    out.set(51, y, c_mid)
    out.set(52, y, c_dark)
# Splash crown:
out.rect(46, 59, 7, 2, c_white)
out.set(45, 59, c_ice)
out.set(53, 59, c_ice)
out.set(45, 60, c_mid)
out.set(53, 60, c_mid)
out.set(46, 58, c_ice)
out.set(52, 58, c_white)
out.set(48, 61, c_ice)
out.set(49, 61, c_white)
out.set(50, 61, c_white)
out.set(51, 61, c_ice)

# =========================================================================
# 6. BASIN SURFACE RIPPLES & FOAM WAVES (y = 62..72)
# =========================================================================
waves = [
    (14, 63, c_ice), (15, 63, c_white), (16, 63, c_ice),
    (13, 64, c_mid), (14, 64, c_ice), (15, 64, c_mid),
    (16, 65, c_ice), (17, 65, c_ice), (18, 66, c_mid),
    (25, 66, c_ice), (26, 66, c_white), (27, 67, c_ice),
    (36, 67, c_ice), (37, 66, c_white), (38, 66, c_ice),
    (47, 63, c_ice), (48, 63, c_white), (49, 63, c_ice),
    (48, 64, c_mid), (49, 64, c_ice), (50, 64, c_mid),
    (45, 65, c_ice), (46, 65, c_ice), (44, 66, c_mid),
    (22, 68, c_ice), (23, 68, c_white), (24, 68, c_ice),
    (29, 68, c_mid), (30, 68, c_ice), (31, 68, c_white), (32, 68, c_white), (33, 68, c_ice), (34, 68, c_mid),
    (39, 68, c_ice), (40, 68, c_white), (41, 68, c_ice),
    (27, 70, c_ice), (28, 70, c_ice), (35, 70, c_ice), (36, 70, c_ice),
    (30, 71, c_mid), (31, 71, c_ice), (32, 71, c_ice), (33, 71, c_mid),
]
for x, y, col in waves:
    out.set(x, y, col)

view(out)
finish(out)
