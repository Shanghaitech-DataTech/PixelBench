import numpy as np
import random

random.seed(7)

W = H = 170
out = input_canvas.copy(name="output")

# ---------- read pixels ----------
w, h, rgba = out.to_rgba()
arr = np.array(rgba, dtype=np.uint8).reshape(h, w, 4).astype(int)

# ---------- 1) remove the character (tall thin figure / pole, x=31..36, y=0..147) ----------
# fill the strip by interpolating between the untouched columns on either side,
# so the sky / street / anything behind it is reconstructed.
for y in range(0, 149):
    L = arr[y, 29, :3].astype(float)
    R = arr[y, 38, :3].astype(float)
    for x in range(30, 38):
        t = (x - 30) / 7.0
        arr[y, x, 0] = int(round(L[0] * (1 - t) + R[0] * t))
        arr[y, x, 1] = int(round(L[1] * (1 - t) + R[1] * t))
        arr[y, x, 2] = int(round(L[2] * (1 - t) + R[2] * t))
        arr[y, x, 3] = 255

# ---------- 2) thunderstorm darkening: sky and bluish surfaces go dark ----------
# (bright warm lights / the lit vending machine / neon keep their glow)
for y in range(H):
    for x in range(W):
        r = arr[y, x, 0]; g = arr[y, x, 1]; b = arr[y, x, 2]
        if b >= r and b >= g - 6 and max(r, g, b) <= 150:
            arr[y, x, 0] = int(r * 0.36)
            arr[y, x, 1] = int(g * 0.40)
            arr[y, x, 2] = int(b * 0.52)

# ---------- rebuild the base canvas ----------
out.clear()
for y in range(H):
    for x in range(W):
        out.set(x, y, (int(arr[y, x, 0]), int(arr[y, x, 1]), int(arr[y, x, 2]), 255))

# ---------- 3) heavy storm clouds across the top ----------
c1 = (7, 9, 16); c2 = (11, 13, 22); c3 = (16, 19, 30)
deck1 = [(6,7,24,8),(40,5,26,9),(76,7,24,8),(112,5,26,9),(148,7,24,8),(168,10,14,7)]
deck2 = [(22,18,22,8),(60,16,24,9),(98,19,22,8),(134,16,24,9),(164,20,18,8),(28,48,20,8)]
deck3 = [(8,30,18,7),(46,28,20,8),(84,31,18,7),(122,28,20,8),(158,31,17,7)]
deck4 = [(30,40,16,5),(70,42,18,5),(110,39,16,5),(148,42,16,5)]
for cx, cy, rx, ry in deck1:
    out.ellipse(cx, cy, rx, ry, c1, fill=True)
for cx, cy, rx, ry in deck2:
    out.ellipse(cx, cy, rx, ry, c2, fill=True)
for cx, cy, rx, ry in deck3:
    out.ellipse(cx, cy, rx, ry, c2, fill=True)
for cx, cy, rx, ry in deck4:
    out.ellipse(cx, cy, rx, ry, c3, fill=True)

# ---------- 4) lightning bolts in the background sky ----------
def stroke(pts, col):
    for i in range(len(pts) - 1):
        out.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], col)

glow = (70, 80, 125)
bolt = [(52,30),(57,41),(48,53),(55,65),(46,77),(52,89),(47,101)]
for dx, dy in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
    stroke([(x+dx, y+dy) for (x, y) in bolt], glow)
stroke(bolt, (255,255,240))
for br in [[(57,41),(65,49),(63,57)], [(48,53),(41,61)], [(55,65),(62,73),(60,81)]]:
    for dx, dy in [(0,0),(1,0),(0,1)]:
        stroke([(x+dx, y+dy) for (x, y) in br], glow)
    stroke(br, (235,240,255))

bolt2 = [(138,28),(143,38),(135,48),(140,58)]
for dx, dy in [(0,0),(1,0),(0,1)]:
    stroke([(x+dx, y+dy) for (x, y) in bolt2], (55,65,105))
stroke(bolt2, (215,225,255))

bolt3 = [(12,34),(8,44),(13,54)]
for dx, dy in [(0,0),(1,0)]:
    stroke([(x+dx, y+dy) for (x, y) in bolt3], (45,52,85))
stroke(bolt3, (180,190,225))

