import math

c = new_canvas(32, 32)

# --- Precise RTS Palette ---
C_OUT        = '#11151e'
C_OUT_SMK    = '#2c3746'

# Ground Shadows
C_SHAD_DEEP  = '#0e121a'
C_SHAD_MID   = '#181e2b'
C_SHAD_SOFT  = '#242d3d'

# Concrete Foundation Base
C_FND_DARK   = '#222934'
C_FND_SHAD   = '#354050'
C_FND_MID    = '#4e5c70'
C_FND_LIT    = '#6b7d96'
C_FND_HI     = '#93a7c2'

# Brick Wall - Sunlit (Left / South-West)
C_MORT_LIT   = '#3c1815'
C_BRK_L_DRK  = '#78271e'
C_BRK_L_MID  = '#a33526'
C_BRK_L_LIT  = '#c94833'
C_BRK_L_HI   = '#e8654b'
C_BRK_L_TOP  = '#f4856c'

# Brick Wall - Shaded (Right / South-East)
C_MORT_SHD   = '#1b0d0f'
C_BRK_S_DRK  = '#351312'
C_BRK_S_MID  = '#541c1b'
C_BRK_S_LIT  = '#752622'
C_BRK_S_HI   = '#94332c'

# Structural Steel Columns / Beams
C_STL_DRK    = '#181d26'
C_STL_SHAD   = '#2c3644'
C_STL_MID    = '#46556b'
C_STL_LIT    = '#6a7e9c'
C_STL_HI     = '#9bb0cc'

# Parapet & Flat Roof
C_PAR_HI     = '#9bb0cc'
C_PAR_MID    = '#677a94'
C_PAR_SHAD   = '#3e4b5e'
C_PAR_IN_SH  = '#181f28'

C_ROOF_DEEP  = '#222934'
C_ROOF_MID   = '#333d4c'
C_ROOF_LIT   = '#49576a'

# Roll-Up Door
C_DR_FRAME   = '#1a2028'
C_DR_SHAD    = '#303a48'
C_DR_MID     = '#4a596e'
C_DR_LIT     = '#6d819c'
C_DR_HI      = '#9bb0cc'

# Hazard Stripe & Indicator Lamp
C_HAZ_YEL    = '#f5b522'
C_HAZ_YEL_H  = '#ffde61'
C_HAZ_BLK    = '#1c1913'
C_LAMP_RED   = '#e82a2a'
C_LAMP_GLW   = '#ff6e6e'

# Vents & Louvers
C_VNT_HOLE   = '#0d1017'
C_VNT_FRAME  = '#26303d'
C_VNT_SLAT   = '#55667d'
C_VNT_SL_H   = '#8aa0bb'
C_VNT_FAN    = '#364454'

# Chimney
C_CHM_DRK    = '#381614'
C_CHM_MID    = '#69251d'
C_CHM_LIT    = '#993527'
C_CHM_HI     = '#c74935'
C_CHM_TOP_H  = '#e86a52'
C_CHM_BAND_S = '#7a4a0e'
C_CHM_BAND_M = '#b87618'
C_CHM_BAND_L = '#f5b522'
C_CHM_BAND_H = '#ffde61'
C_CHM_HOLE   = '#100b0b'

# Smoke
C_SMK_OUT    = '#303b4a'
C_SMK_SHD    = '#526075'
C_SMK_MID    = '#8394ab'
C_SMK_LIT    = '#c2d2e3'
C_SMK_HI     = '#ffffff'

pixels = {}

def set_px(x, y, color):
    if 0 <= x < 32 and 0 <= y < 32 and color is not None:
        pixels[(x, y)] = color

# =========================================================
# 1. GROUND SHADOW
# =========================================================
for x in range(5, 28):
    set_px(x, 29, C_SHAD_DEEP)
for x in range(8, 28):
    set_px(x, 30, C_SHAD_DEEP)
for x in range(12, 27):
    set_px(x, 31, C_SHAD_DEEP)

for (x, y) in [(4, 29), (28, 29), (7, 30), (28, 30), (10, 31), (11, 31), (27, 31), (28, 31)]:
    set_px(x, y, C_SHAD_SOFT)
for (x, y) in [(28, 29), (28, 30), (27, 31), (9, 31)]:
    set_px(x, y, C_SHAD_MID)

# =========================================================
# 2. CONCRETE FOUNDATION SLAB
# =========================================================
left_fnd = [
    (15, 28), (14, 28),
    (13, 27), (12, 27),
    (11, 26), (10, 26),
    (9, 25), (8, 25),
    (7, 24), (6, 24),
    (5, 23), (4, 23)
]
for (x, y) in left_fnd:
    set_px(x, y, C_FND_LIT)
    set_px(x, y - 1, C_FND_HI)
    set_px(x, y + 1, C_OUT)

