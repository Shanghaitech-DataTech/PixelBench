from pixelbench_api import *

src = input_canvas
W, H = 30, 34

# ---- Frame 1: original picture content ----
f1 = new_canvas(W, H, name="f1")
f1.blit(src, 2, 2)

# ---- Frame 2: mid-leap ----
f2 = new_canvas(W, H, name="f2")

# body, head and legs: shear rear down / front up, whole rabbit lifted
for x in range(26):
    dy = round((13 - x) * 0.2) - 2
    for y in range(8, 28):
        col = src.get(x, y)
        if col is not None:
            f2.set(x + 2, y + dy, col)

# ears swept back: top rows shift left (tips), lower rows stay
for x in range(9, 23):
    dy = round((13 - x) * 0.2) - 2
    for y in range(0, 8):
        col = src.get(x, y)
        if col is not None:
            if y <= 3:
                dx = -2
            elif y <= 5:
                dx = -1
            else:
                dx = 0
            f2.set(x + 2 + dx, y + dy, col)

# ground shadow directly beneath the airborne rabbit
f2.ellipse(14, 32, 8, 1, (58, 55, 55, 110))

print("F1 stats:", f1.stats_text())
print("F2 stats:", f2.stats_text())

finish([f1, f2])
