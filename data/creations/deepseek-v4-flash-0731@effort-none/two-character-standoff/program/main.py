from pixelbench_api import *

c = new_canvas(128, 128, name="standoff")

# ===== COLOR PALETTE =====
# Background
SKY = "#16162c"
SKY_MID = "#1c1f3d"
GROUND_D = "#3a2f4e"
GROUND_M = "#483964"
GROUND_L = "#594a7c"

# Knight (red armored knight, left)
K_DARK = "#3d0e0e"
K_RED = "#7a1f1f"
K_REDL = "#b03030"
K_LIGHT = "#e8553f"
K_GOLD = "#d4a017"
K_SKIN = "#e8b98a"
K_BLADE = "#b8c4cc"
K_BLADE_D = "#5a6a72"
K_METAL_D = "#4a4a4a"
K_METAL = "#8a8a8a"
K_PLUME = "#e83333"
K_EYE = "#ffd700"
K_VISOR = "#1a0a0a"

# Rogue (green cloaked rogue, right)
R_CLOAK_D = "#234a1e"
R_CLOAK_M = "#2f6a26"
R_CLOAK_L = "#3d8a30"
R_CLOAK_X = "#4ba63c"
R_GOLD = "#c9a227"
R_SKIN = "#d9a866"
R_SKIN_S = "#b3844d"
R_EYE = "#a8ff6a"
R_BOOT = "#33240f"
R_HAIR = "#4a331e"
R_BLADE = "#9ab0c0"
R_BLADE_D = "#4a5a62"
R_DARK = "#1a2e14"

for col in [SKY, SKY_MID, GROUND_D, GROUND_M, GROUND_L,
            K_DARK, K_RED, K_REDL, K_LIGHT, K_GOLD, K_SKIN, K_BLADE, K_BLADE_D,
            K_METAL_D, K_METAL, K_PLUME, K_EYE, K_VISOR,
            R_CLOAK_D, R_CLOAK_M, R_CLOAK_L, R_CLOAK_X, R_GOLD, R_SKIN, R_SKIN_S,
            R_EYE, R_BOOT, R_HAIR, R_BLADE, R_BLADE_D, R_DARK]:
    c.color(col)

# ===== BACKGROUND =====
# Sky (darker at top)
c.rect(0, 0, 128, 45, SKY, fill=True)
c.rect(0, 45, 128, 50, SKY_MID, fill=True)
# Ground
c.rect(0, 95, 128, 33, GROUND_M, fill=True)
c.rect(0, 116, 128, 12, GROUND_D, fill=True)
c.rect(0, 95, 128, 2, GROUND_L, fill=True)

# ===== Dramatic backdrop: energy moon/sun behind gap =====
c.circle(64, 42, 15, "#3a3a68", fill=True)
c.circle(60, 40, 3, "#48487c", fill=True)
c.circle(69, 47, 2, "#48487c", fill=True)

# ===== Wind streaks =====
c.line(58, 52, 70, 51, "#3c3c6c")
c.line(60, 61, 68, 60, "#32325c")
c.line(56, 72, 72, 71, "#3c3c6c")

# Ground dust
c.circle(60, 95, 2, "#6a5a8a", fill=True)
c.circle(66, 96, 1, "#6a5a8a", fill=True)
c.circle(55, 94, 1, "#6a5a8a", fill=True)

# ============================================================
# KNIGHT - left (x ~ 22-52)
# ============================================================

# --- Legs & boots ---
# Left leg
c.rect(27, 76, 5, 15, K_METAL_D, fill=True)
c.rect(28, 76, 3, 15, K_DARK, fill=True)
# Right leg
c.rect(38, 76, 6, 15, K_METAL_D, fill=True)
c.rect(39, 76, 4, 15, K_DARK, fill=True)
# Boots
c.rect(26, 90, 7, 3, K_DARK, fill=True)
c.rect(37, 90, 7, 3, K_DARK, fill=True)
c.rect(26, 88, 4, 2, K_DARK, fill=True)
c.rect(37, 88, 4, 2, K_DARK, fill=True)

# --- Gold belt ---
c.rect(26, 64, 24, 3, K_GOLD, fill=True)

# --- Hip tassets ---
c.rect(26, 67, 8, 8, K_REDL, fill=True)
c.rect(42, 67, 8, 8, K_REDL, fill=True)

# --- Torso armor ---
c.rect(28, 46, 22, 18, K_RED, fill=True)
# Chest plate (lighter)
c.rect(30, 48, 17, 14, K_REDL, fill=True)
# Chest highlights
c.rect(31, 49, 5, 8, K_LIGHT, fill=True)
c.rect(41, 49, 5, 8, K_LIGHT, fill=True)
# Gold center strip
c.rect(37, 50, 3, 10, K_GOLD, fill=True)

