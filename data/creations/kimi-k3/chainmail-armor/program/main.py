# Chainmail armor (hauberk) - 32x32 RPG item icon

OUT = '#171a21'   # dark outline
DARK = '#3d434f'  # ring shadow / deep metal
MID = '#6e7684'   # base metal
LIGHT = '#aab2bf' # ring light
HI = '#e2e8f0'    # specular highlight

c = new_canvas(32, 32, background=None, name="chainmail")

# ---- Silhouette (filled rows), tracked in a set for ring clipping ----
S = set()
def row(y, x0, x1, col=MID):
    c.rect(x0, y, x1 - x0 + 1, 1, col)
    for x in range(x0, x1 + 1):
        S.add((x, y))

row(3, 12, 19)          # collar top
row(4, 10, 21)
row(5, 7, 24)           # shoulders
row(6, 5, 26)
row(7, 4, 27)
for y in range(8, 13):  # sleeves at full width
    row(y, 3, 28)
row(13, 4, 27)          # sleeve hem
row(14, 7, 24)          # armpit
for y in range(15, 27): # torso
    row(y, 8, 23)
row(27, 9, 22)          # hem
row(28, 10, 21)

# ---- Neck opening (stepped V cut to transparency) ----
for x in range(13, 19):
    c.set(x, 4, None); S.discard((x, 4))
for x in range(14, 18):
    c.set(x, 5, None); S.discard((x, 5))
for x in range(15, 17):
    c.set(x, 6, None); S.discard((x, 6))

# ---- Shading (subtle checker dither under sleeves and at hem) ----
c.dither(8, 14, 16, 2, [MID, DARK], pattern="checker")
c.dither(9, 25, 14, 3, [MID, DARK], pattern="checker")
# left side light catch
c.rect(8, 16, 1, 9, LIGHT)
c.set(9, 15, LIGHT)

# ---- Sleeve hem trim ----
c.line(3, 12, 8, 12, DARK)
c.line(23, 12, 28, 12, DARK)

# ---- Interlocking ring pattern (only where the whole 3x3 fits inside) ----
for r, y in enumerate(range(6, 27, 3)):
    off = 2 if r % 2 else 0
    for x in range(5 + off, 28, 4):
        if all((x + dx, y + dy) in S for dx in (-1, 0, 1) for dy in (-1, 0, 1)):
            c.circle(x, y, 1, DARK, fill=False)  # 3x3 ring
            c.set(x, y - 1, LIGHT)               # top sheen on each ring

# ---- Dark outline everywhere the armor meets transparency ----
c.outline(OUT)

# a couple of bright hits on the upper chest
c.set(11, 10, HI); c.set(12, 10, HI)

view(c)
finish(c)
