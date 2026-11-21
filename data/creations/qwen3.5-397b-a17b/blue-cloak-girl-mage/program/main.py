from pixelbench_api import *

# Create 64x64 canvas for the mage character
c = new_canvas(64, 64, background=None, name="mage")

# Define color palette
# Dark blue cloak colors
c.color("#1a2d4a", "cloak_dark")      # Darkest blue
c.color("#2d4a7a", "cloak_mid")       # Mid blue
c.color("#4a6ba0", "cloak_light")     # Light blue highlight
c.color("#6b8cc4", "cloak_highlight") # Highlight

# White boots
c.color("#ffffff", "boot_white")
c.color("#d0d0d0", "boot_shadow")
c.color("#a0a0a0", "boot_dark")

# Amber staff glow
c.color("#ffaa00", "amber_bright")
c.color("#ff8800", "amber_mid")
c.color("#cc6600", "amber_dark")
c.color("#ffeeaa", "glow_core")
c.color("#ffdd88", "glow_outer")

# Skin tones
c.color("#ffdbac", "skin_light")
c.color("#e8c090", "skin_mid")
c.color("#d4a574", "skin_shadow")

# Hair color (silver/white for mage)
c.color("#f0f0f0", "hair_light")
c.color("#c0c0c0", "hair_mid")
c.color("#909090", "hair_shadow")

# Eyes
c.color("#4a90d9", "eye_blue")
c.color("#2d5a8a", "eye_dark")
c.color("#ffffff", "eye_highlight")

# Staff wood
c.color("#8b6f47", "wood_dark")
c.color("#a68b5e", "wood_mid")
c.color("#c4a87a", "wood_light")

# Outline/shadows
c.color("#0a1525", "outline")

# Draw the character from back to front

# === CLOAK (back layer) ===
# Main cloak body - flowing behind
c.rect(20, 28, 24, 32, "cloak_dark", fill=True)
c.rect(18, 30, 28, 28, "cloak_mid", fill=True)

# Cloak shoulders
c.rect(16, 22, 12, 12, "cloak_dark", fill=True)
c.rect(36, 22, 12, 12, "cloak_dark", fill=True)

# Cloak hood/back
c.rect(24, 14, 16, 12, "cloak_dark", fill=True)
c.rect(22, 16, 20, 8, "cloak_mid", fill=True)

# Cloak folds and highlights
c.rect(22, 32, 4, 24, "cloak_light", fill=True)
c.rect(38, 32, 3, 20, "cloak_light", fill=True)
c.rect(20, 40, 6, 8, "cloak_highlight", fill=True)

# Cloak bottom edge
c.poly([(18, 58), (22, 60), (28, 58), (34, 60), (40, 58), (44, 60), (46, 56), 
        (44, 54), (40, 56), (34, 54), (28, 56), (22, 54), (18, 56)], 
       "cloak_dark", fill=True)

# === BOOTS ===
# Left boot
c.rect(24, 54, 6, 8, "boot_white", fill=True)
c.rect(24, 58, 6, 3, "boot_shadow", fill=True)
c.rect(25, 54, 2, 4, "boot_dark", fill=True)

# Right boot
c.rect(34, 54, 6, 8, "boot_white", fill=True)
c.rect(34, 58, 6, 3, "boot_shadow", fill=True)
c.rect(37, 54, 2, 4, "boot_dark", fill=True)

# === LEGS (visible between cloak and boots) ===
c.rect(25, 50, 4, 6, "skin_mid", fill=True)
c.rect(35, 50, 4, 6, "skin_mid", fill=True)

# === STAFF ===
# Staff shaft
c.rect(46, 20, 4, 42, "wood_mid", fill=True)
c.rect(47, 20, 2, 42, "wood_light", fill=True)
c.rect(46, 20, 1, 42, "wood_dark", fill=True)

# Staff top crystal/glow
c.circle(48, 18, 6, "amber_bright", fill=True)
c.circle(48, 18, 4, "amber_mid", fill=True)
c.circle(48, 18, 2, "glow_core", fill=True)

# Glow effect around staff
c.circle(48, 18, 8, "glow_outer", fill=False)
c.circle(48, 18, 10, "amber_bright", fill=False)

# === BODY/TORSO ===
c.rect(26, 26, 12, 18, "cloak_mid", fill=True)
c.rect(28, 28, 8, 14, "cloak_light", fill=True)

# === ARMS ===
# Left arm (holding staff)
c.rect(40, 28, 8, 4, "skin_mid", fill=True)
c.rect(42, 30, 6, 3, "skin_light", fill=True)

# Right arm (relaxed at side)
c.rect(16, 30, 8, 4, "skin_mid", fill=True)
c.rect(18, 32, 6, 3, "skin_light", fill=True)

# === HEAD ===
# Face base
c.rect(26, 12, 12, 14, "skin_light", fill=True)
c.rect(28, 14, 8, 10, "skin_mid", fill=True)

# Hair
c.rect(24, 8, 16, 8, "hair_light", fill=True)
c.rect(22, 10, 20, 6, "hair_mid", fill=True)
c.rect(26, 6, 12, 4, "hair_shadow", fill=True)

# Hair strands
c.rect(22, 14, 3, 8, "hair_mid", fill=True)
c.rect(39, 14, 3, 8, "hair_mid", fill=True)

# Eyes
c.rect(28, 16, 3, 3, "eye_blue", fill=True)
c.rect(33, 16, 3, 3, "eye_blue", fill=True)
c.set(29, 17, "eye_dark")
c.set(34, 17, "eye_dark")
c.set(29, 16, "eye_highlight")
c.set(34, 16, "eye_highlight")

# Mouth (small smile)
c.set(30, 22, "skin_shadow")
c.set(31, 22, "skin_shadow")
c.set(32, 22, "skin_shadow")

# Nose
c.set(31, 20, "skin_shadow")

# === CLOAK HOOD detail ===
c.rect(24, 10, 16, 6, "cloak_dark", fill=True)
c.rect(26, 11, 12, 4, "cloak_mid", fill=True)

# === Staff hand grip ===
c.rect(44, 32, 6, 4, "skin_mid", fill=True)
c.rect(45, 33, 4, 2, "skin_light", fill=True)

# === Add some final details ===
# Cloak collar
c.rect(26, 24, 12, 4, "cloak_dark", fill=True)

# Belt/sash
c.rect(26, 42, 12, 3, "wood_dark", fill=True)
c.rect(28, 43, 8, 1, "wood_light", fill=True)

# Add outline effect for strong silhouette
c.outline("outline")

# Check stats
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

# Submit
finish(c)
