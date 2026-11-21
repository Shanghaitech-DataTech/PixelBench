# demon-cyclop-hit (edit)
# 3 frames:
# Frame 1: keeps the original picture content
# Frame 2: recoil pose (foot on left lifts off ground, whole body leans back, eye rolls upward, mouth opens)
# Frame 3: blow landing with red filter added over the whole monster

f1 = input_canvas.copy(name="frame1")

# Create Frame 2:
f2 = input_canvas.copy(name="frame2")

# 1. Body leans back (shift upper body rightwards):
# For rows 0 to 14, shift right by 2 pixels.
# For rows 15 to 21, shift right by 1 pixel.
# To keep outlines crisp and clean:
arr = [[input_canvas.get(x, y) for x in range(37)] for y in range(33)]

f2.clear()

for y in range(33):
    shift = 0
    if 0 <= y <= 14:
        shift = 2
    elif 15 <= y <= 21:
        shift = 1
    elif 22 <= y <= 25:
        shift = 1
    
    for x in range(37):
        col = arr[y][x]
        if col != 0:
            nx = x + shift
            if 0 <= nx < 37:
                f2.set(nx, y, col)

# 2. Foot on the left of the image (monster's right foot) lifts off the ground:
# Clear old left leg area (y=26..32, x=5..14)
for y in range(26, 33):
    for x in range(5, 14):
        f2.set(x, y, 0)

# Redraw left leg lifted up (knee bent, foot raised off ground by 3 pixels):
# Row 25: connect hip
f2.set(8, 25, 4).set(9, 25, 4).set(10, 25, 4).set(11, 25, 4)
# Row 26: thigh
f2.set(7, 26, 1).set(8, 26, 4).set(9, 26, 4).set(10, 26, 4).set(11, 26, 1)
# Row 27: knee bending up/forward
f2.set(6, 27, 1).set(7, 27, 4).set(8, 27, 4).set(9, 27, 4).set(10, 27, 4).set(11, 27, 1)
# Row 28: lower leg lifted
f2.set(5, 28, 1).set(6, 28, 4).set(7, 28, 4).set(8, 28, 4).set(9, 28, 4).set(10, 28, 1)
# Row 29: foot
f2.set(5, 29, 1).set(6, 29, 4).set(7, 29, 4).set(8, 29, 4).set(9, 29, 1)
# Row 30: claws lifted off ground
f2.set(5, 30, 1).set(6, 30, 2).set(7, 30, 4).set(8, 30, 2).set(9, 30, 1)
# Rows 31 and 32 remain completely transparent under the lifted foot!

# 3. Eye rolls upward:
# Upper body shifted by 1 at rows 15..21, so eye center is x=18..20
# Clear old eye area
for y in range(15, 22):
    for x in range(13, 26):
        # preserve surrounding skin if outside socket
        pass

# Sclera (6) and socket (5):
# y=15: socket top / sclera
f2.set(15, 15, 5).set(23, 15, 5)
for x in range(16, 23):
    f2.set(x, 15, 6)
# Pupil rolled up to top: rows 15 and 16, x=18..20
for x in range(18, 21):
    f2.set(x, 15, 1)
    f2.set(x, 16, 1)

# Sclera filling below the rolled-up pupil:
for y in range(17, 20):
    for x in range(16, 23):
        f2.set(x, y, 6)
# Socket rings
f2.set(14, 16, 5).set(24, 16, 5)
f2.set(13, 17, 5).set(14, 17, 5).set(24, 17, 5).set(25, 17, 5)
f2.set(13, 18, 5).set(14, 18, 5).set(24, 18, 5).set(25, 18, 5)
f2.set(14, 19, 5).set(15, 19, 5).set(23, 19, 5).set(24, 19, 5)
# Row 20: bottom socket
for x in range(15, 18):
    f2.set(x, 20, 5)
for x in range(18, 21):
    f2.set(x, 20, 6)
for x in range(21, 24):
    f2.set(x, 20, 5)
# Row 21: socket base
for x in range(17, 22):
    f2.set(x, 21, 5)

# 4. Mouth opens:
# At y=22..25, center shifted by 1 (around x=16..22)
# Row 22: upper lip
for x in range(17, 22):
    f2.set(x, 22, 1)
# Row 23: mouth opening with fangs (10) and dark interior (1)
f2.set(16, 23, 1).set(17, 23, 10).set(18, 23, 1).set(19, 23, 1).set(20, 23, 10).set(21, 23, 1).set(22, 23, 1)
# Row 24: red interior / tongue (7)
f2.set(16, 24, 1).set(17, 24, 1).set(18, 24, 7).set(19, 24, 7).set(20, 24, 7).set(21, 24, 1).set(22, 24, 1)
# Row 25: lower lip
for x in range(17, 22):
    f2.set(x, 25, 1)

# Frame 3: Blow landing with red filter added over the whole monster
f3 = new_canvas(37, 33, name="frame3")

# Red filter palette mapping:
# Yellow c1 (2) -> Orange gt08 (8)
# Light green c2 (3) -> Red gt07 (7)
# Dark green c3 (4) -> Dark orange gt09 (9)
# Eyelid c4 (5) -> Dark orange gt09 (9)
# Eye sclera c5 (6) -> White/cyan gt10 (10)
# Outline c0 (1) -> Outline c0 (1)
# Red mouth gt07 (7) -> Red gt07 (7)
# Teeth gt10 (10) -> Teeth gt10 (10)

remap = {
    1: 1,   # outline
    2: 8,   # gt08 orange
    3: 7,   # gt07 red
    4: 9,   # gt09 dark orange
    5: 9,   # gt09
    6: 10,  # gt10 light
    7: 7,   # red
    8: 8,   # orange
    9: 9,   # dark orange
    10: 10  # light
}

for y in range(33):
    for x in range(37):
        col = f2.get(x, y)
        if col != 0:
            f3.set(x, y, remap.get(col, col))

view(f1)
view(f2)
view(f3)

finish([f1, f2, f3])
