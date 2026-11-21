# 32x32 e-scooter rider sprite
result = new_canvas(32, 32, background=None, name="e-scooter-rider")

# Palette
ink = result.color("#17202b", "ink")
ink2 = result.color("#2c3846", "soft_ink")
helmet = result.color("#19b7b0", "helmet_teal")
helmet_hi = result.color("#70e0d4", "helmet_highlight")
skin = result.color("#f2ad7b", "skin")
skin_hi = result.color("#ffd0a3", "skin_highlight")
jacket = result.color("#ed5a4f", "coral_jacket")
jacket_hi = result.color("#ff8272", "jacket_highlight")
pants = result.color("#365f9f", "blue_pants")
pants_hi = result.color("#5685c7", "pants_highlight")
metal = result.color("#73808c", "scooter_metal")
metal_hi = result.color("#b5c0c7", "metal_highlight")
tire = result.color("#111820", "tire")
hub = result.color("#d8e2e5", "wheel_hub")
light = result.color("#f6d34a", "scooter_light")

# Helmet and head, facing right
result.rect(11, 4, 7, 2, ink)
result.rect(9, 6, 10, 4, ink)
result.rect(10, 4, 6, 1, ink)
result.rect(10, 5, 8, 3, helmet)
result.rect(10, 6, 2, 2, helmet_hi)
result.rect(18, 7, 2, 1, ink)  # visor / brim
result.rect(12, 9, 7, 5, ink)
result.rect(13, 9, 5, 4, skin)
result.set(17, 9, skin_hi)
result.set(18, 10, skin)
result.set(17, 10, ink)        # eye
result.rect(12, 12, 2, 3, skin)

# Leaning torso and jacket
result.poly([(10, 13), (15, 12), (19, 18), (16, 22), (10, 20), (8, 16)], ink)
result.poly([(11, 14), (14, 13), (17, 18), (15, 20), (11, 19), (9, 16)], jacket)
result.line(11, 14, 14, 18, jacket_hi)
result.set(10, 15, jacket_hi)

# Forward arm reaching the handlebar
result.line(14, 14, 18, 15, ink)
result.line(18, 15, 22, 13, ink)
result.line(15, 14, 18, 16, skin)
result.line(18, 16, 22, 14, skin)
result.rect(21, 13, 3, 2, skin)
result.set(23, 13, ink)

# Rear arm / hand overlap for a two-handed grip
result.line(13, 15, 17, 17, ink)
result.line(17, 17, 21, 14, ink)
result.line(14, 15, 17, 16, jacket_hi)
result.line(17, 16, 21, 13, skin_hi)
result.set(21, 13, skin)

# Hips and readable legs: planted front foot plus bent rear leg
result.rect(13, 19, 5, 3, ink)
result.rect(14, 19, 3, 2, pants_hi)
# planted leg slopes down-right
result.poly([(16, 20), (19, 20), (21, 24), (25, 24), (25, 26), (20, 26), (18, 24)], ink)
result.poly([(17, 21), (18, 21), (20, 24), (22, 24), (22, 25), (20, 25), (19, 23)], pants)
# bent rear leg kicks back, then reaches deck
result.poly([(14, 20), (17, 22), (14, 24), (11, 24), (10, 23), (13, 21)], ink)
result.poly([(14, 21), (16, 22), (14, 23), (11, 23), (13, 21)], pants_hi)
# shoes
result.rect(9, 23, 5, 2, ink)
result.rect(21, 24, 5, 2, ink)
result.set(25, 24, metal_hi)

# Scooter handlebar and stem
result.rect(21, 11, 6, 2, ink)
result.rect(22, 11, 4, 1, metal_hi)
result.rect(23, 12, 2, 2, ink)
result.line(24, 13, 26, 23, ink)
result.line(25, 14, 27, 23, metal)
result.set(26, 18, metal_hi)
result.rect(25, 22, 3, 3, ink)
result.set(27, 22, light)

# Standing deck
result.rect(8, 24, 20, 3, ink)
result.rect(10, 24, 15, 1, metal_hi)
result.rect(11, 25, 16, 1, metal)
result.set(27, 24, light)

# Wheels, partially tucked under deck
for cx in (9, 26):
    result.circle(cx, 27, 3, tire)
    result.circle(cx, 27, 1, hub)
    result.set(cx, 27, ink2)
# restore deck silhouette over wheel tops
result.rect(10, 24, 15, 1, metal_hi)
result.rect(11, 25, 14, 1, metal)

# Tiny motion pixels behind the scooter
result.rect(3, 24, 4, 1, metal)
result.rect(5, 21, 3, 1, metal_hi)

view(result, scale=16, margin=0)
finish(result)
