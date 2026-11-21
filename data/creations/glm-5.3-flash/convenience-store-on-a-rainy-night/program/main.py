"""Convenience store on a rainy night - 64x64 pixel art."""

import random

c = new_canvas(64, 64, background="#0d1022", name="rainy_store")

# ------------------------------------------------------------------ night sky
c.rect(0, 10, 64, 4, "#131833")          # faint lift near the horizon

# neighbouring buildings, dark against the sky
c.rect(0, 8, 6, 38, "#141830")
c.rect(58, 10, 6, 36, "#141830")
for x, y, colr in ((2, 14, "#31406b"), (4, 20, "#31406b"), (1, 27, "#8a6a30"),
                   (3, 34, "#31406b"), (5, 40, "#31406b"), (60, 16, "#31406b"),
                   (62, 22, "#8a6a30"), (59, 29, "#31406b"), (61, 36, "#31406b")):
    c.set(x, y, colr)

# ------------------------------------------------------------------ the store
c.rect(6, 12, 52, 34, "#383e52")         # wall
c.rect(6, 12, 52, 2, "#262c40")          # parapet
c.rect(6, 12, 52, 1, "#3d4660")          # parapet cap
c.rect(6, 14, 52, 7, "#1b2030")          # sign band
c.rect(6, 21, 52, 1, "#3d4660")          # ledge

# lit sign panel - abstract marks only, no letters, no logos
c.rect(19, 14, 26, 7, "#6b5a2e")
c.rect(20, 15, 24, 5, "#ffd97a")
c.rect(23, 17, 5, 2, "#b57e2e")
c.rect(30, 17, 7, 2, "#b57e2e")
c.rect(39, 17, 3, 2, "#b57e2e")

# frames
c.rect(8, 22, 20, 20, "#23283a")         # left window
c.rect(36, 22, 20, 20, "#23283a")        # right window
c.rect(28, 22, 8, 24, "#1a1e2c")         # door

# left window: bright interior, shelves, counter, clerk
c.rect(9, 23, 18, 18, "#ffd97a")
c.rect(9, 23, 18, 3, "#fff3c4")
c.rect(9, 26, 18, 6, "#ffe9a8")
c.rect(9, 36, 18, 5, "#e8b055")
c.rect(10, 24, 16, 1, "#fffbe6")         # ceiling tube

goods = ("#b5433a", "#5ab0e0", "#3f8f5f", "#e8e4d8", "#b57e2e")
for row, y in enumerate((28, 32, 36)):
    c.rect(10, y, 7, 1, "#6b4a2a")
    for i, x in enumerate(range(10, 17)):
        c.set(x, y - 1, goods[(i + 2 * row) % 5])

c.rect(19, 33, 7, 1, "#5a3f28")          # counter
c.rect(19, 34, 7, 3, "#6b4a2a")
c.rect(21, 29, 2, 2, "#3a2a1c")          # clerk
c.rect(20, 31, 3, 2, "#3a2a1c")
c.rect(24, 31, 2, 2, "#9aa3b8")          # till

# right window: drink cooler glowing cool white
c.rect(37, 23, 18, 18, "#ffd97a")
c.rect(37, 23, 18, 3, "#fff3c4")
c.rect(37, 26, 18, 6, "#ffe9a8")
c.rect(37, 36, 18, 5, "#e8b055")
c.rect(38, 24, 16, 1, "#fffbe6")

c.rect(39, 26, 8, 12, "#cfe8ff")
c.rect(39, 29, 8, 1, "#9fc4e8")
c.rect(39, 33, 8, 1, "#9fc4e8")
bottles = ("#b5433a", "#5ab0e0", "#3f8f5f", "#e8e4d8", "#b5433a", "#5ab0e0")
for row, y in enumerate((28, 32, 36)):
    for i, x in enumerate(range(40, 46)):
        c.set(x, y, bottles[(i + row) % 6])
c.rect(46, 26, 1, 12, "#e8e4d8")

for row, y in enumerate((30, 35)):
    c.rect(48, y, 6, 1, "#6b4a2a")
    for i, x in enumerate(range(48, 54)):
        c.set(x, y - 1, goods[(i + 3 * row) % 5])

# door glass
c.rect(29, 23, 6, 21, "#ffe9a8")
c.rect(29, 23, 6, 2, "#fff3c4")
c.rect(29, 44, 6, 2, "#23283a")          # bottom rail

