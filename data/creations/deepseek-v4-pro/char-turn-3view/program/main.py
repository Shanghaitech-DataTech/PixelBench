from pixelbench_api import *

src = input_canvas.copy(name="src")
W, H = 66, 119

# 1-based palette ids as returned by get()
hair = {1, 2, 3, 4, 5, 6}                  # hair browns
face = {7, 8, 9, 10, 11, 12, 13, 14, 15}   # skin + eyes + red marks + face outline

# ------------------------------------------------------------------
# 3/4 views: rotate a flat sprite about the vertical axis by 45 deg.
# The projection is a horizontal foreshorten by cos(45) ~ 0.707
# (66 * 0.707 -> 47 px).  The two 3/4 views are mirror opposites.
# ------------------------------------------------------------------
def squash(flip=False, new_w=47):
    out = new_canvas(W, H)
    dx = (W - new_w) // 2
    for y in range(H):
        for nx in range(new_w):
            ox = round(nx * (W - 1) / (new_w - 1))
            if flip:
                ox = W - 1 - ox
            col = src.get(ox, y)
            if col != 0:
                out.set(dx + nx, y, col)
    return out

f1 = squash(flip=False)          # frame 1: turned to its left
f2 = f1.copy(name="f2")          # frame 2: opposite 3/4 view
f2.mirror("h")

# ------------------------------------------------------------------
# Rear view: the back of a front-facing sprite is its horizontal
# mirror with the face replaced by the back of the head (hair).
# The hair fill re-uses the existing hair texture so the palette and
# design stay identical.
# ------------------------------------------------------------------
rear = src.copy(name="rear")
rear.mirror("h")

for y in range(24, 51):
    src_y = 8 + ((y - 24) % 12)   # hair texture rows above the face
    for x in range(W):
        col = rear.get(x, y)
        if col in face:
            hcol = rear.get(x, src_y)
            if hcol in hair:
                rear.set(x, y, hcol)
            else:
                rear.set(x, y, 5)

print("f1", f1.stats_text())
print("f2", f2.stats_text())
print("rear", rear.stats_text())

finish([f1, f2, rear])
