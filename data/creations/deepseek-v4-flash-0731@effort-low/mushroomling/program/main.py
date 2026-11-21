from pixelbench_api import *

OUTLINE = (43, 43, 43)        # dark outline
RED     = (205, 55, 60)      # cap
WHITE   = (250, 250, 250)    # spots + eyes
CREAM   = (243, 219, 171)    # stalk / arms / legs

c = new_canvas(16, 16, name="mushroomling")

# --- Cap: red dome ---
c.ellipse(8, 4, 7, 4, RED, fill=True)

# White spots on cap (slightly below centre, away from both edges)
c.circle(4, 2, 1, WHITE)
c.circle(10, 2, 1, WHITE)
c.circle(7, 5, 1, WHITE)
c.circle(11, 5, 1, WHITE)
c.circle(6, 1, 1, WHITE)

# --- Body / stalk: cream ---
c.rect(5, 8, 6, 6, CREAM)

# Eyes: white with dark pupils
c.circle(6, 9, 1, WHITE)
c.circle(9, 9, 1, WHITE)
c.set(6, 9, OUTLINE)
c.set(9, 9, OUTLINE)

# Mouth
c.set(8, 11, OUTLINE)
c.set(7, 11, OUTLINE)
c.set(9, 11, OUTLINE)

# Stubby arms
c.rect(3, 10, 2, 2, CREAM)
c.rect(11, 10, 2, 2, CREAM)

# Stubby legs
c.rect(6, 13, 2, 2, CREAM)
c.rect(9, 13, 2, 2, CREAM)

# Dark outline around the whole creature
c.outline(OUTLINE)

print(c.stats_text())
print(c.matrix_text())

finish(c)
