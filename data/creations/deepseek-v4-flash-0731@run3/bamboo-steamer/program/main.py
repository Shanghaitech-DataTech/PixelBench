from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

# palette
WOOD_L = c.color('#E9BE86')
WOOD_M = c.color('#C9995F')
WOOD_D = c.color('#A87A42')
BAND = c.color('#8A5C30')
INNER = c.color('#5E3C1E')
INNER_D = c.color('#3F260E')
DUM_H = c.color('#FFF6E2')
DUM_L = c.color('#F2E0C2')
DUM_M = c.color('#DDBF94')
KNOB = c.color('#6F4822')
KNOB_H = c.color('#9C6A33')
S1 = c.color((255, 255, 255, 235))
S2 = c.color((255, 255, 255, 160))
S3 = c.color((255, 255, 255, 95))

# ---- bamboo steamer, seen slightly from above ----
c.ellipse(16, 21, 12, 10, WOOD_L)            # outer bamboo wall
c.ellipse(16, 21, 12, 10, WOOD_D, fill=False)  # crisp silhouette
c.ellipse(16, 21, 10, 8, WOOD_M)            # mid wall tone
c.ellipse(16, 21, 9, 7, BAND)               # bamboo band ring
c.ellipse(16, 21, 8, 6, INNER)              # dark interior
c.ellipse(16, 21, 9, 7, WOOD_D, fill=False)  # inner band edge hint
# flat woven base
c.rect(8, 28, 16, 2, WOOD_M)
c.rect(9, 30, 14, 2, WOOD_D)
c.line(11, 28, 20, 28, INNER_D)
c.line(12, 29, 19, 29, INNER_D)
c.line(11, 31, 20, 31, INNER_D)

# ---- three pleated dumplings inside ----
def dumpling(cx, cy):
    c.circle(cx, cy, 2, DUM_L)          # pale body
    c.set(cx - 1, cy - 2, DUM_H)        # top highlight
    c.set(cx, cy - 2, DUM_H)
    c.set(cx - 2, cy, DUM_M)            # side pleats
    c.set(cx + 2, cy, DUM_M)
    c.set(cx, cy + 2, DUM_M)            # bottom pleat

dumpling(11, 23)
dumpling(16, 24)
dumpling(21, 23)

# shadow the lifted lid casts into the interior
for (x, y) in [(22, 18), (23, 19), (24, 20), (18, 16), (13, 17)]:
    c.set(x, y, INNER_D)

# ---- lid, slid partly open toward the upper left ----
c.ellipse(12, 11, 9, 7, WOOD_L)
c.ellipse(12, 11, 8, 6, WOOD_M)
c.ellipse(12, 11, 8, 6, WOOD_D, fill=False)   # lid rim ring
c.ellipse(12, 11, 5, 3, BAND, fill=False)     # lid band
c.circle(12, 11, 2, KNOB)
c.set(11, 10, KNOB_H)
c.set(12, 10, KNOB_H)
c.set(11, 12, KNOB_H)

# ---- small steam wisps rising from the open side ----
steam = [
    (19, 19, S2), (18, 18, S3),
    (17, 15, S2), (16, 15, S3),
    (15, 12, S3), (17, 11, S2),
    (14, 9, S3), (16, 8, S2), (18, 7, S3),
    (21, 16, S3), (22, 13, S3),
    (15, 5, S3), (17, 4, S2),
    (16, 2, S3),
]
for (x, y, col) in steam:
    c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
