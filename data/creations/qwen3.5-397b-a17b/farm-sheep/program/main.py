from pixelbench_api import new_canvas, finish

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="sheep")

# Warm muted Stardew Valley palette - cozy farm style
wool_white = c.color("#FAF7F0", "wool_white")
wool_cream = c.color("#F2EAD8", "wool_cream")
wool_light = c.color("#E8DCC0", "wool_light")
wool_shadow = c.color("#D4C5A8", "wool_shadow")
wool_dark = c.color("#B8A588", "wool_dark")
ear_pink = c.color("#F5CFC5", "ear_pink")
ear_inner = c.color("#E8B5A5", "ear_inner")
eye_dark = c.color("#3D3020", "eye_dark")
eye_highlight = c.color("#FFFFFF", "eye_highlight")
nose_pink = c.color("#E89888", "nose_pink")
hoof_brown = c.color("#856848", "hoof_brown")
mouth = c.color("#9A7858", "mouth")

# Build fluffy body from bottom up
# Lower belly - main mass
c.circle(16, 23, 7, wool_white, fill=True)
c.circle(19, 22, 6, wool_cream, fill=True)
c.circle(13, 22, 6, wool_light, fill=True)

# Middle body - fluffy cloud shape
c.circle(17, 18, 7, wool_white, fill=True)
c.circle(21, 18, 6, wool_cream, fill=True)
c.circle(13, 18, 6, wool_light, fill=True)
c.circle(19, 17, 7, wool_white, fill=True)

# Upper back
c.circle(17, 14, 6, wool_white, fill=True)
c.circle(20, 13, 5, wool_cream, fill=True)
c.circle(14, 14, 5, wool_light, fill=True)

# Fluffy tufts around edges
c.circle(9, 18, 4, wool_cream, fill=True)
c.circle(26, 17, 4, wool_white, fill=True)
c.circle(17, 10, 4, wool_cream, fill=True)
c.circle(17, 26, 4, wool_light, fill=True)
c.circle(7, 20, 3, wool_light, fill=True)
c.circle(28, 18, 3, wool_cream, fill=True)
c.circle(11, 24, 3, wool_white, fill=True)
c.circle(23, 22, 3, wool_cream, fill=True)

# Subtle shading on underside
c.circle(15, 25, 3, wool_shadow, fill=True)
c.circle(19, 25, 3, wool_shadow, fill=True)
c.circle(17, 26, 2, wool_dark, fill=True)
c.circle(14, 24, 2, wool_shadow, fill=True)

# Head - round and cute, facing left
c.circle(7, 12, 5, wool_white, fill=True)
c.circle(5, 12, 4, wool_cream, fill=True)
c.circle(9, 11, 4, wool_white, fill=True)
c.circle(4, 13, 3, wool_light, fill=True)

# Ears - pale pink, droopy and cute
# Front ear
c.ellipse(3, 8, 3, 2, ear_pink, fill=True)
c.ellipse(2, 7, 2, 2, ear_pink, fill=True)
c.set(2, 8, ear_inner)

# Back ear
c.ellipse(8, 7, 3, 2, wool_cream, fill=True)
c.set(8, 7, ear_pink)

# Face
# Eye - simple cute style
c.set(5, 11, eye_dark)
c.set(6, 11, eye_dark)
c.set(5, 12, eye_dark)
c.set(6, 12, eye_highlight)

# Nose
c.set(1, 13, nose_pink)
c.set(2, 13, nose_pink)
c.set(1, 14, nose_pink)

# Smile
c.set(3, 14, mouth)
c.set(4, 15, mouth)

# Cheek
c.set(4, 12, ear_pink)

# Legs - short and stubby (adjusted to fit in canvas)
# Front left
c.rect(12, 26, 3, 4, wool_white, fill=True)
c.rect(12, 29, 3, 2, hoof_brown, fill=True)

# Front right
c.rect(20, 26, 3, 4, wool_cream, fill=True)
c.rect(20, 29, 3, 2, hoof_brown, fill=True)

# Back legs
c.rect(15, 27, 2, 3, wool_light, fill=True)
c.rect(15, 29, 2, 2, hoof_brown, fill=True)
c.rect(23, 27, 2, 3, wool_cream, fill=True)
c.rect(23, 29, 2, 1, hoof_brown, fill=True)

# Tail - fluffy puff
c.circle(27, 16, 3, wool_white, fill=True)
c.circle(28, 15, 2, wool_cream, fill=True)

# Extra fluff details
c.set(8, 16, wool_cream)
c.set(10, 15, wool_cream)
c.set(11, 20, wool_light)
c.set(24, 17, wool_cream)
c.set(21, 11, wool_cream)
c.set(15, 12, wool_white)
c.set(10, 23, wool_shadow)
c.set(7, 9, wool_cream)
c.set(12, 10, wool_cream)
c.set(19, 9, wool_cream)
c.set(25, 14, wool_white)

print(c.stats_text())
print(c.matrix_text())

finish(c)
