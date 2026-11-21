import random
random.seed(7)

# 64x64 underwater sunken shipwreck scene
c = new_canvas(64, 64, name="sunken-shipwreck")

# --- palette ---
palette = [
    ("w0", "#2e86b5"), ("w1", "#256f9e"), ("w2", "#1c5987"),
    ("w3", "#14446e"), ("w4", "#0d3254"), ("w5", "#082440"),
    ("ray", "#3a8cc0"),
    ("sand", "#c2a06b"), ("sand_light", "#d8bb85"), ("sand_dark", "#a5834f"),
    ("wood", "#7a4a26"), ("wood_dark", "#4c2e16"), ("wood_light", "#9a6a3a"),
    ("rot", "#3a2a1a"), ("patina", "#4e7d5b"), ("patina_dark", "#2f5540"),
    ("hole", "#17100a"), ("mast", "#4a2c17"), ("mast_light", "#6b4423"),
    ("sail", "#c9b98f"),
    ("fish_silver", "#bfe3f0"), ("fish_orange", "#f0a45c"), ("fish_blue", "#7fb8d9"),
    ("fish_dark", "#1b2b38"),
    ("coral", "#e0596b"), ("coral_dark", "#a83a4d"), ("coral_light", "#f28a96"),
    ("seaweed1", "#3f7d4a"), ("seaweed2", "#2c5e38"), ("seaweed_light", "#6aa86b"),
    ("bubble", "#bfe8f0"),
]
for name, spec in palette:
    c.color(spec, name)

# --- underwater gradient background ---
bands = [("w0", 0), ("w1", 8), ("w2", 16), ("w3", 24), ("w4", 32), ("w5", 40)]
for i, (name, y0) in enumerate(bands):
    y1 = bands[i + 1][1] if i + 1 < len(bands) else 48
    c.rect(0, y0, 64, y1 - y0, name)

# dither the band boundaries for a softer gradient
for i in range(len(bands) - 1):
    y = bands[i + 1][1] - 1
    c.dither(0, y, 64, 2, [bands[i][0], bands[i + 1][0]], "checker")

# --- light shafts from the surface ---
c.poly([(3, 0), (15, 0), (33, 64), (19, 64)], "ray")
c.poly([(25, 0), (33, 0), (51, 64), (41, 64)], "ray")

# --- sunken wooden hull (side view, bow left, stern right) ---
hull_d = ("M 5 26 "
          "C 14 23, 28 24, 40 28 "
          "C 48 31, 54 32, 60 34 "
          "L 63 38 L 63 56 "
          "C 44 60, 20 59, 8 54 "
          "C 4 52, 3 48, 5 26 Z")
c.path(hull_d, "wood")

# sunlit deck rail highlight
c.path("M 5 26 C 14 23, 28 24, 40 28 C 48 31, 54 32, 60 34", "wood_light", fill=False)

# hull plank seams
for p in [
    "M 7 30 C 18 27, 34 29, 60 35",
    "M 6 36 C 18 33, 36 36, 62 40",
    "M 7 42 C 18 39, 38 42, 63 45",
]:
    c.path(p, "wood_dark", fill=False)

# hull ribs / frames
for r in [
    "M 16 25 C 18 35, 16 46, 20 55",
    "M 28 25 C 30 36, 28 48, 32 58",
    "M 40 28 C 42 38, 40 49, 44 59",
    "M 51 31 C 53 40, 51 50, 55 59",
]:
    c.path(r, "wood_dark", fill=False)

# corroded patina patches
c.ellipse(14, 36, 5, 3, "patina")
c.ellipse(14, 36, 2, 1, "patina_dark")
c.ellipse(48, 41, 6, 3, "patina")
c.ellipse(48, 41, 3, 1, "patina_dark")
c.ellipse(30, 33, 4, 2, "patina_dark")

# gaping hole in the hull side
c.ellipse(33, 40, 5, 4, "hole")
for hx, hy in [(27, 38), (28, 42), (29, 36), (37, 37), (38, 43), (36, 44), (33, 35), (34, 44), (31, 43)]:
    c.set(hx, hy, "rot")

# --- broken mast, yard and tattered sail ---
c.poly([(26, 26), (31, 24), (34, 8), (30, 9)], "mast")
c.poly([(20, 12), (41, 16), (41, 17), (20, 13)], "mast_light")

# jagged break at the top of the mast
c.set(34, 7, "mast_light")
c.set(33, 8, "mast_light")
c.set(32, 8, "mast")
c.set(31, 9, "mast_light")
c.set(30, 9, "mast")

# tattered sail hanging from the yard
c.poly([(30, 15), (38, 16), (40, 26), (36, 24), (37, 30), (33, 27), (34, 33), (30, 29)], "sail")

