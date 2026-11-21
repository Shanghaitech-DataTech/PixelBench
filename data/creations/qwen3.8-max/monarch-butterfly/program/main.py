# Monarch butterfly, 32x32, transparent background.
# Strategy: draw only the left half (x = 0..15), then flip-copy it to the right.

c = new_canvas(32, 32, name="monarch")

# ---------------------------------------------------------------- palette ---
BLACK   = "#1b1210"   # wing margin + veins
ORANGE  = "#e0741e"   # main wing orange
AMBER   = "#f59a2b"   # lighter orange highlight
RUST    = "#b1521a"   # dark orange near the wing base
CREAM   = "#f6ead2"   # white margin spots
BODY    = "#3a2a22"   # body dark
BODY_HI = "#6b5348"   # body highlight
SHELL   = "#0e0a09"   # near-black outline / eyes


def spans(table, colour):
    """Paint one horizontal run per row: table = {y: (x0, x1)} inclusive."""
    for y, (x0, x1) in sorted(table.items()):
        c.rect(x0, y, x1 - x0 + 1, 1, colour)


# ------------------------------------------------- wing silhouette (black) --
# Forewing: pointed apex at the outer top, costa sloping down to the thorax.
fore_out = {
    2:  (6, 8),
    3:  (4, 10),
    4:  (2, 12),
    5:  (1, 12),
    6:  (1, 15),
    7:  (1, 15),
    8:  (2, 15),
    9:  (3, 15),
    10: (4, 15),
    11: (5, 15),
    12: (6, 15),
    13: (7, 15),
    14: (8, 15),
}
# Hindwing: rounded fan, tucked under the forewing.
hind_out = {
    15: (9, 15),
    16: (6, 15),
    17: (4, 15),
    18: (3, 15),
    19: (2, 15),
    20: (2, 15),
    21: (2, 15),
    22: (3, 15),
    23: (4, 15),
    24: (5, 15),
    25: (6, 15),
    26: (7, 15),
    27: (9, 15),
    28: (11, 15),
}
spans(fore_out, BLACK)
spans(hind_out, BLACK)

# ------------------------------------------------------- wing interior ------
fore_in = {
    4:  (6, 10),
    5:  (3, 11),
    6:  (3, 15),
    7:  (3, 15),
    8:  (4, 15),
    9:  (5, 15),
    10: (6, 15),
    11: (7, 15),
    12: (8, 15),
    13: (9, 15),
}
hind_in = {
    15: (11, 15),
    16: (8, 15),
    17: (7, 15),
    18: (5, 15),
    19: (4, 15),
    20: (4, 15),
    21: (4, 15),
    22: (5, 15),
    23: (6, 15),
    24: (7, 15),
    25: (8, 15),
    26: (9, 15),
}
spans(fore_in, ORANGE)
spans(hind_in, ORANGE)

# base shading: darker orange where the wing meets the body
for y in list(range(6, 14)) + list(range(17, 27)):
    c.rect(13, y, 2, 1, RUST)

# lighter amber wash in the open cells of each wing
spans({6: (4, 9), 7: (4, 9), 8: (5, 10), 9: (6, 10)}, AMBER)
spans({18: (6, 10), 19: (5, 9), 20: (5, 9), 21: (5, 9), 22: (6, 10)}, AMBER)

# ------------------------------------------------------------------ veins ---
fore_veins = [
    ((13, 7), (5, 5)),
    ((13, 9), (3, 7)),
    ((13, 11), (3, 10)),
    ((13, 13), (7, 13)),
]
hind_veins = [
    ((13, 18), (6, 17)),
    ((13, 20), (4, 20)),
    ((13, 22), (6, 23)),
    ((13, 24), (9, 25)),
]
for (x0, y0), (x1, y1) in fore_veins + hind_veins:
    c.line(x0, y0, x1, y1, BLACK)

# --------------------------------------------------------- margin spots -----
spots_fore = [(7, 2), (4, 3), (2, 4), (1, 6), (2, 8), (4, 10), (6, 12),
              (8, 13), (10, 14), (12, 14)]
spots_hind = [(6, 16), (3, 18), (2, 20), (3, 22), (5, 24), (7, 25),
              (8, 26), (11, 27), (13, 28)]
for x, y in spots_fore + spots_hind:
    c.set(x, y, CREAM)

# ------------------------------------------------------------------- body ---
# head (2px wide per half -> 4px wide mirrored, eyes on its outer edge)
c.rect(14, 7, 2, 3, BODY)
c.set(14, 8, SHELL)          # eye (mirrors to the other side)
# thorax
c.rect(14, 10, 2, 6, BODY)
c.set(13, 11, BODY)
c.set(13, 12, BODY)
c.rect(15, 10, 1, 5, BODY_HI)
# abdomen, tapering
c.rect(14, 16, 2, 5, BODY)
c.rect(14, 21, 2, 2, BODY)
c.rect(15, 23, 1, 2, BODY)
c.set(15, 17, BODY_HI)
c.set(15, 19, BODY_HI)
# pale body spots
c.set(13, 13, CREAM)
c.set(13, 18, CREAM)
c.set(15, 22, CREAM)

# -------------------------------------------------------------- antennae ----
c.line(15, 6, 12, 3, BLACK)   # shaft: (15,6)(14,5)(13,4)(12,3)
c.set(11, 2, BLACK)
c.set(10, 2, BLACK)           # club
c.set(10, 1, BLACK)

# ------------------------------------------------------------ mirror half ---
half = c.select(0, 0, 16, 32)
half = half.flip(axis="h")
half.copy_to(16, 0, c, mode="replace")

print(c.stats_text())
p = view(c, scale=16)
print("preview:", p)
save("monarch", c, indexed=True)

finish(c)
