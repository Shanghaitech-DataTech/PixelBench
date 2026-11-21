from pixelbench_api import *

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="skeleton_grunt")

# Define color palette
# Bone colors
bone_light = c.color("#f5f0e8", "bone_light")      # Highlight bones
bone_mid = c.color("#e8e0d0", "bone_mid")          # Main bone color
bone_shadow = c.color("#c8c0b0", "bone_shadow")    # Shadow on bones
bone_dark = c.color("#a09080", "bone_dark")        # Deep shadows/joints

# Joint/dark shading colors
joint_dark = c.color("#6b5d52", "joint_dark")      # Dark joints
joint_shadow = c.color("#4a3f36", "joint_shadow")  # Deepest joint shadows

# Shield colors (wooden)
wood_light = c.color("#c4a574", "wood_light")      # Wood highlight
wood_mid = c.color("#a08050", "wood_mid")          # Main wood
wood_dark = c.color("#705530", "wood_dark")        # Wood shadow
wood_edge = c.color("#504025", "wood_edge")        # Wood edge

# Sword colors (steel)
steel_light = c.color("#d0d8e0", "steel_light")    # Steel highlight
steel_mid = c.color("#90a0b0", "steel_mid")        # Main steel
steel_dark = c.color("#506070", "steel_dark")      # Steel shadow
steel_edge = c.color("#303840", "steel_edge")      # Steel edge

# Outline color
outline = c.color("#2a2018", "outline")            # Dark outline

# Build the skeleton grunt from bottom to top

# === FEET/BOOTS ===
# Left foot (x: 10-13, y: 27-29)
c.rect(10, 27, 4, 3, bone_mid)
c.set(10, 29, bone_dark)
c.set(13, 29, bone_dark)

# Right foot (x: 17-20, y: 27-29)
c.rect(17, 27, 4, 3, bone_mid)
c.set(17, 29, bone_dark)
c.set(20, 29, bone_dark)

# === LEGS ===
# Left leg (x: 11-13, y: 20-26) - slightly bent
c.rect(11, 20, 3, 7, bone_mid)
c.set(11, 20, joint_dark)  # Knee joint
c.set(11, 23, bone_shadow)
c.set(13, 23, bone_shadow)

# Right leg (x: 17-19, y: 19-26) - slightly bent forward
c.rect(17, 19, 3, 8, bone_mid)
c.set(17, 19, joint_dark)  # Knee joint
c.set(17, 22, bone_shadow)
c.set(19, 22, bone_shadow)

# === PELVIS/HIPS ===
# Pelvis area (x: 12-18, y: 17-19)
c.rect(12, 17, 7, 3, bone_mid)
c.set(12, 17, joint_dark)  # Hip joint left
c.set(18, 17, joint_dark)  # Hip joint right
c.set(14, 18, bone_shadow)
c.set(16, 18, bone_shadow)

# === SPINE/TORSO ===
# Lower spine (x: 13-17, y: 13-16)
c.rect(13, 13, 5, 4, bone_mid)
c.set(13, 13, joint_dark)  # Lower spine joint
c.set(15, 14, bone_shadow)
c.set(15, 15, bone_shadow)

# Rib cage (x: 11-19, y: 9-12) - hunched pose, wider at top
c.rect(11, 9, 9, 4, bone_mid)
c.set(11, 9, bone_shadow)
c.set(19, 9, bone_shadow)
# Ribs detail
c.set(12, 10, bone_shadow)
c.set(13, 10, bone_shadow)
c.set(17, 10, bone_shadow)
c.set(18, 10, bone_shadow)
c.set(12, 11, bone_shadow)
c.set(18, 11, bone_shadow)

# === SHOULDER JOINTS ===
# Left shoulder (x: 9-11, y: 8-10)
c.rect(9, 8, 3, 3, bone_mid)
c.set(9, 8, joint_dark)
c.set(10, 9, joint_shadow)

# Right shoulder (x: 19-21, y: 8-10) - holding shield, slightly raised
c.rect(19, 7, 3, 3, bone_mid)
c.set(21, 7, joint_dark)
c.set(20, 8, joint_shadow)

# === SPINE/NECK ===
# Neck vertebrae (x: 14-16, y: 6-8)
c.rect(14, 6, 3, 3, bone_mid)
c.set(14, 6, joint_dark)
c.set(15, 7, bone_shadow)

# === SKULL ===
# Main skull (x: 11-19, y: 1-6)
c.rect(11, 1, 9, 6, bone_mid)
# Skull top rounding
c.set(10, 2, bone_mid)
c.set(20, 2, bone_mid)
c.set(10, 3, bone_mid)
c.set(20, 3, bone_mid)

# Eye sockets (dark hollows)
c.set(13, 3, joint_shadow)
c.set(14, 3, joint_shadow)
c.set(13, 4, joint_shadow)
c.set(17, 3, joint_shadow)
c.set(18, 3, joint_shadow)
c.set(17, 4, joint_shadow)

# Nose cavity
c.set(15, 4, joint_shadow)
c.set(15, 5, joint_shadow)
c.set(16, 5, joint_shadow)

# Jaw/teeth area
c.rect(12, 5, 7, 2, bone_light)
c.set(12, 6, bone_shadow)
c.set(18, 6, bone_shadow)
# Teeth gaps
c.set(13, 6, joint_shadow)
c.set(15, 6, joint_shadow)
c.set(17, 6, joint_shadow)

