from pixelbench_api import *

# Let's test the plume design standalone on a small canvas first
test_c = new_canvas(64, 40)
# Draw nozzle at bottom:
test_c.blit(input_canvas, 0, 16)

c_deep = test_c.color('#13546b', 'water_deep')
c_dark = test_c.color('#1d8baa', 'water_dark')
c_mid  = test_c.color('#2ec7dc', 'water_mid')
c_ice  = test_c.color('#a6f3ff', 'water_ice')
c_white= test_c.color('#ffffff', 'water_white')
c_stone= test_c.color('#413e51', 'c0')

# Clear everything above y=21
for y in range(0, 21):
    for x in range(64):
        test_c.set(x, y, 0)

# Redraw the nozzle tip at y=16..20:
# In input_canvas:
# y=0: min_x=31, max_x=32 (1, 1)
# y=1: 30: 1, 31: 2, 32: 2, 33: 1
# y=2: 31: 1, 32: 1
# y=3: 31: 3, 32: 3
# y=4: 31: 2, 32: 2
# y=5: x=26..37 (tier 1 lip)
# With dy=16, nozzle tip is at y=16..20.

# Now, water spouting from the nozzle:
# A fountain plume has:
# A central geyser rising from y=16 up to y=4.
# At y=16: water shoots from nozzle mouth (x=30..33)
# Central rising column: x=29..34 (6 px wide)
# Crown/apex flares out at y=3..7 (width 14-16 px, x=24..39)
# Left and right curtains fall down from y=7 to y=21 into the bowl!

# Let's define the plume as a solid shape:
plume_pixels = {}

# 1. Apex and dome (y=3..7):
# y=3: apex
for x in range(30, 34):
    plume_pixels[(x, 3)] = c_white
plume_pixels[(29, 3)] = c_ice
plume_pixels[(34, 3)] = c_ice

# y=4: dome crest
for x in range(28, 36):
    plume_pixels[(x, 4)] = c_white
plume_pixels[(27, 4)] = c_ice
plume_pixels[(36, 4)] = c_ice
plume_pixels[(26, 4)] = c_mid
plume_pixels[(37, 4)] = c_mid

# y=5: dome expanding
for x in range(27, 37):
    plume_pixels[(x, 5)] = c_ice
for x in range(29, 35):
    plume_pixels[(x, 5)] = c_white
plume_pixels[(25, 5)] = c_dark
plume_pixels[(26, 5)] = c_mid
plume_pixels[(37, 5)] = c_mid
plume_pixels[(38, 5)] = c_dark

# y=6: dome base
for x in range(26, 38):
    plume_pixels[(x, 6)] = c_ice
for x in range(28, 36):
    plume_pixels[(x, 6)] = c_white
plume_pixels[(24, 6)] = c_dark
plume_pixels[(25, 6)] = c_mid
plume_pixels[(38, 6)] = c_mid
plume_pixels[(39, 6)] = c_dark

# y=7: dome underbelly / division into left stream, center column, right stream
for x in range(24, 40):
    plume_pixels[(x, 7)] = c_ice
plume_pixels[(23, 7)] = c_dark
plume_pixels[(24, 7)] = c_mid
plume_pixels[(25, 7)] = c_white
plume_pixels[(26, 7)] = c_white
plume_pixels[(27, 7)] = c_mid
plume_pixels[(28, 7)] = c_dark
# center core:
plume_pixels[(29, 7)] = c_mid
plume_pixels[(30, 7)] = c_white
plume_pixels[(31, 7)] = c_white
plume_pixels[(32, 7)] = c_white
plume_pixels[(33, 7)] = c_white
plume_pixels[(34, 7)] = c_mid
# right stream:
plume_pixels[(35, 7)] = c_dark
plume_pixels[(36, 7)] = c_mid
plume_pixels[(37, 7)] = c_white
plume_pixels[(38, 7)] = c_white
plume_pixels[(39, 7)] = c_mid
plume_pixels[(40, 7)] = c_dark

# Now for y=8..15:
# Left falling stream: x=23..26
# Center rising column: x=29..34
# Right falling stream: x=37..40
# Space between streams: transparent or a few mist droplets!
for y in range(8, 16):
    # Left stream:
    # slight curve inward/outward:
    lx = 23 if y in (8, 9, 10) else (22 if y in (11, 12, 13) else 23)
    plume_pixels[(lx, y)] = c_dark
    plume_pixels[(lx+1, y)] = c_mid
    plume_pixels[(lx+2, y)] = c_white if y%2==0 else c_ice
    plume_pixels[(lx+3, y)] = c_white if y%2==1 else c_ice
    plume_pixels[(lx+4, y)] = c_mid
    
    # Center rising column:
    plume_pixels[(29, y)] = c_dark
    plume_pixels[(30, y)] = c_mid
    plume_pixels[(31, y)] = c_white
    plume_pixels[(32, y)] = c_white
    plume_pixels[(33, y)] = c_ice
    plume_pixels[(34, y)] = c_dark
    
    # Right stream:
    rx = 36 if y in (8, 9, 10) else (37 if y in (11, 12, 13) else 36)
    plume_pixels[(rx, y)] = c_mid
    plume_pixels[(rx+1, y)] = c_ice if y%2==1 else c_white
    plume_pixels[(rx+2, y)] = c_white if y%2==0 else c_ice
    plume_pixels[(rx+3, y)] = c_mid
    plume_pixels[(rx+4, y)] = c_dark

# y=16: Nozzle mouth collar / eruption:
# Water erupts right over nozzle:
for x in range(28, 36):
    plume_pixels[(x, 16)] = c_white
plume_pixels[(27, 16)] = c_mid
plume_pixels[(36, 16)] = c_mid

# Left stream entering bowl (y=16..20):
for y in range(16, 21):
    plume_pixels[(23, y)] = c_dark
    plume_pixels[(24, y)] = c_white
    plume_pixels[(25, y)] = c_ice
    plume_pixels[(26, y)] = c_mid
    
    plume_pixels[(37, y)] = c_mid
    plume_pixels[(38, y)] = c_ice
    plume_pixels[(39, y)] = c_white
    plume_pixels[(40, y)] = c_dark

# Splash where left/right stream hit bowl water (y=21..23):
for x in range(22, 28):
    plume_pixels[(x, 21)] = c_white
plume_pixels[(21, 21)] = c_ice
plume_pixels[(28, 21)] = c_ice
for x in range(23, 27):
    plume_pixels[(x, 22)] = c_ice

for x in range(36, 42):
    plume_pixels[(x, 21)] = c_white
plume_pixels[(35, 21)] = c_ice
plume_pixels[(42, 21)] = c_ice
for x in range(37, 41):
    plume_pixels[(x, 22)] = c_ice

# Droplets in air:
drops = [(31, 1), (32, 1), (28, 2), (35, 2), (23, 4), (40, 4), (20, 8), (43, 8), (20, 12), (43, 12)]
for x, y in drops:
    plume_pixels[(x, y)] = c_white if (x+y)%2==0 else c_ice

for (x, y), col in plume_pixels.items():
    test_c.set(x, y, col)

view(test_c)
