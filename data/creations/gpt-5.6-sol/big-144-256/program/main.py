output = input_canvas.copy(name='output')

# Register a compact edit palette that harmonizes with the existing teal stone.
vine_deep = output.color('#102d24', 'vine_deep')
vine_mid = output.color('#1f5138', 'vine_mid')
vine_light = output.color('#3f7650', 'vine_light')
vine_tip = output.color('#5b8b60', 'vine_tip')
cloak_edge = output.color('#111b28', 'cloak_edge')
cloak_dark = output.color('#172536', 'cloak_dark')
cloak_mid = output.color('#243b4b', 'cloak_mid')
cloak_light = output.color('#315564', 'cloak_light')
cloak_glint = output.color('#477180', 'cloak_glint')
staff_dark = output.color('#493925', 'staff_dark')
staff_wood = output.color('#8a6840', 'staff_wood')
glow_outer = output.color('#3b8f91', 'glow_outer')
glow_mid = output.color('#65c5b5', 'glow_mid')
glow_core = output.color('#c4f4cf', 'glow_core')
glow_white = output.color('#edffdb', 'glow_white')

# Vines crawling over the round tower: dark, angular stems with leaf clusters.
# Upper sweep from the left foliage onto the tower face.
output.path('M31 87 C39 83 40 75 48 72 C55 68 58 61 65 57', vine_deep, fill=False)
output.line(32,88,48,73,vine_mid).line(48,73,65,57,vine_mid)
output.line(43,78,39,73,vine_deep).line(48,73,53,70,vine_deep)
output.line(56,66,52,61,vine_deep).line(59,63,65,64,vine_deep)
for x,y in [(36,83),(39,77),(44,76),(49,71),(53,68),(55,63),(61,61),(65,56)]:
    output.rect(x,y,3,2,vine_mid).set(x+1,y-1,vine_light)
output.set(39,82,vine_tip).set(50,70,vine_tip).set(61,60,vine_tip)

# A hanging fork across the central stonework.
output.path('M77 91 C73 102 80 111 75 122 C72 130 77 139 70 147', vine_deep, fill=False)
output.line(78,92,75,109,vine_mid).line(75,109,76,124,vine_mid).line(76,124,70,147,vine_mid)
output.line(75,105,68,101,vine_deep).line(76,116,83,112,vine_deep)
output.line(74,132,67,128,vine_deep).line(72,140,78,136,vine_deep)
for x,y,flip in [(72,99,0),(66,99,0),(79,109,0),(71,114,0),(65,126,0),(76,133,0),(67,143,0)]:
    output.rect(x,y,4,2,vine_mid)
    output.set(x+(0 if flip else 1),y-1,vine_light)

# Lower vine layer framing the entrance wall, with several branching tendrils.
output.path('M37 225 C34 211 39 200 37 188 C35 177 41 166 47 157', vine_deep, fill=False)
output.line(37,225,36,203,vine_mid).line(36,203,38,184,vine_mid).line(38,184,47,157,vine_mid)
output.line(37,199,29,194,vine_deep).line(38,187,46,181,vine_deep)
output.line(40,176,33,171,vine_deep).line(43,166,50,164,vine_deep)
for x,y in [(32,218),(35,209),(29,192),(38,194),(43,180),(32,169),(41,171),(47,162)]:
    output.rect(x,y,4,2,vine_mid).set(x+1,y-1,vine_light)
output.set(34,207,vine_tip).set(44,179,vine_tip).set(48,161,vine_tip)

# Sparse ivy crossing the right lower wall, visually joining the existing foliage.
output.path('M99 216 C93 207 96 197 91 190 C87 183 91 174 86 168', vine_deep, fill=False)
output.line(99,216,94,201,vine_mid).line(94,201,91,189,vine_mid).line(91,189,86,168,vine_mid)
output.line(94,201,102,197,vine_deep).line(91,189,84,186,vine_deep).line(89,178,96,174,vine_deep)
for x,y in [(96,211),(100,195),(84,184),(92,181),(95,172),(83,166)]:
    output.rect(x,y,4,2,vine_mid).set(x+1,y-1,vine_light)

# Cool reflected glow behind the staff head, stepped to preserve crisp pixel edges.
output.rect(67,170,7,9,glow_outer)
output.rect(65,172,11,5,glow_outer)
output.rect(68,168,5,13,glow_outer)
output.rect(67,171,8,7,glow_mid)
output.rect(69,169,4,11,glow_mid)

# Staff runs behind the mage's raised right arm.
output.line(70,174,64,213,staff_dark)
output.line(71,175,65,213,staff_wood)
output.set(70,184,glow_mid).set(68,195,glow_outer)

# Rear-facing mage: hood, shoulders, broad cloak and separated walking feet.
# Dark outline first.
output.poly([(53,183),(47,185),(43,192),(42,201),(39,219),(43,225),(50,224),(54,220),(58,225),(65,224),(63,214),(64,202),(62,192),(59,186)], cloak_edge)
# Hood and back-of-head cavity, with no facial features.
output.poly([(53,184),(48,186),(45,191),(46,197),(50,200),(56,200),(61,196),(60,190),(57,186)], cloak_mid)
output.poly([(53,186),(49,188),(47,192),(49,196),(53,198),(58,195),(58,190),(56,187)], cloak_dark)
output.line(48,191,50,188,cloak_light).set(47,193,cloak_light)
# Cloak body and folds.
output.poly([(46,197),(43,204),(42,218),(47,222),(51,219),(54,222),(59,222),(62,219),(61,204),(59,198),(55,201),(50,200)], cloak_mid)
output.poly([(46,199),(45,207),(44,217),(48,219),(50,209),(51,201)], cloak_light)
output.poly([(55,201),(56,218),(60,220),(59,205),(57,199)], cloak_dark)
output.line(51,201,51,217,cloak_glint).line(52,203,53,219,cloak_dark)
output.set(46,204,cloak_glint).set(47,205,cloak_light).set(58,205,cloak_light)
# Walking stride: one foot deeper in the doorway, one trailing toward the viewer.
output.poly([(47,219),(51,219),(51,225),(49,228),(44,228),(44,225)], cloak_edge)
output.poly([(55,219),(59,220),(62,226),(61,229),(56,228),(53,223)], cloak_edge)
output.rect(45,224,5,2,cloak_dark).rect(56,224,5,3,cloak_dark)
# Right arm reaches back to grip the staff.
output.poly([(59,199),(62,200),(66,207),(64,211),(61,207)], cloak_dark)
output.rect(64,208,3,3,cloak_light).set(66,209,staff_wood)
# Lower staff segment remains visible beside the trailing leg and plants near the threshold.
output.line(65,211,62,230,staff_dark)
output.line(66,211,63,229,staff_wood)
output.set(62,230,staff_dark).set(63,230,staff_dark)

# Repaint the magical focus on top of the staff and figure.
output.rect(68,170,5,9,glow_mid)
output.rect(66,173,9,4,glow_mid)
output.rect(69,171,4,7,glow_core)
output.rect(68,173,6,3,glow_core)
output.rect(70,172,2,4,glow_white)
output.set(69,169,glow_core).set(73,171,glow_core).set(75,174,glow_outer)
output.set(67,178,glow_outer).set(71,180,glow_outer).set(65,175,glow_outer)

print(output.stats_text())
view(output, scale=2, margin=0)
finish(output)
