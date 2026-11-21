from pixelbench_api import *

c = new_canvas(64, 64, name="tavern")

# ==================== PALETTE ====================
INK      = c.color((10, 6, 4))          # dark outline
WALL     = c.color((62, 40, 22))        # warm wall
WALL_D   = c.color((44, 28, 15))        # dark wall
WALL_L   = c.color((85, 54, 30))        # light wall
PLANK    = c.color((52, 32, 18))        # plank seam
FLOOR    = c.color((74, 46, 26))        
FLOOR_D  = c.color((50, 30, 17))        
WOOD     = c.color((102, 62, 32))
WOOD_L   = c.color((140, 90, 45))
WOOD_D   = c.color((60, 36, 18))
BARREL   = c.color((112, 66, 32))
BARREL_D = c.color((64, 38, 18))
BARREL_L = c.color((150, 96, 50))
METAL    = c.color((95, 95, 100))
GREEN    = c.color((44, 90, 54))
GREEN_D  = c.color((26, 56, 34))
AMBER    = c.color((115, 76, 42))
AMBER_D  = c.color((68, 44, 24))
RED      = c.color((130, 44, 32))
GLASS    = c.color((185, 215, 210))
GLASS_H  = c.color((240, 255, 250))
LAMP_Y   = c.color((255, 220, 120))      # warm lampshade
LAMP_YL  = c.color((255, 238, 175))      # bright lamp
LAMP_A   = c.color((235, 175, 65))       # amber lamp tone
GLOW     = c.color((170, 125, 75))       # medium glow
GLOW_L   = c.color((210, 155, 90))       # bright glow
SMOKE_A  = c.color((95, 80, 85, 70))     # semi-transparent smoke
SMOKE_B  = c.color((115, 95, 100, 50))   # lighter smoke
SHADOW   = c.color((20, 12, 6))

# ==================== BACKGROUND ====================
c.rect(0, 0, 64, 64, WALL)

# ==================== BACK WALL (rows 0-35) ====================
c.rect(0, 0, 64, 36, WALL)
# plank grain lines
for x in range(6, 64, 10):
    c.line(x, 0, x, 36, PLANK)
# horizontal beam
c.line(0, 13, 63, 13, PLANK)
c.line(0, 14, 63, 14, WALL_D)

# ==================== FLOOR (rows 36-63) ====================
c.rect(0, 36, 64, 28, FLOOR)
# floor planks
for y in [39, 44, 49, 54, 59]:
    c.line(0, y, 63, y, FLOOR_D)
# staggered seams
for row in range(5):
    for x in range(1, 64, 12):
        c.set(x + (row % 2) * 6, 37 + row * 5, FLOOR_D)

# ==================== SHELVES ====================
# Top shelf at y=9
c.rect(0, 9, 64, 2, WOOD)
# Bottom shelf at y=21
c.rect(0, 21, 64, 2, WOOD)
# shelf supports (brackets)
c.rect(2, 11, 2, 11, WOOD_D)
c.rect(30, 11, 2, 11, WOOD_D)
c.rect(58, 11, 2, 11, WOOD_D)

