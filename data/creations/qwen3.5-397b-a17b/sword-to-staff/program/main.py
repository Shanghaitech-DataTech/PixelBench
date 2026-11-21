from pixelbench_api import *

# Start fresh with a copy of the input
output = input_canvas.copy(name='output')

# Based on analysis, the sword consists of:
# - Blade tip: index 17 at (43, 38)
# - Blade: index 18 at cols 41-45, rows 39-40
# - Handle: index 19 at col 42, rows 41-53 and index 20 at col 43, rows 41-55
# Note: There's also index 18 at (30-32, 43) which is clothing decoration, NOT sword

# Clear the sword blade (index 17 and 18 in the sword area)
for y in range(38, 41):
    for x in range(41, 46):
        c = output.get(x, y)
        if c in [17, 18]:
            output.set(x, y, None)

# Clear the sword handle (indices 19 and 20 at cols 42-43)
for y in range(41, 56):
    for x in range(42, 44):
        c = output.get(x, y)
        if c in [19, 20]:
            output.set(x, y, None)

# Fill gaps by extending from adjacent pixels
for y in range(64):
    for x in range(64):
        if output.get(x, y) is None:
            # Try filling from left first (body side)
            for lx in range(x-1, max(0, x-20), -1):
                lc = output.get(lx, y)
                if lc is not None:
                    output.set(x, y, lc)
                    break
            else:
                # Try right (background)
                for rx in range(x+1, min(64, x+20)):
                    rc = output.get(rx, y)
                    if rc is not None:
                        output.set(x, y, rc)
                        break

# Draw the staff - a vertical wooden pole
# Position: cols 41-43 (where the sword handle was)
# A staff extends both above and below where a sword would be held

staff_dark = output.color('#4a3120')   # dark brown edge
staff_mid = output.color('#6b4423')    # medium brown shaft
staff_light = output.color('#93785a')  # light brown highlight

# Main staff shaft - 3 pixels wide, from near top to bottom
for y in range(6, 58):
    output.set(41, y, staff_dark)   # left edge
    output.set(42, y, staff_mid)    # center
    output.set(43, y, staff_light)  # right highlight

# Top of staff - decorative rounded top
output.set(42, 5, staff_mid)
output.set(43, 5, staff_light)
output.set(42, 4, staff_light)

# Bottom of staff
output.set(41, 58, staff_dark)
output.set(42, 58, staff_mid)
output.set(43, 58, staff_light)
output.set(42, 59, staff_mid)

# Verify no transparent pixels remain
print("Final stats:")
print(output.stats_text())

# Submit the result
finish(output)
