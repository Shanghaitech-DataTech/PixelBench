from pixelbench_api import *

W, H = 64, 64
c = new_canvas(W, H, name='title')


def mix(a, b, t):
    t = 0.0 if t < 0 else (1.0 if t > 1 else t)
    return (round(a[0] + (b[0] - a[0]) * t),
            round(a[1] + (b[1] - a[1]) * t),
            round(a[2] + (b[2] - a[2]) * t))


# ---------------------------------------------------------------- sky
SKY = [(0, (10, 6, 24)), (20, (38, 18, 74)), (36, (60, 26, 100)),
       (52, (44, 18, 76)), (63, (24, 10, 42))]


def sky_color(y):
    for i in range(len(SKY) - 1):
        y0, c0 = SKY[i]
        y1, c1 = SKY[i + 1]
        if y <= y1:
            return mix(c0, c1, (y - y0) / (y1 - y0))
    return SKY[-1][1]


BAND = 4
for y0 in range(0, H, BAND):
    c.rect(0, y0, W, min(BAND, H - y0), sky_color(y0 + BAND * 0.5))

# ---------------------------------------------------------------- stars
STARS = [(4, 2, '#8f74d8'), (11, 6, '#ffffff'), (17, 2, '#b7a2f2'),
         (24, 7, '#6d54b0'), (31, 3, '#ffffff'), (38, 8, '#8f74d8'),
         (45, 2, '#cfc0ff'), (52, 6, '#6d54b0'), (59, 3, '#ffffff'),
         (7, 9, '#6d54b0'), (56, 9, '#8f74d8')]
for (x, y, col) in STARS:
    c.set(x, y, col)


def sparkle(cx, cy, col, arm=1, tipcol=None):
    c.set(cx, cy, col)
    for d in range(1, arm + 1):
        cc = tipcol or col
        c.set(cx - d, cy, cc)
        c.set(cx + d, cy, cc)
        c.set(cx, cy - d, cc)
        c.set(cx, cy + d, cc)


sparkle(21, 6, '#ffffff', 2, '#b7a2f2')
sparkle(50, 6, '#ffffff', 1)

# ---------------------------------------------------------------- letters
GLYPHS = {
    'P': ["1110", "1001", "1001", "1110", "1000", "1000", "1000"],
    'I': ["111", ".1.", ".1.", ".1.", ".1.", ".1.", "111"],
    'X': ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    'E': ["1111", "1000", "1000", "1110", "1000", "1000", "1111"],
    'L': ["1000", "1000", "1000", "1000", "1000", "1000", "1111"],
    'Q': ["01110", "10001", "10001", "10001", "10101", "01110", "00011"],
    'U': ["1001", "1001", "1001", "1001", "1001", "1001", "0110"],
    'S': [".111", "1...", "1...", ".11.", "...1", "...1", "111."],
    'T': ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
}

SCALE = 2
GAP = 3
LH = 7 * SCALE

ROW_TONE = [
    '#fff6c9', '#fff6c9',
    '#ffe583', '#ffe583',
    '#ffcf3d', '#ffcf3d', '#ffcf3d',
    '#f2ad1c', '#f2ad1c', '#f2ad1c',
    '#d99314', '#d99314',
    '#b96c0f', '#b96c0f',
]
OUTLINE = '#2b1145'
SHADOW = '#0e0618'


def word_grid(word):
    widths = [len(GLYPHS[ch][0]) for ch in word]
    total = sum(w * SCALE for w in widths) + GAP * (len(word) - 1)
    grid = [[False] * total for _ in range(LH)]
    x = 0
    for ch, w in zip(word, widths):
        g = GLYPHS[ch]
        for ry in range(7):
            for rx in range(w):
                if g[ry][rx] == '1':
                    for sy in range(SCALE):
                        for sx in range(SCALE):
                            grid[ry * SCALE + sy][x + rx * SCALE + sx] = True
        x += w * SCALE + GAP
    return grid, total


