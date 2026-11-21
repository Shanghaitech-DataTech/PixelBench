from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="skeleton-grunt")

# === PALETTE ===
BLACK       = c.color("#000000")
WHITE       = c.color("#ffffff")
BONE        = c.color("#e8dcc0")
BONE_LIGHT  = c.color("#f5eed8")
BONE_DARK   = c.color("#c8b896")
BONE_SHADOW = c.color("#8a7a5e")
JOINT_DARK  = c.color("#3a2f1e")
WOOD        = c.color("#8a5a2a")
WOOD_DARK   = c.color("#5a3a18")
WOOD_LIGHT  = c.color("#a87840")
METAL       = c.color("#c8c8c8")
METAL_DARK  = c.color("#888888")
METAL_LIGHT = c.color("#e8e8e8")
EYE_GLOW    = c.color("#ff4444")
GROUND      = c.color((0, 0, 0, 90))

# =============================================================================
# SKELETON GRUNT - 32x32 RPG Enemy
# Hunched skeleton with short sword and small wooden shield
# Dark joint shading between bones
# =============================================================================

# ========== HEAD - SKULL (slightly hunched forward) ==========
# Cranium dome top
c.rect(13, 1, 7, 2, BONE)
c.rect(14, 0, 5, 1, BONE)
c.rect(14, 0, 4, 1, BONE_LIGHT)
# Face area
c.rect(13, 3, 7, 4, BONE)
c.rect(13, 3, 3, 1, BONE_LIGHT)
# Cheekbones
c.set(13, 5, BONE_LIGHT)
c.set(19, 5, BONE_LIGHT)
# Eye sockets
c.rect(14, 4, 2, 2, BLACK)
c.rect(17, 4, 2, 2, BLACK)
# Glowing red eyes
c.set(15, 4, EYE_GLOW)
c.set(18, 4, EYE_GLOW)
# Under-eye shading
c.rect(13, 6, 7, 1, BONE_DARK)
# Nose opening
c.set(16, 6, BLACK)
# Jaw
c.rect(13, 7, 7, 2, BONE_DARK)
# Teeth
c.set(14, 7, WHITE)
c.set(15, 7, WHITE)
c.set(17, 7, WHITE)
c.set(18, 7, WHITE)
# Jaw dark joints
c.set(13, 7, JOINT_DARK)
c.set(19, 7, JOINT_DARK)
# Skull base
c.rect(14, 9, 5, 1, BONE_DARK)

# ========== NECK ==========
c.rect(14, 10, 5, 2, JOINT_DARK)
c.set(15, 10, BONE_DARK)
c.set(16, 10, BONE_DARK)
c.set(17, 10, BONE_DARK)
c.rect(15, 11, 3, 1, BONE_DARK)

# ========== SHOULDERS (broad, hunched) ==========
c.rect(10, 12, 13, 4, BONE)
c.rect(11, 12, 11, 1, BONE_LIGHT)
# Shoulder joints
c.rect(11, 13, 2, 2, JOINT_DARK)
c.rect(20, 13, 2, 2, JOINT_DARK)
# Scapula detail
c.rect(11, 14, 2, 1, BONE_DARK)
c.rect(20, 14, 2, 1, BONE_DARK)

# ========== SPINE ==========
c.rect(15, 14, 2, 7, BONE_DARK)
for vy in [14, 16, 18]:
    c.set(15, vy, JOINT_DARK)
    c.set(16, vy, JOINT_DARK)

# ========== RIB CAGE ==========
# Upper rib band
c.rect(12, 15, 8, 2, BONE)
c.rect(12, 15, 2, 1, BONE_LIGHT)
# Mid rib band
c.rect(12, 18, 8, 2, BONE)
c.rect(12, 18, 2, 1, BONE_LIGHT)
# Lower rib band
c.rect(13, 21, 6, 2, BONE)
c.rect(13, 21, 2, 1, BONE_LIGHT)
# Rib ends curl under
c.rect(12, 17, 1, 3, BONE_SHADOW)
c.rect(19, 17, 1, 3, BONE_SHADOW)
# Sternum
c.set(15, 16, BONE_LIGHT)
c.set(16, 16, BONE_LIGHT)
c.set(15, 19, BONE_LIGHT)
c.set(16, 19, BONE_LIGHT)
c.set(15, 22, BONE_LIGHT)
c.set(16, 22, BONE_LIGHT)
# Fill gaps
c.set(14, 15, BONE)
c.set(17, 15, BONE)
c.set(14, 18, BONE)
c.set(17, 18, BONE)
c.set(14, 19, BONE)
c.set(17, 19, BONE)

# ========== PELVIS ==========
c.rect(11, 23, 10, 3, BONE)
c.rect(11, 23, 10, 1, BONE_LIGHT)
c.set(11, 24, BONE_DARK)
c.set(20, 24, BONE_DARK)
c.rect(11, 25, 10, 1, BONE_SHADOW)
c.set(12, 24, JOINT_DARK)
c.set(19, 24, JOINT_DARK)
c.set(13, 24, BONE_SHADOW)
c.set(18, 24, BONE_SHADOW)

# ========== LEGS ==========
# LEFT LEG
c.rect(12, 26, 2, 3, BONE)
c.set(12, 26, JOINT_DARK)
c.set(13, 26, JOINT_DARK)
c.set(12, 28, JOINT_DARK)
c.set(13, 28, JOINT_DARK)
c.rect(12, 29, 2, 2, BONE_DARK)
# Left foot
c.rect(11, 30, 4, 2, BONE_SHADOW)
c.set(11, 30, BONE)
c.set(12, 30, BONE)

