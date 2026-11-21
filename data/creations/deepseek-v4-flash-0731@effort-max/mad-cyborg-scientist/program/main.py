from pixelbench_api import new_canvas, finish

# ---------------- palette ----------------
BG="#0c0e18"; BG2="#141b34"; RIM="#ffd9a6"
SKIN_L="#f0bd90"; SKIN="#ca915f"; SKIN_S="#8d5d39"; SKIN_D="#57371f"
STEEL_L="#e2e7ef"; STEEL="#a9b1c0"; STEEL_D="#5d6475"; STEEL_DK="#252b3a"
HAIR="#f5f2ea"; HAIR_S="#c9c3b4"; HAIR_D="#8e887a"
GLOW="#00eaff"; GLOW_D="#15505e"; GLOW_C="#d9fbff"
EYE_W="#f7f2e9"; PUPIL="#241a10"
MOUTH="#451f18"; TEETH="#f0e7d4"
CAB_R="#d84a2e"; CAB_Y="#e2b52c"; CAB_G="#43b05f"; CAB_B="#3f7fd4"; CABK="#343940"; CAB_H="#8a94a2"
COAT_L="#eae6da"; COAT="#bab5a4"; DIRT="#8e8776"; COAT_D="#636052"; STAIN="#7c5c38"
LEA="#70411f"; LEA_D="#462708"; LEA_H="#94643e"
BELT="#241a0e"; BUCK="#d2a83c"

c = new_canvas(64, 64)
c.rect(0, 0, 64, 64, BG)
c.circle(32, 30, 20, BG2)

# ---------------- neck ----------------
c.poly([(25,44),(38,44),(38,51),(25,51)], SKIN_S)
c.rect(31,44,7,7, STEEL_D)
c.line(33,45,37,45, STEEL_DK)

# ---------------- head base ----------------
c.ellipse(32, 30, 15, 16, SKIN)
c.line(22,43,41,43, SKIN_D)

# ---------------- hair ----------------
c.circle(24, 16, 10, HAIR)
c.poly([(12,12),(15,7),(19,11),(22,6),(26,10),(30,5),(34,9),(38,5),(42,9),(46,13),(46,18),(49,23),(45,27),(47,31),(43,33),(39,30),(35,33),(31,30),(27,32),(23,28),(19,31),(15,26),(12,21),(12,12)], HAIR)
c.circle(33, 13, 8, HAIR)
c.set(46,14,HAIR_S); c.set(47,16,HAIR_S); c.set(47,19,HAIR_S)

# ---------------- robot plates (right) ----------------
c.poly([(32,14),(35,10),(40,10),(44,13),(47,17),(47,24),(44,28),(39,29),(35,28),(32,25),(32,14)], STEEL_D)
c.line(34,12,43,12, STEEL)
c.line(47,17,47,24, STEEL)
c.poly([(32,24),(35,28),(40,29),(45,27),(47,24),(47,41),(44,45),(39,46),(35,45),(32,42),(32,24)], STEEL_D)
c.line(32,13,32,44, STEEL_DK)
c.line(33,20,45,20, STEEL_DK)   # forehead panel crease
# patches of hair over metal
c.set(42,13,HAIR); c.set(43,14,HAIR_S); c.set(41,15,HAIR); c.set(40,16,HAIR_S)

# ---------------- glowing cybernetic eye ----------------
c.circle(38, 27, 4, GLOW_D)
c.circle(38, 27, 3, GLOW)
c.circle(38, 27, 2, GLOW)
c.set(38,27,GLOW_C); c.set(37,26,GLOW_C)
c.line(34,22,45,22, STEEL_DK)
c.line(35,21,44,21, STEEL)
c.set(43,26,GLOW); c.set(44,25,GLOW)
c.set(42,31,GLOW_D); c.set(43,30,GLOW_D)
c.line(33,33,43,33, STEEL_DK)

# ---------------- human face left ----------------
c.line(19,22,29,23, HAIR_S)
c.line(19,23,28,24, HAIR_D)
c.ellipse(24, 26, 3, 2, EYE_W)
c.set(24,26,SKIN_D); c.set(25,26,PUPIL)
c.set(23,29,SKIN_L)
c.line(27,30,26,35, SKIN_S)
c.set(27,35,SKIN_D)
c.set(21,33,SKIN_L); c.set(20,34,SKIN_L)
c.line(25,33,21,36, SKIN_S)
c.line(20,23,20,26, HAIR_D)
c.line(18,25,20,29, HAIR_S)

