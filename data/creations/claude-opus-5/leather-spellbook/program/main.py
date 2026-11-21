c = new_canvas(32, 32, name="output")

OUT = c.color("#1b1119", "outline")
LEA = c.color("#8c3a2e", "leather")
LEA_D = c.color("#55201f", "leather_dark")
LEA_L = c.color("#b4603f", "leather_light")
PAGE = c.color("#f2e3c0", "page")
PAGE_D = c.color("#bf9f71", "page_dark")
GOLD = c.color("#e8c05a", "gold")
GOLD_D = c.color("#8f6a23", "gold_dark")

# ---------------- pages block (offset right + down) ----------------
c.rect(8, 6, 19, 23, PAGE)            # x 8..26, y 6..28
for y in range(8, 28, 2):             # fore-edge page lines
    c.line(25, y, 26, y, PAGE_D)
for x in range(10, 26, 2):            # bottom page lines
    c.line(x, 27, x, 28, PAGE_D)

# ---------------- leather cover ----------------
c.rect(4, 3, 21, 24, LEA)             # x 4..24, y 3..26
# spine slab + fold
c.rect(4, 3, 4, 24, LEA_D)            # x 4..7
c.line(8, 3, 8, 26, LEA_D)
c.line(5, 4, 5, 25, LEA)
# cover shading
c.line(10, 4, 23, 4, LEA_L)
c.line(10, 5, 11, 5, LEA_L)
c.line(10, 25, 23, 25, LEA_D)
c.line(23, 6, 23, 25, LEA_D)

# ---------------- gold inlay frame ----------------
c.rect(11, 7, 10, 17, GOLD, fill=False)   # x 11..20, y 7..23
c.line(11, 23, 20, 23, GOLD_D)
c.line(20, 7, 20, 23, GOLD_D)

# ---------------- arcane emblem ----------------
c.circle(16, 15, 3, GOLD, fill=False)
c.set(16, 11, GOLD)
c.set(16, 19, GOLD)
c.set(12, 15, GOLD)
c.set(20, 15, GOLD)
for p in ((16, 15), (15, 15), (17, 15), (16, 14), (16, 16)):
    c.set(p[0], p[1], GOLD_D)

# ---------------- metal corners (fore-edge side) ----------------
c.poly([(21, 3), (24, 3), (24, 6)], GOLD)
c.poly([(24, 23), (24, 26), (21, 26)], GOLD)
c.line(21, 3, 24, 6, GOLD_D)
c.line(21, 26, 24, 23, GOLD_D)

# ---------------- spine bands ----------------
c.rect(4, 8, 5, 2, GOLD)
c.rect(4, 19, 5, 2, GOLD)
c.line(4, 9, 8, 9, GOLD_D)
c.line(4, 20, 8, 20, GOLD_D)

# ---------------- clasp strap ----------------
c.rect(23, 14, 4, 3, GOLD)
c.line(23, 16, 26, 16, GOLD_D)
c.set(25, 15, GOLD_D)

# ---------------- dark outline ----------------
c.outline(OUT)

view(c)
finish(c)
