from pixelbench_api import new_canvas, finish

PAL = {
    'o': '#1a1620',   # outline
    's': '#ffd3a8',   # skin
    'e': '#241a12',   # eye
    'm': '#c04a4a',   # mouth
    'h': '#8a4a26',   # hair
    'r': '#d92b33',   # top red
    'k': '#c81e28',   # skirt red
    'w': '#f7f3ee',   # white
    'a': '#e84a50',   # pom accent
    'b': '#26222a',   # shoes
    'y': '#f2d03a',   # bow
}

POM = [
    'ooooo..',
    'owawwo.',
    'owwawo.',
    'owawwo.',
    'owwao..',
    '.oooo..',
    '..oo...',
]


def lines(rows):
    grid = []
    for L, content in rows:
        line = ['d'] * 32
        for i, ch in enumerate(content):
            if 0 <= L + i < 32:
                line[L + i] = ch
        grid.append(line)
    return grid


def place(c, grid, x0, y0):
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch != 'd':
                c.set(x0 + x, y0 + y, PAL[ch])


def pom(c, x0, y0, px, py):
    for y, line in enumerate(POM):
        for x, ch in enumerate(line):
            if ch not in 'd.':
                c.set(x0 + px + x, y0 + py + y, PAL[ch])


FRONT = lines([
    (4, 'o' * 24),
    (4, 'o' + 'h' * 22 + 'o'),
    (4, 'o' + 'h' * 22 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 14 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 14 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 14 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 2 + 'e' * 2 + 's' * 6 + 'e' * 2 + 's' * 2 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 2 + 'e' * 2 + 's' * 6 + 'e' * 2 + 's' * 2 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 14 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 5 + 'm' * 2 + 's' * 7 + 'h' * 3 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 14 + 'h' * 3 + 'o'),
    (10, 'o' + 'h' * 1 + 's' * 8 + 'h' * 1 + 'o'),
    (7, 'o' + 'h' * 3 + 's' * 2 + 'r' * 8 + 's' * 2 + 'h' * 3 + 'o'),
    (7, 'o' + 'h' * 3 + 's' * 2 + 'r' * 8 + 's' * 2 + 'h' * 3 + 'o'),
    (8, 'o' + 's' * 4 + 'r' * 12 + 's' * 4 + 'o'),
    (8, 'o' + 's' * 4 + 'r' * 12 + 's' * 4 + 'o'),
    (9, 'o' + 's' * 4 + 'r' * 10 + 's' * 4 + 'o'),
    (9, 'o' + 's' * 4 + 'r' * 10 + 's' * 4 + 'o'),
    (9, 'o' + 's' * 4 + 'r' * 10 + 's' * 4 + 'o'),
    (8, 'o' + 'k' * 16 + 'o'),
    (7, 'o' + 'k' * 18 + 'o'),
    (6, 'o' * 0 + 'k' * 22 + 'o'),  # placeholder replaced below
])

