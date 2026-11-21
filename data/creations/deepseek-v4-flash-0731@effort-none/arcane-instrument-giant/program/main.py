from pixelbench_api import *

# 256x256 arcane brass astrolabe-orrery over a stone pedestal in a dark hall

W = H = 256
c = new_canvas(W, H)

# Palette colors
BLACK = c.color((5, 5, 10), "black")
DARK = c.color((12, 10, 18), "dark")
DARKER = c.color((8, 8, 14), "darker")
BG = c.color((16, 14, 24), "bg")
DARKBG = c.color((10, 10, 18), "darkbg")

# Brass tones
BRASS_DARK = c.color((80, 56, 20), "brass_dark")
BRASS_MID = c.color((140, 100, 40), "brass_mid")
BRASS = c.color((190, 145, 65), "brass")
BRASS_LIGHT = c.color((215, 170, 90), "brass_light")
BRASS_HI = c.color((245, 210, 130), "brass_hi")

# Gold accents
GOLD = c.color((225, 185, 90), "gold")
GOLD_LIGHT = c.color((250, 220, 140), "gold_light")
GOLD_DARK = c.color((140, 100, 30), "gold_dark")

# Bronze/green tarnish
BRONZE = c.color((110, 90, 50), "bronze")
PATINA = c.color((40, 70, 40), "patina")

# Crystal sphere colors
CRYSTAL_BLUE = c.color((60, 110, 200), "crystal_blue")
CRYSTAL_CYAN = c.color((60, 190, 210), "crystal_cyan")
CRYSTAL_PURPLE = c.color((130, 70, 200), "crystal_purple")
CRYSTAL_GOLD = c.color((230, 190, 90), "crystal_gold")
CRYSTAL_GREEN = c.color((60, 180, 120), "crystal_green")
CRYSTAL_RED = c.color((200, 60, 80), "crystal_red")

# Rune glow
RUNE = c.color((140, 255, 200), "rune")
RUNE_BLUE = c.color((100, 180, 255), "rune_blue")
RUNE_CYAN = c.color((80, 230, 230), "rune_cyan")
RUNE_GOLD = c.color((255, 220, 120), "rune_gold")

# Core colors
CORE = c.color((255, 240, 180), "core")
CORE_MID = c.color((255, 200, 80), "core_mid")
CORE_DEEP = c.color((255, 160, 40), "core_deep")
CORE_EDGE = c.color((150, 90, 20), "core_edge")

# Shadow colors
SHADOW = c.color((8, 6, 10), "shadow")
STONE = c.color((70, 65, 80), "stone")
STONE_LIGHT = c.color((110, 100, 120), "stone_light")
STONE_DARK = c.color((50, 46, 60), "stone_dark")

# Floor/background gradient handled with shapes

# Fill background
c.rect(0, 0, W, H, BG)

# Dark hall - darker edges, slightly lighter center
# Vignette via concentric rects
c.rect(0, 0, W, H, BG)
c.rect(8, 8, W-16, H-16, DARKBG)
c.rect(16, 16, W-32, H-32, c.color((14, 13, 22), "bg2"))
c.rect(28, 24, W-56, H-48, c.color((18, 16, 28), "bg3"))

# Floor at bottom
c.rect(0, 210, W, 46, c.color((14, 12, 22), "floor"))
# Hall columns hint (subtle vertical darker bars on left/right)
for col_x in [22, 228]:
    c.rect(col_x, 0, 12, H, c.color((11, 10, 18), "col"))

