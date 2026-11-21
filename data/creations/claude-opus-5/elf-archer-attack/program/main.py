W, H = 44, 47

GOLD   = "#ffe75a"
AMBER  = "#fcc44c"
GOLD_D = "#bc6c0c"
BROWN  = "#7b4231"
DBROWN = "#422110"
OUT    = "#121311"
STRING = "#f6d39b"
SKIN   = "#c5956a"
SKIN_L = "#f6d39b"
SKIN_D = "#907859"
SLEEVE = "#687862"
SLV_L  = "#a4b496"
SLV_D  = "#3c3c3c"
PINK   = "#ef5ba1"
PINK_D = "#9e005d"

# ---------- frame 1 : original content, recentred ----------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 4, 0)

# ---------- strip the old bow, string and bow arm ----------
body = input_canvas.copy(name="body")
body.clear(23, 0, 12, 40)

upper = body.copy(name="upper")       # head + torso
upper.clear(0, 24, 35, 23)
lower = body.copy(name="lower")       # hips + legs
lower.clear(0, 0, 35, 24)

f2 = new_canvas(W, H, name="frame2")
f2.blit(lower, 4, 0)
f2.blit(upper, 3, 0)                  # torso leans 1px back

# ---------- bow, limbs bent hard forward ----------
f2.path("M 36 5 Q 43 11 41 18", BROWN, fill=False)
f2.path("M 41 21 Q 43 28 34 33", BROWN, fill=False)
f2.path("M 36 4 Q 42 11 40 18", GOLD, fill=False)
f2.path("M 35 32 Q 42 28 40 21", GOLD, fill=False)
f2.set(36, 4, AMBER)
f2.set(35, 32, AMBER)
f2.rect(40, 18, 2, 4, GOLD_D)         # grip
f2.set(40, 18, AMBER)
f2.set(40, 21, AMBER)
for by in (9, 10, 28, 29):            # pink wraps
    f2.set(42, by, PINK)
    f2.set(41, by, PINK_D)

# ---------- string drawn back to the anchor fist ----------
f2.line(36, 4, 26, 17, STRING)
f2.line(26, 17, 35, 32, STRING)

# ---------- bow arm, locked out to the grip ----------
f2.rect(24, 19, 11, 4, SLEEVE)
f2.line(24, 19, 34, 19, SLV_L)
f2.line(24, 22, 34, 22, SLV_D)
f2.line(25, 18, 34, 18, OUT)
f2.line(25, 23, 34, 23, OUT)
f2.rect(35, 18, 2, 5, SLV_D)          # cuff
f2.rect(37, 18, 3, 4, SKIN)           # hand on the grip
f2.set(37, 18, SKIN_L); f2.set(38, 18, SKIN_L)
f2.line(37, 21, 39, 21, SKIN_D)
f2.line(37, 17, 39, 17, OUT)
f2.line(37, 22, 39, 22, OUT)

# ---------- draw arm: elbow swung back, forearm rising to the fist ----------
# forearm, thin and diagonal from the elbow to the anchor
for dy, col in ((0, SKIN_L), (1, SKIN), (2, SKIN_D)):
    f2.line(10, 21 + dy, 23, 15 + dy, col)
f2.line(10, 20, 23, 14, OUT)
f2.line(10, 24, 23, 18, OUT)
# elbow
f2.poly([(6, 20), (10, 19), (11, 24), (7, 25)], SKIN)
f2.line(6, 20, 10, 19, OUT)
f2.line(7, 25, 11, 24, OUT)
f2.line(6, 21, 6, 24, OUT)
f2.set(7, 23, SKIN_D); f2.set(8, 24, SKIN_D)
# bracer across the forearm
f2.rect(14, 18, 3, 3, DBROWN)
f2.set(16, 17, DBROWN); f2.set(17, 17, DBROWN); f2.set(17, 18, DBROWN)
f2.set(14, 19, GOLD_D); f2.set(15, 18, GOLD_D); f2.set(16, 17, GOLD_D)
# fist closed on the string
f2.rect(23, 15, 3, 4, SKIN)
f2.set(23, 15, SKIN_L); f2.set(24, 15, SKIN_L)
f2.line(23, 18, 25, 18, SKIN_D)
f2.line(23, 14, 26, 14, OUT)
f2.line(23, 19, 26, 19, OUT)
f2.set(26, 15, OUT); f2.set(26, 18, OUT)
f2.set(26, 16, STRING); f2.set(26, 17, STRING)

view(f1)
view(f2)
finish([f1, f2])
