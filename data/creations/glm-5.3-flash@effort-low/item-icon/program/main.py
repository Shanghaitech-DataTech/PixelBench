c = new_canvas(32, 32, name="compass")

# palette
DARK   = "#2b2016"   # thick dark outline
GOLD_D = "#8a5a1e"
GOLD   = "#d9a441"
GOLD_L = "#f2d27a"
CRYST  = "#2a6fd6"
CRYST_L= "#7fc0ff"
CRYST_D= "#1a3f8f"
WHITE  = "#eaf6ff"

# outer outline ring (circle r=14 centered 15.5 -> use ellipse)
c.circle(16, 16, 14, DARK)
c.circle(16, 16, 13, GOLD_D)
c.circle(16, 16, 12, GOLD)
c.circle(16, 16, 11, GOLD_D)
c.circle(16, 16, 10, DARK)  # inner rim of bezel

# crystal center
c.circle(16, 16, 8, DARK)
c.circle(16, 16, 7, CRYST_D)
c.circle(16, 16, 6, CRYST)
c.circle(16, 16, 4, CRYST_L)
c.set(16, 15, WHITE); c.set(15, 14, WHITE)

# compass needle points (top-down): N-S-E-W gold points over crystal? keep crystal clean;
# draw small gold ticks at cardinal points on the bezel ring
for (x, y) in [(16, 5), (16, 27), (5, 16), (27, 16)]:
    c.set(x, y, GOLD_L)

# needle: dark outline diamond under crystal? draw small needle tips outside crystal
c.line(16, 8, 16, 10, GOLD_L)
c.line(16, 22, 16, 24, GOLD_D)
c.line(8, 16, 10, 16, GOLD_D)
c.line(22, 16, 24, 16, GOLD_D)

# highlight on bezel top-left
c.line(9, 8, 12, 6, GOLD_L)
c.set(8, 9, GOLD_L)

print(c.stats_text())
finish(c)
