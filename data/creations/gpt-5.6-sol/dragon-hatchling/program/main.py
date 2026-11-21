# Dragon hatchling sprite, 64x64, transparent background.
result = new_canvas(64, 64, background=None, name="dragon-hatchling")

# Palette
outline = result.color("#17242a", "outline")
deep = result.color("#23434a", "deep")
shadow = result.color("#2f5960", "shadow")
scale = result.color("#3f7470", "scale")
light = result.color("#5f9690", "scale_light")
high = result.color("#83b5a6", "highlight")
wing_dark = result.color("#2a4c58", "wing_dark")
wing = result.color("#3e6970", "wing")
membrane = result.color("#668d87", "membrane")
belly_dark = result.color("#9aa77e", "belly_shadow")
belly = result.color("#c7c79a", "belly")
belly_hi = result.color("#e0d9aa", "belly_highlight")
horn = result.color("#b9b68b", "horn")
horn_hi = result.color("#ded5a4", "horn_highlight")
mouth = result.color("#7b3c42", "mouth")
tongue = result.color("#c86768", "tongue")
tooth = result.color("#eee2b9", "tooth")
eye = result.color("#f1c95b", "eye")
pupil = result.color("#222326", "pupil")

# Rear wing, half spread upward-right.
result.poly([(34,28),(37,13),(41,17),(47,8),(48,21),(56,17),(52,29),(45,34)], outline)
result.poly([(37,27),(39,16),(42,20),(46,12),(46,25),(53,21),(49,29),(44,32)], wing)
result.poly([(40,19),(43,22),(46,14),(45,27),(39,28)], membrane)
result.poly([(47,25),(51,22),(49,29),(45,31)], membrane)
result.line(39,17,44,31,deep)
result.line(46,14,45,31,deep)
result.line(52,21,47,31,deep)

# Far leg and rear foot.
result.poly([(37,42),(45,43),(47,50),(45,54),(47,56),(43,56),(41,53),(39,56),(36,56),(38,52),(35,48)], outline)
result.poly([(39,43),(43,44),(45,50),(42,53),(40,51),(38,54),(39,49),(37,47)], shadow)
result.set(45,55,tooth); result.set(39,55,tooth)

# Tail sweeping right and upward, with strong dark silhouette.
result.poly([(38,39),(48,38),(55,41),(60,39),(58,43),(62,45),(57,46),(59,50),(54,48),(53,52),(49,47),(42,47)], outline)
result.poly([(40,41),(48,40),(54,43),(58,42),(56,45),(58,46),(54,46),(55,49),(51,45),(43,45)], scale)
result.line(44,42,53,45,light)
# Tail spikes.
result.poly([(47,40),(49,35),(51,41)], outline); result.poly([(49,39),(49,37),(50,40)], horn)
result.poly([(53,42),(56,38),(56,44)], outline); result.poly([(55,42),(55,40),(56,43)], horn)
result.poly([(57,45),(62,43),(59,48)], outline); result.set(59,45,horn)

# Main body silhouette.
result.poly([(23,28),(31,24),(40,27),(45,34),(44,44),(39,50),(30,52),(23,48),(20,40)], outline)
result.poly([(25,29),(31,26),(38,28),(42,33),(42,42),(38,48),(31,49),(25,46),(22,39)], scale)
result.poly([(33,28),(39,30),(42,35),(41,43),(37,48),(34,46)], shadow)
# Shoulder and scale highlights.
result.poly([(27,29),(32,27),(35,29),(32,32)], light)
result.set(37,31,light); result.set(39,34,light); result.set(40,38,deep)
result.set(26,35,high); result.set(24,39,deep); result.set(28,43,shadow)
# Individual body scales.
for x,y in [(31,34),(35,35),(29,38),(34,39),(38,40),(30,43),(35,44)]:
    result.line(x,y,x+1,y,deep)
    result.set(x,y-1,light)

# Pale segmented belly, curved down the front.
result.poly([(24,31),(29,31),(31,35),(31,43),(34,48),(30,49),(25,45),(23,38)], belly_dark)
result.poly([(25,32),(28,32),(29,36),(29,43),(32,47),(29,47),(26,44),(25,38)], belly)
result.line(25,36,29,36,belly_dark)
result.line(25,40,29,40,belly_dark)
result.line(26,44,30,44,belly_dark)
result.set(26,33,belly_hi); result.set(27,37,belly_hi); result.set(27,41,belly_hi)

