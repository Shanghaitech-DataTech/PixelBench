# Retro film camera RPG item portrait, 32x32.
result = new_canvas(32, 32, background=None, name="retro-film-camera")

# Palette
outline = "#17151a"
deep = "#252027"
shadow = "#3a2928"
leather_dark = "#5a3428"
leather = "#81503a"
leather_mid = "#9b6547"
leather_light = "#bd8258"
metal_dark = "#4b5154"
metal = "#7c8583"
metal_light = "#b8beb4"
shine = "#e1ddc8"
black = "#111419"
lens_rim = "#30383b"
glass_dark = "#12303a"
glass = "#1d5361"
glass_light = "#3e8290"
glass_glint = "#9fc4bd"
red = "#a83d31"

# Stepped outer silhouette and side grip.
result.poly([(5,8),(10,8),(11,6),(19,6),(20,8),(26,8),(26,10),(29,10),(29,24),(27,24),(27,26),(6,26),(6,25),(3,25),(3,11),(5,11)], outline)
result.rect(4,12,24,12, leather_dark)
result.rect(5,11,22,2, metal_dark)
result.rect(6,9,20,3, metal)
result.rect(11,7,8,2, metal_dark)
result.rect(12,7,6,1, metal_light)
result.rect(6,9,6,1, metal_light)
result.rect(20,9,5,1, metal_light)
result.set(5,10, metal_dark)
result.set(26,11, deep)

# Viewfinder, top plate details, shutter button and winding knob.
result.rect(13,8,5,3, outline)
result.rect(14,8,3,2, glass_dark)
result.set(15,8, glass_light)
result.rect(22,7,4,2, outline)
result.rect(23,6,2,1, metal_light)
result.rect(23,7,2,1, shine)
result.rect(7,7,3,2, outline)
result.rect(7,6,3,1, metal)
result.set(8,6, metal_light)
result.rect(20,10,2,1, black)
result.set(21,10, red)

# Leather front panels and pixel texture.
result.rect(5,13,21,10, leather)
result.rect(5,21,21,3, leather_dark)
result.rect(6,13,19,1, leather_mid)
result.rect(5,14,2,7, shadow)
result.rect(25,14,1,8, leather_dark)
# embossed seam lines
result.line(7,14,7,22, leather_dark)
result.line(24,14,24,22, leather_dark)
result.set(8,15, leather_light)
result.set(10,14, leather_mid)
result.set(22,15, leather_light)
result.set(23,18, leather_mid)
result.set(9,21, leather_mid)
result.set(21,22, shadow)
result.set(6,18, leather_mid)
result.set(25,16, leather_light)

# Lens mount shadow and concentric lens.
result.circle(16,18,7, outline)
result.circle(16,18,6, metal_dark)
# rim segmentation
result.circle(16,18,5, lens_rim)
result.set(13,13, metal_light)
result.set(14,12, metal)
result.set(18,13, metal_light)
result.set(20,15, metal)
result.set(21,18, deep)
result.set(20,21, black)
result.set(18,23, deep)
result.set(13,23, black)
result.set(11,21, metal_dark)
result.set(10,17, metal_light)
result.set(11,15, metal)
# glass
result.circle(16,18,4, glass_dark)
result.circle(16,18,3, glass)
result.set(14,16, glass_light)
result.set(15,15, glass_light)
result.set(16,15, glass_glint)
result.set(14,17, glass_light)
result.set(15,16, glass_glint)
result.set(18,19, glass_dark)
result.set(17,20, "#0a222b")
result.set(15,20, "#173c48")
# aperture center
result.rect(15,17,3,3, "#0b171d")
result.set(15,17, glass_dark)
result.set(17,19, black)
result.set(16,18, "#244754")
result.set(16,17, "#6c9da1")

# Bottom edge, feet, side latch and tiny highlights.
result.rect(7,24,19,2, outline)
result.rect(9,24,15,1, shadow)
result.rect(8,26,4,1, deep)
result.rect(22,26,3,1, deep)
result.rect(27,13,2,5, outline)
result.rect(27,14,1,3, metal)
result.set(4,12, leather_light)
result.set(4,13, leather_mid)
result.set(6,23, leather_light)
result.set(26,22, shadow)
# Final readability accents: worn leather corners and lens-ring glints.
result.set(5,15, leather_light)
result.set(5,19, leather_mid)
result.set(7,23, leather_mid)
result.set(23,23, leather)
result.set(26,13, metal_light)
result.set(12,14, shine)
result.set(19,14, metal_light)
result.set(11,16, metal_light)
result.set(20,19, metal)

view(result, scale=16, margin=0)
finish(result)
