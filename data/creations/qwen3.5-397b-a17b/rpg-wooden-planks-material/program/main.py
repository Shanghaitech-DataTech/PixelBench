from pixelbench_api import *

# Create 16x16 canvas for wooden planks tile
c = new_canvas(16, 16)

# Define wood color palette
# Dark seam/groove colors
seam_dark = c.color('#3d2817')  # Very dark brown for deep grooves
seam_mid = c.color('#5c3a21')   # Medium dark for seam edges

# Wood base colors - alternating planks
wood_dark_base = c.color('#8b5a2b')   # Dark wood base
wood_mid_base = c.color('#a06b33')    # Medium wood base
wood_light_base = c.color('#b87d42')  # Light wood base

# Wood grain variations
grain_dark = c.color('#6b4423')       # Dark grain lines
grain_mid = c.color('#7d5330')        # Medium grain
grain_light = c.color('#c48950')      # Light grain highlights

# Knot colors
knot_dark = c.color('#2a1a0f')        # Very dark knot center
knot_mid = c.color('#4a2f1a')         # Knot middle

# Board end variations (alternating light/dark)
end_dark = c.color('#6d4520')         # Dark board end
end_light = c.color('#c99355')        # Light board end

# Draw 4 vertical planks (4 pixels wide each)
# Plank boundaries at x=0,4,8,12,16

# Fill base colors for each plank (alternating)
# Plank 0 (x=0-3): medium base
c.rect(0, 0, 4, 16, wood_mid_base)
# Plank 1 (x=4-7): light base
c.rect(4, 0, 4, 16, wood_light_base)
# Plank 2 (x=8-11): medium base
c.rect(8, 0, 4, 16, wood_mid_base)
# Plank 3 (x=12-15): light base
c.rect(12, 0, 4, 16, wood_light_base)

# Draw dark seams between planks (1 pixel wide grooves)
# Seam at x=3-4, 7-8, 11-12
c.rect(3, 0, 1, 16, seam_dark)
c.rect(7, 0, 1, 16, seam_dark)
c.rect(11, 0, 1, 16, seam_dark)

# Add seam edge highlights (one side of each seam)
c.rect(4, 0, 1, 16, seam_mid)
c.rect(8, 0, 1, 16, seam_mid)
c.rect(12, 0, 1, 16, seam_mid)

# Add wood grain lines (vertical, wavy)
# Plank 0 grain
c.set(1, 2, grain_dark)
c.set(1, 5, grain_mid)
c.set(2, 8, grain_dark)
c.set(1, 11, grain_light)
c.set(2, 14, grain_mid)

# Plank 1 grain
c.set(5, 1, grain_mid)
c.set(6, 4, grain_dark)
c.set(5, 7, grain_light)
c.set(6, 10, grain_dark)
c.set(5, 13, grain_mid)

# Plank 2 grain
c.set(9, 3, grain_dark)
c.set(10, 6, grain_mid)
c.set(9, 9, grain_light)
c.set(10, 12, grain_dark)
c.set(9, 15, grain_mid)

# Plank 3 grain
c.set(13, 2, grain_mid)
c.set(14, 5, grain_dark)
c.set(13, 8, grain_light)
c.set(14, 11, grain_dark)
c.set(13, 14, grain_mid)

# Add wood knots (small irregular shapes)
# Knot 1 - on plank 1
c.set(5, 3, knot_dark)
c.set(6, 3, knot_mid)
c.set(5, 4, knot_mid)
c.set(6, 4, knot_dark)

# Knot 2 - on plank 2
c.set(9, 10, knot_dark)
c.set(10, 10, knot_mid)
c.set(9, 11, knot_mid)
c.set(8, 10, knot_dark)

# Knot 3 - on plank 0
c.set(1, 7, knot_mid)
c.set(2, 7, knot_dark)
c.set(1, 8, knot_dark)

# Add alternating board end highlights (top and bottom) - matching for vertical tiling
# Top row alternating
c.set(0, 0, end_light)
c.set(1, 0, end_light)
c.set(5, 0, end_dark)
c.set(6, 0, end_dark)
c.set(9, 0, end_light)
c.set(10, 0, end_light)
c.set(13, 0, end_dark)
c.set(14, 0, end_dark)

# Bottom row - SAME as top for vertical seamless tiling
c.set(0, 15, end_light)
c.set(1, 15, end_light)
c.set(5, 15, end_dark)
c.set(6, 15, end_dark)
c.set(9, 15, end_light)
c.set(10, 15, end_light)
c.set(13, 15, end_dark)
c.set(14, 15, end_dark)

# Add some horizontal grain variation for texture
c.set(0, 4, grain_light)
c.set(2, 6, grain_dark)
c.set(0, 10, grain_mid)
c.set(2, 12, grain_light)

c.set(5, 6, grain_light)
c.set(7, 9, grain_dark)
c.set(5, 15, grain_mid)

c.set(8, 2, grain_light)
c.set(10, 5, grain_dark)
c.set(8, 14, grain_mid)

c.set(12, 3, grain_light)
c.set(14, 7, grain_dark)
c.set(12, 10, grain_mid)
c.set(15, 13, grain_light)

# Ensure seamless tiling - make left and right edges match for horizontal tiling
# The leftmost plank (x=0-2) should match the rightmost area (x=13-15)
# Copy column 0 pattern to column 15, column 1 to 14, etc.
for y in range(16):
    col0 = c.get(0, y)
    col1 = c.get(1, y)
    col2 = c.get(2, y)
    # Mirror to right side for seamless tiling
    c.set(15, y, col0)
    c.set(14, y, col1)
    c.set(13, y, col2)

# Check stats
print(c.stats_text())
print(c.matrix_text())

# Submit the result
finish(c)
