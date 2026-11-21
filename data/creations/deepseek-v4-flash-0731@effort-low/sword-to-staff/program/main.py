from pixelbench_api import *
out = input_canvas.copy(name='output')

# --- Convert the adventurer's metal sword into a wooden staff ---
# The sword: silver (19 #eaedf3, 20 #c9ced8, 21 #8e96a5) and gold (18 #c9a227)
# metal pixels in the right-hand weapon column. Repaint them as a wooden pole.
WOOD  = out.color('#6b4423')   # staff wood (already palette id 16)
DARK  = out.color('#4a3120')   # dark grain (id 24)
LIGHT = out.color('#93785a')   # light grain (id 26)
HILT  = out.color('#5c3a21')   # guard ring (id 17)

metal = {'#c9a227', '#eaedf3', '#c9ced8', '#8e96a5'}
for y in range(32, 56):
    for x in range(37, 51):
        if out.color_name(out.get(x, y)) in metal:
            if x == 41:
                out.set(x, y, DARK)
            elif x == 42:
                out.set(x, y, WOOD)
            elif x == 43:
                out.set(x, y, LIGHT)
            else:
                out.set(x, y, WOOD)

# --- Staff top: wooden orb/knob above the gripping hand ---
out.set(42, 32, DARK)
out.set(41, 33, WOOD).set(43, 33, WOOD)
out.set(40, 34, DARK).set(42, 34, LIGHT).set(44, 34, DARK)
out.set(41, 35, WOOD).set(43, 35, WOOD)
out.set(42, 36, LIGHT)

# Print verification of the edited region
print(out.matrix_text(region=(36, 30, 52, 56), indices=True))

finish(out)
