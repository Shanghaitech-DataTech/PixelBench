from pixelbench_api import *

c = new_canvas(128, 128, background="#101018", name="standoff")

# --- background: dramatic sky ---
c.rect(0, 0, 128, 128, "#101018")
# moon
c.circle(96, 22, 9, "#e8e4d8")
c.circle(93, 20, 3, "#c9c4b4")
# sky bands
c.rect(0, 34, 128, 18, "#181828")
c.rect(0, 52, 128, 14, "#20202f")
# distant silhouettes (towers)
c.rect(8, 30, 6, 30, "#0a0a12")
c.rect(30, 22, 5, 38, "#0a0a12")
c.rect(70, 26, 5, 34, "#0a0a12")
c.rect(112, 32, 6, 28, "#0a0a12")
# ground
c.rect(0, 86, 128, 42, "#2a2230")
c.rect(0, 86, 128, 2, "#3a3040")
# ground texture
for x in range(0, 128, 9):
    c.set(x, 92 + (x % 3) * 4, "#221a28")
    c.set(x + 4, 100 + (x % 5) * 3, "#221a28")

# --- RED KNIGHT (left), facing right ---
K_ARMOR = "#c03028"; K_DARK = "#7a1a14"; K_LITE = "#e85848"
K_TRIM = "#f0c060"; K_VISOR = "#181018"

# legs
c.rect(28, 74, 6, 14, K_DARK)      # back leg
c.rect(36, 74, 7, 14, K_ARMOR)     # front leg
c.rect(27, 87, 8, 3, "#403030")    # back boot
c.rect(36, 87, 9, 3, "#403030")    # front boot
# torso
c.rect(27, 56, 16, 19, K_ARMOR)
c.rect(27, 56, 16, 3, K_LITE)      # shoulder highlight
c.rect(33, 60, 4, 12, K_TRIM)      # breastplate trim
c.rect(27, 72, 16, 3, K_DARK)      # belt
# cape behind (left side)
c.poly([(26, 54), (14, 60), (10, 80), (20, 78), (26, 70)], "#8a1410")
c.poly([(25, 56), (17, 62), (14, 76), (21, 74), (25, 68)], "#5a0c0a")
# pauldrons
c.rect(24, 55, 7, 6, K_LITE)
c.rect(39, 55, 7, 6, K_LITE)
# head + helm
c.rect(30, 45, 11, 11, K_ARMOR)
c.rect(30, 45, 11, 3, K_LITE)
c.rect(36, 50, 5, 3, K_VISOR)      # visor slit facing right
c.set(41, 51, "#ff4030")           # glowing eye
# helm plume
c.line(33, 45, 30, 38, "#f0c060")
c.line(34, 45, 31, 38, "#f0c060")
# sword arm raised, pointing right toward rogue
c.rect(45, 58, 6, 4, K_ARMOR)      # upper arm
c.rect(50, 56, 5, 4, K_ARMOR)      # forearm
c.rect(54, 55, 3, 4, "#403030")    # gauntlet
# sword blade angled up-right
c.line(57, 56, 70, 44, "#d8dce8")
c.line(58, 57, 70, 44, "#a8b0c8")
c.line(56, 59, 58, 57, K_TRIM)     # crossguard
# shield on back? skip. Add shield front low
c.rect(44, 66, 4, 10, K_DARK)

# --- GREEN-CLOAKED ROGUE (right), facing left ---
R_CLOAK = "#2e7a3a"; R_DARK = "#1c4f26"; R_LITE = "#4fae5c"
R_SKIN = "#d8a878"; R_LEATH = "#5a3a24"; R_METAL = "#9aa4b4"

# legs (crouched, wide stance)
c.rect(88, 74, 6, 13, R_LEATH)
c.rect(97, 74, 6, 13, R_LEATH)
c.rect(86, 86, 8, 3, "#2a1c12")
c.rect(97, 86, 8, 3, "#2a1c12")
# torso
c.rect(87, 57, 15, 18, R_CLOAK)
c.rect(87, 57, 15, 3, R_LITE)
c.rect(93, 62, 4, 10, R_DARK)      # vest
# cloak flowing right
c.poly([(102, 56), (116, 62), (120, 82), (110, 78), (102, 70)], "#1c4f26")
c.poly([(101, 58), (112, 64), (115, 78), (106, 74), (101, 68)], "#123518")
# hood
c.rect(89, 46, 11, 11, R_CLOAK)
c.rect(89, 46, 11, 2, R_LITE)
# face shadow with eyes facing left
c.rect(89, 50, 7, 5, "#141414")
c.set(91, 52, "#7ae08a")           # glowing eye
c.set(89, 52, "#7ae08a")
# arm extended left with dagger
c.rect(80, 60, 6, 4, R_CLOAK)
c.rect(75, 59, 5, 4, R_CLOAK)
c.rect(72, 58, 3, 4, R_SKIN)       # hand
# dagger pointing left
c.line(72, 59, 62, 55, "#d8dce8")
c.line(72, 60, 62, 55, "#a8b0c8")
c.line(73, 61, 71, 59, R_LEATH)
# second dagger low in right hand
c.rect(101, 62, 4, 4, R_SKIN)
c.line(104, 63, 110, 60, "#d8dce8")

# --- tension sparks in the gap between them ---
c.set(64, 50, "#ffd060")
c.set(70, 58, "#ffb040")
c.set(60, 62, "#ffd060")
c.set(67, 44, "#ffb040")
c.set(63, 40, "#fff0a0")
c.set(71, 38, "#ffd060")

print(c.stats_text())
save("standoff", c)
finish(c)
