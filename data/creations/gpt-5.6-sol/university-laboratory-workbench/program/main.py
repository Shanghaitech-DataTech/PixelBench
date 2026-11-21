from pixelbench_api import *

# University laboratory workbench, 64x64 pixel art.
c = new_canvas(64, 64, background="#d7e2dc", name="university-laboratory-workbench")

# Palette
wall = "#d7e2dc"
tile = "#b8ccc8"
tile_hi = "#edf3ec"
ink = "#26383b"
ink2 = "#40585a"
steel = "#718b89"
steel_hi = "#a8bbb5"
bench = "#8b5c3f"
bench_hi = "#b27a52"
bench_dark = "#513a30"
shadow = "#34474a"
white = "#f5f0db"
paper = "#eee8ce"
paper_shade = "#c9c3a9"
blue = "#3d7185"
blue_hi = "#7fb2ba"
cyan = "#a9d9d5"
green = "#4f8a68"
green_hi = "#83b879"
red = "#a94742"
orange = "#d38a3f"
yellow = "#e0bc58"
purple = "#6d5a82"
glass = "#bedbd2"

# Wall tiles and grout.
for x in range(0, 64, 8):
    c.line(x, 0, x, 28, tile)
for y in (8, 16, 24):
    c.line(0, y, 63, y, tile)
# Subtle tile glints.
for x, y in [(2,2),(18,10),(35,3),(51,11),(10,19),(42,19)]:
    c.rect(x, y, 3, 1, tile_hi)

# Rear shelf, supports, and small reagent bottles.
c.rect(3, 5, 27, 2, ink)
c.rect(4, 7, 25, 2, steel)
c.rect(5, 9, 2, 9, ink2)
c.rect(27, 9, 2, 9, ink2)
# Shelf bottles: distinct silhouettes and color bands.
for x, body, cap in [(8, green, ink), (14, orange, red), (21, blue, purple)]:
    c.rect(x+1, 10, 3, 2, cap)
    c.rect(x, 12, 5, 6, ink)
    c.rect(x+1, 13, 3, 4, body)
    c.set(x+1, 13, white)
    c.rect(x+1, 15, 3, 1, paper)
# One squat labeled jar.
c.rect(32, 9, 5, 2, ink)
c.rect(31, 11, 7, 7, ink)
c.rect(32, 12, 5, 5, white)
c.rect(32, 14, 5, 2, yellow)
c.set(33, 12, tile_hi)

# Bench back lip and work surface.
c.rect(0, 27, 64, 3, bench_dark)
c.rect(0, 30, 64, 20, bench)
c.rect(0, 30, 64, 3, bench_hi)
c.line(0, 49, 63, 49, ink)
c.rect(0, 50, 64, 14, bench_dark)
c.rect(3, 52, 19, 12, "#664733")
c.rect(42, 52, 19, 12, "#664733")
c.rect(24, 52, 16, 2, "#6f4c36")
# Drawer pulls.
c.rect(9, 55, 7, 2, ink)
c.rect(48, 55, 7, 2, ink)

