from pixelbench_api import *

# Mad cyborg scientist portrait, 64x64.
c = new_canvas(64, 64, background="#090d13", name="mad-cyborg-scientist")

# Compact palette.
BG2 = "#111925"; BG3 = "#1c2631"; INK = "#05070b"
STEEL0 = "#18242d"; STEEL1 = "#34444c"; STEEL2 = "#65747a"; STEEL3 = "#a7b2ae"
WHITE0 = "#5d6768"; WHITE1 = "#a9aeaa"; WHITE2 = "#e4e1d2"; WHITE3 = "#fff8df"
SKIN0 = "#542e2b"; SKIN1 = "#8d4c3c"; SKIN2 = "#c77855"; SKIN3 = "#efa06b"; SKIN4 = "#ffd092"
RED0 = "#42151b"; RED1 = "#8e2930"; TOOTH = "#ead8b4"
CYAN0 = "#075c6d"; CYAN1 = "#00b7c7"; CYAN2 = "#62ffff"; CYAN3 = "#d4ffff"
COAT0 = "#353b3a"; COAT1 = "#6f746b"; COAT2 = "#b0ad97"
LEATHER0 = "#241817"; LEATHER1 = "#533426"; LEATHER2 = "#8b5933"; BRASS = "#d49a43"
ACID = "#a8d645"

# Background lab gloom: pipes, panel, warning glints.
c.rect(4, 0, 5, 39, BG2)
c.rect(5, 0, 2, 39, BG3)
c.rect(0, 36, 17, 3, BG3)
c.rect(53, 3, 7, 21, BG2)
c.rect(55, 5, 3, 17, STEEL0)
c.set(56, 8, STEEL2); c.set(56, 18, STEEL2)
c.line(1, 51, 12, 40, BG3); c.line(59, 27, 63, 23, BG3)
c.set(11, 8, ACID); c.set(12, 9, ACID); c.set(3, 44, BRASS)

# Hair/back-head silhouette.
c.poly([(15,15),(18,9),(23,8),(24,4),(28,7),(31,2),(34,7),(40,4),(40,9),(47,10),(51,17),(50,32),(45,40),(25,42),(15,32)], INK)

# Wild white hair, broad clustered silhouette.
c.poly([(13,18),(17,12),(15,9),(22,10),(21,5),(27,8),(31,2),(34,8),(40,4),(39,10),(47,8),(44,14),(51,15),(46,20),(37,17),(31,19),(24,15),(19,21)], WHITE1)
c.poly([(15,16),(19,12),(18,10),(24,12),(24,7),(29,11),(31,4),(34,11),(39,7),(37,13),(44,11),(42,16),(48,15),(44,19),(36,16),(29,18),(23,14),(19,19)], WHITE3)
c.poly([(15,18),(19,14),(23,16),(20,21)], WHITE0)
c.poly([(33,9),(39,7),(37,14),(43,12),(41,17),(34,15)], WHITE2)

# Brain electrode plugs and leads.
c.line(22,10,20,3, STEEL2); c.rect(18,1,5,3, STEEL1); c.rect(19,0,3,2, BRASS)
c.line(38,10,43,3, STEEL2); c.rect(41,1,5,4, STEEL1); c.rect(42,0,3,2, CYAN1)
c.line(26,9,27,5, INK); c.line(40,8,45,6, CYAN0)

# Neck shadow.
c.poly([(22,35),(43,35),(46,48),(19,48)], SKIN0)
c.rect(25,37,18,11, SKIN1)

# Human half of face.
c.poly([(18,18),(25,14),(34,16),(35,35),(31,41),(23,38),(18,31)], SKIN2)
c.poly([(19,19),(25,15),(31,16),(29,20),(31,24),(29,28),(32,32),(29,38),(23,36),(19,30)], SKIN3)
# Human lit cheek and brow.
c.poly([(20,20),(25,17),(30,18),(28,22),(23,23)], SKIN4)
c.poly([(19,26),(22,24),(29,25),(27,29),(22,31),(19,29)], SKIN3)
c.set(20,26, SKIN4); c.set(21,29, SKIN4)
# Human ear.
c.rect(15,23,4,9, SKIN1); c.set(16,25, SKIN3); c.set(17,29, SKIN0)

# Central facial divide and robotic skull half.
c.poly([(34,15),(44,14),(49,19),(49,31),(44,38),(35,41),(33,34)], STEEL0)
c.poly([(36,16),(44,15),(48,20),(47,27),(49,31),(43,37),(36,39)], STEEL1)
c.poly([(38,17),(45,17),(47,21),(45,24),(37,23)], STEEL2)
c.poly([(45,27),(48,29),(44,35),(38,38),(39,32)], STEEL2)
# Plating highlights and seams.
c.line(35,16,35,38, STEEL3); c.set(36,19, WHITE3)
c.line(43,16,47,20, STEEL3); c.line(46,29,42,36, STEEL3)
c.line(39,25,47,25, INK); c.line(41,16,41,19, INK)
c.rect(47,22,3,7, STEEL0); c.set(49,24, BRASS); c.set(48,29, INK)

