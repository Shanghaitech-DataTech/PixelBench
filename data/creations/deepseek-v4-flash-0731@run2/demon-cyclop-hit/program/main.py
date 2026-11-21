from pixelbench_api import *

src = input_canvas
W, H = src.stats()["size"]  # 37 x 33

idx_a = src.color("#141b1b")      # black outline
YELLOW = "#ffe18d"                # teeth
RED    = (224, 46, 40, 255)
RED_H  = (255, 92, 64, 255)
WHITE  = (255, 255, 255, 255)

# ---------------------------------------------------------------
# Frame 1: original picture content
# ---------------------------------------------------------------
f1 = src.copy(name="f1")

# ---------------------------------------------------------------
# shear table: top of the body leans back (rows move right)
# ---------------------------------------------------------------
shear = [4]*8 + [2]*8 + [1]*9 + [0]*8

def shifted(src_canvas):
    c = new_canvas(W, H)
    for y in range(H):
        s = shear[y]
        for x in range(W):
            sx = x - s
            if 0 <= sx < W:
                pi = src_canvas.get(sx, y)
                if pi is not None:
                    c.set(x, y, pi)
    return c

# ---------------------------------------------------------------
# Frame 2: recoil  (body leans back, left foot lifts, eye up, mouth open)
# ---------------------------------------------------------------
f2 = shifted(src)

# --- monster's right foot (viewer-left) lifts off the ground ---
foot = new_canvas(9, 4)
for yy in range(4):
    for xx in range(9):
        pi = src.get(5 + xx, 29 + yy)   # x5-13, y29-32
        if pi is not None:
            foot.set(xx, yy, pi)
f2.clear(0, 27, 17, 6)          # erase the planted foot from the ground
f2.blit(foot, 5, 24)            # lifted foot, hovering above the ground

# --- single eye rolls upward ---
for yy in range(15, 21):
    for xx in range(14, 26):
        if f2.get(xx, yy) == idx_a:
            f2.set(xx, yy, None)
f2.rect(18, 15, 4, 2, idx_a)    # pupil rolled to the top of the eye

# --- mouth opens wide (narrower so it stays on the face) ---
f2.clear(11, 21, 14, 8)         # x11-24, y21-28
f2.rect(12, 21, 12, 1, idx_a)   # upper lip
f2.rect(12, 22, 12, 2, YELLOW)  # upper teeth
f2.rect(12, 24, 12, 3, idx_a)   # open dark mouth
f2.rect(12, 27, 12, 1, YELLOW)  # lower teeth
f2.rect(12, 28, 12, 1, idx_a)   # lower lip

# ---------------------------------------------------------------
# Frame 3: blow lands: red filter over the whole monster + impact flash
# ---------------------------------------------------------------
f3 = new_canvas(W, H, name="f3")
pal = {p["index"]: p["rgba"] for p in src.palette()}
for y in range(H):
    for x in range(W):
        pi = f2.get(x, y)
        if pi is not None:
            base = pal[pi]
            if base[3] == 0:
                continue
            mix = tuple(min(255, round(base[i] * 0.45 + RED[i] * 0.55)) for i in range(4))
            f3.set(x, y, mix)

# impact flash over the face/eye
f3.rect(18, 14, 3, 7, RED)      # vertical bar
f3.rect(15, 17, 9, 3, RED_H)    # horizontal bar
f3.rect(18, 17, 3, 3, WHITE)    # white hot core

print(f2.stats_text())
print("F2:")
print(f2.matrix_text())
print("F3:")
print(f3.matrix_text())

finish([f1, f2, f3])

