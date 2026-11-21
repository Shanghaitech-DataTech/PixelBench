from pixelbench_api import *

# Create 128x128 canvas
c = new_canvas(128, 128, name="standoff")

# Define palette - keeping under 86 colors total
# Background
c.color("#1a0f2e", "bg_dark")      # Dark purple background
c.color("#2d1f4a", "bg_mid")       # Mid purple
c.color("#4a3568", "bg_light")     # Light purple

# Knight colors (red armor)
c.color("#8b0000", "knight_dark")   # Dark red
c.color("#c41e3a", "knight_main")   # Main red
c.color("#e63946", "knight_bright") # Bright red
c.color("#ff6b6b", "knight_highlight") # Highlight
c.color("#4a0a0a", "knight_shadow") # Deep shadow
c.color("#ffd700", "knight_gold")   # Gold trim
c.color("#b8860b", "knight_gold_dark") # Dark gold
c.color("#2a2a2a", "knight_steel")  # Steel/dark metal
c.color("#666666", "knight_steel_mid") # Mid steel
c.color("#999999", "knight_steel_bright") # Bright steel

# Rogue colors (green cloak)
c.color("#1a4d1a", "rogue_dark")    # Dark green
c.color("#2d6b2d", "rogue_main")    # Main green
c.color("#4a8f4a", "rogue_bright")  # Bright green
c.color("#7ab87a", "rogue_highlight") # Highlight
c.color("#0d260d", "rogue_shadow")  # Deep shadow
c.color("#3d3d3d", "rogue_leather") # Leather/dark
c.color("#5c4d3d", "rogue_brown")   # Brown
c.color("#8b7355", "rogue_brown_light") # Light brown
c.color("#1a1a1a", "rogue_black")   # Black accents

# Skin tones (shared)
c.color("#ffdbac", "skin_light")    # Light skin
c.color("#e0b084", "skin_mid")      # Mid skin
c.color("#c4915e", "skin_shadow")   # Shadow skin

# Eyes
c.color("#ffffff", "eye_white")
c.color("#000000", "eye_black")
c.color("#87ceeb", "eye_blue")      # Knight eye
c.color("#90ee90", "eye_green")     # Rogue eye

# Weapon colors
c.color("#c0c0c0", "blade_light")   # Sword blade
c.color("#808080", "blade_mid")     # Mid blade
c.color("#505050", "blade_dark")    # Dark blade
c.color("#654321", "handle_brown")  # Handle

# Effects
c.color("#ff4500", "effect_orange") # Spark/energy
c.color("#ffff00", "effect_yellow") # Bright spark

# === BACKGROUND ===
# Gradient background
for y in range(128):
    ratio = y / 127
    if ratio < 0.3:
        col = "bg_dark"
    elif ratio < 0.6:
        col = "bg_mid"
    else:
        col = "bg_light"
    c.rect(0, y, 128, 1, col)

# Ground line
c.rect(0, 100, 128, 28, "#2a1a3a")
c.rect(0, 105, 128, 5, "#3a2a4a")

# === KNIGHT (LEFT SIDE) ===
# Position: centered around x=32, y=85 (feet)

# Knight body/armor silhouette
# Legs
c.rect(24, 75, 6, 25, "knight_dark")  # Left leg
c.rect(36, 75, 6, 25, "knight_dark")  # Right leg
c.rect(25, 75, 4, 25, "knight_main")  # Left leg highlight
c.rect(37, 75, 4, 25, "knight_main")  # Right leg highlight

# Boots
c.rect(23, 95, 8, 8, "knight_shadow")
c.rect(35, 95, 8, 8, "knight_shadow")
c.rect(24, 96, 6, 5, "knight_steel")

# Torso armor
c.rect(22, 45, 24, 32, "knight_main")  # Main torso
c.rect(24, 47, 20, 28, "knight_dark")  # Inner armor plates
c.rect(26, 49, 16, 24, "knight_bright") # Chest plate

# Armor details - horizontal plates
c.rect(22, 55, 24, 3, "knight_dark")
c.rect(22, 65, 24, 3, "knight_dark")
c.rect(24, 56, 20, 1, "knight_gold")
c.rect(24, 66, 20, 1, "knight_gold")

# Shoulder pads (pauldrons)
c.rect(18, 42, 8, 10, "knight_dark")  # Left shoulder
c.rect(42, 42, 8, 10, "knight_dark")  # Right shoulder
c.rect(19, 43, 6, 8, "knight_main")
c.rect(43, 43, 6, 8, "knight_main")
c.rect(20, 44, 4, 6, "knight_bright")
c.rect(44, 44, 4, 6, "knight_bright")

# Arms
c.rect(16, 50, 6, 20, "knight_main")  # Left arm
c.rect(46, 50, 6, 20, "knight_main")  # Right arm
c.rect(17, 52, 4, 16, "knight_dark")
c.rect(47, 52, 4, 16, "knight_dark")

# Gauntlets
c.rect(15, 68, 8, 8, "knight_steel")
c.rect(45, 68, 8, 8, "knight_steel")
c.rect(16, 69, 6, 6, "knight_steel_mid")

# Helmet
c.rect(24, 20, 20, 22, "knight_main")  # Main helmet
c.rect(26, 22, 16, 18, "knight_dark")  # Inner
c.rect(28, 24, 12, 14, "knight_bright") # Face plate

# Helmet visor (T-shape)
c.rect(30, 30, 8, 3, "knight_shadow")  # Eye slit
c.rect(34, 30, 2, 8, "knight_shadow")  # Vertical slit

