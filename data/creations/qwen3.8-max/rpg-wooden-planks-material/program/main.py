import random

# ---------------------------------------------------------------- palette ---
GROOVE    = '#241508'   # bottom of the seam groove
GROOVE_HI = '#3b2412'   # groove wall catching a little light

# board tones: light / light-dark / dark / dark-dark
TONES = {
    'L':  dict(edge='#8a5730', mid='#c08a52', rise='#d8a469', grain='#a06a39'),
    'LD': dict(edge='#79492a', mid='#a97343', rise='#bf8a51', grain='#8c5829'),
    'D':  dict(edge='#75451f', mid='#a2693a', rise='#b87f49', grain='#875329'),
    'DD': dict(edge='#63361a', mid='#8b5730', rise='#9e6739', grain='#75451f'),
}

SEAM_D  = '#43260f'     # butt-joint shadow line
END_LT  = '#e2b67e'     # light cut board end (end grain)
END_HI  = '#f0cd9c'     # fresh-cut highlight
END_MD  = '#a9743f'     # shaded part of a light end
END_DK  = '#6b3f21'     # dark cut board end
END_DK2 = '#54301a'     # shaded part of a dark end

KNOT_RING = '#7e4c26'
KNOT_MID  = '#4d2a13'
KNOT_CORE = '#2e1708'

# ------------------------------------------------------- board definitions ---
# grooves at x = 0, 5, 11  ->  boards 1-4 (4px), 6-10 (5px), 12-15 (4px)
# one butt joint per board; the plank wraps the tile, so one tone per board
BOARDS = [
    dict(x0=1,  w=4, joint=6,  tone='L',  end='light', knot=(1, 10)),
    dict(x0=6,  w=5, joint=12, tone='DD', end='dark',  knot=(7, 4)),
    dict(x0=12, w=4, joint=3,  tone='LD', end='light', knot=(12, 8)),
]

c = new_canvas(16, 16, name='wooden_planks')
rnd = random.Random(7)


def col_tones(w, t):
    """Column shading across a board: lit edge -> body -> shaded edge."""
    if w == 4:
        return [t['rise'], t['mid'], t['mid'], t['edge']]
    return [t['rise'], t['mid'], t['mid'], t['grain'], t['edge']]


# ------------------------------------------------------------- board bodies ---
for b in BOARDS:
    x0, w, j = b['x0'], b['w'], b['joint']
    t = TONES[b['tone']]
    cols = col_tones(w, t)
    for y in range(16):
        for dx in range(w):
            c.set(x0 + dx, y, cols[dx])

    # natural grain: long flowing vertical streaks, broken around the joint
    gcols = [1, w - 2]
    for dx in gcols:
        y = 0
        while y < 16:
            if y in (j - 1, j, j + 1):
                y += 1
                continue
            ln = rnd.choice([3, 4, 5, 6])
            gcol = t['grain'] if rnd.random() < 0.7 else t['edge']
            for k in range(ln):
                yy = y + k
                if 0 <= yy < 16 and yy not in (j - 1, j, j + 1):
                    c.set(x0 + dx, yy, gcol)
            y += ln + rnd.choice([1, 2])
    # a couple of short grain dashes elsewhere on the board
    others = [d for d in range(1, w - 1) if d not in gcols]
    for _ in range(2):
        dx = rnd.choice(others or gcols)
        yy = rnd.randrange(16)
        for k in range(rnd.choice([1, 2])):
            if yy + k not in (j - 1, j, j + 1) and yy + k < 16:
                c.set(x0 + dx, yy + k, t['grain'])
    # a few brighter fibres on the lit edge
    for _ in range(2):
        yy = rnd.randrange(16)
        if yy not in (j - 1, j, j + 1):
            c.set(x0, yy, t['rise'])

    # ---- butt joint: cut end grain above, seam line, shadowed wood below ---
    if b['end'] == 'light':
        band = [END_LT, END_HI, END_LT, END_MD, END_MD][:w]
    else:
        band = [END_DK, END_MD, END_DK, END_DK, END_DK2][:w]
    band[w - 1] = SEAM_D if b['end'] == 'light' else END_DK2
    for dx in range(w):
        c.set(x0 + dx, j - 1, band[dx])
        c.set(x0 + dx, j, SEAM_D)
        c.set(x0 + dx, j + 1, t['edge'])
    c.set(x0 + 1, j + 1, t['grain'])

# ------------------------------------------------------------------- knots ---
def knot(cx, cy, j):
    R, M, C = KNOT_RING, KNOT_MID, KNOT_CORE
    free = lambda y: y not in (j - 1, j, j + 1) and 0 <= y < 16
    c.set(cx + 1, cy, R); c.set(cx + 2, cy, R)
    c.set(cx, cy + 1, R); c.set(cx + 1, cy + 1, M)
    c.set(cx + 2, cy + 1, M); c.set(cx + 3, cy + 1, R)
    c.set(cx, cy + 2, R); c.set(cx + 1, cy + 2, M)
    c.set(cx + 2, cy + 2, C); c.set(cx + 3, cy + 2, R)
    c.set(cx + 1, cy + 3, R); c.set(cx + 2, cy + 3, R)
    # grain bending around the knot
    if free(cy - 1):
        c.set(cx + 1, cy - 1, R)
    if free(cy + 4):
        c.set(cx + 2, cy + 4, R)

for b in BOARDS:
    if b['knot']:
        knot(b['knot'][0], b['knot'][1], b['joint'])

# a small elongated knot on the middle board's lower segment
c.set(7, 14, KNOT_MID); c.set(8, 14, KNOT_MID)
c.set(7, 13, KNOT_RING); c.set(8, 13, KNOT_RING)
c.set(7, 15, KNOT_RING); c.set(8, 15, KNOT_RING)

# ------------------------------------------------------------------ grooves ---
for gx in (0, 5, 11):
    for y in range(16):
        c.set(gx, y, GROOVE)
    for y in (1, 4, 8, 9, 13):
        c.set(gx, (y + gx * 2) % 16, GROOVE_HI)

view(c)
print(c.stats_text())

# seamless-tiling check: 2x2 repeat
tile = new_canvas(32, 32, name='tilecheck')
for ox in (0, 16):
    for oy in (0, 16):
        tile.blit(c, ox, oy)
view(tile, margin=0)

save('wooden_planks', c, indexed=True)
finish(c)
