# 32x32 cozy side-view farm sheep
result = new_canvas(32, 32, background=None, name="farm-sheep")

# Warm muted palette
shadow = "#9b827f"
deep_shadow = "#77676a"
leg = "#cdb5aa"
leg_light = "#dfc8bb"
hoof = "#806d6b"
wool_shadow = "#d8d0c8"
wool_mid = "#ebe5dc"
wool = "#f7f2e9"
wool_light = "#fffaf0"
face = "#d2ad9f"
face_light = "#e4c7b8"
ear = "#dca9ab"
ear_light = "#efc2c0"
eye = "#5f5353"
cheek = "#d99fa0"
ground = "#c9a98966"

# Sparse soft ground pixels, kept clear of the hooves
result.rect(5, 29, 5, 1, "#c9a98933")
result.rect(14, 30, 9, 1, "#c9a98933")
result.rect(25, 29, 3, 1, "#c9a98933")

# Legs behind the wool
result.rect(9, 20, 4, 7, leg)
result.rect(10, 25, 3, 3, leg_light)
result.rect(9, 27, 4, 2, hoof)
result.set(13, 28, hoof)
result.rect(20, 20, 4, 7, leg)
result.rect(20, 25, 3, 3, leg_light)
result.rect(20, 27, 4, 2, hoof)
result.set(19, 28, hoof)

# Wool silhouette, built from overlapping rounded tufts
result.ellipse(15, 16, 11, 8, wool_shadow)
result.circle(7, 15, 4, wool_mid)
result.circle(9, 11, 4, wool)
result.circle(14, 10, 4, wool)
result.circle(19, 11, 5, wool)
result.circle(23, 14, 4, wool_mid)
result.circle(22, 18, 5, wool_mid)
result.circle(17, 21, 5, wool_mid)
result.circle(11, 21, 5, wool_mid)
result.circle(7, 18, 4, wool_mid)

# Main fleece and gentle flat shading
result.ellipse(15, 16, 9, 6, wool)
result.circle(10, 14, 4, wool_light)
result.circle(15, 13, 4, wool_light)
result.circle(19, 15, 4, wool)
result.circle(14, 18, 5, wool)
result.circle(9, 18, 3, wool)
result.circle(19, 19, 3, wool)
# Small shadow clusters between curls
result.rect(6, 20, 3, 2, wool_shadow)
result.rect(11, 23, 4, 2, wool_shadow)
result.rect(18, 22, 4, 2, wool_shadow)
result.set(23, 18, wool_shadow)
result.set(8, 11, wool_mid)
# Highlight tufts
result.rect(10, 10, 4, 2, wool_light)
result.rect(12, 9, 4, 2, wool_light)
result.rect(7, 14, 3, 2, wool_light)
result.rect(14, 14, 4, 2, wool_light)
result.rect(10, 17, 3, 2, wool_light)

# Neck bridge behind the head
result.circle(22, 14, 3, wool)
result.rect(21, 15, 4, 5, wool_mid)
result.set(22, 19, wool_shadow)
result.set(23, 20, wool_shadow)

# Pale pink ear, angled back
result.poly([(23, 12), (22, 9), (24, 7), (27, 9), (26, 12)], ear)
result.poly([(24, 10), (24, 8), (26, 9), (25, 11)], ear_light)
result.set(23, 8, face_light)

# Face in side view, with a soft tapered muzzle
result.ellipse(25, 16, 4, 5, face)
result.rect(24, 13, 4, 7, face_light)
result.rect(27, 15, 3, 5, face)
result.set(29, 17, face)
result.set(28, 20, face)
# Soft jaw shadow
result.rect(24, 20, 4, 2, "#caa9a2")
result.set(28, 19, "#caa9a2")

# Forehead wool cap
result.circle(23, 12, 3, wool)
result.circle(25, 12, 2, wool_light)
result.set(26, 13, wool_mid)

# Gentle facial expression
result.set(27, 15, eye)
result.set(28, 15, "#fff8ed")
result.set(29, 18, "#8d6d6c")
result.set(27, 18, cheek)
result.set(28, 19, "#b98585")

# A few square fleece pixels reinforce the handmade sprite texture
result.set(5, 16, wool_light)
result.set(6, 12, wool_mid)
result.set(8, 23, wool_shadow)
result.set(16, 24, wool_shadow)
result.set(22, 21, wool_shadow)

view(result, scale=16, margin=0)
finish(result)
