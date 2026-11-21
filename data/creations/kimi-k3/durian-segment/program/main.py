import numpy as np

OUT = input_canvas.copy(name="output")
BG = 1; BLACK = 2; R3 = 3; R4 = 4; R5 = 5; PITH = 6
F = (7, 8, 9)
def px(x, y): return OUT.get(x, y)

# 1) remove dangling seed-bit blob
for (x, y) in [(31,56),(32,56),(33,56),(32,57),(33,57)]:
    if px(x,y) != BG: OUT.set(x, y, BG)
# 2) bottom flesh -> rind
for y in range(51, 58):
    for x in range(8, 32):
        if px(x, y) in F: OUT.set(x, y, R5)
# 3) bottom cluster black outline -> rind
for y in range(51, 58):
    for x in range(8, 32):
        if px(x, y) == BLACK: OUT.set(x, y, R4)
# 4) fill small bg notch in rind bottom
for (x, y) in [(29,56),(30,56)]:
    OUT.set(x, y, R4)

# verify
P = np.array([[OUT.get(x,y) for x in range(64)] for y in range(64)])
for y in range(50,58):
    print(f"{y:2d} " + "".join((str(P[y,x]) if P[y,x]>1 else '.') for x in range(8,42)))
cnt = sum(1 for y in range(51,58) for x in range(64) if P[y,x] in F)
print("remaining flesh px rows51-57:", cnt)
view(OUT)
finish(OUT)
