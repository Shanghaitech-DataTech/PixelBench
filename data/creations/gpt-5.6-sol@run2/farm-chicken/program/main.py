# Cozy 32x32 farm chicken sprite
result = new_canvas(32, 32, background=None, name="farm-chicken")

# Warm muted palette
outline = "#4b302b"
deep = "#6a4033"
cream_shadow = "#c98f61"
cream = "#e7bd82"
light = "#f4d79d"
highlight = "#ffe8b5"
rust = "#b9573f"
comb_light = "#d87558"
beak = "#d99b45"
beak_light = "#efbd62"
leg = "#c47b3e"
eye = "#2b2524"

# Legs and feet, tucked naturally beneath the body
result.rect(12, 24, 2, 5, outline)
result.rect(13, 24, 1, 4, leg)
result.set(10, 29, outline)
result.set(11, 29, leg)
result.set(14, 29, leg)
result.set(15, 29, outline)
result.line(12, 28, 10, 29, leg)
result.line(13, 28, 15, 29, leg)
result.rect(19, 24, 2, 5, outline)
result.rect(20, 24, 1, 4, leg)
result.set(18, 29, outline)
result.set(19, 29, leg)
result.set(22, 29, leg)
result.set(23, 29, outline)
result.line(20, 28, 18, 29, leg)
result.line(21, 28, 23, 29, leg)

# Tail fan behind the body
result.poly([(8,13),(3,10),(4,15),(1,15),(5,19),(3,21),(10,22)], outline)
result.poly([(7,14),(4,12),(5,16),(3,16),(7,19),(5,20),(10,20)], cream_shadow)
result.set(5, 13, cream)
result.set(5, 17, cream)

# Plump body and soft belly
result.ellipse(14, 19, 11, 8, outline)
result.ellipse(14, 18, 9, 7, cream)
result.rect(7, 20, 2, 3, cream_shadow)
result.rect(9, 24, 9, 1, cream_shadow)
result.rect(11, 25, 6, 1, cream_shadow)
result.set(8, 23, cream_shadow)
result.set(18, 24, cream_shadow)

# Neck and rounded head, facing right
result.circle(21, 12, 7, outline)
result.circle(21, 12, 6, cream)
result.rect(16, 15, 7, 5, cream)
result.set(16, 18, light)
result.set(17, 19, light)

# Comb with three soft lobes
result.circle(18, 5, 2, outline)
result.circle(21, 4, 2, outline)
result.circle(24, 5, 2, outline)
result.circle(18, 5, 1, rust)
result.circle(21, 4, 1, comb_light)
result.circle(24, 5, 1, rust)
result.rect(18, 6, 7, 2, rust)
result.rect(20, 6, 3, 1, comb_light)

# Face, beak and wattle
result.poly([(26,10),(31,12),(26,14)], outline)
result.poly([(27,11),(30,12),(27,13)], beak)
result.set(28, 11, beak_light)
result.circle(25, 16, 2, outline)
result.circle(25, 16, 1, rust)
result.set(26, 15, comb_light)
result.set(24, 10, eye)
result.set(23, 9, highlight)
result.set(25, 12, cream_shadow)

# Layered wing: broad teardrop with scalloped feather tips
result.poly([(8,16),(11,13),(17,14),(20,17),(19,21),(16,24),(11,23),(8,20)], deep)
result.poly([(9,16),(12,14),(17,15),(19,17),(18,20),(16,22),(12,22),(9,20)], cream_shadow)
result.poly([(10,16),(13,15),(17,16),(18,18),(16,19),(18,20),(15,22),(12,21),(10,19)], light)
result.set(12, 16, highlight)
result.set(13, 16, highlight)
result.set(10, 18, cream)
result.set(14, 20, cream)
result.set(17, 18, cream)

# Sparse feather glints and warm contour pixels
result.set(13, 12, light)
result.set(15, 11, highlight)
result.set(19, 8, light)
result.set(20, 8, highlight)
result.set(8, 18, light)
result.set(21, 20, cream_shadow)
result.set(20, 22, cream_shadow)

finish(result)
view(result, scale=16, margin=0)
