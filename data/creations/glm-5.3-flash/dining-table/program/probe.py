try:
    from pixelbench_api import *
except Exception:
    pass

t = new_canvas(40, 40, background="#ffffff", name="probe")

def spans(y, x0=0, x1=39):
    out = []
    run = None
    for x in range(x0, x1 + 1):
        idx = t.get(x, y)
        if idx != 0:  # 0 = white background? check palette
            pass
    return out

# Draw each test shape in its own colour on white, then report bounding rows.
t.circle(10, 10, 4, "#ff0000")
t.circle(25, 10, 3, "#00ff00")
t.circle(10, 25, 2, "#0000ff")
t.ellipse(30, 30, 6, 4, "#ff00ff")

pal = t.palette()
print("PALETTE:", [(e["index"], e["rgba"]) for e in pal])

def row_spans(cy, colour_idx, x0=0, x1=39):
    res = []
    for y in range(0, 40):
        xs = [x for x in range(x0, x1 + 1) if t.get(x, y) == colour_idx]
        if xs:
            res.append((y, min(xs), max(xs), len(xs)))
    return res

for name, col in [("circle r4 @(10,10)", "#ff0000"), ("circle r3 @(25,10)", "#00ff00"),
                  ("circle r2 @(10,25)", "#0000ff"), ("ellipse 6x4 @(30,30)", "#ff00ff")]:
    idx = t.color(col)
    print(f"--- {name} (idx {idx}) ---")
    for y, xa, xb, n in row_spans(0, idx):
        print(f"  y={y:2d} x={xa}..{xb} n={n}")
