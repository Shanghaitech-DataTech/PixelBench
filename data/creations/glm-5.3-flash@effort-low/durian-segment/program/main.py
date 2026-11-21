c = input_canvas.copy(name="output")

FLESH = {c.color("#fbf4c9"), c.color("#ffc830"), c.color("#ffda45"),
         c.color("#ef9d0e"), c.color("#e08c37")}
RIND = c.color("#be6f48")
RIND_DARK = c.color("#a65537")

# Remove the bottom flesh segment (rows 49-57): replace flesh with rind,
# keep the black outline of the cavity.
for y in range(49, 58):
    for x in range(64):
        i = c.get(x, y)
        if i in FLESH:
            c.set(x, y, RIND)

# depth shading just under the top edge of the cavity
for y in (49, 50):
    for x in range(64):
        if c.get(x, y) == RIND:
            c.set(x, y, RIND_DARK)
# a few darker speckles for rind texture
for (x, y) in [(14, 52), (22, 53), (30, 52), (38, 53), (44, 52), (18, 55), (33, 55)]:
    if c.get(x, y) == RIND:
        c.set(x, y, RIND_DARK)

print(c.stats_text())
print(c.matrix_text(region=(4, 44, 54, 58)))
save("durian_segment_output", c)
finish(c)
