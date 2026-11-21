W, H = 220, 140
out = input_canvas.copy(name='output')
s = out.select(0, 0, 93, 128)
r = s.rotate(-45, algorithm="rotsprite")
prev = r.preview('rot')
bb = prev.stats()['bbox']
x0, y0, x1, y1 = bb
rot = prev.select(x0, y0, x1 - x0 + 1, y1 - y0 + 1)
print(rot.size)

canvas = new_canvas(W, H, background=None, name='knife_thrust')

# afterimages: three faded copies behind, shifted left
def stamp(layer, dx, dy, alpha, name):
    lay = new_canvas(W, H, background=None, name=name)
    rot.copy_to(0, 0, lay)
    lay.shift(dx, dy)
    # apply alpha by rewriting pixels with rgba
    w, h, rgba = lay.to_rgba()
    import numpy as np
    a = np.frombuffer(rgba, dtype=np.uint8).reshape(h, w, 4).copy()
    a[:, :, 3] = (a[:, :, 3].astype(int) * alpha // 255).astype(np.uint8)
    lay2 = new_canvas(W, H, background=None, name=name + '_a')
    # set pixels manually
    ys, xs = np.nonzero(a[:, :, 3])
    for y, x in zip(ys.tolist(), xs.tolist()):
        lay2.set(x + 40, y + 10, tuple(a[y, x]))
    return lay2

a3 = stamp(None, -46, 0, 70, 'after3')
a2 = stamp(None, -30, 0, 110, 'after2')
a1 = stamp(None, -15, 0, 170, 'after1')

main_lay = new_canvas(W, H, background=None, name='knife_main')
rot.copy_to(40, 10, main_lay, mode="replace")

# white slash effect: horizontal streaks along the blade row, ahead of tip
white = canvas.color('#ffffff', name='white')
slash = new_canvas(W, H, background=None, name='slash')
# blade occupies rows ~62-72; slash streaks
for (yy, xa, xb) in [(42, 150, 216), (46, 130, 219), (50, 140, 219), (54, 150, 216), (58, 160, 208)]:
    slash.line(xa, yy, xb, yy, white)
# a few tapered tips
slash.set(216, 43, white); slash.set(217, 44, white)
slash.set(218, 47, white); slash.set(219, 48, white)
slash.set(218, 51, white); slash.set(219, 52, white)
slash.set(216, 55, white); slash.set(217, 56, white)

result = flatten([a3, a2, a1, main_lay, slash], name='result')
print(result.matrix_text(region=(30, 5, 219, 70)))
finish(result)
