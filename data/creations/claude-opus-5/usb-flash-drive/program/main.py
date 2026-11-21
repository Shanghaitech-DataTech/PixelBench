c = new_canvas(32, 32, name="output")

DARK  = c.color("#15121b", "dark")
INK   = c.color("#2a2734", "ink")
ST_HI = c.color("#eef2f7", "steel_hi")
ST_LT = c.color("#c8d0dc", "steel_lt")
ST_MD = c.color("#9aa4b4", "steel_md")
ST_DK = c.color("#6c7687", "steel_dk")
ST_SH = c.color("#4b5361", "steel_sh")
BLU   = c.color("#3f6fb8", "blue")
BLU_D = c.color("#2a4a80", "blue_dk")
BLU_H = c.color("#86b2e8", "blue_hi")
GLD   = c.color("#f2cb62", "gold")
GLD_D = c.color("#b78f2e", "gold_dk")
LED   = c.color("#6ff0d8", "led")
LTH   = c.color("#8a5a3c", "leather")
LTH_D = c.color("#5d3a26", "leather_dk")

# ---- silhouette -----------------------------------------------------------
c.rect(10, 9, 13, 15, ST_MD)       # metal casing body
c.rect(2, 13, 9, 7, ST_LT)         # USB-A connector shell
c.rect(22, 15, 3, 3, LTH)          # keychain strap tab
for (bx, by) in ((10, 9), (22, 9), (10, 23), (22, 23)):
    c.set(bx, by, None)            # bevelled casing corners
c.outline(DARK)

# ---- casing shading -------------------------------------------------------
c.rect(11, 10, 11, 1, ST_HI)
c.rect(11, 11, 11, 1, ST_LT)
c.rect(11, 21, 11, 1, ST_DK)
c.rect(11, 22, 11, 1, ST_SH)
c.set(11, 10, ST_LT)
c.set(21, 10, ST_LT)

# collar where the connector leaves the casing
c.rect(10, 10, 2, 13, ST_DK)
c.rect(10, 10, 2, 1, ST_MD)
c.set(10, 22, ST_SH)
c.set(11, 22, ST_SH)

# label panel
c.rect(13, 13, 7, 7, BLU)
c.rect(13, 13, 7, 7, INK, fill=False)
c.rect(14, 14, 5, 1, BLU_H)
c.rect(14, 18, 5, 1, BLU_D)
c.rect(15, 16, 3, 1, BLU_H)

# screws + activity LED on the right flank
c.set(20, 13, ST_DK)
c.set(20, 20, ST_DK)
c.set(20, 16, LED)
c.set(20, 17, ST_SH)

# ---- connector shell ------------------------------------------------------
c.rect(3, 14, 8, 1, ST_HI)
c.rect(3, 15, 8, 3, ST_LT)
c.rect(3, 18, 8, 1, ST_DK)
c.rect(3, 15, 7, 3, INK)           # recess
c.rect(4, 16, 5, 2, GLD)           # contacts
c.rect(4, 17, 5, 1, GLD_D)
c.set(5, 16, INK)
c.set(5, 17, INK)
c.set(7, 16, INK)
c.set(7, 17, INK)

# ---- strap stitching -----------------------------------------------------
c.set(22, 17, LTH_D)
c.set(23, 17, LTH_D)
c.set(24, 15, LTH_D)

# ---- keyring --------------------------------------------------------------
c.clear(25, 12, 7, 9)
ring_outer = [(27, 13), (28, 13), (29, 13),
              (26, 14), (30, 14),
              (25, 15), (31, 15),
              (25, 16), (31, 16),
              (25, 17), (31, 17),
              (26, 18), (30, 18),
              (27, 19), (28, 19), (29, 19)]
ring_band = [(27, 14), (28, 14), (29, 14),
             (26, 15), (30, 15),
             (26, 16), (30, 16),
             (26, 17), (30, 17),
             (27, 18), (28, 18), (29, 18)]
for p in ring_outer:
    c.set(p[0], p[1], DARK)
for p in ring_band:
    c.set(p[0], p[1], ST_MD)
c.set(27, 14, ST_HI)
c.set(28, 14, ST_HI)
c.set(26, 15, ST_LT)
c.set(29, 18, ST_SH)
c.set(30, 17, ST_SH)
c.set(30, 16, ST_DK)

# strap reads as leather, lit on top
c.rect(22, 15, 3, 1, LTH)
c.rect(22, 16, 3, 1, LTH_D)
c.rect(22, 17, 3, 1, INK)
c.set(21, 15, LTH)
c.set(21, 16, LTH_D)
c.set(21, 17, INK)

save("usb-flash-drive", c)

view(c)
finish(c)
