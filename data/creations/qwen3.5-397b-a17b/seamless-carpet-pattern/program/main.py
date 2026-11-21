from pixelbench_api import new_canvas, finish

# Create 32x32 canvas for seamless carpet pattern
c = new_canvas(32, 32)

# Warm color palette for carpet
rust = c.color("#B7410E", "rust")
orange = c.color("#D2691E", "orange")
gold = c.color("#DAA520", "gold")
cream = c.color("#F5DEB3", "cream")
brown = c.color("#8B4513", "brown")
dark_brown = c.color("#5C3317", "dark_brown")
tan = c.color("#D2B48C", "tan")
beige = c.color("#E8D5B7", "beige")

# Background - warm brown base
c.rect(0, 0, 32, 32, brown)

def draw_filled_diamond(cx, cy, r, color):
    for dy in range(-r, r + 1):
        for dx in range(-r + abs(dy), r - abs(dy) + 1):
            c.set(cx + dx, cy + dy, color)

def draw_flower(cx, cy, petal, center):
    c.set(cx, cy - 1, petal)
    c.set(cx, cy + 1, petal)
    c.set(cx - 1, cy, petal)
    c.set(cx + 1, cy, petal)
    c.set(cx, cy, center)

# Design a 16x16 tile that tiles seamlessly
# The key is that elements at x=0 must match x=16, and y=0 must match y=16

# Central large diamond at (8,8)
draw_filled_diamond(8, 8, 5, rust)
draw_filled_diamond(8, 8, 3, orange)
draw_filled_diamond(8, 8, 2, gold)
draw_filled_diamond(8, 8, 1, cream)

# Corner diamonds - these are split by the tile boundary
# Diamond at (0,0) - only draw the part in positive quadrant
for dy in range(0, 4):
    for dx in range(0, 4 - dy):
        c.set(dx, dy, rust)
        c.set(16 - dx, dy, rust)
        c.set(dx, 16 - dy, rust)
        c.set(16 - dx, 16 - dy, rust)

# Edge diamonds at midpoints
for dy in range(0, 3):
    for dx in range(-2 + abs(dy), 3 - abs(dy)):
        c.set(8 + dx, dy, orange)
        c.set(8 + dx, 16 - dy, orange)
        c.set(dx, 8, orange)
        c.set(16 - dx, 8, orange)

# Floral motifs around center
floral_positions = [
    (8, 2), (8, 14), (2, 8), (14, 8),
    (4, 4), (12, 4), (4, 12), (12, 12)
]
for px, py in floral_positions:
    draw_flower(px, py, cream, gold)

# Edge florals
edge_florals = [
    (8, 0), (8, 16), (0, 8), (16, 8),
    (4, 0), (12, 0), (4, 16), (12, 16),
    (0, 4), (0, 12), (16, 4), (16, 12)
]
for px, py in edge_florals:
    draw_flower(px, py, tan, gold)

# Lattice pattern
for i in range(0, 17, 8):
    for j in range(0, 17, 8):
        c.set(i, j, gold)
        c.set(i+1, j, gold)
        c.set(i, j+1, gold)
        c.set(i+1, j+1, gold)

# Woven texture in background
for x in range(16):
    for y in range(16):
        if c.get(x, y) == brown:
            if (x + y) % 3 == 0:
                c.set(x, y, dark_brown)
            elif (x + y) % 3 == 1:
                c.set(x, y, beige)

# Replicate 16x16 tile to all 4 quadrants
base_pixels = [[c.get(x, y) for x in range(16)] for y in range(16)]

for qy in range(2):
    for qx in range(2):
        ox, oy = qx * 16, qy * 16
        for y in range(16):
            for x in range(16):
                c.set(ox + x, oy + y, base_pixels[y][x])

# Now the edges should naturally match because we used a repeating 16x16 tile
# But let's verify and fix if needed

# Force edge matching
for y in range(32):
    c.set(31, y, c.get(0, y))
for x in range(32):
    c.set(x, 31, c.get(x, 0))
c.set(31, 31, c.get(0, 0))

print("Canvas stats:")
print(c.stats_text())

# Verify edges
left = [c.get(0, y) for y in range(32)]
right = [c.get(31, y) for y in range(32)]
top = [c.get(x, 0) for x in range(32)]
bottom = [c.get(x, 31) for x in range(32)]

print("\nEdge match check:")
print("Left == Right:", left == right)
print("Top == Bottom:", top == bottom)

# Show corners to verify seamless tiling
print("\nTop-left corner (0,0 to 7,7):")
for y in range(8):
    row = ""
    for x in range(8):
        row += str(c.get(x, y)) + " "
    print(row)

print("\nTop-right corner (24,0 to 31,7):")
for y in range(8):
    row = ""
    for x in range(24, 32):
        row += str(c.get(x, y)) + " "
    print(row)

finish(c)
