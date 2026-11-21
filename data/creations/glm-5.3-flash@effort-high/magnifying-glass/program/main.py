from pixelbench_api import new_canvas, finish, view

c = new_canvas(16, 16, background=None, name="magnifier")

# Palette
FRAME   = c.color("#2b2b3a", name="frame_dark")     # lens rim
RIM_HI  = c.color("#5a5a72", name="frame_light")    # rim highlight
GLASS   = c.color("#a9d9f5", name="glass")
GLASS_D = c.color("#7fb8dd", name="glass_shade")
SHINE   = c.color("#eaf8ff", name="shine")
HANDLE  = c.color("#8b5a2b", name="wood")
WOOD_D  = c.color("#5c3a1a", name="wood_dark")
BAND    = c.color("#3d3d52", name="band")

# Lens rim: filled disc then glass inside
c.circle(6, 6, 4, FRAME, fill=True)
c.circle(6, 6, 3, GLASS, fill=True)

# Glass shading: lower-right inner tint
for x in range(5, 9):
    c.set(x, 8, GLASS_D)
c.set(7, 7, GLASS_D)
c.set(8, 7, GLASS_D)

# Shine: small diagonal highlight inside the glass, upper-left
c.set(4, 4, SHINE)
c.set(5, 4, SHINE)
c.set(4, 5, SHINE)

# Rim highlight on the upper-left of the ring itself
c.set(3, 3, RIM_HI)
c.set(2, 5, RIM_HI)
c.set(2, 6, RIM_HI)

# Metal band joining lens to handle (bridges the rim corner)
c.set(8, 9, BAND)
c.set(9, 9, BAND)
c.set(9, 10, BAND)

# Handle: 2px-thick diagonal to the bottom-right corner
wood_px = [(10, 10), (11, 10), (11, 11), (12, 11), (12, 12),
           (13, 12), (13, 13), (14, 13)]
for x, y in wood_px:
    c.set(x, y, HANDLE)

# Darker tip
c.set(14, 14, WOOD_D)
c.set(15, 14, WOOD_D)
c.set(15, 13, WOOD_D)

print(c.stats_text())
print(c.matrix_text())
view(c)
finish(c)
