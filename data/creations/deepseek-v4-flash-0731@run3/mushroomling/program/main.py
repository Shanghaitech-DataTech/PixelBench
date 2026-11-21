from pixelbench_api import new_canvas, finish

W = H = 16

def build(segments):
    """segments: list of (x0, x1, ch), inclusive. Returns a 16-char row."""
    arr = ['.'] * 16
    for x0, x1, ch in segments:
        for x in range(x0, x1 + 1):
            arr[x] = ch
    return ''.join(arr)

rows = [
    build([]),                                                    # 0
    build([(7, 8, 'a')]),                                         # 1  cap top
    build([(6, 9, 'r')]),                                         # 2
    build([(5, 10, 'r')]),                                        # 3
    build([(4, 11, 'r')]),                                        # 4
    build([(3, 12, 'r'), (5, 6, 'w'), (9, 10, 'w')]),             # 5  spots
    build([(3, 12, 'r'), (4, 4, 'w'), (11, 11, 'w')]),            # 6  spots
    build([(2, 13, 'r')]),                                        # 7
    build([(1, 14, 'a')]),                                        # 8  cap rim
    build([(2, 13, 'a'), (3, 12, 'd')]),                          # 9  face top
    build([(2, 13, 'a'), (3, 12, 'd'), (4, 5, 'w'), (10, 11, 'w')]),          # 10 eyes
    build([(2, 13, 'a'), (3, 12, 'd'), (4, 5, 'w'), (10, 11, 'w'),
           (5, 5, 'a'), (10, 10, 'a')]),                          # 11 eyes + pupils
    build([(1, 2, 'a'), (2, 13, 'a'), (3, 12, 'd'), (7, 8, 'a'), (13, 14, 'a')]),  # 12 mouth + arms
    build([(1, 2, 'a'), (2, 13, 'a'), (3, 12, 'd'), (13, 14, 'a')]),             # 13 arms
    build([(3, 5, 'a'), (10, 12, 'a')]),                          # 14 feet
    build([]),                                                    # 15
]

for y, row in enumerate(rows):
    if len(row) != W:
        raise SystemExit(f"row {y} length {len(row)}: {row!r}")

c = new_canvas(W, H, name="mushroomling")
palette = {
    "a": "#3a2a1f",   # dark brown outline / pupils / mouth / arms / feet
    "r": "#d63030",   # red cap
    "w": "#f4f2e8",   # white: cap spots + eye whites
    "d": "#f0d8a8",   # cream flesh
}
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, palette[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
