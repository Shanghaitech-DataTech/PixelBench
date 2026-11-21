from pixelbench_api import *

c = input_canvas
output = c.copy(name='output')

# =============== CLEAR THE SWORD ===============

# Clear the gold crossguard area (y=38-40)
for y in [38, 39, 40]:
    for x in range(40, 47):
        output.set(x, y, None)

# Clear the blade going downward
for y in range(41, 56):
    for x in range(42, 45):
        output.set(x, y, None)

# =============== DRAW THE STAFF ===============

# Register staff colors
wood_dark = output.color('#5A3A20')
wood_med  = output.color('#6B4423')
wood_light = output.color('#8B6B4A')
crystal_lt   = output.color('#66BBFF')
crystal_mid  = output.color('#4488CC')
crystal_dark = output.color('#3366AA')

# But keep the character's hand at y=34-37 showing skin
# The hand stays as skin (the original skin pixels remain)

# Staff pole going UP from the hand
# The staff at x=42 as the main staff
# Going from y=6 going downward through the hand area
for y in range(5, 45):
    output.set(41, y, wood_dark)
    output.set(42, y, wood_med)

# Light color on the right
for y in range(5, 45):
    output.set(43, y, wood_light)

# Staff top crystal
output.set(42, 3, crystal_lt)
output.set(41, 4, crystal_mid)
output.set(42, 4, crystal_mid)
output.set(43, 4, crystal_mid)
output.set(41, 5, crystal_mid)
output.set(43, 5, crystal_mid)
output.set(42, 6, crystal_mid)
output.set(41, 6, crystal_dark)
output.set(43, 6, crystal_dark)

# The hand at y=34 shows the hand gripping the staff
# The hand was at x=38-44, with skin at x=40-43

# At the hand (y=35-37), the staff continues through:
# Already covered by the staff loop

# =============== VERIFY ===============
print("=== Output region (30, 0, 55, 50) ===")
print(output.matrix_text(region=(30, 0, 55, 50)))

finish(output)
