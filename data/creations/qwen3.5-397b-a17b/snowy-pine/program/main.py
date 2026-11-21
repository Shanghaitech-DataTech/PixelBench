# Create output canvas as a copy of input
output = input_canvas.copy(name='output')

# Register white color for snow
white_idx = output.color('#ffffff')

# Get dimensions using stats
stats = output.stats()
w, h = stats['size']

# Strategy: Add snow on top of the tree branches
# For each column, find the topmost tree pixel and add snow above it

for x in range(w):
    # Find all tree pixels in this column (non-transparent = index != 0)
    tree_pixels = []
    for y in range(h):
        idx = output.get(x, y)
        if idx != 0:  # Not transparent
            tree_pixels.append(y)
    
    if tree_pixels:
        # Find the topmost tree pixel
        top_y = min(tree_pixels)
        
        # Add snow cap above the tree (2-4 pixels thick depending on position)
        # Calculate distance from center for variation
        center_x = w // 2
        dist_from_center = abs(x - center_x)
        
        # Make cap thicker near the center of the tree
        if dist_from_center < 15:
            cap_thickness = 4
        elif dist_from_center < 25:
            cap_thickness = 3
        elif dist_from_center < 35:
            cap_thickness = 2
        else:
            cap_thickness = 1
        
        # Add snow cap
        for dy in range(cap_thickness):
            snow_y = top_y - 1 - dy
            if snow_y >= 0:
                output.set(x, snow_y, white_idx)

# Also add snow on horizontal branch surfaces within the tree
# Look for places where there's tree below but empty space above
for x in range(w):
    for y in range(1, h-1):
        current = output.get(x, y)
        above = output.get(x, y-1)
        below = output.get(x, y+1) if y+1 < h else 0
        
        # If current is tree, above is empty (transparent), and below is tree
        # This is a horizontal surface that could accumulate snow
        if current != 0 and current != white_idx and above == 0 and below != 0:
            # Add snow on top (1-2 pixels)
            output.set(x, y-1, white_idx)
            if y-2 >= 0:
                output.set(x, y-2, white_idx)

# Add some additional snow "drifts" - thicker accumulation in concave areas
for x in range(1, w-1):
    for y in range(2, h-1):
        current = output.get(x, y)
        left = output.get(x-1, y)
        right = output.get(x+1, y)
        above_left = output.get(x-1, y-1) if y-1 >= 0 else 0
        above_right = output.get(x+1, y-1) if y-1 >= 0 else 0
        above = output.get(x, y-1) if y-1 >= 0 else 0
        
        # If we're in a "valley" - tree on both sides and above, but empty here
        if current == 0 and left != 0 and right != 0 and above != 0:
            # This is a concave area - add snow drift
            output.set(x, y, white_idx)
            if y-1 >= 0:
                output.set(x, y-1, white_idx)

print("Snow added!")
print(f"Final stats: {output.stats()}")

finish(output)
