c = new_canvas(16, 16, name="result")
GOLD = c.color("#F5C542", "gold")
DARK = c.color("#B8860B", "dark_gold")
LIGHT = c.color("#FFF3B0", "light")
OUT = c.color("#7A5200", "outline")

# coin circle r=7 centered (8,8)
c.circle(8, 8, 7, GOLD)
c.circle(8, 8, 7, OUT, fill=False)
# inner rim
c.circle(8, 8, 6, DARK, fill=False)
# highlight
c.set(5, 4, LIGHT); c.set(6, 4, LIGHT); c.set(5, 5, LIGHT)
# star in middle (5-point, small)
star = [(8,4),(9,7),(12,7),(10,9),(11,12),(8,10),(5,12),(6,9),(4,7),(7,7)]
c.poly(star, DARK)
# star outline hint
for (x,y) in [(8,4),(9,7),(12,7),(10,9),(11,12),(8,10),(5,12),(6,9),(4,7),(7,7)]:
    pass
# shine on star
c.set(8,6,LIGHT)
print(c.stats_text())
finish(c)
