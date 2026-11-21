from pixelbench_api import *
import math

W, H = 47, 43
OX, OY = 5, 6

# ---- Frame 1: original content on the new canvas ----
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, OX, OY)

# ---- Working sprite: recoil face (pupil up, mouth open) ----
m = f1.copy(name="m")
INK = m.color('#141b1b')   # dark outline colour (existing)
EYE = m.color('#fce2ca')   # eye white (existing)
TONG = m.color('#b03a2e')  # tongue red (new)

# pupil rolls upward: top row of eye gets pupil, bottom pupil row becomes white
for x in range(17, 20):
    m.set(OX + x, OY + 15, INK)
    m.set(OX + x, OY + 18, EYE)

# mouth opens: dark open mouth with tongue, replacing the closed dark-green mouth
for x in range(16, 21):          # row 22 top of mouth
    m.set(OX + x, OY + 22, INK)
for x in range(15, 22):          # row 23 full width
    m.set(OX + x, OY + 23, INK)
for x in (15, 16, 20, 21):       # row 24 sides
    m.set(OX + x, OY + 24, INK)
for x in (17, 18, 19):           # tongue
    m.set(OX + x, OY + 24, TONG)
    m.set(OX + x, OY + 25, TONG)
m.set(OX + 16, OY + 25, INK)
m.set(OX + 20, OY + 25, INK)

# ---- Frame 2: rotate sprite clockwise about the image-right foot ----
def rotate(src, angle, pivot, name):
    dst = new_canvas(W, H, name=name)
    th = math.radians(angle)
    c, s = math.cos(th), math.sin(th)
    px, py = pivot
    vis = {p['index'] for p in src.palette() if p['rgba'][3] > 0}
    for y in range(H):
        for x in range(W):
            dx, dy = x - px, y - py
            ix = round(px + c * dx + s * dy)
            iy = round(py - s * dx + c * dy)
            if 0 <= ix < W and 0 <= iy < H:
                idx = src.get(ix, iy)
                if idx in vis:
                    dst.set(x, y, idx)
    return dst

pivot = (OX + 28, OY + 32.5)   # bottom of the image-right foot (monster's left foot)
f2 = rotate(m, 12, pivot, "f2")

# fill single interior holes left by rotation
vis2 = {p['index'] for p in f2.palette() if p['rgba'][3] > 0}
def filled(x, y):
    return 0 <= x < W and 0 <= y < H and f2.get(x, y) in vis2
BODY = f2.color('#adbc3a')
for y in range(H):
    for x in range(W):
        if not filled(x, y):
            n = sum((filled(x+1,y), filled(x-1,y), filled(x,y+1), filled(x,y-1)))
            if n == 4:
                f2.set(x, y, BODY)

# ---- Frame 3: red impact filter over the whole monster ----
overlay = new_canvas(W, H, name="overlay")
RED = overlay.color((255, 0, 0, 130))
for y in range(H):
    for x in range(W):
        if f2.get(x, y) in vis2:
            overlay.set(x, y, RED)
f3 = flatten([f2, overlay], name="f3")

view(f2, scale=10, margin=0)
view(f3, scale=10, margin=0)
finish([f1, f2, f3])
