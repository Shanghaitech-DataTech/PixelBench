from pixelbench_api import input_canvas, new_canvas, finish, view

# ---- palette (same colours as the input drawing) ----
OUTLINE = '#3a3737'   # a
WHITE   = '#efe9e7'   # d
LGREY   = '#b7b3b2'   # b
MGREY   = '#827c7c'   # c
TAN     = '#d6b39d'   # e
DTAN    = '#bc8b6d'   # f
YELLOW  = '#cdae67'   # g  (the input's nose colour)
CM = {'a': OUTLINE, 'b': LGREY, 'c': MGREY, 'd': WHITE,
      'e': TAN, 'f': DTAN, 'g': YELLOW}

W, H = 40, 28


def bar(y, x0, x1, fill='d'):
    """Horizontal band with an outline pixel at each end."""
    return (y, x0, 'a' + fill * (x1 - x0 - 1) + 'a')


SEGS = []

# ---------- EARS (drawn first; the head covers their bases) ----------
# far ear (plain, swept back)
SEGS += [(1, 22, 'ada'), (2, 22, 'adda'), (3, 23, 'adda'), (4, 23, 'adda'),
         (5, 24, 'adda'), (6, 25, 'adda'), (7, 26, 'adda')]
# near ear (tan inner, longer)
SEGS += [(1, 14, 'ada'), (2, 14, 'addda'), (3, 15, 'addda'), (4, 16, 'adeea'),
         (5, 17, 'adeea'), (6, 18, 'adeea'), (7, 19, 'adeea'), (8, 20, 'adeea')]

# ---------- TAIL PUFF (behind the rump) ----------
SEGS += [(11, 9, 'adddd'), (12, 7, 'addda'), (13, 6, 'addda')]

# ---------- HIND LEG (trailing straight back) ----------
SEGS += [(14, 8, 'addda'), (15, 6, 'adddda'), (16, 5, 'adddda'),
         (17, 4, 'addddda'), (18, 3, 'addddda'), (19, 2, 'addddda'),
         (20, 2, 'aaaaaaa')]

# ---------- BODY + HEAD (stretched, muzzle forward-right) ----------
SEGS += [bar(6, 28, 33), bar(7, 26, 34), bar(8, 23, 36), bar(9, 20, 37),
         bar(10, 17, 37), bar(11, 14, 36), bar(12, 11, 35), bar(13, 9, 34),
         bar(14, 8, 33), bar(15, 8, 32), bar(16, 9, 30), bar(17, 11, 28),
         bar(18, 14, 24)]

# ---------- FRONT LEG (reaching forward-down) ----------
SEGS += [(16, 28, 'addda'), (17, 29, 'addda'), (18, 30, 'addda'),
         (19, 31, 'addda'), (20, 31, 'aaaaa')]

# ---------- FACE: eye, amber nose, mouth ----------
SEGS += [(9, 31, 'aa'), (10, 31, 'aa'), (11, 34, 'gg'), (12, 34, 'a')]

# ---------- SHADING ----------
SEGS += [
    # back of the head / neck, running down the back diagonal
    (9, 22, 'bb'), (10, 19, 'bb'), (11, 17, 'bb'), (12, 15, 'bb'),
    (13, 13, 'bb'), (14, 11, 'bb'),
    # jaw, chest and the underside of the muzzle
    (12, 34, 'c'), (13, 33, 'c'), (14, 31, 'cc'), (15, 29, 'cc'),
    # belly, hugging the underside edge
    (16, 25, 'cccc'), (17, 14, 'c' * 11),
    # hind leg underside
    (17, 8, 'cc'), (18, 7, 'cc'), (19, 6, 'cc'),
    # front leg underside
    (17, 32, 'c'), (18, 33, 'c'), (19, 34, 'c'),
    # far ear inner shade
    (2, 23, 'c'), (3, 24, 'c'), (4, 24, 'c'), (5, 25, 'c'), (6, 26, 'c'),
]

# ---------- MOTION: speed lines behind, dust below ----------
SEGS += [(5, 9, 'ccc'), (8, 13, 'ccc'), (11, 4, 'ccc'), (14, 2, 'cc'),
         (21, 4, 'ccc'), (22, 8, 'ccc'), (24, 2, 'cc'), (25, 6, 'cc')]

# ---------- build ----------
f1 = new_canvas(W, H, background=None, name='frame1')
f1.blit(input_canvas, 0, 0)

f2 = new_canvas(W, H, background=None, name='frame2')
for (y, x, s) in SEGS:
    for i, ch in enumerate(s):
        f2.set(x + i, y, CM[ch])


def component_sizes(canvas):
    w, h = canvas.stats()['size']
    seen = [[False] * w for _ in range(h)]
    sizes = []
    for y in range(h):
        for x in range(w):
            if seen[y][x]:
                continue
            seen[y][x] = True
            if canvas.get(x, y) == 0:
                continue
            stack, size = [(x, y)], 0
            while stack:
                cx, cy = stack.pop()
                size += 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx]:
                        seen[ny][nx] = True
                        if canvas.get(nx, ny) != 0:
                            stack.append((nx, ny))
            sizes.append(size)
    return sorted(sizes, reverse=True)


print("FRAME 1:", f1.stats_text())
print("FRAME 2:", f2.stats_text())
print("frame2 components:", component_sizes(f2))
print(f2.matrix_text())

print(view(f1, scale=8))
print(view(f2, scale=8))

finish([f1, f2])
