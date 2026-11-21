c = new_canvas(32, 32, name="output")

OUT = c.color("#15121a", "outline")
VDK = c.color("#222835", "mail_vdk")
DK = c.color("#343c4d", "mail_dk")
MD = c.color("#505b6e", "mail_md")
LT = c.color("#79859a", "mail_lt")
HI = c.color("#a9b6c9", "mail_hi")
WH = c.color("#d7e0ee", "mail_spec")
LTH = c.color("#6b4526", "leather")
LTHD = c.color("#3f2615", "leather_dk")
BRS = c.color("#cfa64b", "brass")
BRSD = c.color("#8d6a24", "brass_dk")

# ---- silhouette: hauberk with short mail sleeves -------------------------
rows = {}
rows[7] = (10, 21)
rows[8] = (8, 23)
rows[9] = (6, 25)
for y in range(10, 16):
    rows[y] = (5, 26)
rows[16] = (6, 25)
for y in range(17, 28):
    rows[y] = (8, 23)


def tier(x, y):
    """(ring crown, ring shadow, base) under upper-left lighting"""
    d = x * 0.45 + y * 1.0
    if d < 12:
        return WH, MD, LT
    if d < 20:
        return HI, DK, MD
    if d < 27:
        return LT, VDK, MD
    return MD, VDK, DK


# ---- interlocking rings: lit crown over dark underside, brick-staggered --
for y, (a, b) in rows.items():
    band = (y // 2) % 2
    for x in range(a, b + 1):
        crown, shade, base = tier(x, y)
        c.set(x, y, base)
        if (x + band) % 2 == 0:
            c.set(x, y, crown if y % 2 == 0 else shade)

# ---- hems: sleeve cuffs and skirt edge ----------------------------------
for x in list(range(5, 9)) + list(range(23, 27)):
    for y in (15, 16):
        if rows.get(y) and rows[y][0] <= x <= rows[y][1]:
            c.set(x, y, VDK if y == 16 else DK)
for x in range(8, 24):
    c.set(x, 27, VDK)
    if x % 2 == 0:
        c.set(x, 26, DK)

# ---- body/sleeve seams and right-side falloff ---------------------------
for y in range(9, 17):
    c.set(9, y, DK)
    c.set(22, y, DK)
for y in range(17, 27):
    c.set(22, y, DK)
    c.set(23, y, VDK)

# ---- neck opening with a dark collar trim -------------------------------
hole = {7: (13, 18), 8: (14, 17), 9: (15, 16)}
trim = [(12, 7), (19, 7), (13, 8), (18, 8), (14, 9), (17, 9),
        (15, 10), (16, 10), (14, 10), (17, 10)]
for x, y in trim:
    c.set(x, y, DK)
for y, (a, b) in hole.items():
    c.rect(a, y, b - a + 1, 1, None)

# ---- belt ---------------------------------------------------------------
c.rect(8, 21, 16, 3, LTH)
c.rect(8, 23, 16, 1, LTHD)
c.rect(14, 21, 4, 3, BRS)
c.rect(15, 22, 2, 1, BRSD)

# ---- shadow cast by the belt onto the skirt ----------------------------
for x in range(9, 23):
    if c.get(x, 24) not in (OUT, None):
        c.set(x, 24, VDK if x % 2 else DK)

# ---- specular pop on the left shoulder ---------------------------------
for x, y in ((9, 10), (11, 10), (10, 11), (8, 11)):
    c.set(x, y, WH)

c.outline(OUT)

print(c.stats_text())
save("chainmail-armor", c)
view(c)
finish(c)
