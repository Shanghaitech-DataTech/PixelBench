from pixelbench_api import *

input_canvas = canvas("input")

arm = new_canvas(43, 61, name="arm")
body = input_canvas.copy(name="body")

thresholds = {
    0: 19, 1: 19, 2: 19, 3: 19, 4: 19, 5: 19, 6: 19, 7: 19,
    8: 24, 9: 24, 10: 25, 11: 26, 12: 28, 13: 29, 14: 30, 15: 30,
    16: 30, 17: 30, 18: 29, 19: 29, 20: 28, 21: 28, 22: 27, 23: 26, 24: 27
}

for y, tx in thresholds.items():
    for x in range(tx, 43):
        c = input_canvas.get(x, y)
        if c != 0:
            arm.set(x, y, c)
            body.set(x, y, 0)

leg = new_canvas(43, 61, name="leg")
for y in range(41, 57):
    for x in range(23, 43):
        c = body.get(x, y)
        if c != 0:
            leg.set(x, y, c)
            body.set(x, y, 0)

f1 = new_canvas(80, 80, name="f1")
f1.blit(input_canvas, 18, 10)

f2 = new_canvas(80, 80, name="f2")
f2.blit(body, 18, 10)
f2.blit(leg, 18 - 4, 10 + 1)

f2.path("M 44 14 Q 65 20 54 44 L 47 40 Q 55 22 40 18 Z", "#ffffff")

arm_sel = arm.select(19, 0, 24, 26)
arm_rot = arm_sel.rotate(135)
arm_rot.copy_to(27, 24, f2, mode="over")

finish([f1, f2])
