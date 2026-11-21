try:
    from pixelbench_api import *
except Exception:
    pass

t = new_canvas(64, 64, background="#000000", name="probe2")

def spans(idx, x0=0, x1=63, y0=0, y1=63):
    res = []
    for y in range(y0, y1 + 1):
        xs = [x for x in range(x0, x1 + 1) if t.get(x, y) == idx]
        if xs:
            res.append((y, min(xs), max(xs), len(xs)))
    return res

t.ellipse(31, 31, 8, 5, "#ff0000")
i1 = t.color("#ff0000")
print("--- ellipse rx8 ry5 ---")
for y, a, b, n in spans(i1):
    print(f"  y={y} x={a}..{b} n={n}")

t.ellipse(31, 31, 7, 4, "#00ff00")
i2 = t.color("#00ff00")
print("--- ellipse rx7 ry4 ---")
for y, a, b, n in spans(i2):
    print(f"  y={y} x={a}..{b} n={n}")

t.ellipse(31, 31, 6, 3, "#0000ff")
i3 = t.color("#0000ff")
print("--- ellipse rx6 ry3 ---")
for y, a, b, n in spans(i3):
    print(f"  y={y} x={a}..{b} n={n}")

t.circle(18, 31, 3, "#ffff00")
i4 = t.color("#ffff00")
print("--- circle r3 @(18,31) ---")
for y, a, b, n in spans(i4, 0, 40, 20, 45):
    print(f"  y={y} x={a}..{b} n={n}")

t.path("M 25 31 A 6 3 0 0 0 37 31", "#00ffff", fill=False)
i5 = t.color("#00ffff")
print("--- arc M25,31 A6,3 -> 37,31 sweep0 ---")
for y, a, b, n in spans(i5, 0, 63, 20, 45):
    print(f"  y={y} x={a}..{b} n={n}")
