from pixelbench_api import new_canvas, finish

# Create 48x48 canvas with transparent background
c = new_canvas(48, 48, background=None, name="polar_researcher")

# Define color palette for polar researcher
# Dark blues and grays for parka, skin tones, pale blue for goggles
colors = {
    'parka_dark': '#1a2f4a',      # Dark blue parka
    'parka_mid': '#2d4a6f',       # Mid blue parka
    'parka_light': '#4a6f94',     # Light blue parka highlight
    'pants_dark': '#2a2a3a',      # Dark pants
    'pants_mid': '#3a3a4a',       # Mid pants
    'boots': '#1a1a1a',           # Black boots
    'boots_trim': '#4a4a5a',      # Boot trim
    'gloves': '#2a2a3a',          # Dark gloves
    'skin': '#d4a574',            # Skin tone
    'skin_shadow': '#b8905a',     # Skin shadow
    'goggle_frame': '#3a3a3a',    # Goggle frame
    'goggle_dark': '#1a2a3a',     # Goggle lens dark
    'goggle_blue': '#6ab4d4',     # Pale blue reflection
    'goggle_light': '#9ad4f4',    # Lighter blue highlight
    'case_dark': '#4a3a2a',       # Sample case dark
    'case_mid': '#6a5a4a',        # Sample case mid
    'case_light': '#8a7a6a',      # Sample case light
    'case_metal': '#7a8a9a',      # Metal clasp
    'scarf': '#5a4a6a',           # Purple scarf
    'scarf_light': '#7a6a8a',     # Scarf highlight
    'wind_white': '#e8e8f0',      # Wind/snow particles
}

# Register colors
for name, hex_val in colors.items():
    c.color(hex_val, name)

# Draw the polar researcher - forward leaning pose
# Working from back to front, bottom to top

# === BOOTS ===
# Left boot (back foot, slightly raised by wind)
c.rect(18, 38, 8, 6, 'boots', fill=True)
c.rect(18, 37, 8, 2, 'boots_trim', fill=True)

# Right boot (front foot, planted)
c.rect(26, 40, 9, 6, 'boots', fill=True)
c.rect(26, 39, 9, 2, 'boots_trim', fill=True)

# === PANTS ===
# Left leg (back, bent slightly)
c.rect(17, 28, 10, 12, 'pants_dark', fill=True)
c.rect(18, 28, 4, 10, 'pants_mid', fill=True)

# Right leg (front, leaning forward)
c.rect(25, 26, 11, 15, 'pants_dark', fill=True)
c.rect(26, 26, 5, 13, 'pants_mid', fill=True)

# === PARKA BODY ===
# Main parka body - heavy, bulky, leaning forward
# Back/lower part
c.rect(14, 14, 24, 18, 'parka_dark', fill=True)
# Mid section with folds
c.rect(15, 15, 22, 16, 'parka_mid', fill=True)
# Front/highlight section
c.rect(16, 16, 18, 14, 'parka_light', fill=True)

# Parka hood area (around head)
c.rect(18, 8, 16, 10, 'parka_dark', fill=True)
c.rect(19, 9, 14, 8, 'parka_mid', fill=True)

# === ARMS ===
# Back arm (left, holding case down)
c.rect(10, 18, 6, 14, 'parka_dark', fill=True)
c.rect(11, 19, 4, 12, 'parka_mid', fill=True)
# Left glove
c.rect(8, 30, 7, 6, 'gloves', fill=True)

# Front arm (right, bent forward into wind)
c.rect(32, 16, 7, 12, 'parka_dark', fill=True)
c.rect(33, 17, 5, 10, 'parka_mid', fill=True)
# Right glove (reaching forward)
c.rect(36, 24, 7, 5, 'gloves', fill=True)

# === SAMPLE CASE ===
# Held in left hand, rectangular case
c.rect(6, 32, 10, 7, 'case_dark', fill=True)
c.rect(7, 33, 8, 5, 'case_mid', fill=True)
c.rect(8, 34, 6, 3, 'case_light', fill=True)
# Metal clasp
c.rect(11, 34, 3, 2, 'case_metal', fill=True)
# Handle
c.rect(8, 31, 6, 2, 'case_dark', fill=True)

# === SCARF ===
# Flowing behind in the wind
c.rect(12, 10, 8, 4, 'scarf', fill=True)
c.rect(10, 8, 6, 4, 'scarf_light', fill=True)
# Scarf tail blowing back
c.poly([(6, 8), (12, 8), (14, 10), (10, 12), (4, 11)], 'scarf', fill=True)
c.poly([(7, 9), (11, 9), (12, 10), (9, 11), (5, 10)], 'scarf_light', fill=True)

# === HEAD ===
# Face area (partially visible under hood)
c.rect(22, 10, 10, 8, 'skin', fill=True)
c.rect(23, 11, 8, 6, 'skin_shadow', fill=True)

# === GOGGLES ===
# Goggle frame
c.rect(21, 11, 12, 5, 'goggle_frame', fill=True)
# Goggle lenses (dark)
c.rect(22, 12, 5, 3, 'goggle_dark', fill=True)
c.rect(28, 12, 5, 3, 'goggle_dark', fill=True)

# Goggle reflections (pale blue) - key feature
# Left lens reflection
c.rect(23, 12, 3, 2, 'goggle_blue', fill=True)
c.set(23, 12, 'goggle_light')
# Right lens reflection  
c.rect(29, 12, 3, 2, 'goggle_blue', fill=True)
c.set(29, 12, 'goggle_light')

# === HOOD TRIM ===
# Fur trim around hood (simplified as textured edge)
c.rect(17, 7, 18, 3, 'parka_light', fill=True)

# === WIND EFFECTS ===
# Snow/wind particles blowing past
c.set(4, 15, 'wind_white')
c.set(2, 20, 'wind_white')
c.set(5, 25, 'wind_white')
c.set(3, 35, 'wind_white')
c.set(42, 12, 'wind_white')
c.set(44, 18, 'wind_white')
c.set(43, 24, 'wind_white')
c.set(45, 30, 'wind_white')

# Wind streaks (horizontal lines suggesting movement)
c.line(0, 16, 8, 16, 'wind_white')
c.line(0, 22, 6, 22, 'wind_white')
c.line(40, 14, 47, 14, 'wind_white')
c.line(41, 26, 47, 26, 'wind_white')

# === FINAL DETAILS ===
# Parka zipper detail
c.line(26, 16, 26, 28, 'parka_dark')

# Add some depth to the parka with additional highlights
c.set(20, 18, 'parka_light')
c.set(24, 20, 'parka_light')
c.set(28, 22, 'parka_light')

# Boot highlights
c.set(20, 39, 'boots_trim')
c.set(28, 41, 'boots_trim')

# Check stats
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 47, 47)))

# Submit the result
finish(c)
