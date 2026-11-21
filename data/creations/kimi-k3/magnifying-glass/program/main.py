# 16x16 detective magnifying glass icon
c = new_canvas(16, 16, background=None, name="magnifier")

OUT     = "#23283a"   # dark outline
GOLD    = "#d9a441"   # brass frame
GOLD_D  = "#8a5a1e"   # frame shadow
GOLD_L  = "#f2d57e"   # frame highlight
GLASS   = "#a8dce8"   # lens glass
GLASS_D = "#5fa8bd"   # glass shade
WHITE   = "#ffffff"   # glint
WOOD    = "#7a4a24"   # handle core
WOOD_L  = "#a06a38"   # handle highlight

# --- lens: dark rim, brass ring, glass ---
c.circle(6, 6, 5, OUT)
c.circle(6, 6, 4, GOLD)
c.circle(6, 6, 3, GLASS)

# --- frame shading ---
c.set(6, 2, GOLD_L)   # specular on top of frame
c.set(5, 3, GOLD_L)
c.set(4, 3, GOLD_L)
c.set(3, 4, GOLD_L)
c.set(3, 5, GOLD_L)
c.set(9, 7, GOLD_D)
c.set(9, 8, GOLD_D)
c.set(8, 9, GOLD_D)
c.set(7, 9, GOLD_D)

# --- glass shading + glint ---
c.set(8, 7, GLASS_D)
c.set(8, 8, GLASS_D)
c.set(7, 8, GLASS_D)
c.set(9, 6, GLASS_D)
c.set(4, 4, WHITE)
c.set(5, 4, WHITE)
c.set(4, 5, WHITE)

# --- bridge between lens and handle ---
c.set(10, 9, OUT)
c.set(9, 10, OUT)

# --- handle: solid 3px-wide diagonal band with dark end cap ---
for i in range(5):
    c.rect(10 + i, 10 + i, 2, 2, OUT)
c.set(15, 15, OUT)
for i in range(3):
    c.rect(11 + i, 11 + i, 2, 2, WOOD)
c.set(12, 11, WOOD_L)
c.set(13, 12, WOOD_L)
c.set(14, 13, WOOD_L)

view(c)
finish(c)
