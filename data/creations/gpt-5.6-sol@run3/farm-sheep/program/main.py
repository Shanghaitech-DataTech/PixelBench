# Cozy side-view farm sheep, 32x32 pixels.
result = new_canvas(32, 32, background=None, name="farm-sheep")

# Warm muted palette.
wool_light = "#fff8e8"
wool_mid = "#f3ead7"
wool_shadow = "#ded2c2"
face_light = "#f4dfd2"
face_shadow = "#dfc4ba"
pink = "#e8aaa7"
pink_shadow = "#c9898d"
leg = "#c7aea5"
hoof = "#8d7473"
eye = "#594f51"
cheek = "#e7a6a2"

# Legs behind the fleece.
result.rect(12, 21, 4, 6, leg)
result.rect(13, 25, 4, 2, hoof)
result.set(16, 25, hoof)
result.rect(22, 21, 4, 6, leg)
result.rect(22, 25, 4, 2, hoof)
result.set(21, 25, hoof)

# Tiny lifted tail at the rear.
result.circle(27, 14, 2, wool_shadow)
result.circle(28, 13, 1, wool_mid)

# Lower wool shadow mass and scallops.
result.ellipse(18, 17, 10, 7, wool_shadow)
for cx, cy, r in [(10, 14, 3), (14, 11, 3), (19, 10, 3), (24, 12, 3),
                  (27, 16, 3), (24, 21, 3), (19, 23, 3), (13, 22, 3), (9, 18, 3)]:
    result.circle(cx, cy, r, wool_shadow)

# Main fleece, built from overlapping rounded tufts.
result.ellipse(18, 16, 9, 6, wool_mid)
for cx, cy, r in [(11, 14, 3), (15, 11, 3), (20, 11, 3), (24, 13, 3),
                  (25, 17, 3), (23, 20, 3), (18, 21, 3), (13, 20, 3), (11, 17, 3)]:
    result.circle(cx, cy, r, wool_mid)

# Cream highlights make the coat feel fluffy without outlining it.
for cx, cy, r in [(13, 13, 2), (17, 12, 2), (21, 13, 2),
                  (23, 16, 2), (20, 18, 2), (15, 18, 2), (12, 16, 2)]:
    result.circle(cx, cy, r, wool_light)
result.rect(15, 13, 6, 4, wool_light)

# Far ear, then side-facing head and near ear.
result.poly([(8, 12), (5, 9), (3, 10), (5, 14)], pink_shadow)
result.set(4, 10, pink)
result.set(5, 11, pink)

# Long, softly rounded face angled down to the muzzle.
result.ellipse(8, 16, 4, 6, face_shadow)
result.circle(7, 14, 3, face_light)
result.rect(4, 14, 7, 5, face_light)
result.circle(6, 19, 3, face_light)
result.rect(5, 19, 5, 2, face_light)

# Near floppy ear.
result.poly([(8, 12), (5, 9), (2, 10), (4, 13)], pink)
result.set(4, 10, "#f3c1ba")
result.set(5, 11, "#f3c1ba")

# Gentle facial details: eye, cheek, nostril and tiny smile.
result.set(6, 15, eye)
result.set(5, 18, cheek)
result.set(4, 20, hoof)
result.set(5, 21, eye)
result.set(6, 21, face_shadow)

# A few single-pixel fleece accents break up the large highlights.
result.set(16, 10, wool_light)
result.set(22, 11, wool_light)
result.set(26, 15, wool_mid)
result.set(10, 20, wool_light)

view(result, scale=16, margin=0)
finish(result)