# Helmet crest
c.rect(32, 12, 4, 10, "knight_bright")
c.rect(30, 10, 8, 4, "knight_gold")
c.rect(32, 8, 4, 4, "knight_gold_dark")

# Knight's sword (held in right hand, pointing down-left)
# Blade
c.line(52, 55, 35, 85, "blade_light")
c.line(54, 56, 37, 86, "blade_light")
c.line(53, 55, 36, 85, "blade_mid")
# Hilt
c.rect(50, 52, 6, 4, "knight_gold")
c.rect(51, 50, 4, 4, "knight_gold_dark")
# Handle
c.rect(51, 48, 4, 4, "handle_brown")

# Knight's shield (on left arm)
c.ellipse(12, 58, 8, 12, "knight_main", fill=True)
c.ellipse(13, 58, 6, 10, "knight_dark", fill=True)
c.ellipse(14, 58, 4, 7, "knight_bright", fill=True)
# Shield emblem
c.rect(12, 52, 4, 6, "knight_gold")

# === ROGUE (RIGHT SIDE) ===
# Position: centered around x=96, y=85 (feet)

# Flowing cloak
c.poly([(82, 35), (80, 100), (88, 105), (92, 100), (96, 105), (104, 100), (110, 95), (112, 40), (105, 35), (96, 38), (88, 35)], "rogue_dark", fill=True)
c.poly([(84, 38), (83, 95), (89, 98), (92, 95), (96, 100), (102, 95), (108, 90), (109, 42), (104, 38), (96, 40), (90, 38)], "rogue_main", fill=True)
c.poly([(86, 42), (86, 85), (90, 88), (92, 85), (96, 90), (100, 85), (105, 80), (106, 45), (102, 42), (96, 43), (92, 42)], "rogue_bright", fill=True)

# Hood
c.rect(90, 28, 16, 14, "rogue_dark")
c.rect(91, 30, 14, 11, "rogue_main")
c.rect(92, 32, 12, 8, "rogue_bright")

# Face (partially visible under hood)
c.rect(93, 38, 10, 10, "skin_mid")
c.rect(94, 39, 8, 8, "skin_light")

# Eyes (glowing)
c.rect(95, 40, 2, 2, "eye_black")
c.rect(99, 40, 2, 2, "eye_black")
c.rect(95, 40, 1, 1, "eye_green")
c.rect(99, 40, 1, 1, "eye_green")

# Body under cloak (leaner than knight)
c.rect(90, 50, 16, 25, "rogue_leather")
c.rect(92, 52, 12, 20, "rogue_brown")

# Belt
c.rect(90, 68, 16, 3, "rogue_brown_light")
c.rect(97, 68, 4, 4, "knight_gold")  # Buckle

# Legs
c.rect(88, 75, 7, 20, "rogue_leather")
c.rect(99, 75, 7, 20, "rogue_leather")
c.rect(89, 76, 5, 18, "rogue_brown")
c.rect(100, 76, 5, 18, "rogue_brown")

# Boots
c.rect(86, 93, 9, 7, "rogue_black")
c.rect(97, 93, 9, 7, "rogue_black")
c.rect(87, 94, 7, 5, "rogue_brown_light")
c.rect(98, 94, 7, 5, "rogue_brown_light")

# Arms (thin, agile)
c.rect(80, 52, 6, 18, "rogue_main")
c.rect(108, 52, 6, 18, "rogue_main")
c.rect(81, 54, 4, 14, "rogue_dark")
c.rect(109, 54, 4, 14, "rogue_dark")

# Gloves
c.rect(78, 68, 8, 6, "rogue_leather")
c.rect(108, 68, 8, 6, "rogue_leather")

# Daggers (dual wielding)
# Left dagger (pointing up-left)
c.line(78, 65, 68, 45, "blade_light")
c.line(80, 66, 70, 46, "blade_light")
c.line(79, 65, 69, 45, "blade_mid")
c.rect(76, 64, 4, 4, "handle_brown")

# Right dagger (pointing down-right)
c.line(116, 68, 126, 85, "blade_light")
c.line(114, 69, 124, 86, "blade_light")
c.line(115, 68, 125, 85, "blade_mid")
c.rect(114, 66, 4, 4, "handle_brown")

# Cloak motion lines (wind effect)
c.line(78, 50, 70, 55, "rogue_highlight")
c.line(80, 60, 72, 65, "rogue_highlight")
c.line(112, 55, 120, 52, "rogue_highlight")
c.line(110, 70, 118, 68, "rogue_highlight")

# === DRAMATIC EFFECTS ===
# Ground cracks between them
c.line(60, 110, 68, 120, "#1a0f2e")
c.line(64, 108, 66, 118, "#1a0f2e")
c.line(68, 112, 72, 122, "#1a0f2e")

# Energy sparks in the gap
c.rect(62, 70, 2, 2, "effect_yellow")
c.rect(66, 80, 2, 2, "effect_orange")
c.rect(64, 90, 2, 2, "effect_yellow")
c.rect(58, 75, 1, 1, "effect_orange")
c.rect(70, 85, 1, 1, "effect_yellow")

# Light rim on knight (backlight from right)
c.line(46, 45, 48, 70, "knight_highlight")
c.line(42, 25, 44, 42, "knight_highlight")

# Light rim on rogue (backlight from left)
c.line(82, 40, 80, 75, "rogue_highlight")
c.line(86, 30, 84, 38, "rogue_highlight")

# Shadow under knight
c.rect(20, 102, 30, 4, "#0a0510")
# Shadow under rogue
c.rect(82, 102, 30, 4, "#0a0510")

print(c.stats_text())
print(c.stats_text())

finish(c)
