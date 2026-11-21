import pixelbench_api as api

src = open("main.py").read().replace("finish(c)", "pass")
ns = {n: getattr(api, n) for n in ("new_canvas", "canvas", "canvases", "flatten",
      "load", "save", "view", "export", "finish", "redraw")}
ns["input_canvas"] = api.input_canvas
exec(compile(src, "main.py", "exec"), ns)
c = ns["c"]

w, h, rgba_bytes = c.to_rgba(1)
import numpy as np
arr = np.frombuffer(rgba_bytes, dtype=np.uint8).reshape(h, w, 4)

# 4x4 block dominant-colour overview -> 32x32 map
def lum(px):
    return 0.299*px[0] + 0.587*px[1] + 0.114*px[2]

def hue_class(px):
    r, g, b = int(px[0]), int(px[1]), int(px[2])
    L = lum(px)
    if L < 40:  return "#"   # very dark (rocks/foreground)
    if r > 200 and g > 150 and b < 120: return "O"  # bright sun/gold
    if r > 180 and g > 90 and b < 100:  return "o"  # orange
    if r > 120 and g < 90 and b < 110:  return "r"  # red / deep sunset
    if r > 80 and b > r:                return "p"  # purple/violet
    if b > 100 and b >= r:              return "b"  # blue-violet
    return "m"                               # mid tones

print("32x32 overview (each char = 4x4 px), rows y0-127:")
for by in range(0, 128, 4):
    cells = []
    for bx in range(0, 128, 4):
        block = arr[by:by+4, bx:bx+4].reshape(-1, 4)
        classes = [hue_class(p) for p in block]
        cells.append(max(set(classes), key=classes.count))
    print(f"{by:3d} {''.join(cells)}")

print()
print("stats:", c.stats_text())
