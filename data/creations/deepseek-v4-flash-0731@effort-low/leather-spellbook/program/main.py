from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUTLINE     = (28, 18, 10, 255)
LEATHER_DARK = (46, 28, 16, 255)
LEATHER_MID  = (98, 58, 30, 255)
LEATHER_LIGHT = (144, 90, 46, 255)
GOLD        = (206, 164, 62, 255)
GOLD_DARK   = (150, 112, 42, 255)
RED         = (172, 42, 30, 255)

# ---- book body (rect x6..25, y7..24) ----
c.rect(6, 7, 20, 18, OUTLINE)          # outer dark outline
c.rect(7, 8, 18, 16, OUTLINE)          # inner darker frame margin

# leather cover
c.rect(8, 9, 16, 14, LEATHER_MID)      # main leather (x8..23, y9..22)

# spine along left edge
c.rect(8, 9, 3, 14, LEATHER_DARK)      # spine strip x8..10
c.line(9, 9, 9, 21, LEATHER_LIGHT)     # spine highlight

# top highlight of leather
c.line(11, 9, 23, 9, LEATHER_LIGHT)

# right edge inner shade
c.line(23, 10, 23, 21, LEATHER_DARK)

# ---- metal corner brackets ----
def corner(x, y):
    # horizontal bar and vertical bar
    c.rect(x, y, 3, 2, GOLD)
    c.rect(x, y, 2, 3, GOLD)
    c.rect(x + 1, y + 1, 2, 1, GOLD_DARK)  # inner shading

corner(6, 7)      # top-left
corner(22, 7)     # top-right
corner(6, 21)     # bottom-left
corner(22, 21)    # bottom-right

# ---- vertical leather straps at thirds ----
c.rect(11, 8, 2, 14, LEATHER_DARK)     # left strap x11..12
c.rect(20, 8, 2, 14, LEATHER_DARK)     # right strap x20..21
c.line(12, 9, 12, 20, LEATHER_LIGHT)   # strap sheen

# metal caps on straps
c.rect(11, 8, 2, 2, GOLD)
c.rect(20, 8, 2, 2, GOLD)
c.rect(11, 20, 2, 2, GOLD)
c.rect(20, 20, 2, 2, GOLD)

# ---- center emblem: diamond + gem ----
c.poly([(16, 12), (20, 16), (16, 20), (12, 16)], GOLD)
c.rect(15, 15, 2, 2, RED)              # red gem
c.rect(15, 15, 2, 1, (196, 70, 46, 255)) if False else None  # gem highlight (skipped, keep colors)

# center clasp around gem
c.rect(15, 14, 2, 4, GOLD_DARK) if False else None

# clamp bar across middle of book over emblem arms
c.rect(14, 15, 4, 2, GOLD_DARK)
c.rect(14, 15, 4, 2, GOLD) if False else None
c.rect(15, 15, 2, 2, RED)

# small gold rim lines
c.rect(14, 14, 4, 4, GOLD) if False else None

print(c.stats_text())
finish(c)
