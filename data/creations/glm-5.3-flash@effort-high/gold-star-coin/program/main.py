from pixelbench_api import *

c = new_canvas(16, 16, name="gold-star-coin")

# Palette
DARK   = c.color("#8a5a00", "dark_gold")    # rim / shadow
GOLD   = c.color("#f0b429", "gold")         # coin face
LIGHT  = c.color("#ffd75e", "light_gold")   # highlight
STAR   = c.color("#fff3b0", "star")         # star symbol
WHITE  = c.color("#ffffff", "sparkle")      # sparkle

# Coin body: dark rim disc, then gold face
c.circle(7.5, 7.5, 7.5, DARK)
c.circle(7.5, 7.5, 6.0, GOLD)

# Five-pointed star, hand-placed rows (x offsets from 3, y from 4)
star_rows = {
    4: [4],
    5: [4],
    6: [3, 4, 5],
    7: list(range(0, 9)),
    8: list(range(1, 8)),
    9: list(range(2, 7)),
    10: list(range(2, 7)),
    11: [1, 2, 3, 5, 6, 7],
    12: [0, 1, 7, 8],
}
for y, xs in star_rows.items():
    for dx in xs:
        c.set(3 + dx, y, STAR)

# Highlight arc on the upper-left of the face
c.line(4, 3, 6, 2, LIGHT)
c.line(3, 4, 3, 6, LIGHT)
c.set(4, 4, LIGHT)

# Sparkle
c.set(11, 4, WHITE)

print(c.stats_text())
print(c.matrix_text())
finish(c)
