from pixelbench_api import *

src = input_canvas.copy(name="src")
W, H = 96, 64

def grab(x, y, w, h):
    s = new_canvas(w, h)
    s.blit(src, -x, -y)
    return s

# ---------------- Frame 1: original picture content --------------------------
f1 = new_canvas(W, H, name="f1")
f1.blit(src, 0, 0)

# ---------------- Frame 2: lunge thrust + released flame with trail -----------
f2 = new_canvas(W, H, name="f2")

# far (back) leg stays planted
f2.blit(grab(0, 44, 16, 19), 2, 44)
# rear arm swings back (body is shifted +6, arm only +3; same rows)
f2.blit(grab(0, 8, 16, 24), 3, 0)
# torso + hips lean forward (rows stay identical)
f2.blit(grab(0, 8, 47, 36), 6, 0)
# head leans further forward
f2.blit(grab(13, 0, 20, 10), 22, 0)
# step forward with the near (left) leg
f2.blit(grab(13, 44, 17, 19), 23, 44)
# remove the old front arm + held flame from the body, then thrust the arm out
f2.clear(35, 8, 20, 25)
armc = grab(30, 10, 17, 22)
armc.clear(41, 14, 6, 9)          # flame is now released from the hand
f2.blit(armc, 40, 8)

# ---- the released flame: trail streaming from the hand, fire flying forward ---
for (x, y, r, col) in [
    (57, 20, 3, 12), (61, 19, 3, 12), (65, 18, 3, 13), (69, 17, 3, 13),
    (73, 16, 2, 13), (76, 15, 2, 13),
]:
    f2.circle(x, y, r, col)
f2.circle(81, 14, 6, 12)   # main fire body (orange)
f2.circle(81, 13, 4, 13)   # (gold)
f2.circle(81, 12, 3, 14)   # (yellow core)
f2.circle(85, 10, 2, 13)
f2.circle(88, 8, 2, 12)
f2.circle(90, 7, 1, 13)
f2.circle(84, 11, 1, 14)
f2.circle(86, 15, 2, 13)
f2.circle(83, 18, 1, 13)
# flame flare right at the hand + embers
for (x, y, r, col) in [(55, 18, 2, 12), (69, 24, 1, 12), (82, 21, 1, 13),
                      (89, 13, 1, 12), (94, 11, 1, 13)]:
    f2.circle(x, y, r, col)

print("FRAME1")
print(f1.stats_text())
print("FRAME2")
print(f2.stats_text())

def rowstr(cv, x0, x1, y):
    out = []
    for x in range(x0, x1 + 1):
        i = cv.get(x, y)
        out.append("." if i == 0 else str(i))
    return "".join(out)

print("-- lower body rows 40..62, cols 0..55 --")
for y in range(40, 63):
    print(y, rowstr(f2, 0, 55, y))

finish([f1, f2])