# striped awning over the entrance
for i, x in enumerate(range(26, 38, 2)):
    c.rect(x, 21, 2, 3, "#b5433a" if i % 2 == 0 else "#e8e4d8")
for i, x in enumerate(range(26, 38, 2)):
    if i % 2 == 0:
        c.rect(x, 24, 2, 1, "#b5433a")
c.rect(29, 25, 6, 1, "#e8b055")          # shadow on the door glass

# ------------------------------------------------------------------ wet ground
c.rect(0, 46, 64, 7, "#3f455a")          # sidewalk
c.rect(0, 49, 64, 1, "#363c50")
for x in (12, 28, 44, 60):
    c.line(x, 46, x, 52, "#363c50")
c.rect(0, 53, 64, 1, "#565d78")          # curb
c.rect(0, 54, 64, 1, "#3a4056")
c.rect(0, 55, 64, 9, "#1c2133")          # road
for x in range(2, 64, 9):
    c.rect(x, 60, 4, 1, "#3a4056")       # worn centre line

c.rect(26, 46, 12, 2, "#5a6076")         # doorstep
c.rect(26, 47, 12, 1, "#4a5066")

# warm light spilling onto the wet pavement
c.rect(27, 48, 10, 1, "#6b5a2e")
c.rect(28, 49, 8, 1, "#6b5a2e")
for x, ln, colr in ((10, 4, "#6b5a2e"), (12, 5, "#8a6a30"), (14, 3, "#a87b32"),
                    (17, 5, "#8a6a30"), (20, 4, "#a87b32"), (23, 5, "#6b5a2e"),
                    (25, 3, "#8a6a30")):
    c.rect(x, 46, 1, ln, colr)
for x, ln in ((29, 4), (31, 5), (33, 4)):
    c.rect(x, 48, 1, ln, "#a87b32")
for x, ln, colr in ((38, 4, "#8a6a30"), (40, 5, "#5a6a94"), (43, 4, "#8a6a30"),
                    (46, 5, "#a87b32"), (49, 4, "#5a6a94"), (52, 5, "#8a6a30")):
    c.rect(x, 46, 1, ln, colr)

# ------------------------------------------------------------------ puddles
c.ellipse(19, 59, 13, 3, "#2a3554")
c.rect(12, 57, 14, 1, "#31406b")
for x, y, ln, colr in ((9, 58, 2, "#8a6224"), (11, 57, 3, "#b57e2e"), (13, 58, 3, "#e8b055"),
                       (16, 57, 4, "#b57e2e"), (19, 58, 3, "#e8b055"), (21, 57, 2, "#b57e2e"),
                       (24, 58, 3, "#8a6224"), (27, 58, 2, "#6b5a2e")):
    c.rect(x, y, 1, ln, colr)

c.ellipse(47, 58, 9, 2, "#2a3554")
for x, y, ln, colr in ((40, 58, 2, "#5a6a94"), (43, 57, 2, "#8a6a30"), (46, 58, 2, "#b57e2e"),
                       (49, 57, 2, "#8a6224"), (52, 58, 2, "#5a6a94")):
    c.rect(x, y, 1, ln, colr)

c.ellipse(5, 50, 4, 1, "#2a3554")
c.rect(4, 50, 2, 1, "#8a6a30")
c.ellipse(52, 51, 5, 1, "#2a3554")
c.rect(51, 51, 2, 1, "#5a6a94")

for x, y in ((30, 57), (57, 61), (10, 61), (50, 62), (35, 55)):
    c.circle(x, y, 1, "#31406b", fill=False)      # raindrop ripples
for x, y in ((7, 54), (24, 53), (36, 55), (52, 55), (61, 57),
             (16, 55), (44, 53), (3, 58), (59, 62)):
    c.set(x, y, "#5a6a94")                         # splash flecks

