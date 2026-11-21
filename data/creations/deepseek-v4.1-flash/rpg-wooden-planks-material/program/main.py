W = H = 16

# ------------------------------------------------------------------ palette
PAL = {
    'S': '#191006',  # seam groove (nearly black)

    # dark plank (x1-4), left -> right gradient
    'A': '#5b391d', 'B': '#6b4324', 'C': '#7b4d2a', 'D': '#8a5830',

    # light plank (x6-10), left -> right gradient
    'E': '#8f5f33', 'F': '#a56d3a', 'G': '#b87f46', 'H': '#c99357', 'I': '#d7a367',

    'J': '#3a2110',  # grain line, dark
    'L': '#e8c08c',  # light grain streak

    'M': '#1f1207',  # knot core (pitch)
    'N': '#6b4526',  # knot ring, on light wood
    'O': '#cfa06a',  # knot ring, light

    'P': '#c08a52',  # lit board end / knot ring, mid
    'Q': '#d3a270',  # lit board end, bright
}

# Row layout:  S | A = x1-4 (dark plank) | S | B = x6-10 (light plank) | S | C = x12-15 (dark plank)
A_ROWS = [
    "ABJD", "ABJD", "ABJD", "ABOD",   # 0-3   knot 1: light ring above
    "APMD", "ABOD", "ABJD", "ABJC",   # 4-7   knot core+ring, lit edge dent
    "AJCD", "AJCD", "ABJD", "ABJD",   # 8-11  grain wobble
    "APQP", "SSSS", "ABJD", "ABJD",   # 12-15 lit board end, joint groove
]
B_ROWS = [
    "EFJHI", "EFJHI", "EJGLI", "EJGHI",   # 0-3   grain lines, light streak
    "EFJHI", "ELJHI", "EFJHI", "SSSSS",   # 4-7   joint groove
    "EPQPI", "EFJLI", "EFOHG", "ENMNI",   # 8-11  lit end, knot 2 ring / core
    "EFOHI", "EFJJI", "EFJHI", "EFJHI",   # 12-15 knot ring below, double grain
]
C_ROWS = [
    "AJCD", "AJCD", "AJCD", "SSSS",   # 0-3   joint groove
    "APQP", "ABJD", "ABOC", "APMD",   # 4-7   lit end, knot 3 ring / core
    "ABOD", "ABJD", "AJCD", "AJCD",   # 8-11  knot ring below, grain wobble
    "AJCD", "ABJD", "AJCD", "AJCD",   # 12-15
]

ROWS = []
for y in range(H):
    row = 'S' + A_ROWS[y] + 'S' + B_ROWS[y] + 'S' + C_ROWS[y]
    assert len(row) == W, (y, len(row), row)
    for ch in row:
        assert ch in PAL, (y, ch)
    ROWS.append(row)

c = new_canvas(W, H, name="wooden_planks")
for y in range(H):
    for x in range(W):
        c.set(x, y, PAL[ROWS[y][x]])

print(c.stats_text())
print(c.matrix_text())


def lum(ch):
    h = PAL[ch].lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return max(0, min(15, round((0.3 * r + 0.59 * g + 0.11 * b) / 255 * 15)))


print("\nLUM (0=f darkest, f=brightest):")
for y in range(H):
    print(' '.join(format(lum(ROWS[y][x]), 'x') for x in range(W)))

save("wooden_planks", c, indexed=True)
finish(c)
