# Stardew Valley style plump chicken, 32x32, gentle side view facing right.
# Warm muted palette, soft rounded shapes, transparent background.

OUT    = "#4a2e1e"   # soft dark brown outline
BODY   = "#f9edd8"   # warm cream
SHADE  = "#ecd3ab"   # tan shadow
WING   = "#e9cda1"   # wing tan
RED    = "#d95b4f"   # comb / wattle
ORANGE = "#eda23e"   # beak / feet
EYE    = "#2f1f16"

c = new_canvas(32, 32, name="chicken")

# ---- silhouette (cream shapes merge, then outlined in brown) ----
c.ellipse(15, 18, 9, 8, SHADE)   # under-mass: belly shadow peeks out at bottom
c.circle(7, 9, 3, BODY)          # tail upper feather bump
c.circle(6, 13, 2, BODY)         # tail lower feather bump
c.ellipse(15, 16, 9, 8, BODY)    # main plump body
c.circle(23, 9, 4, BODY)         # head
c.outline(OUT)

# ---- interior details ----
# wing: hand-placed teardrop rows; shade copy offset +1y for a soft lower rim
c.rect(12, 14, 5, 1, SHADE)
c.rect(11, 15, 7, 1, SHADE)
c.rect(10, 16, 8, 1, SHADE)
c.rect(10, 17, 8, 1, SHADE)
c.rect(10, 18, 7, 1, SHADE)
c.rect(11, 19, 5, 1, SHADE)
c.rect(12, 20, 2, 1, SHADE)
c.rect(12, 13, 5, 1, WING)
c.rect(11, 14, 7, 1, WING)
c.rect(10, 15, 8, 1, WING)
c.rect(10, 16, 8, 1, WING)
c.rect(10, 17, 7, 1, WING)
c.rect(11, 18, 5, 1, WING)
c.rect(12, 19, 2, 1, WING)
# eye
c.set(24, 9, EYE)

# ---- legs & feet (drawn over the body bottom) ----
c.rect(11, 24, 3, 5, OUT)
c.rect(12, 24, 1, 5, ORANGE)
c.rect(18, 24, 3, 5, OUT)
c.rect(19, 24, 1, 5, ORANGE)
c.rect(10, 28, 6, 2, OUT)
c.rect(11, 28, 4, 1, ORANGE)
c.rect(17, 28, 6, 2, OUT)
c.rect(18, 28, 4, 1, ORANGE)

# ---- comb (brown bumps, red hearts) ----
c.circle(21, 4, 2, OUT)
c.circle(23, 3, 2, OUT)
c.circle(25, 4, 2, OUT)
c.circle(21, 4, 1, RED)
c.circle(23, 3, 1, RED)
c.circle(25, 4, 1, RED)
c.rect(21, 5, 5, 1, RED)

# ---- beak ----
c.poly([(26, 8), (30, 10), (26, 12)], OUT)
c.poly([(27, 9), (29, 10), (27, 11)], ORANGE)

# ---- wattle ----
c.circle(27, 13, 1, RED)

# ---- stray pixel touch-ups ----
c.set(26, 12, OUT)    # close the gap between beak and head
c.set(15, 25, OUT)    # solid belly-outline row between the feet
c.set(7, 10, SHADE)   # feather accents on the tail bumps
c.set(6, 13, SHADE)

print(c.stats_text())
save("farm-chicken", c, indexed=True)
view(c)
finish(c)
