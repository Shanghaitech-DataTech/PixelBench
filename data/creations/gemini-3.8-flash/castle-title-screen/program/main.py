import math
import random
from pixelbench_api import *

random.seed(1337)

c = new_canvas(128, 128, background='#120c24')

# =============================================================================
# PALETTE DEFINITIONS (Strictly limited and unified, 40 colors total <= 86)
# =============================================================================
SKY_0 = '#120c24'  # Deep twilight zenith
SKY_1 = '#24143a'  # Dusk purple
SKY_2 = '#421748'  # Royal purple
SKY_3 = '#6a1c4e'  # Rich magenta
SKY_4 = '#962447'  # Ruby crimson
SKY_5 = '#c53c34'  # Warm vermilion
SKY_6 = '#e66226'  # Sunset orange
SKY_7 = '#f6922b'  # Amber gold
SKY_8 = '#fec244'  # Horizon bright gold
SUN_LIT = '#ffea78' # Bright sun yellow / window glow
SUN_WHT = '#fffbca' # Sun core white-yellow

CLD_DARK   = '#281030' # Deep cloud shadow
CLD_MID    = '#4d1640' # Cloud purple
CLD_ROSE   = '#842247' # Cloud crimson
CLD_ORANGE = '#cb442c' # Cloud fiery lit
CLD_GOLD   = '#f7962e' # Cloud gold highlight

SEA_DEEP   = '#060a18' # Deep ocean abyss
SEA_MID    = '#0d152c' # Midnight sea
SEA_UPPER  = '#15213d' # Horizon water
SEA_WAVE1  = '#1d2e4d' # Ambient wave ripple
SEA_WAVE2  = '#2d456b' # Wave crest highlight
SEA_FOAM   = '#4d7594' # Foam base
SEA_SPRAY  = '#94c0cc' # Surf spray
SEA_WHITE  = '#ffffff' # Surf whitecap

ROCK_BLACK  = '#080610' # Deep rock shadow / crevice
ROCK_DARK   = '#130f1d' # Basalt rock base
ROCK_MID    = '#221a2e' # Rock midtone
ROCK_LIGHT  = '#372d47' # Rock light stone

RIM_DARK   = '#521b2f' # Deep warm shadow
RIM_RED    = '#8b2737' # Crimson rim
RIM_RUST   = '#be4432' # Vermilion rim
RIM_ORANGE = '#e87230' # Brilliant orange rim
RIM_AMBER  = '#fca84d' # Golden rim highlight

MOSS_DARK  = '#182418' # Grass shadow
MOSS_MID   = '#324524' # Grass midtone
MOSS_LIT   = '#596e2e' # Grass sunlit edge

ROOF_DARK  = '#331021' # Castle roof shadow
ROOF_MID   = '#591321' # Castle roof maroon slate
FLAG_DARK  = '#6e1220' # Flag shadow
FLAG_RED   = '#b81d2c' # Flag crimson
FLAG_BRIGHT= '#e63236' # Flag highlight
WIN_MULLION= '#4f1710' # Window stone frame

# =============================================================================
# 1. SKY GRADIENT (Rows 0 to 73)
# =============================================================================
sky_bands = [
    (0, 11, SKY_0),
    (12, 21, SKY_1),
    (22, 30, SKY_2),
    (31, 39, SKY_3),
    (40, 47, SKY_4),
    (48, 55, SKY_5),
    (56, 62, SKY_6),
    (63, 68, SKY_7),
    (69, 73, SKY_8),
]

for y0, y1, col in sky_bands:
    c.rect(0, y0, 128, y1 - y0 + 1, col)

# 1-row checker dithering between sky bands
for i in range(len(sky_bands) - 1):
    y_edge = sky_bands[i][1]
    col_a = sky_bands[i][2]
    col_b = sky_bands[i + 1][2]
    for x in range(128):
        if (x + y_edge) % 2 == 0:
            c.set(x, y_edge, col_b)
        if (x + y_edge + 1) % 2 == 1:
            c.set(x, y_edge + 1, col_a)

# =============================================================================
# 2. LARGE ORANGE SUN (Kissing the sea horizon at Y=74)
# =============================================================================
sun_cx, sun_cy, sun_r = 38, 58, 16

