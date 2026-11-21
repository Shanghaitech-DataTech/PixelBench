from pixelbench_api import new_canvas, finish

# Create 16x16 canvas with transparent background
c = new_canvas(16, 16, background=None, name="mushroomling")

# Define 4 colors: red cap, white spots/eyes, dark outline, tan body
red = c.color("#D32F2F", "red")
white = c.color("#FFFFFF", "white")
dark = c.color("#1A1A1A", "dark")
tan = c.color("#D4A574", "tan")

# === MUSHROOM CAP (red dome) ===
# Row 2: top of cap (narrow)
c.set(6, 2, red)
c.set(7, 2, red)
c.set(8, 2, red)
c.set(9, 2, red)

# Row 3: cap wider
c.rect(5, 3, 6, 1, red)

# Row 4: cap wider (has eyes here)
c.rect(4, 4, 8, 1, red)

# Row 5: widest part of cap
c.rect(3, 5, 10, 1, red)

# Row 6: bottom of cap
c.rect(3, 6, 10, 1, red)

# === CAP OUTLINE (dark) ===
# Top edge
c.set(6, 2, dark)
c.set(9, 2, dark)
# Sides row 3
c.set(5, 3, dark)
c.set(10, 3, dark)
# Sides row 4
c.set(4, 4, dark)
c.set(11, 4, dark)
# Sides row 5
c.set(3, 5, dark)
c.set(12, 5, dark)
# Sides row 6
c.set(3, 6, dark)
c.set(12, 6, dark)
# Bottom edge of cap
c.set(4, 7, dark)
c.set(5, 7, dark)
c.set(10, 7, dark)
c.set(11, 7, dark)

# === WHITE SPOTS on cap ===
c.set(6, 3, white)
c.set(9, 3, white)
c.set(5, 5, white)
c.set(10, 5, white)
c.set(7, 4, white)

# === EYES (round, white with dark pupils) ===
# Left eye
c.set(6, 4, white)
c.set(7, 4, white)
c.set(6, 5, white)
c.set(7, 5, white)
c.set(7, 4, dark)  # pupil
# Right eye
c.set(8, 4, white)
c.set(9, 4, white)
c.set(8, 5, white)
c.set(9, 5, white)
c.set(8, 4, dark)  # pupil

# === BODY/STEM (tan) ===
c.rect(6, 7, 4, 3, tan)

# === BODY OUTLINE (dark) ===
c.set(6, 7, dark)
c.set(9, 7, dark)
c.set(6, 8, dark)
c.set(9, 8, dark)
c.set(6, 9, dark)
c.set(9, 9, dark)
c.set(7, 10, dark)
c.set(8, 10, dark)

# === ARMS (tan with dark outline) ===
# Left arm
c.set(5, 8, tan)
c.set(4, 8, dark)
c.set(5, 9, dark)
# Right arm
c.set(10, 8, tan)
c.set(11, 8, dark)
c.set(10, 9, dark)

# === LEGS (tan with dark outline) ===
# Left leg
c.set(6, 10, tan)
c.set(6, 11, tan)
c.set(5, 11, dark)
c.set(6, 12, dark)
c.set(7, 12, dark)
# Right leg
c.set(9, 10, tan)
c.set(9, 11, tan)
c.set(10, 11, dark)
c.set(8, 12, dark)
c.set(9, 12, dark)

# Check stats
print(c.stats_text())

# Submit the canvas
finish(c)
