c = new_canvas(32, 32, name="slime")

BODY_D = c.color("#2d6336", "body_dark")
BODY   = c.color("#43924a", "body")
BODY_L = c.color("#62bc5c", "body_light")
HILITE = c.color("#9fe086", "hilite")
MOSS_D = c.color("#3f7a2e", "moss_dark")
MOSS   = c.color("#8cc63f", "moss")
EYE_G  = c.color("#d6ff5e", "eye_glow")
EYE_C  = c.color("#ffffff", "eye_core")
OUT    = c.color("#17301c", "outline")
ANT    = c.color("#b88c57", "antler")
ANT_D  = c.color("#6b4e2f", "antler_dark")
MUSH   = c.color("#d9463a", "mush")
MUSH_D = c.color("#99281f", "mush_dark")
MUSH_S = c.color("#ffe3cf", "mush_spot")
STEM   = c.color("#e8d3ad", "stem")
STEM_D = c.color("#b39c76", "stem_dark")


def rows(spans, col):
    """spans: list of (y, x0, x1) inclusive."""
    for y, x0, x1 in spans:
        c.rect(x0, y, x1 - x0 + 1, 1, col)


def pix(points, col, mirror=True):
    """points are (x, y); mirror also paints the x -> 31-x twin."""
    for x, y in points:
        c.set(x, y, col)
        if mirror:
            c.set(31 - x, y, col)


# ================================================================ body
rows([
    (8, 13, 18), (9, 11, 20), (10, 10, 21), (11, 9, 22), (12, 9, 22),
    (13, 8, 23), (14, 7, 24), (15, 7, 24), (16, 6, 25), (17, 6, 25),
    (18, 5, 26), (19, 5, 26), (20, 4, 27), (21, 4, 27), (22, 3, 28),
    (23, 3, 28), (24, 3, 28), (25, 3, 28), (26, 3, 28), (27, 4, 27),
    (28, 6, 25),
], BODY)

# upper-left lit region
rows([
    (8, 13, 18), (9, 11, 20), (10, 10, 20), (11, 9, 19), (12, 9, 18),
    (13, 8, 16), (14, 7, 14), (15, 7, 12), (16, 6, 10), (17, 6, 8),
], BODY_L)

# brightest sheen
rows([(11, 10, 12), (12, 9, 11), (13, 9, 10)], HILITE)

# shadow: right flank and the heavy base
rows([
    (14, 23, 24), (15, 23, 24), (16, 24, 25), (17, 24, 25),
    (18, 25, 26), (19, 25, 26), (20, 26, 27), (21, 26, 27),
    (22, 26, 28), (23, 26, 28), (24, 24, 28),
    (25, 3, 28), (26, 3, 28), (27, 4, 27), (28, 6, 25),
], BODY_D)

# ================================================================ moss
rows([
    (8, 13, 18), (9, 11, 13), (9, 16, 19), (10, 10, 11),
    (10, 18, 20), (11, 9, 9), (11, 21, 22),
], MOSS)
pix([(13, 10), (12, 11), (19, 11)], MOSS, mirror=False)
pix([(14, 9), (18, 9), (10, 10)], MOSS_D, mirror=False)
rows([(16, 6, 7), (17, 6, 6), (22, 3, 4)], MOSS)
pix([(27, 21), (28, 22)], MOSS, mirror=False)

# Silhouette outline runs here: body and moss only. Every prop below
# carries its own dark edge so thin shapes are not eaten.
c.outline(OUT)

# ================================================================ antlers
# Two small Y forks rooted in the dome at x=13 and its mirror x=18.
# Inner prongs land on x=14 and x=17, three columns apart, so the
# mirrored pair cannot fuse into a crossbar across the middle.
pix([(13, 8), (13, 7)], ANT_D)       # trunk, rooted in the dome
rows([(6, 12, 14), (6, 17, 19)], ANT_D)   # solid fork junction
pix([(12, 5), (14, 5)], ANT_D)       # prongs rise from the junction
pix([(12, 4), (14, 4)], ANT)         # lit tips
pix([(13, 7)], ANT, mirror=False)    # highlight on the near trunk

# ================================================================ mushroom
# Cap overhangs the right shoulder; stem roots into the dome at y=14.
pix([(22, 13), (22, 14)], STEM, mirror=False)
pix([(23, 13), (23, 14)], STEM_D, mirror=False)

rows([(8, 22, 24)], OUT)
rows([(9, 22, 24)], MUSH)
rows([(10, 21, 25)], MUSH)
rows([(11, 20, 26)], MUSH)
rows([(12, 20, 26)], MUSH_D)
pix([(21, 9), (25, 9), (20, 10), (26, 10), (19, 11), (27, 11),
     (19, 12), (27, 12),
     (20, 13), (21, 13), (24, 13), (25, 13), (26, 13),
     (21, 14), (24, 14)], OUT, mirror=False)
pix([(23, 9), (21, 11), (25, 11), (22, 10)], MUSH_S, mirror=False)

# ================================================================ face
# sockets, then glowing pupils inside them
pix([(10, 15), (11, 15), (12, 15), (13, 15),
     (9, 16), (9, 17), (9, 18),
     (10, 19), (11, 19), (12, 19), (13, 19),
     (14, 16), (14, 17), (14, 18)], OUT)
rows([(16, 10, 13), (17, 10, 13), (18, 10, 13)], EYE_G)
rows([(16, 18, 21), (17, 18, 21), (18, 18, 21)], EYE_G)
pix([(11, 17), (12, 17)], EYE_C)

# smile: one clear row below the sockets so it never merges with them
pix([(13, 21)], OUT)
pix([(14, 22), (15, 22)], OUT)

# moss tuft where the mushroom stem meets the dome
pix([(21, 15), (24, 15)], MOSS, mirror=False)
pix([(22, 15)], MOSS_D, mirror=False)

view(c)
finish(c)
