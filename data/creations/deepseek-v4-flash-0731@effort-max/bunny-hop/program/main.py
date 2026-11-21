from pixelbench_api import *

src = input_canvas
W, H = 34, 44

# ---------------- Frame 1: original picture content ----------------
f1 = new_canvas(W, H, name="f1")
f1.blit(src, 4, 9)

# ---------------- Frame 2: mid-leap hop forward (rabbit faces left) ----------------
f2 = new_canvas(W, H, name="f2")

# output row -> source row: head area kept, torso/legs stretched ~1.3x
map_rows = [0,1,2,3,4,5,6,7,8,
            9,10,10,11,12,12,13,14,14,15,16,16,17,18,18,19,20,20,
            21,22,22,23,24,24,25,26,26,27]
N = len(map_rows)

def off_of(oy):
    # forward lean: head moves left more than the feet (top -> 4, bottom -> 1)
    return round(4 - 3 * oy / (N - 1))

for oy, sy in enumerate(map_rows):
    off = off_of(oy)
    for x in range(26):
        cidx = src.get(x, sy)
        if not cidx:
            continue
        dx = x + off
        if sy >= 23 and 1 <= x <= 8:   # front feet lunge forward-left
            dx -= 1
        f2.set(dx, oy, src.color_name(cidx))

# soft ground shadow under the airborne rabbit
f2.ellipse(12, 39, 11, 1, (95, 95, 100, 60))
f2.ellipse(12, 39, 8, 1, (78, 78, 88, 100))

# motion dashes trailing behind (right), only where empty
dash = [(26, 3), (27, 6), (27, 9), (28, 12), (27, 15), (28, 18)]
for (x0, y0) in dash:
    for i in range(2):
        if y0 + i < H and not f2.get(x0, y0 + i):
            f2.set(x0, y0 + i, (150, 148, 160, 90))

print("f1:", f1.stats_text())
print("f2:", f2.stats_text())

finish([f1, f2])
