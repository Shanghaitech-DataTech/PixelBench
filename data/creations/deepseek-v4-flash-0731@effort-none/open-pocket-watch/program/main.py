from pixelbench_api import *
import math

c = new_canvas(64, 64, background=(0,0,0,0))

# === PALETTE (max 86 colors) ===
BG_NIGHT   = (3, 2, 2)
GOLD_DEEP  = (48, 33, 10)
GOLD_DARK  = (68, 48, 15)
GOLD_MID   = (105, 74, 25)
GOLD       = (146, 104, 38)
GOLD_LIT   = (186, 140, 62)
GOLD_BRT   = (228, 182, 100)
GOLD_HL    = (255, 224, 158)
GOLD_SHD   = (30, 22, 7)

CREAM_DARK = (150, 138, 112)
CREAM      = (196, 184, 158)
CREAM_LT   = (228, 218, 196)
CREAM_HL   = (250, 242, 226)

INK        = (40, 32, 20)
BLUE_HAND  = (36, 50, 82)
BLUE_DARK  = (20, 30, 54)
BLUE_LIGHT = (70, 90, 140)
RED_SEC    = (140, 28, 24)
RED_BRT    = (200, 62, 48)

INT_DB     = (15, 12, 5)       # deep interior shadow
INT_DK     = (26, 20, 9)       # interior shadow
BRASS_DK   = (110, 80, 28)     
BRASS_MD   = (148, 110, 42)
SILVER_DK  = (82, 86, 100)
SILVER_MD  = (140, 144, 160)
SILVER_LT  = (195, 198, 212)
SILVER_HI  = (235, 238, 250)

TOOTH_MD   = (128, 94, 34)
CHAIN_1    = (60, 44, 16)
CHAIN_2    = (100, 72, 26)
CHAIN_3    = (140, 106, 40)
CHAIN_4    = (180, 144, 72)
RUBY_DK    = (68, 10, 30)
RUBY_LT    = (150, 40, 60)

# === BACKGROUND ===
c.rect(0, 0, 64, 64, BG_NIGHT)

# ===== WATCH CHAIN =====
# Chain more prominent at top, drooping down with link structure
chain_pts = [(57,1),(54,3),(51,5),(48,6),(45,7),(42,8),
             (39,9),(36,10),(33,11),(31,13),(30,15)]
# Draw heavier chain links (oval links)
for i,(cx,cy) in enumerate(chain_pts):
    col = [CHAIN_4, CHAIN_2, CHAIN_3, CHAIN_1][i % 4]
    c.ellipse(cx, cy, 2, 1.5, col, fill=True)
# Link separations / borders  
for i,(cx,cy) in enumerate(chain_pts):
    c.ellipse(cx, cy, 2, 1.5, CHAIN_1, fill=False)
# Inner link highlights
for i,(cx,cy) in enumerate(chain_pts):
    if i % 2 == 0:
        c.ellipse(cx, cy, 1, 0.6, CHAIN_4, fill=True)
# Additional link connections
for i in range(len(chain_pts)-1):
    x1, y1 = chain_pts[i]
    x2, y2 = chain_pts[i+1]
    mx, my = (x1+x2)//2, (y1+y2)//2
    c.circle(mx, my, 1, CHAIN_3, fill=True)

