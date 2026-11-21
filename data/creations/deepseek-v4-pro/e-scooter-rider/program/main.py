W = 32
H = 32

c = new_canvas(W, H, name="result")

# Register colours
pal = {
    '.': None,
    'R': c.color("#e63946", "helmet"),
    'V': c.color("#e0e1dd", "visor"),
    'S': c.color("#f4a261", "skin"),
    'J': c.color("#457b9d", "jacket"),
    'P': c.color("#1d3557", "pants"),
    'E': c.color("#2b2d42", "shoes"),
    'D': c.color("#22223b", "deck"),
    'F': c.color("#6c757d", "frame"),
    'W': c.color("#111111", "wheel"),
    'H': c.color("#adb5bd", "hub"),
    'G': c.color("#333333", "handlebar"),
    'K': c.color("#151515", "outline"),
    'L': c.color("#ffffff", "highlight"),
    'M': c.color((30, 30, 40, 80), "shadow"),
}

# Each row: list of (char, x0, x1) inclusive; default is transparent.
# Later segments in a row overwrite earlier ones.
rows = [
    [],  # 0
    [],  # 1
    [],  # 2
    [('R', 14, 14)],  # 3 helmet top
    [('R', 13, 15), ('L', 13, 13)],  # 4 highlight
    [('R', 12, 16), ('V', 15, 16)],  # 5 visor
    [('R', 11, 17), ('V', 15, 17)],  # 6 visor
    [('R', 11, 17), ('V', 15, 16)],  # 7 visor
    [('R', 13, 15)],  # 8
    [('R', 14, 14), ('S', 13, 13)],  # 9 head bottom + neck
    [('J', 12, 16)],  # 10 shoulders
    [('J', 12, 16)],  # 11 torso
    [('J', 12, 16)],  # 12 torso
    [('J', 11, 15)],  # 13
    [('J', 11, 15)],  # 14
    [('J', 11, 14)],  # 15
    [('P', 10, 14)],  # 16 hip
    [('P', 10, 11), ('P', 14, 15)],  # 17 knees
    [('P', 10, 11), ('P', 15, 16)],  # 18 ankles
    [('E', 10, 13), ('E', 15, 18)],  # 19 shoes
    [('F', 8, 24)],  # 20 deck top
    [('D', 8, 24)],  # 21 deck
    [('D', 8, 24), ('W', 9, 9), ('W', 24, 24)],  # 22
    [('W', 8, 10), ('W', 23, 25)],  # 23
    [('W', 7, 11), ('W', 22, 26), ('H', 8, 10), ('H', 23, 25)],  # 24
    [('W', 7, 11), ('W', 22, 26), ('H', 8, 10), ('H', 23, 25)],  # 25
    [('W', 7, 11), ('W', 22, 26), ('H', 8, 10), ('H', 23, 25)],  # 26
    [('W', 8, 10), ('W', 23, 25)],  # 27
    [('W', 9, 9), ('W', 24, 24)],  # 28
    [('M', 6, 12), ('M', 21, 27)],  # 29 ground shadow
    [],  # 30
    [],  # 31
]

# Steering column (stem): draw first so the handlebar can sit over it.
for y in range(11, 21):
    rows[y].append(('F', 23, 24))

# Handlebar: horizontal bar over the stem, hand wrapping the rider's end.
for y in (11, 12):
    rows[y].append(('G', 17, 25))   # bar from hand to front
    rows[y].append(('S', 16, 17))   # hand on the left end of the bar

for y, segs in enumerate(rows):
    line = ['.'] * W
    for ch, x0, x1 in segs:
        for x in range(x0, x1 + 1):
            if 0 <= x < W:
                line[x] = ch
    s = ''.join(line)
    assert len(s) == W, (y, len(s), s)
    for x, ch in enumerate(s):
        if ch != '.':
            c.set(x, y, pal[ch])

print(c.stats_text())
print(c.matrix_text(region=(0, 0, W - 1, H - 1)))

finish(c)
