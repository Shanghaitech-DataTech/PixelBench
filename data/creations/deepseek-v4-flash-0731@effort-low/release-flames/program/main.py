from pixelbench_api import *

src = input_canvas
newW, newH = 95, 63

# ---------- Frame 1: keep original picture content ----------
f1 = new_canvas(newW, newH)
f1.blit(src, 5, 0)

# ---------- Frame 2: thrust fire forward ----------
f2 = new_canvas(newW, newH)

# body: head+torso+arms, leaning forward (shifted right)
torso = src.select(0, 0, 47, 34).preview()
f2.blit(torso, 13, 0)
# remove the old flame held at the hand
f2.clear(56, 12, 26, 16)

# legs: back leg stays planted, front (left) foot steps forward into a lunge
back_leg  = src.select(0, 34, 16, 29).preview()
front_leg = src.select(16, 34, 31, 29).preview()
f2.blit(back_leg, 6, 34)
f2.blit(front_leg, 26, 34)

# flame colours
o = src.color('#f27219')
g = src.color('#f4a30c')
y = src.color('#fed32c')
base = src.color('#7d423a')

# flying flame pushed forward of the hand
f2.circle(72, 18, 7, o)
f2.circle(68, 20, 5, g)
f2.circle(64, 21, 3, y)
f2.circle(76, 14, 3, base)

# fiery trail from hand to flying flame
f2.poly([(48,24),(63,20),(66,24),(66,28),(60,27),(48,26),(48,24)], o)
f2.poly([(50,24),(60,21),(62,24),(62,27),(58,26),(50,25),(50,24)], g)
f2.poly([(52,22),(58,20),(60,22),(60,24),(57,23),(52,23),(52,22)], y)

finish([f1, f2])
