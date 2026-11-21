from pixelbench_api import *

# Two 32x32 animation frames on one 64x64 transparent sprite sheet.
result = new_canvas(64, 64, background=None, name="explosion_effect")

# Palette: warm, stepped ramps with a dark red edge for contrast.
DEEP = "#6e1423"
RED = "#a92724"
VERM = "#e34b22"
ORANGE = "#f87822"
AMBER = "#f6a31c"
GOLD = "#ffd12a"
YELLOW = "#ffe84a"
PALE = "#fff38a"
WHITE = "#fffbd1"
SMOKE = "#7a3040"

# Frame 1, centered at (16, 32): compact, bright ignition fireball.
# Dark irregular fringe.
result.poly([(8,31),(10,27),(9,24),(13,24),(15,20),(18,23),(22,22),(22,26),(25,28),(23,32),(25,35),(21,37),(20,41),(16,39),(12,41),(11,37),(7,35)], DEEP)
result.poly([(9,30),(11,27),(11,24),(14,25),(16,21),(18,25),(21,24),(21,28),(24,30),(22,33),(23,35),(19,36),(19,39),(16,37),(13,39),(13,36),(9,34)], RED)
result.poly([(10,30),(12,27),(14,26),(16,23),(18,26),(21,26),(20,29),(23,31),(20,33),(21,35),(18,35),(17,38),(15,35),(12,36),(13,33),(10,33)], ORANGE)
# Main luminous mass.
result.circle(16, 31, 6, GOLD)
result.poly([(12,30),(13,27),(16,25),(19,27),(21,30),(20,34),(17,36),(13,34)], YELLOW)
result.rect(13, 28, 6, 6, PALE)
result.rect(15, 27, 3, 2, WHITE)
result.rect(13, 30, 2, 3, WHITE)
# Tiny ignition flecks contained within frame one.
result.set(6, 27, AMBER).set(7, 26, GOLD)
result.set(25, 24, ORANGE).set(26, 23, GOLD)
result.set(6, 38, RED).set(7, 37, ORANGE)
result.set(25, 39, RED).set(24, 38, AMBER)

# Frame 2, centered at (48, 32): expanding blast with broken, spiky rim.
# Detached sparks first.
for x, y, c in [
    (35,18,RED),(36,17,ORANGE),(38,20,GOLD),
    (48,14,RED),(48,16,AMBER),(49,15,ORANGE),
    (58,18,RED),(59,17,ORANGE),(60,20,GOLD),
    (62,25,RED),(61,26,AMBER),(63,31,ORANGE),
    (61,40,RED),(60,39,GOLD),(58,45,VERM),
    (49,48,RED),(49,46,AMBER),(42,47,RED),
    (36,43,RED),(37,41,ORANGE),(33,36,VERM),
    (34,27,RED),(36,27,GOLD)
]:
    result.set(x, y, c)
# A few two-pixel spark streaks.
result.line(39,16,40,18,ORANGE)
result.set(40,17,GOLD)
result.line(56,14,55,17,RED)
result.set(55,16,AMBER)
result.line(62,35,60,34,VERM)
result.set(61,34,GOLD)
result.line(39,46,40,44,RED)
result.set(40,45,ORANGE)

# Outer blast silhouette and radial spikes.
result.poly([(34,32),(38,29),(35,25),(41,25),(40,20),(45,23),(48,18),(51,23),(56,20),(56,26),(62,27),(58,32),(62,36),(56,37),(57,43),(52,41),(48,46),(45,41),(39,43),(40,37),(34,36)], DEEP)
result.poly([(36,32),(40,29),(38,26),(43,27),(42,23),(46,25),(48,21),(51,25),(55,23),(54,28),(59,28),(56,32),(60,35),(54,35),(55,40),(51,38),(48,43),(45,38),(41,40),(42,35),(37,35)], RED)
result.poly([(39,31),(42,29),(41,26),(45,28),(47,24),(49,27),(53,25),(53,29),(57,30),(54,33),(57,35),(52,35),(52,39),(48,37),(45,40),(44,35),(40,36),(42,33)], VERM)
# Hot inner turbulent lobes.
result.circle(48, 32, 7, ORANGE)
result.poly([(42,31),(44,27),(47,28),(49,25),(51,29),(55,30),(53,33),(55,36),(50,35),(48,39),(46,35),(42,36),(44,33)], AMBER)
result.rect(46, 29, 6, 6, GOLD)
result.poly([(47,30),(49,28),(52,30),(51,33),(49,35),(46,33)], YELLOW)
result.set(48,30,PALE).set(49,30,WHITE).set(47,31,PALE)
# Broken dark-red debris pixels reinforce outward motion.
result.rect(32,31,2,2,SMOKE)
result.set(34,32,RED)
result.rect(62,29,2,2,SMOKE)
result.set(61,30,RED)
result.rect(52,47,2,1,SMOKE)
result.set(52,46,RED)

view(result, scale=8, margin=0)
finish(result)
