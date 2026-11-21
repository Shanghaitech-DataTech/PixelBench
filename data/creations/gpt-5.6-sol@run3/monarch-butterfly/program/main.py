from pixelbench_api import new_canvas, view, finish

result = new_canvas(32, 32, background=None, name="monarch-butterfly")

INK = "#17120fff"
DEEP = "#6f260fff"
ORANGE = "#e96f18ff"
GOLD = "#f59a25ff"
CREAM = "#fff1c7ff"
WHITE = "#ffffffff"

# Mirrored wing silhouettes.
def mirror(points):
    return [(31 - x, y) for x, y in points]

left_fore = [(14, 11), (12, 7), (9, 4), (5, 3), (2, 5), (1, 9),
             (3, 13), (7, 16), (12, 17), (15, 15)]
left_hind = [(13, 14), (8, 14), (4, 16), (2, 20), (3, 24), (6, 27),
             (10, 28), (13, 25), (15, 20)]
for shape in (left_fore, left_hind):
    result.poly(shape, INK)
    result.poly(mirror(shape), INK)

# Orange forewing fields, separated by heavy monarch veins.
fore_cells = [
    [(13, 11), (11, 8), (9, 6), (7, 5), (7, 10), (10, 13)],
    [(5, 5), (3, 6), (2, 9), (4, 10), (6, 10), (6, 5)],
    [(3, 11), (5, 14), (8, 15), (9, 14), (6, 11)],
    [(8, 11), (10, 14), (12, 15), (14, 14), (13, 12)],
]
for cell in fore_cells:
    result.poly(cell, ORANGE)
    result.poly(mirror(cell), ORANGE)

# Golden inner facets catch the light.
for cell in [
    [(9, 6), (11, 8), (13, 11), (12, 12), (10, 11), (8, 9)],
    [(5, 12), (7, 14), (9, 15), (9, 13), (7, 11)],
]:
    result.poly(cell, GOLD)
    result.poly(mirror(cell), GOLD)

# Hindwing fields fan outward from the body.
hind_cells = [
    [(13, 16), (10, 16), (8, 17), (9, 21), (12, 23), (14, 20)],
    [(7, 16), (5, 17), (3, 20), (4, 22), (8, 21)],
    [(4, 23), (6, 26), (9, 27), (9, 23), (8, 22)],
    [(10, 22), (10, 26), (12, 24), (14, 21), (12, 22)],
]
for cell in hind_cells:
    result.poly(cell, ORANGE)
    result.poly(mirror(cell), ORANGE)

# Veins: sparse single-pixel strokes retain a crisp, graphic read.
for x0, y0, x1, y1 in [
    (14, 13, 7, 5), (13, 14, 3, 10), (12, 16, 7, 15),
    (14, 18, 4, 22), (14, 19, 9, 27), (13, 17, 12, 24),
]:
    result.line(x0, y0, x1, y1, INK)
    result.line(31-x0, y0, 31-x1, y1, INK)

# Pale spots embedded in the black margins.
spots = [(4, 6), (2, 9), (4, 12), (6, 15), (3, 20), (4, 24),
         (7, 26), (10, 27)]
for x, y in spots:
    result.set(x, y, WHITE)
    result.set(31-x, y, WHITE)
# Two slightly warm inner border marks.
for x, y in [(6, 4), (11, 7), (12, 25)]:
    result.set(x, y, CREAM)
    result.set(31-x, y, CREAM)

# Central thorax, abdomen, head, and antennae.
result.rect(14, 11, 4, 8, INK)
result.rect(15, 18, 2, 8, INK)
result.set(15, 26, INK).set(16, 26, INK)
result.rect(15, 8, 2, 3, INK)
result.set(14, 9, INK).set(17, 9, INK)
result.line(15, 8, 12, 4, INK)
result.line(16, 8, 19, 4, INK)
result.set(11, 3, INK).set(20, 3, INK)
# Tiny body highlights suggest segmentation.
result.set(15, 13, DEEP).set(16, 16, DEEP).set(15, 20, DEEP).set(16, 23, DEEP)

view(result, scale=16, margin=0)
finish(result)
