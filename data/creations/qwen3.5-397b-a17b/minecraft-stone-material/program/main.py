from pixelbench_api import new_canvas, finish

# Create a 16x16 canvas for Minecraft-style cracked stone
c = new_canvas(16, 16, name="stone")

# Define a limited palette of 9 colors for cracked stone
crack = c.color((48, 48, 48), "crack")
shadow = c.color((68, 68, 68), "shadow")
dark = c.color((82, 82, 82), "dark")
mid_dark = c.color((96, 96, 96), "mid_dark")
base = c.color((115, 115, 115), "base")
mid_light = c.color((133, 133, 133), "mid_light")
light = c.color((150, 150, 150), "light")
highlight = c.color((168, 168, 168), "highlight")
bright = c.color((185, 185, 185), "bright")

# Fill with base
c.rect(0, 0, 16, 16, base)

# For seamless tiling: 
# - Row 0 must equal Row 15 (top/bottom wrap)
# - Col 0 must equal Col 15 (left/right wrap)
# - Corners: (0,0)=(15,0)=(0,15)=(15,15)

# Build the texture with explicit edge matching
# First define the wrap-around edge row/col

# Edge row (row 0 and row 15 will be identical)
edge_row = [
    mid_dark, dark, mid_light, base, light,
    mid_dark, shadow, base, mid_light, dark,
    base, light, mid_dark, highlight, base, mid_dark
]
for i, col in enumerate(edge_row):
    c.set(i, 0, col)
    c.set(i, 15, col)

# Edge column (col 0 and col 15 will be identical)
# Note: corners already set, so do rows 1-14
edge_col = [
    dark, mid_light, base, light,
    mid_dark, shadow, base, mid_light,
    dark, base, light, mid_dark, highlight, base
]
for i, col in enumerate(edge_col):
    c.set(0, i+1, col)
    c.set(15, i+1, col)

# Now fill interior (rows 1-14, cols 1-14)
# Design rows 1-7, then mirror to rows 14-8 for vertical symmetry
interior_rows = [
    # Row 1 (mirror to row 14)
    [base, shadow, mid_dark, base, light, mid_light, dark, base, shadow, mid_dark, light, base, mid_light, highlight],
    # Row 2 (mirror to row 13)
    [light, base, mid_dark, shadow, base, mid_light, highlight, dark, base, mid_dark, light, shadow, base, mid_light],
    # Row 3 (mirror to row 12)
    [mid_light, dark, base, shadow, mid_dark, light, base, highlight, mid_dark, shadow, base, dark, mid_light, light],
    # Row 4 (mirror to row 11)
    [base, mid_dark, light, shadow, base, mid_light, dark, base, highlight, mid_dark, shadow, light, base, mid_light],
    # Row 5 (mirror to row 10)
    [shadow, base, mid_light, dark, base, mid_dark, light, shadow, base, mid_light, dark, base, highlight, mid_dark],
    # Row 6 (mirror to row 9)
    [base, mid_dark, shadow, light, base, mid_light, dark, base, shadow, mid_dark, light, base, mid_light, highlight],
    # Row 7 (mirror to row 8)
    [mid_light, base, dark, shadow, mid_dark, base, light, mid_light, base, dark, shadow, mid_dark, base, light],
]

for row_idx, row_data in enumerate(interior_rows):
    y = row_idx + 1
    y_mirror = 14 - row_idx
    for x, col in enumerate(row_data):
        c.set(x + 1, y, col)
        c.set(x + 1, y_mirror, col)

# Now add cracks - keeping them away from edges (stay within cols 2-13, rows 2-13)
# Main crack running diagonally
main_crack = [
    (4, 3), (5, 4), (6, 4), (7, 5), (8, 6), (9, 7),
    (9, 8), (10, 9), (10, 10), (11, 11),
]
for x, y in main_crack:
    c.set(x, y, crack)
    # Add depth with shadow neighbors
    if y+1 < 15: c.set(x, y+1, shadow)
    if x+1 < 15: c.set(x+1, y, shadow)

# Secondary crack from upper area
secondary_crack = [
    (11, 3), (10, 4), (9, 5), (8, 6), (7, 7),
    (6, 8), (5, 9), (5, 10), (6, 11),
]
for x, y in secondary_crack:
    c.set(x, y, crack)
    if x+1 < 15: c.set(x+1, y, shadow)

# Small crack fragments
fragments = [
    (3, 5), (3, 6), (4, 7),
    (12, 5), (12, 6), (11, 7),
    (3, 10), (4, 11),
    (11, 10), (12, 11),
    (6, 3), (7, 3), (8, 4),
]
for x, y in fragments:
    c.set(x, y, crack)

# Highlights near cracks for depth
hl = [
    (4, 4, bright), (7, 6, bright), (9, 8, bright),
    (10, 5, bright), (6, 9, bright), (5, 11, bright),
    (12, 4, highlight), (4, 12, highlight),
]
for x, y, col in hl:
    c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text())

# Verify edges match
row0 = [c.get(x, 0) for x in range(16)]
row15 = [c.get(x, 15) for x in range(16)]
col0 = [c.get(0, y) for y in range(16)]
col15 = [c.get(15, y) for y in range(16)]
print(f"Row 0 == Row 15: {row0 == row15}")
print(f"Col 0 == Col 15: {col0 == col15}")

finish(c)
