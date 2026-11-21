from pixelbench_api import *

T = None
OUT = (26, 26, 28)
BODY_L = (226, 225, 228)
BODY = (188, 187, 192)
BODY_D = (106, 105, 112)
METAL = (168, 168, 176)
METAL_D = (96, 96, 106)
GOLD = (216, 178, 106)
GOLD_H = (240, 212, 150)
GOLD_D = (150, 120, 62)
RED = (222, 58, 52)
RED_D = (150, 30, 28)
STRAP = (58, 58, 70)
STRAP_H = (96, 96, 110)

c = new_canvas(32, 32)

# ---------- body (metal casing) ----------
c.rect(10, 9, 18, 14, BODY)          # x10..27, y9..22
c.rect(11, 9, 16, 2, BODY_L)         # top highlight
c.rect(11, 20, 16, 3, BODY_D)        # bottom shadow
# round the corners of the body
for (cx, cy) in [(10, 9), (27, 9), (10, 22), (27, 22)]:
    c.set(cx, cy, T)
c.rect(10, 9, 2, 14, OUT)            # left edge dark bar
c.rect(11, 10, 1, 12, METAL_D)
c.rect(13, 9, 3, 14, RED)            # red band
c.rect(13, 9, 3, 2, (248, 120, 110))
c.set(15, 15, RED_D); c.set(16, 15, RED_D)

# ---------- USB connector (gold metal) ----------
c.rect(2, 12, 8, 9, GOLD)            # x2..9, y12..20
c.rect(2, 12, 8, 2, GOLD_H)
c.rect(2, 19, 8, 2, GOLD_D)
c.rect(2, 12, 1, 9, GOLD_H)
c.rect(9, 12, 1, 9, GOLD_D)
c.rect(4, 14, 2, 2, (60, 46, 24))
c.rect(4, 17, 2, 2, (60, 46, 24))
c.rect(7, 14, 2, 2, (120, 92, 42))
c.rect(7, 17, 2, 2, (120, 92, 42))
c.rect(10, 11, 1, 11, METAL)
c.rect(2, 12, 8, 9, OUT, fill=False)

# ---------- keychain strap ring ----------
c.ellipse(28, 16, 2, 3, STRAP, fill=True)     # x26..30, y13..19
c.ellipse(28, 16, 1, 2, T, fill=True)
c.ellipse(26, 14, 1, 1, STRAP_H, fill=False)
c.set(27, 14, STRAP_H)
c.set(26, 14, STRAP); c.set(26, 17, STRAP)
c.set(27, 13, OUT); c.set(27, 19, OUT)
c.set(25, 13, OUT); c.set(25, 19, OUT)

# dark outline around body last (perimeter)
c.rect(10, 9, 18, 14, OUT, fill=False)

print(c.stats_text())
finish(c)
