from pixelbench_api import *

# ---------------- 32x32 RPG item portrait: USB flash drive ----------------
c = new_canvas(32, 32, background=None, name="usb_flash_drive")

# palette
OUT    = c.color("#1a1a24", name="outline")
MET_L  = c.color("#e7ecf3", name="metal_light")
MET_M  = c.color("#aeb7c4", name="metal_mid")
MET_D  = c.color("#79828f", name="metal_dark")
MET_DD = c.color("#545c6a", name="metal_deep")
SHELL  = c.color("#9aa3b1", name="collar")
GOLD   = c.color("#e8b64a", name="gold")
GOLD_D = c.color("#b8892c", name="gold_dark")
TONGUE = c.color("#f0ead9", name="tongue")
LED    = c.color("#5ad1ff", name="led_blue")
RED_L  = c.color("#ef7d74", name="strap_light")
RED    = c.color("#d9504e", name="strap_red")
RED_D  = c.color("#a23130", name="strap_dark")

# ---- USB connector (top) ----
c.rect(11, 1, 10, 8, OUT)            # dark block x11..20 y1..8
c.rect(12, 2, 8, 6, MET_M)           # shell x12..19 y2..7
c.rect(13, 2, 6, 1, MET_L)           # top bevel
c.rect(12, 2, 1, 6, MET_L)           # left bevel
c.rect(19, 2, 1, 6, MET_D)           # right shade
c.rect(13, 7, 6, 1, MET_D)           # bottom bevel
c.rect(13, 3, 6, 4, TONGUE)          # inner tongue x13..18 y3..6
c.rect(13, 4, 6, 2, GOLD)            # contact band
for x in (15, 17):
    c.set(x, 4, GOLD_D)
    c.set(x, 5, GOLD_D)              # contact separators
c.set(11, 1, None)                   # rounded tip corners
c.set(20, 1, None)

# ---- metal casing body ----
c.rect(9, 8, 14, 16, OUT)            # dark border x9..22 y8..23
c.rect(10, 9, 12, 14, MET_M)         # metal x10..21 y9..22
for x, y in [(10, 9), (21, 9), (10, 22), (21, 22)]:
    c.set(x, y, OUT)                 # chamfered corners
c.rect(11, 9, 10, 1, SHELL)          # collar row under connector
c.rect(11, 10, 1, 12, MET_L)         # left highlight column
c.rect(20, 10, 2, 12, MET_D)         # right shade columns
c.rect(10, 16, 12, 1, MET_DD)        # seam groove across body
c.rect(11, 22, 10, 1, MET_D)         # bottom shade row
c.set(19, 11, LED)                   # activity LED
for x, y in [(12, 11), (13, 12), (14, 13)]:
    c.set(x, y, MET_L)               # diagonal glare
c.set(16, 12, GOLD)                  # engraved rune (diamond)
c.rect(15, 13, 3, 1, GOLD)
c.set(16, 14, GOLD_D)
c.rect(15, 21, 2, 2, OUT)            # strap hole near bottom
c.set(9, 8, None)                    # rounded body corners
c.set(22, 8, None)
c.set(9, 23, None)
c.set(22, 23, None)

# ---- keychain strap loop ----
c.rect(12, 23, 8, 8, OUT)            # dark ring x12..19 y23..30
c.rect(13, 24, 6, 6, RED)            # red strap x13..18 y24..29
c.rect(13, 24, 2, 1, RED_L)          # top highlight
c.set(13, 25, RED_L)                 # left highlight
c.set(13, 26, RED_L)
c.rect(17, 24, 2, 6, RED_D)          # right shade
c.rect(13, 29, 6, 1, RED_D)          # bottom shade
c.rect(15, 26, 2, 2, None)           # punch the loop hole
c.set(12, 30, None)                  # rounded bottom corners
c.set(19, 30, None)

print(c.stats_text())
print(c.matrix_text())
finish(c)