# --- Shoulder pauldrons ---
c.ellipse(49, 47, 5, 7, K_REDL, fill=True)
c.ellipse(49, 47, 3, 4, K_GOLD, fill=True)
c.ellipse(27, 47, 5, 7, K_REDL, fill=True)
c.ellipse(27, 47, 3, 4, K_GOLD, fill=True)

# --- Neck ---
c.rect(36, 40, 4, 5, K_VISOR, fill=True)

# --- Head ---
# Helmet
c.rect(31, 28, 14, 16, K_REDL, fill=True)
# Helmet dome
c.ellipse(38, 29, 8, 9, K_REDL, fill=True)
c.ellipse(35, 27, 3, 5, K_LIGHT, fill=True)
# Face guard / visor (covers lower helmet)
c.rect(32, 38, 12, 5, K_VISOR, fill=True)
# Visor slits with glowing eyes
c.set(33, 39, K_EYE)
c.set(34, 39, K_EYE)
c.set(40, 39, K_EYE)
c.set(41, 39, K_EYE)
# Helmet bottom detail
c.rect(32, 43, 12, 2, K_GOLD, fill=True)

# --- Helmet crest ---
c.rect(36, 27, 4, 3, K_GOLD, fill=True)

# --- Dragon plume (flowing) ---
c.poly([(35, 26), (30, 22), (26, 19), (29, 22), (33, 25)], K_PLUME, fill=True)
c.poly([(38, 26), (43, 21), (46, 16), (43, 20), (40, 25)], K_PLUME, fill=True)
c.poly([(37, 27), (34, 20), (32, 14), (35, 19), (38, 26)], K_PLUME, fill=True)
c.circle(36, 23, 5, K_PLUME, fill=True)
c.circle(34, 18, 2, K_PLUME, fill=True)
c.circle(42, 18, 2, K_PLUME, fill=True)

# --- Sword arm (right side) ---
c.rect(50, 54, 4, 8, K_RED, fill=True)
c.rect(51, 62, 4, 6, K_METAL, fill=True)
# Gauntlet hand
c.rect(51, 68, 4, 3, K_METAL, fill=True)
# Sword handle
c.rect(51, 66, 4, 4, K_DARK, fill=True)
# Sword crossguard
c.rect(49, 72, 9, 2, K_GOLD, fill=True)
# Sword blade - broadsword pointing down, slightly angled
c.poly([(50, 74), (56, 74), (60, 92), (57, 92), (53, 92), (52, 74)], K_BLADE, fill=True)
# Blade edge highlight
c.line(51, 75, 57, 89, K_BLADE)
# Blade valley shadow
c.line(54, 74, 58, 89, K_BLADE_D)
# Blade tip
c.poly([(53, 92), (60, 92), (56, 97)], K_BLADE, fill=True)

# --- Shield arm (left side) ---
c.rect(26, 52, 3, 12, K_RED, fill=True)
# Shield - kite shield
c.poly([(21, 50), (27, 50), (27, 72), (24, 78), (21, 72)], K_RED, fill=True)
c.poly([(22, 52), (26, 52), (26, 70), (24, 75), (22, 70)], K_REDL, fill=True)
# Shield cross
c.rect(24, 54, 2, 16, K_GOLD, fill=True)
c.rect(21, 57, 7, 2, K_GOLD, fill=True)

# ============================================================
# ROGUE - right (x ~ 78-108)
# ============================================================

# --- Legs & boots ---
# Right leg (forward lunge)
c.rect(94, 76, 6, 15, R_CLOAK_D, fill=True)
c.rect(96, 76, 4, 15, R_CLOAK_M, fill=True)
# Left leg (behind)
c.rect(80, 79, 5, 14, R_CLOAK_D, fill=True)
# Boots
c.rect(93, 90, 7, 3, R_BOOT, fill=True)
c.rect(79, 90, 7, 3, R_BOOT, fill=True)

# --- Body / cloak tunic ---
c.rect(79, 48, 23, 34, R_CLOAK_M, fill=True)
# Front cloak layer
c.rect(81, 50, 12, 20, R_CLOAK_L, fill=True)
c.rect(83, 52, 6, 10, R_CLOAK_X, fill=True)

# --- Belt ---
c.rect(80, 66, 22, 3, R_GOLD, fill=True)
c.rect(90, 68, 4, 5, R_GOLD, fill=True)
# Pouch
c.rect(83, 70, 5, 5, R_CLOAK_D, fill=True)

