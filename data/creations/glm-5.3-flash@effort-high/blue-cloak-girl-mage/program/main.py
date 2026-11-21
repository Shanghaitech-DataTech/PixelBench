c = new_canvas(64, 64, name="blue_cloak_girl_mage")

OUT      = "#1b1b2a"
CLOAK    = "#31406e"
CLOAK_D  = "#232e52"
CLOAK_L  = "#45568c"
TRIM     = "#d9a441"
SKIN     = "#f4c99b"
SKIN_D   = "#d69a6e"
HAIR     = "#f2dcab"
HAIR_D   = "#c9a86b"
EYE      = "#f5a623"
BOOT     = "#f2f3f7"
BOOT_D   = "#c3c9d8"
WOOD     = "#8a5a33"
WOOD_D   = "#5f3d22"
ORB1     = "#ffe08a"
ORB2     = "#ffab3d"
HALO     = "#a86a24"

# ---------- ground shadow ----------
c.ellipse(32, 61, 15, 1, OUT)
c.set(32, 62, None)

# ---------- cloak body (flared robe) ----------
for y in range(22, 51):
    t = (y - 22) / 28.0
    hw = 8 + 5 * t
    x0 = int(round(32 - hw)); x1 = int(round(32 + hw))
    c.set(x0, y, OUT); c.set(x1, y, OUT)
    c.rect(x0 + 1, y, x1 - x0 - 1, 1, CLOAK)
# hem shading + gold trim
c.rect(21, 48, 23, 1, CLOAK_D)
c.rect(20, 49, 25, 2, CLOAK_D)
c.rect(22, 46, 21, 1, TRIM)
# collar highlight + clasp
c.rect(27, 23, 11, 1, CLOAK_L)
c.rect(31, 25, 2, 1, TRIM)
# front seam
c.line(32, 27, 32, 45, CLOAK_D)

# ---------- boots ----------
c.rect(21, 50, 9, 11, OUT)
c.rect(34, 50, 9, 11, OUT)
c.rect(22, 51, 7, 9, BOOT)
c.rect(35, 51, 7, 9, BOOT)
c.rect(22, 58, 7, 2, BOOT_D)
c.rect(35, 58, 7, 2, BOOT_D)
c.rect(27, 51, 1, 7, BOOT_D)
c.rect(40, 51, 1, 7, BOOT_D)

# ---------- sleeves ----------
# left sleeve reaching toward the staff
c.poly([(22, 33), (26, 36), (21, 43), (16, 40)], OUT)
c.poly([(22, 34), (25, 36), (20, 42), (17, 40)], CLOAK)
# right sleeve fold hint
c.line(41, 31, 42, 36, CLOAK_D)

# ---------- head ----------
c.ellipse(32, 14, 9, 8, OUT)          # hair silhouette outline
c.ellipse(32, 14, 8, 8, HAIR)         # hair
c.ellipse(32, 16, 7, 7, OUT)          # face outline ring
c.ellipse(32, 16, 6, 6, SKIN)         # face
c.set(26, 21, SKIN)                   # close chin-edge hole
# side locks falling over shoulders
c.rect(23, 12, 3, 16, HAIR)
c.rect(38, 12, 3, 16, HAIR)
c.line(25, 13, 25, 26, HAIR_D)
c.line(38, 13, 38, 26, HAIR_D)
# bangs
c.rect(26, 9, 13, 4, HAIR)
for x in (26, 29, 32, 35, 38):
    c.set(x, 13, HAIR)
for x in (28, 31, 34, 37):
    c.set(x, 12, HAIR_D)
# face details
c.rect(28, 16, 2, 2, EYE)
c.rect(35, 16, 2, 2, EYE)
c.set(32, 19, SKIN_D)                 # mouth
c.set(27, 18, SKIN_D)                 # blush
c.set(37, 18, SKIN_D)

# hair shine
c.rect(29, 9, 4, 1, "#ffffff")
c.set(24, 12, "#ffffff"); c.set(39, 12, "#ffffff")

# ---------- silhouette outline pass ----------
c.outline(OUT)

# ---------- staff + orb ----------
for y in range(15, 59):
    c.set(14, y, OUT)
    c.set(15, y, WOOD)
    c.set(16, y, WOOD_D)
    c.set(17, y, OUT)
c.set(15, 59, OUT); c.set(16, 59, OUT)
c.circle(16, 10, 5, HALO)
c.circle(16, 10, 3, ORB2)
c.circle(16, 10, 1, ORB1)
c.set(10, 7, ORB2); c.set(22, 13, ORB2)   # sparkles
c.set(11, 13, ORB1); c.set(21, 7, ORB1)
c.set(9, 10, ORB1); c.set(23, 10, ORB1)
c.set(13, 4, ORB2); c.set(19, 4, ORB2)

# ---------- hands ----------
# left hand gripping the staff
c.line(14, 37, 16, 37, OUT)
c.rect(14, 38, 3, 2, SKIN)
c.set(16, 39, SKIN_D)
c.line(14, 40, 16, 40, OUT)
c.set(13, 38, OUT); c.set(13, 39, OUT)
# right hand relaxed at the side
c.line(43, 37, 44, 37, OUT)
c.rect(43, 38, 2, 2, SKIN)
c.set(45, 38, OUT); c.set(45, 39, OUT)
c.line(43, 40, 44, 40, OUT)

print(c.stats_text())

save("blue_cloak_girl_mage", c, indexed=True)
finish(c)
