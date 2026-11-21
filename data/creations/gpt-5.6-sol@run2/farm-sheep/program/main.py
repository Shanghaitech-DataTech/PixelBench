# Cozy 32x32 side-view sheep sprite
result = new_canvas(32, 32, background=None, name="farm-sheep")

# Warm muted palette
shadow = "#d8c9b5"
shadow2 = "#eadfce"
cream = "#f5eee2"
white = "#fffaf0"
face = "#ead8c8"
face_light = "#f2e3d5"
pink = "#dca8a5"
pink_light = "#edc4bf"
hoof = "#8d7469"
eye = "#554842"
cheek = "#e7aaa7"

# Back legs, tucked beneath the fleece
result.rect(10, 22, 4, 6, shadow2)
result.rect(11, 27, 3, 2, hoof)
result.set(10, 27, shadow)
result.rect(21, 22, 4, 6, shadow2)
result.rect(22, 27, 3, 2, hoof)
result.set(21, 27, shadow)

# Soft fleece shadow silhouette
result.circle(9, 17, 5, shadow2)
result.circle(13, 13, 6, shadow2)
result.circle(19, 13, 6, shadow2)
result.circle(23, 17, 5, shadow2)
result.rect(8, 13, 16, 9, shadow2)
result.circle(14, 19, 5, shadow2)
result.circle(20, 19, 5, shadow2)

# Main fleece puffs
result.circle(9, 15, 4, cream)
result.circle(12, 11, 4, white)
result.circle(17, 10, 5, white)
result.circle(22, 13, 4, cream)
result.circle(23, 17, 4, cream)
result.circle(18, 18, 5, cream)
result.circle(12, 18, 5, white)
result.rect(9, 12, 13, 7, white)

# Gentle fleece shading and puff separation
result.set(7, 17, shadow2)
result.set(8, 19, shadow2)
result.set(10, 21, shadow2)
result.set(14, 22, shadow2)
result.set(19, 22, shadow2)
result.set(22, 20, shadow2)
result.set(24, 17, shadow2)
result.set(11, 8, cream)
result.set(14, 7, cream)
result.set(20, 8, cream)
result.set(23, 11, shadow2)

# Near legs in front
result.rect(13, 22, 4, 6, cream)
result.rect(14, 27, 3, 2, hoof)
result.set(13, 27, shadow)
result.rect(22, 21, 4, 7, cream)
result.rect(23, 27, 3, 2, hoof)
result.set(22, 27, shadow)

# Ear behind the head, pale pink with a soft cream base
result.poly([(22, 11), (24, 8), (28, 8), (27, 11), (24, 13)], shadow2)
result.poly([(24, 10), (25, 9), (28, 9), (26, 11)], pink_light)

# Rounded head and muzzle, facing right
result.circle(24, 14, 4, face)
result.rect(23, 12, 6, 6, face)
result.circle(27, 16, 3, face)
result.set(29, 14, face_light)
result.set(30, 15, face_light)
result.set(30, 16, face)
result.set(29, 18, face)

# Forehead tuft integrating head into fleece
result.circle(22, 11, 2, white)
result.circle(24, 11, 2, cream)
result.set(25, 12, cream)

# Face details
result.set(27, 13, eye)
result.set(28, 13, eye)
result.set(27, 12, face_light)
result.set(29, 15, cheek)
result.set(30, 16, pink)
result.set(29, 17, shadow)
result.set(30, 17, eye)

# Tiny tail puff at rear
result.circle(6, 16, 2, cream)
result.set(5, 14, white)
result.set(4, 16, shadow2)

finish(result)
view(result, scale=16, margin=0)
