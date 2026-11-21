from pixelbench_api import *

W, H = 68, 63
f1 = new_canvas(W, H, name='frame1')
f1.blit(input_canvas, 0, 0)

f2 = f1.copy(name='frame2')

# --- remove the held flame: clear flame colours by palette index ---
flame_idx = {f2.color('#f27219'), f2.color('#f4a30c'), f2.color('#fed32c')}
for y in range(H):
    for x in range(W):
        if f2.get(x, y) in flame_idx:
            f2.set(x, y, None)

# --- lean the body forward (shear in bands) ---
sA = f2.select(0, 0, 47, 14);  sA.move_to(3, 0, f2)   # head
sB = f2.select(0, 14, 47, 11); sB.move_to(2, 14, f2)  # upper torso + arm
sC = f2.select(0, 25, 47, 8);  sC.move_to(1, 25, f2)  # lower torso / hem

# --- clear old legs, redraw in a stride ---
f2.clear(0, 33, 37, 30)

OUT = '#010202'; HP = '#455363'; G = '#211d2c'; I = '#0b0b13'
J = '#4a222d'; C = '#0b0102'

def shape(cv, pts, fill, out=OUT):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
        cv.poly([(x + dx, y + dy) for x, y in pts], out, fill=True)
    cv.poly(pts, fill, fill=True)

back_leg  = [(11, 32), (18, 32), (12, 46), (9, 55), (4, 55), (7, 44)]
front_leg = [(18, 32), (26, 32), (30, 45), (30, 55), (24, 55), (22, 45)]
back_boot  = [(1, 58), (6, 54), (10, 54), (10, 62), (1, 62)]
front_boot = [(24, 54), (28, 54), (34, 58), (34, 62), (24, 62)]

shape(f2, back_leg, HP)
shape(f2, front_leg, HP)
shape(f2, back_boot, J)
shape(f2, front_boot, J)
f2.line(23, 35, 27, 45, G)   # front-leg inner shade
f2.line(28, 46, 29, 54, I)   # front-leg shin shade
f2.line(8, 40, 6, 52, I)     # back-leg shade
f2.line(1, 62, 10, 62, C)
f2.line(24, 62, 34, 62, C)

# --- fireball flying forward with fiery trail ---
M = '#f27219'; N = '#f4a30c'; O = '#fed32c'
f2.circle(56, 20, 6, M)
f2.circle(56, 20, 4, N)
f2.circle(57, 20, 2, O)
f2.poly([(50, 15), (44, 17), (50, 19)], M)   # trail flames into the ball
f2.poly([(50, 21), (44, 23), (50, 25)], M)
f2.poly([(51, 18), (47, 20), (51, 22)], N)
for x in [41, 43, 45, 47, 49]:
    f2.set(x, 20, M)
for x in [42, 44, 46, 48]:
    f2.set(x, 22, N)
for x in [45, 47]:
    f2.set(x, 24, M)
f2.set(43, 18, N); f2.set(49, 26, M); f2.set(46, 26, N); f2.set(51, 28, M)

view(f1)
view(f2)
finish([f1, f2])
