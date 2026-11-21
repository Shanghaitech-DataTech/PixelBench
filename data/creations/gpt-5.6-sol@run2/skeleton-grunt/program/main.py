# 32x32 skeleton grunt sprite
c = new_canvas(32, 32, name="skeleton_grunt")

# Palette: deep outline, warm bone, weathered wood, and cool steel.
ink = "#20232b"
shade = "#55545a"
bone_shadow = "#a99c83"
bone = "#e5d7b8"
bone_hi = "#fff0cf"
steel_dark = "#49535e"
steel = "#9aa8ad"
steel_hi = "#d1d9d5"
wood_dark = "#493126"
wood = "#875633"
wood_hi = "#b27a45"
strap = "#c49a5a"

# Ragged hood/cowl behind the skull and shoulders.
c.poly([(11,4),(17,3),(21,5),(23,9),(22,12),(25,14),(24,18),(21,20),(10,20),(7,17),(8,13),(10,11)], ink)
c.poly([(12,5),(17,4),(20,6),(22,9),(21,12),(23,15),(22,17),(19,19),(11,19),(9,16),(10,13),(11,11)], shade)
c.poly([(11,13),(14,14),(17,13),(20,15),(19,18),(12,18),(10,16)], "#353840")
# Hood folds
c.line(10,13,12,17,bone_shadow)
c.line(21,12,19,17,ink)
c.set(14,18,shade)
c.set(17,18,shade)

# Skull silhouette: slightly tilted, with cheek/jaw steps.
c.poly([(11,5),(13,3),(18,3),(21,5),(22,8),(21,11),(19,13),(18,15),(13,15),(12,13),(10,12),(9,9),(10,6)], ink)
c.poly([(12,5),(14,4),(18,4),(20,6),(21,8),(20,11),(18,12),(17,14),(14,14),(13,12),(11,11),(10,9),(11,6)], bone_shadow)
c.poly([(13,5),(15,4),(18,5),(20,7),(20,9),(18,10),(16,9),(14,10),(12,9),(11,7)], bone)
c.set(13,5,bone_hi); c.set(14,5,bone_hi); c.set(17,5,bone_hi)
# Eye sockets and nasal cavity
c.poly([(11,7),(13,6),(15,7),(15,9),(14,10),(12,10),(11,9)], ink)
c.poly([(17,7),(19,6),(20,7),(20,9),(19,10),(17,10),(16,9)], ink)
c.set(12,7,steel_dark); c.set(18,7,steel_dark)
c.poly([(15,9),(17,9),(16,12)], shade)
# Teeth and jaw
c.line(13,12,19,12,ink)
c.rect(13,13,1,1,bone_hi); c.rect(15,13,1,1,bone); c.rect(17,13,1,1,bone_hi)
c.line(12,11,14,12,bone_shadow)

# Neck and hunched rib cage, dark joints visible at shoulders and elbows.
c.rect(14,14,4,3,ink)
c.rect(15,14,2,2,bone_shadow)
c.poly([(11,15),(14,14),(18,15),(21,17),(20,21),(18,23),(12,22),(10,20)], ink)
c.poly([(12,16),(14,15),(17,16),(19,17),(19,20),(17,22),(13,21),(11,19)], bone_shadow)
# Rib arcs, segmented highlights
c.line(12,17,14,17,bone_hi); c.line(16,17,18,18,bone)
c.line(12,18,14,19,bone); c.line(16,19,18,20,bone_hi)
c.line(13,20,14,21,bone_hi); c.set(17,21,bone)
# Sternum and dark gaps
c.line(15,16,15,20,ink)
c.set(15,18,shade); c.set(13,18,ink); c.set(17,19,shade); c.set(16,20,shade)

