# Modern city bus - 64x32 side-view sprite, transparent background
c = new_canvas(64, 32, name="bus")

# ---------------------------------------------------------------- palette
OUTLINE   = "#1b2230"
BODY_HI   = "#f2f6fa"
BODY      = "#dde5ee"
BODY_SH   = "#b9c6d3"
BAND      = "#22303d"
ACCENT    = "#2f80b8"
ACCENT_DK = "#1d5c8a"
SKIRT     = "#5a6774"
BUMPER    = "#39424e"
GLASS     = "#2b4a5f"
GLASS_HI  = "#5b8ca6"
GLASS_HI2 = "#9acbe0"
DOOR      = "#c9d4df"
DOOR_DK   = "#8b98a6"
TYRE      = "#22262e"
TYRE_HI   = "#3d4552"
HUB       = "#a9b5c1"
HUB_DK    = "#6b7885"
HUB_HI    = "#e6ecf2"
LAMP      = "#ffd75e"
LAMP_HI   = "#fff4c9"
TAIL      = "#e04b3a"
ARCH      = "#141a24"
DISP_BG   = "#12161f"
DISP_LED  = "#ffb02e"
AMBER     = "#f5a623"

# ---------------------------------------------------------------- silhouette
ROWS = {
    3:  (9, 54),
    4:  (6, 56),
    5:  (4, 58),
    6:  (3, 59),
    7:  (3, 60),
    8:  (2, 61),
    9:  (2, 61),
    10: (2, 61),
    11: (2, 61),
    12: (2, 61),
    13: (2, 61),
    14: (2, 61),
    15: (2, 61),
    16: (2, 61),
    17: (2, 61),
    18: (2, 61),
    19: (2, 61),
    20: (2, 61),
    21: (3, 60),
    22: (4, 59),
}


def base(y):
    if y <= 4:
        return BODY_HI
    if y <= 6:
        return BODY
    if y <= 15:
        return BAND
    if y == 16:
        return BODY_SH
    if y <= 18:
        return ACCENT
    if y == 19:
        return ACCENT_DK
    return SKIRT


for y, (x0, x1) in ROWS.items():
    c.line(x0, y, x1, y, base(y))

c.outline(OUTLINE)

# ---------------------------------------------------------------- helpers
def glass_pane(x0, x1, y0=8, y1=14):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, GLASS)
    for y in range(y0, y1 + 1):
        d = y1 - y
        for xx, col in ((x0 + d - 1, GLASS_HI), (x0 + d, GLASS_HI),
                        (x0 + d + 2, GLASS_HI2)):
            if x0 <= xx <= x1:
                c.set(xx, y, col)


def door(d0):
    """double-leaf door, 9 px wide, header at y=7, threshold at y=21"""
    c.rect(d0, 7, 9, 15, OUTLINE)          # y = 7..21 frame
    for lx in (d0 + 1, d0 + 5):            # two 3px leaves, seam at d0+4
        c.rect(lx, 8, 3, 7, GLASS)         # door glass y = 8..14
        c.rect(lx, 15, 3, 5, DOOR)         # lower panel y = 15..19
        c.rect(lx, 20, 3, 1, DOOR_DK)      # kick plate
    for y in range(8, 15):                 # glass reflection on each leaf
        d = 14 - y
        for lx in (d0 + 1, d0 + 5):
            for xx, col in ((lx + d - 1, GLASS_HI), (lx + d, GLASS_HI)):
                if lx <= xx <= lx + 2:
                    c.set(xx, y, col)


def wheel(cx):
    """9x8 rounded wheel, top row y=19, contact row y=26"""
    c.set(cx - 3, 19, ARCH)
    c.set(cx + 3, 19, ARCH)
    c.line(cx - 2, 19, cx + 2, 19, TYRE)
    for y in range(20, 25):
        c.line(cx - 4, y, cx + 4, y, TYRE)
    c.line(cx - 3, 25, cx + 3, 25, TYRE)
    c.line(cx - 2, 26, cx + 2, 26, TYRE)
    c.set(cx - 2, 20, TYRE_HI)
    c.set(cx - 3, 21, TYRE_HI)
    c.line(cx - 1, 21, cx + 1, 21, HUB)
    for y in (22, 23, 24):
        c.line(cx - 2, y, cx + 2, y, HUB)
    c.line(cx - 1, 25, cx + 1, 25, HUB)
    c.set(cx, 23, HUB_DK)
    c.set(cx - 1, 22, HUB_HI)
    c.set(cx + 1, 24, HUB_DK)


# ---------------------------------------------------------------- glazing
glass_pane(4, 10)      # rear window
glass_pane(12, 19)     # side window 1
glass_pane(31, 35)     # side window 2
glass_pane(47, 54)     # side window 3
c.rect(56, 8, 5, 7, GLASS)                 # windshield / driver glass
c.set(60, 8, BAND)                         # raked top corner
for y in range(8, 15):
    d = 14 - y
    for xx, col in ((56 + d - 1, GLASS_HI), (56 + d, GLASS_HI),
                    (56 + d + 2, GLASS_HI2)):
        if 56 <= xx <= 59:
            c.set(xx, y, col)

door(21)               # rear door
door(37)               # front door

# ---------------------------------------------------------------- roof unit
c.rect(21, 1, 14, 2, BODY_SH)
c.line(21, 1, 34, 1, OUTLINE)
c.line(21, 1, 21, 2, OUTLINE)
c.line(34, 1, 34, 2, OUTLINE)

# ---------------------------------------------------------------- route display
c.rect(48, 3, 10, 5, DISP_BG)              # x 48..57, y 3..7
# "1"
c.set(51, 3, DISP_LED)
c.set(50, 4, DISP_LED); c.set(51, 4, DISP_LED)
c.set(51, 5, DISP_LED)
c.set(51, 6, DISP_LED)
c.set(51, 7, DISP_LED)
# "2"
c.line(53, 3, 55, 3, DISP_LED)
c.set(55, 4, DISP_LED)
c.line(53, 5, 55, 5, DISP_LED)
c.set(53, 6, DISP_LED)
c.line(53, 7, 55, 7, DISP_LED)

# ---------------------------------------------------------------- lights
c.rect(58, 18, 3, 2, LAMP)                 # headlight
c.set(60, 18, LAMP_HI)
c.set(57, 18, AMBER)                       # front indicator
c.set(57, 19, OUTLINE)
c.rect(3, 17, 2, 2, TAIL)                  # tail light
c.set(3, 19, AMBER)
c.rect(3, 20, 4, 2, BUMPER)                # rear bumper
c.rect(56, 20, 5, 2, BUMPER)               # front bumper
c.line(56, 21, 60, 21, OUTLINE)
c.line(3, 21, 6, 21, OUTLINE)

# ---------------------------------------------------------------- wheels
wheel(16)
wheel(50)

# ---------------------------------------------------------------- mirror
c.rect(62, 5, 2, 4, OUTLINE)
c.set(63, 6, GLASS_HI)
c.set(63, 7, GLASS_HI)
c.set(62, 9, OUTLINE)
c.set(62, 10, OUTLINE)

# ---------------------------------------------------------------- body details
c.line(30, 16, 30, 19, BODY_SH)            # panel seam
c.line(46, 16, 46, 19, BODY_SH)
c.set(9, 17, BODY_SH)                      # fuel cap hint

save("city_bus", c)
print(view(c, scale=8, margin=1))
print(c.stats_text())
finish(c)
