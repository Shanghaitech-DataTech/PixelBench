from pixelbench_api import *

src = input_canvas
W, H = 26, 28

# ---- Frame 1: exact copy of the input ----
f1 = src.copy(name='frame1')

# ---- Frame 2: mid-leap hop, facing right ----
f2 = new_canvas(W, H, name='frame2')
D = '#efe9e7'   # fur white
A = '#3a3737'   # outline dark
B = '#b7b3b2'   # light grey shade
C = '#827c7c'   # mid grey shade
E = '#d6b39d'   # inner ear
F = '#bc8b6d'   # nose
G = '#cdae67'   # eye

# fur silhouette (drawn generously; outline() adds the dark rim)
# ears swept back
f2.poly([(6, 1), (10, 1), (17, 8), (13, 9)], D)
f2.poly([(11, 0), (15, 0), (20, 7), (16, 8)], D)
# head
f2.circle(18, 9, 4, D)
# body: diagonal oval, rump low-left, chest high-right
f2.poly([(5, 16), (7, 12), (13, 10), (19, 11), (22, 14), (19, 19), (10, 21), (5, 19)], D)
# front leg reaching forward-down
f2.poly([(16, 15), (19, 14), (24, 19), (21, 21)], D)
# hind leg trailing back-down
f2.poly([(8, 16), (11, 17), (5, 23), (2, 21)], D)
# tail
f2.circle(4, 13, 2, D)

f2.outline(A)

# inner ears
for x, y in [(9, 2), (10, 3), (11, 4), (12, 5), (13, 6),
             (14, 1), (15, 2), (16, 3), (17, 4), (18, 5)]:
    f2.set(x, y, E)
# eye and nose
f2.set(20, 8, G)
f2.set(22, 10, F)
f2.set(23, 10, A)
# haunch shading
for x, y in [(7, 15), (8, 15), (9, 15), (8, 16), (9, 16), (10, 16), (9, 17), (10, 17), (11, 17)]:
    f2.set(x, y, C)
# belly shading
for x in range(11, 18):
    f2.set(x, 17, B)
for x in range(11, 16):
    f2.set(x, 18, B)
for x in range(13, 18):
    f2.set(x, 16, B)
f2.set(6, 13, B)
f2.set(5, 14, B)
# soft ground shadow (airborne)
for x in range(10, 17):
    f2.set(x, 25, B)
for x in range(12, 15):
    f2.set(x, 26, B)

# finalize
print(f2.stats_text())
print(f1.stats_text())
finish([f1, f2])
