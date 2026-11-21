from pixelbench_api import *

c = new_canvas(16, 16)
dark = c.color((22, 22, 26), "dark")
red = c.color((198, 34, 34), "red")
white = c.color((246, 240, 232), "white")
tan = c.color((232, 202, 155), "tan")

def row(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)

# ---- Cap (dome) ----
row(0, 6, 9, dark)          # cap top tip
row(1, 5, 10, dark)
row(2, 4, 11, dark)
row(3, 3, 12, dark)
row(4, 3, 12, dark)
row(5, 3, 12, dark)
row(6, 4, 11, dark)          # cap brim

# Fill cap red
c.rect(5, 1, 6, 1, red)     # y1
c.rect(5, 2, 6, 1, red)     # y2 inner
for yy in range(3, 6):
    c.rect(4, yy, 8, 1, red)

# White spots
c.set(5, 4, white)
c.set(10, 4, white)
c.set(7, 3, white)
c.set(9, 5, white)

# ---- Face / body (tan) ----
row(7, 5, 10, tan)
row(8, 6, 9, tan)
row(9, 6, 9, tan)
row(10, 6, 9, tan)

# Eyes (dark, round pair)
c.set(6, 7, dark)
c.set(7, 7, dark)
c.set(9, 7, dark)
c.set(10, 7, dark)

# ---- Arms (stubby, on sides) ----
row(8, 4, 5, dark)
row(9, 4, 5, dark)
c.set(5, 8, tan)
c.set(5, 9, tan)
row(8, 10, 11, dark)
row(9, 10, 11, dark)
c.set(10, 8, tan)
c.set(10, 9, tan)

# Legs (two stubs)
row(11, 6, 7, dark)
row(12, 6, 7, dark)
row(13, 6, 7, dark)
row(11, 8, 9, dark)
row(12, 8, 9, dark)
row(13, 8, 9, dark)

# Feet bottoms
row(14, 6, 7, dark)
row(14, 8, 9, dark)

print(c.matrix_text(region=(0,0,15,15), indices=False))
print(c.stats_text())
save("mushroomling", c)
result = c
finish(result)
