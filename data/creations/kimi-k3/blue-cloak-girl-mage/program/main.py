from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="blue-cloak-girl-mage")

# ---------- palette ----------
OUT   = "#181a33"   # deep navy outline
HAIR_D= "#6e4326"
HAIR  = "#a06a38"
HAIR_L= "#cf9554"
SKIN  = "#ffd9b0"
SKIN_S= "#e9b285"
EYE   = "#3a3f78"
EYE_L = "#8f9be0"
WHITE = "#ffffff"
MOUTH = "#c26b6b"
BLUSH = "#f2a58e"
CLOAK_D = "#161d42"
CLOAK   = "#26346e"
CLOAK_L = "#3d53a4"
DRESS   = "#e9edf7"
DRESS_S = "#c2cbdf"
GOLD    = "#d9a441"
GOLD_L  = "#ffd35c"
AMBER   = "#ffb52e"
AMBER_L = "#ffe08a"
AMBER_C = "#fff6d8"
GLOW    = "#ffb04040"
WOOD    = "#7a4a2a"
WOOD_D  = "#553420"
BOOT    = "#f4f5fa"
BOOT_S  = "#c9ccda"
SOLE    = "#8d90a4"
TIGHTS  = "#2a2f52"
SHADOW  = "#10102840"

# ---- 1. ground shadow + staff glow ----
c.ellipse(33, 61, 16, 2, SHADOW)
c.circle(47, 11, 6, GLOW)

# ---- 2. back hair ----
c.rect(27, 5, 10, 1, HAIR)
c.rect(25, 6, 14, 3, HAIR)
c.rect(24, 9, 16, 2, HAIR)
c.rect(24, 11, 3, 2, HAIR)
c.rect(37, 11, 3, 2, HAIR)

# ---- 3. face ----
c.rect(27, 10, 10, 7, SKIN)
c.rect(28, 17, 8, 1, SKIN)
c.rect(29, 18, 6, 1, SKIN)
c.rect(30, 19, 4, 1, SKIN)

# ---- 4. bangs ----
c.rect(26, 10, 3, 2, HAIR)
c.rect(31, 10, 2, 1, HAIR)
c.rect(34, 10, 3, 2, HAIR)
c.set(27, 12, HAIR); c.set(35, 12, HAIR)

# ---- 5. face features ----
c.line(28, 12, 34, 12, SKIN_S)        # shadow under bangs
c.rect(29, 13, 2, 3, EYE)
c.rect(33, 13, 2, 3, EYE)
c.set(29, 13, WHITE); c.set(33, 13, WHITE)
c.set(30, 15, EYE_L); c.set(34, 15, EYE_L)
c.line(29, 12, 30, 12, HAIR_D)        # brows
c.line(33, 12, 34, 12, HAIR_D)
c.set(32, 16, SKIN_S)                 # nose
c.set(31, 17, MOUTH); c.set(32, 17, MOUTH)
c.set(28, 16, BLUSH); c.set(35, 16, BLUSH)

# ---- 6. legs ----
c.rect(26, 44, 3, 7, TIGHTS)
c.rect(35, 44, 3, 7, TIGHTS)

# ---- 7. boots ----
c.rect(25, 50, 6, 9, OUT)
c.rect(33, 50, 6, 9, OUT)
c.rect(26, 50, 4, 1, BOOT)
c.rect(34, 50, 4, 1, BOOT)
c.rect(26, 51, 4, 6, BOOT)
c.rect(34, 51, 4, 6, BOOT)
c.rect(29, 52, 1, 5, BOOT_S)
c.rect(34, 52, 1, 5, BOOT_S)
c.rect(26, 57, 4, 1, BOOT_S)
c.rect(34, 57, 4, 1, BOOT_S)
c.rect(26, 58, 4, 1, SOLE)
c.rect(34, 58, 4, 1, SOLE)

# ---- 8. cloak ----
cloak = [(25,20),(24,26),(22,34),(20,42),(19,46),
         (23,48),(27,46),(31,48),(35,46),(39,48),(43,46),
         (45,46),(44,42),(42,34),(40,26),(39,20)]
