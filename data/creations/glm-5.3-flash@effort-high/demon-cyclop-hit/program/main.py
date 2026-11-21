SRC = input_canvas
W, H, rgba = SRC.to_rgba()

OUT   = '#141b1b'   # dark outline / pupil
HORN  = '#ffe18d'   # horn yellow
BODY  = '#adbc3a'   # body green
DARKG = '#74a334'   # dark green shading
LID   = '#c8966b'   # eyelid brown
EYEW  = '#fce2ca'   # eye white

OX, OY = 4, 4
CW, CH = 44, 38

def shear_dx(sy):
    # lean back: rows above the hips shift to the right, feet stay planted
    if sy <= 28:
        return int(round((28 - sy) * 0.12))
    return 0

def build_base(name):
    c = new_canvas(CW, CH, name=name)
    deferred = []
    for sy in range(H):
        for sx in range(W):
            i = (sy * W + sx) * 4
            r, g, b, a = rgba[i], rgba[i+1], rgba[i+2], rgba[i+3]
            if a == 0:
                continue
            col = '#%02x%02x%02x' % (r, g, b)
            cx = sx + OX + shear_dx(sy)
            cy = sy + OY
            # left foot (image left) lifts off the ground and kicks slightly right
            if 5 <= sx <= 13 and sy >= 29:
                cx += 1
                cy -= 3
            # pupil rolls upward: repaint its old spot white, redraw it 2px
            # higher, clipped so it stays inside the eyeball
            if col == OUT and 15 <= sy <= 20 and 16 <= sx <= 22:
                c.set(cx, cy, EYEW)
                if cy - 2 >= OY + 19:
                    deferred.append((cx, cy - 2, col))
                continue
            c.set(cx, cy, col)
    for cx, cy, col in deferred:
        c.set(cx, cy, col)
    return c

def open_mouth(c):
    # wipe the old closed mouth, then draw an open dark mouth
    for yy in range(OY + 22, OY + 25):
        for xx in range(OX + 14, OX + 25):
            c.set(xx, yy, BODY)
    c.ellipse(OX + 19, OY + 23, 3, 2, OUT)
    return c

# ---- frame 1: original picture content, repositioned on a larger canvas ----
f1 = new_canvas(CW, CH, name='output')
f1.blit(SRC, OX, OY)

# ---- frame 2: recoil pose ----
f2 = build_base('recoil')
open_mouth(f2)

# ---- frame 3: blow lands, red filter over the whole monster ----
f3 = build_base('impact')
open_mouth(f3)

RED = (225, 40, 55)
t = 0.55
w3, h3, rb = f3.to_rgba()
for y in range(h3):
    for x in range(w3):
        i = (y * w3 + x) * 4
        if rb[i+3] > 0:
            nr = int(round(rb[i]   * (1 - t) + RED[0] * t))
            ng = int(round(rb[i+1] * (1 - t) + RED[1] * t))
            nb = int(round(rb[i+2] * (1 - t) + RED[2] * t))
            f3.set(x, y, (nr, ng, nb, 255))

# impact sparks where the blow lands (left side)
f3.line(8, 21, 3, 19, EYEW)
f3.line(7, 24, 2, 24, EYEW)
f3.line(8, 27, 3, 29, EYEW)

finish([f1, f2, f3])

print('f1', f1.stats_text())
print('f2', f2.stats_text())
print('f3', f3.stats_text())

pal = {0:'.',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
for tag, cc in (('F1', f1), ('F2', f2), ('F3', f3)):
    print(f'--- {tag} ---')
    print('    ' + ''.join(str(i % 10) for i in range(CW)))
    for y in range(CH):
        print(f'{y:3d} ' + ''.join(pal.get(cc.get(x, y), '?') for x in range(CW)))

