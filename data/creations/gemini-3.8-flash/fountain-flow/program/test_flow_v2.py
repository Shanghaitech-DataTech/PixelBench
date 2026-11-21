from pixelbench_api import *

c = new_canvas(64, 92, name="flowing_fountain_v2")
dy = 16
c.blit(input_canvas, 0, dy)

# Color definitions
c_deep = c.color('#13546b', 'water_deep') # deeper water shadow
c_dark = c.color('#1d8baa', 'water_dark') # original c5
c_mid  = c.color('#2ec7dc', 'water_mid')  # original c6
c_ice  = c.color('#a6f3ff', 'water_ice')  # very pale cyan / foam highlight
c_white= c.color('#ffffff', 'water_white')# white foam / splash

# -------------------------------------------------------------
# 1. TOP SPOUT / JET (y = 2 to 22)
# -------------------------------------------------------------
# Top nozzle tip in input_canvas is at y=0,1 (new canvas y=16, 17)
# Center is x=31, 32

# Water erupting from nozzle (y=15..17):
# Mouth of nozzle covered in energetic white churning water
c.rect(30, 15, 4, 2, c_white)
c.set(29, 16, c_ice)
c.set(34, 16, c_ice)

# Central jet column rising:
# y=7 to 14:
for y in range(7, 15):
    # Width 4-6 px
    c.set(29, y, c_mid)
    c.set(30, y, c_ice)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice)
    c.set(34, y, c_mid)
    if y in (9, 10, 12, 13):
        c.set(28, y, c_dark)
        c.set(35, y, c_dark)

# Apex / crown of the jet (y=3 to 6):
# The plume tops out at y=3
c.rect(30, 3, 4, 2, c_white)
c.set(31, 2, c_ice)
c.set(32, 2, c_white)

# Flowering outward and arching:
# y=4:
c.rect(28, 4, 8, 2, c_white)
c.set(27, 4, c_ice)
c.set(36, 4, c_ice)

# y=5:
c.set(26, 5, c_ice)
c.set(27, 5, c_white)
c.rect(28, 5, 8, 1, c_ice)
c.set(31, 5, c_white)
c.set(32, 5, c_white)
c.set(36, 5, c_white)
c.set(37, 5, c_ice)

# y=6:
c.set(25, 6, c_mid)
c.set(26, 6, c_white)
c.set(27, 6, c_ice)
c.set(36, 6, c_ice)
c.set(37, 6, c_white)
c.set(38, 6, c_mid)

# Parabolic falling streams (left and right):
# Left stream (outer):
left_arc = [
    (24, 7, c_white), (25, 7, c_ice), (26, 7, c_mid),
    (24, 8, c_ice),   (25, 8, c_white), (26, 8, c_mid),
    (23, 9, c_mid),   (24, 9, c_white), (25, 9, c_ice),
    (23, 10, c_white),(24, 10, c_ice),  (25, 10, c_mid),
    (23, 11, c_ice),  (24, 11, c_white),(25, 11, c_dark),
    (22, 12, c_mid),  (23, 12, c_white),(24, 12, c_ice),
    (22, 13, c_white),(23, 13, c_ice),  (24, 13, c_mid),
    (22, 14, c_ice),  (23, 14, c_white),(24, 14, c_mid),
    (22, 15, c_mid),  (23, 15, c_white),(24, 15, c_ice),
    (22, 16, c_ice),  (23, 16, c_white),(24, 16, c_mid),
    (22, 17, c_white),(23, 17, c_ice),  (24, 17, c_dark),
    (22, 18, c_mid),  (23, 18, c_white),(24, 18, c_ice),
    (22, 19, c_white),(23, 19, c_white),(24, 19, c_mid),
    (21, 20, c_ice),  (22, 20, c_white),(23, 20, c_white), (24, 20, c_mid),
    (21, 21, c_white),(22, 21, c_white),(23, 21, c_ice),   (24, 21, c_mid),
    (20, 22, c_white),(21, 22, c_white),(22, 22, c_ice),   (23, 22, c_mid)
]
for x, y, col in left_arc:
    c.set(x, y, col)

