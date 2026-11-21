from pixelbench_api import *

# Frame 1: the original picture content (no slash trail)
f1 = input_canvas.copy(name='f1')

# Frame 2: shows the completed drawn-sword slash
# The character (left-handed, holding the sword in their left hand)
# has swept the sword from lower-left to upper-right, leaving a black slash trail.
f2 = input_canvas.copy(name='f2')

# Black colour for the slash trail
black = f2.color('#020202ff')

# The slash trail: a sweeping black arc from lower-left to upper-right
# where the sword has ended its motion with the completed slash.
# Multiple slightly offset curves give the trail visible thickness.

# Main slash stroke from lower-left curving up to the upper-right
f2.path('M 3,62 Q 14,40 24,28 Q 32,18 44,11', black, fill=False)

# Parallel strokes to thicken the trail
f2.path('M 5,63 Q 15,41 26,29 Q 33,20 45,13', black, fill=False)
f2.path('M 1,61 Q 13,39 22,27 Q 30,16 42,10', black, fill=False)
f2.path('M 4,62 Q 14,39 25,27 Q 31,18 43,11', black, fill=False)

# Additional outer flourish
f2.path('M 6,62 Q 16,40 27,28 Q 34,19 46,12', black, fill=False)

# Verify outputs
print("Frame 1:", f1.stats_text())
print("Frame 2:", f2.stats_text())

finish([f1, f2])
