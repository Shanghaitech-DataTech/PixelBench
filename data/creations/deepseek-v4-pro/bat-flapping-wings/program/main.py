from pixelbench_api import *

src = input_canvas

# Animation canvas: taller than the input so the raised wings fit above the head.
dy = 10          # vertical offset: body stays put in both frames
ys = 5.5         # shoulder line used to fold the drooping wings upward
W, H = 27, 32

names = {0: '.', 1: 'k', 2: 'b', 3: 'p', 4: 'P', 5: 'g', 6: 'r', 7: 'y', 8: 'm'}

# --- Frame 1: original picture content, placed on the shared canvas ---
f1 = new_canvas(W, H, name='frame1')
f1.blit(src, 0, dy)

# --- Frame 2: same body, wings folded upward into a spread position ---
f2 = new_canvas(W, H, name='frame2')

# Keep the central body/head/legs (columns 9..17 inclusive).
for y in range(src.h):
    for x in range(9, 18):
        i = src.get(x, y)
        if i:
            f2.set(x, y + dy, i)

# Left wing: flip the drooping wing vertically about the shoulder line.
for y in range(5, src.h):
    for x in range(0, 10):
        i = src.get(x, y)
        if i:
            ny = dy + int(round(2 * ys - y))
            if 0 <= ny < H:
                f2.set(x, ny, i)

# Right wing: same fold on the right side.
for y in range(5, src.h):
    for x in range(17, 27):
        i = src.get(x, y)
        if i:
            ny = dy + int(round(2 * ys - y))
            if 0 <= ny < H:
                f2.set(x, ny, i)

print('frame1', f1.stats_text())
print('frame2', f2.stats_text())

# Show both frames as text grids for verification.
for label, c in [('F1', f1), ('F2', f2)]:
    print(f'--- {label} ---')
    for y in range(H):
        row = []
        for x in range(W):
            row.append(names.get(c.get(x, y), '?'))
        print(f'{y:2d} ' + ''.join(row))

finish([f1, f2])