# Right stream (outer):
right_arc = [
    (37, 7, c_mid),   (38, 7, c_ice),   (39, 7, c_white),
    (37, 8, c_mid),   (38, 8, c_white), (39, 8, c_ice),
    (38, 9, c_ice),   (39, 9, c_white), (40, 9, c_mid),
    (38, 10, c_mid),  (39, 10, c_ice),  (40, 10, c_white),
    (38, 11, c_dark), (39, 11, c_white),(40, 11, c_ice),
    (39, 12, c_ice),  (40, 12, c_white),(41, 12, c_mid),
    (39, 13, c_mid),  (40, 13, c_ice),  (41, 13, c_white),
    (39, 14, c_mid),  (40, 14, c_white),(41, 14, c_ice),
    (39, 15, c_ice),  (40, 15, c_white),(41, 15, c_mid),
    (39, 16, c_mid),  (40, 16, c_white),(41, 16, c_ice),
    (39, 17, c_dark), (40, 17, c_ice),  (41, 17, c_white),
    (39, 18, c_ice),  (40, 18, c_white),(41, 18, c_mid),
    (39, 19, c_mid),  (40, 19, c_white),(41, 19, c_white),
    (39, 20, c_mid),  (40, 20, c_white),(41, 20, c_white), (42, 20, c_ice),
    (39, 21, c_mid),  (40, 21, c_ice),  (41, 21, c_white), (42, 21, c_white),
    (40, 22, c_mid),  (41, 22, c_ice),  (42, 22, c_white), (43, 22, c_white)
]
for x, y, col in right_arc:
    c.set(x, y, col)

# Droplets dancing in air:
spray_drops = [
    (31, 1), (32, 1), (29, 2), (34, 2), (27, 3), (36, 3),
    (24, 5), (39, 5), (22, 8), (41, 8), (21, 11), (42, 11),
    (20, 14), (43, 14), (19, 18), (44, 18), (28, 8), (35, 8),
    (27, 12), (36, 12), (28, 16), (35, 16)
]
for x, y in spray_drops:
    c.set(x, y, c_white if (x+y)%2==0 else c_ice)

# -------------------------------------------------------------
# 2. TOP BOWL FOAM & SPLASHES (y = 22..28)
# -------------------------------------------------------------
# Water in top bowl: ripples and churning foam
# Landing points of spray arcs: x=20..23 and x=40..43
c.rect(21, 23, 3, 2, c_white)
c.set(20, 24, c_ice)
c.set(24, 24, c_ice)
c.set(21, 25, c_ice)

c.rect(40, 23, 3, 2, c_white)
c.set(39, 24, c_ice)
c.set(43, 24, c_ice)
c.set(42, 25, c_ice)

# Foam rings around central nozzle base (x=28..35, y=23..25):
c.set(29, 23, c_ice)
c.set(30, 23, c_white)
c.set(33, 23, c_white)
c.set(34, 23, c_ice)
c.set(28, 24, c_mid)
c.set(35, 24, c_mid)
c.set(30, 25, c_ice)
c.set(31, 25, c_white)
c.set(32, 25, c_white)
c.set(33, 25, c_ice)

# -------------------------------------------------------------
# 3. CASCADE 1: TOP BOWL OVERFLOW TO MIDDLE BOWL (y = 27..34)
# -------------------------------------------------------------
# Top bowl rim is at y=27..30 (new coords)
# Water spills over in 3 cascades: Left (x=21..23), Center (x=30..33), Right (x=40..42)

# Left cascade:
for y in range(27, 33):
    c.set(20, y, c_ice if y%2==0 else c_mid)
    c.set(21, y, c_white)
    c.set(22, y, c_ice if y%2==1 else c_white)
    c.set(23, y, c_mid)
# Splash landing in middle bowl (y=32..34, x=19..24):
c.set(19, 33, c_ice)
c.rect(20, 33, 3, 2, c_white)
c.set(23, 33, c_ice)
c.set(24, 34, c_mid)
c.set(19, 34, c_mid)

# Center cascade: spills over front lip of top bowl:
c.rect(30, 29, 4, 1, c_white) # breaking over lip
for y in range(30, 34):
    c.set(30, y, c_ice)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice)
