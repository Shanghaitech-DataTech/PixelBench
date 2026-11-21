from pixelbench_api import *

c = new_canvas(64, 64, name="girl_mage")

def col(spec):
    return c.color(spec)

# ============ PALETTE ============
CLOAK_D   = col((8, 16, 52))     # cloak darkest
CLOAK_M   = col((24, 44, 92))    # cloak main
CLOAK_L   = col((54, 82, 140))   # cloak light fold
CLOAK_HI  = col((88, 118, 178))  # cloak highlight
HAIR_D    = col((30, 18, 12))
HAIR_M    = col((68, 46, 30))
HAIR_L    = col((116, 86, 56))
SKIN      = col((238, 204, 178))
SKIN_S    = col((214, 176, 150))
EYE_W     = col((250, 250, 255))
EYE       = col((46, 34, 96))
EYE_HI    = col((134, 126, 214))
CHEEK     = col((248, 184, 172))
MOUTH     = col((172, 100, 100))
BOOT_W    = col((244, 244, 250))
BOOT_S    = col((198, 198, 210))
WOOD      = col((92, 56, 32))
WOOD_D    = col((66, 38, 22))
WOOD_HI   = col((128, 82, 46))
AMBER_B   = col((255, 216, 44))
AMBER_M   = col((255, 176, 22))
AMBER_D   = col((230, 126, 14))
GLOW      = col((255, 236, 140))
GOLD      = col((206, 176, 64))
GOLD_D    = col((166, 136, 50))
SHIRT     = col((20, 30, 76))
LEG       = col((34, 34, 74))
LEG_HI    = col((56, 56, 108))
OUT       = col((4, 6, 24))       # dark outlines
SHADOW    = col((90, 96, 140))    # ground shadow
SHADOW2   = col((60, 66, 108))    # ground shadow inner

def px(x, y, ci):
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, ci)

# ============ GROUND SHADOW (simple ellipse, 2 tones) ============
for y in range(54, 61):
    for x in range(8, 56):
        dx = (x - 33)/24
        dy = (y - 58)/4
        d2 = dx*dx + dy*dy
        if d2 <= 1:
            px(x, y, SHADOW2 if d2 < 0.45 else SHADOW)

# ============ STAFF & CRYSTAL ============
# --- Crystal glow halo ---
for y in range(1, 27):
    for x in range(40, 63):
        if c.get(x, y) == -1:
            dx = x - 52
            dy = y - 13
            d2 = dx*dx + dy*dy
            if d2 < 100 and (x*5 + y*3) % 7 == 0:
                px(x, y, GLOW)

# --- Crystal (teardrop/almond) ---
for y in range(3, 23):
    for x in range(43, 61):
        dx = x - 52
        dy = y - 13
        # almond crystal centered (52,13)
        half_w = 8 * (1 - (dy*dy)/(10*10))
        if abs(dx) <= half_w:
            depth = abs(dy) + abs(dx)*0.45
            if depth < 4:
                px(x, y, AMBER_B)
            elif depth < 7:
                px(x, y, AMBER_M)
            else:
                px(x, y, AMBER_D)
# crystal sparkle
px(52, 9, col((255, 252, 224)))
px(53, 10, col((255, 252, 224)))
px(51, 11, AMBER_B)

# --- Staff shaft ---
for y in range(21, 61):
    for x in range(49, 54):
        px(x, y, WOOD)
    px(50, y, WOOD_HI)
# staff bottom tip
px(50, 61, WOOD_D)

# --- Wrapped grip bands ---
for y in range(28, 60, 6):
    for x in range(48, 55):
        px(x, y, GOLD_D)

# magic particles
for (mx, my) in [(6, 10), (58, 2), (60, 40), (8, 52), (3, 30)]:
    px(mx, my, GLOW)

# ============ CLOAK: HOOD (behind head) ============
# Hood crown
for y in range(4, 15):
    for x in range(19, 47):
        cx = x - 33
        cy = y - 10
        if (cx/14)**2 + (cy/5.5)**2 <= 1:
            px(x, y, CLOAK_M)