# ===== OPEN LID =====
# Lid sits above the watch, swung open showing inner bowl
# This creates the "lid open" look - we see the interior of the lid
L = 30  # lid center x
LY = 8   # lid center y
# Lid outer body - seen from an angle
c.ellipse(L, LY+1, 14, 7, GOLD_DEEP, fill=True)
# Lid metal edge
c.ellipse(L, LY, 13, 6, GOLD_DARK, fill=True)
# Lid interior - dark recess showing exposed movement area through lid
c.ellipse(L, LY, 11, 4, INT_DB, fill=True)
# Gold inner ring (the lid's inner bezel)
c.ellipse(L, LY, 9, 3, GOLD_MID, fill=True)
# Visible machinery in the lid interior
# Small gear visible in the lid
c.circle(L-3, LY, 2, GOLD_DARK, fill=True)
c.circle(L-3, LY, 1, GOLD_LIT, fill=True)
# Another small gear in lid
c.circle(L+3, LY+1, 1.5, GOLD_DARK, fill=True)
c.circle(L+3, LY+1, 0.8, GOLD_LIT, fill=True)
# Lid rim highlight (top, strong light)
c.ellipse(L, LY-1, 12, 4, GOLD_LIT, fill=False)
# Lid top surface catching light
c.ellipse(L-5, LY-3, 5, 1.5, GOLD_BRT, fill=True)
c.ellipse(L-3, LY-3, 3, 1, GOLD_HL, fill=True)

# Hinge between lid and case
c.rect(27, 12, 7, 3, GOLD_DARK, fill=True)
c.rect(28, 12, 5, 1, GOLD_LIT, fill=True)

# Crown
c.rect(29, 14, 5, 4, GOLD_MID, fill=True)
c.rect(30, 13, 3, 3, GOLD_LIT, fill=True)
c.rect(28, 16, 7, 1, GOLD_DEEP, fill=True)

# ===== MAIN WATCH CASE =====
CX, CY = 31, 40
c.circle(CX, CY, 27, GOLD_DEEP, fill=True)
c.circle(CX, CY, 26, GOLD_DARK, fill=True)
c.circle(CX, CY, 25, GOLD_MID, fill=True)
c.circle(CX, CY, 24, GOLD, fill=True)

# Case decoration - engraved rings
c.circle(CX, CY, 23, GOLD_DARK, fill=False)
c.circle(CX, CY, 21.8, GOLD_LIT, fill=False)
# Micro-engraving on the case band (tiny marks for texture)
for a in range(0, 360, 6):
    rad = a * math.pi / 180
    x = int(round(CX + 22.5 * math.cos(rad)))
    y = int(round(CY + 22.5 * math.sin(rad)))
    if a > 100 and a < 300:  # left and bottom sides
        c.set(x, y, GOLD_DEEP)
    elif x < 45 and y < 50:
        c.set(x, y, GOLD_LIT)

# Strong top-left lighting on case edge
for a in range(130, 250, 2):
    rad = a * math.pi / 180
    x = int(round(CX + 23.5 * math.cos(rad)))
    y = int(round(CY + 23.5 * math.sin(rad)))
    if 5 <= x <= 44 and 16 <= y <= 38:
        c.set(x, y, GOLD_BRT)
for a in range(145, 215, 2):
    rad = a * math.pi / 180
    x = int(round(CX + 23.5 * math.cos(rad)))
    y = int(round(CY + 23.5 * math.sin(rad)))
    if x <= 40 and y <= 32:
        c.set(x, y, GOLD_HL)

# Specular sparkle points on case
c.set(11, 35, GOLD_HL)
c.set(15, 27, GOLD_HL)
c.set(20, 20, GOLD_HL)
c.set(44, 22, GOLD_HL)
c.set(13, 32, GOLD_BRT)

# Right side of case falls into shadow (strong contrast)
for a in range(0, 100, 2):
    rad = a * math.pi / 180
    for rr in range(21, 27):
        x = int(round(CX + rr * math.cos(rad)))
        y = int(round(CY + rr * math.sin(rad)))
        if x > 45:
            c.set(x, y, GOLD_DARK)
for a in range(25, 80, 2):
    rad = a * math.pi / 180
    for rr in range(21, 27):
        x = int(round(CX + rr * math.cos(rad)))
        y = int(round(CY + rr * math.sin(rad)))
        if x > 50:
            c.set(x, y, GOLD_DEEP)
