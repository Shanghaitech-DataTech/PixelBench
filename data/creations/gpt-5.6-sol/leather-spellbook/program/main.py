from pixelbench_api import new_canvas, view, finish

# Closed leather spellbook in a slightly tilted three-quarter view.
c = new_canvas(32, 32, background=None, name="leather_spellbook")

INK = "#1b1720"
DEEP = "#3a2023"
LEATHER = "#69342a"
WARM = "#9a5335"
GOLD = "#c58a45"
STEEL_DARK = "#58616a"
STEEL = "#9aa4a5"
PAGE = "#d5bd83"

# Page block and lower silhouette.
c.poly([(6,8),(22,5),(28,10),(27,25),(12,29),(5,24)], INK)
c.poly([(8,11),(22,8),(26,11),(25,23),(12,26),(8,23)], PAGE)
# Page strata and lower shadow.
c.line(9,21,12,24, STEEL_DARK)
c.line(12,24,24,21, STEEL_DARK)
c.line(10,23,13,25, GOLD)
c.line(13,25,24,22, GOLD)
c.line(12,26,25,23, INK)

# Thick leather spine wrapping the page block.
c.poly([(5,9),(10,12),(10,27),(6,24)], DEEP)
c.poly([(6,10),(9,12),(9,25),(7,23)], LEATHER)
c.line(7,13,9,14,WARM)
c.line(7,21,9,22,WARM)
c.set(7,17,GOLD)

# Main cover, dark rim and raised leather inset.
c.poly([(6,7),(21,3),(29,8),(27,22),(11,27),(5,22)], INK)
c.poly([(7,8),(21,5),(27,9),(25,20),(11,24),(7,21)], LEATHER)
# Cover light and worn patches.
c.poly([(9,9),(20,6),(25,9),(24,12),(11,15)], WARM)
c.poly([(11,16),(24,12),(23,19),(12,22)], DEEP)
c.line(11,15,12,22, GOLD)
c.line(12,15,24,12, GOLD)
c.line(12,22,23,19, INK)
c.set(20,7,GOLD)
c.set(23,10,GOLD)
c.set(10,11,GOLD)
c.set(21,18,WARM)

# Decorative central sigil, stamped into the leather.
c.poly([(17,10),(20,12),(19,16),(16,18),(14,15),(14,12)], INK)
c.poly([(17,11),(19,12),(18,15),(16,17),(15,15),(15,13)], GOLD)
c.set(17,13,LEATHER)
c.set(16,14,LEATHER)
c.set(18,14,STEEL)

# Reinforced metal corners, with bright one-pixel facets.
c.poly([(6,7),(10,6),(11,9),(8,11),(6,10)], STEEL_DARK)
c.poly([(7,7),(10,7),(9,9),(7,9)], STEEL)
c.set(8,7,PAGE)

c.poly([(21,3),(25,5),(24,8),(21,7),(19,5)], STEEL_DARK)
c.poly([(21,4),(24,5),(23,7),(21,6)], STEEL)
c.set(22,4,PAGE)

c.poly([(27,18),(27,22),(23,24),(22,21),(24,19)], STEEL_DARK)
c.poly([(26,19),(26,21),(24,22),(23,21),(24,20)], STEEL)
c.set(25,20,PAGE)

c.poly([(11,23),(14,24),(13,27),(10,28),(8,25)], STEEL_DARK)
c.poly([(11,24),(13,25),(12,26),(10,26),(10,25)], STEEL)
c.set(11,24,PAGE)

# Spine bands and small rivets.
c.rect(5,11,4,2,INK)
c.line(6,11,8,12,STEEL_DARK)
c.set(7,11,STEEL)
c.rect(6,20,4,2,INK)
c.line(7,20,9,21,STEEL_DARK)
c.set(8,20,STEEL)
c.set(25,9,STEEL)
c.set(23,20,STEEL_DARK)

view(c, scale=16, margin=0)
finish(c)