# Eyes: human squint and blazing cyber eye.
c.line(21,23,29,22, SKIN0); c.rect(23,23,5,2, INK); c.set(26,23, WHITE2); c.set(24,24, RED1)
c.rect(37,20,10,7, INK)
c.poly([(38,22),(41,19),(46,21),(47,24),(44,27),(39,26)], CYAN0)
c.rect(40,21,5,5, CYAN1); c.rect(41,21,4,4, CYAN2); c.rect(42,22,2,2, CYAN3)
c.set(39,20, CYAN1); c.set(47,22, CYAN1); c.set(48,24, CYAN0)

# Nose split.
c.poly([(31,23),(34,24),(34,31),(29,31),(31,29)], SKIN1)
c.line(35,23,37,31, STEEL3); c.line(37,31,34,32, INK)

# Maniacal grin spanning both halves.
c.poly([(21,31),(27,33),(34,32),(42,30),(45,33),(40,38),(33,40),(26,38)], RED0)
c.poly([(23,33),(29,34),(35,33),(42,32),(40,35),(34,37),(27,36)], TOOTH)
c.line(28,33,28,36, SKIN0); c.line(34,33,34,37, SKIN0); c.line(39,32,39,35, INK)
c.line(27,38,34,39, RED1); c.set(23,32, SKIN4); c.set(42,31, STEEL3)

# Coat silhouette and shoulders.
c.poly([(18,41),(8,46),(4,63),(57,63),(54,47),(45,42),(39,43),(33,49),(26,43)], COAT0)
c.poly([(17,43),(9,47),(6,63),(22,63),(24,48)], COAT2)
c.poly([(46,43),(54,47),(59,63),(44,63),(41,49)], COAT1)
# Dirty shadow patches on coat.
c.poly([(9,52),(15,48),(18,51),(15,57),(8,58)], COAT1)
c.rect(7,60,12,3, COAT0); c.poly([(47,48),(53,50),(54,56),(48,54)], COAT2)
c.set(12,50, LEATHER2); c.set(17,58, SKIN1); c.set(50,52, LEATHER1)

# Lapels.
c.poly([(20,41),(27,45),(24,57),(16,46)], WHITE1)
c.poly([(39,42),(34,48),(41,56),(47,44)], COAT2)
c.line(17,46,23,55, WHITE3); c.line(46,44,40,54, WHITE0)

# Leather apron over chest.
c.poly([(25,45),(34,49),(40,45),(45,63),(20,63)], LEATHER0)
c.poly([(28,47),(34,51),(39,47),(41,63),(24,63)], LEATHER1)
c.line(28,47,24,63, LEATHER2); c.line(39,47,42,63, INK)
c.rect(28,53,10,2, LEATHER2); c.set(29,54, BRASS); c.set(37,54, BRASS)

# Tool belt and tiny tools.
c.rect(14,57,34,5, LEATHER0); c.rect(15,58,32,3, LEATHER2)
c.rect(30,57,6,5, BRASS); c.rect(31,58,4,3, LEATHER0)
c.rect(18,55,2,7, STEEL3); c.set(18,54, CYAN1)
c.rect(42,55,2,7, STEEL2); c.rect(44,56,3,5, LEATHER1)

# Exposed robotic right arm, angled into foreground.
c.poly([(50,45),(56,43),(61,48),(60,56),(55,59),(49,54)], INK)
c.poly([(51,46),(55,44),(59,48),(58,53),(54,56),(50,53)], STEEL1)
c.poly([(54,45),(58,48),(57,51),(52,51)], STEEL3)
c.rect(51,51,8,3, STEEL0); c.set(52,52, CYAN1); c.set(58,50, BRASS)
# Wrist joint.
c.poly([(52,54),(58,52),(61,56),(58,60),(52,58)], STEEL2)
c.rect(54,55,5,3, STEEL3); c.set(55,56, INK); c.set(59,56, BRASS)
# Prosthetic hand and articulated fingers.
c.poly([(53,58),(57,57),(61,59),(60,63),(52,63),(49,61)], STEEL1)
c.rect(53,59,6,4, STEEL2); c.set(54,60, STEEL3)
c.line(53,60,49,57, STEEL3); c.line(52,62,47,60, STEEL2)
c.line(58,60,63,58, STEEL3); c.line(59,62,63,62, STEEL2)
c.set(48,57, BRASS); c.set(46,60, BRASS); c.set(63,58, INK)
# Loose cables from elbow/hand.
c.line(51,48,61,43, RED1); c.line(61,43,63,45, RED1)
c.line(50,50,61,46, CYAN0); c.set(62,46, CYAN2)
c.line(51,57,47,54, INK); c.line(47,54,45,57, CYAN1)

# Final high-contrast rim pixels and grime.
c.line(8,47,6,55, WHITE0); c.set(7,48, WHITE3)
c.set(14,54, INK); c.set(11,57, INK); c.set(47,52, INK)
c.set(5,60, BRASS); c.set(59,38, CYAN0); c.set(60,37, CYAN2)

view(c, scale=8, margin=0)
finish(c)
