from pixelbench_api import *

W, H = 64, 63

K     = '#010202ff'  # near-black outline
KK    = '#0b0102ff'
PANT  = '#455363ff'  # pants / sleeve grey-blue
PANTD = '#211d2cff'  # pants shadow
BOOT  = '#4a222dff'  # dark red-brown (boots, forearm)
BOOTD = '#240b0cff'
BOOTH = '#443d45ff'
SKIN  = '#7d423aff'
M = '#f27219ff'      # flame orange
N = '#f4a30cff'      # flame mid
O = '#fed32cff'      # flame yellow
WH = '#fff6c2ff'     # hot core

# ---------------- frame 1: original content ----------------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 0, 0)

# ---------------- frame 2: fire thrust ----------------
f2 = new_canvas(W, H, name="frame2")
f2.blit(input_canvas, 0, 0)
f2.color(WH)

# 1) erase every flame-coloured pixel (sparks + old fireball)
flame = {f2.color(M), f2.color(N), f2.color(O)}
for y in range(H):
    for x in range(47):
        if f2.get(x, y) in flame:
            f2.set(x, y, None)

# 2) lean the body forward: head leads, torso less, hips least
sA = f2.select(0, 0, 47, 14)   # head band
sB = f2.select(0, 14, 47, 17)  # torso + arm band
sC = f2.select(0, 31, 47, 15)  # hips band
sA.move_to(3, 0, f2)
sB.move_to(2, 14, f2)
sC.move_to(1, 31, f2)

# 3) clear old bent forearm / hand remains, draw straight thrusting arm
f2.clear(33, 17, 17, 9)        # x33-49, rows 17-25
f2.clear(30, 22, 3, 3)         # old lower-arm stub
f2.line(33, 18, 47, 18, K)            # top outline
f2.rect(33, 19, 7, 2, PANT)           # sleeve x33-39 rows 19-20
f2.rect(40, 19, 8, 2, BOOT)           # forearm x40-47
f2.line(33, 21, 47, 21, K)            # bottom outline
# fist
f2.rect(48, 18, 3, 4, BOOT)
f2.line(48, 18, 50, 18, BOOTD)
f2.set(50, 19, BOOTD); f2.set(50, 20, BOOTD)
f2.line(48, 21, 50, 21, BOOTD)

# 4) left foot steps forward: erase old front leg+boot, redraw ahead
f2.clear(14, 43, 19, 20)       # x14-32, rows 43-62
f2.poly([(13, 42), (22, 42), (31, 48), (28, 56), (22, 56)], PANT, fill=True)
f2.line(13, 42, 22, 56, K)                # left edge of the leg
f2.line(28, 55, 27, 52, K)                # right edge hint near boot
f2.line(18, 45, 25, 54, PANTD)            # shading
f2.poly([(22, 55), (28, 55), (31, 58), (31, 60), (30, 62), (21, 62), (21, 57)],
        BOOT, fill=True)
f2.poly([(22, 55), (28, 55), (31, 58), (31, 60), (30, 62), (21, 62), (21, 57)],
        KK, fill=False)
f2.set(24, 57, BOOTH); f2.set(25, 57, BOOTH)

# 5) fireball with fiery trail
f2.rect(51, 19, 4, 2, O)                       # bright trail core
f2.set(51, 18, N); f2.set(52, 18, N); f2.set(53, 18, N)
f2.set(51, 21, N); f2.set(52, 21, N)
f2.line(47, 16, 50, 16, M)                     # motion streaks
f2.line(46, 23, 50, 23, M)
f2.circle(59, 20, 5, M, fill=True)             # flame head
f2.circle(59, 20, 4, N, fill=True)
f2.circle(59, 20, 2, O, fill=True)
f2.rect(58, 19, 2, 2, WH)                      # white-hot core
f2.set(58, 14, M); f2.set(61, 14, M)           # flame licks
# stray embers
f2.set(48, 13, M); f2.set(52, 14, N); f2.set(44, 19, M); f2.set(46, 26, N)

view(f1)
view(f2)
finish([f1, f2])
