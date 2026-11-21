from pixelbench_api import *

f1 = input_canvas.copy(name="frame1")
src = input_canvas
COLS, ROWS = 43, 61
f2 = new_canvas(COLS, ROWS, background=None, name="frame2")

def px(cv, x, y):
    i = cv.get(x, y)
    if i == 0:
        return None
    return tuple(cv.palette()[i]["rgba"])

def put(cv, x, y, col):
    if col is not None:
        cv.set(x, y, col)

# ---- colours ----
K  = (16, 16, 16)
y  = (255, 227, 140)
Y  = (198, 123, 2)
W  = (255, 204, 67)
G  = (192, 128, 8)
h  = (168, 160, 152)
H  = (255, 255, 213)
D  = (51, 45, 50)
B  = (128, 64, 24)
w  = (255, 255, 255)
c  = (220, 202, 202)
O  = (133, 128, 134)
o  = (90, 86, 90)
M  = (63, 0, 22)
v  = (44, 38, 35)
n  = (47, 16, 16)
s  = (218, 160, 136)
Tq = (120, 101, 90)
Z  = (23, 0, 53, 153)

# ---- 1) copy original ----
for yy in range(ROWS):
    for xx in range(COLS):
        p = px(src, xx, yy)
        if p is not None:
            f2.set(xx, yy, p)

# ---- 2) erase old right arm, old sword, old left foot area ----
f2.clear(25, 14, 18, 23)   # old right arm + hilt (x25-42, y14-36)
f2.clear(28, 37, 15, 16)   # old sword hanging on the right (x28-42, y37-52)
f2.clear(0, 47, 13, 13)    # old left foot/boot (x0-12, y47-59)
f2.clear(0, 50, 30, 11)    # old ground shadows (x0-29, y50-60)

# ---- 3) white motion trail streaming from upper right, arching down behind the swing ----
trail = {
 7: (42, 42), 8: (40, 42), 9: (39, 41), 10: (38, 40), 11: (38, 39),
 12: (37, 38), 13: (36, 37), 14: (35, 36), 15: (34, 35), 16: (34,),
 17: (33,), 18: (33,), 19: (33,), 20: (32,), 21: (32,), 22: (32,),
 23: (31, 32), 24: (31,), 25: (31,), 26: (31, 32), 27: (32, 33), 28: (33,),
}
for yy, xs in trail.items():
    for xx in xs:
        put(f2, xx, yy, w)
fringe = [(41, 8), (39, 9), (38, 10), (37, 11), (36, 12), (35, 13), (34, 14),
          (33, 15), (33, 16), (32, 17), (32, 18), (32, 19), (31, 20), (31, 21),
          (30, 22), (30, 23), (30, 24), (31, 25), (32, 26), (32, 27), (33, 28),
          (34, 27), (33, 26), (34, 25), (35, 24), (36, 23), (37, 22)]
for xx, yy in fringe:
    if f2.get(xx, yy) == 0:
        f2.set(xx, yy, c)

# ---- 4) left (front) foot steps forward: shift original left boot 3 px toward the enemy ----
for yy in range(53, 60):
    for xx in range(3, 13):
        p = px(src, xx, yy)
        if p is not None and p != Z:
            f2.set(xx - 3, yy, p)
# reconnect shin -> shifted boot
shin = [
    (5, 50), (6, 51), (5, 52), (4, 53), (3, 54), (3, 55), (2, 55),
]
for xx, yy in shin:
    put(f2, xx, yy, B)
put(f2, 4, 52, Tq); put(f2, 5, 51, Tq); put(f2, 6, 52, Tq)
# outline where boot meets shin
put(f2, 3, 53, K); put(f2, 4, 54, K); put(f2, 2, 54, K)
# new shadow under the stepped foot and under the back foot
shadow1 = [(3,58),(4,58),(5,59),(2,59),(3,59),(4,60),(5,60),(6,59),(7,59)]
shadow2 = [(15,57),(16,57),(17,57),(18,57),(19,57),(20,57),(15,58),(16,58)]
for sx, sy2 in shadow1 + shadow2:
    put(f2, sx, sy2, Z)

# ---- 5) right arm swinging down ----
arm = {
 17: (22, 24), 18: (22, 25), 19: (23, 25), 20: (23, 26), 21: (24, 26),
 22: (24, 27), 23: (25, 27), 24: (25, 28), 25: (26, 28), 26: (26, 29),
 27: (27, 30), 28: (28, 30),
}
for yy, (xa, xb) in arm.items():
    for xx in range(xa, xb + 1):
        f2.set(xx, yy, y)
for xx, yy in [(22, 17), (23, 17), (22, 18), (23, 20), (24, 22), (25, 23), (26, 25), (26, 27), (27, 28)]:
    f2.set(xx, yy, Y)
for xx, yy in [(24, 18), (25, 20), (26, 22), (27, 24), (28, 26), (29, 27)]:
    f2.set(xx, yy, W)

# gauntlet
for xx, yy in [(29, 29), (30, 29), (31, 29), (30, 30), (31, 30), (30, 31), (29, 30), (31, 31)]:
    f2.set(xx, yy, O)
put(f2, 29, 30, o); put(f2, 32, 31, o)

# ---- 6) heavy sword, edge down in front of the body ----
put(f2, 31, 29, B); put(f2, 32, 30, B)   # grip
# crossguard
for xx in range(28, 37):
    f2.set(xx, 31, Y)
put(f2, 28, 31, W); put(f2, 36, 31, W); put(f2, 27, 31, G); put(f2, 37, 31, G)
put(f2, 32, 30, D); put(f2, 31, 31, D)
# blade
for yy in range(32, 49):
    put(f2, 29, yy, K); put(f2, 36, yy, K)
    for xx in range(30, 36):
        f2.set(xx, yy, h)
    put(f2, 31, yy, H)
put(f2, 29, 49, K); put(f2, 30, 49, H); put(f2, 28, 49, K)
# glints
for xx, yy in [(31, 34), (30, 41), (32, 45)]:
    f2.set(xx, yy, w)
# shading on the blade edge
for xx, yy in [(35, 35), (35, 38), (34, 43), (34, 47)]:
    f2.set(xx, yy, o)

print("f2 built")
print(f2.stats_text())

# ---- 8) reconnect left knee to the stepped boot (bridging diagonal) ----
for xx, yy, colv in [
    (9, 47, D), (8, 48, D), (8, 49, D), (7, 50, D), (6, 51, D),
    (5, 52, B), (5, 53, B), (4, 54, B), (3, 55, B), (2, 56, B),
    (7, 49, Tq), (6, 50, Tq), (5, 51, Tq), (4, 52, Tq),
]:
    put(f2, xx, yy, colv)

# ---- 9) visual check: letter map of frame 2 ----
pal = f2.palette()
print("frame2 map:")
for y in range(ROWS):
    line = []
    for x in range(COLS):
        i = f2.get(x, y)
        line.append('.' if i == 0 else chr(33 + i) if i < 90 else '?')
    print(f"{y:2d}|{''.join(line)}")
print("  |" + "".join(str(x % 10) for x in range(COLS)))

# ---- submit ----
finish([f1, f2])
print("SUBMITTED 2 frames")

