from pixelbench_api import new_canvas, view, finish

# 32px monarch butterfly, viewed from above.
c = new_canvas(32, 32, background=None, name="monarch-butterfly")

BLACK = "#171319"
DEEP = "#8f2d16"
ORANGE = "#e85b1d"
GOLD = "#f58a2a"
LIGHT = "#ffe0a3"
WHITE = "#fff4d6"

# Black wing silhouettes. Each wing is deliberately stepped and asymmetric by
# a pixel or two so the organic shape survives the low resolution.
left_upper = [(14,8),(11,5),(7,3),(4,3),(2,5),(1,8),(1,12),(3,15),(7,17),(12,16),(14,13)]
right_upper = [(17,8),(20,5),(24,3),(27,3),(29,5),(30,8),(30,12),(28,15),(24,17),(19,16),(17,13)]
left_lower = [(14,14),(10,15),(6,17),(3,20),(3,24),(5,27),(8,29),(11,28),(14,24),(15,19)]
right_lower = [(17,14),(21,15),(25,17),(28,20),(28,24),(26,27),(23,29),(20,28),(17,24),(16,19)]
for wing in (left_upper, right_upper, left_lower, right_lower):
    c.poly(wing, BLACK)

# Warm inner fields, separated from the silhouette by a heavy dark rim.
c.poly([(13,9),(10,6),(7,5),(4,5),(3,7),(3,11),(5,13),(8,15),(11,14),(13,12)], ORANGE)
c.poly([(18,9),(21,6),(24,5),(27,5),(28,7),(28,11),(26,13),(23,15),(20,14),(18,12)], ORANGE)
c.poly([(13,16),(10,17),(7,18),(5,20),(5,23),(7,26),(9,27),(11,26),(13,23),(14,19)], DEEP)
c.poly([(18,16),(21,17),(24,18),(26,20),(26,23),(24,26),(22,27),(20,26),(18,23),(17,19)], DEEP)

# Golden highlights inside the orange cells.
c.poly([(11,8),(8,6),(5,6),(4,8),(4,10),(6,12),(9,13),(11,12)], GOLD)
c.poly([(20,8),(23,6),(26,6),(27,8),(27,10),(25,12),(22,13),(20,12)], GOLD)
c.poly([(11,18),(8,19),(6,21),(6,23),(8,25),(10,25),(12,22),(12,19)], ORANGE)
c.poly([(20,18),(23,19),(25,21),(25,23),(23,25),(21,25),(19,22),(19,19)], ORANGE)

# Characteristic black veins radiating from the thorax.
for x0,y0,x1,y1 in [
    (14,11,8,5),(13,13,3,11),(13,14,7,16),(14,16,10,27),
    (14,18,4,22),(17,11,23,5),(18,13,28,11),(18,14,24,16),
    (17,16,21,27),(17,18,27,22)]:
    c.line(x0,y0,x1,y1,BLACK)

# Restore a few warm pixels where the one-pixel veins meet broad fields.
c.set(9,8,GOLD).set(22,8,GOLD)
c.set(8,20,ORANGE).set(23,20,ORANGE)

# Pale spots on the black margins, a monarch's defining border pattern.
spots = [
    (4,5),(7,4),(2,8),(2,11),(4,14),(7,15),
    (27,5),(24,4),(29,8),(29,11),(27,14),(24,15),
    (4,21),(5,25),(7,27),(10,27),
    (27,21),(26,25),(24,27),(21,27)
]
for i,(x,y) in enumerate(spots):
    c.set(x,y, WHITE if i % 3 else LIGHT)
# A few elongated edge markings.
c.rect(5,4,2,1,WHITE).rect(25,4,2,1,WHITE)
c.rect(3,16,2,1,LIGHT).rect(27,16,2,1,LIGHT)

# Body, head, subtle highlight, and clubbed antennae.
c.circle(15,7,2,BLACK)
c.rect(14,8,4,12,BLACK)
c.poly([(14,19),(17,19),(17,24),(16,27),(15,27),(14,24)],BLACK)
c.rect(15,9,1,9,"#5b3a2a")
c.set(15,6,"#6e4b35")
# Antennae arc outward as clean pixel stair-steps.
c.line(14,6,11,2,BLACK).line(11,2,9,1,BLACK)
c.line(17,6,20,2,BLACK).line(20,2,22,1,BLACK)
c.set(8,1,BLACK).set(23,1,BLACK)

view(c, scale=14, margin=1, edges="all")
finish(c)
