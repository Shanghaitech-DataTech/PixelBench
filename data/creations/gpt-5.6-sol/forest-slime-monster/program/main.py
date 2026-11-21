# 32x32 forest slime RPG enemy sprite
result = new_canvas(32, 32, background=None, name="forest-slime-monster")

# Palette
outline = "#162d25"
deep = "#214438"
shadow = "#2e5b43"
body = "#477852"
light = "#65a05c"
highlight = "#8abd68"
moss_dark = "#355b2d"
moss = "#527d36"
moss_light = "#7da849"
antler_dark = "#5a3f2a"
antler = "#8b6842"
eye_glow = "#d8ff8a"
eye_core = "#f5ffd0"
red_dark = "#7d2b2a"
red = "#c84a3b"
red_light = "#ef7654"
stem = "#d7bd84"

# Tiny branching antlers behind the body
# left
result.set(9, 9, outline).set(8, 8, outline).set(7, 7, outline)
result.set(7, 6, outline).set(6, 5, outline).set(6, 4, outline)
result.set(7, 7, antler).set(7, 6, antler).set(6, 5, antler)
result.set(8, 7, outline).set(9, 6, outline).set(9, 5, outline)
result.set(8, 7, antler).set(9, 6, antler)
result.set(6, 6, antler).set(5, 6, outline)
result.set(6, 4, antler_dark).set(9, 5, antler_dark)
# right
result.set(22, 9, outline).set(23, 8, outline).set(24, 7, outline)
result.set(24, 6, outline).set(25, 5, outline).set(25, 4, outline)
result.set(24, 7, antler).set(24, 6, antler).set(25, 5, antler)
result.set(23, 7, outline).set(22, 6, outline).set(22, 5, outline)
result.set(23, 7, antler).set(22, 6, antler)
result.set(25, 6, antler).set(26, 6, outline)
result.set(25, 4, antler_dark).set(22, 5, antler_dark)

# Mushroom behind upper-right of slime
result.rect(23, 8, 2, 4, outline)
result.rect(24, 9, 1, 3, stem)
result.rect(21, 6, 6, 3, outline)
result.rect(22, 5, 4, 1, outline)
result.rect(22, 6, 4, 2, red)
result.set(23, 5, red).set(24, 5, red_light)
result.set(21, 7, red_dark).set(26, 7, red_dark)
result.set(23, 6, red_light).set(25, 7, red_light)

# Main compact slime silhouette, dark outer edge
result.poly([(10,8),(13,7),(18,7),(21,9),(23,12),(24,16),(24,21),(26,24),(25,27),(22,29),(18,29),(16,28),(14,29),(9,29),(6,27),(5,24),(7,21),(7,16),(8,12)], outline)
# Inner body mass
result.poly([(11,9),(15,8),(19,9),(22,12),(23,17),(22,22),(24,24),(23,26),(20,28),(17,27),(15,27),(12,28),(8,27),(7,25),(9,22),(8,18),(9,13)], body)

# Bottom shadow and grounded lobes
result.rect(9, 26, 5, 2, shadow)
result.rect(18, 26, 4, 2, shadow)
result.set(7,25,shadow).set(8,26,shadow).set(14,27,deep).set(17,27,deep).set(22,25,shadow)
result.set(6,24,deep).set(25,24,deep).set(9,28,outline).set(22,28,outline)

# Body shading and wet highlights
result.rect(8, 15, 2, 6, shadow)
result.set(9,13,light).set(10,11,light).set(11,10,light)
result.set(10,14,highlight).set(9,15,highlight).set(10,16,light)
result.set(21,14,deep).set(22,15,deep).set(22,19,deep).set(21,21,deep)
result.set(12,25,light).set(13,26,light).set(19,25,light)
result.set(8,23,light).set(23,23,shadow)

# Moss cap with an irregular overhang
result.poly([(9,10),(10,8),(13,8),(14,6),(16,8),(18,7),(19,9),(21,9),(22,12),(20,12),(19,14),(17,13),(16,15),(14,13),(12,14),(11,12),(9,12)], moss_dark)
result.poly([(10,10),(12,8),(14,9),(15,7),(17,9),(19,8),(20,10),(21,10),(20,12),(18,11),(17,13),(15,12),(14,13),(13,11),(11,12)], moss)
result.set(12,9,moss_light).set(15,8,moss_light).set(18,9,moss_light).set(19,10,moss_light)
result.set(10,11,highlight).set(14,10,moss_light).set(20,11,moss_dark)
# Moss flecks on cheeks/body
result.set(8,19,moss_dark).set(9,20,moss).set(22,18,moss_dark)
result.set(20,24,moss_dark).set(21,24,moss).set(11,24,moss)

# Face sockets: friendly but alert downward tilt
result.rect(10,16,5,4, deep)
result.rect(17,16,5,4, deep)
result.set(10,16,outline).set(14,16,outline).set(17,16,outline).set(21,16,outline)
# luminous eyes
result.rect(11,17,3,2, eye_glow)
result.rect(18,17,3,2, eye_glow)
result.set(12,17,eye_core).set(19,17,eye_core)
result.set(11,19,shadow).set(20,19,shadow)
# Small expressive mouth
result.set(14,22,outline).set(15,23,outline).set(16,23,outline).set(17,22,outline)
result.set(15,22,"#9acb71").set(16,22,"#9acb71")

# Tiny foreground grass-like moss tufts for silhouette detail
result.set(10,27,moss).set(10,26,moss_light).set(11,27,moss)
result.set(20,27,moss).set(21,26,moss_light).set(21,27,moss)

view(result, scale=16, margin=0)
finish(result)
