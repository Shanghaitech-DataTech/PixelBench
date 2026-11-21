c = new_canvas(32, 32, name="chicken")

# ---- warm muted palette ----
BODY   = c.color("#f8f1e6", "body")
BODY_S = c.color("#e6d9c3", "body_shade")
BODY_D = c.color("#cdbca1", "body_dark")
OUTL   = c.color("#6e5547", "outline")
OUTL_L = c.color("#8a6e5c", "outline_light")
COMB   = c.color("#c86355", "comb")
COMB_D = c.color("#9a3f35", "comb_dark")
BEAK   = c.color("#e8ad57", "beak")
BEAK_D = c.color("#bd8033", "beak_dark")
LEG    = c.color("#dca25a", "leg")
LEG_D  = c.color("#a9733a", "leg_dark")
EYE    = c.color("#3b2d28", "eye")
WING   = c.color("#e0cdb1", "wing")
WING_D = c.color("#b49c7e", "wing_dark")
BLUSH  = c.color("#e0a99c", "blush")


def rows(canvas, spans, col):
    for y, x0, x1 in spans:
        canvas.rect(x0, y, x1 - x0 + 1, 1, col)


# ---------- silhouette: head, neck, plump body, upswept tail ----------
SIL = [
    (3, 22, 25),
    (4, 21, 26),
    (5, 20, 27),
    (6, 20, 27),
    (7, 20, 27),
    (8, 20, 27),
    (9, 21, 26),
    (10, 20, 26),
    (11, 19, 26),
    (12, 16, 27),
    (13, 13, 27),
    (14, 10, 27),
    (15, 9, 27),
    (16, 8, 27),
    (17, 7, 27),
    (18, 7, 26),
    (19, 7, 26),
    (20, 8, 25),
    (21, 9, 24),
    (22, 11, 22),
    (23, 14, 19),
]
# tail plume rising up-left out of the back
TAILM = [
    (5, 5, 8),
    (6, 4, 9),
    (7, 3, 10),
    (8, 2, 11),
    (9, 2, 11),
    (10, 2, 12),
    (11, 3, 13),
    (12, 5, 14),
    (13, 8, 13),
]
rows(c, SIL, BODY)
rows(c, TAILM, BODY)

c.outline(OUTL)

# soften the lit top-left edges of head and tail
for x, y in [(22, 2), (21, 3), (20, 4), (5, 4), (6, 4), (7, 5), (4, 5)]:
    if c.get(x, y) == OUTL:
        c.set(x, y, OUTL_L)

# ---------- body shading: underside ----------
rows(c, [
    (20, 10, 24),
    (21, 11, 23),
    (22, 13, 21),
], BODY_S)
rows(c, [(22, 15, 19)], BODY_D)
# neck shadow under the head and chest curve
rows(c, [(11, 20, 23), (12, 17, 22)], BODY_S)

# ---------- tail feather separations ----------
c.line(5, 7, 11, 11, BODY_S)
c.line(4, 10, 10, 13, BODY_S)
c.line(6, 5, 9, 7, BODY_S)

# ---------- wing: rounded teardrop ----------
rows(c, [
    (14, 12, 16),
    (15, 11, 18),
    (16, 10, 19),
    (17, 10, 20),
    (18, 11, 20),
    (19, 13, 19),
], WING)
# feather edge along the bottom of the wing
rows(c, [
    (18, 12, 20),
    (19, 14, 19),
], WING_D)
# fold line along the top of the wing
c.line(12, 14, 16, 14, WING_D)
c.line(11, 15, 11, 15, WING_D)
# inner highlight so the wing stays soft
rows(c, [(15, 13, 17), (16, 12, 15)], BODY_S)
c.set(17, 16, BODY_S)

# ---------- breast feather hint ----------
c.set(25, 15, BODY_S)
c.set(25, 16, BODY_S)
c.set(24, 19, BODY_S)

# ---------- comb ----------
c.set(22, 1, COMB)
c.set(24, 1, COMB)
c.rect(21, 2, 5, 1, COMB)
c.set(21, 1, COMB_D)
c.set(23, 2, COMB_D)
c.set(25, 2, COMB_D)

# ---------- beak ----------
c.rect(28, 7, 3, 1, BEAK)
c.rect(28, 8, 2, 1, BEAK_D)

# ---------- wattle ----------
c.set(27, 9, COMB)
c.set(27, 10, COMB_D)

# ---------- face ----------
c.set(25, 6, EYE)
c.set(23, 4, BODY)
c.set(24, 8, BLUSH)

# ---------- legs ----------
for lx in (15, 19):
    c.rect(lx, 24, 1, 4, LEG)
    c.set(lx, 25, LEG_D)
    c.set(lx - 1, 28, LEG_D)
    c.set(lx, 28, LEG)
    c.set(lx + 1, 28, LEG_D)

view(c)
print(c.stats_text())
finish(c)
