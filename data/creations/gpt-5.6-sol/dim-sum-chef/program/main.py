# 32x32 front-facing dim sum chef sprite
result = new_canvas(32, 32, background=None, name="dim-sum-chef")

# Compact palette: strong value and hue separation at sprite scale.
outline = result.color("#352536", "outline")
deep = result.color("#553044", "deep_shadow")
hair = result.color("#4a2d32", "hair")
skin_shadow = result.color("#c97962", "skin_shadow")
skin = result.color("#efa17f", "skin")
skin_light = result.color("#ffc29a", "skin_light")
white_shadow = result.color("#b9c9c3", "white_shadow")
white = result.color("#f7eee0", "flour_white")
highlight = result.color("#fff9e9", "highlight")
teal_dark = result.color("#246367", "teal_dark")
teal = result.color("#33898a", "uniform_teal")
teal_light = result.color("#58aaa0", "teal_light")
bamboo_dark = result.color("#8b552d", "bamboo_dark")
bamboo = result.color("#c98239", "bamboo")
bamboo_light = result.color("#edb854", "bamboo_light")
bun_shadow = result.color("#d9d4ba", "bun_shadow")
blush = result.color("#d96f70", "blush")

# Feet behind the body.
result.rect(9, 28, 6, 3, outline)
result.rect(17, 28, 6, 3, outline)
result.rect(10, 28, 4, 2, teal_dark)
result.rect(18, 28, 4, 2, teal_dark)

# Torso and shoulders: teal jacket silhouette.
result.poly([(7,17),(10,15),(22,15),(25,18),(27,27),(23,30),(9,30),(5,27)], outline)
result.poly([(8,18),(11,16),(21,16),(24,18),(25,27),(22,29),(10,29),(7,27)], teal_dark)
result.rect(8, 19, 4, 8, teal)
result.rect(21, 19, 3, 8, teal)
result.set(8,20,teal_light); result.set(23,20,teal_light)

# Flour-dusted apron, broad and readable beneath the steamer.
result.poly([(11,16),(20,16),(22,29),(10,29)], outline)
result.poly([(12,17),(19,17),(21,28),(11,28)], white_shadow)
result.rect(13, 18, 6, 10, white)
result.rect(12, 20, 1, 6, white)
result.set(13,18,highlight); result.set(18,19,highlight)
# Flour dust speckles.
for x,y in [(12,18),(16,17),(19,18),(12,26),(15,25),(18,27),(20,25)]:
    result.set(x,y,highlight)
for x,y in [(14,21),(19,23),(16,27)]:
    result.set(x,y,white_shadow)

# Neck.
result.rect(13, 13, 6, 5, outline)
result.rect(14, 13, 4, 4, skin_shadow)
result.rect(15, 13, 3, 3, skin)

# Ears behind head.
result.rect(8, 9, 3, 5, outline)
result.rect(21, 9, 3, 5, outline)
result.rect(9, 10, 2, 3, skin_shadow)
result.rect(21, 10, 2, 3, skin_shadow)
result.set(9,11,skin); result.set(22,11,skin)

# Head with squared pixel contours.
result.poly([(11,6),(20,6),(22,8),(22,13),(19,16),(13,16),(10,13),(10,8)], outline)
result.rect(11, 8, 10, 5, skin)
result.rect(12, 7, 8, 8, skin)
result.rect(11, 9, 2, 3, skin_shadow)
result.rect(13, 7, 6, 2, skin_light)
result.set(20,9,skin_light)
# Hair/sideburn edge.
result.rect(10,7,2,3,hair); result.rect(20,7,2,3,hair)
result.set(11,7,hair); result.set(20,7,hair)
# Brows, eyes, nose.
result.rect(12,9,3,1,deep); result.rect(17,9,3,1,deep)
result.set(13,10,outline); result.set(18,10,outline)
result.set(16,11,skin_shadow); result.set(15,12,skin_light)
# Rosy cheeks and friendly moustache/smile.
result.set(11,12,blush); result.set(20,12,blush)
result.set(14,13,hair); result.set(17,13,hair)
result.rect(15,14,2,1,outline)
result.set(15,13,white); result.set(16,13,white)

# Puffy chef hat, outlined as clustered lobes.
result.rect(10,2,12,6,outline)
result.rect(8,3,16,4,outline)
result.rect(10,1,4,2,outline); result.rect(14,0,4,3,outline); result.rect(18,1,4,2,outline)
result.rect(9,4,14,3,white_shadow)
result.rect(11,2,4,4,white)
result.rect(15,1,3,5,highlight)
result.rect(18,2,3,4,white)
result.set(9,4,white); result.set(22,4,white)
result.rect(11,6,10,2,white)
result.rect(12,6,8,1,highlight)
result.set(10,5,highlight); result.set(21,5,white_shadow)

# Buns peeking above the steamer rim (behind hands and basket).
# Three outlined round buns with folded tops.
result.rect(9,18,5,4,outline); result.rect(10,17,3,1,outline)
result.rect(10,18,3,3,bun_shadow); result.set(11,17,white); result.set(11,18,highlight); result.set(12,19,white)
result.rect(14,17,5,5,outline); result.rect(15,16,3,1,outline)
result.rect(15,17,3,4,white); result.set(16,16,highlight); result.set(16,18,highlight); result.set(18,19,bun_shadow)
result.rect(19,18,5,4,outline); result.rect(20,17,3,1,outline)
result.rect(20,18,3,3,bun_shadow); result.set(21,17,white); result.set(21,18,highlight); result.set(20,20,white)

# Forearms and hands sit outside the basket for clear grip/readability.
result.rect(5,20,5,7,outline); result.rect(22,20,5,7,outline)
result.rect(6,21,4,5,skin_shadow); result.rect(22,21,4,5,skin_shadow)
result.rect(7,21,3,3,skin); result.rect(22,21,3,3,skin)
result.set(7,21,skin_light); result.set(24,21,skin_light)

# Bamboo steamer: bold rim, slatted body, and base.
result.rect(8,20,16,8,outline)
result.rect(7,21,18,3,outline)
result.rect(8,21,16,2,bamboo_light)
result.rect(9,23,14,4,bamboo)
result.rect(9,24,14,1,bamboo_light)
result.rect(10,25,2,2,bamboo_dark)
result.rect(14,25,2,2,bamboo_dark)
result.rect(18,25,2,2,bamboo_dark)
result.rect(22,25,1,2,bamboo_dark)
result.rect(8,27,16,2,outline)
result.rect(9,27,14,1,bamboo_light)
# Rim highlights and end caps.
result.set(8,21,bamboo); result.set(23,21,bamboo)
result.set(9,21,highlight); result.set(22,22,bamboo_dark)
# Fingers overlap the rim ends.
result.rect(6,22,3,3,skin)
result.rect(23,22,3,3,skin)
result.set(6,22,skin_light); result.set(25,22,skin_light)
result.set(8,24,skin_shadow); result.set(23,24,skin_shadow)

# A few final single-pixel clothing seams and flour dust that stays visible.
result.set(8,27,teal_light); result.set(24,27,teal_light)
result.set(11,29,white_shadow); result.set(20,29,white_shadow)
result.set(10,18,highlight); result.set(21,18,highlight)
result.set(10,19,white); result.set(20,19,white)
# Pleated bun crowns, separated from the pale apron by dark pinpricks.
result.set(11,18,bun_shadow); result.set(16,17,bun_shadow); result.set(21,18,bun_shadow)
result.set(12,20,outline); result.set(16,20,outline); result.set(20,20,outline)

view(result, scale=16, margin=0)
finish(result)
