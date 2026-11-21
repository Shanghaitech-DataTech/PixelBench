# Monarch butterfly, 32x32, transparent background.
# Dorsal view, wings spread. Symmetrical about the vertical axis:
# rows are defined for the left half (x = 0..15) and mirrored.

c = new_canvas(32, 32, name="monarch")

DK   = "#1a130c"   # near-black brown (body, wing borders, veins)
OR_D = "#c64e00"   # shaded orange (hindwing / lower band)
OR   = "#f07c00"   # main orange
OR_L = "#ffab38"   # highlight orange (forewing)
WH   = "#f6f0e4"   # white spots

def H(y, x0, x1, col):
    """Horizontal run on left half, mirrored to the right half."""
    for x in range(x0, x1 + 1):
        c.set(x, y, col)
        c.set(31 - x, y, col)

# Each row: (x0, x1, colour) runs on the left half, outermost first.
# Wing rows: dark border run first, then the orange interior reaching
# almost to the body line (columns 14-17 stay dark as the body).
ROWS = {
    2:  [(10, 15, DK)],
    3:  [(7, 15, DK)],
    4:  [(5, 15, DK)],
    5:  [(3, 15, DK), (6, 13, OR_L)],
    6:  [(2, 15, DK), (4, 13, OR_L)],
    7:  [(2, 15, DK), (4, 13, OR_L)],
    8:  [(1, 15, DK), (3, 13, OR_L)],
    9:  [(1, 15, DK), (3, 13, OR)],
    10: [(1, 15, DK), (3, 13, OR)],
    11: [(0, 15, DK), (2, 13, OR)],
    12: [(0, 15, DK), (2, 13, OR)],
    13: [(0, 15, DK), (2, 13, OR)],
    14: [(0, 15, DK), (2, 13, OR_D)],
    15: [(1, 15, DK), (3, 13, OR_D)],
    16: [(1, 15, DK), (3, 13, OR_D)],
    17: [(2, 15, DK), (4, 13, OR_D)],
    18: [(2, 15, DK), (4, 13, OR_D)],
    19: [(3, 15, DK), (5, 13, OR_D)],
    20: [(3, 15, DK), (5, 12, OR_D)],
    21: [(4, 15, DK), (6, 11, OR_D)],
    22: [(5, 15, DK), (7, 10, OR_D)],
    23: [(6, 15, DK), (8, 9, OR_D)],
    24: [(7, 15, DK)],
    25: [(8, 15, DK)],
    26: [(9, 15, DK)],
    27: [(10, 15, DK)],
}

for y, runs in ROWS.items():
    for x0, x1, col in runs:
        H(y, x0, x1, col)

# White spots (left-half coordinates, mirrored): forewing + hindwing
SPOTS = [(9, 5), (4, 6), (11, 6), (8, 7), (12, 7), (6, 8), (10, 9),
         (5, 10), (8, 10), (6, 11),
         (4, 13), (7, 14), (6, 16), (8, 17), (5, 19)]
for x, y in SPOTS:
    H(y, x, x, WH)

# Body: slim the wing-root columns so only x=15/16 carry the thorax
# and abdomen; the rest returns to wing colour.
BODY_FIX = {
    2:  [(14, 14, DK), (17, 17, DK)],   # head
    3:  [(14, 14, OR_L), (17, 17, OR_L)],
    4:  [(14, 14, OR_L), (17, 17, OR_L)],
    5:  [(14, 14, OR_L), (17, 17, OR_L)],
    6:  [(14, 14, OR_L), (17, 17, OR_L)],
    7:  [(14, 14, OR_L), (17, 17, OR_L)],
    8:  [(14, 14, OR_L), (17, 17, OR_L)],
    9:  [(14, 14, OR), (17, 17, OR)],
    10: [(14, 14, OR), (17, 17, OR)],
    11: [(14, 14, OR), (17, 17, OR)],
    12: [(14, 14, OR), (17, 17, OR)],
    13: [(14, 14, OR), (17, 17, OR)],
    14: [(14, 14, OR_D), (17, 17, OR_D)],
    15: [(14, 14, OR_D), (17, 17, OR_D)],
    16: [(14, 14, OR_D), (17, 17, OR_D)],
    17: [(14, 14, OR_D), (17, 17, OR_D)],
    18: [(14, 14, OR_D), (17, 17, OR_D)],
    19: [(14, 14, OR_D), (17, 17, OR_D)],
    20: [(14, 14, OR_D), (17, 17, OR_D)],
    21: [(14, 14, OR_D), (17, 17, OR_D)],
    22: [(14, 14, OR_D), (17, 17, OR_D)],
    23: [(14, 14, OR_D), (17, 17, OR_D)],
    24: [(14, 14, DK), (17, 17, DK)],
}
for y, runs in BODY_FIX.items():
    for x0, x1, col in runs:
        for x in range(x0, x1 + 1):
            c.set(x, y, col)

# Head dots and slim thorax/abdomen line (x=15/16 already dark)
c.set(15, 2, WH); c.set(16, 2, WH)          # eyes / head dots
c.set(15, 3, WH); c.set(16, 3, WH)          # thorax dots

# Antennae curving up and out from the head
c.set(13, 1, DK); c.set(18, 1, DK)
c.set(12, 0, DK); c.set(19, 0, DK)

# Dark veins fanning out through the hindwing (monarch diagnostic)
c.line(14, 15, 8, 19, DK);  c.line(17, 15, 23, 19, DK)
c.line(14, 17, 9, 22, DK);  c.line(17, 17, 22, 22, DK)

# Centre the 28-row-tall sprite vertically (2px margin top and bottom)
c.shift(0, 2)

print(c.stats_text())
view(c)
finish(c)
