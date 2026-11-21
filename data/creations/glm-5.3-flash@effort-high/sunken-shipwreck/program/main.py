import math

c = new_canvas(64, 64, name="sunken-shipwreck")

# ---------- palette ----------
W1 = c.color("#2a7ab5")   # shallow water
W2 = c.color("#22689e")
W3 = c.color("#1a5486")
W4 = c.color("#14416c")   # deep water
RAY = c.color("#3d8fc0")  # light shafts
SAND = c.color("#d8c188")
SAND_L = c.color("#e8d8a8")
SAND_D = c.color("#b99e66")
SAND_DD = c.color("#97794c")
HULL = c.color("#6e4b2e")
HULL_D = c.color("#4a3120")
HULL_L = c.color("#8a6440")
RUST = c.color("#96562f")
VERD = c.color("#5d8f72")
SAIL = c.color("#b9ae94")
SAIL_D = c.color("#8d846d")
FISH1 = c.color("#cfe0ec")
FISH2 = c.color("#8fb2ca")
FISH_E = c.color("#22384e")
CORAL = c.color("#e07a90")
CORAL_D = c.color("#b05570")
CORAL_L = c.color("#f4a6b6")
WEED = c.color("#3f9160")
WEED_D = c.color("#2c6b47")
BUB = c.color("#d6ecf7")
ROCK = c.color("#6b7484")
ROCK_D = c.color("#525a68")
STAR = c.color("#e0913f")

# ---------- water gradient ----------
for y in range(64):
    col = W1 if y < 15 else W2 if y < 31 else W3 if y < 47 else W4
    c.rect(0, y, 64, 1, col)
c.dither(0, 13, 64, 4, [W1, W2], pattern="checker")
c.dither(0, 29, 64, 4, [W2, W3], pattern="checker")
c.dither(0, 45, 64, 4, [W3, W4], pattern="checker")

# ---------- light shafts ----------
for x0, ln in [(8, 30), (21, 38), (35, 32), (49, 26)]:
    c.line(x0, 0, x0 + 6, ln, RAY)
    c.line(x0 + 2, 0, x0 + 8, ln, RAY)

# ---------- sunken hull (tilted, bow raised at right) ----------
pts = [(5, 49), (13, 46), (22, 43), (31, 40), (40, 37), (46, 34),
       (49, 33), (50, 37), (47, 43), (42, 49), (34, 55), (22, 60),
       (10, 62), (5, 62)]
c.poly(pts, HULL, fill=True)
# deck edge highlight + planks
c.line(5, 49, 46, 34, HULL_L)
c.line(7, 52, 46, 38, HULL_D)
c.line(10, 55, 46, 42, HULL_D)
c.line(14, 58, 40, 47, HULL_D)
# broken ribs sticking up from the deck
def deck_y(x):
    return 49 - int(round((x - 5) * 15 / 41.0))
for x, h in [(14, 5), (18, 6), (22, 4), (26, 3), (30, 3)]:
    dy = deck_y(x)
    c.line(x, dy + 1, x, dy - h, HULL_D)
# stern quarterdeck cabin
c.rect(5, 43, 7, 5, HULL)
c.line(5, 43, 11, 43, HULL_D)
c.line(5, 43, 5, 47, HULL_D)
c.rect(7, 45, 2, 2, HULL_D)
c.rect(9, 44, 2, 1, RUST)
# corrosion: rust and verdigris patches
c.rect(20, 45, 3, 2, RUST)
c.rect(33, 42, 2, 2, RUST)
c.set(38, 39, RUST)
c.set(39, 40, RUST)
c.rect(12, 51, 2, 2, RUST)
c.set(28, 43, VERD)
c.rect(35, 40, 2, 1, VERD)
c.set(17, 48, VERD)
c.set(24, 47, VERD)

# ---------- broken mast + yard + tattered sail ----------
c.line(24, 42, 16, 12, HULL_D)
c.line(25, 42, 17, 12, HULL_L)
c.set(16, 11, HULL_D)   # splintered top
c.set(15, 10, HULL_D)
c.line(8, 18, 26, 22, HULL_D)      # yard
c.poly([(10, 19), (24, 23), (23, 29), (19, 27), (16, 31), (13, 27), (10, 25)],
       SAIL, fill=True)            # torn sail
