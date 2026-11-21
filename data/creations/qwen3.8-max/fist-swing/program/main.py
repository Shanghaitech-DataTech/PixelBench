from pixelbench_api import *

W, H = 32, 44
OUT, SKIN, ORANGE, SHADOW = 1, 3, 5, 6  # palette indices of the input

# ---- Frame 1: original picture content ----
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 0, 0)

# ---- Frame 2: light punch with the left fist (arm on image-right) ----
f2 = new_canvas(W, H, name="frame2")
f2.blit(input_canvas, 0, 0)

# erase the bent guard arm (raised fist + forearm), keep shoulder/torso (x<=16)
f2.clear(17, 7, 12, 8)  # x17..28, y7..14

def run(y, x0, x1, i):
    for x in range(x0, x1 + 1):
        f2.set(x, y, i)

# extended punching arm, joined to the shoulder
run(9, 16, 23, OUT)          # top outline (starts at shoulder cap)
run(10, 14, 23, ORANGE)      # arm body
run(11, 14, 23, ORANGE)
run(12, 13, 23, SHADOW)      # under-arm shade
run(13, 17, 23, OUT)         # bottom outline (armpit line continues left)
# fist at the end of the extended arm
run(8, 24, 28, OUT)
run(9, 24, 27, SKIN); f2.set(28, 9, OUT)
f2.set(24, 10, SKIN); f2.set(25, 10, SKIN); f2.set(26, 10, SHADOW); f2.set(27, 10, SKIN); f2.set(28, 10, OUT)
f2.set(24, 11, SHADOW); f2.set(25, 11, SKIN); f2.set(26, 11, SKIN); f2.set(27, 11, SHADOW); f2.set(28, 11, OUT)
f2.set(24, 12, SKIN); f2.set(25, 12, SHADOW); f2.set(26, 12, SKIN); f2.set(27, 12, SHADOW); f2.set(28, 12, OUT)
run(13, 24, 27, SHADOW); f2.set(28, 13, OUT)
run(14, 24, 28, OUT)

view(f1)
view(f2)
finish([f1, f2])
