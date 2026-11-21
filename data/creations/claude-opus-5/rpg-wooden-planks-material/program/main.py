c = new_canvas(16, 16, name="output")

GROOVE = "#38220f"
KNOT_D = "#4a2a12"
KNOT_R = "#6b4320"

# tones per board: (base, highlight, shade, grain)
L = ("#bb854b", "#cf9c60", "#a06f3d", "#ab7942")
D = ("#8e5f31", "#a27141", "#73491f", "#7f5429")
M = ("#a5723c", "#b98650", "#86592c", "#946634")


def board(x0, w, tone, endrow, grain, knots=()):
    base, hi, shade, gr = tone
    c.rect(x0, 0, w, 16, base)
    c.line(x0, 0, x0, 15, hi)                    # lit left edge
    c.line(x0 + w - 1, 0, x0 + w - 1, 15, shade)  # shaded right edge
    for gx, y0, y1 in grain:
        c.line(gx, y0, gx, y1, gr)
    # plank end: dark groove with a lit lip below it
    c.rect(x0, endrow, w, 1, GROOVE)
    c.rect(x0, (endrow + 1) % 16, w, 1, hi)
    for kx, ky in knots:
        c.set(kx, ky, KNOT_R)
        c.set(kx + 1, ky, KNOT_D)
        c.set(kx, ky + 1, KNOT_D)
        c.set(kx + 1, ky + 1, KNOT_R)


# board 1: columns 1-4, end seam on row 0
board(1, 4, L, 0,
      [(2, 3, 6), (3, 9, 12), (2, 13, 15), (3, 2, 2)],
      knots=[(2, 8)])

# board 2: columns 6-10, end seam on row 5
board(6, 5, D, 5,
      [(8, 7, 10), (7, 0, 2), (9, 12, 15), (8, 14, 15), (7, 11, 11)],
      knots=[(9, 2)])

# board 3: columns 12-15, end seam on row 10
board(12, 4, M, 10,
      [(13, 1, 4), (14, 12, 14), (13, 7, 8), (14, 6, 6)])

# vertical seam grooves between planks
for sx in (0, 5, 11):
    c.line(sx, 0, sx, 15, GROOVE)

view(c)

print(c.stats_text())
finish(c)
