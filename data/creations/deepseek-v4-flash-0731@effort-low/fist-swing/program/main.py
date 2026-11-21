from pixelbench_api import *

orig = input_canvas

# Frame 1: keep original content, on a slightly larger shared canvas.
f1 = new_canvas(42, 44, name='f1')
f1.blit(orig, 0, 0)

# Frame 2: extended left punch (arm extends horizontally to the right).
f2 = new_canvas(42, 44, name='f2')
f2.blit(orig, 0, 0)

A = '#222034'   # outline / dark
C = '#eec39a'   # skin
E = '#df7126'   # orange shade

# Extended arm: connect from old arm tip (near col 20, rows 10-14) rightward.
f2.rect(21, 10, 9, 1, A)          # top outline rows
f2.rect(20, 11, 10, 1, C)
f2.rect(20, 12, 10, 1, C)
f2.rect(20, 13, 10, 1, C)
f2.rect(20, 14, 9, 1, A)          # bottom outline

# Fist (closed hand) at the end, with finger creases.
for (xx, row) in [(30,9),(31,9),(32,9),(33,9),(34,9),(35,9),(36,9),(37,9),
                  (30,14),(31,14),(32,14),(33,14),(34,14),(35,14),(36,14),(37,14),
                  (30,10),(37,10),(30,11),(37,11),(30,13),(37,13)]:
    f2.set(xx, row, A)
for xx in range(31, 37):
    f2.set(xx, 10, C)
    f2.set(xx, 11, C)
    f2.set(xx, 13, C)
f2.set(31,12,C); f2.set(33,12,C); f2.set(34,12,C); f2.set(36,12,C)
f2.set(32,12,E); f2.set(35,12,E)

print("f1", f1.stats_text())
print("f2", f2.stats_text())
print(f2.matrix_text(region=(16,6,42,20)))

finish([f1, f2])
