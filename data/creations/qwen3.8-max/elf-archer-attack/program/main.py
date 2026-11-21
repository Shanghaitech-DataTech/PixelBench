from pixelbench_api import *

W, H = 40, 47

# ---------- Frame 1: original picture content on the shared canvas ----------
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 2, 0)

# ---------- Frame 2: bow fully open, drawn-bow stance ----------
f2 = new_canvas(W, H, name="f2")

# body (head, torso, legs, feet, upper bow-arm) shifted back +2
body = input_canvas.select(0, 0, 23, 47).preview()
f2.blit(body, 2, 0)

# whole bow (limbs, grip hand, bow tips) extended forward +4
bow = input_canvas.select(23, 0, 12, 40).preview()
f2.blit(bow, 27, 0)

# bridge the stretched bow-arm sleeve (repeat sleeve columns)
bridge = {(25, 19): 31, (26, 19): 32,
          (25, 20): 20, (26, 20): 2,
          (25, 21): 32, (26, 21): 14,
          (25, 22): 32, (26, 22): 14,
          (25, 23): 20, (26, 23): 20}
for (x, y), ci in bridge.items():
    f2.set(x, y, ci)

# erase the old undrawn string (cream 12 / tan 3 / highlight 4 pixels only)
for y in range(7, 19):
    for x in range(29, 34):
        if f2.get(x, y) in (12, 3, 4):
            f2.set(x, y, None)
for y in range(24, 36):
    for x in range(27, 31):
        if f2.get(x, y) in (12, 3, 4):
            f2.set(x, y, None)

# drawing arm: raised elbow flared back below the shoulder, forearm to cheek
f2.line(22, 20, 15, 17, 32)
f2.line(22, 21, 15, 18, 31)
f2.line(15, 17, 20, 13, 32)
f2.line(15, 18, 20, 14, 31)

# fully drawn string: top nock -> draw hand -> bottom nock
f2.line(32, 7, 22, 12, 12)
f2.line(22, 12, 29, 34, 12)

# draw hand pinching the string at the cheek
f2.set(20, 12, 29); f2.set(21, 12, 12); f2.set(22, 12, 12)
f2.set(20, 13, 12); f2.set(21, 13, 29); f2.set(22, 13, 12)
f2.set(19, 12, 20); f2.set(19, 13, 20)

view(f1)
view(f2)
finish([f1, f2])
