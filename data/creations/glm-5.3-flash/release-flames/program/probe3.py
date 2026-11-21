from pixelbench_api import *

W, H = 88, 63
OX = 8
C_M = '#f27219'; C_N = '#f4a30c'; C_O = '#fed32c'; C_F = '#010202'

f2 = new_canvas(W, H, background=None, name='probe')
f2.blit(input_canvas, OX, 0)
i_m = f2.color(C_M); i_n = f2.color(C_N); i_o = f2.color(C_O)
flame_idx = {i_m, i_n, i_o}


def shift_band(c, x0, y0, w, h, dx):
    s = c.select(x0, y0, w, h)
    s.move_to(x0 + dx, y0, c)


shift_band(f2, OX, 0, 47, 14, 4)
shift_band(f2, OX, 14, 47, 11, 3)
shift_band(f2, OX, 25, 47, 9, 2)
shift_band(f2, OX, 34, 47, 20, 1)
shift_band(f2, OX + 18, 54, 12, 7, 5)
f2.set(32, 54, C_F)

for y in range(H):
    for x in range(W):
        if f2.get(x, y) in flame_idx:
            f2.set(x, y, None)

# run-length dump of non-transparent pixels, region x28-70, y14-30
names = {}
for p in f2.palette():
    names[p['index']] = p['name']

for y in range(14, 31):
    runs = []
    x = 28
    while x <= 70:
        v = f2.get(x, y)
        if v == 0:
            x += 1
            continue
        x0 = x
        while x <= 70 and f2.get(x, y) == v:
            x += 1
        runs.append(f"x{x0}-{x-1}:{names.get(v, v)}")
    print(f"y{y}: " + ("  ".join(runs) if runs else "-"))

print()
print("original (36,12):", names.get(input_canvas.get(36, 12)), " (36,13):", names.get(input_canvas.get(36, 13)))
print("orig flame-colour pixels rows 10-15:")
for y in range(10, 16):
    xs = [x for x in range(0, 47) if input_canvas.get(x, y) in flame_idx]
    print(f"  y{y}: {xs}")
