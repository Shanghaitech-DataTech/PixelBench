c = new_canvas(32, 32, background=None, name="retro_camera")

OUT = "#1a1410"   # dark outline
BODY = "#7a5230"  # leather brown
BODY_D = "#5a3a20"
BODY_L = "#9a6f45"
TOP = "#3a3a3a"   # metal top plate
TOP_L = "#5c5c5c"
LENS = "#22201e"
GLASS = "#3f5a6e"
GLASS_L = "#7fa3bd"
SHINE = "#c8d8e4"
SIL = "#b8b8b8"
RED = "#a83232"

# body: leather rectangle with rounded corners
c.rect(6, 14, 20, 12, OUT)
c.rect(7, 15, 18, 10, BODY)
# top plate
c.rect(8, 11, 16, 4, TOP)
c.rect(9, 12, 14, 2, TOP_L)
# viewfinder bump
c.rect(10, 9, 5, 3, OUT)
c.rect(11, 10, 3, 1, TOP_L)
# shutter button
c.set(19, 10, OUT); c.set(19, 9, SIL)
# flash shoe
c.rect(14, 9, 5, 1, OUT)

# leather texture: darker speckles
for (x, y) in [(9,17),(12,18),(15,16),(18,19),(21,17),(10,21),(14,23),(17,22),
               (20,24),(22,21),(8,23),(11,24),(16,20),(19,16),(13,21),(23,24),
               (9,19),(21,22),(24,18),(7,17)]:
    c.set(x, y, BODY_D)
for (x, y) in [(10,16),(13,17),(16,18),(19,17),(22,19),(12,22),(15,24),(18,23),
               (21,25),(24,22),(9,25)]:
    c.set(x, y, BODY_L)

# lens: big circle centered at (16, 20), r=6
c.circle(16, 20, 6, OUT)
c.circle(16, 20, 5, LENS)
c.circle(16, 20, 3, GLASS)
c.set(15, 19, GLASS_L)
c.set(14, 18, SHINE)
c.set(15, 18, SHINE)
c.set(14, 19, GLASS_L)
c.set(18, 22, "#2c4356")
c.set(17, 23, "#2c4356")

# lens ring highlights
c.set(10, 18, SIL); c.set(11, 17, SIL); c.set(12, 16, SIL)
c.set(22, 22, "#111"); c.set(21, 23, "#111")

# strap lugs
c.set(5, 15, OUT); c.set(6, 14, OUT)
c.set(26, 15, OUT); c.set(25, 14, OUT)

# bottom outline shading
c.rect(7, 24, 18, 1, BODY_D)
c.line(7, 24, 24, 24, OUT)
c.set(7, 25, OUT); c.set(24, 25, OUT)
c.set(8, 25, OUT); c.set(23, 25, OUT)
c.set(9, 25, OUT); c.set(22, 25, OUT)

# red window dot
c.rect(24, 18, 2, 2, OUT)
c.set(24, 18, RED)

print(c.stats_text())
save("retro_camera", c)
finish(c)
