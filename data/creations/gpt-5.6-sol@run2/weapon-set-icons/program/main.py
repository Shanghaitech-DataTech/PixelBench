from pixelbench_api import new_canvas, view, finish

# 64x64 transparent weapon icon sheet, arranged as a 2x2 grid.
c = new_canvas(64, 64, background=None, name="weapon-set-icons")

OUT = "#171923"
DEEP = "#282b38"
STEEL = "#aeb9c6"
LIGHT = "#e7edf3"
SHADE = "#687789"
GOLD = "#d99a2b"
GOLD_HI = "#ffd166"
WOOD = "#8f4f2a"
WOOD_HI = "#c87838"
RED = "#a9343f"
RED_HI = "#dc4d57"

# --- Sword, upper-left: rising diagonal ---
# Outer blade silhouette and point.
c.poly([(6,24),(9,27),(25,11),(26,5),(20,7),(5,22)], OUT)
# Blade body.
c.poly([(9,23),(11,24),(23,12),(24,8),(21,9),(8,22)], STEEL)
# Blade lit edge.
c.poly([(10,21),(21,10),(23,9),(22,12),(11,23)], LIGHT)
# Blade shadow edge.
c.line(11,24,24,11,SHADE)
# Guard, dark then gold.
c.poly([(6,19),(8,17),(15,24),(13,27)], OUT)
c.poly([(8,19),(9,18),(14,24),(13,25)], GOLD)
c.set(9,19,GOLD_HI); c.set(10,20,GOLD_HI)
# Grip.
c.poly([(5,24),(8,21),(13,26),(10,30),(7,30),(3,27)], OUT)
c.poly([(6,24),(8,23),(11,26),(9,29),(7,28),(5,27)], WOOD)
c.set(7,24,WOOD_HI); c.set(8,25,WOOD_HI)
# Pommel.
c.rect(4,27,4,4,OUT); c.rect(5,27,2,2,GOLD); c.set(5,27,GOLD_HI)

# --- Bow and arrow, upper-right ---
# Bow outer stepped curve.
c.line(39,7,43,5,OUT); c.line(43,5,48,5,OUT)
c.line(39,7,36,11,OUT); c.line(36,11,35,16,OUT)
c.line(35,16,36,21,OUT); c.line(36,21,39,26,OUT)
c.line(39,26,43,29,OUT); c.line(43,29,48,29,OUT)
# Warm inner bow highlights.
c.line(40,8,44,6,WOOD_HI); c.line(44,6,47,6,WOOD)
c.line(40,8,38,11,WOOD_HI); c.line(38,11,37,16,WOOD)
c.line(37,17,38,21,WOOD); c.line(38,21,40,24,WOOD_HI)
c.line(40,24,44,27,WOOD_HI); c.line(44,27,47,27,WOOD)
# String.
c.line(48,6,44,16,SHADE); c.line(44,16,48,28,SHADE)
c.set(47,8,LIGHT); c.set(47,26,LIGHT)
# Arrow shaft and dark outline.
c.line(32,16,55,16,OUT); c.line(33,15,55,15,OUT); c.line(33,17,55,17,OUT)
c.line(34,16,54,16,GOLD_HI)
# Arrow head.
c.poly([(54,12),(61,16),(54,20),(55,17),(52,16),(55,15)],OUT)
c.poly([(55,14),(59,16),(55,18),(56,16)],STEEL); c.set(57,15,LIGHT)
# Fletching.
c.poly([(34,16),(30,12),(36,14),(37,16),(36,18),(30,20)],OUT)
c.poly([(34,15),(32,13),(36,15)],RED_HI); c.poly([(34,17),(32,19),(36,17)],RED)

# --- Shield, lower-left ---
# Strong symmetrical silhouette.
c.poly([(7,36),(16,33),(25,36),(25,47),(22,54),(16,59),(10,54),(7,47)],OUT)
# Rim.
c.poly([(9,38),(16,35),(23,38),(23,47),(20,52),(16,56),(12,52),(9,47)],GOLD)
# Face.
c.poly([(11,39),(16,37),(21,39),(21,47),(19,51),(16,54),(13,51),(11,47)],RED)
# Face lighting/shadow.
c.poly([(11,39),(16,37),(16,52),(13,50),(11,46)],RED_HI)
c.poly([(16,37),(21,39),(21,47),(19,51),(16,54)],"#7f2935")
# Central boss and cross-like reinforcement.
c.rect(15,39,3,14,GOLD); c.rect(11,44,11,3,GOLD)
c.rect(16,40,1,12,GOLD_HI); c.rect(12,44,9,1,GOLD_HI)
c.rect(14,43,5,5,OUT); c.rect(15,44,3,3,STEEL); c.set(15,44,LIGHT)
# Rim glints.
c.set(10,38,GOLD_HI); c.set(11,37,GOLD_HI); c.set(12,36,GOLD_HI)
c.set(9,40,GOLD_HI); c.set(22,47,"#9e681f")

# --- Battle axe, lower-right: diagonal haft ---
# Haft outline and body.
c.poly([(36,58),(33,55),(51,36),(55,39)],OUT)
c.poly([(37,56),(35,55),(51,38),(53,39)],WOOD)
c.line(38,54,52,39,WOOD_HI)
# End cap.
c.poly([(33,53),(38,58),(36,61),(31,57)],OUT)
c.poly([(34,54),(37,57),(35,59),(33,57)],GOLD); c.set(34,55,GOLD_HI)
# Axe head dark silhouette, broad double-bit.
c.poly([(47,34),(53,31),(60,33),(61,38),(57,43),(52,42),(49,45),(44,43),(42,38)],OUT)
# Left blade.
c.poly([(48,35),(52,33),(53,39),(49,43),(45,41),(44,38)],STEEL)
c.poly([(46,37),(51,34),(51,38),(48,41),(45,40)],LIGHT)
# Right blade.
c.poly([(54,33),(59,34),(59,38),(56,41),(53,40)],SHADE)
c.poly([(56,34),(58,35),(58,37),(56,39)],STEEL)
# Golden socket.
c.poly([(51,34),(55,33),(56,40),(52,43),(50,40)],GOLD)
c.poly([(52,35),(54,34),(54,40),(52,41)],GOLD_HI)
c.rect(50,39,7,3,OUT,fill=False)
# Small edge glints.
c.set(45,38,LIGHT); c.set(46,37,LIGHT); c.set(58,35,LIGHT)

view(c, scale=8, margin=1, edges="all")
finish(c)
