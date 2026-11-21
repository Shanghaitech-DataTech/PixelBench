c = new_canvas(64, 64, name="offshore-wind-maintenance")

# ---------------- sky ----------------
sky = [
    (0, 5, "#3f74ad"),
    (6, 11, "#5286bd"),
    (12, 17, "#6798cc"),
    (18, 23, "#7ca9d9"),
    (24, 28, "#93badf"),
    (29, 33, "#aacbe8"),
    (34, 37, "#c3dcf0"),
    (38, 38, "#b9d6ea"),   # haze at horizon
]
for y0, y1, col in sky:
    c.rect(0, y0, 64, y1 - y0 + 1, col)

# clouds
def cloud(x, y, w):
    c.rect(x + 2, y, w - 4, 1, "#f2f8fc")
    c.rect(x, y + 1, w, 2, "#f2f8fc")
    c.rect(x + 1, y + 3, w - 2, 1, "#dcebf5")
cloud(5, 7, 11)
cloud(44, 5, 12)
cloud(26, 13, 8)

# birds
BIRD = "#3d5468"
for bx, by in ((17, 10), (23, 14), (52, 12)):
    c.set(bx, by + 1, BIRD); c.set(bx + 1, by, BIRD); c.set(bx + 2, by + 1, BIRD)

# ---------------- sea ----------------
sea = [
    (39, 41, "#7aa8c6"),
    (42, 46, "#5b8fb4"),
    (47, 52, "#42749c"),
    (53, 58, "#315d85"),
    (59, 63, "#24496e"),
]
for y0, y1, col in sea:
    c.rect(0, y0, 64, y1 - y0 + 1, col)

# wave crests
waves = [
    (40, "#a9cbde", [(3, 6), (14, 5), (25, 4), (55, 6)]),
    (43, "#8fbcd4", [(7, 5), (19, 6), (36, 5), (50, 4)]),
    (46, "#7aa9c6", [(2, 4), (12, 6), (28, 5), (58, 4)]),
    (49, "#6b9cbb", [(6, 6), (21, 4), (33, 6), (52, 5)]),
    (52, "#5d8fae", [(3, 5), (16, 6), (40, 5), (56, 6)]),
    (55, "#4f81a0", [(9, 6), (24, 5), (46, 6), (60, 3)]),
    (58, "#447394", [(4, 6), (19, 5), (35, 6), (53, 5)]),
    (61, "#3a6586", [(11, 6), (28, 5), (48, 6)]),
]
for y, col, dashes in waves:
    for x0, ln in dashes:
        c.rect(x0, y, ln, 1, col)

# ---------------- distant turbines ----------------
DIST = "#7e96ab"
def dist_turbine(x, h, bl):
    base = 38
    c.line(x, base, x, base - h, DIST)          # tower
    hx, hy = x, base - h
    c.set(hx - 1, hy, DIST)                     # nacelle
    c.line(hx, hy, hx, hy - bl, DIST)           # blade up
    c.line(hx, hy, hx - bl + 1, hy + (bl * 2) // 3, DIST)   # blade low-left
    c.line(hx, hy, hx + bl - 1, hy + (bl * 2) // 3, DIST)   # blade low-right
dist_turbine(12, 11, 5)
dist_turbine(22, 8, 4)


# ---------------- main turbine tower ----------------
for y in range(0, 39):
    off = (3 * y) // 38
    L, R = 42 - off, 44 + off
    c.set(L, y, "#ccd5db")
    for x in range(L + 1, R):
        c.set(x, y, "#aeb8c0")
    c.set(R, y, "#87919a")

# ---------------- maintenance platform ----------------
c.rect(29, 30, 28, 1, "#b9c2c9")   # deck top highlight
c.rect(29, 31, 28, 1, "#7d868e")   # deck face
c.rect(29, 32, 28, 1, "#59626a")   # deck underside
# railings (gap in the middle where the ladder is)
RAIL = "#8d979f"
c.rect(29, 26, 9, 1, RAIL)
for px in (29, 33, 37):
    c.rect(px, 26, 1, 4, RAIL)
c.rect(47, 26, 10, 1, RAIL)
for px in (47, 52, 56):
    c.rect(px, 26, 1, 4, RAIL)
# boat-landing fenders (rubber) flanking the tower below the deck
FEND = "#333b42"
c.rect(37, 33, 2, 6, FEND)
c.rect(46, 33, 2, 6, FEND)

# ---------------- tower ladder ----------------
LAD = "#3f4850"
c.rect(41, 16, 1, 14, LAD)         # stile left
c.rect(44, 16, 1, 14, LAD)         # stile right
for ry in (17, 20, 23, 26, 29):
    c.rect(42, ry, 2, 1, LAD)      # rungs

# ---------------- technician climbing ----------------
HELM = "#f5c531"
VEST = "#e2661f"
SKIN = "#d9a878"
DARK = "#2e3742"
c.set(42, 17, HELM); c.set(43, 17, HELM)          # helmet
c.set(42, 18, SKIN); c.set(43, 18, HELM)          # face + helmet back
c.set(41, 18, DARK)                               # left hand gripping stile
c.rect(41, 19, 4, 1, VEST)                        # shoulders
c.rect(41, 20, 4, 1, VEST)
c.set(44, 21, DARK)                               # right hand on stile
c.rect(41, 22, 4, 1, HELM)                        # hi-vis stripe
c.rect(41, 23, 4, 1, VEST)
c.rect(41, 24, 4, 1, DARK)                        # hips
c.set(41, 25, DARK); c.set(44, 25, DARK)          # legs
c.set(41, 26, DARK); c.set(44, 26, DARK)          # feet on rung

# ---------------- waterline foam + reflection ----------------
FOAM = "#e6f2f8"
for x, y in [(36, 39), (38, 39), (40, 40), (43, 39), (45, 40),
             (47, 39), (48, 40), (35, 40), (41, 41), (46, 41)]:
    c.set(x, y, FOAM)
REFL = "#39678f"
for y, x0, ln in [(41, 40, 4), (43, 41, 4), (45, 40, 5),
                  (47, 41, 4), (49, 40, 5), (51, 42, 3)]:
    c.rect(x0, y, ln, 1, REFL)

print(c.stats_text())
finish(c)