# broken bowsprit at the bow
c.poly([(5, 27), (6, 28), (2, 20), (1, 20)], "mast")
c.set(2, 20, "mast_light")

# broken stern cabin
c.rect(48, 27, 10, 7, "wood_dark")
c.rect(49, 28, 8, 4, "wood_light")
c.set(48, 26, "wood_light")
c.set(56, 26, "wood_light")

# --- sand buries the lower hull ---
sand_d = ("M 0 48 C 8 45, 16 46, 24 45 "
          "C 32 43, 40 45, 48 44 "
          "C 56 43, 60 45, 63 44 "
          "L 63 63 L 0 63 Z")
c.path(sand_d, "sand")

# sandy top highlight
c.path("M 1 48 C 9 45, 17 46, 25 45 C 33 43, 41 45, 49 44 C 57 43, 61 45, 63 44",
       "sand_light", fill=False)

# darker bottom of the seabed
c.rect(0, 57, 64, 7, "sand_dark")
c.dither(0, 54, 64, 4, ["sand", "sand_dark"], "checker")

# sand speckles
for _ in range(70):
    sx = random.randint(0, 63)
    sy = random.randint(46, 63)
    c.set(sx, sy, "sand_light" if random.random() < 0.5 else "sand_dark")

# --- seaweed ---
def seaweed(x, y, h, col, sway=2):
    d = f"M {x} {y} C {x - sway} {y - h // 3}, {x + sway} {y - 2 * h // 3}, {x} {y - h}"
    c.path(d, col, fill=False)
    d2 = f"M {x + 1} {y} C {x + 1 - sway} {y - h // 3}, {x + 1 + sway} {y - 2 * h // 3}, {x + 1} {y - h}"
    c.path(d2, col, fill=False)

seaweed(7, 47, 14, "seaweed1", 3)
seaweed(12, 46, 10, "seaweed2", 2)
seaweed(16, 45, 8, "seaweed1", 2)
seaweed(52, 45, 12, "seaweed2", 3)
seaweed(58, 46, 15, "seaweed1", 3)
seaweed(61, 45, 9, "seaweed2", 2)

# a strand of seaweed draped over the hull
seaweed(22, 46, 12, "seaweed2", 3)
seaweed(37, 45, 10, "seaweed1", 2)

# --- coral ---
def staghorn(x, y, col, tip, dark):
    c.line(x, y, x, y - 8, col)
    c.line(x + 1, y, x + 1, y - 7, col)
    c.line(x, y - 4, x - 4, y - 8, col)
    c.line(x, y - 4, x + 4, y - 8, col)
    c.set(x, y - 8, tip)
    c.set(x + 1, y - 7, tip)
    c.set(x - 4, y - 8, tip)
    c.set(x + 4, y - 8, tip)
    c.set(x, y, dark)
    c.set(x + 1, y, dark)

staghorn(6, 47, "coral", "coral_light", "coral_dark")
staghorn(19, 45, "coral", "coral_light", "coral_dark")
staghorn(57, 46, "coral", "coral_light", "coral_dark")

# brain-coral blob on the right
c.ellipse(48, 45, 6, 3, "coral")
c.ellipse(44, 44, 3, 2, "coral")
c.ellipse(52, 44, 3, 2, "coral")
c.ellipse(48, 43, 3, 2, "coral_light")
c.ellipse(44, 43, 1, 1, "coral_light")
c.ellipse(52, 43, 1, 1, "coral_light")

# --- bubbles rising from the wreck ---
for bx, by, r in [(31, 20, 0), (34, 17, 1), (28, 13, 0), (36, 10, 0), (32, 7, 1), (38, 5, 0)]:
    c.circle(bx, by, r, "bubble")

# --- school of fish swimming past ---
def fish(x, y, body, tail, eye):
    # small fish facing left: oval body + notched tail
    c.ellipse(x, y, 2, 1, body)
    c.poly([(x + 2, y), (x + 5, y - 2), (x + 5, y + 2)], tail)
    c.set(x - 1, y, eye)

school = [(9, 9), (15, 12), (21, 14), (27, 15), (33, 15), (39, 14), (45, 12), (51, 9)]
for i, (fx, fy) in enumerate(school):
    if i % 3 == 0:
        fish(fx, fy, "fish_silver", "fish_silver", "fish_dark")
    elif i % 3 == 1:
        fish(fx, fy, "fish_orange", "fish_orange", "fish_dark")
    else:
        fish(fx, fy, "fish_blue", "fish_blue", "fish_dark")

# a few more fish closer to the wreck
fish(44, 25, "fish_orange", "fish_orange", "fish_dark")
fish(50, 23, "fish_silver", "fish_silver", "fish_dark")
fish(56, 21, "fish_blue", "fish_blue", "fish_dark")

# --- inspect ---
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

finish(c)
