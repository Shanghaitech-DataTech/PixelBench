c = new_canvas(64, 64, name="weapon_set")

outline = "#202536"
metal = "#c7d6df"
metal_hi = "#f4f0d8"
metal_sh = "#73889b"
wood = "#9b593b"
wood_hi = "#d28b50"
wood_sh = "#653d3d"
leather = "#557b63"
leather_hi = "#90ad72"
gold = "#e6b85c"

# Sword: diagonal blade, guard and wrapped grip.
c.poly([(3,25),(5,26),(23,8),(23,4),(19,4)], outline)
c.poly([(5,24),(7,24),(22,8),(22,6),(20,6)], metal)
c.poly([(7,23),(20,10),(20,8)], metal_hi)
c.poly([(3,24),(7,28),(9,26),(5,22)], outline)
c.poly([(4,24),(7,27),(8,26),(5,23)], gold)
c.poly([(7,28),(10,31),(13,28),(10,25)], outline)
c.poly([(9,28),(11,30),(12,28),(10,27)], wood)
c.line(10,28,14,24,wood_hi)
c.line(11,29,15,25,wood_sh)
c.circle(8,30,1,outline)
c.set(8,30,gold)

# Bow: chunky curved wooden limb with a taut string.
c.path("M 39 4 C 52 7 58 16 58 21 C 58 26 52 29 46 30 L 45 27 C 51 25 54 22 54 19 C 54 14 49 9 40 7 Z", outline)
c.path("M 40 6 C 49 9 54 14 54 19 C 54 22 51 25 46 27 L 46 25 C 50 23 52 21 52 19 C 52 15 48 11 40 8 Z", wood)
c.line(40,5,46,30,metal_hi)
c.line(40,5,47,17,gold)
c.line(47,17,46,30,gold)
c.poly([(39,3),(42,4),(41,8),(39,7)], outline)
c.poly([(39,4),(41,5),(40,7)], wood_hi)
c.poly([(44,28),(47,27),(48,30),(45,31)], outline)
c.poly([(45,29),(47,28),(47,30)], wood_hi)
c.line(46,17,55,14,outline)
c.poly([(55,14),(59,12),(56,16)], outline)
c.poly([(56,14),(58,13),(56,15)], metal)

# Shield: green face, warm rim and a central boss.
c.poly([(5,36),(13,34),(24,37),(24,47),(21,54),(15,60),(8,56),(4,49),(4,39)], outline)
c.poly([(7,38),(13,36),(22,39),(22,47),(19,53),(15,57),(10,54),(7,48)], wood)
c.poly([(9,39),(14,38),(20,40),(20,47),(18,52),(15,55),(11,52),(9,47)], leather)
c.poly([(10,40),(14,39),(18,41),(18,46),(16,51),(14,53),(12,50),(10,46)], leather_hi)
c.line(6,40,6,48,gold)
c.line(21,41,20,47,gold)
c.poly([(12,42),(15,40),(18,43),(17,48),(14,51),(11,48)], outline)
c.poly([(13,43),(15,42),(17,44),(16,47),(14,49),(12,47)], gold)
c.set(14,44,metal_hi)
c.set(8,43,outline)
c.set(20,45,outline)
c.set(14,54,wood_sh)

# Battle axe: broad double-edged head on a banded haft.
c.poly([(44,36),(49,36),(51,40),(55,38),(60,40),(59,45),(56,51),(51,53),(49,49),(46,49),(43,54),(39,51),(41,46),(43,41)], outline)
c.poly([(45,38),(49,38),(51,42),(55,40),(58,41),(57,45),(54,49),(51,50),(48,46),(45,47),(43,51),(41,50),(43,45)], metal_sh)
c.poly([(45,39),(48,39),(50,43),(54,41),(57,42),(55,45),(52,47),(49,44),(46,45),(44,49),(43,49),(45,44)], metal)
c.poly([(46,40),(48,40),(50,43),(54,42),(56,42),(53,44),(50,45),(48,43)], metal_hi)
c.poly([(46,46),(50,44),(51,50),(49,56),(47,61),(43,60),(45,55)], outline)
c.poly([(47,47),(49,46),(49,54),(46,59),(44,59),(46,54)], wood)
c.line(46,51,49,50,wood_hi)
c.line(45,56,48,55,wood_sh)
c.poly([(43,51),(47,51),(46,54),(42,54)], outline)
c.poly([(44,52),(46,52),(45,53),(43,53)], gold)
c.poly([(44,58),(47,59),(46,62),(42,61)], outline)
c.poly([(44,59),(46,60),(45,61),(43,60)], wood_hi)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
