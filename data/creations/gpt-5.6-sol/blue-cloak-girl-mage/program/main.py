# 64x64 anime-style girl mage sprite
c = new_canvas(64, 64, background=None, name="blue-cloak-girl-mage")

# Palette
outline = "#10152a"
deep = "#172342"
blue0 = "#1d315b"
blue1 = "#294878"
blue2 = "#38639a"
blue3 = "#527db0"
cloth_shadow = "#253454"
hair_dark = "#7a563f"
hair = "#b9855b"
hair_light = "#d9ad79"
skin_dark = "#b96855"
skin = "#e49a7f"
skin_light = "#ffc2a0"
white_shadow = "#aab9c9"
white = "#eef4ef"
white_hi = "#ffffff"
amber_dark = "#9b4b16"
amber = "#e8881d"
amber_hi = "#ffd45a"
glow = "#ffb52e"

# Staff glow motes behind the figure
for x, y, col in [(53,8,amber),(57,12,amber_hi),(54,18,glow),(59,22,amber),(48,5,amber_hi),(51,25,amber_dark)]:
    c.set(x,y,col)
c.rect(55,6,2,2,amber)
c.set(57,5,amber_hi)
c.set(47,12,amber)

# Back hair silhouette
c.rect(25,7,12,3,outline)
c.rect(22,10,18,11,outline)
c.rect(23,19,16,8,outline)
c.rect(24,26,5,5,outline)
c.rect(35,25,4,6,outline)
# Hair mass
c.rect(25,7,10,2,hair_dark)
c.rect(23,10,15,10,hair)
c.rect(24,18,13,8,hair_dark)
c.rect(25,21,4,7,hair)
c.rect(34,20,3,8,hair)
c.rect(24,11,2,8,hair_light)
c.rect(26,9,8,2,hair_light)
c.rect(36,12,2,6,hair_dark)

# Neck behind collar
c.rect(28,22,7,5,outline)
c.rect(29,22,5,5,skin)
c.rect(30,23,4,3,skin_light)

# Cloak strong outer silhouette
c.poly([(22,24),(17,28),(14,39),(13,51),(18,54),(23,52),(25,56),(38,56),(40,52),(46,54),(49,50),(47,37),(43,28),(37,24)], outline)
# Cloak fill
c.poly([(23,26),(19,29),(16,39),(15,49),(19,52),(24,49),(27,53),(36,53),(39,49),(45,52),(47,49),(45,38),(41,29),(36,26)], blue0)
# Shoulder planes
c.poly([(23,26),(18,30),(16,39),(22,40),(27,28)], blue1)
c.poly([(36,26),(41,29),(45,38),(40,40),(33,28)], blue1)
c.poly([(18,31),(16,38),(20,37),(24,29)], blue2)
c.poly([(41,30),(44,37),(40,36),(37,28)], blue2)
# Long cloak folds
c.poly([(25,31),(28,31),(27,51),(23,49)], deep)
c.poly([(34,31),(38,32),(41,49),(36,51)], deep)
c.poly([(29,32),(33,32),(34,52),(29,52)], blue1)
c.line(31,34,31,51,blue2)
c.line(22,41,20,49,blue3)
c.line(40,41,43,49,blue3)
# Hem notches and dark edge
c.rect(18,51,7,2,outline)
c.rect(26,53,11,3,outline)
c.rect(39,51,7,2,outline)
c.rect(20,50,4,2,blue1)
c.rect(28,52,7,2,blue1)
c.rect(40,50,4,2,blue1)

# Cape clasp and collar
c.poly([(22,24),(27,23),(31,27),(25,31)], outline)
c.poly([(37,24),(34,23),(31,27),(38,31)], outline)
c.poly([(23,25),(27,24),(30,27),(25,29)], blue2)
c.poly([(36,25),(34,24),(32,27),(37,29)], blue2)
c.rect(29,26,5,4,outline)
c.rect(30,27,3,2,amber)
c.set(31,27,amber_hi)

