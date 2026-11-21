# 16x16 wooden key sprite for a detective-game inventory.
result = new_canvas(16, 16, background=None, name="wooden_key")

outline = "#29170f"
shadow = "#5b2e18"
wood = "#945027"
light = "#c77935"
highlight = "#e7a755"

# Dark silhouette: carved bow, neck, shaft, and stepped teeth.
result.rect(2, 3, 5, 1, outline)
result.rect(1, 4, 7, 4, outline)
result.rect(2, 8, 6, 2, outline)
result.rect(7, 6, 7, 4, outline)
result.rect(11, 9, 2, 3, outline)
result.rect(13, 9, 2, 2, outline)

# Bow wood and its square-cut finger hole.
result.rect(2, 4, 4, 1, light)
result.set(6, 4, wood)
result.set(2, 5, light)
result.rect(3, 5, 3, 3, wood)
result.set(6, 5, shadow)
result.set(2, 6, wood)
result.set(6, 6, shadow)
result.rect(2, 7, 5, 1, shadow)
result.rect(3, 8, 4, 1, wood)
result.clear(3, 5, 2, 2)
result.set(5, 5, shadow)
result.set(5, 6, shadow)

# Neck and shaft, with chunky carved highlights and grain.
result.set(7, 6, shadow)
result.rect(7, 7, 7, 1, light)
result.rect(7, 8, 7, 1, wood)
result.set(8, 8, highlight)
result.set(9, 8, light)
result.rect(7, 9, 4, 1, shadow)
result.set(12, 9, light)
result.set(13, 9, wood)

# Teeth shading.
result.set(11, 10, wood)
result.set(12, 10, shadow)
result.set(13, 10, light)
result.set(14, 10, shadow)
result.set(11, 11, shadow)
result.set(12, 11, outline)

# Small irregular grain marks make the material read as wood.
result.set(3, 4, highlight)
result.set(5, 8, light)
result.set(10, 7, highlight)
result.set(11, 8, shadow)

view(result, scale=24, margin=1, edges="all")
finish(result)
