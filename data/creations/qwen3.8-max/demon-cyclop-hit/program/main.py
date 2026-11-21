from pixelbench_api import *

W, H = 40, 33

# ---------- Frame 1: original picture content ----------
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 3, 0)

# ---------- Frame 2: recoil pose (built on a 37x33 temp) ----------
t = input_canvas.copy(name="t2")

# erase left (monster's right) leg + foot
t.rect(5, 26, 9, 2, None)     # rows 26-27, cols 5-13
t.rect(2, 28, 12, 5, None)    # rows 28-32, cols 2-13

# repair body bottom-left contour after leg removal
for (x, y) in [(11, 26), (12, 26), (13, 26), (13, 27), (13, 28), (14, 29)]:
    t.set(x, y, 1)

# lifted foot tucked up in front of body (bottom row 28 -> 4px off ground)
t.rect(5, 24, 6, 1, 1)
t.rect(5, 25, 6, 1, 1); t.rect(6, 25, 4, 1, 4)
t.rect(5, 26, 6, 1, 1); t.rect(6, 26, 4, 1, 4)
t.rect(5, 27, 6, 1, 1); t.rect(6, 27, 4, 1, 4)
t.rect(5, 28, 5, 1, 1)
t.set(6, 28, 2); t.set(8, 28, 2)

# eye rolls upward: pupil to top of eye
t.rect(17, 16, 3, 3, 6)   # clear old pupil
t.rect(17, 15, 3, 3, 1)   # new pupil at top

# mouth opens: dark open mouth with tongue
t.rect(16, 22, 5, 1, 1)
t.rect(15, 23, 7, 2, 1)
t.rect(16, 25, 5, 1, 1)
t.rect(17, 25, 3, 1, 4)

# lean back: shear rows (top shifts left relative to planted foot)
f2 = new_canvas(W, H, name="f2")
for y in range(33):
    off = int(4 * (32 - y) / 32 + 0.5)
    for x in range(37):
        idx = t.get(x, y)
        if idx:
            f2.set(x + 3 - off, y, idx)

# ---------- Frame 3: blow lands - red filter over whole monster ----------
redmap = {1: (114, 29, 29), 2: (255, 108, 74), 3: (222, 94, 41),
          4: (199, 84, 39), 5: (233, 78, 61), 6: (253, 108, 99)}
f3 = new_canvas(W, H, name="f3")
for y in range(H):
    for x in range(W):
        idx = f2.get(x, y)
        if idx:
            f3.set(x, y, redmap[idx])

print(view(f1, scale=8, margin=2))
print(view(f2, scale=8, margin=2))
print(view(f3, scale=8, margin=2))

save("frame1_original", f1)
save("frame2_recoil", f2)
save("frame3_hit_red", f3)

finish([f1, f2, f3])
