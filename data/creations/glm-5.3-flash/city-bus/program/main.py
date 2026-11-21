# 64x32 modern city bus - side view, facing right, transparent background
W, H = 64, 32
c = new_canvas(W, H, None, "city-bus")

PAL = [
    ("body",    "#E9EDF1"),
    ("shade",   "#C9D2DB"),
    ("roof",    "#A9B4C0"),
    ("skirt",   "#3A4450"),
    ("stripe",  "#2E77C0"),
    ("glass",   "#33566F"),
    ("glass_l", "#82B4CD"),
    ("glass_d", "#223B4D"),
    ("pillar",  "#BCC6D0"),
    ("tire",    "#23262E"),
    ("hub",     "#9AA4B0"),
    ("hubc",    "#D8DFE6"),
    ("disp",    "#101319"),
    ("amber",   "#FFB627"),
    ("light",   "#FFF6CF"),
    ("light2",  "#FFC94D"),
    ("tail",    "#D8453C"),
    ("out",     "#1E232B"),
    ("well",    "#171B22"),
]
P = {}
for k, v in PAL:
    P[k] = c.color(v, k)

# ---------------- body block  x2..61  y5..21 ----------------
c.rect(2, 5, 60, 17, P["body"])
c.rect(3, 6, 58, 1, P["roof"])          # roof cap strip
c.rect(2, 20, 60, 2, P["skirt"])        # skirt / underframe y20..21

# ---------------- window band  y13..18 ----------------
segs = [(4, 8), (10, 14), (16, 20), (32, 36), (38, 42), (44, 48)]
for x0, x1 in segs:
    w = x1 - x0 + 1
    c.rect(x0, 13, w, 6, P["glass"])
    c.rect(x0, 13, w, 1, P["glass_l"])
    c.rect(x0, 18, w, 1, P["glass_d"])
for x in (9, 15, 21, 31, 37, 43, 49):
    c.rect(x, 13, 1, 6, P["pillar"])
# windshield wrapping the front corner
c.rect(59, 13, 3, 6, P["glass"])
c.rect(59, 13, 3, 1, P["glass_l"])
c.rect(59, 18, 3, 1, P["glass_d"])

# ---------------- livery stripe ----------------
c.rect(2, 19, 60, 1, P["stripe"])

# ---------------- wheel arch openings cut into the skirt ----------------
for cx in (17, 45):
    c.rect(cx - 2, 20, 5, 1, P["well"])
    c.rect(cx - 3, 21, 7, 1, P["well"])

# ---------------- doors (9 wide, glazed, centre split) ----------------
def door(x0):
    c.rect(x0, 13, 9, 9, P["shade"])            # shell y13..21
    c.rect(x0 + 1, 13, 3, 6, P["glass"])
    c.rect(x0 + 5, 13, 3, 6, P["glass"])
    c.rect(x0 + 1, 13, 3, 1, P["glass_l"])
    c.rect(x0 + 5, 13, 3, 1, P["glass_l"])
    c.rect(x0 + 1, 18, 3, 1, P["glass_d"])
    c.rect(x0 + 5, 18, 3, 1, P["glass_d"])
    c.rect(x0 + 4, 13, 1, 9, P["pillar"])       # centre split

door(22)    # rear door   x22..30
door(50)    # front door  x50..58

# ---------------- electronic route display ----------------
c.rect(49, 7, 11, 6, P["disp"])                 # x49..59, y7..12
DIG = {
    "4": ["..#", "#.#", "###", "..#"],
    "2": ["###", "..#", "###", "#.."],
}
def digit(ch, x, y):
    for j, row in enumerate(DIG[ch]):
        for i, v in enumerate(row):
            if v == "#":
                c.set(x + i, y + j, P["amber"])
digit("4", 51, 8)
digit("2", 55, 8)

# ---------------- round the corners ----------------
for x, y in [(2, 5), (3, 5), (2, 6), (61, 5), (60, 5), (61, 6), (2, 21), (61, 21)]:
    c.set(x, y, None)

# ---------------- contour ----------------
c.outline(P["out"])

# ---------------- wheels ----------------
for cx in (17, 45):
    for dy in range(-3, 4):
        for dx in range(-3, 4):
            if dx * dx + dy * dy <= 10:
                c.set(cx + dx, 24 + dy, P["tire"])
    c.rect(cx - 1, 23, 3, 3, P["hub"])
    c.set(cx, 24, P["hubc"])

# ---------------- lights ----------------
c.rect(59, 19, 3, 2, P["light"])        # headlight
c.set(61, 20, P["light2"])
c.rect(2, 19, 2, 2, P["tail"])          # taillight

# ---------------- mirror ----------------
c.rect(62, 11, 2, 3, P["out"])

print(c.stats_text())
save("city-bus", c)
finish(c)