# hood rim (over forehead)
for x in range(19, 47):
    cx = x - 33
    if abs(cx) <= 14 and not (x >= 27 and x <= 39):
        px(x, 14, CLOAK_L)
# hood sides framing face
for y in range(13, 27):
    for x in range(18, 27):
        px(x, y, CLOAK_M)
    for x in range(39, 48):
        px(x, y, CLOAK_M)
# hood side highlights
for y in range(13, 26, 2):
    px(19, y, CLOAK_L)
    px(46, y, CLOAK_L)

# ============ FACE ============
for y in range(14, 26):
    for x in range(27, 40):
        cx = x - 33.5
        cy = y - 20
        if (cx/6.5)**2 + (cy/6.5)**2 <= 1:
            px(x, y, SKIN)
# face left shadow
for y in range(15, 25):
    for x in range(27, 30):
        px(x, y, SKIN_S)
# chin highlight
for x in range(31, 36):
    px(x, 24, SKIN)
# neck/chin shadow
for x in range(30, 38):
    px(x, 25, SKIN_S)

# ============ HAIR ============
# hair top & bangs
for y in range(5, 15):
    for x in range(26, 41):
        cx = x - 33.5
        cy = y - 11
        if abs(cx)*0.5 + abs(cy)*0.65 < 5.5:
            px(x, y, HAIR_M)
        elif abs(cx)*0.4 + abs(cy)*0.5 < 6.5:
            px(x, y, HAIR_D)
# hair wisps behind
for y in range(5, 12):
    for x in range(20, 26):
        if abs(x-23)*0.8 + y*0.3 < 4:
            px(x, y, HAIR_D)
for y in range(5, 13):
    for x in range(41, 48):
        if abs(x-44)*0.7 + y*0.3 < 5:
            px(x, y, HAIR_D)
# hair highlight
for x in range(37, 42):
    px(x, 10, HAIR_L)
for x in range(29, 33):
    px(x, 10, HAIR_L)

# side locks falling by face
for y in range(12, 28):
    for x in range(24, 28):
        px(x, y, HAIR_M)
    for x in range(38, 42):
        px(x, y, HAIR_M)

# ============ FACE FEATURES (on top) ============
# Left eye
for y in range(17, 21):
    for x in range(28, 32):
        px(x, y, EYE_W)
for y in range(18, 20):
    for x in range(29, 31):
        px(x, y, EYE)
px(29, 18, EYE_HI)
# Right eye
for y in range(17, 21):
    for x in range(34, 38):
        px(x, y, EYE_W)
for y in range(18, 20):
    for x in range(35, 37):
        px(x, y, EYE)
px(35, 18, EYE_HI)
# upper lashes
for x in range(27, 32):
    px(x, 16, HAIR_D)
for x in range(34, 39):
    px(x, 16, HAIR_D)
# brows
for x in range(27, 31):
    px(x, 14, HAIR_M)
for x in range(35, 39):
    px(x, 14, HAIR_M)
# blush
px(27, 22, CHEEK); px(28, 22, CHEEK)
px(37, 22, CHEEK); px(38, 22, CHEEK)
# mouth (relaxed)
px(31, 23, MOUTH); px(32, 23, MOUTH); px(33, 23, MOUTH)
px(32, 24, MOUTH)

# ============ CLOAK: BODY ============
# shoulders
for y in range(27, 32):
    for x in range(16, 50):
        cx = x - 33
        w = 18 - (y-27)*0.4
        if abs(cx) <= w:
            px(x, y, CLOAK_M)
# shoulders edge highlight
for x in range(16, 50):
    if abs(x-33) > 15:
        px(x, 27, CLOAK_L)

# main cloak drape
for y in range(31, 50):
    for x in range(14, 52):
        cx = x - 33
        w = 19 - (y-31)*0.18
        if abs(cx) <= w:
            px(x, y, CLOAK_M)

# vertical folds
for y in range(29, 50, 2):
    px(20, y, CLOAK_D)
    px(45, y, CLOAK_D)
