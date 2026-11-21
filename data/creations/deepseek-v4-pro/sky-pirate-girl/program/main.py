from pixelbench_api import *

W = 64
H = 64
grid = [['.' for _ in range(W)] for _ in range(H)]

# ---------- grid helpers ----------
def px(x, y, ch):
    if 0 <= x < W and 0 <= y < H:
        grid[y][x] = ch

def rect(x0, y0, x1, y1, ch):
    for y in range(max(0, y0), min(H, y1 + 1)):
        for x in range(max(0, x0), min(W, x1 + 1)):
            grid[y][x] = ch

def ellipse(cx, cy, rx, ry, ch):
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            dx = (x - cx) / rx if rx else 0
            dy = (y - cy) / ry if ry else 0
            if dx * dx + dy * dy <= 1.0:
                px(x, y, ch)

def circle(cx, cy, r, ch):
    ellipse(cx, cy, r, r, ch)

def line(x0, y0, x1, y1, ch):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    dx = abs(x1 - x0); dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        px(x0, y0, ch)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy; x0 += sx
        if e2 < dx:
            err += dx; y0 += sy

def poly(pts, ch):
    if len(pts) < 3:
        return
    minx = min(p[0] for p in pts)
    maxx = max(p[0] for p in pts)
    miny = min(p[1] for p in pts)
    maxy = max(p[1] for p in pts)
    for y in range(max(0, miny), min(H, maxy + 1)):
        for x in range(max(0, minx), min(W, maxx + 1)):
            inside = False
            j = len(pts) - 1
            for i in range(len(pts)):
                xi, yi = pts[i]
                xj, yj = pts[j]
                if (yi > y) != (yj > y):
                    xint = xi + (y - yi) * (xj - xi) / (yj - yi)
                    if x < xint:
                        inside = not inside
                j = i
            if inside:
                grid[y][x] = ch

def poly_stroke(pts, ch):
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        line(x0, y0, x1, y1, ch)

# ---------- painting ----------
# 1. hair back mass + wind-swept extension
ellipse(31, 20, 16, 18, 'H')
wind = [(33, 3), (46, 3), (53, 7), (52, 12), (55, 16), (50, 21), (44, 25), (38, 19), (35, 13)]
poly(wind, 'H')
# strand separation lines inside the wind mass
line(42, 12, 50, 9, 'h')
line(44, 17, 51, 16, 'h')
line(45, 22, 50, 21, 'h')
# soft highlight on top-left hair
line(19, 5, 26, 5, 'L')
line(18, 7, 24, 7, 'L')

# 2. neck
rect(26, 31, 33, 40, 'S')

# 3. coat
coat = [(12, 50), (20, 41), (27, 37), (33, 37), (40, 41), (51, 50), (53, 64), (11, 64)]
poly(coat, 'N')

# 4. face (three-quarter, facing viewer's left)
face = [(23, 11), (36, 11), (39, 18), (37, 26), (30, 34), (21, 27), (20, 17)]
poly(face, 'S')
poly_stroke(face, 'k')

# 5. scarf (red, wind-blown tail to the right)
poly([(23, 36), (44, 32), (49, 35), (46, 40), (24, 40)], 'R')  # tail (longer)
poly([(21, 34), (36, 34), (39, 39), (21, 39)], 'R')             # wrap
circle(22, 37, 2, 'R')                                          # knot
px(22, 37, 'w')
line(26, 35, 26, 38, 'r')
line(31, 35, 31, 38, 'r')
line(35, 35, 35, 38, 'r')
line(22, 34, 35, 34, 'w')
line(25, 36, 43, 33, 'w')                                       # tail top light

# 6. fringe over forehead
fringe = [(19, 7), (40, 7), (40, 11), (36, 10), (33, 13), (30, 11), (27, 13), (24, 11), (21, 13), (19, 10)]
poly(fringe, 'H')
line(21, 13, 24, 11, 'h')
line(24, 11, 27, 13, 'h')
line(27, 13, 30, 11, 'h')
line(30, 11, 33, 13, 'h')
line(33, 13, 36, 10, 'h')
line(36, 10, 40, 11, 'h')

# 7. goggles on hair
rect(21, 6, 40, 6, 'k')     # thin strap
circle(26, 8, 2, 'G')       # left lens frame
circle(26, 8, 1, 'g')       # left glass
circle(33, 8, 2, 'G')       # right lens frame
circle(33, 8, 1, 'g')       # right glass
px(25, 7, 'B')
px(32, 7, 'B')

# 8. facial features
# brows
line(21, 16, 27, 15, 'h')
line(30, 16, 33, 15, 'h')

# near (left, larger) eye
ellipse(24, 20, 3, 3, 'k')
ellipse(24, 20, 2, 2, 'B')
ellipse(24, 21, 2, 1, 'E')
circle(24, 21, 1, 'e')
px(23, 19, 'B')

# far (right, smaller) eye
ellipse(31, 20, 2, 3, 'k')
ellipse(31, 20, 1, 2, 'B')
circle(31, 21, 1, 'E')
px(30, 19, 'B')

# nose, mouth, blush
px(22, 25, 's')
px(23, 26, 's')
line(26, 29, 28, 28, 'M')
px(29, 28, 'M')
px(21, 26, 'b')
px(22, 27, 'b')

# 9. coat details
line(26, 40, 22, 48, 'n')
line(34, 40, 38, 48, 'n')
rect(23, 40, 37, 40, 'n')
px(30, 46, 'G')
px(30, 51, 'G')
px(30, 56, 'G')
line(15, 47, 19, 43, 'c')
line(47, 47, 43, 43, 'c')

# 10. final outer silhouette outline
def silhouette_outline():
    newg = [row[:] for row in grid]
    for y in range(H):
        for x in range(W):
            ch = grid[y][x]
            if ch == '.':
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] == '.':
                    newg[y][x] = 'k'
                    break
    return newg

grid = silhouette_outline()

# ---------- render ----------
pal = {
    '.': None,
    'k': '#33201c',
    'S': '#f6cfae',
    's': '#dda374',
    'H': '#8c5a3c',
    'h': '#6b3f28',
    'L': '#b5834f',
    'G': '#c9973f',
    'g': '#6fc7dd',
    'B': '#ffffff',
    'E': '#3f9b6b',
    'e': '#1f5a44',
    'R': '#c9402f',
    'r': '#8f2a1f',
    'w': '#e25b4a',
    'N': '#2f3d63',
    'n': '#20294a',
    'c': '#46598c',
    'M': '#a04a42',
    'b': '#e8a0a0',
}

c = new_canvas(64, 64, name='sky-pirate')
idx = {}
for ch, hexv in pal.items():
    idx[ch] = None if hexv is None else c.color(hexv)

for y in range(H):
    for x in range(W):
        ch = grid[y][x]
        if ch != '.':
            c.set(x, y, idx[ch])

# text inspection
print('legend: k=outline S=skin H/h/L=hair G/g=goggles B=white E/e=eye R/r/w=scarf N/n/c=coat M=mouth b=blush')
for y in range(H):
    print(''.join(grid[y]))
print(c.stats_text())

save('sky-pirate-girl', c)
finish(c)