BACK = lines([
    (4, 'o' * 24),
    (4, 'o' + 'h' * 22 + 'o'),
    (4, 'o' + 'h' * 22 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 9 + 'y' * 2 + 'h' * 9 + 'o'),
    (5, 'o' + 'h' * 8 + 'y' * 4 + 'h' * 8 + 'o'),
    (5, 'o' + 'h' * 9 + 'y' * 2 + 'h' * 9 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (7, 'o' + 'h' * 14 + 'o'),
    (7, 'o' + 'h' * 3 + 'r' * 12 + 'h' * 3 + 'o'),
    (7, 'o' + 'h' * 2 + 'r' * 14 + 'h' * 2 + 'o'),
    (8, 'o' + 'r' * 16 + 'o'),
    (8, 'o' + 'r' * 16 + 'o'),
    (8, 'o' + 'r' * 16 + 'o'),
    (9, 'o' + 'r' * 14 + 'o'),
    (8, 'o' + 'k' * 16 + 'o'),
    (7, 'o' + 'k' * 18 + 'o'),
    (6, 'o' + 'k' * 20 + 'o'),
    (5, 'o' + 'k' * 22 + 'o'),
    (5, 'o' + 'k' * 22 + 'o'),
    (6, 'o' + 'k' * 20 + 'o'),
    (10, 'o' + 's' * 4 + 'o' + 's' * 4 + 'o'),
    (10, 'o' + 's' * 4 + 'o' + 's' * 4 + 'o'),
    (10, 'o' + 's' * 4 + 'o' + 's' * 4 + 'o'),
    (10, 'o' + 'w' * 4 + 'o' + 'w' * 4 + 'o'),
    (9, 'o' + 'b' * 5 + 'o' + 'b' * 5 + 'o'),
    (8, 'o' + 'b' * 7 + 'o' + 'b' * 6 + 'o'),
])

FRONT2 = lines([
    (6, 'o' + 'k' * 20 + 'o'),
    (6, 'o' + 'k' * 20 + 'o'),
    (6, 'o' + 'k' * 20 + 'o'),
    (10, 'o' + 's' * 4 + 'o' + 's' * 4 + 'o'),
    (10, 'o' + 's' * 4 + 'o' + 's' * 4 + 'o'),
    (10, 'o' + 's' * 4 + 'o' + 's' * 4 + 'o'),
    (10, 'o' + 'w' * 4 + 'o' + 'w' * 4 + 'o'),
    (9, 'o' + 'b' * 5 + 'o' + 'b' * 5 + 'o'),
    (8, 'o' + 'b' * 7 + 'o' + 'b' * 6 + 'o'),
])

LEFT = lines([
    (6, 'o' * 20),
    (6, 'o' + 'h' * 18 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 20 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 8 + 'h' * 9 + 'o'),
    (5, 'o' + 'h' * 2 + 's' * 4 + 'e' * 1 + 's' * 3 + 'h' * 10 + 'o'),
    (5, 'o' + 'h' * 2 + 's' * 7 + 'h' * 11 + 'o'),
    (5, 'o' + 'h' * 2 + 's' * 6 + 'm' * 1 + 's' * 2 + 'h' * 9 + 'o'),
    (5, 'o' + 'h' * 3 + 's' * 7 + 'h' * 10 + 'o'),
    (5, 'o' + 'h' * 4 + 's' * 5 + 'h' * 9 + 'o'),
    (7, 'o' + 'h' * 2 + 's' * 3 + 'h' * 5 + 'o'),
    (7, 'o' + 'h' * 2 + 's' * 1 + 'r' * 4 + 'h' * 5 + 'o'),
    (7, 'o' + 's' * 3 + 'r' * 5 + 'h' * 3 + 'o'),
    (7, 'o' + 's' * 3 + 'r' * 5 + 'h' * 3 + 'o'),
    (8, 'o' + 's' * 3 + 'r' * 4 + 'h' * 2 + 'o'),
    (8, 'o' + 's' * 3 + 'r' * 4 + 'h' * 2 + 'o'),
    (8, 'o' + 's' * 3 + 'r' * 4 + 'h' * 2 + 'o'),
    (8, 'o' + 'k' * 7 + 'h' * 2 + 'o'),
    (7, 'o' + 'k' * 9 + 'h' * 2 + 'o'),
    (6, 'o' + 'k' * 11 + 'o'),
    (6, 'o' + 'k' * 11 + 'o'),
    (5, 'o' + 'k' * 13 + 'o'),
    (5, 'o' + 'k' * 13 + 'o'),
    (6, 'o' + 'k' * 11 + 'o'),
    (8, 'o' + 's' * 4 + 'o' + 's' * 3 + 'o'),
    (8, 'o' + 's' * 4 + 'o' + 's' * 3 + 'o'),
    (8, 'o' + 's' * 4 + 'o' + 's' * 3 + 'o'),
    (8, 'o' + 'w' * 4 + 'o' + 'w' * 3 + 'o'),
    (7, 'o' + 'b' * 5 + 'o' + 'b' * 4 + 'o'),
    (6, 'o' + 'b' * 7 + 'o' + 'b' * 5 + 'o'),
])

# extend the front skirt/legs rows (continue FRONT to the bottom)
FRONT = FRONT + FRONT2

c = new_canvas(64, 64)
place(c, FRONT, 0, 0)
place(c, BACK, 32, 0)
place(c, LEFT, 0, 32)
pom(c, 0, 0, 3, 17)
pom(c, 0, 0, 22, 17)
pom(c, 32, 0, 3, 17)
pom(c, 32, 0, 22, 17)

lv = new_canvas(32, 32)
place(lv, LEFT, 0, 0)
pom(lv, 0, 0, 3, 17)
lv.mirror('h')
c.blit(lv, 32, 32)

print(c.stats_text())
print("=== FRONT ===")
print(c.matrix_text(region=(0, 0, 31, 31)))
print("=== BACK ===")
print(c.matrix_text(region=(32, 0, 63, 31)))
print("=== RIGHT ===")
print(c.matrix_text(region=(32, 32, 63, 63)))

finish(c)
