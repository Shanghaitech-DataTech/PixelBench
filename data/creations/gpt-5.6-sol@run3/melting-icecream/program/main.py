output = input_canvas.copy(name='output')

# Existing chocolate palette, reused to match the sprite.
outline = '#61363d'
deep = '#5e363e'
choc = '#95524c'
light = '#ba6d5b'
shine = '#c46f5b'

# A soft, uneven melted skirt joining the scoop to the cone.
output.rect(19, 31, 24, 4, outline)
output.rect(21, 31, 20, 4, choc)
output.rect(24, 31, 14, 2, light)
output.set(20, 32, choc)
output.set(41, 32, choc)
output.set(22, 35, outline)
output.set(40, 35, outline)

# Left short drip, stepped and rounded.
output.rect(21, 34, 7, 4, outline)
output.rect(22, 34, 5, 4, choc)
output.rect(23, 38, 4, 3, outline)
output.rect(24, 38, 2, 3, choc)
output.rect(24, 41, 2, 1, outline)

# Long central drip down the cone.
output.rect(29, 34, 8, 3, outline)
output.rect(30, 34, 6, 4, choc)
output.rect(30, 37, 7, 6, outline)
output.rect(31, 37, 5, 6, choc)
output.rect(31, 42, 6, 4, outline)
output.rect(32, 42, 4, 5, choc)
output.rect(32, 47, 4, 2, outline)
output.rect(33, 47, 2, 2, choc)
output.rect(33, 49, 2, 1, outline)

# Right drip is shorter so the melt has an organic silhouette.
output.rect(37, 34, 5, 3, outline)
output.rect(38, 34, 3, 4, choc)
output.rect(38, 37, 4, 3, outline)
output.rect(39, 37, 2, 3, choc)
output.set(39, 40, outline)
output.set(40, 40, outline)

# Sparse reflected warmth on the wet chocolate.
output.rect(24, 34, 2, 2, light)
output.rect(31, 35, 2, 2, light)
output.rect(32, 37, 2, 3, shine)
output.set(33, 40, light)
output.set(39, 35, light)

view(output, scale=8, margin=0)
finish(output)
