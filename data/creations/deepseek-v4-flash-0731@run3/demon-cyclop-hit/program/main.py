from pixelbench_api import *

src = input_canvas
W, H = 37, 33
PW, PH = 42, 35   # shared frame size
OX, OY = 2, 1

src_px = [[src.get(x, y) for x in range(W)] for y in range(H)]
pal = {p['index']: p['rgba'] for p in src.palette()}

# ---------------- Frame 1: original picture content ----------------
f1 = new_canvas(PW, PH, name="f1")
f1.blit(src, OX, OY)

# ---------------- Frame 2: recoil pose ----------------
grid = {}
for y in range(H):
    # lean the body back: upper part shifts right, lower stays planted
    sh = 3 if y <= 8 else (2 if y <= 14 else (1 if y <= 22 else 0))
    for x in range(W):
        v = src_px[y][x]
        if v != 0:
            grid[(x + sh, y)] = v

# the monster's right foot (image-left) lifts off the ground
LIFT = 4
foot = [(x, y, src_px[y][x]) for y in range(26, 33) for x in range(5, 14) if src_px[y][x] != 0]
for (x, y, v) in foot:
    grid.pop((x, y), None)
for (x, y, v) in foot:
    grid[(x, y - LIFT)] = v

# single eye rolls upward: erase the old (lower) pupil, keep the whites,
# then draw the pupil at the top of the eye socket
for y in range(15, 22):
    for x in range(14, 28):
        if grid.get((x, y)) == 1:
            grid[(x, y)] = 6
for y in range(15, 18):
    for x in range(17, 22):
        grid[(x, y)] = 1

# mouth opens: dark interior, teeth, dark lips
mouth_dark = (118, 20, 24)
for x in range(14, 26):
    grid[(x, 23)] = 1      # upper lip
for y in range(24, 26):
    for x in range(14, 26):
        grid[(x, y)] = mouth_dark   # open interior
for x in range(15, 26, 2):
    grid[(x, 24)] = 6      # teeth
for x in range(14, 26):
    grid[(x, 26)] = 1      # lower lip

f2 = new_canvas(PW, PH, name="f2")
for (x, y), v in grid.items():
    f2.set(x + OX, y + OY, v)

# ---------------- Frame 3: blow landing + red filter over the monster ----------------
red = (235, 45, 55)
f3 = new_canvas(PW, PH, name="f3")
for y in range(H):
    for x in range(W):
        v = src_px[y][x]
        if v != 0:
            col = pal[v]
            rc = tuple(int(col[i] * 0.55 + red[i] * 0.45) for i in range(3)) + (255,)
            f3.set(x + OX, y + OY, rc)

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())

finish([f1, f2, f3])
