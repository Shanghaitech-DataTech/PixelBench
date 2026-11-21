from pixelbench_api import new_canvas, finish

# Create a 32x32 canvas
c = new_canvas(32, 32, name="scooter_rider")

# Define colors (keep under 86 visible colors)
black = c.color("#1a1a2e")      # Dark outline/shadows
dark_gray = c.color("#4a4a5a")  # Scooter frame dark
light_gray = c.color("#8a8a9a") # Scooter frame light
white = c.color("#f0f0f0")      # Highlights
skin = c.color("#e0b090")       # Skin tone
helmet = c.color("#ff6b6b")     # Red helmet
helmet_dark = c.color("#cc5555") # Helmet shadow
shirt = c.color("#4ecdc4")      # Teal shirt
pants = c.color("#2d3436")      # Dark pants
wheel = c.color("#2d2d2d")      # Wheel dark
tire = c.color("#1a1a1a")       # Tire
shadow = c.color("#3a3a4a")     # Ground shadow

c.clear()

# === SCOOTER WHEELS ===
# Back wheel - center (4, 26), radius 4
c.circle(4, 26, 4, tire, fill=True)
c.circle(4, 26, 3, wheel, fill=True)
c.circle(4, 26, 1, light_gray, fill=True)

# Front wheel - center (27, 26), radius 4
c.circle(27, 26, 4, tire, fill=True)
c.circle(27, 26, 3, wheel, fill=True)
c.circle(27, 26, 1, light_gray, fill=True)

# === SCOOTER DECK ===
# Main platform between wheels
c.rect(6, 24, 19, 3, dark_gray, fill=True)
c.rect(6, 23, 19, 1, light_gray, fill=True)

# === SCOOTER STEM (vertical pole) ===
# Connects deck to handlebars, angled slightly
c.rect(23, 13, 2, 11, dark_gray, fill=True)
c.rect(24, 13, 1, 11, light_gray, fill=True)

# === HANDLEBARS ===
# Horizontal bar
c.rect(20, 11, 9, 2, dark_gray, fill=True)
c.rect(20, 10, 9, 1, light_gray, fill=True)
# Grips at ends
c.set(19, 11, black)
c.set(19, 10, black)
c.set(29, 11, black)
c.set(29, 10, black)

# === RIDER ===
# Rider is standing, leaning forward, holding handlebars

# Back leg (left) - from hip to foot on deck
c.rect(12, 19, 3, 6, pants, fill=True)
# Front leg (right) - slightly forward, bent
c.rect(16, 19, 3, 6, pants, fill=True)

# Shoes on deck
c.rect(11, 24, 4, 2, black, fill=True)
c.rect(16, 24, 4, 2, black, fill=True)

# Torso - leaning forward significantly (riding pose)
c.rect(12, 11, 7, 9, shirt, fill=True)

# Arms - reaching forward and up to grips
# Back arm (left) - shoulder to elbow to hand
c.line(13, 12, 18, 11, skin)
c.line(18, 11, 23, 11, skin)
# Front arm (right)
c.line(17, 13, 22, 11, skin)
c.line(22, 11, 27, 11, skin)

# Hands on grips
c.set(23, 11, skin)
c.set(27, 11, skin)

# Neck
c.rect(14, 9, 2, 3, skin, fill=True)

# Head - side view, facing right, tilted slightly down
c.circle(16, 7, 4, skin, fill=True)

# Helmet - covers top/back of head
c.circle(16, 6, 5, helmet, fill=True)
# Helmet visor/front shadow
c.rect(17, 6, 3, 2, helmet_dark, fill=True)
# Helmet stripe
c.rect(13, 4, 5, 1, white, fill=True)

# Face details - side view looking right
c.set(18, 6, black)  # Eye
c.set(19, 8, "#c09080")  # Mouth area

# === GROUND SHADOW ===
c.rect(3, 30, 26, 1, shadow, fill=True)

# === SPEED LINES (motion effect) ===
c.set(1, 15, light_gray)
c.set(0, 16, light_gray)
c.set(1, 17, light_gray)
c.set(2, 26, light_gray)
c.set(1, 27, light_gray)

print(c.stats_text())
print(c.matrix_text())

finish(c)
