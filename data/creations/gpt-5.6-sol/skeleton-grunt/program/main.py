# 32x32 RPG skeleton grunt sprite on transparency.
result = new_canvas(32, 32, background=None, name="skeleton-grunt")

# Palette
outline = "#171922"
deep = "#242633"
joint = "#343440"
bone_dark = "#7d7668"
bone = "#b9b09b"
bone_light = "#e0d6bc"
wood_dark = "#4b2c23"
wood = "#795036"
wood_light = "#a87549"
metal_dark = "#59616a"
metal = "#9aa4a8"
metal_light = "#d3d9d5"
leather = "#51372a"

# Back arm behind the shield: bent and heavily shaded at the joints.
result.line(14, 13, 10, 15, outline)
result.line(13, 13, 10, 15, bone_dark)
result.circle(10, 15, 1, joint)
result.line(10, 16, 8, 19, outline)
result.line(10, 16, 9, 18, bone)

# Small wooden shield, dark rim, slightly tilted silhouette.
result.poly([(5,14),(9,12),(13,14),(13,20),(10,24),(7,23),(5,20)], outline)
result.poly([(6,15),(9,13),(12,15),(12,20),(9,23),(6,20)], wood_dark)
result.poly([(7,15),(9,14),(11,15),(11,20),(9,22),(7,20)], wood)
result.line(9, 14, 9, 22, wood_light)
result.set(10,15,wood_light)
result.set(7,19,wood_dark)
result.circle(9,18,1,metal_dark)
result.set(9,18,metal)

# Rear leg, bent backward.
result.circle(16, 20, 2, outline)
result.line(16, 21, 13, 25, outline)
result.line(15, 22, 13, 25, bone_dark)
result.circle(13, 25, 1, joint)
result.line(13, 26, 10, 28, outline)
result.line(13, 26, 11, 28, bone)
result.poly([(10,27),(14,27),(15,29),(10,29),(9,28)], outline)
result.rect(10,28,4,1,bone_dark)

# Pelvis and hunched torso core.
result.poly([(14,18),(20,18),(21,21),(19,23),(15,22),(13,20)], outline)
result.poly([(15,18),(19,18),(20,20),(18,22),(15,21),(14,20)], bone_dark)
result.set(16,19,bone)
result.set(19,20,bone)
result.circle(17,17,1,joint)

# Spine, ribs and forward-sloping shoulder line.
result.line(17, 17, 18, 11, outline)
result.line(18, 16, 19, 11, bone_dark)
result.set(18,14,bone_light)
result.line(13, 12, 22, 13, outline)
result.line(14, 12, 21, 13, bone)
result.set(18,12,bone_light)
# Rib cage arcs in stepped pixel form.
result.line(15, 13, 14, 16, bone_dark)
result.line(15, 14, 20, 15, bone)
result.line(14, 16, 20, 17, bone_dark)
result.set(15,15,bone_light)
result.set(20,15,outline)
result.set(19,16,deep)

# Front leg, planted forward with dark knee.
result.circle(19, 22, 2, outline)
result.set(19,22,joint)
result.set(20,22,bone_dark)
result.line(20, 23, 22, 27, outline)
result.line(20, 23, 21, 27, bone)
result.set(21,24,bone_light)
result.circle(22,27,1,joint)
result.poly([(21,27),(24,27),(27,29),(27,30),(21,30),(20,29)], outline)
result.poly([(22,28),(24,28),(26,29),(22,29)], bone_dark)
result.set(22,28,bone_light)

# Sword arm thrust forward and down from the hunched shoulder.
result.circle(22, 13, 2, outline)
result.set(22,13,joint)
result.set(21,12,bone)
result.line(23, 14, 25, 17, outline)
result.line(23, 14, 24, 17, bone)
result.set(24,15,bone_light)
result.circle(25,18,1,outline)
result.set(25,18,bone_dark)
# Grip and guard.
result.line(24,18,27,20,outline)
result.line(25,18,27,20,leather)
result.line(25,20,29,17,outline)
result.set(26,19,metal_dark)
result.set(27,18,metal)
# Short sword blade points up-right.
result.poly([(27,18),(26,17),(29,10),(31,8),(30,12),(28,19)], outline)
result.poly([(28,17),(27,17),(29,11),(30,9),(29,16)], metal)
result.line(29,11,30,9,metal_light)
result.set(28,16,metal_light)

# Skull sits forward of spine, with a compact jaw and broken-tooth edge.
result.poly([(15,5),(17,3),(21,3),(24,5),(24,9),(22,11),(21,13),(16,12),(14,10),(14,7)], outline)
result.poly([(16,5),(18,4),(21,4),(23,5),(23,9),(21,10),(21,12),(17,11),(15,9),(15,7)], bone)
# Brow, temple shadow, nasal cavity and eye sockets.
result.line(16,6,22,6,bone_light)
result.set(16,7,bone_light)
result.rect(17,7,2,2,deep)
result.rect(21,7,2,2,deep)
result.set(19,9,joint)
result.set(20,8,bone_dark)
result.set(22,9,bone_dark)
# Jaw and teeth read as a jagged lower edge.
result.line(17,10,22,10,bone_light)
result.set(17,11,bone_dark)
result.set(19,11,outline)
result.set(21,11,outline)
result.set(20,12,bone_dark)
# A chipped crown pixel improves the battered grunt silhouette.
result.set(16,4,bone_dark)
result.set(15,5,outline)
# Temple crack and a darker underbite separate cranium from jaw.
result.set(22,5,bone_dark)
result.set(21,6,bone_dark)
result.set(16,10,bone_dark)
result.set(22,10,outline)
result.set(18,12,outline)

# Re-open the rib cage with dark negative channels and bright rib tips.
result.set(16,14,deep)
result.set(18,14,deep)
result.set(20,14,bone_light)
result.set(15,16,deep)
result.set(17,16,deep)
result.set(19,16,bone_light)
result.set(16,17,outline)
# Tiny phalanges gripping the sword handle.
result.set(24,17,bone_light)
result.set(26,18,bone_dark)

view(result, scale=16, margin=1, edges="all")
finish(result)
