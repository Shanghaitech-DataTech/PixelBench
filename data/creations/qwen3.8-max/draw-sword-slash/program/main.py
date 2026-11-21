from pixelbench_api import *
import math

W, H = 104, 92
OX, OY = 20, 10

# ---- Frame 1: original picture content on the shared larger canvas ----
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, OX, OY)

# ---- Frame 2: completed draw-sword slash ----
f2 = f1.copy(name="frame2")

def erase(x, y, w, h):
    f2.clear(OX + x, OY + y, w, h)

# remove old gripping hand + tsuba/white patch + hilt bar (sword is drawn now)
erase(47, 36, 9, 1)    # y36 x47..55
erase(47, 37, 14, 1)   # y37 x47..60
erase(44, 38, 18, 1)   # y38 x44..61
erase(42, 39, 20, 1)   # y39 x42..61
erase(41, 40, 21, 1)   # y40 x41..61
erase(41, 41, 10, 1)   # y41 x41..50
erase(44, 42, 7, 1)    # y42 x44..50

# ---- black slash trail: sweeps lower-left -> upper-right ----
BLACK = '#020202'
P0 = (8.0, 84.0)
C = (46.0, 70.0)
P2 = (91.0, 37.0)
N = 200
for i in range(N + 1):
    t = i / N
    x = (1 - t) ** 2 * P0[0] + 2 * t * (1 - t) * C[0] + t * t * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * t * (1 - t) * C[1] + t * t * P2[1]
    r = 0.5 + 1.7 * (math.sin(math.pi * t) ** 1.6)
    f2.circle(int(round(x)), int(round(y)), int(round(r)), BLACK, fill=True)

# ---- left arm extended up-right, holding the drawn sword ----
D = '#454463'   # kimono
A = '#020202'   # outline black
K = '#f3a473'   # skin
J = '#1b0202'   # hilt wrap
NN = '#b2aeb1'  # guard / blade light
L = '#eedddd'   # blade highlight
M = '#9b938d'   # blade shade

sleeve = [(62, 48), (70, 40), (80, 33), (86, 37), (78, 44), (70, 52)]
f2.poly(sleeve, D, fill=True)
f2.poly(sleeve, A, fill=False)

# hand gripping hilt
f2.circle(86, 36, 2, K, fill=True)
# hilt (down-left of guard, through the fist)
f2.line(83, 39, 90, 32, J)
f2.line(84, 40, 91, 33, J)
f2.set(82, 40, J)
# guard
f2.rect(89, 30, 3, 3, NN)
# blade pointing up-right (end of the slash)
f2.line(91, 29, 101, 19, L)
f2.line(91, 30, 102, 20, NN)
f2.line(92, 31, 102, 21, M)
f2.set(103, 19, NN)

view(f1, margin=0)
view(f2, margin=0)
finish([f1, f2])
