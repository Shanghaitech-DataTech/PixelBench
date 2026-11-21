from pixelbench_api import *

ORANGE = 13   # c12 #f27219
YELLOW = 14   # c13 #f4a30c
BRIGHT = 15   # c14 #fed32c

src = input_canvas
sw, sh = src.stats()['size']   # 47 x 63
W, H = 100, 63

# ---------- Frame 1: original content, kept exactly ----------
f1 = new_canvas(W, H, name='f1')
f1.blit(src, 0, 0)

# ---------- Frame 2: thrusting pose + flying flame ----------
grid = [[src.get(x, y) for x in range(sw)] for y in range(sh)]

def lean_dx(y):
    if y <= 9:   return 6   # head leans in most
    if y <= 19:  return 5
    if y <= 29:  return 4
    if y <= 36:  return 2
    if y <= 44:  return 1
    return 0

def step_dx(x, y):
    # left foot (back foot) steps forward to the right
    if x <= 13:
        if y >= 55:   return 9
        if y >= 52:   return 5
        if y >= 50:   return 2
    return 0

out = [[0] * W for _ in range(H)]
for y in range(sh):
    for x in range(sw):
        idx = grid[y][x]
        if idx == 0:
            continue
        if idx in (ORANGE, YELLOW, BRIGHT):
            continue   # remove the old flame
        dx = x + lean_dx(y) + step_dx(x, y)
        dy = y
        if 0 <= dx < W and 0 <= dy < H:
            out[dy][dx] = idx

f2 = new_canvas(W, H, name='f2')
for y in range(H):
    for x in range(W):
        if out[y][x] != 0:
            f2.set(x, y, out[y][x])

# ----- fire spell flying forward with a fiery trail -----
hx, hy = 40, 22    # hand / launch point
cx, cy = 72, 18    # fireball centre

# tapering orange trail from the hand to the fireball
for i in range(41):
    t = i / 40.0
    x = round(hx + (cx - hx) * t)
    y = round(hy + (cy - hy) * t)
    r = 1 + int(6 * t)
    f2.circle(x, y, r, ORANGE, fill=True)

# yellow core along the rear of the trail
for i in range(20, 41):
    t = i / 40.0
    x = round(hx + (cx - hx) * t)
    y = round(hy + (cy - hy) * t)
    r = int(4 * (t - 0.45) / 0.55)
    if r > 0:
        f2.circle(x, y, r, YELLOW, fill=True)

# fireball head with hot core
f2.circle(cx, cy, 8, ORANGE, fill=True)
f2.circle(cx, cy, 6, YELLOW, fill=True)
f2.circle(cx - 1, cy - 1, 3, BRIGHT, fill=True)

# flame licks around the fireball and trail edges
for px, py, col in [
    (cx - 9, cy - 3, ORANGE), (cx - 10, cy + 1, ORANGE),
    (cx - 8, cy + 6, ORANGE), (cx - 3, cy + 9, YELLOW),
    (cx + 3, cy + 9, YELLOW), (cx + 8, cy + 5, ORANGE),
    (cx + 9, cy - 1, ORANGE), (cx + 7, cy - 6, ORANGE),
    (cx + 2, cy - 9, ORANGE), (cx - 4, cy - 8, YELLOW),
    (45, 17, ORANGE), (50, 15, ORANGE), (55, 13, ORANGE),
    (62, 12, ORANGE), (66, 13, ORANGE), (48, 24, ORANGE),
    (54, 25, ORANGE), (60, 25, ORANGE), (66, 26, ORANGE),
]:
    f2.set(px, py, col)

# flying sparks / embers
for px, py, col in [
    (46, 15, ORANGE), (50, 23, YELLOW), (55, 14, ORANGE),
    (59, 24, BRIGHT), (63, 11, ORANGE), (67, 26, YELLOW),
    (78, 12, ORANGE), (83, 20, YELLOW), (87, 15, BRIGHT),
    (44, 24, YELLOW),
]:
    f2.set(px, py, col)

print("f1", f1.stats_text())
print("f2", f2.stats_text())

sym = {5:'e',6:'f',8:'h',10:'j',12:'l',13:'m',14:'n',15:'o',
       1:'a',2:'b',3:'c',4:'d',7:'g',9:'i',11:'k'}

print()
print("=== f2 flame region y8-30 x30-100 ===")
for y in range(8, 31):
    row = ''
    for x in range(30, 100):
        idx = f2.get(x, y)
        row += sym.get(idx, '.')
    print(f"{y:3d} {row}")

print()
print("=== f2 feet region y48-62 x0-45 ===")
for y in range(48, 63):
    row = ''
    for x in range(0, 46):
        idx = f2.get(x, y)
        row += sym.get(idx, '.')
    print(f"{y:3d} {row}")

finish([f1, f2])
