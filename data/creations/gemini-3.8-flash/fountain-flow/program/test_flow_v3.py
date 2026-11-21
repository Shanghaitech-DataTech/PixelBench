from pixelbench_api import *

c = new_canvas(64, 92, name="flowing_fountain_v3")
dy = 16
c.blit(input_canvas, 0, dy)

# Color definitions
c_deep = c.color('#13546b', 'water_deep') # deep teal/shadow
c_dark = c.color('#1d8baa', 'water_dark') # original c5
c_mid  = c.color('#2ec7dc', 'water_mid')  # original c6
c_ice  = c.color('#a6f3ff', 'water_ice')  # very pale cyan / foam highlight
c_white= c.color('#ffffff', 'water_white')# white foam / splash
c_trans_slate = c.color('#413e51', 'stone_outline')

# =========================================================================
# 1. TOP SPOUT: LUSH VOLUMETRIC FOUNTAIN PLUME
# =========================================================================
# Apex of the plume at y=3..4, dome at y=4..7, rising core y=8..16
# Droplets above apex (y=1..3):
for x, y in [(31, 1), (32, 1), (29, 2), (34, 2), (31, 2), (32, 2), (28, 3), (35, 3)]:
    c.set(x, y, c_white if (x+y)%2==0 else c_ice)

# Apex crest (y=3..4):
c.rect(30, 3, 4, 1, c_white)
c.rect(29, 4, 6, 1, c_white)
c.set(28, 4, c_ice)
c.set(35, 4, c_ice)

# Dome top (y=5..7):
# Volumetric fill with texture
for y, (x0, x1) in enumerate([(26, 37), (25, 38), (24, 39)], start=5):
    # outer edges
    c.set(x0, y, c_mid)
    c.set(x0+1, y, c_ice)
    c.rect(x0+2, y, x1 - x0 - 3, 1, c_white)
    c.set(x1-1, y, c_ice)
    c.set(x1, y, c_mid)

# Shading inside the dome to give depth and fluid texture:
# y=6:
c.set(29, 6, c_ice)
c.set(34, 6, c_ice)
# y=7:
c.set(27, 7, c_white)
c.set(28, 7, c_ice)
c.set(29, 7, c_mid)
c.set(30, 7, c_ice)
c.rect(31, 7, 2, 1, c_white)
c.set(33, 7, c_ice)
c.set(34, 7, c_mid)
c.set(35, 7, c_ice)
c.set(36, 7, c_white)

# Plume mid-section (y=8..12):
# Divided into:
# - Left falling sheet (x=23..27)
# - Center rising core (x=30..33)
# - Right falling sheet (x=36..40)
# - Inner spray mist filling the gap between sheets and core!
for y in range(8, 13):
    # Left falling stream:
    c.set(23, y, c_mid)
    c.set(24, y, c_ice if y%2==0 else c_white)
    c.set(25, y, c_white)
    c.set(26, y, c_ice if y%2==1 else c_white)
    c.set(27, y, c_mid)
    
    # Mist in left gap (x=28..29):
    c.set(28, y, c_mid if y%2==0 else c_ice)
    c.set(29, y, c_ice if y%2==1 else c_white)
    
    # Center core:
    c.set(30, y, c_white)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_white)
    
    # Mist in right gap (x=34..35):
    c.set(34, y, c_ice if y%2==1 else c_white)
    c.set(35, y, c_mid if y%2==0 else c_ice)
    
    # Right falling stream:
    c.set(36, y, c_mid)
    c.set(37, y, c_ice if y%2==1 else c_white)
    c.set(38, y, c_white)
    c.set(39, y, c_ice if y%2==0 else c_white)
    c.set(40, y, c_mid)

# Plume lower section (y=13..16):
# Water streams falling into top bowl and central column erupting from nozzle:
for y in range(13, 17):
    # Left stream descending into bowl:
    c.set(22, y, c_mid)
    c.set(23, y, c_white)
    c.set(24, y, c_ice)
    c.set(25, y, c_mid)
    
    # Center jet from nozzle (x=30..33):
    c.set(29, y, c_mid)
    c.set(30, y, c_ice)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice)
    c.set(34, y, c_mid)
    
    # Right stream descending into bowl:
    c.set(38, y, c_mid)
    c.set(39, y, c_ice)
    c.set(40, y, c_white)
    c.set(41, y, c_mid)

# Water erupting from nozzle collar (y=16..18):
c.rect(30, 16, 4, 2, c_white)
c.set(29, 17, c_ice)
c.set(34, 17, c_ice)

