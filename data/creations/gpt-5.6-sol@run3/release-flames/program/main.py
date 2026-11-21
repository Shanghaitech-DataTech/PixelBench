# Two-frame release animation on a shared expanded stage.
W, H = 80, 64
f1 = new_canvas(W, H, name="release_01")
f2 = new_canvas(W, H, name="release_02")

# Frame 1: preserve every source pixel, only adding transparent room for motion.
f1.blit(input_canvas, 8, 1)

# Existing palette, kept deliberately tight.
INK = "#010202"
DEEP = "#0b0102"
SHADOW = "#240b0c"
PLUM = "#4a222d"
SKIN = "#7d423a"
SKIN_DARK = "#443d45"
CLOTH_DARK = "#211d2c"
CLOTH = "#455363"
HI = "#828684"
PALE = "#dfb2ac"
ORANGE = "#f27219"
GOLD = "#f4a30c"
YELLOW = "#fed32c"

# Back leg, braced behind the lunge.
f2.poly([(20,31),(27,34),(24,43),(18,50),(14,58),(8,58),(9,52),(13,46),(15,37)], INK)
f2.poly([(19,33),(24,35),(21,42),(17,48),(13,55),(10,55),(12,50),(15,44),(16,36)], CLOTH)
f2.rect(11,49,3,4,HI)
f2.poly([(9,55),(15,55),(14,59),(7,62),(3,62),(3,59)], INK)
f2.poly([(8,57),(13,57),(11,59),(5,61),(4,60)], CLOTH_DARK)
f2.set(5,58,HI)

# Forward leg: left foot plants far ahead, making the action readable.
f2.poly([(19,31),(27,31),(31,39),(34,47),(39,54),(48,56),(49,61),(44,63),(35,60),(30,55),(26,49),(21,44),(16,39)], INK)
f2.poly([(21,33),(26,34),(28,40),(32,48),(37,54),(34,57),(29,52),(25,47),(21,43),(18,38)], CLOTH)
f2.poly([(37,53),(42,55),(43,59),(37,60),(33,56)], CLOTH)
f2.poly([(42,55),(50,57),(52,61),(49,63),(39,62),(36,59)], INK)
f2.poly([(43,57),(49,59),(48,61),(40,60),(38,59)], CLOTH_DARK)
f2.set(45,58,HI)

# Tunic and leaning torso, pitched toward the cast.
f2.poly([(17,14),(28,14),(35,19),(37,25),(31,31),(27,38),(17,39),(10,36),(12,29),(14,21)], INK)
f2.poly([(18,15),(27,16),(33,20),(34,25),(29,30),(25,36),(17,37),(12,35),(14,29),(15,21)], SKIN)
f2.poly([(12,33),(22,33),(29,29),(27,36),(20,40),(11,39)], SHADOW)
f2.rect(15,36,11,3,DEEP)
f2.set(13,29,SKIN_DARK)
f2.set(14,25,SKIN_DARK)

# Head shifted forward and slightly down to reinforce the lean.
head = input_canvas.select(14, 0, 14, 16)
head.copy_to(20, 2, f2, mode="over")
# Neck connection and a sharper forward-facing jaw edge.
f2.poly([(21,13),(28,13),(29,18),(23,18),(19,15)], INK)
f2.poly([(22,13),(27,13),(27,17),(22,16)], SKIN)
f2.set(28,12,PALE)
f2.set(29,11,INK)

# Rear arm sweeps back for counterbalance.
f2.poly([(17,18),(12,21),(8,27),(4,31),(1,30),(3,25),(9,18),(15,15)], INK)
f2.poly([(16,19),(12,22),(8,28),(4,29),(6,25),(11,19),(15,17)], SKIN)
f2.set(5,27,SKIN_DARK)

# Casting arm: shoulder, sleeve, forearm and open pushing hand.
f2.poly([(29,18),(37,18),(42,20),(47,20),(47,26),(40,27),(34,25),(29,24)], INK)
f2.poly([(30,19),(36,20),(40,21),(40,25),(35,24),(30,23)], SKIN)
f2.rect(39,20,7,6,CLOTH_DARK)
f2.rect(40,21,6,4,PLUM)
f2.poly([(45,20),(54,20),(58,22),(57,25),(51,26),(45,25)], INK)
f2.poly([(46,21),(53,21),(56,23),(52,24),(46,24)], SKIN)
# Fingers visibly thrust into the spell.
f2.line(53,21,59,20,PALE)
f2.line(54,23,60,23,SKIN)
f2.line(53,25,58,26,SKIN_DARK)
f2.set(59,20,INK)
f2.set(60,23,INK)

# Fiery trail: broken, tapered stream from palm to the projectile.
f2.set(58,22,ORANGE)
f2.rect(60,21,3,3,ORANGE)
f2.rect(62,20,4,4,GOLD)
f2.set(63,19,ORANGE)
f2.set(61,24,ORANGE)
f2.rect(65,20,4,5,ORANGE)
f2.rect(66,21,4,3,GOLD)
f2.set(68,19,YELLOW)
f2.set(66,25,GOLD)

# Released flame, arrowing right with a hot core and jagged wake.
f2.poly([(67,18),(71,17),(70,14),(73,16),(75,13),(76,18),(79,17),(78,22),(79,25),(76,25),(77,29),(73,27),(71,31),(69,27),(65,27),(67,24),(64,22)], ORANGE)
f2.poly([(69,19),(72,18),(72,16),(74,19),(77,19),(75,22),(77,24),(73,24),(73,28),(70,25),(67,25),(69,22)], GOLD)
f2.poly([(71,20),(74,19),(74,21),(76,22),(73,23),(72,26),(70,24),(69,22)], YELLOW)
f2.set(78,20,GOLD)
f2.set(76,27,GOLD)
f2.set(66,19,ORANGE)

finish([f1, f2])
view(f1, scale=7, margin=1, edges="all")
view(f2, scale=7, margin=1, edges="all")
