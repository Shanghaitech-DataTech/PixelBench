from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16, name="glow-jellyfish")

# palette
dark  = c.color((8, 18, 34))          # dark outline
glow_a = c.color((90, 200, 255, 24))  # outer halo
glow_b = c.color((130, 218, 255, 50)) # inner halo
low   = c.color((90, 185, 240, 115))  # bell shading
mid   = c.color((140, 218, 252, 145))
hi    = c.color((195, 245, 255, 172))
core  = c.color((235, 252, 255, 205)) # glowing core
tent  = c.color((165, 232, 255, 148))
spark = c.color((235, 250, 255, 160))

def row(y, xs, col):
    for x in xs:
        c.set(x, y, col)

# soft glow around the bell
c.circle(7, 5, 6, glow_a)
c.circle(7, 5, 4, glow_b)

# bell dome, dark outline ring + translucent body
c.set(7, 0, dark); c.set(8, 0, dark)
row(1, [6, 9], dark);   row(1, [7, 8], hi)
row(2, [5, 10], dark);  row(2, [6, 7], hi);  row(2, [8, 9], mid)
row(3, [4, 11], dark);  row(3, [5, 6, 7], hi);  row(3, [8, 9], mid);  row(3, [10], low)
row(4, [3, 12], dark);  row(4, [4, 5], hi);  row(4, [6, 7, 8], mid); row(4, [9, 10, 11], low)
row(5, [3, 12], dark);  row(5, [4], hi);     row(5, [5, 6, 7], mid); row(5, [8, 9, 10, 11], low)
row(6, [3, 12], dark);  row(6, [4, 5], mid); row(6, [6, 7, 8, 9], mid); row(6, [10, 11], low)
row(7, [3, 12], dark);  row(7, [4, 5, 6, 7], mid); row(7, [8, 9, 10, 11], low)
row(8, [4, 11], dark);  row(8, range(5, 11), low)
row(9, [5, 10], dark);  row(9, range(6, 10), low)

# luminous interior
c.set(5, 5, core); c.set(6, 5, core); c.set(6, 6, core)
c.set(7, 4, core)

# short wavy tentacles with dark bases
for x in (5, 7, 9, 11):
    c.set(x, 10, dark)
for (x, y) in [(5, 11), (5, 12), (4, 13), (5, 14),
               (7, 11), (7, 12), (6, 13), (7, 14),
               (9, 11), (9, 12), (10, 13), (9, 14),
               (11, 11), (11, 12), (11, 13), (10, 14)]:
    c.set(x, y, tent)

# drifting plankton sparks in the deep
for (x, y) in [(1, 2), (13, 4), (2, 10), (14, 9), (1, 13), (13, 14), (3, 1), (14, 12)]:
    c.set(x, y, spark)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))
finish(c)
