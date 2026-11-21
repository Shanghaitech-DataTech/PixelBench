# 64x64 skill icon set: 2x2 grid (fireball, ice shield, healing, lightning)
# Each icon is drawn on its own 32x32 canvas, then blitted into the 64x64 result.
# Shared style: 1px dark outline, 3-4 tone ramp per element, small sparkle accents.

DARK = "#191430"

# fire
F_SH = "#a1280f"; F_MID = "#e8541b"; F_LT = "#ffa32b"; F_HI = "#ffe27a"
# ice
I_SH = "#1d5b9a"; I_MID = "#3fa9dd"; I_LT = "#9ce8ff"; I_HI = "#eafcff"
# healing
H_SH = "#137a3d"; H_MID = "#31b95f"; H_LT = "#8ef2a8"; H_HI = "#ecfff2"
# lightning
L_SH = "#b86b09"; L_MID = "#f2b224"; L_LT = "#ffe873"; L_HI = "#fffce0"


def P(pts):
    d = "M %s %s " % (pts[0][0], pts[0][1])
    d += " ".join("L %s %s" % (x, y) for x, y in pts[1:])
    return d + " Z"


def poly_scale(pts, k, ctr=None):
    n = len(pts)
    if ctr is None:
        cx = sum(p[0] for p in pts) / n
        cy = sum(p[1] for p in pts) / n
    else:
        cx, cy = ctr
    return [(round(cx + (x - cx) * k, 2), round(cy + (y - cy) * k, 2)) for x, y in pts]


def flame(tipx, tipy, bx, by, w):
    cy = tipy + (by - tipy) * 0.5
    return ("M %s %s Q %s %s %s %s L %s %s Q %s %s %s %s Z" % (
        tipx, tipy,
        round(tipx - w * 1.55, 2), round(cy, 2), round(bx - w, 2), by,
        round(bx + w, 2), by,
        round(tipx + w * 1.55, 2), round(cy, 2), tipx, tipy))


def sparkle(c, cx, cy, colour, r=1):
    c.set(cx, cy, colour)
    for i in range(1, r + 1):
        c.set(cx + i, cy, colour)
        c.set(cx - i, cy, colour)
        c.set(cx, cy + i, colour)
        c.set(cx, cy - i, colour)


# ---------------------------------------------------------------- fireball
f = new_canvas(32, 32, name="fire")

flames = [(16, 2, 16.5, 13, 4.2), (8, 6, 12, 14, 3.8), (25, 8, 21, 14, 3.4)]
for tx, ty, bx, by, w in flames:
    f.path(flame(tx, ty, bx, by, w), F_MID, fill=True)
    f.path(flame(tx + (bx - tx) * 0.24, ty + (by - ty) * 0.36, bx, by - 1, w * 0.5),
           F_LT, fill=True)

# molten sphere
f.circle(16, 20, 9, F_SH)
f.circle(15, 20, 8, F_MID)
f.circle(13, 19, 6, F_LT)
f.circle(12, 18, 3, F_HI)
f.outline(DARK)
# accents drawn after the outline
sparkle(f, 27, 4, F_HI, r=1)
sparkle(f, 4, 25, F_HI, r=1)

# ---------------------------------------------------------------- ice shield
i = new_canvas(32, 32, name="ice")

# silhouette
i.path("M 16 2 L 26.5 7 L 26.5 15.5 Q 26.5 24 16 29.5 Q 5.5 24 5.5 15.5 L 5.5 7 Z",
       I_MID, fill=True)
# shadow rim (even-odd ring between the silhouette and an inner shield)
i.path("M 16 2 L 26.5 7 L 26.5 15.5 Q 26.5 24 16 29.5 Q 5.5 24 5.5 15.5 L 5.5 7 Z "
       "M 16 3.9 L 24.5 8.3 L 24.5 15.5 Q 24.5 22.2 16 27.4 Q 7.5 22.2 7.5 15.5 L 7.5 8.3 Z",
       I_SH, fill=True)
# light bevel, top-left
i.path("M 16 2 L 5.5 7 L 5.5 15.5 Q 5.5 17.5 6.2 19.6 L 8 18.8 "
       "Q 7.5 17.2 7.5 15.5 L 7.5 8.3 L 16 3.9 Z", I_LT, fill=True)
# snowflake emblem
i.line(16, 8.5, 16, 22, I_HI)
i.line(11, 11.5, 21, 18.5, I_HI)
i.line(21, 11.5, 11, 18.5, I_HI)
i.set(16, 7.5, I_HI); i.set(16, 23, I_HI)
i.set(15, 9.5, I_LT); i.set(17, 9.5, I_LT)
i.set(15, 21, I_LT); i.set(17, 21, I_LT)
i.set(10, 11, I_LT); i.set(22, 19, I_LT)
i.set(22, 11, I_LT); i.set(10, 19, I_LT)
i.outline(DARK)
sparkle(i, 26, 4, I_HI, r=1)
sparkle(i, 5, 25, I_HI, r=1)

# ---------------------------------------------------------------- healing
h = new_canvas(32, 32, name="heal")

h.rect(11, 4, 10, 24, H_MID)
h.rect(4, 11, 24, 10, H_MID)
# shadow faces (bottom + right)
h.rect(19, 4, 2, 7, H_SH)
h.rect(26, 11, 2, 10, H_SH)
h.rect(19, 21, 2, 7, H_SH)
h.rect(11, 26, 10, 2, H_SH)
h.rect(4, 19, 7, 2, H_SH)
h.rect(21, 19, 7, 2, H_SH)
# lit faces (top + left)
h.rect(11, 4, 10, 2, H_LT)
h.rect(11, 4, 2, 7, H_LT)
h.rect(4, 11, 2, 10, H_LT)
h.rect(4, 11, 7, 2, H_LT)
h.rect(21, 11, 7, 2, H_LT)
h.rect(11, 21, 2, 7, H_LT)
# brightest rim
h.rect(11, 4, 10, 1, H_HI)
h.rect(4, 11, 1, 10, H_HI)
h.outline(DARK)
sparkle(h, 26, 4, H_HI, r=1)
sparkle(h, 5, 25, H_HI, r=1)

# ---------------------------------------------------------------- lightning
l = new_canvas(32, 32, name="bolt")
bolt = [(16, 2), (3, 18), (11, 18), (8, 30), (29, 11), (20, 11), (26, 2)]
l.path(P(bolt), L_MID, fill=True)
l.path(P(poly_scale(bolt, 0.72, (16, 13))), L_LT, fill=True)
l.path(P(poly_scale(bolt, 0.44, (15, 12))), L_HI, fill=True)
l.path(P([(24.2, 4), (19.8, 10.6), (17.3, 10.6), (21.7, 4)]), L_SH, fill=True)
l.outline(DARK)
sparkle(l, 28, 4, L_HI, r=1)
sparkle(l, 5, 25, L_HI, r=1)

# ---------------------------------------------------------------- assemble
c = new_canvas(64, 64, name="skill_icons")
c.blit(f, 0, 0)
c.blit(i, 32, 0)
c.blit(h, 0, 32)
c.blit(l, 32, 32)

print(c.stats_text())
for lay in (f, i, h, l):
    print(lay.stats_text())
print("FULL"); print(c.matrix_text())

save("skill_icons", c)
finish(c)