# Left arm reaching forward to hold shield: shoulder, upper arm, elbow, forearm, hand.
c.poly([(10,15),(12,15),(13,17),(12,19),(10,20),(8,19),(8,17)], ink)
c.poly([(10,16),(11,16),(12,18),(10,19),(9,18)], bone_shadow)
c.line(10,16,11,17,bone_hi)
c.circle(9,19,1,ink); c.set(9,19,shade)
c.poly([(8,19),(10,19),(11,21),(10,23),(8,23),(7,21)], ink)
c.poly([(8,20),(9,20),(10,21),(9,22),(8,22)], bone_shadow)
c.set(8,20,bone_hi)
# Shield: small, upright, wooden, held on left side.
c.poly([(2,15),(7,14),(9,16),(9,22),(7,25),(4,24),(2,21)], ink)
c.poly([(3,16),(7,15),(8,17),(8,21),(6,24),(4,23),(3,21)], wood_dark)
c.poly([(4,16),(7,16),(7,22),(5,23),(4,21)], wood)
c.line(4,17,4,20,wood_hi)
c.line(7,17,7,21,wood_dark)
c.rect(5,18,1,3,strap)
c.set(5,19,bone_hi)

# Right arm and sword arm, angled down and outward.
c.poly([(19,15),(22,15),(24,17),(23,19),(21,20),(19,18)], ink)
c.poly([(20,16),(22,16),(23,17),(22,18),(20,18)], bone_shadow)
c.set(21,16,bone_hi)
c.circle(23,19,1,ink); c.set(23,19,shade)
c.poly([(22,19),(24,18),(26,19),(26,21),(24,22),(22,21)], ink)
c.poly([(23,19),(24,19),(25,20),(24,21),(23,21)], bone_shadow)
c.set(24,19,bone_hi)
# Short sword in right hand; pommel, grip, crossguard and broad pointed blade.
c.line(24,20,26,22,ink)
c.line(24,20,25,21,wood)
c.set(24,20,wood_hi)
c.line(25,20,26,18,ink); c.line(25,21,27,19,steel_dark)
c.poly([(24,20),(26,17),(27,12),(26,12),(23,18)], ink)
c.poly([(24,19),(25,16),(26,13),(26,17)], steel)
c.poly([(25,16),(26,13),(26,17)], steel_hi)
c.set(26,12,steel_hi)

# Pelvis, belt, and separated leg bones with visible dark joints.
c.poly([(12,21),(18,21),(20,23),(19,25),(17,26),(12,25),(10,23)], ink)
c.poly([(12,22),(18,22),(18,24),(16,25),(12,24),(11,23)], bone_shadow)
c.line(12,22,17,22,bone_hi)
c.rect(11,24,8,2,ink)
c.rect(12,24,6,1,wood_dark)
c.rect(14,24,2,1,strap)
# Left leg bent forward
c.poly([(12,25),(15,25),(15,27),(13,28),(12,30),(9,30),(8,29),(10,27)], ink)
c.poly([(12,26),(14,26),(14,27),(12,28),(11,29),(9,29),(11,27)], bone_shadow)
c.line(12,26,13,26,bone_hi)
c.circle(11,28,1,ink); c.set(11,28,shade)
c.poly([(8,28),(11,28),(10,30),(7,31),(5,30),(6,29)], ink)
c.poly([(7,29),(10,29),(9,30),(6,30)], bone_shadow)
c.line(6,29,8,29,bone_hi)
# Right leg planted back
c.poly([(16,25),(19,25),(20,27),(19,28),(18,30),(15,30),(14,29),(16,27)], ink)
c.poly([(16,26),(18,26),(19,27),(18,28),(17,29),(15,29),(16,27)], bone_shadow)
c.line(16,26,18,26,bone_hi)
c.circle(17,28,1,ink); c.set(17,28,shade)
c.poly([(15,28),(18,28),(20,29),(20,31),(14,31),(13,30)], ink)
c.poly([(15,29),(18,29),(19,30),(15,30)], bone_shadow)
c.line(15,29,17,29,bone_hi)

view(c)
finish(c)
