from pixelbench_api import new_canvas, view, finish

# 32px side-view e-scooter rider, facing right.
c = new_canvas(32, 32, background=None, name="e-scooter-rider")

# Compact palette.
outline = "#172330"
rubber = "#202832"
metal_dark = "#334b59"
metal = "#4f7785"
cyan = "#35d1c5"
cyan_hi = "#8cf5df"
skin = "#d99769"
skin_hi = "#f2bb86"
jacket = "#ed5b45"
jacket_hi = "#ff8464"
pants = "#263f66"
shoe = "#f1e9d2"
helmet = "#ffd34f"
helmet_hi = "#fff08a"

# Scooter wheels: dark 5x5 tire clusters with bright hubs.
for cx in (8, 24):
    c.rect(cx-1, 25, 3, 5, rubber)
    c.rect(cx-2, 26, 5, 3, rubber)
    c.rect(cx-1, 26, 3, 3, metal_dark)
    c.set(cx, 27, cyan_hi)

# Standing deck and rear fender.
c.rect(7, 23, 17, 2, outline)
c.rect(9, 22, 14, 2, metal)
c.rect(10, 22, 10, 1, cyan)
c.line(6, 24, 7, 22, metal_dark)
c.line(6, 23, 8, 23, metal_dark)

# Angled steering stem, fork and handlebar.
c.line(24, 25, 22, 14, outline)
c.line(23, 24, 21, 14, metal)
c.line(22, 15, 25, 14, outline)
c.line(24, 14, 26, 14, cyan)
c.set(26, 14, outline)
c.line(23, 24, 24, 27, outline)

# Back leg: bent behind, then shoe planted toward rear of deck.
c.line(16, 17, 13, 20, outline)
c.line(13, 20, 11, 23, outline)
c.line(15, 17, 12, 20, pants)
c.line(12, 20, 11, 22, pants)
c.rect(9, 22, 4, 2, outline)
c.rect(9, 22, 3, 1, shoe)

# Front leg: thigh slopes down and forward, shin nearly vertical onto deck.
c.line(16, 17, 20, 19, outline)
c.line(20, 19, 20, 23, outline)
c.line(16, 18, 19, 20, pants)
c.line(19, 20, 19, 22, pants)
c.rect(18, 22, 5, 2, outline)
c.rect(19, 22, 4, 1, shoe)

# Torso leaning into the ride, outlined first.
c.poly([(12,10),(16,9),(19,12),(18,18),(14,18),(11,14)], outline)
c.poly([(13,10),(16,10),(18,12),(17,17),(14,17),(12,14)], jacket)
c.line(13, 11, 16, 11, jacket_hi)
c.set(13, 12, jacket_hi)
c.set(17, 16, outline)

# Rear arm and front arm form a readable bent reach to the grips.
c.line(16, 11, 19, 13, outline)
c.line(19, 13, 22, 13, outline)
c.line(16, 12, 19, 14, jacket_hi)
c.line(19, 14, 22, 14, skin)
c.line(22, 14, 24, 14, skin_hi)
c.set(24, 14, outline)
# Small elbow highlight.
c.set(18, 13, skin_hi)

# Neck and head in profile.
c.rect(14, 8, 3, 3, outline)
c.rect(15, 8, 2, 3, skin)
c.rect(12, 4, 7, 6, outline)
c.rect(13, 5, 6, 4, skin)
# Nose and face direction.
c.set(19, 6, skin)
c.set(19, 7, outline)
c.set(17, 6, outline)
c.set(18, 8, skin_hi)

# Helmet with brim, bright top plane, and dark strap.
c.rect(12, 3, 7, 2, outline)
c.rect(11, 4, 9, 2, outline)
c.rect(12, 3, 6, 2, helmet)
c.rect(12, 4, 7, 1, helmet_hi)
c.rect(18, 5, 3, 1, outline)
c.line(13, 6, 14, 9, outline)
c.set(14, 7, skin)

# Motion accents reinforce rightward travel without clutter.
c.line(2, 19, 6, 19, cyan)
c.line(4, 21, 7, 21, metal)
c.line(1, 17, 4, 17, cyan_hi)

result = c
view(result, scale=14, margin=1, edges="all")
finish(result)