# Deepest dark at far right
for a in range(35, 70, 2):
    rad = a * math.pi / 180
    for rr in range(23, 27):
        x = int(round(CX + rr * math.cos(rad)))
        y = int(round(CY + rr * math.sin(rad)))
        if x > 53:
            c.set(x, y, GOLD_SHD)

# Bottom-left subtle bounce light
for a in range(210, 330, 3):
    rad = a * math.pi / 180
    x = int(round(CX + 24 * math.cos(rad)))
    y = int(round(CY + 24 * math.sin(rad)))
    if 8 <= x <= 25 and 55 <= y <= 63:
        c.set(x, y, GOLD_LIT)

# ===== INTERIOR (dark) =====
c.circle(CX, CY, 21, INT_DB, fill=True)
c.circle(CX, CY, 20, INT_DK, fill=True)

# ===== GEAR TRAIN =====
# All gears drawn ON the dark interior. Strong gold on dark.

def draw_gear(cv, cx, cy, R, n_teeth, rot=0.0, is_silver=False):
    """Draw a gear with visible teeth on dark background."""
    if is_silver:
        dark_color  = SILVER_DK
        mid_color   = SILVER_MD
        light_color = SILVER_LT
        hi_color    = SILVER_HI
    else:
        dark_color  = GOLD_DARK
        mid_color   = GOLD_MID
        light_color = GOLD_LIT
        hi_color    = GOLD_HL
    
    # Teeth - draw as small rectangles pointing outward
    for k in range(n_teeth):
        t = k * 2 * math.pi / n_teeth + rot
        tx = int(round(cx + R * math.cos(t)))
        ty = int(round(cy + R * math.sin(t)))
        # Tooth as small circle with highlight
        cv.circle(tx, ty, 1, dark_color, fill=True)
        cv.circle(tx, ty, 0.6, light_color, fill=True)
    # Gear body
    cv.circle(cx, cy, max(1.5, R), dark_color, fill=True)
    cv.circle(cx, cy, max(1, R-1), mid_color, fill=True)
    cv.circle(cx, cy, max(0.5, R-2), light_color, fill=True)
    # Center hole
    cv.circle(cx, cy, 1.3, dark_color, fill=True)
    cv.circle(cx, cy, 0.6, hi_color, fill=True)

# --- Coordinates of machinery (all within interior radius ~15) ---
# Gear 1: large main wheel (left-center, slightly below center)
draw_gear(c, 27, 41, 7, 12, 0.2)
# Large gear spokes (dark slots)
for sp in range(3):
    t = sp * 2 * math.pi / 3 + 0.6
    for rr in range(2, 5):
        sx = int(round(27 + rr * math.cos(t)))
        sy = int(round(41 + rr * math.sin(t)))
        c.set(sx, sy, INT_DB)
# Gear 2: right-upper (meshes with gear 1)
draw_gear(c, 41, 33, 4.5, 8, 0.5)
# Gear 3: right-lower (meshes with gear 2)
draw_gear(c, 37, 48, 4, 7, 1.2)
# Gear 4: silver escapement (lower-left)
draw_gear(c, 18, 50, 3.5, 7, 0.4, is_silver=True)
# Pallet fork arms from escapement
c.line(18, 50, 26, 44, SILVER_LT)
c.line(18, 50, 13, 44, SILVER_LT)
# Gear 5: small above large
draw_gear(c, 28, 27, 3, 5, 0.8)
# Gear 6: small top-center-right
draw_gear(c, 37, 25, 2.5, 5, 0.3)
# Small pinion
draw_gear(c, 35, 36, 2, 4, 1.0)
# Small lower-center gear
draw_gear(c, 24, 53, 2.5, 4, 0.5)
# Tiny far-right
draw_gear(c, 48, 44, 2, 4, 0.7)

