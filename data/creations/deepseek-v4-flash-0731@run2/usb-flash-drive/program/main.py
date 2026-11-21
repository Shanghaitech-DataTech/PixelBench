from pixelbench_api import *

c = new_canvas(32, 32)

OUT   = c.color("#17171a", "outline")
HI    = c.color("#eaecf0", "metal_hi")
LIGHT = c.color("#c9ccd2", "metal_light")
MID   = c.color("#a9adb5", "metal_mid")
DARK  = c.color("#878b94", "metal_dark")
DEEP  = c.color("#636873", "metal_deep")
SEAM  = c.color("#4f545d", "seam")
ACC   = c.color("#3f7fd6", "accent")
ACC_D = c.color("#2a5da8", "accent_dark")
STRAP = c.color("#212126", "strap")
SHI   = c.color("#3e3e46", "strap_hi")
LED   = c.color("#ff5a3c", "led")
LEDH  = c.color("#ff9a72", "led_hi")

# ---- metal casing body (rounded 2px corners) ----
c.rect(9, 8, 17, 16, LIGHT)
c.rect(9, 13, 17, 5, MID)
c.rect(9, 18, 17, 3, DARK)
c.rect(9, 21, 17, 3, DEEP)
c.rect(9, 8, 17, 2, HI)
for (x, y) in [(9, 8), (10, 8), (9, 9),
               (25, 8), (24, 8), (25, 9),
               (9, 23), (10, 23), (9, 22),
               (25, 23), (24, 23), (25, 22)]:
    c.set(x, y, None)

# ---- USB connector (left) ----
c.rect(3, 11, 7, 10, MID)
c.rect(3, 11, 7, 2, LIGHT)
c.rect(3, 11, 7, 1, HI)
c.rect(3, 17, 7, 4, DARK)
c.rect(4, 13, 2, 5, SEAM)   # contact openings
c.rect(7, 13, 2, 5, SEAM)
c.rect(9, 11, 1, 10, DARK)  # joint seam

# ---- blue accent stripe ----
c.rect(22, 10, 2, 13, ACC)
c.rect(23, 10, 1, 13, ACC_D)

# ---- LED ----
c.rect(11, 10, 2, 2, LED)
c.set(11, 10, LEDH)

# ---- keychain strap loop (right) ----
c.rect(24, 9, 6, 15, STRAP)
c.rect(26, 12, 2, 9, None)   # hole in loop
c.rect(24, 9, 6, 1, SHI)
c.rect(25, 12, 1, 9, SHI)

# ---- strong dark outline around the whole item ----
c.outline(OUT)

print(c.stats_text())
finish(c)
