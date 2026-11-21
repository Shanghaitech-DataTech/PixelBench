# 64x64 front-facing girl mage sprite
result = new_canvas(64, 64, background=None, name="blue-cloak-girl-mage")

# Compact RPG palette
OUT = "#11152b"
DEEP = "#18234a"
BLUE = "#24366d"
MID = "#345095"
LITE = "#5775bd"
EDGE = "#8295d3"
SKIN = "#f2c6ad"
SKIN_D = "#c98379"
HAIR = "#372b4a"
HAIR_H = "#624566"
WHITE = "#eef1e8"
BOOT_S = "#b8c6d4"
AMBER_D = "#8f4b25"
AMBER = "#e89a35"
GLOW = "#ffd66b"
HOT = "#fff1aa"
WOOD = "#70452f"

# Staff glow, deliberately sparse and pixel-stepped
result.set(53, 7, AMBER_D).set(57, 7, AMBER_D)
result.set(50, 10, AMBER_D).set(60, 10, AMBER_D)
result.set(49, 14, AMBER_D).set(61, 14, AMBER_D)
result.set(51, 18, AMBER_D).set(59, 18, AMBER_D)
result.rect(52, 8, 7, 9, AMBER_D)
result.rect(51, 10, 9, 5, AMBER)
result.rect(53, 7, 5, 11, AMBER)
result.rect(52, 11, 7, 4, GLOW)
result.rect(54, 9, 3, 8, GLOW)
result.rect(55, 11, 2, 4, HOT)
result.set(52, 9, GLOW).set(58, 10, GLOW).set(52, 16, AMBER)

# Staff shaft behind the body
result.rect(55, 17, 3, 43, OUT)
result.rect(56, 18, 1, 41, WOOD)
result.rect(54, 58, 5, 3, OUT)
# Small dark cradle under the focus, without masking its bright core
result.rect(54, 17, 4, 2, OUT)
result.set(53, 16, OUT).set(58, 16, OUT)
result.set(54, 15, AMBER).set(57, 15, GLOW)

# Back hair and head outline
result.rect(25, 7, 14, 3, OUT)
result.rect(22, 10, 20, 12, OUT)
result.rect(24, 6, 4, 3, OUT)
result.rect(28, 4, 8, 3, OUT)
result.rect(36, 6, 4, 3, OUT)
result.set(21, 13, OUT).set(42, 13, OUT)
result.rect(23, 10, 18, 12, HAIR)
result.rect(25, 7, 14, 4, HAIR)
result.rect(28, 5, 8, 3, HAIR)
result.rect(24, 9, 4, 5, HAIR_H)
result.set(26, 7, HAIR_H).set(37, 8, HAIR_H)

# Face and ears
result.rect(26, 11, 12, 11, SKIN)
result.rect(24, 14, 2, 5, SKIN_D)
result.rect(38, 14, 2, 5, SKIN_D)
# Fringe with a central anime point
result.rect(25, 10, 14, 3, HAIR)
result.rect(25, 12, 4, 3, HAIR)
result.rect(35, 12, 4, 3, HAIR)
result.set(29, 13, HAIR).set(34, 13, HAIR)
# Eyes, brows, nose and tiny smile
result.set(28, 15, HAIR_H).set(35, 15, HAIR_H)
result.rect(28, 16, 2, 2, OUT).rect(34, 16, 2, 2, OUT)
result.set(29, 16, EDGE).set(35, 16, EDGE)
result.set(32, 18, SKIN_D)
result.set(31, 20, SKIN_D).set(32, 21, SKIN_D).set(33, 20, SKIN_D)

# Neck and high cloak collar
result.rect(29, 21, 6, 4, OUT)
result.rect(30, 21, 4, 3, SKIN)
result.poly([(21,20),(27,20),(31,24),(37,20),(43,20),(45,29),(19,29)], OUT)
result.poly([(22,21),(27,21),(31,25),(37,21),(42,21),(43,27),(20,27)], DEEP)
result.poly([(27,22),(31,26),(37,22),(36,28),(28,28)], MID)
result.set(31, 24, EDGE).set(32, 25, EDGE)

# Cloak silhouette: broad shoulders, long tapered drape
result.poly([(19,25),(24,23),(40,23),(45,26),(48,39),(44,46),(42,57),(36,59),(28,59),(22,57),(20,46),(16,40)], OUT)
result.poly([(20,26),(25,24),(39,24),(44,27),(46,39),(42,45),(40,56),(35,57),(29,57),(24,55),(22,44),(18,39)], BLUE)
# Main front plane and folds
result.poly([(27,27),(37,27),(40,34),(39,55),(34,57),(29,56),(24,53),(24,36)], MID)
result.poly([(27,28),(31,28),(30,55),(26,53),(25,38)], LITE)
result.poly([(36,28),(39,32),(38,52),(34,56),(34,32)], DEEP)
result.line(32, 28, 32, 55, EDGE)
result.set(31, 30, WHITE).set(33, 30, WHITE)
# Hem pixels
result.rect(23, 55, 4, 3, OUT).rect(38, 55, 4, 3, OUT)
result.set(27, 56, LITE).set(37, 56, DEEP)

# Left relaxed arm, hand peeking out
result.poly([(20,27),(16,29),(13,39),(16,43),(21,40),(23,31)], OUT)
result.poly([(20,28),(17,30),(15,39),(17,41),(20,39),(22,31)], DEEP)
result.line(17, 31, 16, 38, MID)
result.rect(15, 40, 5, 4, OUT)
result.rect(16, 40, 3, 3, SKIN)
result.set(15, 42, SKIN_D)

# Right arm angled casually toward staff
result.poly([(42,27),(46,29),(49,35),(54,34),(56,38),(50,41),(45,38),(41,33)], OUT)
result.poly([(42,28),(45,30),(48,37),(51,38),(53,36),(50,35),(47,36),(44,32)], DEEP)
result.line(43, 29, 47, 37, MID)
# Hand gripping staff
result.rect(52, 34, 6, 6, OUT)
result.rect(52, 35, 4, 4, SKIN)
result.set(53, 39, SKIN_D).set(57, 36, WOOD)

# White boots separated under cloak
result.poly([(25,56),(31,56),(31,60),(29,63),(22,63),(22,60)], OUT)
result.poly([(26,56),(30,57),(29,60),(28,61),(23,61),(24,58)], WHITE)
result.set(24, 60, BOOT_S).set(25, 60, BOOT_S)
result.poly([(34,56),(40,56),(42,60),(42,63),(35,63),(33,60)], OUT)
result.poly([(35,57),(39,56),(40,59),(41,61),(36,61),(35,60)], WHITE)
result.set(39, 60, BOOT_S).set(40, 60, BOOT_S)

# Final selective outline accents for a crisp silhouette
result.set(18, 26, OUT).set(45, 27, OUT)
result.set(21, 51, OUT).set(42, 52, OUT)

view(result, scale=8, margin=1, edges="all")
finish(result)