# Side spray mist droplets:
air_drops = [
    (23, 6), (40, 6), (22, 7), (41, 7), (21, 9), (42, 9),
    (21, 11), (42, 11), (20, 14), (43, 14), (20, 16), (43, 16),
    (27, 14), (36, 14), (28, 15), (35, 15)
]
for x, y in air_drops:
    c.set(x, y, c_white if (x+y)%2==0 else c_ice)

# =========================================================================
# 2. TOP BOWL: CHURNING WATER & SPLASHES (y = 20..27)
# =========================================================================
# Where left stream hits (x=21..25, y=21..24):
c.rect(21, 21, 4, 2, c_white)
c.set(20, 21, c_ice)
c.set(25, 21, c_ice)
c.set(21, 23, c_ice)
c.set(24, 23, c_ice)

# Where right stream hits (x=38..42, y=21..24):
c.rect(38, 21, 4, 2, c_white)
c.set(37, 21, c_ice)
c.set(42, 21, c_ice)
c.set(38, 23, c_ice)
c.set(41, 23, c_ice)

# Foam rings and ripples in top bowl:
c.rect(29, 22, 6, 1, c_ice)
c.rect(30, 22, 4, 1, c_white)
c.set(28, 23, c_mid)
c.set(35, 23, c_mid)
c.set(27, 24, c_ice)
c.set(36, 24, c_ice)
c.set(28, 25, c_white)
c.set(35, 25, c_white)

# =========================================================================
# 3. CASCADE 1: TOP BOWL TO MIDDLE BOWL (y = 26..34)
# =========================================================================
# Top bowl rim is at y=27..30 (new coords)
# Cascades spill over:
# Left cascade: x=21..23
# Center cascade: x=30..33
# Right cascade: x=40..42

# Left cascade:
c.rect(21, 26, 3, 1, c_white) # breaking over rim
for y in range(27, 33):
    c.set(20, y, c_mid)
    c.set(21, y, c_white)
    c.set(22, y, c_ice if y%2==0 else c_white)
    c.set(23, y, c_mid)
# Impact splash in middle bowl (y=32..34):
c.set(19, 32, c_ice)
c.set(20, 32, c_white)
c.set(21, 32, c_white)
c.set(22, 32, c_white)
c.set(23, 32, c_ice)
c.set(20, 33, c_ice)
c.set(21, 33, c_white)
c.set(22, 33, c_ice)
c.set(19, 33, c_mid)
c.set(24, 33, c_mid)

# Center cascade (over front lip):
c.rect(30, 28, 4, 1, c_white)
for y in range(29, 34):
    c.set(30, y, c_ice)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice)
# Impact splash in middle bowl:
c.rect(29, 34, 6, 1, c_white)
c.set(28, 34, c_ice)
c.set(35, 34, c_ice)
c.set(30, 35, c_ice)
c.set(31, 35, c_white)
c.set(32, 35, c_white)
c.set(33, 35, c_ice)

# Right cascade:
c.rect(40, 26, 3, 1, c_white)
for y in range(27, 33):
    c.set(40, y, c_mid)
    c.set(41, y, c_ice if y%2==1 else c_white)
    c.set(42, y, c_white)
    c.set(43, y, c_mid)
# Impact splash in middle bowl (y=32..34):
c.set(40, 32, c_ice)
c.set(41, 32, c_white)
c.set(42, 32, c_white)
c.set(43, 32, c_white)
c.set(44, 32, c_ice)
c.set(41, 33, c_ice)
c.set(42, 33, c_white)
c.set(43, 33, c_ice)
c.set(39, 33, c_mid)
c.set(44, 33, c_mid)

# Extra splash droplets between tier 1 and 2:
for x, y in [(19, 30), (24, 31), (39, 31), (44, 30)]:
    c.set(x, y, c_white)

# Middle bowl surface ripples:
c.set(25, 33, c_ice)
c.set(26, 34, c_mid)
c.set(37, 34, c_mid)
c.set(38, 33, c_ice)

# =========================================================================
# 4. CASCADE 2: MIDDLE BOWL TO BOTTOM BOWL (y = 37..45)
# =========================================================================
# Spills over:
# Far-left: x=15..17
# Mid-left: x=24..26
# Center:   x=30..33
# Mid-right:x=37..39
# Far-right:x=46..48

# Far-left cascade:
c.rect(15, 37, 3, 1, c_white)
for y in range(38, 43):
    c.set(14, y, c_mid)
    c.set(15, y, c_white)
    c.set(16, y, c_ice if y%2==0 else c_white)
    c.set(17, y, c_mid)
# Splash in bottom bowl:
c.set(13, 42, c_ice)
c.set(14, 42, c_white)
c.set(15, 42, c_white)
c.set(16, 42, c_white)
c.set(17, 42, c_ice)
c.set(14, 43, c_ice)
c.set(15, 43, c_white)
c.set(16, 43, c_ice)

