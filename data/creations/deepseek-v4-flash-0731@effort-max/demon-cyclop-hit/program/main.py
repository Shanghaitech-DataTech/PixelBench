from pixelbench_api import *

orig = input_canvas
SRC = [[orig.get(x, y) for x in range(37)] for y in range(33)]

# palette colours
K = orig.color((20, 27, 27))        # dark outline
Y = orig.color((255, 225, 141))     # horns / fangs
L = orig.color((173, 188, 58))      # light green
D = orig.color((116, 163, 52))      # dark green
T = orig.color((200, 150, 107))     # tan
P = orig.color((252, 226, 202))     # peach
RED1 = orig.color((148, 18, 32))     # dark red (outline)
RED2 = orig.color((219, 46, 52))     # red filter
RED3 = orig.color((252, 96, 64))     # bright red (highlights)
WHT = orig.color((250, 248, 242))   # impact flash

PX, PY = 5, 4
W, H = 48, 42
sh = {0:8, 1:8, 2:8, 3:7, 4:7, 5:7, 6:6, 7:6, 8:6, 9:5, 10:5, 11:5, 12:4,
      13:4, 14:4, 15:3, 16:3, 17:3, 18:3, 19:2, 20:2, 21:2, 22:2, 23:1, 24:1, 25:1, 26:1}

def draw_src(g, y0, y1, x0, x1, dy=0, dx=0):
    for y in range(y0, y1 + 1):
        ox = dx + sh.get(y, 0)
        for x in range(x0, x1 + 1):
            p = SRC[y][x]
            if p:
                g[PY + y + dy][PX + x + ox] = p

# ---------------- frame 1 : original picture content ----------------
f1 = [[0] * W for _ in range(H)]
for y in range(33):
    for x in range(37):
        f1[PY + y][PX + x] = SRC[y][x]

# ---------------- frame 2 : recoil pose ----------------
f2 = [[0] * W for _ in range(H)]
for y in range(0, 24):
    draw_src(f2, y, y, 0, 36)          # head + torso, leaning back
draw_src(f2, 24, 26, 0, 36)            # hips, arms, upper legs
draw_src(f2, 27, 28, 15, 36)           # right leg stays planted
for y in range(29, 33):                 # right foot stays planted
    for x in range(16, 37):
        if SRC[y][x]:
            f2[PY + y][PX + x] = SRC[y][x]
for y in range(29, 33):                  # LEFT foot lifts off the ground (up 5, right 4)
    for x in range(0, 15):
        if SRC[y][x]:
            f2[PY + y - 5][PX + x + 4] = SRC[y][x]

# eye rolls upward: pupil moves to the top of the eye (canvas coords)
for x in range(25, 28):
    f2[18][x] = K
    f2[19][x] = K
    f2[20][x] = P          # old pupil row becomes white of the eye again
for x in range(27, 30):
    f2[21][x] = P

# mouth opens wide (canvas coords), with teeth row and fangs
for x in range(21, 33):
    f2[25][x] = K
    f2[26][x] = K
for x in range(22, 32):
    f2[27][x] = K
for x in range(23, 30):
    f2[25][x] = T          # top teeth
for x in (23, 24, 28, 29):
    f2[27][x] = T          # bottom fangs

# ---------------- frame 3 : impact, red filter ----------------
redmap = {K: RED1, Y: RED3, L: RED2, D: RED2, T: RED2, P: RED3}
f3 = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        p = f2[y][x]
        if p:
            f3[y][x] = redmap.get(p, RED2)
# bright impact flash where the blow lands (right side of the head)
for pts in [(31, 36), (31, 37), (31, 39), (31, 40), (30, 38), (32, 38),
           (29, 37), (29, 39), (33, 37), (33, 39)]:
    f3[pts[0]][pts[1]] = WHT

def to_canvas(grid, name):
    c = new_canvas(W, H, name=name)
    for y in range(H):
        for x in range(W):
            p = grid[y][x]
            if p:
                c.set(x, y, p)
    return c

c1 = to_canvas(f1, "f1")
c2 = to_canvas(f2, "f2")
c3 = to_canvas(f3, "f3")

print(c1.stats_text())
print(c2.stats_text())
print(c3.stats_text())
cmap = {0: '.', 1: 'K', 2: 'Y', 3: 'L', 4: 'D', 5: 'T', 6: 'W', 7: 'r', 8: 'R', 9: 'O', 10: '#'}
for name, cv in [("F1", c1), ("F2", c2), ("F3", c3)]:
    print("==", name)
    for y in range(H):
        print(f"{y:2d}|" + ''.join(cmap.get(cv.get(x, y), '?') for x in range(W)))
finish([c1, c2, c3])
