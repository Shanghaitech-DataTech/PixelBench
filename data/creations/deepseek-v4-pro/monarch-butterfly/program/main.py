from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="monarch")

# palette
orange = c.color("#e8790a", name="orange")
deep   = c.color("#c85a0a", name="deep")
black  = c.color("#221a12", name="black")
white  = c.color("#f6efe2", name="white")
yellow = c.color("#f7c94d", name="yellow")

# ---- left wing: orange fills with a thin black outline ----
fore = [(15, 6), (5, 2), (1, 6), (3, 12), (15, 12)]
hind = [(15, 13), (6, 13), (2, 19), (5, 27), (15, 25)]

c.poly(fore, orange)
c.poly(hind, orange)
c.poly(fore, black, fill=False)
c.poly(hind, black, fill=False)

# a few black veins
for x0, y0, x1, y1 in [
    (14, 7, 3, 5),
    (14, 10, 4, 11),
    (14, 16, 4, 17),
    (14, 21, 6, 24),
]:
    c.line(x0, y0, x1, y1, black)

# white spots along the dark margin
for x, y in [
    (5, 2), (4, 3), (3, 5), (2, 7), (2, 9), (3, 11), (3, 12),
    (6, 13), (5, 15), (3, 18), (2, 19), (3, 22), (4, 24),
    (5, 26), (6, 26), (7, 27),
]:
    c.set(x, y, white)

# ---- mirror left half onto the right half ----
sel = c.select(0, 0, 16, 32)
sel.flip("h").copy_to(16, 0, c)

# ---- body over the centre ----
c.rect(15, 4, 2, 22, black)          # head, thorax, abdomen
c.rect(15, 6, 2, 8, deep)            # thorax shade
c.line(15, 5, 13, 3, black)          # antennae
c.line(13, 3, 11, 1, black)
c.line(16, 5, 18, 3, black)
c.line(18, 3, 20, 1, black)
c.set(11, 1, black)
c.set(20, 1, black)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

save("monarch", c)
finish(c)