# Face over hair
c.rect(25,11,11,11,outline)
c.rect(24,13,13,5,outline)
c.rect(26,11,9,11,skin)
c.rect(25,13,11,5,skin)
c.rect(27,12,8,8,skin_light)
c.rect(26,18,10,3,skin)
# Hair fringe over forehead
c.poly([(24,10),(36,10),(36,13),(33,12),(32,15),(30,12),(28,15),(27,12),(24,14)], hair)
c.rect(25,10,10,2,hair_light)
c.set(25,12,hair_light)
c.set(35,12,hair_dark)
# Anime eyes and brows
c.rect(27,15,3,2,outline)
c.rect(33,15,3,2,outline)
c.set(28,15,white_hi)
c.set(34,15,white_hi)
c.set(29,16,blue3)
c.set(33,16,blue3)
c.set(31,17,skin_dark)
# Small relaxed smile
c.set(30,20,skin_dark)
c.set(31,21,skin_dark)
c.set(32,21,skin_dark)
c.set(33,20,skin_dark)

# Left arm relaxed under cloak, hand visible
c.poly([(19,31),(15,39),(16,46),(20,45),(22,37)], outline)
c.poly([(19,32),(17,39),(17,44),(20,44),(21,37)], blue1)
c.rect(17,44,4,5,outline)
c.rect(18,44,3,4,skin)
c.set(19,44,skin_light)

# Right arm reaching to staff
c.poly([(41,31),(44,34),(47,40),(51,38),(53,41),(48,45),(44,43),(39,36)], outline)
c.poly([(41,32),(43,35),(46,41),(49,40),(51,42),(48,43),(45,42),(40,35)], blue2)
# Hand around staff
c.rect(49,37,5,6,outline)
c.rect(50,38,3,4,skin)
c.set(50,38,skin_light)

# Legs visible below cloak
c.rect(24,53,7,6,outline)
c.rect(34,53,7,6,outline)
c.rect(26,53,5,5,cloth_shadow)
c.rect(34,53,5,5,cloth_shadow)

# White boots, slightly splayed relaxed stance
c.poly([(24,56),(31,56),(31,60),(29,62),(20,62),(20,59)], outline)
c.poly([(25,56),(30,56),(30,59),(28,60),(22,60),(22,59)], white)
c.rect(25,56,5,2,white_hi)
c.set(22,59,white_shadow)
c.poly([(34,56),(40,56),(44,59),(44,62),(34,62),(33,60)], outline)
c.poly([(35,56),(39,56),(42,59),(42,60),(35,60),(34,59)], white)
c.rect(35,56,4,2,white_hi)
c.set(41,59,white_shadow)

# Staff shaft in front, dark border then warm wood
c.line(53,14,51,59,outline)
c.line(54,14,52,59,outline)
c.line(53,15,52,59,amber_dark)
c.set(52,48,amber)
c.set(52,56,amber)
# Staff foot
c.rect(50,58,4,3,outline)
c.rect(51,58,2,2,amber)

# Ornate glowing staff head
c.poly([(53,4),(57,7),(58,12),(55,16),(50,16),(47,12),(48,7)], outline)
c.poly([(53,6),(56,8),(56,12),(54,14),(51,14),(49,11),(50,8)], amber)
c.poly([(53,7),(55,9),(55,11),(53,13),(51,11),(51,9)], amber_hi)
c.rect(52,8,2,4,white_hi)
c.set(51,7,glow)
c.set(55,7,glow)
c.set(48,10,amber_hi)
c.set(57,10,amber_hi)
c.set(49,14,amber)
c.set(56,14,amber)

# Final selective highlights for readability
c.set(17,37,blue3)
c.set(44,37,blue3)
c.line(19,31,22,28,blue3)
c.line(40,28,43,32,blue3)
c.set(29,27,amber_hi)

result = c
view(result, scale=8, margin=0)
finish(result)
