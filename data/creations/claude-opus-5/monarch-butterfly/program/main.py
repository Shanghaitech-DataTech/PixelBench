W = H = 32

half = new_canvas(W, H, name="half")

BLK = half.color("#20141a", "black")
ORG = half.color("#e8821e", "orange")
DRK = half.color("#bb5e12", "deep")
LIT = half.color("#f6b23c", "light")
WHT = half.color("#fdf6e8", "white")
BOD = half.color("#2b1d20", "body")

def spans(c, rows, col):
    for y, x0, x1 in rows:
        c.rect(x0, y, x1 - x0 + 1, 1, col)

fore = [
    (3, 21, 26),
    (4, 19, 28),
    (5, 18, 29),
    (6, 16, 29),
    (7, 16, 30),
    (8, 16, 30),
    (9, 16, 30),
    (10, 16, 29),
    (11, 16, 28),
    (12, 16, 28),
    (13, 16, 26),
    (14, 16, 24),
]
hind = [
    (15, 16, 22),
    (16, 16, 23),
    (17, 16, 24),
    (18, 16, 25),
    (19, 16, 26),
    (20, 16, 26),
    (21, 16, 26),
    (22, 16, 25),
    (23, 16, 24),
    (24, 17, 23),
    (25, 18, 21),
    (26, 19, 20),
]

spans(half, fore, ORG)
spans(half, hind, ORG)

half.outline(BLK)

# black apex wedge of the forewing
half.poly([(26, 4), (29, 6), (29, 9), (27, 10), (23, 5)], BLK)

# seam between fore- and hindwing
half.line(17, 14, 22, 14, BLK)

# veins as explicit single-pixel strokes so they stay thin
fore_veins = [
    [(18, 12), (19, 11), (19, 10), (20, 9), (20, 8), (21, 7), (21, 6), (22, 5)],
    [(20, 12), (21, 11), (22, 11), (23, 10), (24, 10), (25, 9)],
]
hind_veins = [
    [(19, 17), (20, 17), (21, 18), (22, 18), (23, 19)],
    [(18, 18), (19, 19), (19, 20), (20, 21), (20, 22), (21, 23)],
    [(18, 20), (18, 21), (19, 22), (19, 23)],
]
for stroke in fore_veins + hind_veins:
    for x, y in stroke:
        half.set(x, y, BLK)

# thicken the outer black margin so marginal spots sit on black
margin = [
    (4, 27, 28), (5, 28, 29), (6, 29, 29), (10, 28, 29), (11, 27, 28),
    (12, 27, 28), (13, 25, 26), (14, 23, 24),
    (18, 25, 25), (19, 25, 26), (20, 25, 26), (21, 25, 26),
    (22, 24, 25), (23, 23, 24), (24, 22, 23), (25, 20, 21),
]
spans(half, margin, BLK)

# white spots on the black apex / margins
for x, y in [(25, 4), (27, 4), (28, 5), (29, 7), (28, 10), (26, 12),
             (25, 20), (24, 22), (22, 23), (20, 25), (18, 24)]:
    half.set(x, y, WHT)

# shading along the inner/lower edges
half.set(19, 13, DRK)
half.set(20, 13, DRK)
half.line(19, 22, 22, 22, DRK)
# highlight along the leading edge
half.line(22, 4, 24, 4, LIT)
half.set(20, 5, LIT)
half.set(21, 5, LIT)
half.line(18, 16, 20, 16, LIT)

left = half.copy(name="left")
left.mirror("h")

body = new_canvas(W, H, name="body")
# abdomen / thorax
body.rect(15, 8, 2, 15, BOD)
body.rect(15, 23, 2, 1, BOD)
body.set(15, 24, BOD)
body.set(16, 24, BOD)
# head
body.rect(15, 6, 2, 2, BOD)
# body speckles (monarch's white dots)
for y in [12, 15, 18, 21]:
    body.set(15, y, WHT)
    body.set(16, y, WHT)
# antennae
body.line(14, 5, 12, 2, BLK)
body.line(17, 5, 19, 2, BLK)
body.set(11, 1, BLK)
body.set(20, 1, BLK)

result = flatten([left, half, body], name="output")

view(result)
print(result.stats_text())
finish(result)
