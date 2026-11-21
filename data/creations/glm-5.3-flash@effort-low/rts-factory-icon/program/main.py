c = new_canvas(32, 32, background="#1a1a24", name="factory")

BRICK = "#8a4a32"
BRICK_D = "#6e3826"
ROOF = "#4a4e5a"
ROOF_D = "#33363f"
CHIM = "#5c5f6b"
VENT = "#9aa0ad"
WIN = "#f2c94c"
DARK = "#241f1c"
SMOKE = "#c9c9d2"

# chimney (behind, left of center)
c.rect(8, 3, 4, 9, CHIM)
c.rect(8, 3, 4, 1, DARK)          # opening
c.rect(8, 4, 1, 8, "#6b6e7a")     # highlight
# smoke puffs
c.set(9, 1, SMOKE); c.set(10, 0, SMOKE); c.set(11, 1, SMOKE)
c.set(12, 2, SMOKE)

# main building body
c.rect(5, 12, 22, 14, BRICK)
# roof
c.rect(5, 10, 22, 3, ROOF)
c.rect(5, 10, 22, 1, ROOF_D)
c.rect(5, 12, 22, 1, ROOF_D)

# brick texture: horizontal mortar lines + staggered verticals
for y in range(14, 26, 3):
    c.rect(5, y, 22, 1, BRICK_D)
for y in range(12, 26, 3):
    off = 2 if ((y - 12) // 3) % 2 else 0
    for x in range(5 + off, 27, 6):
        c.set(x, y + 1, BRICK_D)

# vents on roof
c.rect(9, 8, 3, 2, VENT)
c.rect(20, 8, 3, 2, VENT)
c.rect(9, 8, 3, 1, "#c3c8d2")
c.rect(20, 8, 3, 1, "#c3c8d2")

# windows
c.rect(8, 16, 4, 5, WIN)
c.rect(20, 16, 4, 5, WIN)
c.rect(10, 16, 1, 5, BRICK_D)
c.rect(22, 16, 1, 5, BRICK_D)
c.rect(8, 18, 4, 1, BRICK_D)
c.rect(20, 18, 4, 1, BRICK_D)

# door
c.rect(14, 20, 4, 6, DARK)
c.rect(14, 20, 4, 1, "#3a3a44")
c.set(16, 23, WIN)

# base shadow line
c.rect(5, 25, 22, 1, BRICK_D)

print(c.stats_text())
save("factory", c)
finish(c)
