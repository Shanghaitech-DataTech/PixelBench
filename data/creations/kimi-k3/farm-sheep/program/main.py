from pixelbench_api import *

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="sheep")

# Warm muted palette for a cozy Stardew Valley sheep
# Wool tones
wool_hi = c.color("#FAF4EA")    # warm highlight wool
wool_light = c.color("#F2EADA") # light wool
wool_mid = c.color("#E6DACA")   # mid wool tone
wool_shadow = c.color("#D4C6B2") # shadow wool
wool_dark = c.color("#BCAA94")  # deep wool shadow

# Face / skin tones
face_light = c.color("#E8C4B4") # light skin
face_mid = c.color("#D6AC9C")   # mid skin
face_shadow = c.color("#C09484") # shadow skin

# Pink ears
ear_light = c.color("#F0B4B4")  # pale pink ear
ear_mid = c.color("#E29C9C")    # mid pink ear
ear_inner = c.color("#CE8282")  # inner ear

# Legs
leg_light = c.color("#CCAC9C")
leg_mid = c.color("#B69484")
leg_dark = c.color("#9C7C6C")

# Details
eye_dark = c.color("#4A3830")
nose_dark = c.color("#7A5C52")
hoof_dark = c.color("#5A4A42")
blush = c.color("#E8A8A0")     # gentle cheek blush

# === BODY: fluffy cloud-like mass ===
# Main body circles
c.circle(16, 17, 8, wool_mid, fill=True)
c.circle(14, 15, 7, wool_mid, fill=True)
c.circle(18, 19, 6, wool_mid, fill=True)
c.circle(12, 18, 6, wool_mid, fill=True)

# Wool fluff bumps around edges (smaller, more subtle)
c.circle(13, 11, 2, wool_mid, fill=True)
c.circle(17, 10, 2, wool_mid, fill=True)
c.circle(21, 12, 2, wool_mid, fill=True)
c.circle(23, 16, 2, wool_mid, fill=True)
c.circle(22, 21, 2, wool_mid, fill=True)
c.circle(18, 24, 2, wool_mid, fill=True)
c.circle(12, 24, 2, wool_mid, fill=True)
c.circle(8, 20, 2, wool_mid, fill=True)
c.circle(8, 15, 2, wool_mid, fill=True)

# Fill body
c.fill_at(16, 17, wool_mid)

# === HEAD: distinct round shape on right side ===
# Head - slightly overlapping body
c.circle(24, 14, 5, wool_mid, fill=True)

# === EARS: small, droopy, on top of head ===
# Left ear (slightly behind)
c.rect(20, 9, 2, 3, ear_mid, fill=True)
c.set(20, 10, ear_inner)
# Right ear (front, more visible)
c.rect(25, 8, 3, 3, ear_light, fill=True)
c.rect(26, 9, 1, 2, ear_inner, fill=True)

# === FACE: lighter patch on head ===
c.circle(25, 15, 3, face_mid, fill=True)
c.set(24, 14, face_light)
c.set(25, 14, face_light)
c.set(26, 14, face_light)
c.set(24, 16, face_shadow)
c.set(25, 17, face_shadow)

# === EYES ===
c.set(24, 14, eye_dark)
c.set(26, 14, eye_dark)

# === NOSE ===
c.set(27, 16, nose_dark)

# === BLUSH ===
c.set(23, 15, blush)

# === WOOL SHADING on body (gentle) ===
# Highlight top-left
c.circle(13, 13, 4, wool_light, fill=True)
c.set(12, 12, wool_hi)
c.set(13, 11, wool_hi)
c.set(14, 11, wool_hi)
c.set(11, 13, wool_hi)

# Shadow bottom-right
c.circle(19, 21, 4, wool_shadow, fill=True)
c.set(21, 23, wool_dark)
c.set(22, 21, wool_dark)
c.set(23, 19, wool_shadow)

# Head highlight
c.set(22, 11, wool_light)
c.set(23, 10, wool_light)

# === TAIL: small fluffy nub ===
c.circle(7, 17, 2, wool_mid, fill=True)
c.set(6, 17, wool_light)

# === LEGS: short, positioned below body ===
# Back leg (left, slightly behind)
c.rect(13, 24, 2, 3, leg_mid, fill=True)
c.rect(13, 26, 2, 1, hoof_dark, fill=True)

# Front leg (right)
c.rect(20, 24, 2, 3, leg_light, fill=True)
c.rect(20, 26, 2, 1, hoof_dark, fill=True)

# Far back leg
c.rect(10, 24, 2, 2, leg_dark, fill=True)
c.rect(10, 25, 2, 1, hoof_dark, fill=True)

# Far front leg
c.rect(17, 24, 2, 2, leg_dark, fill=True)
c.rect(17, 25, 2, 1, hoof_dark, fill=True)

# Soft wool fringe where body meets legs
c.set(12, 24, wool_shadow)
c.set(15, 24, wool_shadow)
c.set(16, 24, wool_shadow)
c.set(19, 24, wool_shadow)
c.set(22, 24, wool_shadow)

# Check color count
stats = c.stats()
print(f"Colors used: {stats['colors_used']}")
print(f"Visible pixels: {stats['visible_pixels']}")
print(f"Coverage: {stats['coverage']:.2f}")

# Submit the final canvas
finish(c)
