# Monarch butterfly - 32x32, transparent background.
# The right half is drawn on a 16x32 layer and mirrored, so the wings stay
# perfectly symmetric; body and antennae are added on the full canvas.

c = new_canvas(32, 32, background=None, name="monarch")

BLACK  = c.color("#1A1008", name="black")
ORANGE = c.color("#F5891F", name="orange")
DEEP   = c.color("#D96A10", name="deep_orange")
CREAM  = c.color("#FBEED2", name="cream")

half = new_canvas(16, 32, background=None, name="half")

# ---------------- forewing (right side) ----------------
# black base
half.poly([(0,8),(3,6),(7,4),(11,2),(13,2),(14,4),(14,6),(12,9),(10,12),(7,14),(4,16),(1,17),(0,17)], BLACK)
# orange field, inset from the margin
half.poly([(1,9),(4,7),(8,5),(10,4),(12,4),(13,5),(13,7),(11,9),(9,12),(6,14),(3,16),(1,16)], ORANGE)
# darker basal wedge next to the body
half.poly([(1,9),(3,9),(1,12)], DEEP)
# veins radiating from the wing base
half.line(1,10,12,4, BLACK)
half.line(1,12,11,8, BLACK)
half.line(1,14,8,12, BLACK)
# white spot band in the black apex
for x,y in [(10,3),(12,3),(13,4)]:
    half.set(x,y,CREAM)

# ---------------- hindwing (right side) ----------------
# black base
half.poly([(0,18),(4,18),(8,20),(11,23),(10,26),(7,28),(3,28),(1,26),(0,24)], BLACK)
# orange field
half.poly([(1,19),(5,19),(8,21),(9,23),(8,26),(5,27),(2,27),(1,25)], ORANGE)
# darker basal wedge
half.poly([(1,19),(3,19),(1,22)], DEEP)
# veins
half.line(1,20,8,21, BLACK)
half.line(1,22,8,23, BLACK)
half.line(1,24,6,25, BLACK)
# white spots dotted along the black margin
for x,y in [(10,23),(9,24),(10,25),(7,27)]:
    half.set(x,y,CREAM)

# ---------------- mirror onto the full canvas ----------------
left = half.copy(name="left").mirror(axis="h")
c.blit(left, 0, 0)
c.blit(half, 16, 0)

# ---------------- body ----------------
c.rect(15,6,2,2,BLACK)     # head
c.rect(15,8,2,6,BLACK)     # thorax
c.rect(15,14,2,11,BLACK)   # abdomen
# clubbed antennae
c.line(15,6,11,2,BLACK); c.set(10,1,BLACK)
c.line(16,6,20,2,BLACK); c.set(21,1,BLACK)
# white polka dots on the body
for x,y in [(15,9),(16,11),(15,16),(16,18),(15,20)]:
    c.set(x,y,CREAM)

# sit centered in the frame
c.shift(0, 1)

# ---------------- checks ----------------
asym = [(x, y) for y in range(32) for x in range(16) if c.get(x, y) != c.get(31 - x, y)]
print("asymmetric px (body dots only):", asym)
print(c.stats_text())

finish(c)
