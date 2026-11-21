from pixelbench_api import *

# Let's inspect step 28 image 3's pixels and color counts
# We'll reproduce it exactly, print stats and matrix_text to inspect!
D = '#2b1400'
S = '#8a4c04'
M = '#db8e09'
L = '#f7c325'
P = '#fff07a'
W = '#ffffff'

outline_pts = [
    (1, range(6, 10)),
    (2, [4, 5, 10, 11]),
    (3, [3, 12]),
    (4, [2, 13]), (5, [2, 13]),
    (6, [1, 14]), (7, [1, 14]), (8, [1, 14]), (9, [1, 14]),
    (10, [2, 13]), (11, [2, 13]),
    (12, [3, 12]),
    (13, [4, 5, 10, 11]),
    (14, range(6, 10)),
]

def make_base():
    c = new_canvas(16, 16)
    for y, xs in outline_pts:
        for x in xs:
            c.set(x, y, D)

    # Fill base coin face
    inside = [
        (2, range(6, 10)),
        (3, range(4, 12)),
        (4, range(3, 13)), (5, range(3, 13)),
        (6, range(2, 14)), (7, range(2, 14)), (8, range(2, 14)), (9, range(2, 14)),
        (10, range(3, 12)), (11, range(3, 12)),
        (12, range(4, 12)),
        (13, range(6, 10)),
    ]
    for y, xs in inside:
        for x in xs:
            c.set(x, y, L)

    # Outer Rim bevel:
    for x in range(6, 10): c.set(x, 2, P)
    c.set(4, 3, P); c.set(5, 3, P)
    c.set(3, 4, P); c.set(3, 5, P)
    c.set(2, 6, P); c.set(2, 7, P)
    c.set(2, 8, L); c.set(2, 9, L)
    c.set(3, 10, L); c.set(3, 11, M)
    c.set(4, 12, M); c.set(5, 12, M)
    
    # Specular glint on rim
    c.set(6, 2, W); c.set(7, 2, W); c.set(5, 3, W)

    # Bottom-right rim shadow
    c.set(10, 3, M); c.set(11, 3, S)
    c.set(12, 4, S); c.set(12, 5, S)
    c.set(13, 6, S); c.set(13, 7, S)
    c.set(13, 8, S); c.set(13, 9, S)
    c.set(12, 10, S); c.set(12, 11, S)
    c.set(10, 12, S); c.set(11, 12, S)
    for x in range(6, 10): c.set(x, 13, S)

    # Bottom-right background shading
    c.set(11, 8, M); c.set(12, 8, M)
    c.set(11, 9, M); c.set(12, 9, M)
    c.set(10, 10, M); c.set(11, 10, M)
    c.set(9, 11, M); c.set(10, 11, M)
    c.set(7, 12, M); c.set(8, 12, M); c.set(9, 12, M)

    return c

c3 = make_base()
star_border = [
    (3, [7, 8]),
    (4, [6, 9]),
    (5, [3, 4, 5, 10, 11, 12]),
    (6, [3, 12]),
    (7, [4, 11]),
    (8, [5, 10]),
    (9, [4, 7, 8, 11]),
    (10, [4, 6, 9, 11]),
    (11, [5, 10]),
]
for y, xs in star_border:
    for x in xs:
        c3.set(x, y, D)
# Fill star inside c3
for y, xs in [
    (4, [7, 8]),
    (5, range(6, 10)),
    (6, range(4, 12)),
    (7, range(5, 11)),
    (8, range(6, 10)),
    (9, [5, 6, 9, 10]),
    (10, [5, 10]),
]:
    for x in xs:
        c3.set(x, y, P)
c3.set(7, 4, W); c3.set(7, 5, W); c3.set(4, 6, W); c3.set(5, 6, W); c3.set(7, 6, W)

print(c3.matrix_text())
print(c3.stats_text())