c.circle(sun_cx, sun_cy, sun_r, SKY_6)
c.circle(sun_cx, sun_cy, sun_r - 2, SKY_7)
c.circle(sun_cx, sun_cy, sun_r - 5, SKY_8)
c.circle(sun_cx, sun_cy, sun_r - 9, SUN_LIT)
c.circle(sun_cx, sun_cy, 3, SUN_WHT)

# =============================================================================
# 3. LAYERED CLOUDS
# =============================================================================
# High cirrus wisps in upper purple sky (Y=4..22)
wisps = [
    (6, 6, 26, CLD_MID, CLD_ROSE),
    (46, 8, 34, CLD_DARK, CLD_MID),
    (92, 5, 26, CLD_DARK, CLD_MID),
    (14, 15, 38, CLD_MID, CLD_ROSE),
    (66, 13, 36, CLD_MID, CLD_ROSE),
    (102, 17, 22, CLD_DARK, CLD_MID),
]
for x0, y0, length, c_dark, c_light in wisps:
    for dx in range(length):
        x = x0 + dx
        if 0 <= x < 128:
            thick = 1 if (dx < 4 or dx > length - 5) else 2
            c.set(x, y0, c_light)
            if thick == 2:
                c.set(x, y0 + 1, c_dark)

# Billowing mid-level sunset clouds on the left (X=0..48, Y=24..42)
def draw_cloud_puff(cx_p, cy_p, rx_p, ry_p):
    for y in range(cy_p - ry_p, cy_p + ry_p + 1):
        for x in range(cx_p - rx_p, cx_p + rx_p + 1):
            if 0 <= x < 128 and 0 <= y < 74:
                d = ((x - cx_p) / rx_p) ** 2 + ((y - cy_p) / ry_p) ** 2
                if d <= 1.0:
                    rel_y = (y - (cy_p - ry_p)) / (2.0 * ry_p)
                    if rel_y < 0.25:
                        col = CLD_ORANGE
                    elif rel_y < 0.5:
                        col = CLD_ROSE
                    elif rel_y < 0.75:
                        col = CLD_MID
                    else:
                        col = CLD_DARK
                    c.set(x, y, col)

left_puffs = [
    (0, 32, 16, 7),
    (14, 27, 13, 6),
    (26, 30, 11, 5),
    (8, 35, 18, 5),
]
for p in left_puffs:
    draw_cloud_puff(p[0], p[1], p[2], p[3])

# Cloud bank base with golden/orange sunset illumination
for x in range(0, 36):
    y = 38 + int(math.sin(x * 0.28) * 0.8)
    c.set(x, y, CLD_ORANGE)
    c.set(x, y + 1, CLD_ROSE if (x % 2 == 0) else CLD_DARK)

# Clouds behind the castle on the right (X=56..88, Y=22..34)
mid_puffs = [
    (68, 27, 13, 5),
    (80, 24, 14, 5),
    (58, 30, 10, 4),
]
for p in mid_puffs:
    draw_cloud_puff(p[0], p[1], p[2], p[3])

# Volumetric cloud bank drifting across upper part of sun (X=14..54, Y=45..52)
for cx_c, cy_c, rx_c, ry_c in [(22, 49, 10, 4), (35, 48, 12, 4), (46, 50, 9, 3)]:
    for y in range(cy_c - ry_c, cy_c + ry_c + 1):
        for x in range(cx_c - rx_c, cx_c + rx_c + 1):
            if 0 <= x < 128 and 0 <= y < 74:
                d = ((x - cx_c) / rx_c) ** 2 + ((y - cy_c) / ry_c) ** 2
                if d <= 1.0:
                    rel_y = (y - (cy_c - ry_c)) / (2.0 * ry_c)
                    if rel_y < 0.3:
                        col = SUN_LIT if (26 <= x <= 46) else CLD_GOLD
                    elif rel_y < 0.6:
                        col = CLD_ORANGE
                    else:
                        col = CLD_ROSE
                    c.set(x, y, col)

# =============================================================================
# 4. SEA & WATER HORIZON (Rows 74 to 127)
# =============================================================================
for y in range(74, 128):
    if y < 80:
        base_c = SEA_UPPER
    elif y < 94:
        base_c = SEA_MID
    else:
        base_c = SEA_DEEP
    c.rect(0, y, 128, 1, base_c)