# Microscope shadow.
c.ellipse(19, 46, 14, 3, "#684832")
# Microscope base, stepped and heavy.
c.poly([(7,45),(9,41),(25,41),(30,45),(29,48),(8,48)], ink)
c.rect(10, 42, 16, 3, steel)
c.rect(12, 41, 11, 2, steel_hi)
c.rect(10, 46, 18, 1, ink2)
# Curved microscope arm.
c.path("M13 41 L13 34 Q13 24 23 21 L27 24 Q19 27 19 35 L19 41 Z", ink, fill=True)
c.path("M15 39 L15 34 Q15 27 22 24 L23 26 Q18 29 18 35 L18 39 Z", steel, fill=True)
c.set(16, 29, steel_hi)
c.set(17, 27, steel_hi)
# Upright joint and focus wheels.
c.rect(24, 20, 5, 14, ink)
c.rect(25, 21, 3, 12, steel)
c.circle(29, 29, 3, ink)
c.circle(29, 29, 1, steel_hi)
c.circle(23, 31, 2, ink2)
c.set(23, 31, steel_hi)
# Angled eyepiece and objective body.
c.poly([(20,17),(30,17),(31,20),(28,23),(24,22),(26,20),(20,20)], ink)
c.rect(20, 17, 7, 2, steel_hi)
c.rect(18, 16, 7, 2, ink)
c.rect(18, 15, 5, 1, steel)
c.poly([(24,22),(29,23),(28,29),(23,28)], ink)
c.poly([(25,23),(28,24),(27,27),(24,27)], steel_hi)
# Objective turret and lenses.
c.rect(21, 28, 9, 3, ink)
c.rect(22, 31, 2, 5, steel)
c.rect(27, 31, 2, 6, steel)
c.rect(22, 35, 2, 2, ink)
c.rect(27, 36, 2, 2, ink)
# Stage and slide.
c.rect(8, 35, 18, 3, ink)
c.rect(10, 34, 13, 2, steel)
c.rect(14, 34, 8, 1, cyan)
c.set(18, 34, red)
c.rect(11, 38, 2, 4, ink2)
c.rect(23, 38, 2, 4, ink2)

# Test-tube rack on right, perspective rails and legs.
c.rect(39, 38, 21, 3, ink)
c.rect(41, 39, 17, 1, bench_hi)
c.rect(40, 46, 20, 3, ink)
c.rect(42, 46, 16, 1, steel)
c.rect(41, 48, 3, 3, ink2)
c.rect(56, 48, 3, 3, ink2)
# Tubes, outlined with colored liquids and highlights.
for x, liquid in [(42, blue),(47, green),(52, orange),(57, purple)]:
    c.rect(x, 32, 4, 15, ink)
    c.rect(x+1, 33, 2, 12, glass)
    c.set(x+1, 34, tile_hi)
    c.rect(x+1, 40, 2, 5, liquid)
    c.set(x+2, 40, white)
    c.rect(x-1, 31, 6, 2, ink)
    c.rect(x, 31, 4, 1, tile_hi)

# Tall wash/reagent bottle behind the rack.
c.rect(52, 19, 7, 2, ink)
c.rect(53, 21, 5, 3, blue)
c.rect(50, 24, 11, 10, ink)
c.rect(51, 25, 9, 8, cyan)
c.rect(52, 26, 2, 6, tile_hi)
c.rect(53, 28, 6, 3, white)
c.rect(55, 29, 2, 1, blue)

# Dropper lying diagonally: rubber bulb, glass pipette, bright fluid tip.
c.poly([(31,35),(34,32),(37,35),(34,38)], purple)
c.poly([(30,34),(33,31),(35,33),(32,36)], ink)
c.line(34, 36, 40, 42, ink)
c.line(35, 36, 41, 42, glass)
c.set(41, 43, red)
c.set(42, 44, red)

# Open notebook in foreground, strong page silhouette and central binding.
c.poly([(18,49),(31,47),(32,50),(32,61),(18,59),(14,52)], ink)
c.poly([(32,50),(46,47),(51,51),(47,59),(32,61)], ink)
c.poly([(18,50),(31,48),(31,59),(19,57),(16,52)], paper)
c.poly([(33,50),(45,48),(49,51),(46,57),(33,59)], white)
c.line(32, 50, 32, 60, bench_dark)
c.line(31, 50, 31, 58, paper_shade)
# Page corners and ruled notes/diagram marks.
c.line(19, 52, 28, 51, blue)
c.line(20, 54, 29, 53, steel)
c.line(21, 56, 28, 55, steel)
c.circle(25, 52, 2, red, fill=False)
c.line(35, 52, 44, 51, blue)
c.line(35, 54, 45, 53, steel)
c.line(36, 56, 42, 55, steel)
c.line(44, 54, 46, 56, red)
c.line(46, 54, 44, 56, red)
# Binding stitches.
for y in (51,54,57):
    c.set(32, y, yellow)

# A few crisp highlights and bench marks.
c.set(4, 32, bench_hi)
c.line(1, 35, 7, 35, "#986748")
c.line(60, 36, 63, 36, bench_hi)

view(c, scale=8, margin=0)
finish(c)
