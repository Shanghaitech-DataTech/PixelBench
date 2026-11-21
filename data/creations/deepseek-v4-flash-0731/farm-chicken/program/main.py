from pixelbench_api import new_canvas, finish

OUTLINE = "#6B4F3A"
BODY = "#F4E6C8"
BELLY = "#EAD7AE"
WING = "#E3C891"
TAIL = "#D5AF72"
TAIL_D = "#C49A5E"
COMB = "#D06E55"
BEAK = "#E8A04C"
LEG = "#DFA558"
EYE = "#4A3B2E"

c = new_canvas(32, 32)

# --- legs (behind the body) ---
c.rect(10, 24, 2, 6, LEG)
c.rect(17, 24, 2, 6, LEG)
c.rect(9, 29, 4, 2, LEG)
c.rect(16, 29, 4, 2, LEG)

# --- tail feathers at the back (left) ---
c.ellipse(6, 16, 4, 6, TAIL)
c.ellipse(8, 13, 2, 2, TAIL)
c.ellipse(5, 20, 3, 3, TAIL_D)

# --- plump body ---
c.ellipse(15, 18, 10, 8, BODY)

# --- soft belly shading ---
c.ellipse(14, 21, 5, 3, BELLY)

# --- wing ---
c.ellipse(14, 17, 5, 4, WING)

# --- head ---
c.circle(21, 11, 5, BODY)

# --- comb (rounded crest with a solid base) ---
c.circle(19, 4, 2, COMB)
c.circle(22, 2, 2, COMB)
c.circle(25, 4, 2, COMB)
c.rect(17, 5, 10, 2, COMB)

# --- beak ---
c.poly([(26, 10), (30, 12), (26, 14)], BEAK)

# --- wattle ---
c.ellipse(25, 15, 2, 1, COMB)

# --- gentle eye ---
c.set(24, 9, EYE)
c.set(25, 9, EYE)

# --- soft dark outline, Stardew style ---
c.outline(OUTLINE)

print(c.stats_text())
print(c.matrix_text((0, 0, 31, 31)))
finish(c)