# Ambient sea ripples across open water (horizontal perspective lines)
for y in range(75, 126):
    is_ripple_row = False
    if y < 84:
        is_ripple_row = (y % 2 == 1)
    elif y < 96:
        is_ripple_row = (y % 2 == 0)
    elif y < 110:
        is_ripple_row = (y % 3 == 0)
    else:
        is_ripple_row = (y % 4 == 0)
        
    if is_ripple_row:
        step = 6 if y < 86 else (10 if y < 100 else 14)
        offset = (y * 5) % step
        for x in range(offset, 128, step):
            refl_dist = abs(x - sun_cx)
            refl_w = 4 + int((y - 74) * 0.45)
            if refl_dist > refl_w + 3:
                c.set(x, y, SEA_WAVE1)
                if y > 86 and x + 1 < 128 and (x % 2 == 0):
                    c.set(x + 1, y, SEA_WAVE2)

# Shimmering Sunset Reflection Path on the Water:
# Authentic liquid reflection directly under the setting sun!
for y in range(74, 122):
    prog = (y - 74) / 48.0
    half_w = 3 + int(prog * 25)
    
    # Alternating ripple rows with natural water gaps
    draw_row = True
    if y < 82:
        draw_row = (y % 2 == 0)
    elif y < 96:
        draw_row = (y % 2 == 0)
    elif y < 108:
        draw_row = (y % 3 != 1)
    else:
        draw_row = (y % 4 == 0)
        
    if draw_row:
        # Core glint
        core_w = 1 if y > 95 else (2 if y > 80 else 1)
        for dx in range(-core_w, core_w + 1):
            x = sun_cx + dx
            if 0 <= x < 128:
                c.set(x, y, SUN_WHT if (abs(dx) <= 0 and y < 92) else SUN_LIT)
                
        # Inner gold ripples
        inner_w = 3 + int(prog * 7)
        for dx in range(-inner_w, inner_w + 1):
            x = sun_cx + dx
            if 0 <= x < 128 and abs(dx) > core_w:
                if (x + y * 2) % 3 != 0:
                    c.set(x, y, SKY_8)
                    
        # Mid orange ripples
        mid_w = 6 + int(prog * 15)
        for dx in range(-mid_w, mid_w + 1):
            x = sun_cx + dx
            if 0 <= x < 128 and abs(dx) > inner_w:
                if (x * 2 + y) % 3 != 0:
                    c.set(x, y, SKY_6)
                    
        # Outer crimson ripple edges
        for dx in range(-half_w, half_w + 1):
            x = sun_cx + dx
            if 0 <= x < 128 and abs(dx) > mid_w:
                if (x + y) % 2 == 0:
                    c.set(x, y, SKY_4)

# =============================================================================
# 5. SEASIDE CLIFF (Right side)
# Natural craggy headland with authentic sedimentary strata and joint fractures
# =============================================================================
def get_cliff_edge_x(y):
    if y < 46:
        return 80
    elif y <= 54:
        return 80 - int((y - 46) * 0.75) # 80 down to 74
    elif y <= 64:
        return 74 + int((y - 54) * 0.4)  # 74 to 78
    elif y <= 76:
        return 78 - int((y - 64) * 0.75) # 78 out to 69 (promontory)
    elif y <= 90:
        return 69 + int((y - 76) * 0.3)  # 69 to 73
    elif y <= 104:
        return 73 - int((y - 90) * 0.6)  # 73 to 64
    else:
        return 64 + int((y - 104) * 0.6) # 64 to 78

def get_cliff_plateau_y(x):
    y = 46 - int((x - 80) * 0.1) + int(math.sin(x * 0.35) * 1.0)
    return max(40, int(y))