c.poly(cloak, CLOAK)
c.poly(cloak, OUT, fill=False)

# ---- 9. dress opening ----
c.poly([(30,27),(34,27),(36,45),(28,45)], DRESS)
c.line(29, 44, 35, 44, DRESS_S)
c.line(30, 33, 34, 33, GOLD)          # sash
c.set(32, 33, GOLD_L)

# ---- 10. gold trims ----
c.line(30, 27, 28, 44, GOLD)
c.line(34, 27, 36, 44, GOLD)
c.path("M19 45 L23 47 L27 45 L31 47 L35 45 L39 47 L43 45 L45 45", GOLD, fill=False)

# ---- 11. collar + brooch ----
c.rect(27, 19, 10, 2, CLOAK_D)
c.set(26, 20, CLOAK_D); c.set(37, 20, CLOAK_D)
c.set(27, 18, CLOAK_D); c.set(36, 18, CLOAK_D)
c.line(28, 21, 35, 21, OUT)
c.set(31, 22, AMBER_C); c.set(32, 22, AMBER)
c.set(31, 23, GOLD);   c.set(32, 23, GOLD)

# ---- 12. cloak shading ----
c.poly([(40,25),(42,33),(44,45),(41,45),(39,33)], CLOAK_D)
c.line(26, 30, 25, 41, CLOAK_D)
c.line(38, 30, 39, 41, CLOAK_D)
c.line(22, 28, 21, 41, CLOAK_L)

# ---- 13. sleeve ----
sleeve = [(38,24),(43,27),(47,31),(47,37),(43,37),(41,31),(38,28)]
c.poly(sleeve, CLOAK)
c.poly(sleeve, OUT, fill=False)
c.line(44, 33, 47, 33, CLOAK_L)       # cuff

# ---- 14. staff ----
c.line(46, 15, 46, 56, WOOD_D)
c.line(47, 15, 47, 56, WOOD)
c.line(46, 16, 47, 16, GOLD)
c.line(46, 39, 47, 39, GOLD)
c.set(46, 57, GOLD); c.set(47, 57, GOLD)

# ---- 15. hand ----
c.rect(44, 34, 4, 3, SKIN)
c.line(44, 35, 45, 35, SKIN_S)
c.line(44, 37, 47, 37, OUT)
c.set(48, 35, SKIN)

# ---- 16. orb + sparkles ----
c.circle(47, 11, 3, AMBER)
c.circle(47, 11, 2, AMBER_L)
c.set(46, 10, AMBER_C); c.set(47, 9, AMBER_C)
c.set(44, 13, GOLD); c.set(50, 13, GOLD)   # claws
c.set(55, 5, AMBER_L); c.set(54, 6, AMBER_L); c.set(56, 6, AMBER_L); c.set(55, 7, AMBER_L)
c.set(52, 19, AMBER_L)

# ---- 17. front locks + highlights + ahoge ----
c.rect(24, 12, 3, 12, HAIR)
c.rect(37, 12, 3, 12, HAIR)
c.rect(25, 24, 1, 2, HAIR)
c.rect(38, 24, 1, 2, HAIR)
c.line(26, 13, 26, 22, HAIR_D)
c.line(37, 13, 37, 22, HAIR_D)
c.line(28, 6, 31, 6, HAIR_L)
c.set(26, 8, HAIR_L); c.set(27, 7, HAIR_L)
c.set(24, 14, HAIR_L); c.set(39, 14, HAIR_L)
c.set(33, 4, HAIR); c.set(34, 4, HAIR); c.set(34, 3, HAIR)

# ---- 18. face-framing strands + final touches ----
c.line(27, 13, 27, 15, HAIR)
c.line(36, 13, 36, 15, HAIR)
c.set(27, 16, HAIR_D); c.set(36, 16, HAIR_D)
c.set(42, 8, AMBER_L)
c.line(24, 12, 24, 23, OUT)          # lock outlines against cloak
c.line(39, 13, 39, 23, OUT)

print(c.stats_text())

view(c)
finish(c)
