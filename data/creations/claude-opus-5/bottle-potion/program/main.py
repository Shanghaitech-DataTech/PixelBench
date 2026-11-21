out = input_canvas.copy(name="output")

# the source art is drawn in 2x2 pixel blocks (effectively a 32x32 grid)
LENS  = out.color('#5a1f8c', 'potion_lens')   # dark liquid surface seen through the tilted mouth
BODY  = out.color('#8b35c4', 'potion_body')   # liquid body
DEEP  = out.color('#66209a', 'potion_deep')   # shading at the bottom of the body
GLASS = out.color('#b06ce0', 'potion_glass')  # glass / surface highlights
LINE  = out.color('#2a0a3f', 'potion_line')   # dark waterline
B1    = out.color('#b36ce0', 'bub_lens')
B1H   = out.color('#e6c4fa', 'bub_lens_hi')
B2    = out.color('#cf93f2', 'bub_body')
B2H   = out.color('#f6ecff', 'bub_body_hi')
SPARK = out.color('#c98cee', 'spark')
WHITE_IDX = out.color('#ffffff')


def blk(bx, by, col):
    out.rect(bx * 2, by * 2, 2, 2, col)


# ---- 1. recolour the water to purple -----------------------------------
mapping = {'c4': LENS, 'c5': BODY, 'c6': GLASS, 'c7': GLASS, 'c9': GLASS,
           'c8': LINE}
for y in range(64):
    for x in range(64):
        name = out.color_name(out.get(x, y))
        if name in mapping:
            out.set(x, y, mapping[name])

# deeper tone towards the bottom of the flask
for by in range(27, 31):
    for y in (by * 2, by * 2 + 1):
        for x in range(64):
            if out.get(x, y) == BODY:
                out.set(x, y, DEEP)


# ---- 2. bubbles --------------------------------------------------------
def bubble(bx, by, size, fill, hi):
    if size == 1:
        blk(bx, by, fill)
    elif size == 2:
        for dx in (0, 1):
            for dy in (0, 1):
                blk(bx + dx, by + dy, fill)
        blk(bx, by, hi)
    else:
        for dx, dy in ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)):
            blk(bx + dx, by + dy, fill)
        blk(bx + 1, by + 1, hi)


# in the dark surface lens (block rows 14-20)
for bx, by, s in ((7, 19, 1), (10, 17, 2), (14, 15, 3), (18, 17, 2),
                  (21, 19, 1), (12, 20, 1), (16, 19, 1), (20, 14, 2),
                  (5, 16, 1), (23, 16, 1), (9, 14, 1)):
    bubble(bx, by, s, B1, B1H)

# in the liquid body (block rows 22-30)
for bx, by, s in ((8, 25, 2), (12, 23, 1), (14, 27, 2), (18, 24, 1),
                  (20, 26, 2), (10, 28, 1), (16, 22, 1), (22, 23, 1),
                  (13, 30, 1), (6, 23, 1), (19, 29, 1), (11, 26, 1)):
    bubble(bx, by, s, B2, B2H)


# ---- 3. a few sparkles in the air, only where the canvas is still white -
def sparkle(bx, by):
    cells = ((bx, by), (bx - 1, by), (bx + 1, by), (bx, by - 1), (bx, by + 1))
    for cx, cy in cells:
        if not (0 <= cx < 32 and 0 <= cy < 32):
            return
        for y in (cy * 2, cy * 2 + 1):
            for x in (cx * 2, cx * 2 + 1):
                if out.get(x, y) != WHITE_IDX:
                    return
    blk(bx, by, SPARK)
    for cx, cy in cells[1:]:
        out.set(cx * 2 + 1 if cx < bx else cx * 2, cy * 2 + 1 if cy < by else cy * 2, SPARK)


for bx, by in ((27, 18), (29, 24), (4, 20), (3, 30), (25, 29), (8, 11)):
    sparkle(bx, by)

view(out)
print(out.stats_text())
finish(out)