# Mid-left cascade:
c.rect(24, 38, 3, 1, c_white)
for y in range(39, 44):
    c.set(23, y, c_mid)
    c.set(24, y, c_ice if y%2==1 else c_white)
    c.set(25, y, c_white)
    c.set(26, y, c_mid)
# Splash:
c.set(23, 43, c_ice)
c.set(24, 43, c_white)
c.set(25, 43, c_white)
c.set(26, 43, c_ice)
c.set(24, 44, c_ice)
c.set(25, 44, c_white)

# Center cascade:
c.rect(30, 39, 4, 1, c_white)
for y in range(40, 44):
    c.set(29, y, c_mid)
    c.set(30, y, c_ice)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice)
    c.set(34, y, c_mid)
# Splash:
c.rect(29, 44, 6, 1, c_white)
c.set(28, 44, c_ice)
c.set(35, 44, c_ice)
c.set(30, 45, c_ice)
c.set(31, 45, c_white)
c.set(32, 45, c_white)
c.set(33, 45, c_ice)

# Mid-right cascade:
c.rect(37, 38, 3, 1, c_white)
for y in range(39, 44):
    c.set(37, y, c_mid)
    c.set(38, y, c_white)
    c.set(39, y, c_ice if y%2==0 else c_white)
    c.set(40, y, c_mid)
# Splash:
c.set(37, 43, c_ice)
c.set(38, 43, c_white)
c.set(39, 43, c_white)
c.set(40, 43, c_ice)
c.set(38, 44, c_white)
c.set(39, 44, c_ice)

# Far-right cascade:
c.rect(46, 37, 3, 1, c_white)
for y in range(38, 43):
    c.set(46, y, c_mid)
    c.set(47, y, c_ice if y%2==0 else c_white)
    c.set(48, y, c_white)
    c.set(49, y, c_mid)
# Splash:
c.set(46, 42, c_ice)
c.set(47, 42, c_white)
c.set(48, 42, c_white)
c.set(49, 42, c_white)
c.set(50, 42, c_ice)
c.set(47, 43, c_ice)
c.set(48, 43, c_white)
c.set(49, 43, c_ice)

# =========================================================================
# 5. CASCADE 3: BOTTOM BOWL TO GROUND BASIN (y = 47..68)
# =========================================================================
# Dramatic waterfalls pouring into the large basin!
# 1) Far Left: x=13..15, falling to y=60
# 2) Mid Left: x=21..24, falling to y=63
# 3) Center:   x=30..33, falling to y=65
# 4) Mid Right:x=39..42, falling to y=63
# 5) Far Right:x=48..50, falling to y=60

# 1) Far Left Waterfall (x=13..15):
c.rect(13, 47, 3, 1, c_white)
for y in range(48, 60):
    c.set(12, y, c_mid)
    c.set(13, y, c_white if y%2==0 else c_ice)
    c.set(14, y, c_white)
    c.set(15, y, c_ice if y%2==1 else c_white)
    c.set(16, y, c_mid)
# Splash foam & churning crown:
c.set(11, 59, c_ice)
c.rect(12, 59, 5, 2, c_white)
c.set(17, 59, c_ice)
c.set(11, 60, c_white)
c.set(17, 60, c_white)
c.set(10, 60, c_mid)
c.set(18, 60, c_mid)
# Splash droplets & ripples:
c.set(11, 58, c_white)
c.set(17, 58, c_ice)
c.set(12, 61, c_ice)
c.set(13, 61, c_white)
c.set(14, 61, c_white)
c.set(15, 61, c_ice)
c.set(10, 61, c_ice)
c.set(18, 61, c_ice)

# 2) Mid Left Waterfall (x=21..24):
c.rect(21, 48, 4, 1, c_white)
for y in range(49, 63):
    c.set(20, y, c_mid)
    c.set(21, y, c_ice if y%2==1 else c_white)
    c.set(22, y, c_white)
    c.set(23, y, c_white if y%2==0 else c_ice)
    c.set(24, y, c_mid)
# Splash foam:
c.set(19, 62, c_ice)
c.rect(20, 62, 5, 2, c_white)
c.set(25, 62, c_ice)
c.set(19, 63, c_white)
c.set(25, 63, c_white)
c.set(18, 63, c_mid)
c.set(26, 63, c_mid)
# Splash droplets & ripples:
c.set(19, 61, c_white)
c.set(25, 61, c_ice)
c.set(21, 64, c_ice)
c.set(22, 64, c_white)
c.set(23, 64, c_white)
c.set(24, 64, c_ice)
c.set(18, 64, c_ice)
c.set(26, 64, c_ice)

