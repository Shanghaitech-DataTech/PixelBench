# Dim sum chef sprite, 32x32, transparent background.
result = new_canvas(32, 32, background=None, name="dim-sum-chef")

# Compact palette.
INK = "#2b2530"
DEEP = "#55383a"
SKIN_D = "#b96f58"
SKIN = "#e6a071"
SKIN_HI = "#ffd0a0"
WHITE_D = "#b9c4c5"
WHITE = "#eef0df"
WHITE_HI = "#fffbe9"
RED_D = "#8f3337"
RED = "#c94b45"
BAMBOO_D = "#8b552c"
BAMBOO = "#c8893e"
BAMBOO_HI = "#edb85b"
BUN_D = "#d8d2b7"
BUN = "#fff2cf"
FLOUR = "#ffffff"

# Feet and trouser shadows behind the coat.
result.rect(10, 27, 5, 3, INK)
result.rect(17, 27, 5, 3, INK)
result.rect(9, 30, 6, 2, DEEP)
result.rect(17, 30, 6, 2, DEEP)
result.set(9, 30, None).set(22, 30, None)

# Chef coat silhouette and sleeves.
result.poly([(7,16),(11,14),(21,14),(25,16),(29,22),(27,27),(23,27),(22,30),(10,30),(9,27),(5,27),(3,22)], INK)
result.poly([(8,17),(12,15),(20,15),(24,17),(26,25),(22,27),(10,27),(6,25)], WHITE_D)
result.poly([(9,17),(15,16),(15,27),(10,27),(7,24)], WHITE)
result.poly([(17,16),(21,16),(25,20),(24,25),(17,27)], WHITE_HI)
# Sleeve cuffs / red neckerchief.
result.poly([(12,15),(16,17),(20,15),(19,19),(16,20),(13,19)], RED_D)
result.poly([(14,16),(16,17),(18,16),(18,18),(16,19),(14,18)], RED)

# Ears and head outline.
result.rect(7, 9, 3, 7, INK)
result.rect(22, 9, 3, 7, INK)
result.rect(8, 8, 16, 9, INK)
result.set(8,8,None).set(23,8,None)
result.rect(8, 10, 2, 4, SKIN_D)
result.rect(22, 10, 2, 4, SKIN_D)
result.set(8,11,SKIN).set(23,11,SKIN)
result.rect(10, 8, 12, 8, SKIN)
result.rect(11, 9, 10, 6, SKIN_HI)
# Hairline / brows / eyes / nose.
result.rect(10, 8, 12, 2, DEEP)
result.set(11,10,DEEP).set(20,10,DEEP)
result.rect(12, 11, 2, 1, INK)
result.rect(18, 11, 2, 1, INK)
result.set(13,12,WHITE_HI).set(18,12,WHITE_HI)
result.set(16,12,SKIN_D).set(15,13,SKIN_D).set(16,13,SKIN_D)
# Friendly moustache and smile.
result.rect(12, 14, 3, 1, DEEP)
result.rect(17, 14, 3, 1, DEEP)
result.set(15,15,INK).set(16,15,INK)
result.set(14,14,SKIN_HI).set(17,14,SKIN_HI)

# Tall chef toque, dark stepped outline.
result.poly([(9,9),(8,8),(8,5),(10,5),(10,3),(12,3),(12,1),(15,1),(16,2),(17,1),(20,1),(20,3),(22,3),(22,5),(24,5),(24,8),(23,9)], INK)
result.poly([(10,8),(9,7),(9,6),(11,6),(11,4),(13,4),(13,2),(15,2),(16,4),(17,4),(18,2),(20,2),(20,4),(22,4),(22,6),(23,6),(22,8)], WHITE)
result.rect(10, 7, 12, 2, WHITE_D)
result.rect(11, 7, 10, 1, WHITE_HI)
result.set(12,3,WHITE_HI).set(19,3,WHITE_HI)

# Apron panel visible around the steamer.
result.poly([(11,19),(21,19),(23,28),(21,30),(11,30),(9,28)], INK)
result.poly([(12,19),(20,19),(21,28),(20,29),(12,29),(11,28)], WHITE_HI)
# Flour dust on apron.
for x, y in [(12,21),(19,21),(13,24),(18,25),(11,26),(20,27),(15,28)]:
    result.set(x, y, FLOUR)
result.set(13,22,WHITE_D).set(19,23,WHITE_D)

# Steamer rear rim and three clearly separated buns.
result.rect(6, 20, 20, 4, INK)
result.rect(7, 20, 18, 2, BAMBOO_D)
# Buns outlined individually above the basket.
result.poly([(8,20),(8,18),(9,17),(12,17),(13,18),(13,20)], INK)
result.poly([(9,20),(9,18),(10,17),(12,18),(12,20)], BUN)
result.set(10,18,BUN_D).set(11,17,WHITE_HI)
result.poly([(13,20),(13,17),(15,16),(17,16),(19,17),(19,20)], INK)
result.poly([(14,20),(14,18),(15,17),(17,17),(18,18),(18,20)], BUN)
result.set(15,18,BUN_D).set(16,16,WHITE_HI)
result.poly([(19,20),(19,18),(20,17),(23,17),(24,18),(24,20)], INK)
result.poly([(20,20),(20,18),(21,17),(23,18),(23,20)], BUN)
result.set(21,18,BUN_D).set(22,17,WHITE_HI)

# Reinforce bun folds and silhouette so the food does not merge into the coat.
result.line(9, 20, 12, 20, BUN_D)
result.line(14, 20, 18, 20, BUN_D)
result.line(20, 20, 23, 20, BUN_D)
result.set(10,18,WHITE_HI).set(16,17,WHITE_HI).set(22,18,WHITE_HI)
result.set(11,19,BUN_D).set(15,19,BUN_D).set(17,19,BUN_D).set(21,19,BUN_D)
# Flour dust remains visible above and beside the tray.
result.set(8,18,FLOUR).set(23,19,FLOUR).set(10,17,FLOUR).set(21,16,FLOUR)

# Hands wrap around the outside of the steamer, separated by dark cuffs.
result.rect(3, 20, 4, 6, INK)
result.rect(25, 20, 4, 6, INK)
result.poly([(4,21),(7,21),(8,23),(7,26),(5,26),(4,24)], SKIN)
result.poly([(24,23),(25,21),(28,21),(28,24),(27,26),(25,26)], SKIN)
result.set(5,21,SKIN_HI).set(26,21,SKIN_HI)
result.line(5,24,7,24,SKIN_D)
result.line(25,24,27,24,SKIN_D)

# Bamboo steamer front: bold rim, slatted body, and base.
result.rect(6, 21, 20, 2, BAMBOO_HI)
result.rect(6, 23, 20, 6, INK)
result.rect(7, 23, 18, 5, BAMBOO)
result.rect(7, 23, 18, 1, BAMBOO_HI)
result.rect(7, 27, 18, 1, BAMBOO_D)
for x in (10, 15, 20):
    result.rect(x, 24, 1, 3, BAMBOO_D)
result.set(8,24,BAMBOO_HI).set(13,24,BAMBOO_HI).set(18,24,BAMBOO_HI).set(23,24,BAMBOO_HI)
result.rect(8, 28, 16, 1, BAMBOO_D)

# Apron flap below the basket, visibly dusted with flour.
result.rect(11, 29, 10, 2, INK)
result.rect(12, 29, 8, 2, WHITE)
result.set(13,29,FLOUR).set(16,30,FLOUR).set(19,29,WHITE_D)

view(result, scale=16, margin=1, edges="all")
finish(result)
