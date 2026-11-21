from pixelbench_api import *

# Create a 16x16 canvas for the magnifying glass icon
c = new_canvas(16, 16)

# Define colors
dark_frame = c.color("#4a4a4a", "dark_frame")  # Dark gray for frame
lens_glass = c.color("#c0e8f8", "lens_glass")  # Light blue for glass
lens_highlight = c.color("#ffffff", "highlight")  # White highlight
handle_color = c.color("#8b5a2b", "handle")  # Brown for handle
handle_shadow = c.color("#5c3a1a", "handle_shadow")  # Darker brown for shadow

# Draw the circular lens frame - center at (6, 6), radius 5
c.circle(6, 6, 5, dark_frame, fill=False)

# Fill the lens with glass color (radius 4 to leave frame visible)
c.circle(6, 6, 4, lens_glass, fill=True)

# Add a highlight/reflection on the lens (upper-left quadrant)
c.circle(4, 4, 2, lens_highlight, fill=True)

# Draw the handle - extends from bottom-right of the lens
# Handle starts at frame and goes diagonally down-right
# Make a clean 2-pixel wide handle with slight curve

# Handle pixels - starting from frame at (9,9) going to (14,14)
c.set(9, 9, handle_color)
c.set(10, 9, handle_color)
c.set(10, 10, handle_color)
c.set(11, 10, handle_color)
c.set(11, 11, handle_color)
c.set(12, 11, handle_color)
c.set(12, 12, handle_color)
c.set(13, 12, handle_color)
c.set(13, 13, handle_color)
c.set(14, 13, handle_color)
c.set(14, 14, handle_color)

# Add shadow detail down the center of handle
c.set(10, 10, handle_shadow)
c.set(11, 11, handle_shadow)
c.set(12, 12, handle_shadow)
c.set(13, 13, handle_shadow)

# Ensure clean connection to frame
c.set(9, 8, dark_frame)

# Check the result
print(c.stats_text())
print(c.matrix_text())

# Submit the canvas
finish(c)
