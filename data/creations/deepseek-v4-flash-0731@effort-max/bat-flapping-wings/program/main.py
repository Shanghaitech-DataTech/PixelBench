from pixelbench_api import *

W, H = 41, 24
DX, DY = 7, 1  # offset of the original 27x22 picture on the frame canvas

# Frame 1: original picture content, on the shared canvas.
f1 = new_canvas(W, H)
f1.blit(input_canvas, DX, DY)

# Frame 2: wings opened up into a raised, spread position.
f2 = new_canvas(W, H)
f2.blit(input_canvas, DX, DY)

# Remove the drooping wings (original columns 0-6 and 20-26, rows 6-20).
f2.clear(DX + 0, DY + 6, 7, 15)     # original x0-6, y6-20
f2.clear(DX + 20, DY + 6, 7, 15)    # original x20-26, y6-20

# Raised right wing: leading edge sweeps up from the shoulder to a high tip,
# trailing edge comes back down with scallops.  Colors: c3=4 fill, c0=1 outline,
# c7=8 web highlight.
right = [(25, 10), (28, 7), (31, 4), (34, 2), (37, 1), (38, 2), (37, 3),
        (35, 4), (34, 6), (35, 8), (32, 9), (33, 11), (30, 12), (31, 14),
        (28, 14), (29, 16), (26, 16), (27, 18), (24, 15), (24, 11)]
left = [(40 - x, y) for (x, y) in right]

for pts in (left, right):
    f2.poly(pts, 4).poly(pts, 1, fill=False)
    # small inner web highlight along the wing
    inner = pts[2:16]
    f2.poly(inner, 8, fill=False)

print("f1:", f1.stats())
print("f2:", f2.stats())
print(f2.matrix_text(region=(0, 0, 40, 15)))
print(f2.matrix_text(region=(0, 15, 40, 23)))

finish([f1, f2])
