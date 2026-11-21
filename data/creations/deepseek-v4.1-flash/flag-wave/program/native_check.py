import math

LW, LH = 12, 14          # native art resolution (48x56 is a 4x upscale of this)
W, H, F = 48, 56, 4

bad = 0
for y in range(0, H, F):
    for x in range(0, W, F):
        v = input_canvas.get(x, y)
        for dy in range(F):
            for dx in range(F):
                if input_canvas.get(x + dx, y + dy) != v:
                    bad += 1
print("non-uniform 4x4 blocks:", bad)

g = [[input_canvas.get(F * x, F * y) for x in range(LW)] for y in range(LH)]
SYM = {0: '.', 1: '#', 2: 'R', 3: 'r', 4: 'M', 5: 'P'}
for y in range(LH):
    print(f"{y:3d}  " + "".join(SYM[g[y][x]] for x in range(LW)))
print("     " + "".join(str(x % 10) for x in range(LW)))