# ---------- 5) clinging water droplets on the wet ground / surfaces ----------
drop_cols = [(146,224,237),(97,179,203),(166,214,224),(196,242,240)]
def pick_drop():
    v = random.random()
    if v < 0.36: return drop_cols[0]
    if v < 0.66: return drop_cols[1]
    if v < 0.88: return drop_cols[2]
    return drop_cols[3]

placed = 0; guard = 0
while placed < 240 and guard < 6000:
    guard += 1
    x = random.randint(0, W-1); y = random.randint(122, H-1)
    r = arr[y,x,0]; g = arr[y,x,1]; b = arr[y,x,2]
    if max(r,g,b) > 180:
        continue
    col = pick_drop()
    out.set(x, y, col)
    arr[y,x,0], arr[y,x,1], arr[y,x,2], arr[y,x,3] = col[0], col[1], col[2], 255
    if random.random() < 0.45:
        dx, dy = random.choice([(1,0),(0,1),(-1,0),(0,-1)])
        xx = x + dx; yy = y + dy
        if 0 <= xx < W and 0 <= yy < H and max(arr[yy,xx,0], arr[yy,xx,1], arr[yy,xx,2]) <= 180:
            out.set(xx, yy, (97,179,203))
            arr[yy,xx,0], arr[yy,xx,1], arr[yy,xx,2], arr[yy,xx,3] = 97,179,203,255
    placed += 1

# droplets beading on the vending machine front
md = 0; guard = 0
while md < 14 and guard < 900:
    guard += 1
    x = random.randint(85, 117); y = random.randint(60, 150)
    m = max(arr[y,x,0], arr[y,x,1], arr[y,x,2])
    if m > 235 or m < 60:
        continue
    out.set(x, y, (210,244,246))
    md += 1

# ---------- 6) lightning flash / glow layer (semi-transparent) ----------
b1 = new_canvas(W, H, background=None, name="flash")
b1.ellipse(60, 46, 46, 28, (120,140,190,22), fill=True)
b1.ellipse(50, 142, 30, 16, (140,160,210,18), fill=True)
b1.ellipse(52, 32, 18, 10, (170,185,235,55), fill=True)
b1.ellipse(51, 58, 13, 30, (160,180,230,42), fill=True)
b1.ellipse(139, 42, 10, 17, (150,170,225,30), fill=True)
far = (165,185,215,55)
for i in range(280):
    x = random.randint(0, W-1); y = random.randint(0, H-6)
    ln = random.randint(3, 4)
    b1.line(x, y, max(0, x-1), y+ln, far)

# ---------- 7) near rain layer: semi-transparent streaks, droplets, splashes ----------
b2 = new_canvas(W, H, background=None, name="rain")
near = (210,228,248,105)
for i in range(200):
    x = random.randint(0, W-1); y = random.randint(0, H-9)
    ln = random.randint(4, 7)
    b2.line(x, y, max(0, x-2), y+ln, near)
dot = (200,220,245,90)
for i in range(60):
    x = random.randint(0, W-1); y = random.randint(0, H-1)
    b2.set(x, y, dot)
for i in range(30):
    x = random.randint(0, W-2); y = random.randint(0, H-2)
    b2.set(x, y, dot); b2.set(x+1, y, dot); b2.set(x, y+1, dot)
bright = (240,248,255,150)
for i in range(45):
    x = random.randint(76, W-1); y = random.randint(40, 148)
    ln = random.randint(3, 5)
    b2.line(x, y, max(0, x-1), y+ln, bright)
for i in range(25):
    x = random.randint(0, 75); y = random.randint(40, 140)
    ln = random.randint(3, 5)
    b2.line(x, y, max(0, x-1), y+ln, bright)
sp = (205,225,245,120)
for i in range(55):
    x = random.randint(2, W-3); y = random.randint(151, H-2)
    b2.set(x, y, sp); b2.set(x-1, y-1, sp); b2.set(x+1, y-1, sp)
for i in range(12):
    x = random.randint(8, W-9); y = random.randint(151, H-3)
    b2.ellipse(x, y, 2, 1, (190,215,240,90), fill=False)
# faint reflection of the main bolt on the wet street
b2.line(50, 148, 48, 166, (190,205,245,70))
b2.line(52, 150, 50, 161, (220,232,252,90))

result = flatten([out, b1, b2], name="result")
print(result.stats_text())
print(result.matrix_text(region=(26, 60, 44, 76)))
print(result.matrix_text(region=(42, 40, 60, 60)))
finish(result)
