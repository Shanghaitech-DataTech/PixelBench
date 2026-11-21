c = new_canvas(32, 32, name="skeleton_grunt")

# Palette
ink = "#20212b"
shadow = "#45434b"
bone_shadow = "#a99878"
bone = "#d8c9a2"
bone_light = "#f0e4c4"
steel_dark = "#555b66"
steel = "#aeb6b7"
steel_light = "#dce0d5"
wood_dark = "#54372c"
wood = "#8b5938"
wood_light = "#bd8150"
leather = "#704535"

# Sword behind body: angled short blade to the right, held low.
c.line(24, 14, 28, 10, ink)
c.line(25, 14, 28, 11, steel)
c.set(29, 9, ink)
c.set(28, 10, steel_light)
c.set(27, 11, steel_light)
c.line(23, 15, 25, 13, wood_dark)
c.line(22, 16, 24, 14, wood)
c.set(22, 15, ink)
c.set(25, 13, ink)
c.set(24, 14, steel_dark)

# Legs, separated at the pelvis, with dark joint shading.
c.poly([(12,20),(16,20),(17,23),(16,25),(15,29),(12,29),(13,25),(11,23)], ink)
c.poly([(17,20),(21,20),(21,23),(20,25),(21,29),(18,29),(16,25),(17,23)], ink)
c.poly([(13,21),(16,21),(16,23),(14,25),(14,28),(12,28),(14,24),(12,23)], bone_shadow)
c.poly([(18,21),(20,21),(20,23),(18,25),(19,28),(18,28),(16,24),(18,23)], bone)
c.line(12, 29, 15, 29, ink)
c.line(18, 29, 21, 29, ink)
c.set(14, 26, bone_light)
c.set(19, 26, bone_light)

# Slightly hunched torso and rib cage.
c.poly([(11,10),(14,9),(19,10),(21,13),(20,18),(22,20),(19,22),(14,21),(11,19),(10,15)], ink)
c.poly([(12,11),(15,10),(19,11),(20,14),(19,18),(21,20),(18,21),(14,20),(12,18),(11,15)], bone_shadow)
# Rib stripes, left to right, segmented and dark between ribs.
c.line(12, 13, 18, 13, ink)
c.line(12, 15, 19, 15, ink)
c.line(13, 17, 18, 17, ink)
c.line(14, 19, 17, 19, ink)
c.line(13, 13, 13, 14, bone)
c.line(15, 13, 15, 14, bone_light)
c.line(17, 13, 17, 14, bone)
c.line(14, 15, 14, 16, bone_light)
c.line(16, 15, 16, 16, bone)
c.line(18, 15, 18, 16, bone_light)
c.line(15, 17, 15, 18, bone)
c.line(17, 17, 17, 18, bone_light)
c.poly([(15,19),(18,19),(19,20),(18,21),(15,20)], bone)
# Shoulder and elbow joints.
c.circle(11, 12, 1, ink)
c.set(11, 12, bone)
c.circle(21, 16, 1, ink)
c.set(21, 16, bone_shadow)
c.line(20, 17, 23, 15, ink)
c.set(22, 15, bone_shadow)
c.set(23, 15, bone)

# Shield arm angled forward on left.
c.poly([(10,12),(12,13),(11,16),(10,19),(8,18),(9,15)], ink)
c.line(10, 13, 11, 14, bone)
c.line(10, 15, 9, 17, bone_shadow)
c.set(10, 18, bone)

# Small round wooden shield on the left foreground.
c.poly([(4,14),(6,12),(9,12),(11,14),(11,18),(9,20),(6,20),(4,18)], ink)
c.poly([(5,14),(6,13),(9,13),(10,15),(10,18),(9,19),(6,19),(5,18)], wood_dark)
c.rect(6, 14, 2, 4, wood)
c.rect(8, 14, 1, 4, wood_light)
c.set(6, 13, wood_light)
c.set(9, 18, wood_dark)
# Boss and iron rim details.
c.set(8, 16, steel_light)
c.set(8, 17, steel)
c.set(5, 15, steel_dark)
c.set(9, 17, steel_dark)

# Neck and skull, turned slightly toward viewer.
c.rect(14, 8, 4, 3, ink)
c.rect(15, 8, 2, 3, bone_shadow)
c.poly([(12,3),(14,1),(19,1),(21,4),(20,8),(18,10),(14,9),(12,7)], ink)
c.poly([(13,3),(15,2),(18,2),(20,4),(19,7),(17,9),(14,8),(13,6)], bone)
# Cranium highlights and brow.
c.line(14, 3, 17, 2, bone_light)
c.set(18, 3, bone_light)
c.line(13, 5, 19, 5, bone_shadow)
# Eye sockets, nose, and jaw.
c.rect(14, 5, 2, 2, ink)
c.rect(17, 5, 2, 2, ink)
c.set(15, 5, "#c55d43")
c.set(18, 5, "#c55d43")
c.set(16, 7, ink)
c.line(14, 8, 18, 8, ink)
c.set(15, 8, bone_light)
c.set(17, 8, bone_light)

# Belt and a small ragged waist wrap.
c.line(12, 20, 20, 20, ink)
c.line(13, 20, 19, 20, wood_dark)
c.set(16, 20, steel_light)
c.poly([(13,21),(17,21),(16,24),(14,23)], bone_shadow)

view(c)
finish(c)