# --- Cape (left side, flowing back) ---
c.poly([(79, 50), (70, 60), (66, 80), (74, 88), (79, 82), (79, 62)], R_CLOAK_D, fill=True)
# Cape (right side trailing)
c.poly([(101, 52), (108, 60), (110, 78), (105, 86), (101, 78)], R_CLOAK_D, fill=True)

# --- Left arm with dagger (extended toward knight) ---
# Upper arm
c.rect(79, 48, 4, 6, R_CLOAK_D, fill=True)
# Forearm extended
c.rect(68, 55, 14, 4, R_CLOAK_M, fill=True)
c.rect(70, 54, 8, 6, R_CLOAK_L, fill=True)
# Hand
c.rect(66, 55, 6, 4, R_SKIN, fill=True)
# Dagger handle
c.rect(64, 56, 4, 3, R_DARK, fill=True)
# Dagger guard
c.rect(62, 54, 3, 7, R_GOLD, fill=True)
# Dagger blade pointing left at knight
c.poly([(50, 55), (62, 55), (62, 60), (50, 60)], R_BLADE, fill=True)
c.line(51, 57, 61, 57, R_BLADE_D)
# Dagger tip
c.poly([(46, 56), (50, 55), (50, 60)], R_BLADE, fill=True)

# --- Right arm (at side) ---
c.rect(100, 48, 4, 10, R_CLOAK_D, fill=True)
c.rect(101, 58, 3, 4, R_SKIN, fill=True)

# --- Head ---
# Neck
c.rect(88, 40, 7, 6, R_SKIN, fill=True)
# Chin/face
c.rect(86, 30, 13, 14, R_SKIN, fill=True)
# Hood - rounded top
c.ellipse(92, 29, 10, 9, R_CLOAK_M, fill=True)
c.ellipse(92, 27, 6, 4, R_CLOAK_L, fill=True)
# Hood framing the face
c.poly([(82, 30), (82, 40), (84, 47), (90, 48), (96, 47), (101, 43), (102, 34), (99, 29), (95, 28), (89, 28)], R_CLOAK_D, fill=True)
# Inner hood opening (face revealed)
c.rect(85, 31, 14, 15, R_SKIN, fill=True)
# Hair
c.rect(86, 31, 12, 4, R_HAIR, fill=True)
c.poly([(86, 32), (84, 35), (88, 34)], R_HAIR, fill=True)
c.poly([(98, 32), (100, 35), (95, 34)], R_HAIR, fill=True)
# Eyes - intense green glowing
c.rect(87, 37, 4, 2, R_SKIN_S, fill=True)
c.rect(93, 37, 4, 2, R_SKIN_S, fill=True)
c.set(88, 37, R_EYE)
c.set(89, 38, R_EYE)
c.set(94, 37, R_EYE)
c.set(95, 38, R_EYE)
# Angry eyebrows
c.line(86, 36, 91, 37, R_HAIR)
c.line(93, 37, 98, 36, R_HAIR)
# Scarf/neck wrap
c.rect(84, 46, 16, 4, R_CLOAK_D, fill=True)
c.rect(86, 47, 12, 3, R_CLOAK_M, fill=True)

# ===== Clash energy sparks between them ====
K_EYE_DIM = "#ffc800"
R_EYE_DIM = "#8ae850"

# Spark at center of their gaze
c.set(57, 44, K_EYE)
c.set(56, 46, R_EYE)
c.set(58, 47, K_EYE)
c.set(57, 45, K_GOLD)

# Add subtle rim light on characters from moon
# Knight rim light (gold-ish highlight on right side silhouette)
c.line(49, 45, 49, 55, K_GOLD)
c.line(50, 44, 50, 58, K_LIGHT)
c.line(44, 43, 44, 50, K_LIGHT)
# Rogue rim light (green highlight on left side)
c.line(80, 45, 80, 56, R_CLOAK_X)
c.line(82, 43, 82, 54, R_CLOAK_X)

# More dramatic ground: scattered blades of grass
# Left (around knight)
c.line(15, 94, 13, 90, GROUND_D)
c.line(19, 95, 18, 91, GROUND_D)
c.line(50, 93, 49, 90, GROUND_D)
# Right (around rogue)
c.line(78, 93, 77, 90, GROUND_D)
c.line(110, 94, 108, 90, GROUND_D)

# Spark burst at center where their weapons converge
# Small star/energy effect
c.rect(55, 55, 3, 3, K_EYE, fill=True)
c.set(56, 53, K_EYE)
c.set(56, 59, K_EYE)
c.set(53, 56, K_EYE)
c.set(59, 56, K_EYE)
c.set(54, 54, R_EYE)
c.set(58, 58, R_EYE)
c.set(54, 58, K_GOLD)
c.set(58, 54, K_GOLD)

# Final image ready
print(c.stats_text())
save("standoff", c)
finish(c)