# ==================== BOTTLES ON TOP SHELF ====================
b_top = [
    (5,  GREEN,   4, 8, GREEN_D),
    (13, AMBER_D, 3, 8, SHADOW),
    (20, RED,     3, 8, SHADOW),
    (27, GREEN_D, 4, 9, GREEN),
    (35, AMBER,   3, 8, AMBER_D),
    (43, AMBER_D, 3, 8, SHADOW),
    (50, GREEN,   4, 9, GREEN_D),
    (57, AMBER,   3, 8, AMBER_D),
]
for bx, col, bw, bh, hl in b_top:
    # body
    c.rect(bx, 11, bw, bh, col)
    # neck
    nx = bx + max(0, (bw - 2) // 2)
    c.rect(nx, 8, 2, 3, col)
    # cap
    c.rect(nx, 7, 2, 1, METAL)
    # highlight
    c.rect(bx, 11, 1, bh, hl)

# ==================== BOTTLES ON BOTTOM SHELF ====================
b_bot = [
    (3,  AMBER,   5, 10, AMBER_D),
    (13, AMBER_D, 4, 10, SHADOW),
    (24, GREEN,   5, 10, GREEN_D),
    (34, RED,     4, 10, SHADOW),
    (43, AMBER,   5, 10, AMBER_D),
    (53, GREEN_D, 4, 10, GREEN),
]
for bx, col, bw, bh, hl in b_bot:
    c.rect(bx, 23, bw, bh, col)
    nx = bx + max(0, (bw - 2) // 2)
    c.rect(nx, 20, 2, 3, col)
    c.rect(nx, 19, 2, 1, METAL)
    c.rect(bx, 23, 1, bh, hl)

# Small glass on bottom shelf
c.rect(56, 18, 2, 3, GLASS)
c.rect(58, 18, 2, 2, GLASS)
c.rect(56, 17, 4, 1, GLASS_H)

# ==================== WARM WALL GLOW ====================
# From left lamp
c.rect(15, 6, 16, 18, GLOW)
c.rect(18, 7, 10, 15, GLOW_L)
# From right lamp
c.rect(35, 6, 16, 18, GLOW)
c.rect(38, 7, 10, 15, GLOW_L)
# Additional ambient warm tones
c.rect(13, 8, 4, 16, GLOW_L)
c.rect(47, 8, 4, 16, GLOW_L)
c.rect(20, 6, 8, 4, GLOW_L)
c.rect(40, 6, 8, 4, GLOW_L)

# ==================== HANGING LAMPS ====================
# Wire/cord from ceiling
c.line(22, 0, 22, 5, INK)
c.line(42, 0, 42, 5, INK)

# --- Left pendant lamp ---
# Shade (inverted cone/traperzoid)
c.poly([(16, 4), (28, 4), (25, 9), (19, 9)], LAMP_Y)
c.line(19, 9, 25, 9, LAMP_A)
# shade inner glow
c.rect(20, 6, 4, 3, LAMP_YL)
# visible warm bulb
c.rect(21, 9, 2, 2, LAMP_YL)
# glow below lamp
c.rect(19, 10, 6, 3, GLOW_L)
c.circle(22, 12, 2, GLOW_L, fill=True)

# --- Right pendant lamp ---
c.poly([(36, 4), (48, 4), (45, 9), (39, 9)], LAMP_Y)
c.line(39, 9, 45, 9, LAMP_A)
c.rect(40, 6, 4, 3, LAMP_YL)
c.rect(41, 9, 2, 2, LAMP_YL)
c.rect(39, 10, 6, 3, GLOW_L)
c.circle(42, 12, 2, GLOW_L, fill=True)

# ==================== BAR COUNTER ====================
# Counter top surface (y=29 to y=34)
c.rect(0, 29, 64, 6, WOOD)
# top surface lighter band
c.rect(0, 29, 64, 2, WOOD_L)
# dark outline on top edge
c.line(0, 29, 63, 29, INK)
# wood grain lines on counter
c.line(0, 32, 63, 32, WOOD_D)

# Counter front panel (y=35 to y=46)
c.rect(0, 35, 64, 12, WOOD_D)
# Panel frame
c.line(0, 35, 63, 35, INK)
c.line(0, 46, 63, 46, INK)
# vertical panel separators
for x in [7, 17, 27, 37, 47]:
    c.line(x, 36, x, 45, SHADOW)
# horizontal detail lines
c.line(0, 38, 63, 38, SHADOW)
c.line(0, 42, 63, 42, SHADOW)
# highlight on counter front edge
c.line(0, 35, 63, 35, WOOD)

# ==================== BARRELS (behind counter) ====================
# Barrel 1 - visible on floor between shelves and counter, left
# mostly hidden behind counter, show top visible
c.rect(3, 36, 13, 10, BARREL)
# rounded top
c.ellipse(9, 36, 7, 2, BARREL_L, fill=True)
c.ellipse(9, 36, 4, 1, RUST := c.color((75, 48, 22)), fill=True)
# staves
c.line(5, 37, 5, 45, BARREL_D)
c.line(9, 36, 9, 46, BARREL_D)
c.line(13, 37, 13, 45, BARREL_D)
# outline
c.rect(3, 36, 13, 1, INK)
c.line(3, 36, 3, 45, INK)
c.line(15, 36, 15, 45, INK)

# Barrel 2 - on the floor right, next to counter front area (visible below counter top)
# Partially behind/next to counter, partially visible
c.rect(48, 38, 14, 12, BARREL)
c.ellipse(55, 38, 7, 2, BARREL_L, fill=True)  
c.ellipse(55, 38, 4, 1, BARREL_D, fill=True)
c.ellipse(55, 50, 7, 2, BARREL_D, fill=True)
# staves
c.line(50, 39, 50, 49, BARREL_D)
c.line(55, 38, 55, 50, BARREL_D)
c.line(60, 39, 60, 49, BARREL_D)
c.rect(48, 38, 14, 1, INK)
c.line(48, 38, 48, 49, INK)
c.line(61, 38, 61, 49, INK)

# ==================== GLASSES & DRINKS ON COUNTER ====================
# Wine glasses
for gx in [36, 44]:
    c.rect(gx, 26, 3, 3, GLASS)
    c.rect(gx, 25, 3, 1, GLASS_H)
    # stem
    c.rect(gx + 1, 30, 1, 3, GLASS)
    # base
    c.rect(gx, 33, 3, 1, GLASS)

# Pint glass on counter
c.rect(52, 27, 4, 4, GLASS)
c.rect(52, 26, 4, 1, GLASS_H)
c.rect(53, 28, 2, 2, AMBER)  # amber liquid inside

# ==================== BAR STOOLS ====================
def draw_stool(cx):
    # Seat cushion
    c.rect(cx - 5, 46, 11, 2, WOOD_L)
    c.rect(cx - 5, 48, 11, 2, WOOD)
    # seat outline
    c.line(cx - 6, 46, cx + 6, 46, INK)
    c.line(cx - 6, 46, cx - 6, 49, INK)
    c.line(cx + 6, 46, cx + 6, 49, INK)
    # legs
    c.line(cx - 4, 50, cx - 5, 59, WOOD_D)
    c.line(cx + 4, 50, cx + 5, 59, WOOD_D)
    # strut
    c.line(cx - 3, 57, cx + 3, 57, WOOD_D)
    c.line(cx - 4, 50, cx - 2, 57, WOOD_D)
    c.line(cx + 4, 50, cx + 2, 57, WOOD_D)
    # footrest ring
    c.line(cx - 4, 55, cx + 4, 55, WOOD_D)

draw_stool(10)
draw_stool(28)
draw_stool(56)

# ==================== SMOKE / ATMOSPHERE ====================
# Thin wisps using semi-transparent colors (will show through)
# Upper area haze
for x0, y0, w, h in [(0, 12, 30, 2), (36, 14, 28, 2), (14, 17, 14, 2),
                     (30, 19, 22, 1), (4, 22, 16, 2), (44, 23, 18, 2),
                     (10, 15, 10, 1), (50, 16, 12, 1), (22, 20, 12, 1)]:
    c.rect(x0, y0, w, h, SMOKE_A)
# lighter wisps
c.rect(5, 13, 15, 1, SMOKE_B)
c.rect(40, 15, 10, 1, SMOKE_B)
c.rect(15, 18, 12, 1, SMOKE_B)
c.rect(50, 22, 10, 1, SMOKE_B)

# Framed sign on the wall between lamps
c.rect(25, 1, 14, 7, WOOD_D)
c.rect(26, 2, 12, 5, WALL_L)
# simple text marks on sign
c.rect(28, 3, 8, 1, AMBER)
c.rect(29, 4, 6, 1, AMBER)

# ==================== FLOOR WARM GLOW / SHADOWS ====================
# Light pools under lamps on floor
c.rect(16, 36, 12, 8, GLOW)
c.rect(36, 36, 12, 8, GLOW)
c.rect(19, 37, 8, 6, GLOW_L)
c.rect(39, 37, 8, 6, GLOW_L)
# Floor shadows under stools
c.rect(4, 58, 12, 6, SHADOW)
c.rect(22, 58, 12, 6, SHADOW)
c.rect(50, 58, 12, 6, SHADOW)

# ==================== COUNTER TOP ENHANCEMENTS ============
# Bottle of spirits on counter  
c.rect(8, 25, 4, 6, GLASS)
c.rect(8, 24, 4, 1, GLASS_H)
c.rect(9, 22, 2, 3, GLASS)
c.rect(9, 21, 2, 1, METAL)
# amber liquid in bottle
c.rect(8, 27, 4, 4, AMBER)

# small stack of books/jars on counter
c.rect(2, 27, 4, 3, WOOD_D)
c.rect(3, 28, 3, 2, WOOD)
c.rect(4, 26, 2, 1, RED)

# ==================== ADDITIONAL WARM LIGHTING ====================
# Warm half-light on the counter top from lamps
c.rect(16, 29, 14, 4, GLOW_L)
c.rect(36, 29, 14, 4, GLOW_L)

# Counter top shadow areas (darker at edges)
c.rect(0, 32, 64, 3, WOOD_D)
c.rect(0, 31, 6, 3, SHADOW)
c.rect(58, 31, 6, 3, SHADOW)

# ==================== FINAL POLISH ====================
# Scene is complete

result = c
finish(result)
