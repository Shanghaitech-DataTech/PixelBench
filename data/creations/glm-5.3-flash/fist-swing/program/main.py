from pixelbench_api import *

W, H = 36, 44

# ---------- frame 1: original picture content, on the shared larger canvas ----------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 0, 0)

# ---------- frame 2: same character, left-screen arm extended in a light punch ----------
f2 = new_canvas(W, H, name="frame2")
f2.blit(input_canvas, 0, 0)

OUT = f2.color('c0')    # dark outline      (index 1)
SKIN = f2.color('c2')   # skin              (index 3)
ORG = f2.color('c4')    # orange shading    (index 5)
BRN = f2.color('c5')    # brown shading     (index 6)


def hline(c, y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)


# 1) remove the old bent arm + fist (torso edge column x12..13 kept)
f2.clear(x=13, y=8, w=11, h=7)

# 2) shoulder / deltoid (as in the original)
f2.set(13, 8, SKIN); f2.set(14, 8, SKIN); f2.set(15, 8, ORG)
f2.set(13, 9, ORG);  f2.set(14, 9, SKIN); f2.set(15, 9, SKIN)
f2.set(13, 10, BRN)

# 3) straight arm, horizontal to the right (interior rows 9-11)
hline(f2, 8, 16, 23, OUT)       # top outline
hline(f2, 9, 14, 23, SKIN)
hline(f2, 10, 14, 23, SKIN)
f2.set(13, 11, ORG)
hline(f2, 11, 14, 23, ORG)      # underside shading
hline(f2, 12, 14, 23, OUT)      # bottom outline

# 4) torso side below the arm (original edge shape restored)
f2.set(13, 12, ORG)
f2.set(13, 13, SKIN); f2.set(14, 13, ORG); f2.set(15, 13, BRN); f2.set(16, 13, OUT)
f2.set(13, 14, SKIN); f2.set(14, 14, SKIN); f2.set(15, 14, BRN); f2.set(16, 14, OUT)

# 5) fist at the end of the jab (bulges one pixel above the arm)
hline(f2, 7, 24, 28, OUT)       # top outline (bulge)
hline(f2, 12, 24, 28, OUT)      # bottom outline
for y in range(7, 13):
    f2.set(28, y, OUT)          # front outline
# fist interior: light top-left -> dark bottom-right
f2.set(24, 8, SKIN); f2.set(25, 8, SKIN); f2.set(26, 8, SKIN); f2.set(27, 8, SKIN)
f2.set(24, 9, SKIN); f2.set(25, 9, SKIN); f2.set(26, 9, SKIN); f2.set(27, 9, SKIN)
f2.set(24, 10, SKIN); f2.set(25, 10, SKIN); f2.set(26, 10, ORG); f2.set(27, 10, ORG)
f2.set(24, 11, ORG); f2.set(25, 11, ORG); f2.set(26, 11, BRN); f2.set(27, 11, BRN)

# 6) small speed lines past the fist
hline(f2, 9, 30, 32, OUT)
hline(f2, 11, 30, 32, OUT)

# ---------- inspection ----------
print("f1:", f1.stats_text())
print("f2:", f2.stats_text())
diff = 0
for y in range(29):
    for x in range(29):
        if f1.get(x, y) != input_canvas.get(x, y):
            diff += 1
print("f1 pixels differing from input:", diff)
print("--- frame 2, upper body ---")
print(f2.matrix_text(region=(0, 0, 35, 22), indices=True))

# sanity: everything below the arm must match the input exactly
same = 0
for y in range(16, 44):
    for x in range(29):
        if f2.get(x, y) == input_canvas.get(x, y):
            same += 1
print("lower-body pixels identical to input:", same, "/ 406")

finish([f1, f2])
