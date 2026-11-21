from pixelbench_api import *

# 64x64 four-icon weapon sheet on transparency.
c = new_canvas(64, 64, background=None, name="weapon-set-icons")

INK = "#171827"
DEEP = "#30334b"
STEEL_D = "#667b8d"
STEEL = "#aebdca"
STEEL_L = "#e7eef2"
GOLD_D = "#92552a"
GOLD = "#e2a63a"
GOLD_L = "#ffd66b"
WOOD_D = "#603426"
WOOD = "#a85b3d"
WOOD_L = "#d48650"
RED_D = "#7f2f3c"
RED = "#c84b55"
RED_L = "#ed7373"

# SWORD (top-left), rising from lower-left to upper-right.
# Blade outline and stepped point.
c.poly([(6,23),(9,26),(20,15),(25,7),(26,4),(23,5),(15,10),(4,21)], INK)
c.poly([(8,22),(10,24),(21,13),(24,7),(22,8),(16,12)], STEEL)
c.poly([(10,21),(11,22),(21,12),(23,8),(20,11)], STEEL_L)
c.set(8,23, STEEL_D)
# Crossguard.
c.poly([(7,21),(10,24),(8,26),(6,25),(5,27),(3,25),(6,22)], INK)
c.poly([(7,22),(9,24),(7,25),(6,24),(5,25),(4,25),(7,23)], GOLD)
c.set(5,24, GOLD_L)
# Wrapped grip and pommel.
c.poly([(7,25),(10,27),(6,31),(3,31),(3,29)], INK)
c.poly([(7,27),(8,27),(5,30),(4,30)], WOOD)
c.set(7,27, WOOD_L); c.set(5,29, RED_L); c.set(6,28, RED)
c.poly([(2,29),(5,29),(7,31),(5,33),(2,32),(1,31)], INK)
c.rect(2,30,4,2,GOLD)
c.set(2,30,GOLD_L)

# BOW (top-right), taut bow with nocked arrow.
# String and bow outline.
c.line(40,5,40,28,INK)
c.line(41,6,41,15,"#d8c9a6"); c.line(41,17,41,27,"#d8c9a6")
# Pixel-stepped wooden limbs.
c.poly([(42,4),(47,6),(52,10),(56,15),(56,18),(52,23),(47,27),(42,29),(40,27),(45,24),(49,21),(52,17),(52,15),(49,11),(45,8),(40,6)], INK)
c.poly([(43,6),(47,8),(51,11),(54,15),(54,18),(51,22),(47,25),(43,27),(46,23),(49,20),(51,17),(51,15),(49,12),(46,9)], WOOD)
c.poly([(44,7),(47,9),(49,11),(47,10)], WOOD_L)
c.poly([(51,21),(48,24),(44,26),(47,23)], WOOD_D)
# Gold bindings at limb tips and grip.
c.rect(41,5,4,3,GOLD_D); c.rect(42,6,3,2,GOLD)
c.rect(41,26,4,3,GOLD_D); c.rect(42,26,3,2,GOLD)
c.rect(51,14,5,5,INK); c.rect(52,15,3,3,GOLD); c.set(52,15,GOLD_L)
# Arrow across the bow.
c.rect(36,15,23,3,INK)
c.rect(37,16,22,1,STEEL_L)
c.poly([(59,13),(63,16),(59,20),(58,18),(58,14)],INK)
c.poly([(59,15),(61,16),(59,18)],GOLD_L)
c.poly([(36,13),(41,16),(36,19)],INK)
c.poly([(37,15),(39,16),(37,17)],RED)

# SHIELD (bottom-left), heraldic kite shield.
c.poly([(5,36),(16,33),(27,36),(27,46),(24,54),(16,61),(8,54),(5,46)],INK)
c.poly([(8,38),(16,36),(24,38),(24,46),(21,52),(16,57),(11,52),(8,46)],GOLD_D)
c.poly([(10,39),(16,37),(22,39),(22,46),(20,51),(16,55),(12,51),(10,46)],RED)
# Split-tone face and central steel boss.
c.poly([(16,37),(22,39),(22,46),(20,51),(16,55)],RED_D)
c.poly([(10,39),(16,37),(16,40),(11,41)],RED_L)
c.poly([(14,42),(18,42),(20,46),(18,50),(14,50),(12,46)],INK)
c.poly([(15,43),(17,43),(19,46),(17,49),(15,49),(13,46)],STEEL)
c.set(14,45,STEEL_L); c.set(15,44,STEEL_L)
# Rivets.
for x,y in [(9,40),(23,40),(10,48),(22,48)]:
    c.set(x,y,GOLD_L)

# BATTLE AXE (bottom-right), diagonal haft and broad crescent head.
# Handle outline, lower-left to upper-right.
c.poly([(36,58),(39,61),(52,45),(49,42)],INK)
c.poly([(38,58),(39,59),(51,44),(50,43)],WOOD)
c.line(40,56,49,45,WOOD_L)
# Pommel.
c.poly([(34,58),(38,57),(41,60),(39,63),(36,62)],INK)
c.poly([(36,59),(38,58),(40,60),(38,61)],GOLD)
c.set(36,59,GOLD_L)
# Axe head dark silhouette and steel body.
c.poly([(45,38),(51,34),(58,35),(62,39),(59,45),(53,49),(47,47),(50,43),(48,41)],INK)
c.poly([(48,38),(52,36),(57,37),(60,39),(57,43),(53,46),(49,45),(52,42),(51,40)],STEEL_D)
c.poly([(52,36),(57,37),(59,39),(56,40),(52,39),(49,40),(48,38)],STEEL)
c.poly([(57,38),(59,39),(57,42),(55,43),(56,40)],STEEL_L)
# Reinforced gold socket.
c.poly([(47,40),(51,41),(54,45),(52,49),(49,47),(51,44),(48,43)],INK)
c.poly([(49,41),(51,42),(53,45),(52,47),(50,46),(51,44)],GOLD)
c.set(50,42,GOLD_L)

view(c, scale=8, margin=0)
finish(c)