# Skull shading (hunched, looking down)
c.set(11, 2, bone_shadow)
c.set(19, 2, bone_shadow)
c.set(12, 2, bone_shadow)
c.set(18, 2, bone_shadow)

# === LEFT ARM (holding sword) ===
# Upper arm (x: 6-9, y: 9-13) - angled down for sword
c.set(8, 9, bone_mid)
c.set(7, 10, bone_mid)
c.set(7, 11, bone_mid)
c.set(6, 12, bone_mid)
c.set(6, 13, bone_mid)
c.set(7, 9, joint_dark)  # Shoulder/elbow joint area
c.set(6, 11, bone_shadow)

# Forearm (x: 4-7, y: 13-17)
c.set(5, 13, bone_mid)
c.set(4, 14, bone_mid)
c.set(4, 15, bone_mid)
c.set(3, 16, bone_mid)
c.set(3, 17, bone_mid)
c.set(5, 14, bone_shadow)
c.set(4, 16, bone_shadow)

# Left hand gripping sword (x: 2-4, y: 17-19)
c.set(3, 17, bone_mid)
c.set(2, 18, bone_mid)
c.set(2, 19, bone_mid)
c.set(3, 18, joint_dark)  # Finger joints

# === RIGHT ARM (holding shield) ===
# Upper arm (x: 21-24, y: 9-13) - raised for shield
c.set(22, 9, bone_mid)
c.set(23, 10, bone_mid)
c.set(24, 10, bone_mid)
c.set(24, 11, bone_mid)
c.set(23, 12, bone_mid)
c.set(22, 11, joint_dark)  # Elbow joint
c.set(23, 11, bone_shadow)

# Forearm (x: 23-26, y: 12-16)
c.set(25, 12, bone_mid)
c.set(26, 13, bone_mid)
c.set(26, 14, bone_mid)
c.set(25, 15, bone_mid)
c.set(25, 16, bone_mid)
c.set(25, 13, bone_shadow)
c.set(26, 15, bone_shadow)

# Right hand on shield (x: 25-27, y: 16-18)
c.set(26, 16, bone_mid)
c.set(27, 17, bone_mid)
c.set(27, 18, bone_mid)
c.set(26, 17, joint_dark)

# === SWORD (short sword in left hand) ===
# Sword tip (x: 0-2, y: 17-19)
c.set(0, 18, steel_light)
c.set(1, 17, steel_mid)
c.set(1, 18, steel_mid)
c.set(1, 19, steel_mid)
c.set(2, 18, steel_mid)

# Sword blade (x: 2-5, y: 16-20)
c.rect(2, 16, 4, 5, steel_mid)
c.set(2, 16, steel_light)
c.set(3, 16, steel_light)
c.set(5, 18, steel_dark)
c.set(5, 19, steel_dark)
c.set(4, 20, steel_edge)

# Sword guard/crossguard (x: 1-4, y: 19-20)
c.set(1, 19, steel_edge)
c.set(2, 19, steel_edge)
c.set(3, 19, steel_edge)
c.set(4, 19, steel_edge)
c.set(2, 20, steel_dark)
c.set(3, 20, steel_dark)

# Sword hilt/grip (x: 3-4, y: 20-22)
c.set(3, 20, wood_dark)
c.set(3, 21, wood_dark)
c.set(4, 21, wood_mid)

# Sword pommel (x: 3-4, y: 22-23)
c.set(3, 22, steel_edge)
c.set(4, 22, steel_edge)
c.set(3, 23, steel_dark)

# === SHIELD (small wooden shield in right hand) ===
# Shield shape - small round/oval shield (x: 26-31, y: 12-20)
# Shield outline
c.set(28, 12, wood_edge)
c.set(29, 12, wood_edge)
c.set(27, 13, wood_edge)
c.set(30, 13, wood_edge)

# Shield face
c.rect(27, 13, 5, 6, wood_mid)
c.set(27, 14, wood_light)
c.set(28, 14, wood_light)
c.set(29, 14, wood_light)
c.set(27, 15, wood_mid)
c.set(31, 15, wood_mid)
c.set(27, 16, wood_mid)
c.set(31, 16, wood_mid)
c.set(27, 17, wood_dark)
c.set(28, 17, wood_dark)
c.set(29, 17, wood_dark)
c.set(27, 18, wood_dark)
c.set(31, 18, wood_dark)

# Shield bottom
c.set(28, 19, wood_edge)
c.set(29, 19, wood_edge)
c.set(30, 19, wood_edge)

# Shield boss/center (metal)
c.set(29, 15, steel_mid)
c.set(29, 16, steel_light)
c.set(30, 15, steel_dark)
c.set(30, 16, steel_dark)

# Shield rim detail
c.set(26, 14, wood_edge)
c.set(26, 15, wood_edge)
c.set(26, 16, wood_edge)
c.set(31, 14, wood_edge)
c.set(31, 17, wood_edge)

# === OUTLINE (subtle, on key edges) ===
# Skull outline
c.set(10, 1, outline)
c.set(20, 1, outline)
c.set(10, 4, outline)
c.set(20, 4, outline)
c.set(11, 6, outline)
c.set(19, 6, outline)

# Shoulder outlines
c.set(9, 8, outline)
c.set(21, 7, outline)

# Rib cage outline
c.set(10, 9, outline)
c.set(20, 9, outline)
c.set(10, 12, outline)
c.set(20, 12, outline)

# Pelvis outline
c.set(11, 17, outline)
c.set(19, 17, outline)

# Print stats to check color count
print(c.stats_text())
print(c.matrix_text())

# Submit the result
finish(c)
