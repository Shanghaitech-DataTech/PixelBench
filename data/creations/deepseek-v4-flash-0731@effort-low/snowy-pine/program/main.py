from pixelbench_api import *

c = canvas("input")
out = c.copy(name="output")

snow = out.color((240, 246, 253), name="snow")

FOL = 118
def pix(x, y):
    if x < 0 or x >= 82 or y < 0 or y >= FOL:
        return 0
    return c.get(x, y)

# Snow along upper edges of foliage.
for y in range(FOL):
    for x in range(82):
        if pix(x, y) != 0 and pix(x, y-1) == 0:
            out.set(x, y, snow)

# Add thickness (second row of snow) under top edges that form wide/flat
# surfaces: a top-edge pixel whose left and right same-row neighbours are
# also foliage (i.e. it sits on a flat bench of a tier).
for y in range(FOL-1):
    for x in range(82):
        if out.get(x, y) == snow and pix(x, y+1) != 0:
            if pix(x-1, y) != 0 and pix(x+1, y) != 0:
                out.set(x, y+1, snow)

print(out.stats_text())
print(out.matrix_text(region=(0,90,81,117)))
finish(out)
