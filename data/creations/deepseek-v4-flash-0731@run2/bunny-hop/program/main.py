from pixelbench_api import *

src = input_canvas
W, H = 36, 36
A = 1   # dark outline  #3A3737
D = 4   # white fur    #EFE9E7

# ---- Frame 1: original picture content, on the shared 36x36 canvas ----
f1 = new_canvas(W, H, name='frame1')
f1.blit(src, 0, 0)

# ---- Frame 2: rabbit caught in a mid-leap, hopping forward (right) ----
f2 = new_canvas(W, H, name='frame2')
f2.blit(src, 8, 1)

# remove the old standing feet rows so we can redraw the leap stride
f2.clear(3, 26, 30, 6)

# hind leg: stretches back (left) and down
f2.set(6, 26, A); f2.set(7, 26, D); f2.set(8, 26, A)
f2.set(6, 27, A); f2.set(7, 27, D); f2.set(8, 27, A)
f2.set(5, 28, A); f2.set(6, 28, D); f2.set(7, 28, A)
f2.set(4, 29, A); f2.set(5, 29, D); f2.set(6, 29, A)
f2.rect(4, 30, 3, 1, A)
f2.rect(5, 31, 2, 1, A)
f2.set(6, 32, A)

# front legs: reaching forward (right) and down
f2.set(24, 26, A); f2.rect(25, 26, 3, 1, D); f2.set(28, 26, A)
f2.set(25, 27, A); f2.rect(26, 27, 3, 1, D); f2.set(29, 27, A)
f2.set(26, 28, A); f2.set(30, 28, A); f2.set(31, 28, A)
f2.set(29, 29, A); f2.set(30, 29, A); f2.set(31, 29, A)
f2.set(30, 30, A); f2.set(31, 30, A)

# soft shadow on the ground below the airborne bunny
f2.ellipse(15, 33, 7, 1, (40, 38, 38, 110))
f2.ellipse(14, 34, 6, 1, (58, 55, 55, 60))
f2.set(2, 33, (90, 90, 90, 50))
f2.set(1, 34, (90, 90, 90, 42))
f2.set(4, 32, (90, 90, 90, 36))
f2.set(3, 35, (80, 80, 80, 30))

print(f1.stats_text())
print(f2.stats_text())
print("--- frame2 lower body ---")
print(f2.matrix_text(region=(0, 18, 35, 35)))
print("--- frame2 full ---")
print(f2.matrix_text())
print("--- frame2 top half ---")
print(f2.matrix_text(region=(0, 0, 35, 17)))
finish([f1, f2])
