from pixelbench_api import *

# ===== Colours from the input palette =====
OUTLINE = 1       # #222034 - dark navy outline
DARK_HAIR = 2     # #45283c
SKIN = 3          # #eec39a - light peach skin
DARK_RED = 4      # #663931
ORANGE = 5        # #df7126 - bright orange (armor/clothing)
BROWN = 6         # #8f563b
GRAY = 7          # #847e87
DARK_BLUE = 8     # #3f3f74
MED_BLUE = 9       # #5b6ee1
LIGHT_BLUE = 10   # #cbdbfc

# Original input is 29x44
w = 40
h = 44

# ===== FRAME 1: original picture content =====
f1 = new_canvas(w, h, name="frame1")
f1.blit(input_canvas, 0, 0)

# ===== FRAME 2: left fist throwing a light punch =====
f2 = new_canvas(w, h, name="frame2")
f2.blit(input_canvas, 0, 0)

# === Replace the arm region for the punch ===
# The arm area is roughly cols 10-28, rows 8-15
# Keep the arm from the body but extend it right with a proper fist

# Clear the arm that extends to the right
for yy in range(8, 16):
    for xx in range(12, 30):
        f2.set(xx, yy, None)

# === Draw extended arm ===

# Extend the arm horizontally for a light punch
# Arm extends from about col 12 to col 25, with a fist at col 26-31

# Upper arm top/outline
for col in range(11, 26):
    f2.set(col, 9, OUTLINE)

# Arm body
for col in range(11, 26):
    f2.set(col, 10, ORANGE)
    f2.set(col, 11, ORANGE)
    f2.set(col, 12, ORANGE)
    f2.set(col, 13, ORANGE)

# Arm bottom/outline
for col in range(11, 25):
    f2.set(col, 14, OUTLINE)

# Add shading/details within the arm
for col in range(12, 24):
    if col % 3 == 1:
        f2.set(col, 12, BROWN)
    if col % 2 == 0:
        f2.set(col, 11, BROWN)

# === Fist ===
# Compact fist at the end of the arm
fist_start = 26
fist_end = 33

# Fist at cols 26-33, rows 9-15

# Fist outline - perimeter
f2.set(fist_start, 9, OUTLINE)
f2.set(fist_start+1, 9, SKIN)
f2.set(fist_start+2, 9, SKIN)
f2.set(fist_start+3, 9, OUTLINE)

f2.set(fist_start, 10, SKIN)
f2.set(fist_start+1, 10, SKIN)
f2.set(fist_start+2, 10, SKIN)
f2.set(fist_start+3, 10, OUTLINE)

f2.set(fist_start, 11, SKIN)
f2.set(fist_start+1, 11, OUTLINE)
f2.set(fist_start+2, 11, SKIN)
f2.set(fist_start+3, 11, SKIN)

f2.set(fist_start, 12, SKIN)
f2.set(fist_start+1, 12, OUTLINE)
f2.set(fist_start+2, 12, SKIN)
f2.set(fist_start+3, 12, SKIN)

f2.set(fist_start, 13, SKIN)
f2.set(fist_start+1, 13, SKIN)
f2.set(fist_start+2, 13, OUTLINE)
f2.set(fist_start+3, 13, OUTLINE)

f2.set(26, 14, OUTLINE)
f2.set(27, 14, OUTLINE)
f2.set(28, 14, OUTLINE)
f2.set(29, 14, OUTLINE)

# Small fist bumps (knuckles)
f2.set(28, 8, OUTLINE)
f2.set(29, 8, OUTLINE)

# Connect arm to fist
f2.set(26, 10, SKIN)
f2.set(25, 10, ORANGE)
f2.set(25, 11, ORANGE)
f2.set(25, 12, ORANGE)
f2.set(25, 13, SKIN)
f2.set(25, 14, OUTLINE)
f2.set(24, 10, ORANGE)
f2.set(26, 9, OUTLINE)

# Motion blur/speed lines
f2.set(34, 9, OUTLINE)
f2.set(35, 10, OUTLINE)
f2.set(35, 11, OUTLINE)
f2.set(36, 11, OUTLINE)
f2.set(36, 12, OUTLINE)
f2.set(35, 12, OUTLINE)
f2.set(34, 13, OUTLINE)
f2.set(36, 13, OUTLINE)

# Make sure arm from original is properly connected
# The connection from the body to the extended arm

print("=== Frame 2 arm/fist detail (cols 9-37, rows 7-16) ===")
for yy in range(7, 17):
    row = []
    for xx in range(9, 38):
        val = f2.get(xx, yy)
        row.append(val)
    print(f"  row {yy}: {row}")

print()
print("=== Frame 2 full matrix ===")
s = f2.stats()
w2, h2 = s['size']
print(f2.matrix_text(region=(0, 0, w2-1, h2-1)))
print()
print("f2 stats:", f2.stats())

finish([f1, f2])