def draw_word(word, top_y):
    grid, w = word_grid(word)
    x0 = (W - w) // 2 - 1
    shape = {(x, y) for y in range(LH) for x in range(w) if grid[y][x]}
    dil = set()
    for (x, y) in shape:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                dil.add((x + dx, y + dy))

    # holes fully enclosed by the outline
    lo_x, hi_x, lo_y, hi_y = -2, w + 1, -2, LH + 1
    outside = set()
    stack = [(lo_x, lo_y)]
    while stack:
        p = stack.pop()
        if p in outside or p in dil:
            continue
        outside.add(p)
        px, py = p
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (px + dx, py + dy)
            if lo_x <= q[0] <= hi_x and lo_y <= q[1] <= hi_y and q not in outside:
                stack.append(q)
    counter = [(x, y) for y in range(lo_y, hi_y + 1) for x in range(lo_x, hi_x + 1)
               if (x, y) not in outside and (x, y) not in dil]

    ring = set()
    for (x, y) in dil:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                p = (x + dx, y + dy)
                if p not in dil:
                    ring.add(p)
    for (x, y) in ring:
        if (x - 1, y) in dil or (x, y - 1) in dil or (x - 1, y - 1) in dil:
            c.set(x0 + x, top_y + y, SHADOW)
    for (x, y) in dil:
        c.set(x0 + x, top_y + y, OUTLINE)
    for (x, y) in shape:
        c.set(x0 + x, top_y + y, ROW_TONE[y])
    for (x, y) in counter:
        c.set(x0 + x, top_y + y, SHADOW)
    return x0, w


draw_word('PIXEL', 12)
draw_word('QUEST', 32)

# ---------------------------------------------------------------- tagline
TAG = 'START'
tx = (W - (len(TAG) * 6 - 1)) // 2
c.text(tx, 53, TAG, '#efe0ff', font='5x7')

for x in range(5, 13):
    c.set(x, 56, '#6f52b0')
for x in range(51, 59):
    c.set(x, 56, '#6f52b0')
c.set(13, 55, '#e0a020')
c.set(13, 57, '#e0a020')
c.set(50, 55, '#e0a020')
c.set(50, 57, '#e0a020')

# small sparkle between the two title lines and the tagline
c.set(29, 50, '#d99314')
c.set(33, 50, '#d99314')
c.set(31, 49, '#ffe583')
c.set(31, 51, '#ffe583')
c.set(30, 50, '#ffcf3d')
c.set(32, 50, '#ffcf3d')
c.set(31, 50, '#fff6c9')

c.set(3, 61, '#8f74d8')
c.set(60, 61, '#8f74d8')


# ---------------------------------------------------------------- debug
def debug_map():
    def hexof(v):
        if isinstance(v, str):
            return v[:7]
        return '#%02x%02x%02x' % (v[0], v[1], v[2])
    pal = {p['index']: hexof(p['rgba']) for p in c.palette()}
    gold = set(ROW_TONE)
    sky = set()
    for y0 in range(0, H, BAND):
        r, g, b = sky_color(y0 + BAND * 0.5)
        sky.add('#%02x%02x%02x' % (r, g, b))
    tagline = {'#efe0ff', '#6f52b0', '#b49cff', '#e0a020'}
    stars = {'#ffffff', '#b7a2f2', '#cfc0ff', '#8f74d8', '#6d54b0'}
    out = []
    for y in range(H):
        line = []
        for x in range(W):
            h = pal[c.get(x, y)]
            if h in gold:
                line.append('#')
            elif h == OUTLINE:
                line.append('O')
            elif h == SHADOW:
                line.append('s')
            elif h in sky:
                line.append('.')
            elif h in tagline:
                line.append('t')
            elif h in stars:
                line.append('*')
            else:
                line.append('?')
        out.append('%02d %s' % (y, ''.join(line)))
    return '\n'.join(out)


print(c.stats_text())
print(debug_map())
save('title', c)
finish(c)