# 3) Center Waterfall (x=30..33, pouring over pedestal into front basin):
c.rect(30, 49, 4, 1, c_white)
for y in range(50, 65):
    c.set(29, y, c_mid)
    c.set(30, y, c_ice if y%2==0 else c_white)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_ice if y%2==1 else c_white)
    c.set(34, y, c_mid)
# Splash foam:
c.set(28, 64, c_ice)
c.rect(29, 64, 6, 2, c_white)
c.set(35, 64, c_ice)
c.set(27, 65, c_mid)
c.set(28, 65, c_white)
c.set(35, 65, c_white)
c.set(36, 65, c_mid)
# Splash droplets & ripples:
c.set(28, 63, c_white)
c.set(35, 63, c_white)
c.set(29, 66, c_ice)
c.set(30, 66, c_white)
c.set(31, 66, c_white)
c.set(32, 66, c_white)
c.set(33, 66, c_white)
c.set(34, 66, c_ice)
c.set(28, 66, c_ice)
c.set(35, 66, c_ice)

# 4) Mid Right Waterfall (x=39..42):
c.rect(39, 48, 4, 1, c_white)
for y in range(49, 63):
    c.set(39, y, c_mid)
    c.set(40, y, c_ice if y%2==0 else c_white)
    c.set(41, y, c_white)
    c.set(42, y, c_white if y%2==1 else c_ice)
    c.set(43, y, c_mid)
# Splash foam:
c.set(38, 62, c_ice)
c.rect(39, 62, 5, 2, c_white)
c.set(44, 62, c_ice)
c.set(38, 63, c_white)
c.set(44, 63, c_white)
c.set(37, 63, c_mid)
c.set(45, 63, c_mid)
# Droplets & ripples:
c.set(38, 61, c_ice)
c.set(44, 61, c_white)
c.set(39, 64, c_ice)
c.set(40, 64, c_white)
c.set(41, 64, c_white)
c.set(42, 64, c_ice)
c.set(37, 64, c_ice)
c.set(45, 64, c_ice)

# 5) Far Right Waterfall (x=48..50):
c.rect(48, 47, 3, 1, c_white)
for y in range(48, 60):
    c.set(47, y, c_mid)
    c.set(48, y, c_ice if y%2==1 else c_white)
    c.set(49, y, c_white)
    c.set(50, y, c_white if y%2==0 else c_ice)
    c.set(51, y, c_mid)
# Splash foam:
c.set(46, 59, c_ice)
c.rect(47, 59, 5, 2, c_white)
c.set(52, 59, c_ice)
c.set(46, 60, c_white)
c.set(52, 60, c_white)
c.set(45, 60, c_mid)
c.set(53, 60, c_mid)
# Droplets & ripples:
c.set(46, 58, c_ice)
c.set(52, 58, c_white)
c.set(48, 61, c_ice)
c.set(49, 61, c_white)
c.set(50, 61, c_white)
c.set(51, 61, c_ice)
c.set(45, 61, c_ice)
c.set(53, 61, c_ice)

# =========================================================================
# 6. BASIN SURFACE AGITATION & RIPPLES (y = 62..72)
# =========================================================================
# Expanding wave rings connecting the splash points:
extra_waves = [
    # Left waves:
    (14, 63, c_ice), (15, 63, c_white), (16, 63, c_ice),
    (13, 64, c_mid), (14, 64, c_ice), (15, 64, c_mid),
    (16, 65, c_ice), (17, 65, c_ice), (18, 66, c_mid),
    # Center-left ripples:
    (25, 66, c_ice), (26, 66, c_white), (27, 67, c_ice),
    # Center-right ripples:
    (36, 67, c_ice), (37, 66, c_white), (38, 66, c_ice),
    # Right waves:
    (47, 63, c_ice), (48, 63, c_white), (49, 63, c_ice),
    (48, 64, c_mid), (49, 64, c_ice), (50, 64, c_mid),
    (45, 65, c_ice), (46, 65, c_ice), (44, 66, c_mid),
    # Front ripples near rim:
    (22, 68, c_ice), (23, 68, c_white), (24, 68, c_ice),
    (29, 68, c_mid), (30, 68, c_ice), (31, 68, c_white), (32, 68, c_white), (33, 68, c_ice), (34, 68, c_mid),
    (39, 68, c_ice), (40, 68, c_white), (41, 68, c_ice),
    (27, 70, c_ice), (28, 70, c_ice), (35, 70, c_ice), (36, 70, c_ice),
    (30, 71, c_mid), (31, 71, c_ice), (32, 71, c_ice), (33, 71, c_mid),
]
for x, y, col in extra_waves:
    c.set(x, y, col)

view(c)
