OX, OY = 2, 1
W, H = 41, 35

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, OX, OY)

f2 = f1.copy(name="f2")

A = '#141b1b'   # outline / dark
C = '#adbc3a'   # body light green
F = '#fce2ca'   # eye white

# --- recoil pose ---
# 1. lean back: shift whole upper body (rows 0-21) right by 2
upper = f2.select(OX + 0, OY + 0, 37, 22)
upper.move_to(OX + 2, OY + 0, f2)

# 2. left foot (monster's right foot) lifts off the ground: up 2, right 1
foot = f2.select(OX + 0, OY + 24, 7, 6)
foot.move_to(OX + 1, OY + 22, f2)

# 3. eye rolls upward: erase pupil, redraw near top of the eye
f2.rect(OX + 18, OY + 16, 5, 4, F)
f2.rect(OX + 18, OY + 15, 5, 3, A)

# 4. mouth opens: clear closed mouth line, draw dark open mouth
f2.rect(OX + 17, OY + 23, 7, 2, C)
f2.ellipse(OX + 20, OY + 23, 3, 1, A)

# --- frame 3: same pose + red impact filter ---
f3 = f2.copy(name="f3")
w, h, rgba = f2.to_rgba()
overlay = new_canvas(W, H, name="ov")
for y in range(h):
    for x in range(w):
        i = (y * w + x) * 4
        r, g, b, a = rgba[i:i + 4]
        if a > 0:
            overlay.set(x, y, (255, 30, 20, 110))
f3 = flatten([f3, overlay], name="f3")

print(f2.stats_text())
print(f3.stats_text())
finish([f1, f2, f3])
