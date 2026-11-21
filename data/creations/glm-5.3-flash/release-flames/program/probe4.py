from pixelbench_api import *

W, H = 88, 63
OX = 8
C_M = '#f27219'; C_N = '#f4a30c'; C_O = '#fed32c'; C_F = '#010202'

names = {}
for p in input_canvas.palette():
    names[p['index']] = p['name']


def runs(c, x0, x1, y0, y1, label):
    print(label)
    for y in range(y0, y1 + 1):
        rr = []
        x = x0
        while x <= x1:
            v = c.get(x, y)
            if v == 0:
                x += 1
                continue
            xs = x
            while x <= x1 and c.get(x, y) == v:
                x += 1
            rr.append(f"{xs}-{x-1}:{names.get(v, v)}")
        print(f"y{y}: " + ("  ".join(rr) if rr else "-"))
    print()


runs(input_canvas, 24, 46, 16, 26, "=== ORIGINAL x24-46 ===")

# build the shifted + wiped frame exactly as in main
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

runs(f2, 30, 60, 16, 26, "=== FRAME2 (shifted+wiped) x30-60 ===")