right_fnd = [
    (16, 28), (17, 28),
    (18, 27), (19, 27),
    (20, 26), (21, 26),
    (22, 25), (23, 25),
    (24, 24), (25, 24),
    (26, 23), (27, 23)
]
for (x, y) in right_fnd:
    set_px(x, y, C_FND_DARK)
    set_px(x, y - 1, C_FND_SHAD)
    set_px(x, y + 1, C_OUT)

# =========================================================
# 3. BRICK WALLS (Prompt: "brick walls")
# =========================================================
left_bot = {4: 22, 5: 22, 6: 23, 7: 23, 8: 24, 9: 24, 10: 25, 11: 25, 12: 26, 13: 26, 14: 27, 15: 27}
left_top = {4: 12, 5: 12, 6: 13, 7: 13, 8: 14, 9: 14, 10: 15, 11: 15, 12: 16, 13: 16, 14: 17, 15: 17}

for x in range(4, 16):
    y_b = left_bot[x]
    y_t = left_top[x]
    for y in range(y_t, y_b + 1):
        iso_c = y - (x // 2)
        if iso_c % 2 == 0:
            set_px(x, y, C_MORT_LIT if (x + y) % 2 == 0 else C_BRK_L_DRK)
        else:
            brick_phase = (x + (iso_c // 2) * 2) % 3
            if brick_phase == 0:
                set_px(x, y, C_MORT_LIT)
            elif (x + y) % 4 == 0:
                set_px(x, y, C_BRK_L_TOP)
            elif (x + y) % 2 == 0:
                set_px(x, y, C_BRK_L_HI)
            else:
                set_px(x, y, C_BRK_L_MID)

right_bot = {16: 27, 17: 27, 18: 26, 19: 26, 20: 25, 21: 25, 22: 24, 23: 24, 24: 23, 25: 23, 26: 22, 27: 22}
right_top = {16: 17, 17: 17, 18: 16, 19: 16, 20: 15, 21: 15, 22: 14, 23: 14, 24: 13, 25: 13, 26: 12, 27: 12}

for x in range(16, 28):
    y_b = right_bot[x]
    y_t = right_top[x]
    for y in range(y_t, y_b + 1):
        iso_c = y - ((31 - x) // 2)
        if iso_c % 2 == 0:
            set_px(x, y, C_MORT_SHD)
        else:
            brick_phase = (x + (iso_c // 2) * 2) % 3
            if brick_phase == 0:
                set_px(x, y, C_MORT_SHD)
            elif (x + y) % 3 == 0:
                set_px(x, y, C_BRK_S_HI)
            elif (x + y) % 2 == 0:
                set_px(x, y, C_BRK_S_LIT)
            else:
                set_px(x, y, C_BRK_S_MID)

# =========================================================
# 4. ROLL-UP FACTORY SHUTTER DOOR (Left Wall)
# =========================================================
# Frame posts:
for y in range(19, 24):
    set_px(6, y, C_DR_FRAME)
for y in range(21, 26):
    set_px(11, y, C_DR_FRAME)

# Lintel Header (Row following isometric slope)
# x=6..11
lintel_header = [(6, 19), (7, 19), (8, 20), (9, 20), (10, 21), (11, 21)]
for (lx, ly) in lintel_header:
    set_px(lx, ly, C_DR_FRAME)

# Warning beacon light on top of lintel:
set_px(8, 19, C_LAMP_GLW)
set_px(9, 19, C_LAMP_RED)

# Hazard stripes directly under lintel:
hazard_pts = [(6, 20), (7, 20), (8, 21), (9, 21), (10, 22), (11, 22)]
for i, (hx, hy) in enumerate(hazard_pts):
    set_px(hx, hy, C_HAZ_YEL if (i % 2 == 0) else C_HAZ_BLK)

# Corrugated shutter slats
slat_cols = {
    7: (21, 23),
    8: (22, 24),
    9: (22, 24),
    10: (23, 25)
}
for x, (y0, y1) in slat_cols.items():
    for y in range(y0, y1 + 1):
        if y == y0:
            set_px(x, y, C_DR_HI)
        elif (y - y0) % 2 == 1:
            set_px(x, y, C_DR_SHAD)
        else:
            set_px(x, y, C_DR_LIT if x <= 8 else C_DR_MID)

# =========================================================
# 5. WALL VENTS (Prompt: "vents", crisp industrial design)
# =========================================================
# Wall Vent 1 (Left wall, between door and center column):
# Clean louvered vent grille at x=13..14, y=22..25
set_px(12, 22, C_VNT_FRAME); set_px(12, 23, C_VNT_FRAME); set_px(12, 24, C_VNT_FRAME)
set_px(15, 23, C_VNT_FRAME); set_px(15, 24, C_VNT_FRAME); set_px(15, 25, C_VNT_FRAME)
set_px(13, 21, C_VNT_FRAME); set_px(14, 22, C_VNT_FRAME)

set_px(13, 22, C_VNT_SL_H); set_px(14, 23, C_VNT_SL_H)
set_px(13, 23, C_VNT_HOLE); set_px(14, 24, C_VNT_HOLE)
set_px(13, 24, C_VNT_SLAT); set_px(14, 25, C_VNT_SLAT)
set_px(13, 25, C_VNT_HOLE); set_px(14, 26, C_VNT_HOLE)

# Wall Vent 2 (Right wall): Large industrial louvered vent panel at x=18..23, y=18..23
for vx in range(18, 24):
    set_px(vx, 18, C_VNT_FRAME)
    set_px(vx, 23, C_VNT_FRAME)
for vy in range(18, 24):
    set_px(18, vy, C_VNT_FRAME)
    set_px(23, vy, C_VNT_FRAME)

# Louver slats & dark airflow gaps inside Vent 2:
for vx in range(19, 23):
    set_px(vx, 19, C_VNT_SL_H if vx <= 20 else C_VNT_SLAT)
    set_px(vx, 20, C_VNT_HOLE)
    set_px(vx, 21, C_VNT_SLAT if vx <= 20 else C_STL_SHAD)
    set_px(vx, 22, C_VNT_HOLE)

# Vertical steel conduit / pipe on right wall:
for vy in range(14, 23):
    set_px(25, vy, C_STL_LIT if vy % 2 == 0 else C_STL_MID)
    set_px(26, vy, C_STL_DRK)

# =========================================================
# 6. STRUCTURAL CORNER COLUMNS & SILHOUETTE
# =========================================================
for y in range(17, 28):
    set_px(15, y, C_STL_HI if y % 3 != 0 else C_STL_LIT)
    set_px(16, y, C_STL_MID if y % 3 != 0 else C_STL_SHAD)

for y in range(12, 23):
    set_px(4, y, C_STL_HI)
    set_px(3, y, C_OUT)

for y in range(12, 23):
    set_px(27, y, C_STL_SHAD)
    set_px(28, y, C_OUT)

# =========================================================
# 7. PARAPET & FLAT ROOF DECK (Prompt: "flat roof")
# =========================================================
# Front-left parapet coping
for (x, y) in [
    (4, 12), (5, 12),
    (6, 13), (7, 13),
    (8, 14), (9, 14),
    (10, 15), (11, 15),
    (12, 16), (13, 16),
    (14, 17), (15, 17)
]:
    set_px(x, y, C_PAR_HI)
    set_px(x, y + 1, C_PAR_MID)

# Front-right parapet coping
for (x, y) in [
    (16, 17), (17, 17),
    (18, 16), (19, 16),
    (20, 15), (21, 15),
    (22, 14), (23, 14),
    (24, 13), (25, 13),
    (26, 12), (27, 12)
]:
    set_px(x, y, C_PAR_MID)
    set_px(x, y + 1, C_PAR_SHAD)

# Back-left parapet coping
for (x, y) in [
    (4, 12), (5, 12),
    (6, 11), (7, 11),
    (8, 10), (9, 10),
    (10, 9), (11, 9),
    (12, 8), (13, 8),
    (14, 7), (15, 7)
]:
    set_px(x, y, C_PAR_MID)
    set_px(x, y - 1, C_OUT)

# Back-right parapet coping
for (x, y) in [
    (16, 7), (17, 7),
    (18, 8), (19, 8),
    (20, 9), (21, 9),
    (22, 10), (23, 10),
    (24, 11), (25, 11),
    (26, 12), (27, 12)
]:
    set_px(x, y, C_PAR_SHAD)
    set_px(x, y - 1, C_OUT)

# Recessed Flat Roof Deck
for x in range(5, 27):
    if x <= 15:
        y_back = 7 + (15 - x) // 2
        y_front = 16 - (15 - x) // 2
    else:
        y_back = 7 + (x - 16) // 2
        y_front = 16 - (x - 16) // 2

    for y in range(y_back + 1, y_front):
        if y == y_back + 1:
            set_px(x, y, C_PAR_IN_SH)
        elif y == y_back + 2:
            set_px(x, y, C_ROOF_DEEP)
        elif (x + y) % 3 == 0:
            set_px(x, y, C_ROOF_LIT)
        else:
            set_px(x, y, C_ROOF_MID)

# =========================================================
# 8. ROOFTOP VENTILATION UNIT & PIPE (Rooftop Vent)
# =========================================================
# HVAC Air Handler Box at x=17..21, y=9..13
set_px(19, 9, C_STL_HI)
set_px(18, 10, C_STL_HI); set_px(19, 10, C_VNT_HOLE); set_px(20, 10, C_STL_LIT)
set_px(17, 11, C_STL_HI); set_px(18, 11, C_VNT_HOLE); set_px(19, 11, C_VNT_FAN); set_px(20, 11, C_VNT_HOLE); set_px(21, 11, C_STL_SHAD)
set_px(18, 12, C_STL_MID); set_px(19, 12, C_VNT_HOLE); set_px(20, 12, C_STL_SHAD)

set_px(17, 12, C_VNT_SL_H); set_px(18, 13, C_VNT_SLAT)
set_px(21, 12, C_STL_DRK); set_px(20, 13, C_STL_DRK)

# Rooftop pipe
for px in range(13, 17):
    set_px(px, 11, C_STL_HI if px % 2 == 0 else C_STL_LIT)
    set_px(px, 12, C_STL_MID)

# =========================================================
# 9. CHIMNEY / SMOKESTACK (Prompt: "chimney")
# =========================================================
# Penetration collar at roof (y=11)
set_px(6, 11, C_OUT); set_px(11, 11, C_OUT)
set_px(7, 11, C_STL_HI); set_px(8, 11, C_STL_LIT); set_px(9, 11, C_STL_MID); set_px(10, 11, C_STL_SHAD)

# Shaft (y=7..10)
for y in range(7, 11):
    set_px(6, y, C_OUT)
    set_px(11, y, C_OUT)
    if y in (7, 8):
        set_px(7, y, C_CHM_BAND_H)
        set_px(8, y, C_CHM_BAND_L)
        set_px(9, y, C_CHM_BAND_M)
        set_px(10, y, C_CHM_BAND_S)
    elif y == 9:
        set_px(7, y, C_STL_HI)
        set_px(8, y, C_STL_LIT)
        set_px(9, y, C_STL_MID)
        set_px(10, y, C_STL_SHAD)
    else:
        set_px(7, y, C_CHM_HI)
        set_px(8, y, C_CHM_LIT)
        set_px(9, y, C_CHM_MID)
        set_px(10, y, C_CHM_DRK)

# Chimney rim / flared collar at y=6:
set_px(5, 6, C_OUT)
set_px(6, 6, C_CHM_TOP_H)
set_px(7, 6, C_CHM_HI)
set_px(8, 6, C_CHM_HOLE)
set_px(9, 6, C_CHM_HOLE)
set_px(10, 6, C_CHM_DRK)
set_px(11, 6, C_OUT)

# =========================================================
# 10. BILLOWING SMOKE (Solid, volumetric, fluffy RTS clouds)
# =========================================================
smoke_cloud = {}

# Three overlapping puffs:
puffs = [
    {'cx': 8.5, 'cy': 4.5, 'r': 2.0},
    {'cx': 12.0, 'cy': 2.2, 'r': 3.0},
    {'cx': 16.5, 'cy': 2.0, 'r': 2.5},
    {'cx': 20.5, 'cy': 2.8, 'r': 1.6}
]

for y in range(0, 6):
    for x in range(6, 24):
        inside = False
        min_norm_dist = 999
        closest_puff = None

        for p in puffs:
            d = math.hypot(x - p['cx'], y - p['cy'])
            if d <= p['r']:
                inside = True
                norm_d = d / p['r']
                if norm_d < min_norm_dist:
                    min_norm_dist = norm_d
                    closest_puff = p

        if inside:
            # Check outline
            touches_outside = False
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                n_inside = False
                for p in puffs:
                    if math.hypot(nx - p['cx'], ny - p['cy']) <= p['r']:
                        n_inside = True
                        break
                if not n_inside:
                    touches_outside = True
                    break

            if touches_outside:
                smoke_cloud[(x, y)] = C_SMK_OUT
            else:
                p = closest_puff
                rel_x = (x - p['cx']) / p['r']
                rel_y = (y - p['cy']) / p['r']
                light_val = -0.7 * rel_x - 0.7 * rel_y

                if light_val > 0.40:
                    smoke_cloud[(x, y)] = C_SMK_HI
                elif light_val > 0.0:
                    smoke_cloud[(x, y)] = C_SMK_LIT
                elif light_val > -0.4:
                    smoke_cloud[(x, y)] = C_SMK_MID
                else:
                    smoke_cloud[(x, y)] = C_SMK_SHD

# Overlay smoke pixels
for (sx, sy), scol in smoke_cloud.items():
    set_px(sx, sy, scol)

# Copy all to canvas
for (x, y), col in pixels.items():
    c.set(x, y, col)

view(c)
print(c.stats_text())
finish(c)
