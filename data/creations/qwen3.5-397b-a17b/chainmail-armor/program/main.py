from pixelbench_api import *

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32)

# Define colors for chainmail
dark_outline = c.color("#181828")
metal_dark = c.color("#383848")
metal_mid = c.color("#585868")
metal_base = c.color("#787888")
metal_light = c.color("#9898a8")
metal_bright = c.color("#b8b8c8")

def draw_ring(cx, cy, r, shade_idx):
    """Draw a chainmail ring - filled circle with shading"""
    colors = [metal_dark, metal_mid, metal_base, metal_light, metal_bright]
    idx = shade_idx % len(colors)
    
    # Main ring body - filled circle
    c.circle(cx, cy, r, colors[idx], fill=True)
    
    # Dark outline around each ring for definition
    c.circle(cx, cy, r, dark_outline, fill=False)
    
    # Small highlight on top-left for metallic effect
    if r >= 2:
        c.set(cx - 1, cy - 1, metal_bright)

# Chainmail pattern - interlocking rings in offset rows
# European chainmail style

ring_r = 2
h_gap = 5
v_gap = 4

# Main armor body rows (wider in middle, narrower at top/bottom)
main_rows = [
    (6, 4, 8),    # y, num_rings, x_start
    (10, 5, 6),
    (14, 6, 4),
    (18, 7, 2),
    (22, 7, 2),
    (26, 6, 4),
    (30, 4, 8),
]

shade_offset = 0
for row_idx, (y, num_rings, x_start) in enumerate(main_rows):
    for col in range(num_rings):
        x = x_start + col * h_gap
        if 2 <= x < 30 and 2 <= y < 30:
            shade = (shade_offset + col + row_idx * 2) % 5
            draw_ring(x, y, ring_r, shade)
    shade_offset += 1

# Connecting rows (offset to interlock)
connect_rows = [
    (8, 4, 11),
    (12, 5, 9),
    (16, 6, 7),
    (20, 7, 5),
    (24, 6, 7),
    (28, 4, 11),
]

shade_offset = 2
for row_idx, (y, num_rings, x_start) in enumerate(connect_rows):
    for col in range(num_rings):
        x = x_start + col * h_gap
        if 2 <= x < 30 and 2 <= y < 30:
            shade = (shade_offset + col + row_idx * 2) % 5
            draw_ring(x, y, ring_r, shade)
    shade_offset += 1

# Add dark outline around the entire piece
c.outline(dark_outline)

# Add subtle edge shading
for x in range(6, 26):
    c.set(x, 6, metal_dark)
    c.set(x, 29, metal_dark)

print(c.stats_text())
print(c.matrix_text())

finish(c)