# ------------------------------------------------------------------ umbrella rack
c.line(39, 47, 39, 34, "#7a6a9a")        # shafts first, bin over their feet
c.line(42, 47, 42, 37, "#9a8a6a")
c.rect(38, 46, 5, 4, "#2e2638")
c.rect(38, 46, 5, 1, "#4a3f5a")
c.rect(37, 50, 7, 1, "#313850")          # bin shadow on the wet pavement
c.set(39, 33, "#e8e4d8")                 # ferrule
c.rect(38, 34, 3, 1, "#b5433a")          # canopy 1
c.rect(37, 35, 5, 1, "#b5433a")
c.set(42, 35, "#e8e4d8")
c.rect(41, 36, 3, 1, "#5ab0e0")          # canopy 2
c.line(44, 49, 46, 38, "#3f8f5f")        # one leaning on the wall
c.set(46, 37, "#e8e4d8")
c.set(44, 49, "#151824")

# ------------------------------------------------------------------ parked bicycle
c.circle(12, 49, 3, "#151824")
c.circle(21, 49, 3, "#151824")
c.set(12, 49, "#9aa3b8")
c.set(21, 49, "#9aa3b8")
c.line(12, 49, 16, 44, "#b5433a")
c.line(16, 44, 20, 44, "#b5433a")
c.line(20, 44, 21, 49, "#b5433a")
c.line(12, 49, 17, 48, "#b5433a")
c.line(17, 48, 16, 44, "#b5433a")
c.set(17, 48, "#151824")                 # crank
c.rect(15, 43, 3, 1, "#151824")          # saddle
c.line(20, 44, 22, 42, "#9aa3b8")        # handlebar


# ------------------------------------------------------------------ person entering
def person_shape(colr, dx=0, dy=0):
    c.circle(31 + dx, 29 + dy, 2, colr)          # hood
    c.rect(29 + dx, 32 + dy, 5, 6, colr)         # coat
    c.rect(28 + dx, 37 + dy, 7, 3, colr)         # hem flare
    c.rect(30 + dx, 40 + dy, 1, 4, colr)         # legs
    c.rect(32 + dx, 40 + dy, 1, 4, colr)
    c.rect(29 + dx, 44 + dy, 2, 1, colr)         # shoes
    c.rect(32 + dx, 44 + dy, 2, 1, colr)


for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    person_shape("#6b4a2a", dx, dy)              # dark rim so the coat reads
person_shape("#f2c744")
c.rect(29, 31, 5, 1, "#c79426")                  # hood rim
c.rect(33, 32, 1, 6, "#c79426")                  # side shade
c.rect(28, 39, 7, 1, "#c79426")                  # hem shadow
c.set(29, 33, "#ffe08a")
c.set(30, 32, "#ffe08a")
c.set(31, 34, "#fff3c4")                         # rain beads on the coat
c.set(32, 37, "#fff3c4")
c.rect(30, 40, 1, 4, "#1a1e2c")
c.rect(32, 40, 1, 4, "#1a1e2c")
c.rect(29, 44, 2, 1, "#151824")
c.rect(32, 44, 2, 1, "#151824")
c.line(34, 34, 34, 44, "#4a5578")                # furled umbrella, point down
c.set(34, 33, "#6b4a2a")
c.set(34, 36, "#c79426")                         # hand
c.set(34, 45, "#e8e4d8")                         # ferrule

# ------------------------------------------------------------------ rain
random.seed(11)


def lum(x, y):
    idx = c.get(x, y)
    if idx is None or idx < 0:
        return 0.0
    r, g, b, a = c.palette()[idx]["rgba"]
    return (0.3 * r + 0.6 * g + 0.1 * b) * (a / 255.0)


for i in range(120):
    x = random.randrange(2, 65)
    y = random.randrange(-4, 58)
    ln = random.choice((3, 4, 5, 6))
    mx = min(63, max(0, x - 1))
    my = min(63, max(0, y + ln // 2))
    if 26 <= mx <= 37 and 22 <= my <= 45:
        continue                                 # sheltered under the awning
    L = lum(mx, my)
    colr = "#4a5578" if L > 150 else ("#7688b3" if L > 60 else "#4d5d85")
    c.line(x, y, x - 2, y + ln, colr)

for i in range(12):                              # longer gusts up in the sky
    x = random.randrange(2, 65)
    y = random.randrange(0, 8)
    c.line(x, y, x - 2, y + 7, "#7688b3")

# ------------------------------------------------------------------ report
print(c.stats_text())
print("--- door / person ---")
print(c.matrix_text(region=(26, 20, 40, 48)))
print("--- bike ---")
print(c.matrix_text(region=(6, 40, 26, 54)))

save("rainy_convenience_store", c)
finish(c)
