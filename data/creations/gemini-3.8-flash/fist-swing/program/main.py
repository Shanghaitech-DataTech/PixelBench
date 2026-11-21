# Final submission: 2 frames of fist-swing animation

W = 38
H = 44

# Frame 1: Original picture content preserved on new canvas
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, 0)

# Frame 2: Character throwing a light punch with the left fist extending horizontally to the right
f2 = new_canvas(W, H, name="f2")
f2.blit(input_canvas, 0, 0)

c_out = input_canvas.color('#222034')  # c0
c_hair = input_canvas.color('#45283c') # c1
c_light = input_canvas.color('#eec39a')# c2
c_hair2 = input_canvas.color('#663931')# c3
c_mid = input_canvas.color('#df7126')  # c4
c_dark = input_canvas.color('#8f563b') # c5

# Clear only the old bent arm pixels from Frame 1:
f2.set(14, 7, None)
f2.set(15, 7, None)

for x in range(13, 17):
    f2.set(x, 8, None)

for x in range(13, 19):
    f2.set(x, 9, None)

for y in range(10, 15):
    for x in range(16, 22):
        f2.set(x, y, None)

# 1. Head & Neck (Exact Frame 1 profile)
f2.set(10, 7, c_light)
f2.set(11, 7, c_light)
f2.set(12, 7, c_light)
f2.set(13, 7, c_out)

f2.set(9, 8, c_dark)
f2.set(10, 8, c_light)
f2.set(11, 8, c_light)
f2.set(12, 8, c_out)

f2.set(9, 9, c_out)
f2.set(10, 9, c_mid)
f2.set(11, 9, c_mid)
f2.set(12, 9, c_out)

# 2. Clavicle & Trapezius
f2.set(13, 9, c_out)
f2.set(14, 9, c_out)
f2.set(15, 9, c_out)

# 3. Chest (Left Pec) & Ribs
f2.set(12, 10, c_out)
f2.set(13, 10, c_dark)
f2.set(14, 10, c_mid)
f2.set(15, 10, c_light)
f2.set(16, 10, c_mid)

f2.set(12, 11, c_mid)
f2.set(13, 11, c_light)
f2.set(14, 11, c_light)
f2.set(15, 11, c_mid)
f2.set(16, 11, c_dark)

f2.set(12, 12, c_light)
f2.set(13, 12, c_mid)
f2.set(14, 12, c_dark)
f2.set(15, 12, c_dark)
f2.set(16, 12, c_dark)
f2.set(17, 12, c_out)

f2.set(12, 13, c_light)
f2.set(13, 13, c_light)
f2.set(14, 13, c_mid)
f2.set(15, 13, c_dark)
f2.set(16, 13, c_dark)
f2.set(17, 13, c_out)

f2.set(12, 14, c_light)
f2.set(13, 14, c_light)
f2.set(14, 14, c_light)
f2.set(15, 14, c_dark)
f2.set(16, 14, c_dark)
f2.set(17, 14, c_out)

# 4. Shoulder (Deltoid)
f2.set(16, 8, c_out)
f2.set(17, 8, c_out)
f2.set(18, 8, c_out)

f2.set(16, 9, c_light)
f2.set(17, 9, c_light)
f2.set(18, 9, c_light)

f2.set(17, 10, c_light)
f2.set(18, 10, c_light)

f2.set(17, 11, c_mid)
f2.set(18, 11, c_mid)

# 5. Punching Arm
for x in range(19, 29):
    f2.set(x, 9, c_out)

for x in range(19, 29):
    f2.set(x, 10, c_light)

for x in range(19, 29):
    f2.set(x, 11, c_mid)

for x in range(18, 29):
    f2.set(x, 12, c_dark if x < 23 else c_mid)

for x in range(18, 29):
    f2.set(x, 13, c_out)

# 6. Clenched Fist
for x in range(29, 33):
    f2.set(x, 8, c_out)

# Row 9 (index knuckle):
f2.set(29, 9, c_light)
f2.set(30, 9, c_light)
f2.set(31, 9, c_light)
f2.set(32, 9, c_out)

# Row 10 (middle knuckle protruding forward):
f2.set(29, 10, c_light)
f2.set(30, 10, c_light)
f2.set(31, 10, c_light)
f2.set(32, 10, c_light)
f2.set(33, 10, c_out)

# Row 11 (ring knuckle):
f2.set(29, 11, c_mid)
f2.set(30, 11, c_mid)
f2.set(31, 11, c_light)
f2.set(32, 11, c_out)

# Row 12 (pinky / thumb):
f2.set(29, 12, c_dark)
f2.set(30, 12, c_dark)
f2.set(31, 12, c_out)

# Row 13 (fist bottom outline):
for x in range(29, 32):
    f2.set(x, 13, c_out)

view(f1)
view(f2)
finish([f1, f2])
