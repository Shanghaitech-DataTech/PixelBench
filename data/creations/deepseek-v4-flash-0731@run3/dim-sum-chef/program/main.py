from pixelbench_api import *

c = new_canvas(32, 32)

W   = c.color("#f8f6f0")   # white (hat, jacket, buns)
WS  = c.color("#c9c4ba")   # white shade
SK  = c.color("#f4c49a")   # skin
SKD = c.color("#d9a878")   # skin shade / neck
BL  = c.color("#eda48f")   # blush
DK  = c.color("#33241a")   # dark (eyes, mouth)
AP  = c.color("#e6cf9f")   # apron
APD = c.color("#d3b57f")   # apron shade
RED = c.color("#c03a2b")   # neckerchief
BA  = c.color("#c89a52")   # bamboo
BA2 = c.color("#9a7230")   # bamboo dark
BA3 = c.color("#e8c98e")   # bamboo light rim
IN  = c.color("#5f4418")   # steamer inside
PA  = c.color("#4a4a52")   # pants
SH  = c.color("#2e2a28")   # shoes

# ---------- Chef hat ----------
c.rect(14, 2, 4, 1, W)
c.rect(12, 3, 8, 1, W)
c.rect(11, 4, 10, 1, W)
c.rect(10, 5, 12, 1, W)
c.rect(10, 6, 12, 1, W)
c.rect(11, 7, 10, 1, W)
c.set(10, 5, WS); c.set(21, 5, WS)
c.set(10, 6, WS); c.set(21, 6, WS)

# ---------- Head ----------
c.rect(11, 8, 10, 1, SK)          # forehead
c.rect(11, 9, 10, 1, SK)
c.set(10, 9, SK); c.set(21, 9, SK) # ears
c.set(13, 9, DK); c.set(14, 9, DK)
c.set(17, 9, DK); c.set(18, 9, DK) # eyes
c.rect(11, 10, 10, 1, SK)
c.set(10, 10, SK); c.set(21, 10, SK)
c.set(12, 10, BL); c.set(19, 10, BL)
c.rect(11, 11, 10, 1, SK)
c.set(14, 11, DK); c.set(17, 11, DK)  # smile corners
c.rect(12, 12, 8, 1, SK)             # chin
c.set(15, 12, DK); c.set(16, 12, DK)  # smile
c.rect(13, 13, 6, 1, SKD)            # neck

# ---------- Jacket ----------
c.rect(9, 14, 14, 1, W)              # shoulders
c.rect(9, 15, 14, 1, W)
c.rect(5, 16, 4, 6, W)               # left arm (x5..8, y16..21)
c.rect(23, 16, 4, 6, W)               # right arm (x23..26, y16..21)
c.rect(9, 16, 14, 8, W)               # torso (x9..22, y16..23)
c.set(8, 17, WS); c.set(23, 17, WS)

# ---------- Apron ----------
c.rect(11, 16, 10, 4, AP)             # bib (x11..20, y16..19)
c.set(12, 17, W); c.set(15, 17, W); c.set(17, 17, W); c.set(19, 17, W)
c.set(14, 18, W); c.set(18, 18, W)
c.set(13, 19, W); c.set(17, 19, W)
c.set(18, 16, APD); c.set(12, 19, APD); c.set(16, 19, APD)

# ---------- Neckerchief ----------
c.rect(14, 15, 4, 1, RED)
c.rect(15, 16, 2, 1, RED)

# ---------- Bamboo steamer ----------
# rim / top ring
c.rect(8, 20, 16, 1, BA3)
c.rect(7, 21, 18, 1, BA)
c.rect(7, 22, 18, 1, BA)
c.rect(7, 23, 18, 1, BA)
# dark opening
c.rect(9, 21, 14, 1, IN)
c.rect(10, 22, 12, 1, IN)
c.rect(10, 23, 12, 1, IN)
# buns
c.rect(11, 21, 3, 1, W)
c.rect(15, 21, 3, 1, W)
c.rect(19, 21, 3, 1, W)
c.rect(10, 22, 4, 1, W)
c.rect(15, 22, 4, 1, W)
c.rect(20, 22, 3, 1, W)
c.rect(11, 23, 3, 1, W)
c.rect(15, 23, 3, 1, W)
c.rect(19, 23, 3, 1, W)
c.set(12, 23, WS); c.set(16, 23, WS); c.set(20, 23, WS)
# wall
c.rect(7, 24, 18, 1, BA)
c.rect(8, 25, 16, 1, BA)
c.rect(8, 26, 16, 1, BA2)
c.rect(9, 27, 14, 1, BA2)
c.set(11, 25, BA2); c.set(15, 25, BA2); c.set(19, 25, BA2)
c.set(11, 26, BA2); c.set(15, 26, BA2); c.set(19, 26, BA2)

# ---------- Hands over steamer ----------
c.rect(4, 22, 4, 4, SK)               # left hand (x4..7, y22..25)
c.rect(24, 22, 4, 4, SK)              # right hand (x24..27, y22..25)

# ---------- Legs ----------
c.rect(11, 28, 4, 2, PA)
c.rect(17, 28, 4, 2, PA)
c.rect(10, 30, 5, 2, SH)
c.rect(17, 30, 5, 2, SH)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 13)))
print(c.matrix_text(region=(0, 20, 27, 27), indices=True))

finish(c)