# --- Balance spring (visible as partial coil) ---
c.circle(27, 41, 5.5, GOLD_MID, fill=False)
c.circle(27, 41, 4.5, GOLD_LIT, fill=False)
c.circle(27, 41, 3.5, GOLD_MID, fill=False)
# Spring coil shimmer
for i in range(0, 360, 15):
    rad = i * math.pi / 180
    sx = int(round(27 + 5 * math.cos(rad)))
    sy = int(round(41 + 5 * math.sin(rad)))
    if i < 180:
        c.set(sx, sy, GOLD_LIT)
    else:
        c.set(sx, sy, GOLD_DARK)

# --- Jewel bearings (rubies) ---
jewels = [(27,41),(41,33),(37,48),(18,50),(28,27)]
for jx, jy in jewels:
    c.circle(jx, jy, 1, RUBY_DK, fill=True)
    # Ruby highlight
    c.set(jx-1, jy-1, RUBY_LT)

# --- Screws ---
for sx, sy in [(21,31),(46,32),(43,55),(16,54)]:
    c.circle(sx, sy, 0.8, GOLD_DEEP, fill=True)
    c.set(sx, sy, GOLD_LIT)

# ===== DIAL RING =====
# Cream dial ring between case and mechanism
c.circle(CX, CY, 21, CREAM_DARK, fill=True)
c.circle(CX, CY, 20.5, CREAM, fill=True)
c.circle(CX, CY, 16, CREAM_LT, fill=True)
# Inner dial edge (transition to mechanism)
c.circle(CX, CY, 15.5, CREAM_DARK, fill=True)
# Highlight on inner dial edge top
c.circle(CX, CY, 16, CREAM_HL, fill=False)
# Dial subtle texture - faint engraved circles
c.circle(CX, CY, 18, CREAM, fill=False)
c.circle(CX, CY, 19, CREAM_DARK, fill=False)

# ===== DIAL MARKINGS =====
# Hour markers at 12 positions - prominent INK bars (spade markers)
for hr in range(12):
    t = hr * math.pi / 6 - math.pi / 2
    nx = int(round(CX + 18.5 * math.cos(t)))
    ny = int(round(CY + 18.5 * math.sin(t)))
    c.rect(nx-1, ny-1, 3, 3, INK, fill=True)
    # Extended bar at  3, 6, 9, 12
    if hr % 3 == 0:
        nx2 = int(round(CX + 16.8 * math.cos(t)))
        ny2 = int(round(CY + 16.8 * math.sin(t)))
        c.rect(nx2-1, ny2-1, 3, 3, INK, fill=True)
    # Double bar for main hours
    if hr % 3 == 0:
        nx0 = int(round(CX + 19.5 * math.cos(t)))
        ny0 = int(round(CY + 19.5 * math.sin(t)))
        c.rect(nx0-1, ny0-1, 3, 3, INK, fill=True)

# Fine minute ticks
for i in range(60):
    if i % 5 == 0:
        continue
    t = i * 2 * math.pi / 60 - math.pi / 2
    x1 = int(round(CX + 19.5 * math.cos(t)))
    y1 = int(round(CY + 19.5 * math.sin(t)))
    x2 = int(round(CX + 18.5 * math.cos(t)))
    y2 = int(round(CY + 18.5 * math.sin(t)))
    c.line(x1, y1, x2, y2, INK)

# ===== WATCH HANDS =====
# Hour hand - toward 2 o'clock, bolder
c.line(CX, CY, 44, 29, BLUE_DARK)
# Hour hand body (thicker)
c.line(CX, CY, 44, 29, BLUE_HAND)
c.line(CX-1, CY, 43, 29, BLUE_HAND)
c.line(CX, CY+1, 44, 30, BLUE_HAND)
# Hour hand highlight
c.line(CX-1, CY-1, 43, 28, BLUE_LIGHT)
# Minute hand - toward 10 o'clock, longer
c.line(CX, CY, 18, 28, BLUE_DARK)
c.line(CX, CY, 18, 28, BLUE_HAND)
c.line(CX, CY, 19, 29, BLUE_HAND)
c.set(17, 27, BLUE_HAND)
# Second hand - red toward 5 o'clock, hair-thin
c.line(CX, CY, 36, 58, RED_SEC)
c.line(CX+1, CY, 37, 58, RED_BRT)
# Small counterweight
c.line(CX, CY, 27, 35, RED_SEC)

