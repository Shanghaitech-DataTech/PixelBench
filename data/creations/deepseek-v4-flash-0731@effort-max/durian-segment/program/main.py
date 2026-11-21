from pixelbench_api import *

src = canvas("input")
out = src.copy(name="output")
w, h = out.stats()["size"]

FLESH = {6, 7, 8, 9}
RIND = 5  # be6f48 shell rind brown

# verify: all pixels above row 42 identical to input
diff = 0
for y in range(42):
    for x in range(w):
        if out.get(x, y) != src.get(x, y):
            diff += 1
print("diffs above row 42:", diff)

# remove bottom-segment flesh (rows 42-53) -> expose rind underneath
for y in range(42, h):
    for x in range(w):
        if out.get(x, y) in FLESH:
            out.set(x, y, RIND)

print(out.stats_text())
finish(out)
