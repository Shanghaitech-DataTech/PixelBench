from pixelbench_api import *

output = input_canvas.copy(name="output")

# Look up the colours we need (all already in the shared palette).
bg = output.color("#ffffff")       # background white
dark = output.color("#2e1f12")     # dark outline
wood_L = output.color("#93785a")   # light wood (c25)
wood_R = output.color("#73492a")   # darker wood (c22)

# --- Remove the old sword ------------------------------------------------
# Blade: columns x42..44, rows y41..55.
for y in range(41, 56):
    for x in range(42, 45):
        output.set(x, y, bg)

# Gold crossguard: x41..45 at y39..40, plus its right outline at x46.
for y in range(39, 41):
    for x in range(41, 46):
        output.set(x, y, bg)
    output.set(46, y, bg)

# Pommel / lower hand area at y38; x40 remains as the hand outline.
for x in range(41, 45):
    output.set(x, 38, bg)

# --- Draw a wooden staff in the same hand --------------------------------
# 2 px vertical pole at x41..42.  Rows 12..13 are left untouched so the
# staff passes behind the adventurer's head rather than through it.
for y in range(1, 56):
    if y in (12, 13):
        continue
    output.set(41, y, wood_L)
    output.set(42, y, wood_R)

# Rounded cap at the top of the staff.
output.set(40, 0, dark)
output.set(41, 0, wood_L)
output.set(42, 0, wood_R)
output.set(43, 0, dark)

# Lower edge of the gripping hand at y38 beside the staff.
output.set(40, 38, dark)
output.set(43, 38, dark)
output.set(44, 38, dark)

finish(output)
