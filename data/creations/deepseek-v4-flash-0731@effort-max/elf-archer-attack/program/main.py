from pixelbench_api import *

SRC = input_canvas

# ---------- Frame 1: original picture content (placed on larger canvas) ----------
F1 = new_canvas(58, 50, name="f1")
SRC.select(0, 0, 35, 47).copy_to(8, 1, F1)

# ---------- Frame 2: bow drawn to its maximum (fully open bow, no arrow) ----------
F2 = new_canvas(58, 50, name="f2")
SRC.select(0, 0, 35, 47).copy_to(10, 1, F2)    # whole pose shifted right

# clear the old upright bow + string region; it is redrawn full-open
F2.clear(32, 2, 14, 35)                         # x32..45, y2..36

D = '#121311'   # dark outline
W = '#f3f4b6'  # bow belly (original pale bow colour)
G = '#fcc44c'  # gold parts
S = '#df9859'  # skin
V = '#55002a'  # violet glove
ST = '#e0c89e' # bowstring

# --- fully open recurve bow: limbs bend back, tips pulled toward the string ---
for y in range(9, 17):                       # upper limb (straight column near top)
    F2.set(40, y, D)
    F2.set(39, y, W)
F2.set(38, 8, W); F2.set(39, 8, D)
F2.set(37, 7, W); F2.set(38, 7, D)
F2.set(36, 6, D); F2.set(37, 6, W)
F2.set(35, 5, D); F2.set(36, 5, W)
# lower limb (mirrored)
for y in range(22, 31):
    F2.set(40, y, D)
    F2.set(39, y, W)
F2.set(39, 31, D); F2.set(38, 31, W)
F2.set(38, 32, D); F2.set(37, 32, W)
F2.set(36, 33, D); F2.set(37, 33, W)
F2.set(35, 34, D); F2.set(36, 34, W)
# grip
F2.rect(38, 16, 5, 6, D)
F2.rect(39, 17, 3, 3, G)
# bow arm (left arm extended, pushing the bow out)
F2.rect(30, 16, 7, 1, D)
F2.rect(30, 17, 6, 2, S)
F2.rect(30, 19, 6, 1, D)
# fist holding the grip
F2.rect(36, 15, 3, 4, D)
F2.rect(37, 16, 2, 2, V)
# drawing fist at the jaw (right hand, violet glove)
F2.rect(24, 11, 4, 4, D)
F2.rect(25, 12, 2, 2, V)
# string pulled to maximum anchor at the jaw -- NO arrow
F2.line(36, 6, 25, 13, ST)
F2.line(36, 33, 25, 13, ST)

print("f1:", F1.stats())
print("f2:", F2.stats())

finish([F1, F2])   # frame 1: original content; frame 2: full draw, bow fully open, no arrow
