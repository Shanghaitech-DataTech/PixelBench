# Two-frame explosion sprite sheet on one 64x64 transparent canvas.
result = new_canvas(64, 64, background=None, name="explosion_effect")

# Palette: shared warm ramp.
white = "#fffbe8"
pale = "#fff4a3"
yellow = "#ffd928"
gold = "#ffad14"
orange = "#f66a16"
red = "#d93616"
darkred = "#8f1f16"
smoke = "#572126"

# Frame 1: compact ignition centered in the left 32px cell (16, 32).
# Outer hot fireball silhouette.
result.poly([(16,17),(19,23),(24,21),(23,27),(29,30),(24,34),(26,40),
             (20,39),(17,47),(13,40),(8,42),(9,35),(3,32),(9,28),(7,22),(13,24)], red)
# Orange body, asymmetrical tongues.
result.poly([(16,20),(19,26),(23,25),(21,30),(27,32),(21,35),(22,39),
             (17,37),(15,43),(12,37),(7,39),(10,33),(6,31),(11,29),(10,25),(14,27)], orange)
# Gold inner flame.
result.poly([(16,23),(18,28),(21,28),(20,32),(23,33),(19,35),(19,38),
             (16,36),(14,40),(13,36),(10,37),(12,33),(9,31),(13,30),(13,27)], gold)
# Bright yellow core.
result.poly([(16,26),(18,30),(21,31),(18,33),(19,36),(16,35),(14,38),
             (13,34),(11,32),(14,30),(14,27)], yellow)
result.rect(14,29,4,5,pale)
result.rect(15,30,3,3,white)
# Tiny ignition flecks contained in frame one.
result.rect(4,20,2,2,gold)
result.set(2,18,yellow)
result.rect(26,23,2,2,yellow)
result.set(29,20,orange)
result.rect(4,43,2,2,orange)
result.set(27,45,red)
result.set(16,13,yellow)
result.set(17,14,gold)

# Frame 2: expanded blast centered in the right 32px cell (48, 32).
# Dark-red far rim and long radial lobes.
result.poly([(48,14),(51,22),(56,18),(56,25),(63,24),(59,30),(63,34),
             (58,36),(61,43),(54,41),(53,49),(48,43),(43,50),(41,42),
             (34,45),(37,37),(32,34),(38,30),(33,25),(41,25),(42,18)], darkred)
# Red blast shell.
result.poly([(48,18),(51,24),(55,21),(54,28),(61,27),(57,32),(62,34),
             (56,36),(58,41),(52,39),(51,46),(48,40),(44,46),(43,39),
             (36,42),(39,36),(34,33),(40,30),(37,27),(43,28),(43,22)], red)
# Orange rolling cloud mass.
result.poly([(48,21),(51,27),(54,25),(53,30),(58,30),(55,34),(58,37),
             (52,36),(52,41),(48,38),(45,42),(44,37),(39,38),(42,34),
             (38,32),(44,30),(42,27),(46,28)], orange)
# Gold center and irregular hot pockets.
result.poly([(48,24),(50,29),(53,28),(52,32),(56,33),(52,35),(52,38),
             (48,36),(46,39),(45,35),(42,35),(45,32),(43,30),(47,30)], gold)
result.rect(46,29,5,6,yellow)
result.rect(47,30,3,4,pale)
result.rect(48,31,2,2,white)
# Rim highlights suggesting rolling flame fronts.
result.rect(40,29,3,2,gold)
result.rect(54,31,3,2,yellow)
result.rect(42,36,3,2,gold)
result.rect(50,38,2,2,gold)
result.rect(45,24,2,3,yellow)
# Sparse detached sparks, all inside the right frame cell.
result.rect(35,17,2,2,orange)
result.set(38,13,yellow)
result.set(39,14,gold)
result.rect(45,9,2,3,red)
result.set(51,10,gold)
result.rect(57,14,2,2,orange)
result.set(61,18,yellow)
result.rect(61,45,2,2,red)
result.set(58,50,orange)
result.rect(52,52,2,2,gold)
result.set(44,54,red)
result.rect(36,48,2,2,orange)
result.set(33,41,yellow)

view(result, scale=8, margin=0)
finish(result)
