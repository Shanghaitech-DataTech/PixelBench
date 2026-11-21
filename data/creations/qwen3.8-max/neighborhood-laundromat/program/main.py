# Neighborhood laundromat interior - 64x64 pixel art
# Cool white lighting, two rows of front-loading washers, basket, folding table, wall clock.

C = {
    # architecture
    'CEIL':   '#e8f0f7',
    'CEILD':  '#c2d3e2',
    'FIXT':   '#a9bdce',
    'GLOW':   '#ffffff',
    'WALLL':  '#eaf2f8',
    'WALL':   '#dbe6ef',
    'WALLD':  '#c3d2df',
    'BASE':   '#b0c1d0',
    # floor
    'FLOOR':  '#93a8ba',
    'FLOORD': '#7e93a7',
    'FLOORL': '#a8bccb',
    'SHADOW': '#6b8093',
    # machines
    'OUT':    '#3d5262',
    'OUT2':   '#61798c',
    'MACH':   '#eff4f8',
    'MACHM':  '#d2dde7',
    'MACHD':  '#a5b6c4',
    'PANEL':  '#c2d0dc',
    'DARK':   '#2f4250',
    'GLASS':  '#7ea3bb',
    'GLASSD': '#4d7388',
    'GLASSL': '#c3dcea',
    'ACC1':   '#5cb8cc',
    'ACC2':   '#e2836b',
    # props
    'BASKET':  '#d99a5b',
    'BASKETL': '#e8b47c',
    'BASKETD': '#b0733c',
    'CLOTH1':  '#f7fafc',
    'CLOTH2':  '#f0a7b9',
    'CLOTH3':  '#9fd1e9',
    'CLOTH4':  '#cfe0a5',
    'TABLET':  '#e2e9ee',
    'TABLED':  '#9dabb6',
    'METAL':   '#7b8c99',
}

c = new_canvas(64, 64, name='laundromat')

# ---------------------------------------------------------------- wall / room
c.rect(0, 3, 64, 26, C['WALL'])          # wall rows 3..28
c.rect(0, 3, 64, 2, C['WALLL'])          # brighter near ceiling
c.rect(0, 24, 64, 3, C['WALLD'])         # darker near floor
c.rect(0, 27, 64, 2, C['BASE'])          # baseboard
c.line(0, 26, 63, 26, C['OUT2'])

# ceiling
c.rect(0, 0, 64, 3, C['CEILD'])
for fx in (6, 40):                        # two fluorescent fixtures
    c.rect(fx, 0, 18, 2, C['FIXT'])
    c.rect(fx + 1, 0, 16, 2, C['GLOW'])
    c.rect(fx - 1, 3, 20, 1, C['WALLL'])  # light spill on wall

# ---------------------------------------------------------------- floor
c.rect(0, 29, 64, 35, C['FLOOR'])
# converging tile joints
for y in range(29, 64):
    s = (y - 20) / 9.0
    for k in range(-6, 7):
        x = int(round(32 + k * 7 * s))
        if 0 <= x < 64:
            c.set(x, y, C['FLOORD'])
for y in (31, 34, 38, 43, 49, 56):
    c.line(0, y - 1, 63, y - 1, C['FLOORL'])
    c.line(0, y, 63, y, C['FLOORD'])
# cool light pools on the floor
c.ellipse(15, 33, 13, 3, C['FLOORL'])
c.ellipse(49, 33, 13, 3, C['FLOORL'])
c.ellipse(32, 41, 9, 3, C['FLOORL'])

# ---------------------------------------------------------------- wall decor
# sign plate
c.rect(3, 3, 45, 9, C['WALLL'])
c.rect(3, 3, 45, 9, C['OUT2'], fill=False)
c.text(5, 4, 'LAUNDRY', C['OUT'])

# wall clock
c.circle(54, 7, 4, C['OUT'])
c.circle(54, 7, 3, C['GLOW'])
c.line(54, 7, 54, 5, C['DARK'])
c.line(54, 7, 56, 8, C['DARK'])
c.set(54, 7, C['ACC2'])


# ---------------------------------------------------------------- machines
def washer_back(x):
    """13x17 machine, rows 12..28, standing on the back floor line."""
    y = 12
    c.rect(x, y, 13, 17, C['OUT'])
    c.rect(x + 1, y + 1, 11, 15, C['MACH'])
    c.rect(x + 9, y + 1, 2, 15, C['MACHM'])
    c.rect(x + 11, y + 1, 1, 15, C['MACHD'])
    c.rect(x + 1, y + 1, 10, 1, C['GLOW'])
    # control panel
    c.rect(x + 1, y + 2, 11, 4, C['PANEL'])
    c.rect(x + 1, y + 6, 11, 1, C['OUT2'])
    c.rect(x + 2, y + 3, 4, 2, C['DARK'])
    c.set(x + 3, y + 3, C['ACC1'])
    c.set(x + 4, y + 4, C['ACC1'])
    c.set(x + 8, y + 3, C['ACC2'])
    c.set(x + 10, y + 3, C['ACC1'])
    c.set(x + 8, y + 5, C['OUT2'])
    c.set(x + 10, y + 5, C['OUT2'])
    # round door
    cx, cy = x + 6, y + 10
    c.circle(cx, cy, 4, C['OUT'])
    c.circle(cx, cy, 3, C['OUT2'])
    c.circle(cx, cy, 2, C['GLASS'])
    c.set(cx - 1, cy - 1, C['GLASSL'])
    c.set(cx + 1, cy + 1, C['GLASSD'])
    # plinth
    c.rect(x + 1, y + 15, 11, 1, C['MACHD'])
    # contact shadow
    c.rect(x - 1, y + 17, 15, 1, C['SHADOW'])


