from pixelbench_api import *

f1 = new_canvas(34, 34)
f1.blit(input_canvas, 4, 3)

W, H = 34, 34
f2 = new_canvas(W, H)

d = f2.color('#efe9e7')    # body white
a = f2.color('#3a3737')    # outline dark
b = f2.color('#b7b3b2')    # light gray (feet/cheek)
cc = f2.color('#827c7c')   # shadow gray
e_ = f2.color('#d6b39d')   # inner ear

# ground shadow
f2.ellipse(17, 31, 9, 2, cc)

# --- leap bunny, facing left, airborne ---
f2.ellipse(19, 21, 8, 6, d)     # body
f2.ellipse(24, 26, 4.5, 4.5, d) # haunch
f2.circle(28, 17, 2.5, d)       # tail
f2.ellipse(10, 20, 5, 5, d)     # head
f2.ellipse(14, 9, 2.2, 6.5, d)  # ears
f2.ellipse(10, 10, 2.4, 6, d)
f2.ellipse(6, 24, 2.4, 5, d)    # front legs
f2.ellipse(9.5, 27, 2.2, 5, d)

f2.ellipse(14, 9, 1.1, 4.5, e_) # inner ears
f2.ellipse(10, 10, 1.1, 4, e_)
f2.ellipse(7, 19, 1.2, 1.2, a)  # eye
f2.ellipse(6, 21.5, 0.9, 0.9, a) # nose
f2.ellipse(24, 30, 3.5, 1.8, b) # hind foot
f2.ellipse(9, 23, 2, 1.2, b)    # cheek

f2.outline(a)

finish([f1, f2])
