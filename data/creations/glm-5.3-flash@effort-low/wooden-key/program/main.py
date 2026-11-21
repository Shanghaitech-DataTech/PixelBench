from pixelbench_api import *

DARK = "#4a2f18"
MID  = "#8b5a2b"
LIGHT= "#c68e4f"

c = new_canvas(16, 16, name="wooden-key")

# --- bow: ring centred (5,7), radius 3 ---
c.circle(5, 7, 3, DARK, fill=True)
c.circle(5, 7, 1, None, fill=True)   # hole
# wood tone on the ring body
for (x, y) in [(3,6),(3,7),(3,8),(4,5),(5,4),(6,5),(7,6),(7,7),(7,8),(6,9),(5,10),(4,9)]:
    c.set(x, y, MID)
# highlight, upper-left
for (x, y) in [(4,5),(3,6),(4,6)]:
    c.set(x, y, LIGHT)

# --- shaft, rows 6-8, x 8..14 ---
c.rect(8, 6, 7, 3, DARK)
c.rect(8, 7, 7, 1, MID)
for x in range(9, 14):
    c.set(x, 6, MID)
    c.set(x, 8, MID)
c.set(9, 7, LIGHT)
c.set(14, 6, LIGHT)

# --- teeth ---
c.rect(11, 9, 1, 2, DARK); c.set(11, 10, MID)
c.rect(14, 9, 1, 2, DARK); c.set(14, 10, MID)

# --- grain details on shaft ---
c.set(12, 6, DARK)
c.set(13, 8, DARK)
c.set(10, 7, DARK)

print(c.stats_text())
print(c.matrix_text())
save("wooden-key", c)
finish(c)
