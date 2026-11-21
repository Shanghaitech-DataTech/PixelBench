output = input_canvas.copy(name='output')

bg = 'c0'
outline = 'c1'
wood_dark = 'c6'
wood = 'c4'
wood_light = 'c2'
gem_dark = 'c14'
gem = 'c13'
gem_light = 'c7'
shine = output.color('#c9df69', name='staff_gem_shine')

# Remove the sword's crossguard and blade while leaving the gripping hand intact.
output.rect(40, 37, 7, 20, bg)

# Staff shaft, interrupted where the hand wraps around it.
output.rect(43, 11, 3, 22, outline)
output.rect(44, 11, 1, 22, wood)
output.set(44, 17, wood_light)
output.set(44, 18, wood_light)
output.set(44, 27, wood_dark)
output.rect(43, 37, 3, 20, outline)
output.rect(44, 37, 1, 20, wood)
output.set(44, 43, wood_light)
output.set(44, 44, wood_light)
output.set(44, 52, wood_dark)
output.set(42, 57, outline)
output.rect(43, 57, 3, 1, wood_dark)
output.set(46, 57, outline)

# Forked wooden crown around a faceted green crystal.
output.set(42, 12, outline)
output.set(41, 11, outline)
output.set(40, 10, outline)
output.set(40, 9, wood_dark)
output.set(39, 8, outline)
output.set(46, 12, outline)
output.set(47, 11, outline)
output.set(48, 10, outline)
output.set(48, 9, wood_dark)
output.set(49, 8, outline)

# Crystal outline and facets.
output.poly([(44, 3), (49, 7), (47, 11), (44, 13), (41, 11), (39, 7)], outline)
output.poly([(44, 4), (48, 7), (46, 10), (44, 12), (42, 10), (40, 7)], gem_dark)
output.poly([(44, 4), (47, 7), (44, 9), (41, 7)], gem)
output.poly([(44, 9), (47, 7), (46, 10), (44, 12)], 'c12')
output.set(43, 5, gem_light)
output.set(44, 5, shine)
output.set(42, 6, shine)

view(output, scale=8, margin=0)
finish(output)
