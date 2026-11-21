from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="usb_thumb")

# Palette
INK     = c.color("#16181c")   # dark outline
STRAP   = c.color("#3c4149")   # keychain strap
STEEL_D = c.color("#616a75")   # dark steel
STEEL   = c.color("#a7aeb8")   # main casing metal
STEEL_X = c.color("#8d95a0")   # cap metal
STEEL_L = c.color("#e5eaf0")   # bright metal / highlight
GOLD    = c.color("#ecc65e")   # USB contacts
GOLD_D  = c.color("#a97e33")
LED     = c.color("#6fe06a")   # status LED
WHITE   = c.color("#ffffff")  # sparkle

# --- casing body (bottom-most) ---
c.rect(8, 11, 16, 14, INK, fill=False)      # x8..23, y11..24 outline
c.rect(9, 12, 14, 12, STEEL)                # fill
c.rect(9, 12, 2, 12, STEEL_L)               # left-edge highlight
c.rect(21, 12, 2, 12, STEEL_D)              # right-edge shade
c.line(14, 15, 19, 15, STEEL_D)             # engraved groove
c.line(9, 20, 22, 20, INK)                  # cap seam
c.rect(10, 21, 12, 3, STEEL_X)              # cap section

# --- lug joining strap ---
c.rect(11, 7, 10, 4, INK, fill=False)       # x11..20, y7..10
c.rect(12, 8, 8, 2, STEEL_D)

# --- keychain strap loop ---
c.rect(13, 2, 6, 7, INK, fill=False)        # x13..18, y2..8
c.rect(14, 3, 4, 5, STRAP)

# --- USB connector (metal tongue) ---
c.rect(11, 25, 10, 5, INK, fill=False)      # x11..20, y25..29
c.rect(12, 26, 8, 3, STEEL_L)               # metal interior
c.rect(13, 26, 6, 1, GOLD)                  # contact strip
c.rect(13, 28, 6, 1, GOLD)                  # contact strip

# --- small details ---
c.set(20, 13, LED)                           # status light
c.set(10, 13, WHITE)                         # shine sparkle

# guarantee a coherent dark outline around the whole item
c.outline(INK)

print(c.stats_text())
finish(c)
