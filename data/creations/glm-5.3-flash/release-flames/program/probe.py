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
f2.clear(44, 21, 11, 5)

# precise dump: index 0 -> '.', else hex digit
def dump(c, x0, x1, y0, y1):
    hdr = ''.join(str((x // 10) % 10) if x % 5 == 0 else ' ' for x in range(x0, x1 + 1))
    hdr2 = ''.join(str(x % 10) if x % 5 == 0 else ' ' for x in range(x0, x1 + 1))
    print('x:  ' + hdr)
    print('    ' + hdr2)
    for y in range(y0, y1 + 1):
        row = ''
        for x in range(x0, x1 + 1):
            v = c.get(x, y)
            row += '.' if v == 0 else ('%x' % v)
        print(f'{y:3d} ' + row)


dump(f2, 34, 66, 14, 30)
print()
# fist extent per row
for y in range(18, 27):
    xs = [x for x in range(34, 54) if f2.get(x, y) != 0]
    print('row', y, 'solid x:', (min(xs), max(xs)) if xs else None)
