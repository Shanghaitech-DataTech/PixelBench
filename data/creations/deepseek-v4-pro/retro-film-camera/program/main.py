c = new_canvas(32, 32)

# Palette
OUT = c.color("#20140c", "outline")
LEATHER = c.color("#5c3a22", "leather")
LEATHER_D = c.color("#3c2414", "leather_dark")
LEATHER_L = c.color("#7a4f2c", "leather_light")
METAL = c.color("#b8af9c", "metal")
METAL_D = c.color("#6f6757", "metal_dark")
METAL_L = c.color("#e8e0cc", "metal_light")
LENS_D = c.color("#101013", "lens_dark")
GLASS = c.color("#35556f", "glass")
GLASS_L = c.color("#7fb0d0", "glass_light")
SHUTTER = c.color("#c9c1b0", "shutter")
RED = c.color("#a83a2a", "red")

# --- Silhouette (dark outline) ---
# Main body
c.rect(2, 9, 28, 19, OUT)
# Top plate
c.rect(4, 5, 24, 5, OUT)

# Round a couple of outer corners slightly
for (px, py) in [(2, 9), (29, 9), (2, 27), (29, 27), (4, 5), (27, 5)]:
    c.set(px, py, None)

# --- Top plate metal face ---
c.rect(5, 6, 22, 3, METAL)

# Viewfinder window (rangefinder style)
c.rect(12, 5, 8, 5, OUT)
c.rect(13, 6, 6, 3, GLASS)
c.set(14, 6, GLASS_L)
c.set(15, 6, GLASS_L)

# Top plate highlight
c.line(6, 6, 11, 6, METAL_L)
c.line(20, 6, 25, 6, METAL_L)

# --- Leather body panel ---
c.rect(3, 10, 26, 17, LEATHER)

# Leather texture: scattered grain specks (avoid regular diagonal stripes)
for yy in range(11, 26):
    for xx in range(5, 27):
        n = (xx * 3 + yy * 5) % 7
        if n == 0:
            c.set(xx, yy, LEATHER_D)
        elif n == 4 and (xx * 5 + yy * 3) % 11 == 6:
            c.set(xx, yy, LEATHER_L)

# Soft top seam/highlight on the leather panel
c.line(5, 11, 26, 11, LEATHER_L)

# Small red self-timer lamp on the leather body
c.circle(7, 23, 1, RED)

# --- Lens ---
# Dark outline ring, then concentric metal and glass rings
c.circle(19, 18, 7, OUT)
c.circle(19, 18, 6, METAL)
c.circle(19, 18, 5, METAL_D)
c.circle(19, 18, 4, LENS_D)
c.circle(19, 18, 3, GLASS)

# Outer ring highlight (upper-left arc)
c.path("M 13 18 A 6 6 0 0 1 19 12", METAL_L, fill=False)

# Glass reflection
for (px, py) in [(17, 16), (18, 16), (17, 17)]:
    c.set(px, py, GLASS_L)

# --- Shutter button ---
c.circle(8, 4, 3, OUT)
c.circle(8, 4, 2, SHUTTER)
c.set(7, 3, METAL_L)

# Report
print(c.stats_text())
print(c.matrix_text())
finish(c)
