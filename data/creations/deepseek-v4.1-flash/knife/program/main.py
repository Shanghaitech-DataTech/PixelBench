import math

# ---------------------------------------------------------------- helpers
def crescent_d(x0, ytop, ybot, xout, xin):
    """Path data for a lens/crescent: two quadratic arcs meeting at sharp points."""
    ym = (ytop + ybot) / 2.0
    cout = 2 * xout - x0
    cin = 2 * xin - x0
    return "M%d,%d Q%.1f,%.1f %d,%d Q%.1f,%.1f %d,%d Z" % (
        x0, ytop, cout, ym, x0, ybot, cin, ym, x0, ytop)

def coarse(c, step=2, x0=0, y0=0, x1=None, y1=None):
    w, h, data = c.to_rgba()
    if x1 is None: x1 = w - 1
    if y1 is None: y1 = h - 1
    out = []
    for y in range(y0, y1 + 1, step):
        line = ''
        for x in range(x0, x1 + 1, step):
            ch = '.'
            for dy in range(step):
                for dx in range(step):
                    yy, xx = y + dy, x + dx
                    if yy < h and xx < w:
                        i = (yy * w + xx) * 4
                        r, g, b, a = data[i], data[i + 1], data[i + 2], data[i + 3]
                        if a == 0:
                            continue
                        if r > 235 and g > 235 and b > 235:
                            ch = '*'
                        elif a < 255:
                            if ch != '*':
                                ch = 'o'
                        else:
                            ch = '#'
            line += ch
        out.append('%3d|%s' % (y, line))
    return '\n'.join(out)

# ---------------------------------------------------------------- 1. pose the knife: tip to the right, cutting edge downward
work = new_canvas(280, 280, background=None, name='rot')
sel = input_canvas.select(0, 0, 93, 128)
rot = sel.rotate(125, algorithm='rotsprite')
rot.copy_to(0, 0, work)

ww, wh, wdata = work.to_rgba()
def wpx(x, y):
    i = (y * ww + x) * 4
    return (wdata[i], wdata[i + 1], wdata[i + 2], wdata[i + 3])

xs = [x for y in range(wh) for x in range(ww) if wpx(x, y)[3] > 0]
ys = [y for y in range(wh) for x in range(ww) if wpx(x, y)[3] > 0]
bb = (min(xs), min(ys), max(xs), max(ys))
print('knife bbox (work)', bb, 'size', bb[2] - bb[0] + 1, bb[3] - bb[1] + 1)

# ---------------------------------------------------------------- 2. final canvas
W, H = 272, 132
out = new_canvas(W, H, background=None, name='output')
X0, Y0 = 85, 50                       # where the knife bbox lands (tip ~ x 238)
KX, KY = X0 - bb[0], Y0 - bb[1]

# ---------------------------------------------------------------- 3. afterimages (farthest first)
GHOSTS = [(-78, 15, 50), (-52, 10, 95), (-26, 5, 150)]
for gx, gy, al in GHOSTS:
    for y in range(bb[1], bb[3] + 1):
        for x in range(bb[0], bb[2] + 1):
            r, g, b, a = wpx(x, y)
            if a == 0:
                continue
            tx, ty = x + KX + gx, y + KY + gy
            if 0 <= tx < W and 0 <= ty < H:
                out.set(tx, ty, (r, g, b, al))

# ---------------------------------------------------------------- 4. white slash: soft halo crescent
out.path(crescent_d(236, 12, 118, 264, 250), (255, 255, 255, 85), fill=True)

# ---------------------------------------------------------------- 5. the knife itself, on top of the ghosts
for y in range(bb[1], bb[3] + 1):
    for x in range(bb[0], bb[2] + 1):
        r, g, b, a = wpx(x, y)
        if a:
            tx, ty = x + KX, y + KY
            if 0 <= tx < W and 0 <= ty < H:
                out.set(tx, ty, (r, g, b, 255))

# ---------------------------------------------------------------- 6. white slash: bright core + sparks in front
out.path(crescent_d(240, 34, 96, 262, 256), (255, 255, 255, 245), fill=True)
for (sx, sy, ss, sa) in ((268, 32, 2, 210), (269, 92, 2, 180), (270, 62, 1, 230)):
    for dy in range(ss):
        for dx in range(ss):
            out.set(sx + dx, sy + dy, (255, 255, 255, sa))

print(out.stats_text())
print(coarse(out, 2))
print(out.matrix_text(region=(180, 46, 245, 92)))

finish(out)
