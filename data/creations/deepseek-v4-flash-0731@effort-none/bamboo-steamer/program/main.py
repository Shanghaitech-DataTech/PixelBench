from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="steamer")

# Palette
BROWN_D = "#5b3a1e"
BROWN = "#8b5e34"
BROWN_L = "#a8703a"
BAMBOO = "#c9a06c"
BAMBOO_L = "#dbb98a"
CREAM = "#e8d5a8"
CREAM_D = "#dcc89a"
DUMPLING = "#f5e6c8"
DUMPLING_SH = "#d8b890"
STEAM = "#ffffff"
STEAM_D = "#e8e8e8"

# === STEAMER BODY ===
# Bottom base (slightly wider)
c.ellipse(16, 28, 13, 3, BROWN_D, fill=True)
# Body wall
c.rect(3, 13, 26, 15, BROWN, fill=True)
# Bottom base lip
c.ellipse(16, 29, 13, 2, BROWN_D, fill=True)
# Top rim (outer edge of basket opening)
c.ellipse(16, 13, 12, 4, BROWN_D, fill=True)
# Inner platform where dumplings sit
c.ellipse(16, 13, 10, 3, CREAM, fill=True)
# Inner ring detail line
c.ellipse(16, 13, 10, 3, CREAM_D, fill=False)

# Bamboo ring texture on the body walls
for y in range(17, 28, 3):
    c.ellipse(16, y, 12, 2, BROWN_D, fill=False)

# Vertical bamboo slat lines
for x in range(5, 28, 2):
    c.line(x, 15, x, 27, BROWN_D)

# === DUMPLINGS (three clearly shaped, sitting in the opening) ===

# Dumpling 1 (left)
c.ellipse(10, 11, 3, 2, DUMPLING_SH, fill=True)
c.ellipse(10, 9, 3, 2, DUMPLING, fill=True)
# Pleat folds
c.line(8, 8, 8, 11, DUMPLING_SH)
c.line(10, 8, 10, 11, DUMPLING_SH)
c.line(12, 8, 12, 11, DUMPLING_SH)
# Top pinched crown
c.set(9, 7, DUMPLING)
c.set(10, 7, DUMPLING)
c.set(11, 7, DUMPLING)

# Dumpling 2 (middle)
c.ellipse(16, 12, 3, 2, DUMPLING_SH, fill=True)
c.ellipse(16, 10, 3, 2, DUMPLING, fill=True)
c.line(14, 9, 14, 12, DUMPLING_SH)
c.line(16, 9, 16, 12, DUMPLING_SH)
c.line(18, 9, 18, 12, DUMPLING_SH)
c.set(15, 8, DUMPLING)
c.set(16, 8, DUMPLING)
c.set(17, 8, DUMPLING)

# Dumpling 3 (right)
c.ellipse(21, 11, 3, 2, DUMPLING_SH, fill=True)
c.ellipse(21, 9, 3, 2, DUMPLING, fill=True)
c.line(19, 8, 19, 11, DUMPLING_SH)
c.line(21, 8, 21, 11, DUMPLING_SH)
c.line(23, 8, 23, 11, DUMPLING_SH)
c.set(20, 7, DUMPLING)
c.set(21, 7, DUMPLING)
c.set(22, 7, DUMPLING)

# === LID (partially open, tilted up and to the right) ===
# Lid body (elliptical dome tilted back/right)
c.ellipse(24, 6, 6, 4, BROWN_L, fill=True)
# Lid inner surface
c.ellipse(24, 6, 5, 3, BAMBOO, fill=True)
c.ellipse(24, 5, 3, 2, BAMBOO_L, fill=True)
# Lid edge highlight
c.ellipse(24, 6, 6, 4, BROWN, fill=False)
# Lid knob (handle on top)
c.circle(24, 2, 2, BROWN_D, fill=True)
c.circle(24, 2, 1, BROWN, fill=True)
c.set(24, 1, BROWN_L)

# === STEAM (small wisps rising from the opening) ===
c.set(5, 6, STEAM)
c.set(6, 5, STEAM)
c.set(7, 6, STEAM)
c.set(8, 4, STEAM)
c.set(9, 5, STEAM)
c.set(10, 3, STEAM)
c.set(11, 4, STEAM_D)
c.set(4, 7, STEAM)
c.set(12, 2, STEAM)
c.set(9, 2, STEAM)
c.set(13, 3, STEAM_D)
c.set(6, 3, STEAM_D)
c.set(11, 1, STEAM)

finish(c)