# Render Cliff Body with natural rock strata, ledges and vertical joints
for y in range(40, 128):
    x_edge = get_cliff_edge_x(y)
    for x in range(max(0, x_edge), 128):
        if x >= 80 and y < get_cliff_plateau_y(x):
            continue
            
        dist_from_edge = x - x_edge
        
        # Sedimentary rock layers & fracture joints:
        # Strata layer thickness: ~8 pixels
        stratum = (y // 8) % 2
        # Vertical joint fractures: 3 natural jagged fissures
        j1 = 88 + int(math.sin(y * 0.15) * 1.5)
        j2 = 103 + int(math.cos(y * 0.12) * 2.0)
        j3 = 118 + int(math.sin(y * 0.2) * 1.5)
        is_joint = (x == j1 or x == j2 or x == j3)
        
        # Base rock color
        if is_joint:
            col = ROCK_BLACK
        elif stratum == 0:
            col = ROCK_DARK
        else:
            col = ROCK_MID if ((x + y) % 3 == 0) else ROCK_LIGHT
            
        # Left-facing seaward crags catch brilliant sunset rim lighting!
        if dist_from_edge == 0:
            col = RIM_AMBER if y < 75 else RIM_ORANGE
        elif dist_from_edge == 1:
            col = RIM_ORANGE if y < 75 else RIM_RUST
        elif dist_from_edge == 2:
            col = RIM_RUST if y < 75 else RIM_RED
        elif dist_from_edge <= 4:
            col = RIM_RED if y < 75 else RIM_DARK
        elif dist_from_edge <= 6 and y < 75:
            col = RIM_DARK
            
        # Natural horizontal shelf ledges at Y=54, Y=76, Y=90
        if y in [54, 76, 90] and dist_from_edge < 10:
            col = RIM_ORANGE if dist_from_edge < 3 else RIM_RUST
        elif y in [55, 77, 91] and dist_from_edge < 10:
            col = ROCK_BLACK
            
        # Plateau hardy grass & moss
        if x >= 80 and y == get_cliff_plateau_y(x):
            col = MOSS_LIT if dist_from_edge < 4 else MOSS_MID
        elif x >= 80 and y == get_cliff_plateau_y(x) + 1 and dist_from_edge > 3:
            col = MOSS_DARK
            
        c.set(x, y, col)

# Sea foam & crashing surf at the foot of the sea cliff (Y=96 to 110)
for y in range(96, 112):
    x_base = get_cliff_edge_x(y)
    for x in range(x_base - 8, x_base + 3):
        if 0 <= x < 128:
            dist_to_rock = abs(x - x_base)
            spray_noise = (x * 7 + y * 13) % 9
            if spray_noise > 2:
                if dist_to_rock <= 1:
                    c.set(x, y, SEA_WHITE)
                elif dist_to_rock <= 3:
                    c.set(x, y, SEA_SPRAY)
                elif dist_to_rock <= 6:
                    c.set(x, y, SEA_FOAM)

# =============================================================================
# 6. CASTLE ON THE CLIFF
# =============================================================================

# Connecting Curtain Wall: X=92 to 106
for x in range(92, 107):
    is_merlon = (x % 3 != 1)
    wall_top = 33 if is_merlon else 35
    y_base = get_cliff_plateau_y(x)
    for y in range(wall_top, y_base):
        col = ROCK_MID
        if y % 3 == 0:
            col = ROCK_DARK
        elif (x + y * 2) % 4 == 0:
            col = ROCK_LIGHT
        if x == 92:  # rim light
            col = RIM_RUST
        c.set(x, y, col)

# Palace roof behind curtain wall
for x in range(94, 105):
    for y in range(28, 34):
        col = ROOF_MID
        if (x + y) % 3 == 0:
            col = ROOF_DARK
        if x == 94:
            col = RIM_ORANGE
        c.set(x, y, col)

# Central palace dormer / turret
for x in range(97, 101):
    for y in range(23, 29):
        c.set(x, y, ROCK_MID if x > 97 else RIM_RUST)
    c.set(x, 22, ROOF_MID)
c.set(98, 21, ROOF_MID)
c.set(99, 21, ROOF_DARK)
c.set(98, 20, RIM_ORANGE)
# Warm window in central turret
c.set(98, 25, SUN_LIT)
c.set(99, 25, SKY_7)

# Warm glowing window in the curtain wall at X=98..100, Y=37..40
for wy in range(38, 41):
    c.set(98, wy, SUN_LIT)
    c.set(99, wy, SUN_LIT)
c.set(98, 37, SUN_LIT)
c.set(99, 37, SUN_LIT)
c.set(98, 39, WIN_MULLION)

# -------------------------------------------------------------
# LEFT TOWER (Outer Seaward Watchtower): X=80 to 92
# -------------------------------------------------------------
lt_left, lt_right = 80, 92

# Tower Shaft: Y=25 to plateau
for x in range(lt_left, lt_right + 1):
    for y in range(25, get_cliff_plateau_y(x)):
        col = ROCK_MID
        if y % 3 == 0:
            col = ROCK_DARK
        elif (x + y * 2) % 5 == 0:
            col = ROCK_LIGHT
            
        if x == lt_left:
            col = RIM_AMBER
        elif x == lt_left + 1:
            col = RIM_ORANGE
        elif x == lt_left + 2:
            col = RIM_RUST
        elif x == lt_left + 3:
            col = RIM_RED
        c.set(x, y, col)

# Machicolation / Parapet: Y=22 to 25 (flared X=79 to 93)
for x in range(lt_left - 1, lt_right + 2):
    c.set(x, 24, ROCK_DARK)
    c.set(x, 25, ROCK_LIGHT if (x % 2 == 0) else ROCK_MID)
    if x == lt_left - 1:
        c.set(x, 24, RIM_AMBER)
        c.set(x, 25, RIM_ORANGE)
    if (x - 79) % 3 != 1:
        c.set(x, 22, RIM_AMBER if x == lt_left - 1 else ROCK_LIGHT)
        c.set(x, 23, RIM_ORANGE if x == lt_left - 1 else ROCK_MID)

# Conical Spire Roof: Apex at (86, 9), Base at Y=22 (X=78 to 94)
lt_apex_x, lt_apex_y = 86, 9
for y in range(lt_apex_y, 23):
    prog = (y - lt_apex_y) / 14.0
    w = int(prog * 8)
    for x in range(lt_apex_x - w, lt_apex_x + w + 1):
        col = ROOF_MID
        if (x + y) % 3 == 0:
            col = ROOF_DARK
        if x == lt_apex_x - w:
            col = RIM_AMBER
        elif x == lt_apex_x - w + 1:
            col = RIM_ORANGE
        c.set(x, y, col)

# Flagpole on Left Tower: X=86, Y=4 to 9
for y in range(4, 10):
    c.set(lt_apex_x, y, SKY_8 if y <= 6 else ROCK_LIGHT)

# FLAG 1: Fluttering swallowtail pennant streaming left in the sea wind!
flag1 = [
    # Top edge
    (85, 5, FLAG_BRIGHT), (84, 5, FLAG_BRIGHT), (83, 5, FLAG_BRIGHT), (82, 5, FLAG_BRIGHT),
    (81, 6, FLAG_BRIGHT), (80, 6, FLAG_BRIGHT), (79, 6, FLAG_BRIGHT), (78, 6, FLAG_BRIGHT),
    (77, 7, FLAG_BRIGHT), (76, 7, FLAG_BRIGHT), (75, 7, FLAG_BRIGHT), (74, 8, FLAG_BRIGHT),
    (73, 8, FLAG_BRIGHT), (72, 8, FLAG_BRIGHT),
    # Body with gold heraldic stripe
    (85, 6, FLAG_RED), (84, 6, SKY_8), (83, 6, FLAG_RED), (82, 6, FLAG_RED),
    (81, 7, FLAG_RED), (80, 7, SKY_8), (79, 7, FLAG_RED), (78, 7, FLAG_RED),
    (77, 8, FLAG_RED), (76, 8, FLAG_RED), (75, 8, FLAG_RED), (74, 9, FLAG_RED),
    # Bottom edge and swallowtail fork
    (85, 7, FLAG_DARK), (84, 7, FLAG_DARK), (83, 7, FLAG_DARK), (82, 7, FLAG_DARK),
    (81, 8, FLAG_DARK), (80, 8, FLAG_DARK), (79, 8, FLAG_DARK),
    # Fork tips
    (72, 7, FLAG_BRIGHT), (71, 6, FLAG_BRIGHT),
    (73, 9, FLAG_DARK), (72, 10, FLAG_DARK),
]
for fx, fy, fcol in flag1:
    c.set(fx, fy, fcol)

# Left Tower Arched Window with glowing light
for wy in range(32, 38):
    for wx in range(84, 88):
        c.set(wx, wy, SUN_LIT)
c.set(85, 31, SUN_LIT)
c.set(86, 31, SUN_LIT)
for wy in range(32, 38):
    c.set(85, wy, WIN_MULLION)
c.rect(84, 34, 4, 1, WIN_MULLION)
c.set(83, 34, RIM_ORANGE)
c.set(88, 34, RIM_DARK)

# -------------------------------------------------------------
# RIGHT TOWER (High Keep / Grand Tower): X=106 to 124
# -------------------------------------------------------------
rt_left, rt_right = 106, 124

# Tower Shaft: Y=17 to plateau
for x in range(rt_left, rt_right + 1):
    for y in range(17, get_cliff_plateau_y(x)):
        col = ROCK_MID
        if y % 3 == 0:
            col = ROCK_DARK
        elif (x + y * 2) % 5 == 0:
            col = ROCK_LIGHT
            
        if x == rt_left:
            col = RIM_AMBER
        elif x == rt_left + 1:
            col = RIM_ORANGE
        elif x == rt_left + 2:
            col = RIM_RUST
        elif x == rt_left + 3:
            col = RIM_RED
        c.set(x, y, col)

# Battlement Gallery: Y=14 to 17 (flared X=104 to 126)
for x in range(rt_left - 2, rt_right + 3):
    c.set(x, 16, ROCK_DARK)
    c.set(x, 17, ROCK_LIGHT if (x % 2 == 0) else ROCK_MID)
    if x == rt_left - 2:
        c.set(x, 16, RIM_AMBER)
        c.set(x, 17, RIM_ORANGE)
    if (x - 104) % 3 != 1:
        c.set(x, 14, RIM_AMBER if x == rt_left - 2 else ROCK_LIGHT)
        c.set(x, 15, RIM_ORANGE if x == rt_left - 2 else ROCK_MID)

# High Grand Conical Spire: Apex at (115, 1), Base at Y=14 (X=103 to 127)
rt_apex_x, rt_apex_y = 115, 1
for y in range(rt_apex_y, 15):
    prog = (y - rt_apex_y) / 14.0
    w = int(prog * 12)
    for x in range(rt_apex_x - w, rt_apex_x + w + 1):
        if x < 128:
            col = ROOF_MID
            if (x + y) % 3 == 0:
                col = ROOF_DARK
            if x == rt_apex_x - w:
                col = RIM_AMBER
            elif x == rt_apex_x - w + 1:
                col = RIM_ORANGE
            c.set(x, y, col)

# Flagpole on Right Tower: X=115, Y=0 to 2
c.set(rt_apex_x, 0, SKY_8)
c.set(rt_apex_x, 1, SKY_8)
c.set(rt_apex_x, 2, ROCK_LIGHT)

# FLAG 2: Royal standard streaming left into the sunset sky!
flag2 = [
    (114, 0, FLAG_BRIGHT), (113, 0, FLAG_BRIGHT), (112, 0, FLAG_BRIGHT), (111, 0, FLAG_BRIGHT),
    (110, 1, FLAG_BRIGHT), (109, 1, FLAG_BRIGHT), (108, 1, FLAG_BRIGHT), (107, 1, FLAG_BRIGHT),
    (106, 2, FLAG_BRIGHT), (105, 2, FLAG_BRIGHT), (104, 2, FLAG_BRIGHT), (103, 2, FLAG_BRIGHT),
    (102, 3, FLAG_BRIGHT), (101, 3, FLAG_BRIGHT), (100, 3, FLAG_BRIGHT), (99, 4, FLAG_BRIGHT),
    (98, 4, FLAG_BRIGHT), (97, 4, FLAG_BRIGHT),
    (114, 1, FLAG_RED), (113, 1, SKY_8), (112, 1, FLAG_RED), (111, 1, FLAG_RED),
    (110, 2, FLAG_RED), (109, 2, SKY_8), (108, 2, FLAG_RED), (107, 2, FLAG_RED),
    (106, 3, FLAG_RED), (105, 3, SKY_8), (104, 3, FLAG_RED), (103, 3, FLAG_RED),
    (102, 4, FLAG_RED), (101, 4, FLAG_RED), (100, 4, FLAG_RED), (99, 5, FLAG_RED),
    (114, 2, FLAG_DARK), (113, 2, FLAG_DARK), (112, 2, FLAG_DARK), (111, 2, FLAG_DARK),
    (110, 3, FLAG_DARK), (109, 3, FLAG_DARK), (108, 3, FLAG_DARK), (107, 3, FLAG_DARK),
    (106, 4, FLAG_DARK), (105, 4, FLAG_DARK), (104, 4, FLAG_DARK), (103, 4, FLAG_DARK),
    (96, 3, FLAG_BRIGHT), (95, 3, FLAG_BRIGHT),
    (97, 5, FLAG_DARK), (96, 6, FLAG_DARK),
]
for fx, fy, fcol in flag2:
    c.set(fx, fy, fcol)

# Right Tower Windows
# Grand High Arched Double Window: X=112..118, Y=23..29
for wy in range(24, 30):
    for wx in range(112, 119):
        c.set(wx, wy, SUN_LIT)
c.set(113, 23, SUN_LIT)
c.set(114, 23, SUN_LIT)
c.set(115, 23, SUN_LIT)
c.set(116, 23, SUN_LIT)
c.set(117, 23, SUN_LIT)
for wy in range(23, 30):
    c.set(115, wy, WIN_MULLION)
c.rect(112, 26, 7, 1, WIN_MULLION)
c.set(111, 26, RIM_ORANGE)
c.set(119, 26, RIM_DARK)

# Lower arrow-slit window: X=114..116, Y=35..39
for wy in range(36, 40):
    c.set(115, wy, SUN_LIT)
c.set(114, 37, SKY_7)

# =============================================================================
# 7. FOREGROUND DARK ROCKS & SURF
# =============================================================================
# Left Foreground Sea Stack Crags: X=0 to 36, rising to peak at X=14, Y=92
def fg_rock_left_y(x):
    if x > 36:
        return 999
    y = 92 + int(((x - 14) / 18.0) ** 2 * 30)
    y += int(math.sin(x * 0.7) * 2.5)
    return min(128, max(90, y))

for x in range(37):
    y_top = fg_rock_left_y(x)
    for y in range(y_top, 128):
        facet = (x * 3 + y * 2) % 13
        if facet == 0:
            col = ROCK_BLACK
        elif facet > 8:
            col = ROCK_MID
        else:
            col = ROCK_DARK
            
        # Top and right rim light from sunset
        if y == y_top:
            col = RIM_ORANGE if x < 22 else RIM_RUST
        elif y == y_top + 1:
            col = RIM_RUST if x < 22 else RIM_RED
        elif x >= 34 or (x > 28 and y < y_top + 4):
            col = RIM_RED
            
        c.set(x, y, col)

# Foamy surf and sea spray swirling around the base of left rocks
for y in range(116, 126):
    is_foam_row = (y % 2 == 0)
    if is_foam_row:
        for x in range(28, 44):
            dist_rock = abs(x - 36)
            if dist_rock < 7:
                p = (x * 7 + y * 13) % 9
                if p > 2:
                    c.set(x, y, SEA_WHITE if p > 6 else (SEA_SPRAY if p > 4 else SEA_FOAM))

# Right Foreground Rock Outcrop: X=98 to 127, Y=114 to 127
def fg_rock_right_y(x):
    if x < 98:
        return 999
    y = 114 + int(math.sin(x * 0.4) * 2.0) - int((x - 98) * 0.1)
    return min(128, max(112, y))

for x in range(98, 128):
    y_top = fg_rock_right_y(x)
    for y in range(y_top, 128):
        facet = (x * 2 + y * 3) % 11
        col = ROCK_BLACK if facet == 0 else (ROCK_MID if facet > 7 else ROCK_DARK)
        if y == y_top:
            col = RIM_RED if x < 112 else RIM_DARK
        elif y == y_top + 1:
            col = RIM_DARK
        c.set(x, y, col)

# Surf breaking on right rocks
for y in [114, 116, 118]:
    for x in range(94, 106):
        dist = abs(x - 98)
        if dist < 6:
            p = (x * 5 + y * 7) % 7
            if p > 2:
                c.set(x, y, SEA_WHITE if p > 5 else (SEA_SPRAY if p > 3 else SEA_FOAM))

# =============================================================================
# 8. DISTANT BIRDS (Fantasy RPG opening flight towards sunset)
# =============================================================================
birds = [
    (18, 36),
    (24, 33),
    (30, 30),
    (35, 34),
    (41, 31),
]
for bx, by in birds:
    c.set(bx - 2, by - 1, CLD_MID)
    c.set(bx - 1, by, CLD_DARK)
    c.set(bx, by + 1, ROCK_BLACK)
    c.set(bx + 1, by, CLD_DARK)
    c.set(bx + 2, by - 1, CLD_MID)

print(c.stats_text())
finish(c)
view(c)
