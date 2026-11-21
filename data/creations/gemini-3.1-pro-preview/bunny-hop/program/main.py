from pixelbench_api import input_canvas, view, new_canvas, finish

c1 = new_canvas(48, 32, name="frame1")
c1.blit(input_canvas, 10, 4)

c2 = new_canvas(48, 32, name="frame2")

legless = input_canvas.copy()
legless.clear(0, 20, 26, 8)
legless.line(1, 20, 20, 20, 1)
legless.line(2, 19, 19, 19, 4)

body_rot = legless.select(0, 0, 26, 21).rotate(-15)
body_rot.copy_to(12, 2, c2, mode="over")

front_leg = input_canvas.select(13, 20, 11, 8)
f_leg_rot = front_leg.rotate(-45)
f_leg_rot.copy_to(27, 15, c2, mode="over")

back_leg = input_canvas.select(0, 20, 12, 8)
b_leg_rot = back_leg.rotate(45)
b_leg_rot.copy_to(6, 15, c2, mode="over")

finish([c1, c2])
