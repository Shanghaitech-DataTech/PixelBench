from pixelbench_api import new_canvas, finish

W, H = 32, 32
c = new_canvas(W, H, name="escooter_rider")

legend = {
    'H': '#D8432E',   # helmet red
    'h': '#A93226',   # helmet shade / brim
    'S': '#F5C9A0',   # skin
    's': '#D9A87E',   # skin shade
    'E': '#2B2B2B',   # eye
    'B': '#2E6BB0',   # shirt
    'b': '#1D4B80',   # shirt shade
    'P': '#5A5A5A',   # pants
    'K': '#1E1E1E',   # shoes
    'W': '#171717',   # tire
    'w': '#9A9A9A',   # hub
    'M': '#B4B4B4',   # handlebar metal
    'm': '#6E6E6E',   # stem metal dark
    'D': '#4A4A4A',   # deck top
    'd': '#333333',   # deck side
}

# ---- scooter ----
c.circle(7, 24, 3, legend['W'])
c.circle(7, 24, 1, legend['w'])
c.circle(26, 24, 3, legend['W'])
c.circle(26, 24, 1, legend['w'])
c.rect(23, 12, 2, 10, legend['m'])   # stem: x23..24, y12..21
c.rect(20, 11, 7, 1, legend['M'])    # handlebar top
c.rect(20, 12, 7, 1, legend['m'])    # handlebar bottom
c.set(27, 11, legend['m'])
c.set(27, 12, legend['m'])
c.rect(10, 22, 14, 1, legend['D'])   # deck platform
c.rect(10, 23, 14, 1, legend['d'])

# ---- rider (side view, riding right) ----
runs = {
    4:  [(14, 18, 'H')],
    5:  [(14, 18, 'H')],
    6:  [(13, 19, 'H')],
    7:  [(13, 18, 'H'), (19, 19, 'h')],
    8:  [(14, 18, 'S')],
    9:  [(14, 16, 'S'), (17, 17, 'E'), (18, 18, 'S')],
    10: [(14, 17, 'S')],
    11: [(14, 17, 'B'), (18, 19, 'S')],
    12: [(14, 17, 'B'), (18, 19, 'S')],
    13: [(14, 17, 'B')],
    14: [(14, 17, 'B')],
    15: [(14, 16, 'B')],
    16: [(14, 16, 'B')],
    17: [(13, 16, 'P')],
    18: [(13, 16, 'P')],
    19: [(13, 15, 'P'), (17, 18, 'P')],
    20: [(13, 14, 'P'), (18, 19, 'P')],
    21: [(13, 15, 'K'), (20, 21, 'K')],
}

for y, segs in runs.items():
    for x0, x1, ch in segs:
        col = legend[ch]
        for x in range(x0, x1 + 1):
            c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text())
finish(c)
