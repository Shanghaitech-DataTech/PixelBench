from pixelbench_api import *

base = input_canvas
W, H = base.stats()['size']

# ---- Frame 1: original picture content ----
f1 = base.copy(name='f1')

# ---- Frame 2: completed drawn-sword slash ----
# The sword is held in the LEFT hand (the hand gripping the blade, upper area).
# The slash sweeps from the lower left up to the upper right, and a BLACK
# slash trail marks the completed motion, ending on the blade at upper right.
f2 = base.copy(name='f2')
black = f2.color((0, 0, 0))

# Quadratic Bezier from lower-left to upper-right, ending on the blade base.
p0 = (6, 56)
pc = (22, 45)
p2 = (41, 23)
steps = 70
pts = []
for i in range(steps + 1):
    t = i / steps
    x = (1 - t) * (1 - t) * p0[0] + 2 * (1 - t) * t * pc[0] + t * t * p2[0]
    y = (1 - t) * (1 - t) * p0[1] + 2 * (1 - t) * t * pc[1] + t * t * p2[1]
    pts.append((x, y))

# Thick tapered brush body (5px -> 1px), drawn in front of the figure.
for i, (x, y) in enumerate(pts):
    t = i / steps
    r = int(round(2.6 - 1.7 * t))
    if r >= 0:
        f2.circle(int(round(x)), int(round(y)), r, black)

# Crisp 1px core line along the sweep for a clean slash edge.
f2.path(f"M{p0[0]} {p0[1]} Q{pc[0]} {pc[1]} {p2[0]} {p2[1]}", black, fill=False)

# Small black flecks kicked up along the middle of the arc (action detail).
for fx, fy in [(30, 37), (35, 32), (38, 29)]:
    f2.set(fx, fy, black)

print("f1:", f1.stats())
print(f1.stats_text())
print("f2:")
print(f2.stats_text())

finish([f1, f2])
