from pixelbench_api import *

# Frame 1: Keep the original picture
f1 = input_canvas.copy(name="frame1")

# Frame 2: Create a fresh copy and modify for punching motion
f2 = input_canvas.copy(name="frame2")

# Reset f2 to original
f2 = input_canvas.copy(name="frame2")

# Clear the forearm and fist area (cols 17-25, rows 15-21)
f2.clear(x=17, y=15, w=10, h=8)

# Draw a cleaner extended arm for the punch
# The arm should flow from upper arm (left) to fist (right)

# Row 15: top of extended arm
f2.set(17, 15, 5)  # e - sleeve continues
f2.set(18, 15, 5)
f2.set(19, 15, 5)
f2.set(20, 15, 3)  # c - skin
f2.set(21, 15, 3)

# Row 16: arm/forearm
f2.set(17, 16, 5)  # e
f2.set(18, 16, 5)
f2.set(19, 16, 5)
f2.set(20, 16, 3)  # c
f2.set(21, 16, 3)

# Row 17: forearm
f2.set(17, 17, 5)
f2.set(18, 17, 5)
f2.set(19, 17, 3)
f2.set(20, 17, 3)
f2.set(21, 17, 3)

# Row 18: forearm/wrist
f2.set(17, 18, 5)
f2.set(18, 18, 5)
f2.set(19, 18, 3)
f2.set(20, 18, 3)
f2.set(21, 18, 3)

# Row 19: wrist
f2.set(17, 19, 5)
f2.set(18, 19, 3)
f2.set(19, 19, 3)
f2.set(20, 19, 3)

# Fist at cols 22-26 (orange glove with brown knuckles)
# Row 16: top of fist
f2.set(22, 16, 5)
f2.set(23, 16, 5)
f2.set(24, 16, 5)
f2.set(25, 16, 5)

# Row 17: middle of fist
f2.set(22, 17, 5)
f2.set(23, 17, 5)
f2.set(24, 17, 6)  # brown knuckle
f2.set(25, 17, 5)

# Row 18: lower fist
f2.set(22, 18, 5)
f2.set(23, 18, 5)
f2.set(24, 18, 5)
f2.set(25, 18, 5)

# Row 19: bottom of fist
f2.set(22, 19, 5)
f2.set(23, 19, 5)
f2.set(24, 19, 6)
f2.set(25, 19, 5)

# Outline around fist (color 1 - dark purple)
f2.set(22, 15, 1)
f2.set(23, 15, 1)
f2.set(24, 15, 1)
f2.set(25, 15, 1)
f2.set(26, 16, 1)
f2.set(26, 17, 1)
f2.set(26, 18, 1)
f2.set(25, 20, 1)
f2.set(24, 20, 1)
f2.set(23, 20, 1)
f2.set(22, 20, 1)

# Fill in any gaps to make the arm solid
# Row 16: ensure connection
f2.set(21, 16, 3)  # wrist connects to fist

print("Frame 2 stats:", f2.stats_text())
print("Frame 2 matrix (arm area):")
print(f2.matrix_text(region=(12, 14, 28, 24)))

# Submit the frames
finish([f1, f2])
