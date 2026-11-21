# bat-flapping-wings: 2 frames on a shared 39x34 canvas.
# frame 1 = the original picture, centred on the larger canvas
# frame 2 = same body/head/legs, wings rotated up into a spread, raised pose
BLACK = "#1d181e"
DARK  = "#432f53"
MID   = "#5c436f"
GREY  = "#5f5f7b"
PINK  = "#b572b1"
BLUE  = "#7784a2"
CREAM = "#fff9d6"

W, H = 39, 34
OX, OY = 6, 10                      # original 27x22 placed here (centred)

# ---------------- frame 1 : the original picture -------------------------------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, OX, OY)

# ---------------- frame 2 : wings opened up ------------------------------------
# body only (original columns x=9..17); the drooping wings are dropped
body = input_canvas.copy(name="body")
body.clear(0, 0, 9, 22)
body.clear(18, 0, 9, 22)

# raised left wing: fill span per row (y, x first, x last)
spans = [
    (4,  5,  6),    # wing tip / claw, above the head
    (5,  4,  6),
    (6,  3,  7),
    (7,  3,  8),
    (8,  2,  9),
    (9,  4, 10),
    (10, 5, 11),
    (11, 4, 12),
    (12, 2, 13),
    (13, 3, 14),
    (14, 4, 18),    # right end runs behind the body
    (15, 5, 18),
    (16, 6, 18),
    (17, 7, 18),
    (18, 8, 18),
    (19, 9, 18),
    (20, 10, 18),
    (21, 12, 18),
    (22, 14, 18),
]
wing = new_canvas(W, H, name="wingL")
for (y, x0, x1) in spans:
    wing.rect(x0, y, x1 - x0 + 1, 1, DARK)

# membrane detail: band inside the leading edge (the arm) + finger streaks
for y in range(7, 18):
    wing.set(y - 1, y, MID)
for i in range(0, 5):
    wing.set(5 + i, 9 + i, MID)
for i in range(0, 4):
    wing.set(7 + i, 15 + i, MID)
for (x, y) in [(5, 9), (6, 12), (8, 15), (10, 18), (12, 20)]:
    wing.set(x, y, PINK)
for (x, y) in [(7, 7), (10, 11), (12, 14), (14, 17)]:
    wing.set(x, y, GREY)

wing.outline(BLACK)

f2 = new_canvas(W, H, name="frame2")
wingR = wing.copy(name="wingR")
wingR.mirror("h")
f2.blit(wing, 0, 0)
f2.blit(wingR, 0, 0)
f2.blit(body, OX, OY)               # body on top: clean shoulder join

save("bat_flap", f1)
save("bat_flap", f2)
print(f1.stats_text())
print(f2.stats_text())
finish([f1, f2])