# RIGHT LEG
c.rect(18, 26, 2, 3, BONE)
c.set(18, 26, JOINT_DARK)
c.set(19, 26, JOINT_DARK)
c.set(18, 28, JOINT_DARK)
c.set(19, 28, JOINT_DARK)
c.rect(18, 29, 2, 2, BONE_DARK)
# Right foot
c.rect(18, 30, 3, 2, BONE_SHADOW)
c.set(18, 30, BONE)
c.set(19, 30, BONE)

# ========== LEFT ARM (shield side) ==========
c.rect(9, 14, 3, 4, BONE)
c.set(9, 14, BONE_DARK)
c.set(9, 15, BONE_DARK)
c.set(9, 17, JOINT_DARK)
c.set(10, 17, JOINT_DARK)
c.set(11, 17, JOINT_DARK)
# Forearm
c.rect(8, 18, 4, 3, BONE)
c.set(8, 18, BONE_DARK)
c.set(8, 19, BONE_DARK)
# Wrist
c.set(8, 20, JOINT_DARK)
c.set(9, 20, JOINT_DARK)
# Hand behind shield
c.set(7, 18, BONE_DARK)
c.set(7, 19, BONE_DARK)

# ========== SHIELD ==========
# Small wooden shield
c.ellipse(5, 21, 3, 4, WOOD)
# Top of shield
c.set(4, 18, WOOD_LIGHT)
c.set(5, 18, WOOD_LIGHT)
c.set(6, 18, WOOD_LIGHT)
# Shield rim shading
c.set(2, 20, WOOD_DARK)
c.set(2, 21, WOOD_DARK)
c.set(2, 22, WOOD_DARK)
c.set(3, 23, WOOD_DARK)
c.set(4, 24, WOOD_DARK)
c.set(5, 24, WOOD_DARK)
c.set(6, 23, WOOD_DARK)
c.set(7, 21, WOOD_DARK)
# Wood grain lines
c.set(3, 20, WOOD_DARK)
c.set(4, 20, WOOD_DARK)
c.set(5, 20, WOOD_DARK)
c.set(3, 21, WOOD_DARK)
c.set(5, 21, WOOD_DARK)
# Wood highlight
c.set(6, 20, WOOD_LIGHT)
# Metal boss
c.circle(4, 21, 1, METAL)
c.set(4, 20, METAL_LIGHT)
c.set(5, 21, METAL_DARK)

# ========== RIGHT ARM (sword side) ==========
c.rect(20, 14, 4, 4, BONE)
c.set(22, 14, BONE_DARK)
c.set(22, 15, BONE_DARK)
c.set(22, 17, JOINT_DARK)
c.set(23, 17, JOINT_DARK)
# Forearm
c.rect(23, 18, 3, 4, BONE)
c.set(24, 18, BONE_DARK)
c.set(24, 19, BONE_DARK)

# ========== SWORD (short sword) ==========
# Crossguard
c.rect(24, 21, 4, 1, METAL_DARK)
# Grip
c.rect(25, 22, 2, 2, BONE)
c.set(25, 22, BONE_DARK)
c.set(25, 23, BONE_DARK)
# Pommel
c.set(25, 24, METAL_DARK)
c.set(26, 24, METAL_DARK)
# Hand on grip
c.set(24, 21, BONE_DARK)
c.set(26, 22, BONE_DARK)
# Blade body (3-wide short sword pointing up)
c.rect(27, 14, 3, 7, METAL)
# Blade edges
c.set(27, 14, METAL_DARK)
c.set(27, 15, METAL_DARK)
c.set(27, 16, METAL_DARK)
c.set(27, 17, METAL_DARK)
c.set(29, 14, METAL_LIGHT)
c.set(29, 15, METAL_LIGHT)
c.set(29, 16, METAL_LIGHT)
c.set(29, 17, METAL_LIGHT)
c.set(29, 18, METAL_LIGHT)
c.set(28, 19, METAL)
c.set(29, 19, METAL_LIGHT)
c.set(28, 20, METAL)
c.set(28, 18, METAL)
# Blade tip
c.set(28, 13, METAL)
c.set(29, 13, METAL_LIGHT)
c.set(29, 12, METAL_LIGHT)

# ========== EXTRA JOINT DARK SHADING ==========
# Additional dark joints at bone connections
c.set(12, 25, JOINT_DARK)
c.set(19, 25, JOINT_DARK)
# Skull-neck boundary
c.rect(14, 10, 5, 1, JOINT_DARK)

# ========== GROUND SHADOW ==========
c.ellipse(16, 30, 7, 1, GROUND)

# ========== FINAL POLISH ==========
# Fix blade bottom connecting to crossguard
c.set(28, 21, METAL_DARK)
# Better separation between right arm and body
c.set(24, 21, BONE_DARK)
c.set(24, 22, BONE_DARK)
# Wrist highlight on sword hand  
c.set(26, 21, BONE)
c.set(27, 21, BONE)

# Key joint highlights for the sword arm knuckles
c.set(25, 21, BONE_DARK)
c.set(26, 21, JOINT_DARK)
c.set(27, 21, BONE)

# Shield grip detail (hand wrapping behind shield edge)
c.set(6, 21, WOOD_DARK)

print(c.stats_text())

# Submit the final drawing
finish(c)