# brighter fold highlights
for y in range(29, 50, 3):
    px(17, y, CLOAK_L)
    px(47, y, CLOAK_L)

# cloak base flare
for y in range(50, 58):
    for x in range(12, 54):
        cx = x - 33
        if abs(cx) <= 21:
            px(x, y, CLOAK_M)
# hem scallops
for x in range(12, 54):
    if x % 5 in (0, 1):
        px(x, 58, CLOAK_M)
    if x % 5 in (2, 3):
        px(x, 57, CLOAK_M)
# hem highlight
for x in range(12, 54):
    if x % 5 in (0, 1):
        px(x, 57, CLOAK_L)

# ============ SHIRT / INNER ============
# inner shirt visible at chest (cloak has an open front)
for y in range(29, 38):
    for x in range(28, 39):
        px(x, y, SHIRT)
# shirt collar trim
for x in range(27, 40):
    px(x, 28, CLOAK_L)
# outer cloak edges of the chest opening
for y in range(28, 40):
    px(26, y, CLOAK_M); px(27, y, CLOAK_D)
    px(39, y, CLOAK_M); px(38, y, CLOAK_D)

# ============ BELT ============
for x in range(27, 40):
    px(x, 38, GOLD_D); px(x, 39, GOLD_D)
for x in range(30, 36):
    px(x, 38, GOLD); px(x, 39, GOLD)

# ============ LEGS (tights under cloak) ============
for y in range(40, 50):
    for x in range(23, 31):
        px(x, y, LEG)
    for x in range(34, 42):
        px(x, y, LEG)
# leg highlights
for y in range(40, 50):
    px(24, y, LEG_HI)
    px(35, y, LEG_HI)

# ============ BOOTS ============
# left boot
for y in range(49, 57):
    for x in range(21, 32):
        px(x, y, BOOT_W)
    for x in range(21, 25):
        px(x, y, BOOT_S)
# left toe
for x in range(18, 22):
    px(x, 53, BOOT_W); px(x, 54, BOOT_W)
    px(x, 54, BOOT_S) if x == 18 else None
# right boot
for y in range(49, 57):
    for x in range(34, 45):
        px(x, y, BOOT_W)
    for x in range(40, 44):
        px(x, y, BOOT_S)
# right toe
for x in range(44, 48):
    px(x, 53, BOOT_W); px(x, 54, BOOT_W)
    px(x, 53, BOOT_S) if x == 47 else None
# boot cuffs
for x in range(20, 32):
    px(x, 49, BOOT_S)
for x in range(33, 45):
    px(x, 48, BOOT_S); px(x, 49, BOOT_S)
# soles
for x in range(18, 32):
    px(x, 57, BOOT_S)
for x in range(33, 48):
    px(x, 57, BOOT_S)

# ============ ARMS ============
# left arm hanging at side
for y in range(28, 42):
    for x in range(17, 22):
        px(x, y, CLOAK_M)
# left sleeve cuff
for x in range(17, 23):
    px(x, 41, CLOAK_L)
# left hand
for y in range(42, 46):
    for x in range(18, 24):
        px(x, y, SKIN)
for x in range(18, 20):
    for y in range(42, 46):
        px(x, y, SKIN_S)

# right arm reaching for staff
for y in range(28, 33):
    for x in range(40, 47):
        px(x, y, CLOAK_M)
# elbow
for y in range(32, 37):
    for x in range(44, 49):
        px(x, y, CLOAK_M)
# right hand gripping staff
for y in range(24, 29):
    for x in range(47, 52):
        px(x, y, SKIN)
# fingers over shaft
for x in range(47, 51):
    px(x, 26, SKIN_S)

# ============ CHARACTER OUTLINE (silhouette definition) ============
# Strong simple silhouette: add a darker outline along cloak outer edge
def outline_canvas():
    # Simple pass: for each pixel of cloak, if neighbor left or above is empty, 
    # we could outline. But simpler: just ensure cloak outer boundary reads.
    pass

print(c.stats_text())
print("Colors used:", len(c.palette()))
finish(c)
