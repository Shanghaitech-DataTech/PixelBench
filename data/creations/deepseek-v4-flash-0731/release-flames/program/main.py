from pixelbench_api import *

W, H = 77, 63

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, 0)

f2 = f1.copy(name="f2")

# --- fire pixels of the original (indices 13,14,15) ---
FIRE = {13, 14, 15}
fire = [(x, y, f1.get(x, y)) for x in range(W) for y in range(H) if f1.get(x, y) in FIRE]
for x, y, idx in fire:
    f2.set(x, y, 0)


def move(c, x0, y0, x1, y1, dx, dy):
    pix = [(x, y, c.get(x, y)) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)
           if c.get(x, y) != 0]
    for x, y, idx in pix:
        c.set(x, y, 0)
    for x, y, idx in pix:
        c.set(x + dx, y + dy, idx)


# --- pose: body leans in (upper body shifts forward) ---
move(f2, 0, 0, 33, 32, 3, 0)
# --- pose: left (rear) foot steps forward ---
move(f2, 0, 33, 16, 62, 6, 0)

# --- flame flies forward: big flame base, original flame, trail, sparks ---
f2.ellipse(50, 21, 9, 6, "#8f2f07")
f2.ellipse(50, 19, 7, 5, "#b33d09")
f2.ellipse(51, 18, 6, 4, "#e05c0e")
# original flame moved forward (flies out)
for x, y, idx in fire:
    f2.set(x + 14, y, idx)
# fiery trail streaming back to the extended hand
f2.ellipse(45, 20, 5, 4, "#e05c0e")
f2.ellipse(41, 19, 3, 3, "#b33d09")
f2.ellipse(37, 21, 2, 2, "#8f2f07")
f2.ellipse(34, 18, 1, 1, "#8f2f07")
f2.ellipse(46, 16, 2, 1, "#b33d09")
# bright core
f2.ellipse(52, 15, 4, 3, "#fed32c")
f2.ellipse(49, 13, 2, 2, "#f4a30c")
# sparks ahead of the flame
for sx, sy in [(62, 21), (64, 15), (61, 9), (66, 18), (63, 25), (58, 7), (67, 13), (60, 27)]:
    f2.set(sx, sy, "#f4a30c")
for sx, sy in [(65, 12), (68, 17), (63, 10), (66, 23)]:
    f2.set(sx, sy, "#fed32c")
for sx, sy in [(69, 20), (60, 8), (66, 27), (64, 6), (56, 12)]:
    f2.set(sx, sy, "#f27219")
# motion streaks behind the flame
for yy in (10, 14, 18, 22, 26):
    f2.line(40, yy, 46, yy, "#e05c0e")
for yy in (12, 20, 24):
    f2.line(37, yy, 42, yy, "#f27219")
# flame tongues licking off the leading edge
f2.ellipse(57, 10, 2, 2, "#e05c0e")
f2.ellipse(60, 16, 2, 3, "#f4a30c")
f2.ellipse(56, 23, 2, 3, "#f27219")
# bright rim on the fireball front
f2.ellipse(55, 14, 2, 2, "#fed32c")
f2.ellipse(57, 19, 1, 2, "#fed32c")
# extra sparks trailing
for sx, sy in [(63, 20), (58, 26), (64, 22), (55, 5)]:
    f2.set(sx, sy, "#f4a30c")

print("f1", f1.stats_text())
print("f2", f2.stats_text())

# save exports
save("f1", f1)
save("f2", f2)

finish([f1, f2])
