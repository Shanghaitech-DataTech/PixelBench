from pixelbench_api import *

out = input_canvas.copy(name='output')

BG = 1  # white background

# --- clear old sword pixels ---
# gold crossguard (index 18) at x41-45 y39-40, stray outline at x46
for y in range(39, 41):
    for x in range(41, 47):
        out.set(x, y, BG)
# steel blade (indices 19,20,21) at x42-44 y41-55
for y in range(41, 56):
    for x in range(42, 45):
        out.set(x, y, BG)

# --- wooden staff (brown palette: 24 dark, 25 light, 23 mid) ---
# knob top
out.set(44, 15, 25)
out.set(43, 16, 24)
out.set(44, 16, 25)
out.set(45, 16, 23)
# shaft columns x43/44/45
for y in range(17, 58):
    out.set(43, y, 24)
    out.set(44, y, 25)
    out.set(45, y, 23)
# tapered foot
out.set(44, 58, 25)
out.set(45, 58, 23)
out.set(44, 59, 25)

# --- verify old sword colors are gone ---
leftover = []
for y in range(64):
    for x in range(64):
        if out.get(x, y) in (18, 19, 20, 21):
            leftover.append((x, y))
print("leftover sword pixels:", leftover)
print(out.stats_text())

def dump(x0, y0, x1, y1, label=""):
    print(f"--- {label} ({x0},{y0})-({x1},{y1}) ---")
    hdr = "    " + " ".join(f"{x%100:02d}" for x in range(x0, x1+1))
    print(hdr)
    for y in range(y0, y1+1):
        row = " ".join(f"{out.get(x,y):02d}" for x in range(x0, x1+1))
        print(f"y{y:02d} " + row)
    print()

dump(30, 0, 62, 63, "FULL RIGHT HALF")

finish(out)
