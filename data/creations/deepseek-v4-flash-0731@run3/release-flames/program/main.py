from pixelbench_api import *

m = '#f27219'  # orange
n = '#f4a30c'  # yellow
o = '#fed32c'  # bright yellow
robe = '#7d423a'

W, H = 110, 63

# ---- Frame 1: original picture content, kept on a wider canvas ----
f1 = new_canvas(W, H)
f1.blit(input_canvas, 2, 0)

# ---- Frame 2: thrust pose + flying flame ----
f2 = new_canvas(W, H)
f2.blit(input_canvas, 2, 0)

# body leans in: head/shoulders pushed forward
f2.select(11, 0, 25, 9).move_to(13, 1, f2)

# left arm raised forward toward the thrust
f2.select(10, 26, 15, 8).move_to(12, 20, f2)
f2.rect(10, 26, 15, 8, robe)   # keep the robe fabric where the arm was

# left foot steps forward (toward the flame)
f2.select(2, 54, 13, 9).move_to(6, 54, f2)

# clear the old stationary flame and its sparks
f2.clear(34, 10, 32, 19)

# fiery burst just leaving the hand
f2.circle(45, 19, 5, m)
f2.circle(47, 20, 3, n)
f2.circle(48, 20, 2, o)
f2.circle(39, 19, 3, m)
f2.circle(40, 20, 2, n)

# flaming trail streaming forward
f2.circle(52, 17, 3, m)
f2.circle(50, 14, 2, m)
f2.circle(53, 23, 3, m)
f2.circle(50, 21, 2, n)
f2.circle(58, 14, 3, m)
f2.circle(56, 22, 3, m)
f2.circle(60, 11, 2, m)
f2.circle(60, 25, 2, m)
f2.circle(62, 16, 2, n)
f2.circle(61, 21, 2, n)

# the flying fireball thrown forward
f2.circle(72, 19, 11, m)
f2.circle(70, 18, 8, n)
f2.circle(68, 19, 5, o)
f2.circle(66, 17, 3, o)
# flicking flames around the fireball
f2.circle(80, 24, 3, m)
f2.circle(78, 11, 3, m)
f2.circle(82, 18, 2, n)

# sparks flying ahead
for (x, y) in [(82, 14), (86, 18), (84, 22), (88, 12), (82, 26), (86, 24), (90, 16), (84, 18), (80, 10), (88, 26), (92, 13), (86, 28), (84, 12)]:
    f2.set(x, y, m)
for (x, y) in [(84, 16), (86, 20), (82, 20), (88, 14), (90, 18)]:
    f2.set(x, y, o)

print("f1", f1.stats_text())
print("f2", f2.stats_text())

finish([f1, f2])
