from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16)

RIM = "#3A3A4E"
GLASS = "#A9D8F2"
GLASS_D = "#7FBEE4"
HL = "#FFFFFF"
WOOD = "#8A5A2B"
WOOD_D = "#4E2E12"
BAND = "#D9A93F"

# --- lens ---
c.circle(7, 6, 4, RIM)      # rim disc
c.circle(7, 6, 3, GLASS)    # glass interior

# shade lower-right of glass
c.circle(8, 7, 2, GLASS_D)

# highlight sparkle (inside glass, upper-left)
c.set(5, 4, HL)
c.set(6, 4, HL)
c.set(5, 5, HL)

# --- handle connecting band (gold) ---
c.set(8, 9, BAND)
c.set(9, 9, BAND)
c.set(8, 10, BAND)
c.set(9, 10, BAND)

# --- handle shaft: 2-wide diagonal bar, lit from above ---
for x in range(10, 16):
    c.set(x, x - 1, WOOD)   # upper edge (light)
    c.set(x, x, WOOD_D)     # lower edge (shade)

print(c.stats_text())
print(c.matrix_text(indices=True))

finish(c)

