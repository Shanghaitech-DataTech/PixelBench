from pixelbench_api import *

# Both frames need to have the same dimensions
canvas_width = 100
canvas_height = 100

# Frame 1: Copy of original, placed on a canvas of the final size
f1 = new_canvas(canvas_width, canvas_height, background=None, name="frame1")
# Place original at position that makes sense - center it a bit
f1.blit(input_canvas, 20, 10)

# Frame 2: Same base, but with the slash added
f2 = new_canvas(canvas_width, canvas_height, background=None, name="frame2")
f2.blit(input_canvas, 20, 10)

# Register black color
black = f2.color("#000000ff")

# The slash should be a visible trail from the sword motion
# From lower left to upper right
# Let's make it thinner and positioned so it doesn't cover the character too much

# The character is at (20,10) to (81,81)
# The slash should sweep from lower left (outside character) to upper right
# Let's draw it more to the left side, arcing up

# Draw a thinner slash - just a few parallel lines
slash_points = [(10, 85), (25, 60), (45, 35), (65, 15), (80, 5)]

# Draw the slash as connected line segments, thinner
for offset in range(-2, 3):
    prev = None
    for pt in slash_points:
        curr = (pt[0] + offset, pt[1])
        if prev:
            f2.line(prev[0], prev[1], curr[0], curr[1], black)
        prev = curr

# Also add some filled circles at key points to emphasize the motion
f2.circle(10, 85, 2, black, fill=True)
f2.circle(45, 35, 2, black, fill=True)
f2.circle(80, 5, 2, black, fill=True)

print("Frame 1 stats:", f1.stats_text())
print("Frame 2 stats:", f2.stats_text())

# Submit both frames
finish([f1, f2])