# Near wing half spread to the left/back, its lower edge frames the head.
result.poly([(28,30),(23,17),(18,12),(18,21),(10,17),(14,28),(8,27),(18,36)], outline)
result.poly([(26,29),(22,19),(20,16),(20,25),(13,20),(17,30),(12,29),(19,34)], wing_dark)
result.poly([(21,19),(23,28),(19,31),(15,22),(20,26)], membrane)
result.poly([(14,20),(19,27),(17,29)], wing)
result.line(20,16,19,32,deep)
result.line(13,20,19,32,deep)
# Wing claw at elbow.
result.poly([(13,28),(8,30),(14,31)], horn)

# Neck connecting to head.
result.poly([(22,27),(28,28),(29,38),(24,41),(19,35)], outline)
result.poly([(23,29),(27,29),(27,37),(24,39),(21,34)], scale)
result.set(24,31,light); result.set(25,35,shadow)

# Head: broad brow, cheek, and snout.
result.poly([(10,25),(14,20),(23,20),(28,24),(28,31),(24,35),(16,34),(12,31),(7,30)], outline)
result.poly([(11,26),(15,22),(22,22),(26,25),(26,30),(23,33),(16,32),(13,29),(9,29)], scale)
# Brow plates and cheek.
result.poly([(14,23),(19,21),(24,24),(20,26),(15,26)], light)
result.poly([(18,29),(25,27),(25,31),(22,33),(17,32)], shadow)
result.set(13,27,high); result.set(11,28,light)

# Horns and ear fins.
result.poly([(16,22),(15,15),(20,21)], outline)
result.poly([(17,20),(16,17),(19,21)], horn)
result.set(17,18,horn_hi)
result.poly([(22,21),(25,15),(25,23)], outline)
result.poly([(23,21),(24,17),(24,22)], horn)
result.poly([(25,25),(31,22),(28,29)], outline)
result.poly([(27,25),(29,24),(27,27)], deep)

# Eye under heavy brow.
result.rect(16,25,4,3,outline)
result.rect(17,25,2,2,eye)
result.set(18,26,pupil)
result.set(17,25,"#fff2a6")

# Open growling mouth, upper and lower jaw silhouette.
result.poly([(8,29),(16,29),(20,32),(17,34),(9,34),(5,32)], outline)
result.poly([(8,30),(15,30),(18,32),(15,33),(8,33),(6,32)], mouth)
# Lower jaw, separated at front for readable gape.
result.poly([(7,34),(17,34),(21,32),(19,37),(15,39),(9,37),(6,35)], outline)
result.poly([(9,35),(17,35),(18,34),(17,36),(14,37),(10,36)], scale)
# Tongue and teeth.
result.line(9,33,15,33,tongue)
result.poly([(10,30),(12,30),(11,32)], tooth)
result.poly([(15,30),(17,31),(15,32)], tooth)
result.poly([(12,35),(14,35),(13,34)], tooth)
result.set(7,31,deep)
# Nose and nostril.
result.rect(7,28,4,3,scale)
result.set(8,29,pupil); result.set(7,28,light)

# Near arm, clawed and planted forward.
result.poly([(22,36),(18,39),(15,45),(10,47),(13,50),(18,48),(20,51),(22,49),(20,46),(23,42),(27,40)], outline)
result.poly([(22,38),(19,40),(17,45),(13,47),(16,47),(18,45),(20,48),(20,45),(24,40)], scale)
result.set(13,49,tooth); result.set(17,48,tooth); result.set(21,50,tooth)
result.set(19,41,light); result.line(17,44,19,44,deep)

# Near hind leg and large three-toed foot.
result.poly([(31,44),(38,43),(41,48),(40,53),(46,57),(40,58),(37,56),(34,59),(30,58),(32,54),(27,56),(24,54),(29,51)], outline)
result.poly([(33,45),(37,45),(39,48),(38,53),(41,56),(37,55),(34,57),(32,56),(34,52),(29,54),(27,53),(31,50)], scale)
result.set(44,56,tooth); result.set(39,57,tooth); result.set(33,58,tooth); result.set(26,54,tooth)
result.line(33,48,38,48,light)
result.set(35,52,shadow)

# A few crisp silhouette accents: neck spikes and reflected scale pixels.
result.poly([(27,28),(30,23),(31,29)], outline); result.poly([(29,27),(30,25),(30,28)], horn)
result.poly([(35,27),(37,22),(39,29)], outline); result.poly([(37,27),(37,24),(38,28)], horn)
result.set(23,23,high)

finish(result)
