# Two-frame slash spritesheet: each 24x48 cell is one animation frame.
c = new_canvas(48, 48, name="slash_effect")

WHITE = "#fff9ee"
ICE = "#c9f7ff"
CYAN = "#62dfff"
BLUE = "#2a9dce"

# Compact curved slash, built as a stepped crescent silhouette.
c.poly([(3,31),(4,26),(6,22),(9,18),(13,15),(17,13),(21,12),(20,15),(17,17),(14,20),(11,24),(9,28),(7,33),(6,36),(4,34)], ICE)
c.poly([(4,30),(5,26),(7,22),(10,19),(14,16),(18,14),(20,14),(18,17),(15,20),(12,24),(10,28),(8,33),(6,34),(5,33)], WHITE)
# A tiny glint at the leading tip.
c.set(20, 13, WHITE)

# Expanded second pose in the right-hand frame, preserving the same motion.
c.poly([(26,34),(27,28),(29,22),(32,17),(36,12),(40,9),(45,7),(46,8),(44,12),(41,15),(38,19),(35,24),(33,29),(31,34),(29,39),(27,38)], BLUE)
c.poly([(27,33),(28,28),(30,23),(33,18),(37,13),(41,10),(44,9),(43,12),(40,16),(37,20),(34,25),(32,30),(30,35),(28,37)], CYAN)
c.poly([(29,31),(30,27),(32,23),(35,18),(39,14),(42,12),(43,12),(41,15),(38,19),(35,24),(33,29),(31,33),(30,35)], WHITE)
# Tapered energy trail behind the larger arc.
c.poly([(25,39),(30,35),(34,32),(36,31),(34,34),(30,37),(27,41)], CYAN)
c.poly([(27,39),(31,36),(34,34),(31,37),(28,40)], ICE)
c.poly([(26,29),(28,25),(30,23),(29,27),(27,31)], BLUE)

print(c.stats_text())
print(c.matrix_text(region=(0, 10, 23, 39)))
print(c.matrix_text(region=(24, 5, 47, 42)))
finish(c)
