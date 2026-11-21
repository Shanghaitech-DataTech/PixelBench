from pixelbench_api import *

c = new_canvas(64, 64, name="mage")

# palette
CLOAK   = c.color("#2c3d78", "cloak")
CLOAK_D = c.color("#1d2a54", "cloak_dark")
CLOAK_L = c.color("#41589e", "cloak_light")
SKIN    = c.color("#f4d2b0", "skin")
SKIN_D  = c.color("#d9a97f", "skin_shade")
HAIR    = c.color("#f2e3c4", "hair")
HAIR_D  = c.color("#cdb98f", "hair_shade")
EYE     = c.color("#2a2038", "eye")
BLUSH   = c.color("#e8a9a0", "blush")
BOOT    = c.color("#f4f4f8", "boot")
BOOT_D  = c.color("#c9ccd8", "boot_shade")
WOOD    = c.color("#6e4b2e", "wood")
AMBER   = c.color("#ffb23e", "amber")
GLOW    = c.color("#ffdf8e", "glow")
TRIM    = c.color("#e8c766", "trim")

CX = 31  # body center (leave room for staff on right)

# ---- staff (behind body) ----
c.line(46, 12, 46, 57, WOOD)
c.line(47, 13, 47, 56, WOOD)
# orb + glow
c.circle(46, 8, 4, GLOW)
c.circle(46, 8, 3, AMBER)
c.set(45, 7, GLOW); c.set(45, 6, GLOW)

# ---- cloak body: flared robe ----
c.poly([(CX-6, 26), (CX+6, 26), (CX+12, 55), (CX-12, 55)], CLOAK)
# cloak shading (left edge dark, right light)
c.line(CX-6, 26, CX-12, 55, CLOAK_D)
c.line(CX-5, 27, CX-10, 54, CLOAK_D)
c.line(CX+6, 26, CX+12, 55, CLOAK_L)
# hem
c.line(CX-12, 55, CX+12, 55, CLOAK_D)
# centre seam + trim
c.line(CX, 27, CX, 54, CLOAK_D)
c.line(CX-4, 26, CX-4, 40, TRIM)
c.line(CX+4, 26, CX+4, 40, TRIM)

# ---- shoulders / upper cloak ----
c.rect(CX-7, 24, 14, 4, CLOAK)
c.line(CX-7, 24, CX-7, 27, CLOAK_D)
c.line(CX+6, 24, CX+6, 27, CLOAK_L)

# ---- arms ----
# viewer-left arm relaxed down
c.rect(CX-10, 26, 3, 12, CLOAK)
c.set(CX-9, 38, SKIN); c.set(CX-10, 38, SKIN); c.set(CX-9, 39, SKIN_D)
# viewer-right arm reaching to staff
c.rect(CX+7, 26, 3, 9, CLOAK)
c.line(CX+9, 33, CX+12, 33, SKIN)
c.line(CX+9, 34, CX+13, 34, SKIN)
c.set(CX+13, 33, SKIN_D)
c.set(CX+9, 32, SKIN)

# ---- head ----
c.rect(CX-6, 14, 12, 11, SKIN)          # face
c.rect(CX-6, 22, 12, 2, SKIN_D)         # jaw shade
# hair: fringe and long side locks
c.rect(CX-7, 12, 14, 4, HAIR)
c.line(CX-7, 16, CX-7, 15, HAIR)
c.line(CX+6, 16, CX+6, 15, HAIR)
# fringe zigzag
for i, x in enumerate(range(CX-6, CX+6, 2)):
    c.line(x, 16, x, 15 + (i % 2), HAIR)
# long side hair
c.rect(CX-9, 14, 3, 16, HAIR)
c.line(CX-9, 30, CX-8, 30, HAIR_D)
c.rect(CX+6, 14, 3, 16, HAIR)
c.line(CX+6, 30, CX+7, 30, HAIR_D)
c.line(CX-8, 14, CX-8, 28, HAIR_D)
c.line(CX+7, 14, CX+7, 28, HAIR_D)

# eyes (front-facing, big anime eyes)
c.rect(CX-4, 19, 3, 3, EYE)
c.rect(CX+2, 19, 3, 3, EYE)
c.set(CX-3, 19, "#ffffff"); c.set(CX+3, 19, "#ffffff")
c.set(CX-3, 21, "#ffffff"); c.set(CX+3, 21, "#ffffff")
c.set(CX-5, 20, BLUSH); c.set(CX+4, 20, BLUSH)
c.set(CX-5, 21, BLUSH); c.set(CX+4, 21, BLUSH)
# mouth
c.set(CX, 23, SKIN_D)

# ---- hat: dark blue wizard hat ----
c.poly([(CX, 1), (CX-8, 13), (CX+8, 13)], CLOAK)
c.line(CX, 1, CX-8, 13, CLOAK_D)
c.line(CX-8, 13, CX+8, 13, CLOAK_D)
c.line(CX+1, 2, CX+8, 13, CLOAK_L)
# brim
c.ellipse(CX, 14, 11, 3, CLOAK)
c.ellipse(CX, 13, 11, 2, CLOAK)
c.line(CX-11, 14, CX+11, 14, CLOAK_D)
# hat band
c.line(CX-6, 11, CX+6, 11, TRIM)
# hat tip flop
c.line(CX, 1, CX+3, 0, CLOAK)
c.set(CX+4, 0, CLOAK)

# ---- white boots ----
c.rect(CX-9, 55, 6, 4, BOOT)
c.rect(CX+3, 55, 6, 4, BOOT)
c.line(CX-9, 58, CX-4, 58, BOOT_D)
c.line(CX+3, 58, CX+8, 58, BOOT_D)
c.set(CX-9, 55, CLOAK_D); c.set(CX+8, 55, CLOAK_D)
# feet toes
c.set(CX-10, 58, BOOT); c.set(CX+9, 58, BOOT)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 64, 64)))
save("blue-cloak-girl-mage", c)
finish(c)
