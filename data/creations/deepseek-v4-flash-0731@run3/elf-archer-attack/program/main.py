from pixelbench_api import *

src = input_canvas

# ---- Frame 1: original picture content unchanged ----
f1 = src.copy(name="f1")

# ---- Frame 2: full-draw pose ----
# Start from the original, then clear the old bow/string region on the right
# and redraw a wide-open bow with the string pulled all the way back to the
# draw hand at the face.
f2 = src.copy(name="f2")
f2.clear(22, 0, 13, 47)          # wipe x22..34 (old narrow bow + old string)

G = 7    # yellow bow limbs
Q = 17   # brown grip
T = 20   # dark string
C = 3    # skin (draw hand)

# Bow limbs fully open: a wide V-shaped bow, grip at x22, tips at x31.
f2.line(31, 2, 22, 20, G)       # top limb
f2.line(22, 20, 31, 44, G)      # bottom limb
f2.line(32, 3, 23, 21, G)       # limb thickness
f2.line(23, 21, 32, 43, G)
for (x, y) in [(30, 1), (31, 2), (32, 2), (31, 43), (32, 43), (31, 44),
              (30, 3), (30, 42), (22, 20), (22, 21), (21, 20), (21, 21)]:
    f2.set(x, y, G)
for (x, y) in [(21, 19), (21, 20), (21, 21), (22, 20), (22, 21), (22, 22)]:
    f2.set(x, y, Q)
# bow hand gripping
for (x, y) in [(20, 19), (20, 20), (20, 21)]:
    f2.set(x, y, C)

# String pulled to the draw hand at the face (no arrow).
f2.line(31, 2, 14, 12, T)
f2.line(14, 12, 31, 44, T)
# Draw hand at the face + short draw arm hint
for (x, y) in [(14, 11), (14, 12), (15, 11), (15, 12), (15, 13), (13, 10), (12, 10)]:
    f2.set(x, y, C)

print(f1.stats()["size"], f2.stats()["size"])
print(f2.stats_text())

finish([f1, f2])
