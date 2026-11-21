# Retro film camera RPG item portrait, 32x32, transparent background.
result = new_canvas(32, 32, background=None, name="retro-film-camera")

# Compact material palette.
ink = result.color("#17151b", "ink")
ink2 = result.color("#27232a", "soft_ink")
edge = result.color("#3a2b2a", "warm_edge")
leather_dark = result.color("#56342b", "leather_dark")
leather = result.color("#7b4933", "leather")
leather_mid = result.color("#955d3b", "leather_mid")
leather_light = result.color("#b67749", "leather_light")
metal_dark = result.color("#4b4d50", "metal_dark")
metal = result.color("#777b7b", "metal")
metal_light = result.color("#b4b5aa", "metal_light")
metal_glint = result.color("#e2ddc8", "metal_glint")
blue_dark = result.color("#18313a", "glass_dark")
blue = result.color("#245665", "glass")
blue_light = result.color("#4e8a91", "glass_light")
cyan = result.color("#9bc0b5", "glass_glint")
red_dark = result.color("#6b2928", "red_dark")
red = result.color("#bb4a38", "red")

# Strap lugs and the chunky stepped outer silhouette.
result.rect(1, 12, 3, 9, ink)
result.rect(28, 12, 3, 9, ink)
result.poly([(3,10),(6,10),(6,8),(11,8),(12,5),(22,5),(23,7),(27,7),(27,9),(29,11),(29,24),(27,27),(5,27),(2,24),(2,13)], ink)

# Main leather shell, including beveled lower corners.
result.poly([(4,12),(7,12),(7,11),(26,11),(28,13),(28,23),(26,25),(6,25),(4,23)], leather_dark)
result.rect(5, 14, 22, 9, leather)
result.rect(6, 13, 20, 2, leather_mid)
result.rect(6, 23, 20, 2, edge)
result.set(5,15,leather_light)
result.set(5,16,leather_mid)
result.set(27,15,edge)
result.set(27,22,ink2)

# Brushed metal top plate and raised prism/viewfinder housing.
result.rect(7, 8, 19, 5, metal_dark)
result.rect(8, 8, 17, 3, metal)
result.rect(9, 8, 15, 1, metal_light)
result.rect(11, 6, 11, 2, ink2)
result.rect(12, 6, 9, 2, metal)
result.rect(13, 6, 7, 1, metal_light)
result.set(8,9,metal_glint)
result.set(24,10,metal_dark)

# Left viewfinder window.
result.rect(6, 8, 6, 5, ink)
result.rect(7, 9, 4, 3, blue_dark)
result.rect(8, 9, 2, 1, blue_light)
result.set(7,10,blue)

# Film advance dial and shutter release on the top.
result.rect(22, 5, 5, 3, ink)
result.rect(23, 5, 3, 2, metal)
result.rect(24, 5, 1, 1, metal_glint)
result.rect(4, 7, 4, 2, ink)
result.rect(5, 7, 2, 1, metal_light)
result.rect(26, 8, 2, 3, ink2)

# Small front controls.
result.rect(24, 13, 3, 3, ink)
result.rect(25, 14, 1, 1, red)
result.rect(6, 14, 3, 2, edge)
result.rect(7, 14, 1, 1, metal_light)

# Oversized lens mount, with stepped pixel rings.
result.circle(16, 19, 8, ink)
result.circle(16, 19, 7, metal_dark)
result.circle(16, 19, 6, ink2)
# Break the perfect circles into a chunky mounted profile.
result.rect(11, 12, 10, 1, metal)
result.rect(9, 15, 1, 8, metal_dark)
result.rect(22, 16, 1, 7, ink)
result.set(10,14,metal_light)
result.set(11,13,metal)
result.set(21,14,metal_dark)
result.set(22,15,metal)
result.set(11,25,ink)
result.set(21,24,metal_dark)

# Glass: deep teal aperture with crescent reflections.
result.circle(16, 19, 5, blue_dark)
result.circle(16, 19, 4, blue)
result.poly([(13,16),(15,15),(18,15),(20,17),(18,17),(16,16),(14,18),(13,20),(12,19)], blue_light)
result.rect(13, 16, 3, 1, cyan)
result.rect(12, 17, 2, 2, blue_light)
result.set(13,17,metal_glint)
result.set(19,21,blue_dark)
result.set(18,22,ink2)
result.set(14,22,blue_dark)
result.set(12,20,blue)

# Lens rim ticks and metal catches.
for x, y in [(13,13),(16,12),(19,13),(22,19),(20,24),(16,26),(12,24),(10,21)]:
    result.set(x, y, metal_light)
for x, y in [(14,13),(18,13),(22,18),(21,22),(18,25),(13,25),(10,22),(10,17)]:
    result.set(x, y, metal)

# Sparse leather grain and edge wear.
for x, y, col in [
    (5,18,leather_light),(6,21,leather_dark),(7,17,leather_mid),(7,24,leather_light),
    (24,18,leather_light),(26,20,leather_dark),(25,23,leather_mid),(4,22,leather_mid),
    (8,13,leather_light),(23,13,leather_dark),(6,16,edge),(26,17,leather_light),
    (4,14,leather_mid),(27,14,leather_light),(24,24,leather_dark)
]:
    result.set(x, y, col)

# Bottom seam and tiny tripod socket.
result.line(7, 25, 11, 25, leather_light)
result.line(22, 25, 25, 25, leather_mid)
result.rect(14, 26, 5, 1, ink)
result.rect(15, 26, 3, 1, metal_dark)

view(result, scale=16, margin=1, edges="all")
finish(result)
