# squid-red-idle (edit) - 3-frame breathing idle
# Frame 1: original picture content (rest), placed with 1px of headroom on a 58x58 canvas.
# Frame 2: inhale  - mantle (head, eyes, mouth, fringe) rises 1px; leg columns stretch to stay connected.
# Frame 3: exhale  - mantle settles 1px down over the leg tops; feet stay planted throughout.

SRC = input_canvas
SW, SH = SRC.stats()['size']            # 58 x 57
W, H = SW, SH + 1                       # 58 x 58

LEG_X = [(12, 25), (32, 45)]            # sprite row 48 columns belonging to the legs


def stamp(dst, y0, y1, dy, x0=0, x1=SW - 1):
    """Stamp sprite rows y0..y1 so that sprite row y0 lands on canvas row dy."""
    for y in range(y0, y1 + 1):
        cy = dy + (y - y0)
        if 0 <= cy < H:
            for x in range(x0, x1 + 1):
                v = SRC.get(x, y)
                if v:
                    dst.set(x, cy, v)


def draw_mantle(dst, dy):
    stamp(dst, 0, 47, dy)               # head, eyes, mouth and scalloped fringe


def draw_legs(dst, dy):
    for a, b in LEG_X:                  # sprite row 48: only the leg columns
        stamp(dst, 48, 48, dy, a, b)
    stamp(dst, 49, 56, dy + 1)          # legs + planted feet


# ---- frame 1: rest (original content, 1px down to make bob headroom) ----
f1 = new_canvas(W, H, name='f1_rest')
draw_mantle(f1, 1)
draw_legs(f1, 49)

# ---- frame 2: inhale, mantle up 1px ----
f2 = new_canvas(W, H, name='f2_up')
draw_legs(f2, 49)
for a, b in LEG_X:                      # legs stretch 1px to meet the risen mantle
    stamp(f2, 48, 48, 48, a, b)
draw_mantle(f2, 0)

# ---- frame 3: exhale, mantle down 1px over the leg tops ----
f3 = new_canvas(W, H, name='f3_down')
draw_legs(f3, 49)
draw_mantle(f3, 2)

# ---- verification ----
mism = sum(1 for y in range(SH) for x in range(SW) if f1.get(x, y + 1) != SRC.get(x, y))
print('frame1 vs original (shifted 1px): mismatches =', mism)


def diff(a, b):
    rows, n = set(), 0
    for y in range(H):
        for x in range(W):
            if a.get(x, y) != b.get(x, y):
                n += 1
                rows.add(y)
    return n, sorted(rows)


print('diff f1->f2:', diff(f1, f2))
print('diff f1->f3:', diff(f1, f3))
for f in (f1, f2, f3):
    print(f.stats_text())

CHAR = {0: '.', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g'}
for f, r0, r1 in ((f2, 0, 3), (f3, 1, 4)):
    print('---', f.name, f'head rows {r0}-{r1} ---')
    for y in range(r0, r1 + 1):
        print(f'{y:2d} ' + ''.join(CHAR.get(f.get(x, y), '?') for x in range(58)))

finish([f1, f2, f3])