def washer_front(x):
    """19x19 machine, rows 45..63, nearest row."""
    y = 45
    c.rect(x, y, 19, 19, C['OUT'])
    c.rect(x + 1, y + 1, 17, 17, C['MACH'])
    c.rect(x + 13, y + 1, 4, 17, C['MACHM'])
    c.rect(x + 16, y + 1, 2, 17, C['MACHD'])
    c.rect(x + 1, y + 1, 15, 1, C['GLOW'])
    # control panel
    c.rect(x + 1, y + 2, 17, 4, C['PANEL'])
    c.rect(x + 1, y + 6, 17, 1, C['OUT2'])
    c.rect(x + 2, y + 3, 8, 2, C['DARK'])
    c.rect(x + 3, y + 3, 6, 1, C['ACC1'])
    c.set(x + 4, y + 4, C['ACC1'])
    c.circle(x + 13, y + 4, 1, C['MACHM'])
    c.set(x + 13, y + 4, C['OUT'])
    c.set(x + 13, y + 3, C['ACC2'])
    c.set(x + 16, y + 3, C['ACC2'])
    c.set(x + 16, y + 5, C['ACC1'])
    # round door
    cx, cy = x + 9, y + 11
    c.circle(cx, cy, 5, C['OUT'])
    c.circle(cx, cy, 4, C['MACHD'])
    c.circle(cx, cy, 3, C['GLASS'])
    c.circle(cx, cy, 2, C['GLASSD'])
    c.set(cx - 2, cy - 2, C['GLASSL'])
    c.set(cx - 1, cy - 2, C['GLASSL'])
    c.set(cx - 2, cy - 1, C['GLASSL'])
    c.set(cx - 1, cy - 1, C['GLASSL'])
    c.set(cx + 1, cy + 1, C['CLOTH2'])
    c.set(cx + 2, cy + 1, C['CLOTH3'])
    c.set(cx, cy + 2, C['CLOTH1'])
    # door handle
    c.rect(x + 15, y + 9, 2, 5, C['OUT2'])
    c.rect(x + 15, y + 10, 1, 3, C['MACHM'])
    # plinth
    c.rect(x + 1, y + 17, 17, 1, C['MACHD'])


for x in (3, 18, 33, 48):
    washer_back(x)
for x in (1, 22, 43):
    washer_front(x)

# ---------------------------------------------------------------- folding table
tx, tw = 3, 26
c.rect(tx + 1, 44, tw - 2, 1, C['SHADOW'])
c.rect(tx + 2, 38, 2, 6, C['METAL'])
c.rect(tx + tw - 4, 38, 2, 6, C['METAL'])
c.rect(tx + 2, 42, tw - 4, 1, C['TABLED'])
c.rect(tx, 36, tw, 2, C['TABLED'])
c.rect(tx, 33, tw, 3, C['TABLET'])
c.rect(tx, 33, tw, 1, C['GLOW'])
c.line(tx, 35, tx + tw - 1, 35, C['MACHM'])
c.rect(tx, 38, tw, 1, C['OUT2'])

# folded clothes on the table
c.rect(5, 30, 8, 3, C['OUT'])
c.rect(6, 30, 6, 2, C['CLOTH1'])
c.rect(6, 31, 6, 1, C['CLOTH2'])
c.rect(14, 29, 9, 4, C['OUT'])
c.rect(15, 29, 7, 3, C['CLOTH3'])
c.rect(15, 31, 7, 1, C['CLOTH1'])
# detergent bottle on the table
c.rect(24, 27, 3, 6, C['OUT'])
c.rect(25, 28, 1, 4, C['ACC1'])
c.rect(24, 30, 3, 2, C['CLOTH1'])

# ---------------------------------------------------------------- floor bottle
c.rect(31, 36, 3, 1, C['OUT'])
c.rect(30, 37, 5, 7, C['OUT'])
c.rect(31, 38, 3, 5, C['CLOTH3'])
c.rect(31, 40, 3, 2, C['CLOTH1'])
c.rect(30, 44, 5, 1, C['SHADOW'])

# ---------------------------------------------------------------- laundry basket
bx = 37
c.rect(bx + 1, 44, 16, 1, C['SHADOW'])
# clothes piled above the rim
c.rect(39, 30, 5, 4, C['OUT'])
c.rect(40, 31, 3, 2, C['CLOTH1'])
c.rect(44, 29, 5, 5, C['OUT'])
c.rect(45, 30, 3, 3, C['CLOTH2'])
c.rect(49, 30, 5, 4, C['OUT'])
c.rect(50, 31, 3, 2, C['CLOTH4'])
# basket silhouette
c.poly([(36, 33), (54, 33), (51, 44), (39, 44)], C['OUT'])
c.rect(37, 34, 16, 1, C['BASKETL'])
c.poly([(37, 35), (53, 35), (51, 43), (39, 43)], C['BASKET'])
# wicker weave
for xx in (40, 43, 46, 49):
    c.line(xx, 35, xx, 43, C['BASKETD'])
for yy in (37, 40, 42):
    lx = 37 + int(round((yy - 35) * 2 / 8.0))
    rx = 53 - int(round((yy - 35) * 2 / 8.0))
    c.line(lx + 1, yy, rx - 1, yy, C['BASKETD'])
# a sock draped over the rim
c.rect(52, 34, 2, 4, C['OUT'])
c.rect(52, 35, 1, 2, C['CLOTH1'])

print(c.stats_text())
view(c)
finish(c)
