import numpy as np

output = input_canvas.copy(name='output')

# --- palette lookup (robust: read the indices the drawing actually uses) ---
pal = {tuple(e['rgba']): e['index'] for e in output.palette()}
WHITE = pal[(255, 255, 255, 255)]
BLACK = pal[(0, 0, 0, 255)]
F = pal[(251, 244, 201, 255)]   # cream flesh
H = pal[(255, 218, 69, 255)]    # light yellow flesh
G = pal[(255, 200, 48, 255)]    # golden flesh
I = pal[(239, 157, 14, 255)]    # dark orange flesh edge
E = pal[(190, 111, 72, 255)]    # rind brown (matches the rind patches already visible)
FLESH = {F, H, G, I}

# --- Remove the BOTTOM flesh segment ---
# The three wedges are separated by two brown crevice streaks whose centre
# lines are  8x - 9y = 31    (upper crevice, streak (32,25)-(41,33))
#        and 15x - 13y = -129 (lower crevice, streak (20,33)-(33,48))
# The bottom wedge is the flesh strictly below/left of the lower crevice line.
# Only flesh pixels are replaced; the crevice streak, the existing rind
# patches and the black silhouette outline are all left untouched, so the
# other two wedges stay pixel-identical.
new_rind = []
n_top = n_mid = 0
for y in range(64):
    for x in range(64):
        if output.get(x, y) in FLESH:
            if 15 * x - 13 * y < -129:
                output.set(x, y, E)
                new_rind.append((x, y))
            elif 8 * x - 9 * y > 31:
                n_top += 1
            else:
                n_mid += 1

print("bottom-segment flesh pixels replaced:", len(new_rind),
      "| top kept:", n_top, "middle kept:", n_mid)

# --- safety: any newly exposed rind pixel touching the background becomes
#     silhouette outline, matching the fruit's existing black edge ---
for (x, y) in new_rind:
    touch = False
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 64 and 0 <= ny < 64 and output.get(nx, ny) == WHITE:
                touch = True
    if touch:
        output.set(x, y, BLACK)

print(output.stats_text())
print(output.matrix_text())
finish(output)
