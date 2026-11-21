try:
    from pixelbench_api import *
except Exception:
    pass

t = new_canvas(64, 64, background="#000000", name="probe4")
t.ellipse(31, 31, 8, 6, "#ff0000")
i1 = t.color("#ff0000")
print("--- ellipse rx8 ry6 @(31,31) ---")
for y in range(20, 45):
    xs = [x for x in range(0, 64) if t.get(x, y) == i1]
    if xs:
        print(f"  y={y} x={min(xs)}..{max(xs)} n={len(xs)}")

t.path("M 25 31 A 6 4 0 0 0 37 31", "#00ff00", fill=False)
i2 = t.color("#00ff00")
print("--- arc M25,31 A6,4 -> 37,31 sweep0 ---")
for y in range(20, 45):
    xs = [x for x in range(0, 64) if t.get(x, y) == i2]
    if xs:
        print(f"  y={y} x={xs}")
