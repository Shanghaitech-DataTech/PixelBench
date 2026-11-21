try:
    from pixelbench_api import *
except Exception:
    pass

t = new_canvas(64, 64, background="#000000", name="probe3")

def fruit(cx, cy, r, base, hi, sh, dimple=None):
    t.circle(cx, cy, r + 1, "#888888")
    t.circle(cx, cy, r, base)
    t.set(cx - 1, cy - 1, hi)
    if r >= 3:
        t.set(cx - 2, cy, hi)
        t.set(cx + 1, cy + 2, sh)
        t.set(cx + 2, cy + 1, sh)
    else:
        t.set(cx + 1, cy + 1, sh)
    if dimple:
        t.set(cx, cy, dimple)

fruit(35, 31, 2, "#ff0000", "#ff8888", "#880000", "#880000")
fruit(27, 31, 2, "#00ff00", "#88ff88", "#008800")

i_out = t.color("#888888")
i_red = t.color("#ff0000")
i_green = t.color("#00ff00")

def grid(x0, x1, y0, y1, title):
    print(f"--- {title} ---")
    print("     " + "".join(str((x0 + i) % 10) for i in range(x1 - x0 + 1)))
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            v = t.get(x, y)
            row += "." if v == 0 else ("#" if v == i_out else ("R" if v == i_red else ("G" if v == i_green else "?")))
        print(f"{y:4d} {row}")

grid(20, 42, 25, 37, "FRUITS r2")

# ellipse spans
t.ellipse(5, 50, 8, 6, "#ffff00")
iy = t.color("#ffff00")
print("--- ellipse rx8 ry6 @(5,50) spans ---")
for y in range(40, 60):
    xs = [x for x in range(0, 64) if t.get(x, y) == iy]
    if xs:
        print(f"  y={y} x={min(xs)}..{max(xs)} n={len(xs)}")

t.ellipse(20, 50, 7, 5, "#00ffff")
ic = t.color("#00ffff")
print("--- ellipse rx7 ry5 @(20,50) spans ---")
for y in range(40, 60):
    xs = [x for x in range(0, 64) if t.get(x, y) == ic]
    if xs:
        print(f"  y={y} x={min(xs)}..{max(xs)} n={len(xs)}")

t.ellipse(40, 50, 6, 4, "#ff00ff")
im = t.color("#ff00ff")
print("--- ellipse rx6 ry4 @(40,50) spans ---")
for y in range(40, 60):
    xs = [x for x in range(0, 64) if t.get(x, y) == im]
    if xs:
        print(f"  y={y} x={min(xs)}..{max(xs)} n={len(xs)}")
