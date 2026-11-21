from pixelbench_api import *

src = input_canvas
W, H = 37, 33

W0, H0, rgba = src.to_rgba()
grid = {}
for y in range(H0):
    for x in range(W0):
        i = (y * W0 + x) * 4
        a = rgba[i + 3]
        if a > 0:
            grid[(x, y)] = (rgba[i], rgba[i + 1], rgba[i + 2], a)

dark = (20, 27, 27)
light = (255, 225, 141)
body = (173, 188, 58)
shade = (116, 163, 52)
brown = (200, 150, 107)
cream = (252, 226, 202)

def dx_for(y):
    if y <= 10:
        return 3
    if y <= 20:
        return 2
    if y <= 27:
        return 1
    return 0

# ---------------- Frame 1: original ----------------
f1 = src.copy(name="f1")

# ---------------- Frame 2: recoil ----------------
f2 = new_canvas(W, H, name="f2")
for (x, y), (r, g, b, a) in grid.items():
    if x <= 14 and y >= 27:
        nx, ny = x, y - 3          # monster's right foot (image-left) lifts off the ground
    else:
        nx, ny = x + dx_for(y), y   # upper body leans back to the right
    if 0 <= nx < W:
        f2.set(nx, ny, (r, g, b, a))

# repair the clipped right outline at rows 19-20
f2.set(36, 19, shade)
f2.set(36, 20, dark)

# eye rolls upward: pupil moves to the top of the eye
for x in range(19, 24):
    for y in range(13, 16):
        f2.set(x, y, dark)
# whites below the rolled pupil
for x in range(15, 26):
    for y in range(16, 19):
        f2.set(x, y, cream)
# mouth opens: teeth row on top, dark open mouth below, tongue
for x in range(15, 26):
    f2.set(x, 20, cream)
for x in range(14, 27):
    f2.set(x, 21, cream)
for y in range(22, 26):
    for x in range(14, 27):
        f2.set(x, y, dark)
for x in range(17, 22):
    f2.set(x, 24, brown)

# ---------------- Frame 3: blow landing, red filter ----------------
tint = {
    dark:  (149, 34, 34),
    light: (255, 123, 85),
    body:  (218, 106, 48),
    shade: (192, 95, 45),
    brown: (230, 89, 69),
    cream: (253, 123, 113),
}

f3 = new_canvas(W, H, name="f3")
pal = src.palette()
for y in range(H):
    for x in range(W):
        idx = f2.get(x, y)
        r, g, b, a = pal[idx]["rgba"]
        if a > 0:
            f3.set(x, y, tint.get((r, g, b), (r, g, b)))

# white impact flash where the blow lands (left side of the head)
for (fx, fy) in [(5, 9), (6, 7), (4, 11), (8, 6), (9, 8), (6, 13), (10, 11), (4, 13), (8, 14)]:
    f3.set(fx, fy, (255, 255, 255))

for name, c in [("f1", f1), ("f2", f2), ("f3", f3)]:
    print("==", name, c.stats_text())

print("--- f2 head/eye/mouth ---")
print(f2.matrix_text(region=(0, 0, 36, 27), indices=False))
print("--- f3 head/eye/mouth ---")
print(f3.matrix_text(region=(0, 0, 36, 27), indices=False))

finish([f1, f2, f3])
