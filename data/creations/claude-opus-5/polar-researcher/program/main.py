c = new_canvas(48, 48, name="output")

PARKA      = c.color("#c8502a", "parka")
PARKA_D    = c.color("#8f3318", "parka_d")
PARKA_L    = c.color("#e0723f", "parka_l")
FUR        = c.color("#e8dcc8", "fur")
FUR_D      = c.color("#b4a58c", "fur_d")
MASK       = c.color("#39465a", "mask")
MASK_D     = c.color("#242d3b", "mask_d")
GOG_FRAME  = c.color("#1f2733", "gog_frame")
GOG_GLASS  = c.color("#7fb6d9", "goggle")
GOG_HI     = c.color("#dff2ff", "goggle_hi")
PANTS      = c.color("#3a4a63", "pants")
PANTS_D    = c.color("#27334a", "pants_d")
BOOT       = c.color("#2a2622", "boot")
BOOT_L     = c.color("#4d453c", "boot_l")
GLOVE      = c.color("#6b4a2e", "glove")
GLOVE_D    = c.color("#48301f", "glove_d")
CASE       = c.color("#9aa4ad", "case")
CASE_D     = c.color("#646e77", "case_d")
CASE_HI    = c.color("#c8d2d9", "case_hi")
LATCH      = c.color("#d9c05a", "latch")
SCARF      = c.color("#3f8f86", "scarf")
SCARF_D    = c.color("#2a635c", "scarf_d")
SNOW       = c.color("#e6f2ff", "snow")

# ---------------- legs (wide stance, trailing back-left) ----------------
c.poly([(16,33),(21,33),(19,43),(14,43)], PANTS_D)   # back leg
c.poly([(22,33),(28,34),(31,42),(25,42)], PANTS)     # front leg
c.poly([(22,33),(26,34),(27,42),(25,42)], PANTS_D)

# boots
c.rect(10, 43, 9, 3, BOOT)
c.rect(10, 43, 9, 1, BOOT_L)
c.rect(24, 42, 9, 3, BOOT)
c.rect(24, 42, 9, 1, BOOT_L)

# ---------------- scarf streaming backward in the wind ----------------
c.poly([(24,19),(18,18),(12,16),(6,17),(8,19),(15,20),(22,22)], SCARF)
c.poly([(22,21),(16,21),(10,23),(5,22),(9,25),(16,24),(22,23)], SCARF_D)
c.set(6, 17, SCARF_D)
c.set(23, 20, SCARF_D)

# ---------------- torso, leaning forward-right ----------------
c.poly([(23,18),(34,19),(36,28),(29,36),(17,36),(14,28),(18,21)], PARKA)
c.poly([(31,19),(34,19),(36,28),(30,36),(27,35)], PARKA_L)    # windward highlight
c.poly([(14,28),(17,36),(26,36),(24,31)], PARKA_D)            # lee shading
c.line(23, 22, 25, 34, PARKA_D)                               # zip seam
c.rect(17, 34, 12, 2, FUR_D)                                  # hem fur
c.line(18, 34, 28, 34, FUR)

# ---------------- back arm, pressed back ----------------
c.poly([(18,21),(14,23),(12,30),(16,31),(19,25)], PARKA_D)
c.rect(11, 30, 5, 4, GLOVE_D)

# ---------------- hood and head ----------------
c.poly([(22,8),(28,4),(35,6),(38,12),(35,20),(27,21),(21,16)], PARKA)
c.poly([(30,5),(35,6),(38,12),(35,20),(32,20)], PARKA_L)
c.ellipse(30, 13, 6, 6, FUR)              # fur ruff
c.ellipse(30, 13, 6, 6, FUR_D, fill=False)
c.ellipse(30, 13, 4, 5, MASK)             # face opening
c.ellipse(30, 16, 3, 2, MASK_D)           # breath mask

# goggles: inset band with pale blue reflections
c.rect(27, 11, 7, 3, GOG_FRAME)
c.set(26, 12, GOG_FRAME)
c.set(34, 12, GOG_FRAME)
c.rect(27, 12, 3, 2, GOG_GLASS)
c.rect(31, 12, 3, 2, GOG_GLASS)
c.line(27, 13, 28, 12, GOG_HI)
c.line(31, 13, 32, 12, GOG_HI)
c.set(33, 12, GOG_HI)
c.set(29, 12, GOG_HI)

# ---------------- front arm + sample case ----------------
c.poly([(33,20),(36,22),(37,31),(33,31),(32,24)], PARKA)
c.poly([(35,22),(36,22),(37,31),(35,31)], PARKA_L)
c.rect(33, 31, 5, 4, GLOVE)
c.line(33, 31, 37, 31, GLOVE_D)

c.rect(33, 35, 13, 9, CASE)
c.line(33, 35, 45, 35, CASE_HI)
c.line(33, 43, 45, 43, CASE_D)
c.line(33, 39, 45, 39, CASE_D)
c.rect(38, 37, 3, 2, LATCH)
c.line(45, 36, 45, 42, CASE_D)
c.line(34, 36, 34, 42, CASE_HI)
# case handle up to the glove
c.line(36, 34, 39, 34, CASE_D)
c.set(39, 35, CASE_D)

# snow dust catching light on hood and shoulders
c.set(29, 7, SNOW)
c.set(32, 6, SNOW)
c.set(35, 8, SNOW)
c.set(33, 20, SNOW)
c.set(20, 21, SNOW)
c.set(36, 24, SNOW)

# ---------------- wind streaks (snow driven right-to-left) ----------------
c.line(1, 9, 8, 9, SNOW)
c.line(3, 26, 10, 26, SNOW)
c.line(0, 38, 6, 38, SNOW)
c.line(39, 16, 46, 16, SNOW)
c.line(40, 29, 47, 29, SNOW)
c.line(20, 46, 27, 46, SNOW)

view(c)
finish(c)