# ---------------- mouth (wide grin) ----------------
c.poly([(15,37),(18,36),(23,37),(28,36),(33,37),(38,36),(44,37),(43,42),(33,43),(26,42),(19,43),(15,41)], MOUTH)
for x in (16,19,22,25,28,31,34,37,40,42):
    c.set(x,37,TEETH)
c.set(34,42,TEETH); c.set(37,42,TEETH); c.set(40,42,TEETH)
c.line(20,43,33,43, SKIN_D)
# robot jaw seam
c.line(36,45,44,45, STEEL_DK)

# ---------------- ear + cables ----------------
c.rect(46,23,5,12, STEEL_D)
c.rect(47,25,3,8, STEEL_DK)
c.set(48,27,STEEL); c.set(48,30,STEEL)
c.set(48,26,CAB_Y)
c.line(50,26,52,30,CABK); c.line(52,30,51,35,CABK)
c.line(51,35,53,39,CABK); c.line(53,39,52,43,CABK)
c.set(52,37,CAB_R); c.set(53,41,CAB_Y)

# ---------------- brain electrode plugs ----------------
for (px,py,led) in [(35,8,CAB_G),(39,7,CAB_B),(43,9,CAB_R),(37,13,CAB_Y)]:
    c.circle(px, py, 1, STEEL)
    c.set(px, py, led)
c.line(39,7,44,4,CABK); c.line(43,9,47,6,CABK); c.line(35,8,32,5,CABK)
c.line(44,4,48,6,CABK); c.set(47,6,CABK)
c.set(40,6,CAB_H)

# ---------------- coat / torso ----------------
c.poly([(0,52),(6,49),(15,48),(24,50),(31,52),(40,51),(48,50),(56,51),(63,54),(63,63),(0,63)], COAT)
c.circle(6,55,3, DIRT)
c.circle(9,59,3, STAIN)
c.circle(13,56,2, STAIN)
c.rect(1,56,4,7, COAT_L)
c.set(2,59,CAB_B); c.set(2,60,CAB_B)
c.line(0,53,7,51, COAT_D); c.line(0,55,8,53, COAT_D)
# right chest metal plate
c.poly([(38,49),(47,50),(48,57),(44,61),(38,60),(36,55),(37,51)], STEEL_D)
c.line(38,53,46,54, STEEL_DK); c.line(38,58,43,60, STEEL_DK)

# ---------------- apron ----------------
c.poly([(22,52),(41,52),(38,63),(25,63)], LEA)
c.rect(25,53,2,9, LEA_H)
c.rect(36,53,2,9, LEA_D)

# ---------------- tool belt ----------------
c.rect(15,56,32,4, BELT)
c.rect(27,56,7,4, BUCK)
c.rect(29,57,3,2, BELT)
c.line(30,56,30,59, BELT)
c.rect(19,53,2,4, LEA_D); c.rect(17,51,6,2, STEEL); c.set(17,50,STEEL_D)
c.set(40,53,CAB_Y); c.set(41,54,CAB_R)

# ---------------- robotic arm ----------------
c.circle(45, 50, 4, STEEL_D)
c.circle(43, 48, 2, STEEL)
c.poly([(42,51),(51,52),(51,58),(43,57)], STEEL)
c.line(43,54,51,55, STEEL_DK)
c.line(43,57,51,58, STEEL_DK)
c.line(44,52,50,53, STEEL_L)
c.poly([(44,57),(52,58),(51,61),(43,60)], STEEL)
c.rect(45,60,8,3, STEEL_L)
c.rect(48,57,3,4, STEEL_D)
c.rect(52,57,3,4, STEEL)
c.set(49,57,STEEL_DK); c.set(50,57,STEEL)
c.set(53,57,STEEL_DK)
c.line(49,61,47,62,CAB_Y); c.line(47,62,46,63,CAB_Y)
c.line(52,61,52,63,CAB_B)
c.line(54,61,56,63,CAB_G)
c.set(51,61,CAB_R); c.set(50,62,CAB_R)
c.set(45,61,STEEL_DK)

# ---------------- rim light (strong left light) ----------------
for y in range(12, 26):
    c.set(12, y, RIM)
c.set(13,26,RIM); c.set(13,27,RIM)
c.set(18,30,RIM); c.set(17,31,RIM); c.set(17,32,RIM); c.set(16,33,RIM)
c.set(5,50,RIM); c.set(14,49,RIM)
c.set(14,10,HAIR); c.set(15,13,HAIR); c.set(19,9,HAIR)
c.set(13,10,RIM); c.set(14,12,RIM)

print(c.stats_text())
print(c.matrix_text())
finish(c)
