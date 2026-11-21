from pixelbench_api import *

print(input_canvas.stats_text())
print(input_canvas.matrix_text())

f1 = input_canvas.copy(name="frame1")
f2 = input_canvas.copy(name="frame2")

# Remove the original drooping membranes while preserving the central bat.
f2.rect(0, 6, 9, 16, None)
f2.rect(18, 6, 9, 16, None)

# Raised wings: dark scalloped silhouette, muted membrane, and a few ribs.
left_outer = [(8, 8), (6, 7), (4, 5), (2, 3), (0, 1), (1, 1), (3, 2),
              (5, 3), (7, 4), (8, 6), (8, 7), (7, 8), (6, 7), (5, 8),
              (4, 7), (3, 6), (2, 5), (1, 4), (0, 3), (1, 6), (3, 8),
              (5, 10), (7, 11), (8, 10)]
left_inner = [(7, 8), (5, 6), (3, 4), (1, 2), (3, 3), (5, 4), (7, 5),
              (8, 7), (7, 7), (6, 6), (5, 7), (4, 6), (3, 5), (2, 4),
              (2, 6), (4, 8), (6, 10), (7, 10)]
right_outer = [(26-x, y) for x, y in left_outer]
right_inner = [(26-x, y) for x, y in left_inner]

f2.poly(left_outer, "#432f53")
f2.poly(right_outer, "#432f53")
f2.poly(left_inner, "#5c436f")
f2.poly(right_inner, "#5c436f")

for a, b in [((7, 8), (1, 2)), ((6, 9), (2, 5)), ((7, 10), (4, 7))]:
    f2.line(a[0], a[1], b[0], b[1], "#5f5f7b")
    f2.line(26-a[0], a[1], 26-b[0], b[1], "#5f5f7b")

print(f2.stats_text())
print(f2.matrix_text())
finish([f1, f2])
