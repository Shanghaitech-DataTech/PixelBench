from pixelbench_api import *

# Create a new canvas 64x92
c = new_canvas(64, 92, name="flowing_fountain")
dy = 16
c.blit(input_canvas, 0, dy)

# Palette colors from input:
# 1: #413e51
# 2: #b9ab90
# 3: #645d72
# 4: #ffffff
# 5: #e1e2ba
# 6: #1d8baa
# 7: #2ec7dc

# Register helper water colors:
c_deep = c.color('#13546b', 'water_deep')
c_dark = c.color('#1d8baa', 'water_dark')
c_mid  = c.color('#2ec7dc', 'water_mid')
c_ice  = c.color('#a6f3ff', 'water_ice')
c_white= c.color('#ffffff', 'water_white')

# Let's inspect the top finial in original coordinates:
# y=0: x=31, 32 (outline a)
# y=1: x=30 (a), 31,32 (b), 33 (a)
# y=2: x=31, 32 (a)
# y=3: x=31, 32 (c)
# y=4: x=31, 32 (b)
# In new coordinates, add dy=16:
# y=16..20 is the nozzle.

# 1. Central jet column rising from nozzle (y=16 down to y=4):
# Nozzle mouth at y=16:
c.rect(30, 14, 4, 3, c_white)
c.set(29, 15, c_mid)
c.set(34, 15, c_mid)
c.set(29, 16, c_dark)
c.set(34, 16, c_dark)

# Column rising:
# y=6..14:
for y in range(7, 15):
    c.set(30, y, c_mid)
    c.set(31, y, c_white)
    c.set(32, y, c_white)
    c.set(33, y, c_mid)
    c.set(29, y, c_dark if y > 10 else c_mid)
    c.set(34, y, c_dark if y > 10 else c_mid)

# At peak (y=3..6), plume blooms and arches:
# Crown / dome:
c.rect(31, 3, 2, 2, c_white)
c.set(30, 4, c_ice)
c.set(33, 4, c_ice)
c.set(29, 4, c_white)
c.set(34, 4, c_white)

c.set(28, 5, c_white)
c.set(29, 5, c_ice)
c.set(30, 5, c_white)
c.set(31, 5, c_white)
c.set(32, 5, c_white)
c.set(33, 5, c_ice)
c.set(34, 5, c_white)
c.set(35, 5, c_white)

# Arcs spreading out and curving down:
# Left arc:
c.set(27, 6, c_white)
c.set(28, 6, c_mid)
c.set(26, 7, c_white)
c.set(27, 7, c_mid)
c.set(26, 8, c_ice)
c.set(27, 8, c_mid)
c.set(25, 9, c_white)
c.set(26, 9, c_mid)
c.set(25, 10, c_ice)
c.set(26, 10, c_dark)
c.set(25, 11, c_mid)
c.set(26, 11, c_white)
c.set(25, 12, c_dark)
c.set(26, 12, c_mid)
c.set(25, 13, c_mid)
c.set(26, 13, c_white)
# splash into top bowl at y=14..15 (new y=30..31):
c.set(24, 14, c_mid)
c.set(25, 14, c_white)
c.set(26, 14, c_ice)
c.set(27, 14, c_mid)

# Right arc:
c.set(36, 6, c_mid)
c.set(37, 6, c_white)
c.set(36, 7, c_mid)
c.set(37, 7, c_white)
c.set(36, 8, c_mid)
c.set(37, 8, c_ice)
c.set(37, 9, c_mid)
c.set(38, 9, c_white)
c.set(37, 10, c_dark)
c.set(38, 10, c_ice)
c.set(37, 11, c_white)
c.set(38, 11, c_mid)
c.set(37, 12, c_mid)
c.set(38, 12, c_dark)
c.set(37, 13, c_white)
c.set(38, 13, c_mid)
# splash into top bowl at y=14..15:
c.set(36, 14, c_mid)
c.set(37, 14, c_ice)
c.set(38, 14, c_white)
c.set(39, 14, c_mid)

# Air droplets:
droplets = [(31, 1), (32, 1), (29, 2), (34, 2), (26, 4), (37, 4), (24, 6), (39, 6), 
            (23, 8), (40, 8), (28, 9), (35, 9), (24, 11), (39, 11), (30, 2), (33, 2)]
for dx, dy_drop in droplets:
    c.set(dx, dy_drop, c_white if (dx+dy_drop)%2==0 else c_ice)

view(c)