c.set(17, 25, W2)       # holes in the sail
c.set(14, 23, W2)
c.set(20, 26, W2)
# rigging
c.line(16, 12, 46, 34, SAIL_D)
c.line(16, 12, 8, 18, SAIL_D)

# ---------- sea floor ----------
def sand_top(x):
    return 53 + int(round(2 * math.sin((x - 3) / 7.0)))
for x in range(64):
    t = sand_top(x)
    c.rect(x, t, 1, 64 - t, SAND)
    c.set(x, t, SAND_L)
# dune shadow + speckle
c.rect(0, 60, 64, 4, SAND_D)
c.dither(0, 58, 64, 4, [SAND, SAND_D], pattern="checker")
c.rect(0, 62, 64, 2, SAND_DD)
for x, y in [(6, 55), (15, 57), (27, 56), (38, 58), (47, 55), (57, 57),
             (20, 60), (33, 61), (51, 60), (43, 62), (10, 61)]:
    c.set(x, y, SAND_DD)
# sand drift over the buried hull base
c.ellipse(24, 59, 15, 4, SAND)
c.ellipse(24, 60, 15, 3, SAND_D)
c.set(18, 57, SAND_L); c.set(28, 57, SAND_L); c.set(34, 58, SAND_L)

# ---------- rocks ----------
c.ellipse(44, 55, 3, 2, ROCK)
c.set(43, 54, "#8a93a2")
c.ellipse(3, 56, 3, 2, ROCK_D)
c.set(2, 55, ROCK)

# ---------- seaweed ----------
def weed(x, base, h, c1, c2):
    for i in range(h):
        y = base - i
        xx = x + int(round(1.6 * math.sin(i / 2.8)))
        c.set(xx, y, c1)
        c.set(xx + 1, y, c2)
weed(5, 55, 15, WEED, WEED_D)
weed(11, 54, 10, WEED_D, WEED)
weed(59, 54, 13, WEED, WEED_D)
weed(37, 56, 8, WEED_D, WEED)

# ---------- coral ----------
# branching coral, right
c.line(56, 58, 56, 50, CORAL_D)
c.line(57, 58, 57, 51, CORAL_D)
c.line(56, 52, 51, 46, CORAL)
c.line(57, 51, 61, 45, CORAL)
c.line(56, 55, 52, 52, CORAL)
c.set(51, 46, CORAL_L); c.set(61, 45, CORAL_L)
c.set(52, 52, CORAL_L); c.set(56, 50, CORAL_L)
# brain coral mound
c.ellipse(47, 58, 4, 3, CORAL)
c.set(46, 57, CORAL_D); c.set(48, 58, CORAL_D); c.set(45, 59, CORAL_D)
c.set(48, 56, CORAL_L)
# small coral, left
c.line(15, 54, 13, 48, CORAL_D)
c.line(15, 54, 17, 49, CORAL)
c.set(13, 48, CORAL_L); c.set(17, 49, CORAL_L)

# ---------- school of fish ----------
def fish(x, y, col, dark):
    for dx, dy in [(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2), (2, 2)]:
        c.set(x + dx, y + dy, col)
    c.set(x + 0, y + 1, dark)           # head / eye
    c.set(x + 4, y + 1, col)
    c.set(x + 5, y + 0, dark)           # tail fin
    c.set(x + 5, y + 2, dark)

school = [(34, 13), (41, 15), (47, 18), (52, 22), (55, 27), (54, 32),
          (48, 35), (41, 36)]
for i, (fx, fy) in enumerate(school):
    col = FISH1 if i % 2 == 0 else FISH2
    fish(fx, fy, col, FISH_E)

# ---------- bubbles ----------
for bx, by in [(18, 9), (19, 6), (17, 3), (30, 20), (31, 16), (52, 14),
               (53, 11), (58, 41), (59, 38), (44, 30), (12, 24)]:
    c.set(bx, by, BUB)

# ---------- starfish on the sand ----------
c.set(22, 61, STAR)
c.set(21, 61, STAR); c.set(23, 61, STAR)
c.set(22, 60, STAR); c.set(22, 62, STAR)

print(c.stats_text())
print("colors used:", c.stats()["colors_used"], "<= 86 limit")
save("sunken-shipwreck", c)
finish(c)