# Splash landing in middle bowl (y=33..35, x=29..34):
c.rect(30, 34, 4, 1, c_white)
c.set(29, 34, c_ice)
c.set(34, 34, c_ice)
c.set(31, 35, c_ice)
c.set(32, 35, c_ice)

# Right cascade:
for y in range(27, 33):
    c.set(40, y, c_mid)
    c.set(41, y, c_ice if y%2==1 else c_white)
    c.set(42, y, c_white)
    c.set(43, y, c_ice if y%2==0 else c_mid)
# Splash landing in middle bowl (y=32..34, x=39..44):
c.set(39, 33, c_ice)
c.rect(40, 33, 3, 2, c_white)
c.set(43, 33, c_ice)
c.set(44, 34, c_mid)
c.set(39, 34, c_mid)

# -------------------------------------------------------------
# 4. CASCADE 2: MIDDLE BOWL OVERFLOW TO BOTTOM BOWL (y = 37..44)
# -------------------------------------------------------------
# Middle bowl rim is at y=37..40
# Water spills over in 4 cascades: Far-left (x=15..17), Mid-left (x=24..26), Mid-right (x=37..39), Far-right (x=46..48)

# Far-left cascade:
for y in range(37, 43):
    c.set(14, y, c_mid)
    c.set(15, y, c_white)
    c.set(16, y, c_ice if y%2==0 else c_white)
    c.set(17, y, c_mid)
# Splash in bottom bowl (y=42..44, x=13..18):
c.rect(14, 43, 3, 1, c_white)
c.set(13, 43, c_ice)
c.set(17, 43, c_ice)
c.set(14, 44, c_ice)

# Mid-left cascade:
for y in range(38, 44):
    c.set(24, y, c_ice)
    c.set(25, y, c_white)
    c.set(26, y, c_mid)
# Splash in bottom bowl:
c.rect(24, 44, 3, 1, c_white)
c.set(23, 44, c_ice)
c.set(27, 44, c_ice)

# Center front overflow of middle tier:
c.rect(30, 39, 4, 1, c_white)
for y in range(40, 44):
    c.set(30, y, c_mid)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_mid)
c.rect(30, 44, 4, 1, c_white)
c.set(29, 44, c_ice)
c.set(34, 44, c_ice)

# Mid-right cascade:
for y in range(38, 44):
    c.set(37, y, c_mid)
    c.set(38, y, c_white)
    c.set(39, y, c_ice)
# Splash in bottom bowl:
c.rect(37, 44, 3, 1, c_white)
c.set(36, 44, c_ice)
c.set(40, 44, c_ice)

# Far-right cascade:
for y in range(37, 43):
    c.set(46, y, c_mid)
    c.set(47, y, c_ice if y%2==0 else c_white)
    c.set(48, y, c_white)
    c.set(49, y, c_mid)
# Splash in bottom bowl:
c.rect(46, 43, 3, 1, c_white)
c.set(45, 43, c_ice)
c.set(49, 43, c_ice)
c.set(48, 44, c_ice)

# -------------------------------------------------------------
# 5. CASCADE 3: BOTTOM BOWL OVERFLOW TO GROUND BASIN (y = 47..65)
# -------------------------------------------------------------
# Bottom bowl rim is at y=47..50
# Grand waterfalls cascading down into the large ground basin!
# 5 major waterfall curtains:
# 1) Far Left: x=12..15, falling from y=48 to y=60
# 2) Mid Left: x=21..24, falling from y=49 to y=63
# 3) Center:   x=30..33, falling from y=50 to y=65
# 4) Mid Right:x=39..42, falling from y=49 to y=63
# 5) Far Right:x=48..51, falling from y=48 to y=60

# 1) Far Left waterfall:
c.rect(12, 48, 4, 1, c_white)
for y in range(49, 61):
    c.set(11, y, c_dark if y > 53 else c_mid)
    c.set(12, y, c_mid)
    c.set(13, y, c_white)
    c.set(14, y, c_ice if y%2==0 else c_white)
    c.set(15, y, c_mid)
