from pixelbench_api import new_canvas, finish

# Create 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None, name="void_eye")

# Define color palette
# Main body colors (dark purples)
body_dark = c.color("#1a0a2e", "body_dark")
body_mid = c.color("#3d1a5c", "body_mid")
body_light = c.color("#5c2a8a", "body_light")
body_highlight = c.color("#7a3aba", "body_highlight")

# Iris colors (deep purple gradient)
iris_outer = c.color("#4a1a6e", "iris_outer")
iris_mid = c.color("#6a2a9e", "iris_mid")
iris_inner = c.color("#8a3ace", "iris_inner")
iris_bright = c.color("#aa4afe", "iris_bright")

# Pupil (glowing)
pupil_dark = c.color("#ffaa00", "pupil_dark")
pupil_bright = c.color("#ffff66", "pupil_bright")
pupil_glow = c.color("#ffdd44", "pupil_glow")
pupil_core = c.color("#ffffff", "pupil_core")

# Tentacle colors
tentacle_dark = c.color("#2d1245", "tentacle_dark")
tentacle_mid = c.color("#4a1f70", "tentacle_mid")
tentacle_light = c.color("#6a3a9a", "tentacle_light")

# Shadow colors
shadow_dark = c.color("#0a0a0a", "shadow_dark")
shadow_mid = c.color("#1a1a1a", "shadow_mid")
shadow_light = c.color("#2a2a2a", "shadow_light")

# Draw soft shadow underneath (elliptical, below the eye) - more subtle
c.ellipse(32, 56, 18, 3, shadow_dark, fill=True)
c.ellipse(32, 55, 15, 2, shadow_mid, fill=True)
c.ellipse(32, 54, 12, 1, shadow_light, fill=True)

# Draw tentacles - make them thicker and more visible with filled shapes
# Left side tentacles
# Tentacle 1 - left outer
c.path("M 14 42 Q 8 48 10 52 Q 14 54 16 50 Q 14 56 12 58", tentacle_dark, fill=False)
c.set(10, 50, tentacle_mid)
c.set(12, 54, tentacle_light)

# Tentacle 2 - left middle  
c.path("M 20 44 Q 14 52 16 56 Q 20 58 22 54 Q 20 58 18 60", tentacle_mid, fill=False)
c.set(16, 54, tentacle_light)

# Tentacle 3 - left inner
c.path("M 25 46 Q 22 54 24 58 Q 28 60 30 56", tentacle_light, fill=False)
c.set(24, 56, tentacle_mid)

# Right side tentacles (mirrored)
# Tentacle 4 - right outer
c.path("M 50 42 Q 56 48 54 52 Q 50 54 48 50 Q 50 56 52 58", tentacle_dark, fill=False)
c.set(54, 50, tentacle_mid)
c.set(52, 54, tentacle_light)

# Tentacle 5 - right middle
c.path("M 44 44 Q 50 52 48 56 Q 44 58 42 54 Q 44 58 46 60", tentacle_mid, fill=False)
c.set(48, 54, tentacle_light)

# Tentacle 6 - right inner
c.path("M 39 46 Q 42 54 40 58 Q 36 60 34 56", tentacle_light, fill=False)
c.set(40, 56, tentacle_mid)

# Center tentacles (hanging down)
c.path("M 28 48 Q 28 56 30 60 Q 32 62 34 58", tentacle_mid, fill=False)
c.path("M 36 48 Q 36 56 34 60 Q 32 62 30 58", tentacle_light, fill=False)

# Draw main eye body (large circle, dark purple)
c.circle(32, 32, 22, body_dark, fill=True)

# Add dimension to the eye body with gradient layers
c.circle(32, 32, 19, body_mid, fill=True)
c.circle(32, 31, 16, body_light, fill=True)
c.circle(32, 30, 13, body_highlight, fill=True)

# Add subtle rim light on top of eye
c.path("M 16 16 Q 32 10 48 16", body_highlight, fill=False)
c.path("M 20 18 Q 32 14 44 18", body_light, fill=False)

# Draw iris (deep purple gradient) - larger and more prominent
c.circle(32, 32, 14, iris_outer, fill=True)
c.circle(32, 32, 11, iris_mid, fill=True)
c.circle(32, 32, 8, iris_inner, fill=True)
c.circle(32, 32, 5, iris_bright, fill=True)

# Draw pupil (glowing yellow/orange) - larger for more impact
c.circle(32, 32, 5, pupil_dark, fill=True)
c.circle(32, 32, 3, pupil_bright, fill=True)
c.circle(32, 32, 1, pupil_glow, fill=True)
c.set(32, 32, pupil_core)

# Add glow effect around pupil
c.circle(32, 32, 6, pupil_glow, fill=False)
c.circle(32, 32, 7, pupil_bright, fill=False)

# Add highlights to eye for dimension (top-left highlight)
c.circle(24, 24, 3, body_highlight, fill=True)
c.set(25, 25, "#ffffff")

# Add secondary highlight (bottom-right rim)
c.path("M 42 42 Q 46 44 44 46", body_light, fill=False)

# Add vein-like details on the eye body for ominous effect
c.path("M 18 28 Q 22 30 20 34", body_dark, fill=False)
c.path("M 46 28 Q 42 30 44 34", body_dark, fill=False)

# Add small accent dots on iris for texture
c.set(28, 28, iris_bright)
c.set(36, 36, iris_bright)
c.set(28, 36, iris_mid)
c.set(36, 28, iris_mid)

# Add some scattered pixels for eye texture
c.set(22, 30, body_mid)
c.set(42, 30, body_mid)
c.set(32, 22, body_mid)

# Add tentacle suction cups (small dots)
c.set(12, 54, tentacle_light)
c.set(18, 58, tentacle_light)
c.set(52, 54, tentacle_light)
c.set(46, 58, tentacle_light)
c.set(30, 60, tentacle_light)
c.set(34, 60, tentacle_light)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

finish(c)