# Stone pedestal
# Base platform
ped_x, ped_y = 128, 205
ped_w = 92
ped_h = 26
c.rect(ped_x - ped_w//2, ped_y, ped_w, ped_h, STONE_DARK)
c.rect(ped_x - ped_w//2 - 8, ped_y + 14, ped_w + 16, 10, STONE_DARK)
c.rect(ped_x - ped_w//2 - 12, ped_y + 22, ped_w + 24, 8, c.color((38, 34, 48), "peddark"))
# Pedestal pillar
pillar_w = 46
c.rect(ped_x - pillar_w//2, 195, pillar_w, 14, STONE)
c.rect(ped_x - pillar_w//2 - 4, 178, pillar_w + 8, 18, STONE_DARK)
# Top platform
c.rect(ped_x - 56, 168, 112, 12, STONE)
c.rect(ped_x - 56, 168, 112, 4, STONE_LIGHT)

# Stone highlights on platform
for gx in range(ped_x - 46, ped_x + 46, 12):
    ci = (gx - (ped_x - 46)) // 12
    shade = STONE_LIGHT if ci % 3 == 0 else STONE
    c.rect(gx, 192, 8, 3, shade)

# ============ MAIN ASTRAL ORRERY ============
# Center of instrument
cx, cy = 128, 108
R_OUTER = 74   # outermost ring radius
R_INNER = 26   # central core

# Draw layered rings from outermost inward

def draw_ring(radius, color, thickness=3, hi_color=None, lo_color=None):
    """Draw an annular ring via circles."""
    hi_color = hi_color or color
    lo_color = lo_color or color
    # Outer edge highlight
    c.circle(cx, cy, radius, lo_color, fill=True)
    c.circle(cx, cy, radius - thickness, color, fill=True)
    if hi_color:
        # thin highlight on outside edge
        pass

# ---- Ring 1: Outermost (largest brass band) ----
r1 = 70
c.circle(cx, cy, r1, BRASS_DARK, fill=True)
c.circle(cx, cy, r1 - 4, BRASS_MID, fill=True)
c.circle(cx, cy, r1 - 8, BRASS_DARK, fill=True)
c.circle(cx, cy, r1 - 10, PATINA, fill=True)
c.circle(cx, cy, r1 - 12, BRASS_DARK, fill=True)
# Bright edge on outer rim
c.circle(cx, cy, r1, BRASS_HI, fill=False)

# ---- Ring 2: Second ring with runes ----
r2 = 56
c.circle(cx, cy, r2, BRASS_MID, fill=True)
c.circle(cx, cy, r2 - 3, BRASS, fill=True)
c.circle(cx, cy, r2 - 6, BRASS_DARK, fill=True)
c.circle(cx, cy, r2 - 7, PATINA, fill=True)

# ---- Ring 3: Third ring ----
r3 = 42
c.circle(cx, cy, r3, BRASS_MID, fill=True)
c.circle(cx, cy, r3 - 2, BRASS_LIGHT, fill=True)
c.circle(cx, cy, r3 - 4, BRASS_DARK, fill=True)
c.circle(cx, cy, r3 - 5, PATINA, fill=True)

# ---- Ring 4: Inner ring ----
r4 = 30
c.circle(cx, cy, r4, BRASS_MID, fill=True)
c.circle(cx, cy, r4 - 2, BRASS, fill=True)

# ---- Shadow/undercut under the instrument ----
# Dark ellipse anchor below
c.ellipse(cx, cy + 78, 48, 8, SHADOW, fill=True)
c.ellipse(cx, cy + 76, 36, 5, c.color((5, 4, 8), "shad2"), fill=True)

# ---- Central core - radiating ----
core_r = 14
# Outer glow rings
c.circle(cx, cy, core_r + 8, CORE_EDGE, fill=True)
c.circle(cx, cy, core_r + 6, CORE_DEEP, fill=True)
c.circle(cx, cy, core_r + 4, CORE_MID, fill=True)
c.circle(cx, cy, core_r, CORE_MID, fill=True)
c.circle(cx, cy, core_r - 3, CORE, fill=True)
c.circle(cx, cy, core_r - 7, c.color((255, 250, 220), "core_white"), fill=True)
c.circle(cx, cy, 4, c.color((255, 255, 245), "core_bright"), fill=True)

# ---- Orbiting crystal spheres ----
def draw_crystal(gx, gy, radius, color, hl_color):
    """Draw a crystal sphere with highlight."""
    # dark rim
    c.circle(gx, gy, radius, color, fill=True)
    # darker side (add a shadow side using a darker shade)
    dark_shade = c.color((20, 20, 30), f"crs_{gx}_{gy}")
    c.circle(gx + 1, gy + 1, radius - 1, dark_shade, fill=True)
    # re-draw main over for the bright side offset
    c.circle(gx, gy, radius, color, fill=True)
    # highlight
    c.circle(gx - radius//3, gy - radius//3, max(1, radius//3), hl_color, fill=True)
    # small bright spot
    if radius > 3:
        c.circle(gx - radius//2, gy - radius//2, 1, c.color((255,255,255), f"spot_{gx}_{gy}"), fill=True)
    # thin outline
    c.circle(gx, gy, radius, c.color((20,20,30), f"crout_{gx}_{gy}"), fill=False)

# Crystal on outer ring - positions
import math
crystal_positions = [
    (cx + 66, cy - 25, 6, CRYSTAL_BLUE, (150, 210, 255), "blue"),
    (cx - 72, cy + 12, 5, CRYSTAL_PURPLE, (180, 140, 255), "purple"),
    (cx + 32, cy - 76, 5, CRYSTAL_GREEN, (130, 240, 180), "green"),
    (cx - 42, cy + 72, 5, CRYSTAL_CYAN, (140, 240, 255), "cyan"),
    (cx + 70, cy + 58, 4, CRYSTAL_RED, (255, 150, 170), "red"),
    (cx - 58, cy - 62, 4, CRYSTAL_GOLD, (255, 230, 160), "gold"),
    (cx + 12, cy + 62, 3, CRYSTAL_PURPLE, (180, 140, 255), "purple2"),
]

for gx, gy, gr, gcol, ghl, gname in crystal_positions:
    draw_crystal(gx, gy, gr, gcol, ghl)

# Mounting arms for spheres (thin metallic lines)
# Arms reaching from ring to sphere positions
arms = [
    (cx + 56, cy - 21, cx + 63, cy - 23),
    (cx - 60, cy + 9, cx - 68, cy + 11),
    (cx + 27, cy - 66, cx + 30, cy - 73),
    (cx - 35, cy + 62, cx - 40, cy + 68),
    (cx + 58, cy + 50, cx + 67, cy + 55),
    (cx - 50, cy - 54, cx - 56, cy - 59),
    (cx + 10, cy + 50, cx + 11, cy + 58),
]
for ax0, ay0, ax1, ay1 in arms:
    c.line(ax0, ay0, ax1, ay1, BRASS_MID)
    c.line(ax0, ay0, ax1, ay1, BRASS_DARK)

# ---- Engraved ring details ----
# Concentric engraved grooves on the bands
for ang_idx in range(0, 360, 30):
    rad = math.radians(ang_idx)
    # tick marks on outer ring
    x0 = cx + math.cos(rad) * (r1 - 3)
    y0 = cy + math.sin(rad) * (r1 - 3)
    x1 = cx + math.cos(rad) * (r1 - 1)
    y1 = cy + math.sin(rad) * (r1 - 1)
    c.line(int(x0), int(y0), int(x1), int(y1), GOLD_DARK)
    # tick on second ring
    x0 = cx + math.cos(rad) * (r2 - 6)
    y0 = cy + math.sin(rad) * (r2 - 6)
    x1 = cx + math.cos(rad) * (r2 - 2)
    y1 = cy + math.sin(rad) * (r2 - 2)
    c.line(int(x0), int(y0), int(x1), int(y1), GOLD_DARK)

# Tick marks at finer intervals
for ang_idx in range(0, 360, 15):
    rad = math.radians(ang_idx)
    x0 = cx + math.cos(rad) * (r1 - 3)
    y0 = cy + math.sin(rad) * (r1 - 3)
    x1 = cx + math.cos(rad) * (r1 - 0)
    y1 = cy + math.sin(rad) * (r1 - 0)
    # Skip those also at 30 interval to avoid doubling
    if ang_idx % 30 != 0:
        c.line(int(x0), int(y0), int(x1), int(y1), BRASS_DARK)
    # inner ring marks
    x0 = cx + math.cos(rad) * (r2 - 6)
    y0 = cy + math.sin(rad) * (r2 - 6)
    x1 = cx + math.cos(rad) * (r2 - 0)
    y1 = cy + math.sin(rad) * (r2 - 0)
    if ang_idx % 30 != 0:
        c.line(int(x0), int(y0), int(x1), int(y1), BRASS_DARK)

# ---- Glowing runes along the rings ----
def draw_rune(gx, gy, color, glyph_type):
    """Draw a small runic glyph."""
    col = color
    if glyph_type == "a":
        # angular rune
        c.line(gx, gy+2, gx, gy-2, col)
        c.line(gx, gy-2, gx+2, gy, col)
        c.line(gx, gy+2, gx-2, gy, col)
    elif glyph_type == "b":
        # diamond
        c.rect(gx-1, gy-1, 3, 3, col)
        c.set(gx, gy, c.color((255,255,255)), )
    elif glyph_type == "c":
        # vertical with crossbar
        c.line(gx, gy-3, gx, gy+3, col)
        c.line(gx-2, gy, gx+2, gy, col)
    elif glyph_type == "d":
        # triangle
        c.line(gx-2, gy+2, gx+2, gy+2, col)
        c.line(gx-2, gy+2, gx, gy-2, col)
        c.line(gx+2, gy+2, gx, gy-2, col)
    elif glyph_type == "e":
        # X marks
        c.line(gx-2, gy-2, gx+2, gy+2, col)
        c.line(gx+2, gy-2, gx-2, gy+2, col)    
    elif glyph_type == "f":
        # arrow
        c.line(gx-2, gy+2, gx+2, gy-2, col)
        c.line(gx-2, gy+2, gx+1, gy+3, col)
        c.line(gx-2, gy+2, gx-3, gy+1, col)

glyph_types = "abcdef"
rune_radius = r2 - 1  # on second ring
rune_colors = [RUNE, RUNE_BLUE, RUNE_CYAN, RUNE, RUNE_GOLD, RUNE_BLUE]
rune_rgbs = [(140, 255, 200), (100, 180, 255), (80, 230, 230), (140, 255, 200), (255, 220, 120), (100, 180, 255)]

# Runes on ring 2
for i in range(24):
    ang = 360.0 * i / 24
    rad = math.radians(ang)
    gx = cx + math.cos(rad) * (r2 - 2)
    gy = cy + math.sin(rad) * (r2 - 2)
    col = rune_colors[i % len(rune_colors)]
    draw_rune(int(gx), int(gy), col, glyph_types[i % 6])
    # faint glow pixel around rune
    rcol = rune_rgbs[i % len(rune_rgbs)]
    for ox in (-1, 1):
        for oy in (-1, 1):
            c.set(int(gx)+ox, int(gy)+oy, c.color((rcol[0]//3, rcol[1]//2, rcol[2]//2), f"rgl_{i}_{ox}_{oy}"))

# Runes on ring 3
for i in range(16):
    ang = 360.0 * i / 16 + 11.25
    rad = math.radians(ang)
    gx = cx + math.cos(rad) * (r3 - 2)
    gy = cy + math.sin(rad) * (r3 - 2)
    col = rune_colors[(i+2) % len(rune_colors)]
    draw_rune(int(gx), int(gy), col, glyph_types[(i+3) % 6])

# Also few runes on outer ring ticks
for i in range(12):
    ang = 360.0 * i / 12 + 5
    rad = math.radians(ang)
    gx = cx + math.cos(rad) * (r1 - 5)
    gy = cy + math.sin(rad) * (r1 - 5)
    col = rune_colors[(i+4) % len(rune_colors)]
    draw_rune(int(gx), int(gy), col, glyph_types[(i+1) % 6])

# ---- Inner mechanical detail ----
# Inner calibration dials
# Spokes from core to ring
for i in range(8):
    ang = 360.0 * i / 8 + 22.5
    rad = math.radians(ang)
    x0 = cx + math.cos(rad) * 18
    y0 = cy + math.sin(rad) * 18
    x1 = cx + math.cos(rad) * (r4 - 2)
    y1 = cy + math.sin(rad) * (r4 - 2)
    c.line(int(x0), int(y0), int(x1), int(y1), BRASS_DARK)

# Small dials (gear-like rings) on inner area
for dial_i, (drad, dcol) in enumerate([(36, BRASS), (44, BRASS_DARK)]):
    # small gear teeth
    for t in range(12):
        ta = 360.0 * t / 12 + dial_i * 8
        trad = math.radians(ta)
        tx = cx + math.cos(trad) * drad
        ty = cy + math.sin(trad) * drad
        c.set(int(tx), int(ty), BRASS_DARK)
        c.set(int(tx) + ((int(tx) != int(cx + (math.cos(trad)*drad))) and 0), int(ty), BRASS_DARK)
    c.circle(int(cx), int(cy), int(drad) - 1, dcol, fill=False)

# Gear teeth between ring 3 and ring 4 (more intricate gears)
for t in range(18):
    ta = 360.0 * t / 18 + 3
    trad = math.radians(ta)
    grx = cx + math.cos(trad) * (r3 - 2)
    gry = cy + math.sin(trad) * (r3 - 2)
    c.set(int(grx), int(gry), BRASS_MID)
    c.set(int(grx) - int(math.cos(trad + 0.35) * 2), int(gry) - int(math.sin(trad + 0.35) * 2), BRASS_DARK)

# Fine cross-hatch texture on ring 2 surface (small dots across the band)
for hi in range(12):
    ha2 = 360.0 * hi / 12 + 6
    hrad2 = math.radians(ha2)
    hdx = cx + math.cos(hrad2) * (r2 - 4)
    hdy = cy + math.sin(hrad2) * (r2 - 4)
    c.set(int(hdx), int(hdy), GOLD_DARK)

# ---- Complex gear arrangement near pedestal ----
# Gears between instrument and pedestal (floating assembly brackets)
# Support brackets from under instrument to pedestal
for bx in [-20, 0, 20]:
    c.line(cx + bx, cy + 44, cx + bx, cy + 58, BRASS_DARK)
    c.line(cx + bx - 3, cy + 58, cx + bx + 3, cy + 58, BRASS_DARK)

# Small dangling gear below the orrery
c.circle(cx, cy + 50, 6, BRASS_DARK, fill=True)
c.circle(cx, cy + 50, 4, BRASS_MID, fill=True)
c.circle(cx, cy + 50, 2, BRASS_DARK, fill=True)
for t in range(8):
    ta2 = 360.0 * t / 8 + 12
    trad2 = math.radians(ta2)
    tx2 = cx + math.cos(trad2) * 5
    ty2 = cy + 50 + math.sin(trad2) * 5
    c.set(int(tx2), int(ty2), BRASS_DARK)

# More complex pedestal crown embellishment
# Decorative filigree on pedestal top
for fx in range(cx-40, cx+40, 8):
    c.set(fx, 169, c.color((50, 45, 65), "pededge"))
for fx in range(cx-32, cx+32, 8):
    c.set(fx, 174, GOLD_DARK)
    c.set(fx, 175, GOLD_DARK)

# ---- Outer decorative framework ----
# Scalloped outer edge embellishments (small circles around the main orb)
for e_i in range(16):
    ea = 360.0 * e_i / 16
    erad = math.radians(ea)
    ex = cx + math.cos(erad) * (r1 + 6)
    ey = cy + math.sin(erad) * (r1 + 6)
    c.circle(int(ex), int(ey), 3, BRASS_DARK, fill=True)
    c.circle(int(ex), int(ey), 2, BRASS_MID, fill=True)
    c.set(int(ex)+1, int(ey), BRASS_LIGHT)

# Outer protective cage structure (thin arcs connect the scallops)
for e_i in range(16):
    ea0 = math.radians(360.0 * e_i / 16)
    ea1 = math.radians(360.0 * (e_i+1) / 16)
    ex0 = cx + math.cos(ea0) * (r1 + 6)
    ey0 = cy + math.sin(ea0) * (r1 + 6)
    ex1 = cx + math.cos(ea1) * (r1 + 6)
    ey1 = cy + math.sin(ea1) * (r1 + 6)
    # connect every other pair with a thin line
    if e_i % 2 == 0:
        c.line(int(ex0), int(ey0), int(ex1), int(ey1), BRASS_DARK)

# Additional small decorative torus rings floating above the orrery
for orbit in [(r1+10, c.color((45, 35, 60), "smallorb")),
              (r1-r3, c.color((40, 50, 70), "smallorb2"))]:
    # small orbits
    for ao in range(0, 360, 10):
        arad = math.radians(ao)
        ox = cx + math.cos(arad) * orbit[0]
        oy = cy + math.sin(arad) * orbit[0]
        c.set(int(ox), int(oy), orbit[1])

# ---- Glowing aura around the whole instrument ----
for aura_r, aura_c in [(r1+14, c.color((30, 25, 45), "aura1")),
                       (r1+20, c.color((22, 20, 38), "aura2"))]:
    c.circle(cx, cy, aura_r, aura_c, fill=False)

# Light spill from core onto floor
c.ellipse(cx, 196, 40, 14, c.color((50, 35, 20), "light_floor"), fill=True)
c.ellipse(cx, 194, 28, 8, c.color((90, 60, 25), "light_floor2"), fill=True)

# Light rays from core (subtle radial glow lines)
for ray_i in range(12):
    ra = 360.0 * ray_i / 12 + 15
    rrad = math.radians(ra)
    # short radial rays in the gap between core and r4
    for dist in range(core_r + 1, core_r + 9, 2):
        rx = cx + math.cos(rrad) * dist
        ry = cy + math.sin(rrad) * dist
        c.set(int(rx), int(ry), CORE_DEEP)

# ---- Dark outline around key features for dramatic look ----
def dark_px(gx, gy):
    c.set(gx, gy, c.color((12, 12, 16), "darkln"))

# Outline around outer rim
for ang_idx in range(0, 360, 2):
    rad = math.radians(ang_idx)
    ox = cx + math.cos(rad) * (r1 + 2)
    oy = cy + math.sin(rad) * (r1 + 2)
    dark_px(int(ox), int(oy))

# Additional ring shadows for depth - inner edge shadows
for ang_idx in range(0, 360, 3):
    rad = math.radians(ang_idx)
    sx = cx + math.cos(rad) * (r3 - 7)
    sy = cy + math.sin(rad) * (r3 - 7)
    c.set(int(sx), int(sy), PATINA)

# Highlight top-left of brass (dramatic lighting from top-left)
for ang_idx in range(90, 270, 3):
    rad = math.radians(ang_idx)
    hx = cx + math.cos(rad) * r2
    hy = cy + math.sin(rad) * r2
    c.set(int(hx), int(hy), BRASS_LIGHT)

for ang_idx in range(100, 260, 4):
    rad = math.radians(ang_idx)
    hx = cx + math.cos(rad) * (r2 - 1)
    hy = cy + math.sin(rad) * (r2 - 1)
    c.set(int(hx), int(hy), GOLD_LIGHT)

# ---- Additional fine gear detail in the thin gaps ----
# Small dots along ring 3 (studs)
for i in range(20):
    ang = 360.0 * i / 20 + 4
    rad = math.radians(ang)
    sx = cx + math.cos(rad) * (r3)
    sy = cy + math.sin(rad) * (r3)
    c.set(int(sx), int(sy), BRASS_LIGHT)
    c.set(int(sx)+1, int(sy), BRASS)

# Additional fine rivets every few degrees on ring 4
for i in range(16):
    ang = 360.0 * i / 16 + 17
    rad = math.radians(ang)
    rx = cx + math.cos(rad) * (r4 - 1)
    ry = cy + math.sin(rad) * (r4 - 1)
    c.set(int(rx), int(ry), GOLD_DARK)
    c.set(int(rx) + 1, int(ry), BRASS_LIGHT)

# ---- Decorative alchemical dial needle ----
# A set of pointer hands at angles
for hand_i, (hstart, hlen, hcol) in enumerate([
    (40, 30, BRASS_DARK),  # from ring4 outward
    (160, 30, BRASS_DARK),
    (280, 30, BRASS_DARK),
]):
    ha = math.radians(hstart)
    hx0 = cx + math.cos(ha) * (r4 - 2)
    hy0 = cy + math.sin(ha) * (r4 - 2)
    hx1 = cx + math.cos(ha) * (r4 - 2 + hlen)
    hy1 = cy + math.sin(ha) * (r4 - 2 + hlen)
    c.line(int(hx0), int(hy0), int(hx1), int(hy1), hcol)
    # needle tip
    c.line(int(hx1) - int(math.cos(ha)*3), int(hy1) - int(math.sin(ha)*3),
           int(hx1) - int(math.cos(ha+0.4)*3), int(hy1) - int(math.sin(ha+0.4)*3), BRASS_DARK)

# Additional inner dial with degree markings
for di in range(36):
    da = math.radians(di * 10)
    # small degree marks between r4 and r3
    dmag = r3 - 4
    dx = cx + math.cos(da) * dmag
    dy = cy + math.sin(da) * dmag
    dot = c.color((90, 75, 45), "degmark") if di % 3 == 0 else GOLD_DARK
    c.set(int(dx), int(dy), dot)

# ---- Additional hotspots ----
# Small decorative glyphs around core
for i in range(6):
    ang = 90 + i * 60
    rad = math.radians(ang)
    gx = cx + math.cos(rad) * (r4 - 5)
    gy = cy + math.sin(rad) * (r4 - 5)
    c.set(int(gx), int(gy), RUNE_CYAN)

# Ambient dust / particles floating
import random
random.seed(42)
particle_colors = [c.color((80, 70, 100), "dust"), c.color((60, 50, 80), "dust2"), c.color((120, 90, 60), "dust3")]
for _ in range(40):
    px = random.randint(20, 235)
    py = random.randint(20, 200)
    # keep clear of the main instrument area
    dist = math.sqrt((px-cx)**2 + (py-cy)**2)
    if dist > r1:
        c.set(px, py, particle_colors[_ % 3])

# Final polish - a thin decorative top arch hint above the instrument
# Corner flourishes in the hall (arches)
for arch_x in [30, 200]:
    c.poly([(arch_x, 200), (arch_x+20, 200), (arch_x+20, 208), (arch_x, 208)], c.color((13, 12, 20), "arch"), fill=True)

# ===== ENHANCED DETAIL =====

# Outer ring etching - fine circular line details
for etch_r in [r1-5, r1-7, r1-13, r1-1]:
    c.circle(cx, cy, etch_r, BRASS_DARK, fill=False)

# Decorative swirls on ring band (small curved accents)
for swl in range(8):
    swa = 360.0 * swl / 8 + 45
    srad = math.radians(swa)
    # small arc-like features
    for ed in range(-20, 20, 4):
        cura = math.radians(swa + ed)
        crx = cx + math.cos(cura) * (r2 - 4)
        cry = cy + math.sin(cura) * (r2 - 4)
        c.set(int(crx), int(cry), c.color((170, 125, 55), "etch"))

# Add a delicate outer rotating assembly ring (thin gold thread at an offset angle)
for oa in range(0, 360, 4):
    orad = math.radians(oa)
    otx = cx + math.cos(orad) * 61
    oty = cy + math.sin(orad) * 61
    c.set(int(otx), int(oty), GOLD_DARK)

# Complex gear arrangement - small gears at cardinal points of the outer ring
for gear_ang, gear_r in [(0, 8), (90, 6), (180, 8), (270, 6)]:
    ga = math.radians(gear_ang)
    ggx = cx + math.cos(ga) * (r1 + 1)
    ggy = cy + math.sin(ga) * (r1 + 1)
    c.circle(int(ggx), int(ggy), gear_r, BRASS_DARK, fill=True)
    c.circle(int(ggx), int(ggy), gear_r - 1, BRASS_MID, fill=True)
    c.circle(int(ggx), int(ggy), 1, BRASS_DARK, fill=True)

# Additional exotic rune cluster near pedestal base  
for pr_idx, (prx, pry) in enumerate([(100, 190), (125, 187), (150, 190), (135, 194), (112, 194)]):
    c.set(prx, pry, RUNE_BLUE)
    c.set(prx+1, pry, RUNE)
    c.set(prx, pry+1, RUNE_CYAN)

# More visible floating rings with small moons
for moon_ang, moon_r in [(200, 3), (320, 2), (50, 2)]:
    ma = math.radians(moon_ang)
    mx = cx + math.cos(ma) * (r1 + 9)
    my = cy + math.sin(ma) * (r1 + 9)
    c.circle(int(mx), int(my), moon_r, c.color((180, 155, 100), "moon"), fill=True)
    c.circle(int(mx) - 1, int(my) - 1, moon_r - 1, c.color((230, 205, 150), "moon_hi"), fill=True)

# ===== ADDITIONAL MECHANICAL COMPLEXITY =====

# Fine interleaved gear teeth between ring 2 and ring 3
for gt in range(36):
    gta = math.radians(gt * 10)
    # teeth pattern alternating brass shades
    for sign in [-1, 1]:
        tx_pos = cx + math.cos(gta) * (r2 - 5) + sign * math.sin(gta) * 1
        ty_pos = cy + math.sin(gta) * (r2 - 5) - sign * math.cos(gta) * 1
        c.set(int(tx_pos), int(ty_pos), BRASS_MID if gt % 2 == 0 else BRASS_DARK)

# Small ornate flourishes at the top of the instrument (crown structure)
top_crown_y = cy - r1 - 14
c.rect(cx - 8, top_crown_y, 16, 5, BRASS_DARK)
c.rect(cx - 6, top_crown_y - 3, 12, 4, BRASS_MID)
c.rect(cx - 3, top_crown_y - 6, 6, 3, BRASS_DARK)
c.set(cx, top_crown_y - 7, RUNE_GOLD)
# crown finial
c.circle(cx, top_crown_y - 9, 2, BRASS_DARK, fill=True)
c.set(cx, top_crown_y - 10, RUNE_GOLD)

# Under-glow illumination on the pedestal surface
# Antigravity gap glow
for gy2 in range(156, 166):
    fade = 1.0 - (gy2 - 156) / 10.0
    gl_color = c.color((int(60 * fade), int(50 * fade), int(90 * fade)), f"aglow_{gy2}")
    c.rect(90, gy2, 76, 1, gl_color)

# Multiple small cogs and gears at various positions touching the rings
import random as rnd2
rnd2.seed(7)
for _g in range(5):
    ga2 = rnd2.uniform(0, 360)
    grad = math.radians(ga2)
    gd = rnd2.uniform(r2, r3) if _g < 2 else rnd2.uniform(r3, r4)
    ggr_r = rnd2.randint(2, 4)
    ggx2 = cx + math.cos(grad) * (gd - ggr_r)
    ggy2 = cy + math.sin(grad) * (gd - ggr_r)
    c.circle(int(ggx2), int(ggy2), ggr_r, BRASS_DARK, fill=True)
    c.circle(int(ggx2), int(ggy2), ggr_r - 1, BRASS_MID, fill=True)

# Gateway arches on the hall columns (decorative)
for gwx, gw in [(22, 12), (228, 12)]:
    # subtle gold trim on columns
    c.rect(gwx, 100, gw, 2, c.color((50, 40, 30), "coltrim"))
    c.rect(gwx, 140, gw, 2, c.color((50, 40, 30), "coltrim2"))
    c.set(gwx + gw//2, 100, RUNE_GOLD)
    c.set(gwx + gw//2, 140, RUNE_GOLD)

# ===== DRAMATIC LIGHTING ENHANCEMENTS =====

# Upper arch light shaft from a high window (soft glow)
# Subtle gradient beam from above
for by in range(30, 100, 3):
    beam_alpha = 0.8 - (by - 30) / 150.0
    beam_w = int(20 + (by - 30) * 0.8)
    beam_col = c.color((int(60 * beam_alpha), int(50 * beam_alpha), int(80 * beam_alpha)), f"beam_{by}")
    c.rect(cx - beam_w, by, beam_w * 2, 2, beam_col)

# Reflective glints on the brass (small bright spots scattered on ring surfaces)
for _gl in range(30):
    gl_a = rnd2.uniform(0, 360)
    gl_rad = math.radians(gl_a)
    gl_r = rnd2.choice([r1-2, r1-6, r2-1, r2-4, r3-1, r3-3])
    if _gl % 3 == 0:
        glx = cx + math.cos(gl_rad) * gl_r
        gly = cy + math.sin(gl_rad) * gl_r
        c.set(int(glx), int(gly), BRASS_LIGHT)

# Detailed base decoration on pedestal 
# Carved relief along pedestal body
for relief_y in [180, 184, 188, 196, 200, 204]:
    for relief_x in range(80, 177, 4):
        if (relief_x + relief_y) % 4 == 0:
            c.set(relief_x, relief_y, c.color((30, 28, 40), "relief"))

# Small floating rune particles suspended around the instrument
for fp_i, (fx, fy) in enumerate([
    (95, 55), (160, 70), (85, 100), (175, 130), 
    (75, 140), (180, 90), (100, 170), (155, 165),
    (70, 75), (190, 110),
]):
    fcol = rune_colors[fp_i % len(rune_colors)]
    c.set(fx, fy, fcol)
    # faint connection line to instrument
    c.line(fx, fy, cx, cy, c.color((40, 30, 50), f"fconn_{fp_i}"))

# Additional ornate details on the outer ring - small rose-window patterns
for rw in range(12):
    rwa = math.radians(rw * 30)
    for dist_r in [r1 - 9, r1 - 11]:
        rx2 = cx + math.cos(rwa) * dist_r
        ry2 = cy + math.sin(rwa) * dist_r
        c.set(int(rx2), int(ry2), c.color((95, 75, 35), "rosepetal"))

# Etched symbols between rings  
for sym_i in range(4):
    sym_a = math.radians(90 * sym_i + 45)
    for sd in range(0, 8, 2):
        sx2 = cx + math.cos(sym_a) * (r3 - 7 + sd)
        sy2 = cy + math.sin(sym_a) * (r3 - 7 + sd)
        c.set(int(sx2), int(sy2), PATINA)

# Quadrant markers on the outermost ring (IV, X, Ω symbols)
# Using simple glyph marks at 0/90/180/270  
for q_i in range(4):
    qa = math.radians(90 * q_i + 22)
    # diamond markers
    for qd in range(-2, 3):
        qdx = cx + math.cos(qa + math.pi/4) * 0 - math.sin(qa + math.pi/4) * qd
        qdy = cy + math.sin(qa + math.pi/4) * 0 + math.cos(qa + math.pi/4) * qd
    # directly set diamond around r1-9
    qpx = int(cx + math.cos(qa) * (r1 - 9))
    qpy = int(cy + math.sin(qa) * (r1 - 9))
    c.set(qpx, qpy, GOLD)
    c.set(qpx + 2, qpy, GOLD_DARK)
    c.set(qpx - 2, qpy, GOLD_DARK)
    c.set(qpx + 1, qpy + 1, GOLD_LIGHT)
    c.set(qpx - 1, qpy + 1, GOLD)

# Radial energy lines emanating from core outward through the rings
for e_i in range(8):
    ea_rad = math.radians(45 * e_i + 10)
    # thin metallic spokes passing through the rings
    for spd in range(45, 65, 5):
        spx = cx + math.cos(ea_rad) * spd
        spy = cy + math.sin(ea_rad) * spd
        if spd % 5 == 0:
            c.set(int(spx), int(spy), BRASS_MID)

# Subtle pulsing core edge - bright ring
c.circle(cx, cy, core_r + 9, c.color((255, 180, 90), "corepulse"), fill=False)
c.circle(cx, cy, core_r + 10, c.color((200, 120, 50), "corepulse2"), fill=False)

# Additional fine brass wire pods at intersection points of rings
for w_i in range(10):
    wa = math.radians(36 * w_i + 3)
    wx2 = cx + math.cos(wa) * (r1 - 9)
    wy2 = cy + math.sin(wa) * (r1 - 9)
    c.circle(int(wx2), int(wy2), 1, BRASS_HI, fill=True)

# Complex secondary mechanism - curved comet tails behind spheres
for cm_i, (cm_ang, cm_len, cm_col) in enumerate([
    (350, 12, BRASS_DARK),
    (170, 10, BRASS_DARK),
    (80, 10, BRASS_DARK),
    (260, 12, BRASS_DARK),
]):
    cm_rad = math.radians(cm_ang)
    # tail trailing from crystal positions
    for td in range(1, cm_len):
        tx2 = int(cx + math.cos(cm_rad) * (r1 - 15 - td))
        ty2 = int(cy + math.sin(cm_rad) * (r1 - 15 - td))
        # fade the tail
        if td < cm_len // 3:
            c.set(tx2, ty2, BRASS_MID)
        else:
            c.set(tx2, ty2, cm_col)

# Sky/machinery faint clockwork arc above the main orrery
# Large faint metallic frame arches
for arc_r in [78, 82]:
    for arc_a in range(0, 181, 6):
        aar = math.radians(arc_a)
        ax2 = cx + math.cos(aar) * arc_r
        ay2 = cy + math.sin(aar) * arc_r
        c.set(int(ax2), int(ay2), c.color((35, 28, 45), "frame"))

# More ornate pedestal detailing - carved steps
for step_y in range(168, 214, 6):
    step_shade = STONE if (step_y - 168) % 12 < 6 else STONE_DARK
    step_width = 96 - ((step_y - 168) // 6) * 4
    c.rect(cx - step_width//2, step_y, step_width, 5, step_shade)

# Small torch light sources on pedestal sides
for tl_side, tl_y in [(-1, 190), (1, 190)]:
    torch_color = c.color((200, 140, 60), "torch")
    tl_x = cx + tl_side * 45
    c.circle(tl_x, tl_y, 2, torch_color, fill=True)
    # torch glow
    c.set(tl_x, tl_y + 3, c.color((150, 100, 40), "torch_low"))
    c.set(tl_x + tl_side, tl_y - 1, c.color((255, 200, 120), "torch_hi"))

# Verify and finish
print(c.stats_text())

finish(c)