# Center cap
c.circle(CX, CY, 2.5, GOLD_DARK, fill=True)
c.circle(CX, CY, 1.5, GOLD_LIT, fill=True)
c.set(CX-1, CY-1, GOLD_HL)

# ===== GLASS REFLECTION =====
# Curved glass highlight (upper-left quarter)
for a in range(150, 270, 2):
    rad = a * math.pi / 180
    x = int(round(CX + 12 * math.cos(rad)))
    y = int(round(CY + 12 * math.sin(rad)))
    if 15 <= x <= 38 and 27 <= y <= 44:
        c.set(x, y, CREAM_HL)
# Diagonal light streak
for i in range(6):
    c.set(18+i, 33-i, CREAM_HL)
    c.set(16+i, 34-i, CREAM_LT)
    c.set(17+i, 32-i, CREAM_HL)

# ===== AMBIENT DRAMA =====
# Vignette at very edges (not covering the chain at top-right)
c.rect(0, 0, 64, 2, BG_NIGHT)
c.rect(0, 0, 2, 64, BG_NIGHT)
c.rect(62, 0, 2, 64, BG_NIGHT)
# Darken bottom only outside the watch
for y in range(58, 64):
    for x in range(0, 64):
        if (x-31)**2 + (y-40)**2 > 700:
            c.set(x, y, BG_NIGHT)

# ===== BROUGHT TO LIFE =====
# Strong warm gradient wrap on the top-left case arc
for a in range(140, 240, 3):
    rad = a * math.pi / 180
    for rr in range(20, 24):
        x = int(round(CX + rr * math.cos(rad)))
        y = int(round(CY + rr * math.sin(rad)))
        if 5 <= x <= 42 and 17 <= y <= 38:
            if rr < 21:
                c.set(x, y, GOLD_LIT)
            elif rr < 22:
                c.set(x, y, GOLD)
            elif rr < 23:
                c.set(x, y, GOLD_MID)

# ===== FINAL DETAIL =====
# Re-draw dial markings after hands, to keep the ring crisp
for i in range(60):
    t = i * 2 * math.pi / 60 - math.pi / 2
    x1 = int(round(CX + 19.5 * math.cos(t)))
    y1 = int(round(CY + 19.5 * math.sin(t)))
    x2 = int(round(CX + 18.5 * math.cos(t)))
    y2 = int(round(CY + 18.5 * math.sin(t)))
    c.line(x1, y1, x2, y2, INK)
for hr in range(12):
    t = hr * math.pi / 6 - math.pi / 2
    nx = int(round(CX + 18.5 * math.cos(t)))
    ny = int(round(CY + 18.5 * math.sin(t)))
    c.rect(nx-1, ny-1, 3, 3, INK, fill=True)
    if hr % 3 == 0:
        nx2 = int(round(CX + 16.8 * math.cos(t)))
        ny2 = int(round(CY + 16.8 * math.sin(t)))
        c.rect(nx2-1, ny2-1, 3, 3, INK, fill=True)
        nx0 = int(round(CX + 19.5 * math.cos(t)))
        ny0 = int(round(CY + 19.5 * math.sin(t)))
        c.rect(nx0-1, ny0-1, 3, 3, INK, fill=True)

stats = c.stats()
print(stats["colors_used"], "colors used")
# Quick region checks
print(c.matrix_text(region=(5,0,25,15), indices=False))  # lid area
print(c.matrix_text(region=(10,20,50,60), indices=False))  # main body

result = c
finish(result)
