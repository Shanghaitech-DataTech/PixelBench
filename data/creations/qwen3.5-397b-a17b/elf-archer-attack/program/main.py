from pixelbench_api import *

# Frame 1: Keep the original picture content
f1 = input_canvas.copy(name="frame1")

# Frame 2: Drawn bow stance - full coverage archer
f2 = new_canvas(35, 47, background=None, name="frame2")

# Color indices from the shared palette
outline = 20  # t - #121311ff dark outline
skin = 3      # c - #c5956aff tan/skin
hair_dark = 10  # j - #55002aff dark purple
hair_pink = 11  # k - #ef5ba1ff pink
hair_mag = 21   # u - #9e005dff magenta
green1 = 22     # v - #529439ff green
green2 = 24     # x - #304915ff dark green
green3 = 26     # z - #9cde5aff light green
green4 = 32     # F - #687862ff medium green-grey
green5 = 33     # G - #a4b496ff light green-grey
brown = 1       # a - #422110ff brown
brown2 = 2      # b - #7b4231ff darker brown
white = 4       # d - #ffffffff white
dark_cloth = 25 # y - #14110eff very dark
tan = 12        # l - #f6d39bff light tan

# === BOW ===
bow_color = brown
bow_dark = brown2

# Bow limbs - thick, fill them in
for y in range(4, 19):
    x_base = 3
    offset = max(0, (18 - y) // 3)
    for ox in range(offset + 2):
        if 0 <= x_base - ox < 35:
            f2.set(x_base - ox, y, bow_color if ox == 0 else bow_dark)

for y in range(22, 41):
    x_base = 3
    offset = max(0, (y - 22) // 3)
    for ox in range(offset + 2):
        if 0 <= x_base - ox < 35:
            f2.set(x_base - ox, y, bow_color if ox == 0 else bow_dark)

# Bow grip
for y in range(18, 23):
    f2.set(4, y, bow_color)
    f2.set(5, y, bow_dark)
    f2.set(3, y, bow_dark)

# Bow string
string_color = white
f2.line(2, 4, 16, 14, string_color)
f2.line(16, 14, 2, 40, string_color)
f2.line(3, 5, 16, 14, string_color)
f2.line(16, 14, 3, 39, string_color)

# === BOOTS ===
for y in range(41, 47):
    for x in range(9, 17):
        f2.set(x, y, dark_cloth)
for y in range(41, 47):
    f2.set(9, y, outline)
    f2.set(16, y, outline)

for y in range(42, 47):
    for x in range(17, 25):
        f2.set(x, y, dark_cloth)
for y in range(42, 47):
    f2.set(17, y, outline)
    f2.set(24, y, outline)

# === LEGS ===
for y in range(32, 43):
    for x in range(10, 17):
        f2.set(x, y, green1)
for y in range(32, 43):
    f2.set(10, y, outline)
    f2.set(16, y, outline)

for y in range(34, 44):
    for x in range(17, 24):
        f2.set(x, y, green1)
for y in range(34, 44):
    f2.set(17, y, outline)
    f2.set(23, y, outline)

# === TORSO ===
for y in range(22, 35):
    for x in range(12, 25):
        f2.set(x, y, green2)

for y in range(24, 33):
    for x in range(14, 22):
        f2.set(x, y, green4)
    if y % 3 == 0:
        for x in range(13, 24, 2):
            f2.set(x, y, green1)

for y in range(22, 35):
    f2.set(12, y, outline)
    f2.set(24, y, outline)
for x in range(12, 25):
    f2.set(x, 34, outline)

for x in range(12, 25):
    f2.set(x, 33, brown)
    f2.set(x, 34, brown2)
    f2.set(x, 32, brown)

# === SHOULDERS ===
for y in range(20, 25):
    for x in range(11, 19):
        f2.set(x, y, green2)

for y in range(18, 24):
    for x in range(19, 28):
        f2.set(x, y, green2)

# === ARMS ===
for i in range(16):
    x = 15 - i
    y = 22 - (i // 6)
    if 0 <= x < 35 and 0 <= y < 47:
        for dy in range(4):
            if 0 <= y + dy < 47:
                f2.set(x, y + dy, skin)

f2.line(15, 22, 6, 21, outline)
f2.line(15, 26, 6, 25, outline)

for x in range(4, 9):
    for y in range(19, 25):
        f2.set(x, y, skin)

for i in range(12):
    x = 21 + i
    y = 20 - i
    if 0 <= x < 35 and 0 <= y < 47:
        for dx in range(3):
            for dy in range(3):
                if 0 <= x + dx < 35 and 0 <= y + dy < 47:
                    f2.set(x + dx, y + dy, skin)

for i in range(14):
    x = 28 - i
    y = 13 - (i // 5)
    if 0 <= x < 35 and 0 <= y < 47:
        for dy in range(4):
            if 0 <= y + dy < 47:
                f2.set(x, y + dy, skin)

f2.line(21, 20, 29, 12, outline)
f2.line(29, 12, 16, 12, outline)
f2.line(22, 24, 30, 16, outline)
f2.line(30, 16, 17, 16, outline)

for x in range(13, 19):
    for y in range(11, 17):
        f2.set(x, y, skin)

# === HEAD ===
for y in range(6, 24):
    for x in range(15, 33):
        if y < 10:
            if 17 <= x <= 30:
                f2.set(x, y, hair_dark)
        elif y < 14:
            if 16 <= x <= 32:
                if (x + y) % 2 == 0:
                    f2.set(x, y, hair_mag)
                else:
                    f2.set(x, y, hair_dark)
        elif y < 18:
            if 16 <= x <= 32:
                f2.set(x, y, hair_mag)
        else:
            if 18 <= x <= 31:
                f2.set(x, y, hair_pink)

for y in range(10, 19):
    for x in range(14, 19):
        f2.set(x, y, hair_dark)

for y in range(10, 18):
    for x in range(17, 25):
        f2.set(x, y, skin)

for y in range(10, 18):
    f2.set(17, y, outline)
    f2.set(24, y, outline)
for x in range(17, 25):
    f2.set(x, 10, outline)
    f2.set(x, 17, outline)

f2.set(19, 13, outline)
f2.set(20, 13, white)
f2.set(21, 13, white)
f2.line(18, 12, 22, 12, outline)
f2.set(22, 14, outline)
f2.set(23, 14, outline)
f2.set(19, 15, outline)
f2.set(20, 15, outline)
f2.set(21, 15, outline)
f2.set(22, 15, outline)
f2.set(24, 13, skin)
f2.set(25, 13, skin)
f2.set(24, 14, skin)

# === CAPE ===
for y in range(19, 38):
    for x in range(23, 34):
        if x >= 23 and x <= 33:
            if (x + y) % 3 == 0:
                f2.set(x, y, green3)
            else:
                f2.set(x, y, green2)

for y in range(19, 38):
    f2.set(23, y, outline)
    if y < 37:
        f2.set(33, y, outline)

for y in range(21, 37, 3):
    for x in range(25, 32):
        f2.set(x, y, green1)

# === QUIVER ===
for y in range(21, 33):
    for x in range(25, 31):
        f2.set(x, y, brown)
for y in range(21, 33):
    f2.set(25, y, outline)
    f2.set(30, y, outline)
for x in range(25, 31):
    f2.set(x, 32, outline)

# === ARM GUARDS ===
for y in range(21, 27):
    for x in range(8, 14):
        f2.set(x, y, brown2)
for y in range(21, 27):
    f2.set(8, y, outline)
    f2.set(13, y, outline)

for y in range(17, 22):
    for x in range(26, 31):
        f2.set(x, y, brown2)

# === CHEST ===
for y in range(23, 29):
    for x in range(14, 21):
        f2.set(x, y, green5)

# === HAIR strands ===
for y in range(8, 25):
    for x in range(14, 34):
        if f2.get(x, y) is None and (x * y) % 7 == 0:
            f2.set(x, y, hair_pink)

# === Fill gaps ===
for y in range(18, 38):
    for x in range(10, 28):
        if f2.get(x, y) is None:
            if 12 <= x <= 24 and 22 <= y <= 34:
                f2.set(x, y, green2)
            elif 10 <= x <= 16 and 32 <= y <= 42:
                f2.set(x, y, green1)
            elif 17 <= x <= 23 and 34 <= y <= 43:
                f2.set(x, y, green1)

print("F1 stats:", f1.stats_text())
print("F2 stats:", f2.stats_text())

save("frame1_preview", f1)
save("frame2_preview", f2)

finish([f1, f2])
