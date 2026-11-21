# Two-frame elf archer attack animation.
# Frame 1 preserves every source pixel, with transparent room added for motion.
W, H = 48, 47
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 6, 0)

f2 = new_canvas(W, H, name="frame_2_full_draw")

# Existing palette indices from the supplied sprite.
INK = 20
DEEP = 25
BROWN = 1
BROWN2 = 2
LEATHER = 27
SKIN_D = 16
SKIN = 3
SKIN_L = 12
CREAM = 13
GOLD_D = 27
GOLD = 19
YELLOW = 7
GREEN_D = 24
GREEN = 22
GREEN_L = 26
CLOTH_D = 10
CLOTH = 8
CLOTH_L = 11
STEEL_D = 31
STEEL = 32
STEEL_L = 33
BOOT = 37
BOOT_L = 40

# Bowstring: a deep V from the limb tips to the hand pulled beside the cheek.
f2.line(40, 3, 24, 15, CREAM)
f2.line(24, 15, 40, 43, CREAM)
f2.set(39, 4, SKIN_L)
f2.set(39, 42, SKIN_L)

# Fully opened recurve bow, outlined and highlighted. The bent limb sits well
# ahead of the archer and contains no arrow shaft.
bow_outline = [(40,3),(43,5),(44,8),(46,11),(46,16),(45,20),(44,23),
               (45,26),(46,31),(46,35),(44,39),(42,42),(40,44)]
for a, b in zip(bow_outline, bow_outline[1:]):
    f2.line(a[0], a[1], b[0], b[1], INK)
bow_inner = [(40,4),(42,6),(43,9),(45,12),(45,16),(44,20),(43,23),
             (44,26),(45,31),(45,35),(43,39),(41,42),(40,43)]
for a, b in zip(bow_inner, bow_inner[1:]):
    f2.line(a[0], a[1], b[0], b[1], GOLD)
f2.line(42,7,44,16,YELLOW)
f2.line(44,30,43,38,YELLOW)
f2.rect(42,21,3,5,BROWN)
f2.rect(43,22,2,3,GOLD_D)

# Rear cape flares opposite the shot, helping the planted stance read.
f2.poly([(14,21),(10,25),(8,31),(5,36),(5,41),(10,40),(14,35),(18,30)], INK)
f2.poly([(14,22),(11,26),(10,31),(7,36),(7,39),(10,38),(13,34),(17,29)], CLOTH_D)
f2.poly([(11,27),(9,32),(8,37),(11,35),(14,29)], CLOTH)
f2.line(10,30,8,36,CLOTH_L)

# Wide braced legs: rear foot drives left, lead foot drives right.
f2.poly([(15,29),(21,30),(19,35),(16,41),(14,44),(5,44),(5,41),(11,38),(12,32)], INK)
f2.poly([(14,31),(19,31),(17,35),(15,40),(12,42),(7,42),(12,38)], STEEL_D)
f2.poly([(16,32),(18,33),(16,38),(14,40),(13,37)], STEEL)
f2.poly([(5,41),(13,41),(15,44),(13,46),(4,46),(2,44)], DEEP)
f2.poly([(6,42),(12,42),(13,44),(11,45),(4,45)], BOOT)
f2.rect(6,42,4,2,BOOT_L)

f2.poly([(20,29),(26,29),(29,34),(33,39),(40,41),(41,44),(38,46),(29,45),(29,42),(25,38),(21,35)], INK)
f2.poly([(22,30),(25,31),(28,35),(32,40),(38,41),(37,43),(31,42),(27,38),(22,35)], STEEL_D)
f2.poly([(24,31),(26,34),(30,39),(32,39),(29,35)], STEEL)
f2.poly([(31,40),(39,40),(43,43),(41,46),(31,46),(28,44)], DEEP)
f2.poly([(33,41),(38,41),(41,43),(39,45),(31,44)], BOOT)
f2.rect(34,41,4,2,BOOT_L)

# Torso leaned into the shot, with dark outline, green tunic, belt and armor.
f2.poly([(14,17),(23,16),(28,19),(30,25),(27,31),(23,34),(14,32),(11,28),(11,22)], INK)
f2.poly([(15,18),(22,18),(26,20),(27,25),(25,30),(21,32),(15,30),(13,27),(13,22)], GREEN_D)
f2.poly([(17,19),(23,19),(25,22),(25,27),(22,29),(16,28),(15,24)], GREEN)
f2.poly([(20,20),(24,21),(24,25),(20,25)], GREEN_L)
f2.line(14,28,25,30,BROWN)
f2.line(15,29,24,31,LEATHER)
f2.rect(19,29,3,3,GOLD_D)
f2.set(20,29,GOLD)
# Shoulder guard and breastplate glints.
f2.poly([(13,18),(17,16),(20,18),(18,22),(13,22),(11,20)], INK)
f2.poly([(14,18),(17,17),(19,19),(17,21),(13,20)], STEEL)
f2.set(15,18,STEEL_L)
f2.poly([(22,18),(26,19),(28,23),(26,25),(24,22)], STEEL_D)
f2.line(24,19,27,23,STEEL_L)

# Copy the original head so face, hair, ear, and palette-specific detail stay
# recognizably the same character. It is shifted into a forward lean.
head = input_canvas.select(7, 0, 16, 18)
head.copy_to(12, 0, f2, mode="over")

# Pointed ear silhouette and small hair tie, reinforcing the elf profile.
f2.poly([(24,8),(31,10),(25,13)], INK)
f2.poly([(24,9),(29,10),(24,12)], SKIN)
f2.set(26,10,SKIN_L)
f2.rect(13,14,3,2,CLOTH_D)
f2.set(12,15,CLOTH)

# Pulling arm: elbow thrown back, forearm returning to the cheek/string hand.
f2.poly([(15,18),(11,18),(7,22),(8,26),(12,27),(14,24),(18,20),(25,17),(26,14),(23,12),(21,15),(17,17)], INK)
f2.poly([(14,19),(11,20),(9,22),(10,24),(12,25),(13,23),(17,19),(23,17),(24,15),(23,14),(21,17),(17,18)], SKIN_D)
f2.poly([(11,20),(9,22),(10,23),(12,23),(15,20)], SKIN)
f2.line(15,19,22,16,SKIN)
f2.set(22,15,SKIN_L)
# Draw hand wrapped around the string at maximum draw, beside the face.
f2.rect(22,13,4,4,INK)
f2.rect(23,14,3,3,SKIN)
f2.set(24,14,SKIN_L)
f2.set(24,15,BROWN)

# Bow arm: shoulder to locked elbow to the grip, angled slightly downward.
f2.poly([(24,19),(28,18),(33,20),(39,21),(43,21),(44,25),(40,27),(37,25),(32,24),(27,24),(23,22)], INK)
f2.poly([(26,20),(29,20),(33,22),(39,22),(41,23),(40,25),(37,24),(32,23),(28,23),(25,22)], SKIN_D)
f2.line(28,21,38,23,SKIN)
f2.line(30,22,38,24,SKIN)
f2.rect(39,22,3,4,SKIN)
f2.set(40,22,SKIN_L)
f2.set(41,24,BROWN)
# Bracer on the extended forearm.
f2.poly([(31,20),(35,21),(35,25),(31,24)], BROWN)
f2.line(32,21,34,22,GOLD_D)

# A few crisp contour repairs after overlapping parts.
f2.line(14,31,20,33,INK)
f2.set(24,15,SKIN_L)
f2.set(24,16,SKIN)
f2.set(40,23,SKIN_L)

finish([f1, f2])
view(f2, scale=10, margin=1, edges="all")