# Splash in basin:
c.rect(11, 60, 5, 2, c_white)
c.set(10, 60, c_ice)
c.set(16, 60, c_ice)
c.set(10, 61, c_mid)
c.set(16, 61, c_mid)
# Ripples:
c.set(9, 61, c_ice)
c.set(17, 61, c_ice)
c.set(11, 62, c_ice)
c.set(15, 62, c_ice)

# 2) Mid Left waterfall:
c.rect(21, 49, 4, 1, c_white)
for y in range(50, 64):
    c.set(20, y, c_mid)
    c.set(21, y, c_ice if y%2==1 else c_white)
    c.set(22, y, c_white)
    c.set(23, y, c_white if y%2==0 else c_ice)
    c.set(24, y, c_mid)
# Splash in basin:
c.rect(20, 63, 5, 2, c_white)
c.set(19, 63, c_ice)
c.set(25, 63, c_ice)
c.set(19, 64, c_mid)
c.set(25, 64, c_mid)
# Ripples:
c.set(18, 64, c_ice)
c.set(26, 64, c_ice)
c.set(21, 65, c_ice)
c.set(23, 65, c_ice)

# 3) Center waterfall:
c.rect(30, 50, 4, 1, c_white)
for y in range(51, 66):
    c.set(29, y, c_mid)
    c.set(30, y, c_ice if y%2==0 else c_white)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice if y%2==1 else c_white)
    c.set(34, y, c_mid)
# Splash in basin:
c.rect(29, 65, 6, 2, c_white)
c.set(28, 65, c_ice)
c.set(35, 65, c_ice)
c.set(28, 66, c_mid)
c.set(35, 66, c_mid)
# Ripples:
c.set(27, 66, c_ice)
c.set(36, 66, c_ice)
c.set(30, 67, c_ice)
c.set(33, 67, c_ice)

# 4) Mid Right waterfall:
c.rect(39, 49, 4, 1, c_white)
for y in range(50, 64):
    c.set(39, y, c_mid)
    c.set(40, y, c_white if y%2==0 else c_ice)
    c.set(41, y, c_white)
    c.set(42, y, c_ice if y%2==1 else c_white)
    c.set(43, y, c_mid)
# Splash in basin:
c.rect(38, 63, 5, 2, c_white)
c.set(37, 63, c_ice)
c.set(43, 63, c_ice)
c.set(37, 64, c_mid)
c.set(43, 64, c_mid)
# Ripples:
c.set(36, 64, c_ice)
c.set(44, 64, c_ice)
c.set(39, 65, c_ice)
c.set(42, 65, c_ice)

# 5) Far Right waterfall:
c.rect(48, 48, 4, 1, c_white)
for y in range(49, 61):
    c.set(48, y, c_mid)
    c.set(49, y, c_ice if y%2==0 else c_white)
    c.set(50, y, c_white)
    c.set(51, y, c_mid)
    c.set(52, y, c_dark if y > 53 else c_mid)
# Splash in basin:
c.rect(48, 60, 5, 2, c_white)
c.set(47, 60, c_ice)
c.set(53, 60, c_ice)
c.set(47, 61, c_mid)
c.set(53, 61, c_mid)
# Ripples:
c.set(46, 61, c_ice)
c.set(54, 61, c_ice)
c.set(48, 62, c_ice)
c.set(52, 62, c_ice)

# Spray mist droplets around the grand waterfalls:
basin_spray = [
    (10, 58), (17, 58), (18, 59), (26, 61), (27, 62), 
    (36, 62), (37, 61), (45, 59), (46, 58), (54, 58),
    (14, 63), (22, 66), (41, 66), (49, 63)
]
for x, y in basin_spray:
    c.set(x, y, c_white if (x+y)%2==0 else c_ice)

# Ripples and waves across basin pool:
# Adding active wavelets:
pool_waves = [
    (15, 68), (16, 68), (18, 69), (19, 69),
    (44, 69), (45, 69), (47, 68), (48, 68),
    (24, 70), (25, 70), (38, 70), (39, 70),
    (31, 71), (32, 71)
]
for x, y in pool_waves:
    c.set(x, y, c_ice)

view(c)
