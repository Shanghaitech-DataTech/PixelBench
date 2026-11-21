# Mushroomling: 16x16 RPG enemy pixel art.
# 4 visible colors: dark outline, red cap, white spots, cream body.
c = new_canvas(16, 16)

O = "#141414"  # dark outline
R = "#d93a2b"  # red cap
W = "#f7f2e7"  # white spots / eyes
C = "#f0d9a8"  # cream body


def hline(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)


def vline(y0, y1, x, col):
    for y in range(y0, y1 + 1):
        c.set(x, y, col)


# ---- cap (red dome with outline) ----
hline(1, 6, 9, O)          # top
hline(2, 5, 10, O); hline(2, 6, 9, R)
hline(3, 4, 11, O); hline(3, 5, 10, R)
hline(4, 3, 12, O); hline(4, 4, 11, R)
hline(5, 3, 12, O); hline(5, 4, 11, R)
hline(6, 4, 11, O); hline(6, 5, 10, R)
hline(7, 5, 10, O)          # rim

# ---- white spots ----
for sx, sy in [(5, 4), (6, 4), (5, 5), (6, 5),
               (9, 4), (10, 4), (9, 5), (10, 5),
               (6, 6), (9, 6)]:
    c.set(sx, sy, W)

# ---- stem / body ----
hline(8, 4, 11, O); hline(8, 5, 10, C)
# face: round eyes
hline(9, 4, 11, O)
c.set(5, 9, W); c.set(6, 9, W)
c.set(7, 9, C); c.set(8, 9, C)
c.set(9, 9, W); c.set(10, 9, W)
# arms + lower face row
hline(10, 2, 13, O)
for x in [5, 6, 9, 10]:
    c.set(x, 10, W)
for x in [7, 8]:
    c.set(x, 10, C)
c.set(3, 10, C); c.set(12, 10, C)
hline(11, 4, 11, O); hline(11, 5, 10, C)
# arms at row 11
c.set(2, 11, O); c.set(3, 11, C)
c.set(12, 11, C); c.set(13, 11, O)
# mouth
c.set(7, 11, O); c.set(8, 11, O)

# ---- legs ----
c.set(4, 12, O); c.set(5, 12, C); c.set(6, 12, O)
c.set(9, 12, O); c.set(10, 12, C); c.set(11, 12, O)
c.set(5, 13, O); c.set(6, 13, O)
c.set(9, 13, O); c.set(10, 13, O)

print(c.stats_text())
print()
print(c.matrix_text())
finish(c)
