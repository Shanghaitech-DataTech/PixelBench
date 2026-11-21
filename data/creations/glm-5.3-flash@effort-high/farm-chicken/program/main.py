from pixelbench_api import *

c = new_canvas(32, 32, name="chicken")

# warm muted palette
CREAM  = c.color("#F2E8D5", "cream")
WING   = c.color("#E6D8BE", "wing")
SHADE  = c.color("#D5C3A3", "shade")
OUT    = c.color("#7A4E33", "outline")
RED    = c.color("#C65B4E", "comb")
ORANGE = c.color("#E2913C", "beak")
LEG    = c.color("#D99A45", "legs")
EYE    = c.color("#3B2A1E", "eye")

# --- body (plump, rounded) ---
c.ellipse(16, 19, 9, 7, CREAM)          # main body blob
c.circle(10, 10, 5, CREAM)              # head

# --- tail: rounded plume curving up-right ---
c.ellipse(24, 12, 3, 5, CREAM)
c.ellipse(25, 10, 2, 3, CREAM)

# --- comb (drawn later, after outline, so it stays chunky) ---

# --- beak (pointing left) ---
c.poly([(5, 9), (1, 11), (5, 13)], ORANGE)

# --- wattle ---
c.circle(7, 15, 1, RED)

# --- eye ---
c.set(8, 9, EYE)
c.set(9, 9, EYE)
c.set(8, 10, EYE)

# --- wing (soft rounded, on body) ---
c.ellipse(18, 18, 5, 4, WING)
c.ellipse(18, 18, 5, 4, SHADE, fill=False)

# --- belly shading ---
for x in range(11, 22):
    c.set(x, 25, SHADE)
c.set(10, 24, SHADE)
c.set(22, 24, SHADE)

# --- tail shading ---
c.line(25, 15, 26, 11, SHADE)

# --- legs and feet ---
c.line(14, 25, 14, 27, LEG)
c.line(12, 28, 16, 28, LEG)
c.line(19, 25, 19, 27, LEG)
c.line(17, 28, 21, 28, LEG)
c.set(15, 27, LEG)
c.set(18, 27, LEG)

# --- outline everything that touches transparency ---
c.outline(OUT)
# keep legs and feet warm orange after outlining
c.line(14, 25, 14, 27, LEG)
c.line(12, 28, 16, 28, LEG)
c.line(19, 25, 19, 27, LEG)
c.line(17, 28, 21, 28, LEG)
c.set(15, 27, LEG)
c.set(18, 27, LEG)

# --- comb: chunky red crest drawn after outline so it keeps its shape ---
COMB = [(7, 4), (8, 3), (9, 4), (10, 3), (11, 4), (12, 4),
        (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5),
        (8, 6), (9, 6), (10, 6), (11, 6), (12, 6)]
for (x, y) in COMB:
    c.set(x, y, RED)
c.set(8, 4, RED)
c.set(10, 4, RED)
# darker bottom edge of comb where it meets the head
for x in (8, 9, 10, 11, 12):
    c.set(x, 6, SHADE)
c.set(7, 6, SHADE)

# --- wattle: redraw after outline so it shows ---
c.circle(7, 15, 1, RED)

print(c.stats_text())
print(c.matrix_text())

finish(c)
