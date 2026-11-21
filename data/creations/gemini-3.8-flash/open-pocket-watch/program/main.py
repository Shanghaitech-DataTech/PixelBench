import math
from pixelbench_api import new_canvas, view, finish

# Palette Definition (Strictly controlled, 42 colors, well below 86 limit)
P = {
    # Background & Surface
    "BG0": "#07090e",       # Deepest midnight vignette
    "BG1": "#0c0f16",       # Dark navy charcoal
    "BG2": "#131722",       # Deep slate
    "BG3": "#1a202e",       # Ambient slate surface
    "BG_LGT": "#232a3d",    # Ambient light wash
    "SHADOW": "#040508",    # Deep drop shadow

    # Gold Ramp (Rich metallic brass & gold)
    "G_BLACK": "#1b1104",   # Deepest crevice / gear tooth root shadow
    "G_SHADOW2": "#321f08", # Deep golden brown shadow
    "G_SHADOW1": "#4c320d", # Warm shadow gold
    "G_DULL": "#6c4814",    # Muted antique gold
    "G_BASE": "#92621c",    # Solid rich gold
    "G_MID": "#b68126",     # Warm polished gold
    "G_LIGHT": "#d7a136",   # Bright lustrous gold
    "G_HI": "#ecc04e",      # Glistening gold highlight
    "G_PALE": "#f8dc7e",    # Pale specular gold
    "G_WHITE": "#fff8db",   # Near-white specular gleam

    # White Metal / Steel (Pinions, click spring, escapement)
    "S_DARK": "#181d26",    # Steel shadow
    "S_MID": "#363e4d",     # Medium steel
    "S_LIGHT": "#6b778c",   # Polished steel
    "S_HI": "#afbccd",      # Bright steel highlight
    "WHITE": "#ffffff",     # Pure specular glint

    # Blued Steel (Heat-blued horology screws & Breguet hands)
    "B_BLACK": "#080d19",   # Deepest blued steel / slot
    "B_DARK": "#0e1a30",    # Dark royal blue
    "B_MID": "#173462",     # Rich cobalt blue
    "B_LIGHT": "#26549c",   # Vibrant heat-blued steel
    "B_HI": "#4f88de",      # Bright blue reflection
    "B_PALE": "#91baee",    # Specular blue sheen

    # Chapter Ring (Dial Enamel)
    "D_DARK": "#544c3f",    # Dial shadow border
    "D_MID": "#807462",     # Muted ivory shadow
    "D_LIGHT": "#aea391",   # Soft cream
    "D_CREAM": "#d3c9b7",   # Warm cream enamel
    "D_WHITE": "#ede7dc",   # Bright enamel
    "D_BRIGHT": "#fcf9f2",  # Specular dial highlight
    "D_TICK": "#120f0b",    # Crisp tick mark

    # Synthetic Ruby Jewels
    "R_DARK": "#36030f",    # Ruby setting shadow
    "R_MID": "#6e0820",     # Deep ruby red
    "R_BRIGHT": "#b80e38",  # Radiant ruby magenta
    "R_HI": "#f2426c",      # Ruby facet highlight
}

c = new_canvas(64, 64, name="watch")

fb = [[P["BG0"] for _ in range(64)] for _ in range(64)]

def set_p(x, y, color):
    if 0 <= x < 64 and 0 <= y < 64:
        fb[y][x] = color

def get_p(x, y):
    if 0 <= x < 64 and 0 <= y < 64:
        return fb[y][x]
    return P["BG0"]

# -------------------------------------------------------------
# 1. Background & Atmospheric Ambient Lighting
# -------------------------------------------------------------
for y in range(64):
    for x in range(64):
        dist = math.hypot(x - 37, y - 34)
        diag = (x * 0.4 + y * 0.3)
        eff_dist = dist + diag * 0.25
        
        if eff_dist < 20:
            col = P["BG3"]
        elif eff_dist < 28:
            col = P["BG2"]
        elif eff_dist < 38:
            col = P["BG1"]
        else:
            col = P["BG0"]
        fb[y][x] = col

# Top-left ambient illumination
for y in range(25):
    for x in range(25):
        if x + y < 24 and fb[y][x] in [P["BG2"], P["BG1"]]:
            fb[y][x] = P["BG3"]

# Cast Dropshadows (directional offset dx=+3, dy=+3)
# Watch body shadow
for y in range(16, 58):
    for x in range(20, 61):
        if math.hypot(x - 40, y - 37) <= 19.5:
            fb[y][x] = P["SHADOW"]

# Lid shadow
for y in range(17, 56):
    for x in range(2, 23):
        if (((x - 13) / 8.5) ** 2 + ((y - 37) / 18.0) ** 2) <= 1.0:
            fb[y][x] = P["SHADOW"]

# -------------------------------------------------------------
# 2. Watch Chain (Interconnected Golden Curb Links)
# -------------------------------------------------------------
chain_links = [
    (43, 7, 'h'),
    (46, 8, 'v'),
    (49, 10, 'h'),
    (52, 13, 'v'),
    (55, 17, 'h'),
    (57, 21, 'v'),
    (59, 26, 'h'),
    (60, 31, 'v'),
    (61, 37, 'h'),
    (60, 43, 'v'),
    (59, 48, 'h'),
    (57, 53, 'v'),
    (54, 57, 'h'),
    (50, 60, 'v'),
    (45, 62, 'h')
]

# Draw chain cast shadow
for cx, cy, ori in chain_links:
    for ox, oy in [(1, 2), (2, 2), (2, 3)]:
        set_p(cx + ox, cy + oy, P["SHADOW"])

# Draw interlocking curb links
for i, (cx, cy, ori) in enumerate(chain_links):
    if ori == 'h':
        # Horizontal oval link (3x2)
        set_p(cx - 1, cy - 1, P["G_PALE"])
        set_p(cx,     cy - 1, P["G_WHITE"])
        set_p(cx + 1, cy - 1, P["G_HI"])
        set_p(cx - 1, cy,     P["G_LIGHT"])
        set_p(cx,     cy,     P["BG0"])      # hollow center
        set_p(cx + 1, cy,     P["G_MID"])
        set_p(cx - 1, cy + 1, P["G_BASE"])
        set_p(cx,     cy + 1, P["G_SHADOW1"])
        set_p(cx + 1, cy + 1, P["G_SHADOW2"])
    else:
        # Vertical oval link (2x3)
        set_p(cx - 1, cy - 1, P["G_WHITE"])
        set_p(cx,     cy - 1, P["G_PALE"])
        set_p(cx - 1, cy,     P["G_HI"])
        set_p(cx,     cy,     P["BG0"])      # hollow center
        set_p(cx + 1, cy,     P["G_MID"])
        set_p(cx - 1, cy + 1, P["G_LIGHT"])
        set_p(cx,     cy + 1, P["G_BASE"])
        set_p(cx + 1, cy + 1, P["G_SHADOW1"])

# Swivel connector ring at bow
set_p(41, 6, P["G_WHITE"])
set_p(42, 6, P["G_HI"])
set_p(41, 7, P["G_MID"])

# -------------------------------------------------------------
# 3. Open Lid (Hunter Case Front Cover)
# -------------------------------------------------------------
for y in range(16, 53):
    for x in range(2, 19):
        norm_x = (x - 10) / 8.0
        norm_y = (y - 34) / 18.0
        d2 = norm_x * norm_x + norm_y * norm_y
        
        if d2 <= 1.05:
            # 1. Outer Gold Bezel Rim (d2 >= 0.78)
            if d2 >= 0.78:
                if norm_y < -0.4:
                    if norm_x < 0:
                        col = P["G_WHITE"] if y <= 20 else P["G_PALE"]
                    else:
                        col = P["G_HI"]
                elif norm_y > 0.4:
                    if norm_x < 0:
                        col = P["G_BASE"]
                    else:
                        col = P["G_SHADOW1"] if y >= 48 else P["G_DULL"]
                elif norm_x < -0.6:
                    col = P["G_PALE"] if y < 34 else P["G_LIGHT"]
                else:
                    col = P["G_MID"]
            
            # 2. Inner Concave Gold Dish (d2 < 0.78)
            else:
                dist_center = math.sqrt(d2)
                is_groove = (0.42 <= dist_center <= 0.52)
                is_center = (dist_center <= 0.20)
                
                concave_val = 0.65 * norm_x + 0.65 * norm_y
                
                if is_center:
                    col = P["G_PALE"] if concave_val > 0 else P["G_MID"]
                    if x == 10 and y == 34:
                        col = P["G_WHITE"]
                elif is_groove:
                    if concave_val > 0.1:
                        col = P["G_WHITE"] if concave_val > 0.4 else P["G_HI"]
                    else:
                        col = P["G_DULL"]
                else:
                    if concave_val > 0.45:
                        col = P["G_PALE"]
                    elif concave_val > 0.2:
                        col = P["G_HI"]
                    elif concave_val > -0.05:
                        col = P["G_LIGHT"]
                    elif concave_val > -0.3:
                        col = P["G_MID"]
                    elif concave_val > -0.55:
                        col = P["G_BASE"]
                    elif concave_val > -0.75:
                        col = P["G_SHADOW1"]
                    else:
                        col = P["G_SHADOW2"]
                
                refl_axis = norm_x * 1.1 - norm_y * 0.9
                if abs(refl_axis - 0.15) < 0.18 and d2 < 0.70:
                    if col in [P["G_LIGHT"], P["G_MID"]]:
                        col = P["G_HI"]
                    elif col == P["G_HI"]:
                        col = P["G_PALE"]
                    elif col == P["G_PALE"]:
                        col = P["G_WHITE"]
            
            set_p(x, y, col)

# Continuous highlight along top-left rim of lid
set_p(3, 20, P["G_PALE"])
set_p(4, 19, P["G_WHITE"])
set_p(5, 18, P["WHITE"])
set_p(6, 17, P["WHITE"])
set_p(7, 17, P["G_WHITE"])

# Lid Spring Catch at (1..2, 33..35)
set_p(1, 33, P["G_PALE"])
set_p(1, 34, P["WHITE"])
set_p(1, 35, P["G_LIGHT"])
set_p(2, 33, P["G_WHITE"])
set_p(2, 34, P["WHITE"])
set_p(2, 35, P["G_MID"])

# Hinge mechanism at x=17..19, y=32..36 (Three-knuckle gold hinge)
set_p(17, 32, P["G_HI"])
set_p(18, 32, P["G_WHITE"])
set_p(19, 32, P["G_LIGHT"])

set_p(17, 33, P["G_BLACK"])
set_p(18, 33, P["G_SHADOW2"])
set_p(19, 33, P["G_SHADOW1"])

set_p(17, 34, P["G_WHITE"])
set_p(18, 34, P["WHITE"])
set_p(19, 34, P["G_HI"])

set_p(17, 35, P["G_BLACK"])
set_p(18, 35, P["G_SHADOW2"])
set_p(19, 35, P["G_SHADOW1"])

set_p(17, 36, P["G_LIGHT"])
set_p(18, 36, P["G_HI"])
set_p(19, 36, P["G_BASE"])

# -------------------------------------------------------------
# 4. Watch Case Body, Pendant, Crown, and Bow
# -------------------------------------------------------------
CX, CY = 37, 34
R_CASE = 19.3

# Pendant Neck (x=35..39, y=12..15)
for y in range(12, 16):
    for x in range(35, 40):
        if x == 36:
            col = P["G_WHITE"] if y == 12 else P["G_PALE"]
        elif x == 37:
            col = P["G_HI"]
        elif x == 35:
            col = P["G_LIGHT"]
        elif x == 38:
            col = P["G_MID"]
        else:
            col = P["G_SHADOW1"]
        set_p(x, y, col)

# Winding Crown (Knurled knob at x=34..40, y=8..11)
crown_fluting = [
    P["G_DULL"],     # 34
    P["G_HI"],       # 35
    P["G_BASE"],     # 36
    P["G_WHITE"],    # 37
    P["G_MID"],      # 38
    P["G_LIGHT"],    # 39
    P["G_SHADOW2"]   # 40
]
for y in range(8, 12):
    for x in range(34, 41):
        col = crown_fluting[x - 34]
        if y == 8:
            if x in [36, 37]: col = P["WHITE"]
            elif x in [35, 38]: col = P["G_PALE"]
        set_p(x, y, col)

# Crown Push-Button (Hunter case release at top, x=36..38, y=6..7)
set_p(36, 7, P["G_LIGHT"])
set_p(37, 7, P["WHITE"])
set_p(38, 7, P["G_MID"])
set_p(36, 6, P["G_BASE"])
set_p(37, 6, P["G_WHITE"])
set_p(38, 6, P["G_SHADOW1"])

# Bow (Pendant Ring around Crown)
bow_pts = [
    (33, 13, P["G_BASE"]), (32, 12, P["G_MID"]), (32, 11, P["G_LIGHT"]),
    (31, 10, P["G_LIGHT"]), (32, 10, P["G_HI"]),
    (31, 8, P["G_HI"]), (32, 8, P["G_PALE"]),
    (32, 6, P["G_PALE"]), (33, 6, P["G_WHITE"]),
    (33, 5, P["G_WHITE"]), (34, 5, P["G_WHITE"]),
    (34, 4, P["WHITE"]), (35, 4, P["WHITE"]),
    (36, 3, P["WHITE"]), (37, 3, P["WHITE"]), (38, 3, P["G_WHITE"]),
    (39, 4, P["G_PALE"]), (40, 4, P["G_HI"]),
    (40, 5, P["G_HI"]), (41, 5, P["G_MID"]),
    (41, 7, P["G_MID"]), (42, 7, P["G_LIGHT"]),
    (42, 9, P["G_BASE"]), (43, 9, P["G_MID"]),
    (42, 11, P["G_SHADOW1"]), (43, 11, P["G_BASE"]),
    (41, 12, P["G_SHADOW1"]), (41, 13, P["G_DULL"]),
]
for bx, by, bcol in bow_pts:
    set_p(bx, by, bcol)

# Watch Case Outer Bezel & Chamfer (CX=37, CY=34)
for y in range(14, 55):
    for x in range(17, 58):
        dist = math.hypot(x - CX, y - CY)
        if dist <= R_CASE:
            angle = math.atan2(y - CY, x - CX)
            light_fac = -math.cos(angle + math.pi * 0.25)
            
            # 1. Outer Bezel (dist >= 17.6)
            if dist >= 17.6:
                if light_fac > 0.65:
                    col = P["WHITE"] if dist < 18.7 else P["G_WHITE"]
                elif light_fac > 0.25:
                    col = P["G_PALE"] if dist < 18.7 else P["G_HI"]
                elif light_fac > -0.2:
                    col = P["G_HI"] if dist < 18.7 else P["G_LIGHT"]
                elif light_fac > -0.6:
                    col = P["G_BASE"]
                elif light_fac > -0.85:
                    col = P["G_SHADOW1"]
                else:
                    col = P["G_SHADOW2"]
                
                # Bottom-right rim specular bounce
                if dist >= 18.4 and 0.4 < angle < 1.2:
                    col = P["G_MID"]

            # 2. Bevelled Chamfer (dist 16.2 to 17.6)
            elif dist >= 16.2:
                if light_fac > 0.35:
                    col = P["G_SHADOW1"]
                elif light_fac < -0.3:
                    col = P["G_HI"]
                else:
                    col = P["G_MID"]
            
            # 3. Chapter Ring / Dial (dist 13.6 to 16.2)
            elif dist >= 13.6:
                dial_light = -math.cos(angle + math.pi * 0.25)
                if dial_light > 0.4:
                    col = P["D_BRIGHT"]
                elif dial_light > 0.0:
                    col = P["D_WHITE"]
                elif dial_light > -0.4:
                    col = P["D_CREAM"]
                else:
                    col = P["D_LIGHT"]
                
                if dist >= 15.8:
                    col = P["G_BASE"]
                elif dist <= 13.9:
                    col = P["G_MID"]
            
            # 4. Movement Interior (dist < 13.6)
            else:
                col = P["G_SHADOW2"]
            
            set_p(x, y, col)

# Dial Chapter Ring Tick Marks (12 Hour Marks & Minute Dots)
hour_ticks = [
    [(37, 19), (37, 20)],
    [(44, 21), (44, 22)],
    [(49, 26), (50, 27)],
    [(51, 34), (52, 34)],
    [(49, 41), (50, 42)],
    [(44, 46), (44, 47)],
    [(37, 48), (37, 49)],
    [(30, 46), (30, 47)],
    [(24, 41), (25, 42)],
    [(22, 34), (23, 34)],
    [(24, 26), (25, 27)],
    [(30, 21), (30, 22)]
]
for tick in hour_ticks:
    for tx, ty in tick:
        set_p(tx, ty, P["D_TICK"])

for minute in range(60):
    if minute % 5 != 0:
        ang = minute * (math.pi * 2 / 60) - (math.pi / 2)
        mx = int(round(CX + 14.8 * math.cos(ang)))
        my = int(round(CY + 14.8 * math.sin(ang)))
        if 13.8 <= math.hypot(mx - CX, my - CY) <= 15.6:
            set_p(mx, my, P["D_DARK"])

# -------------------------------------------------------------
# 5. Golden Movement Baseplate & Cutaways
# -------------------------------------------------------------
for y in range(21, 48):
    for x in range(24, 51):
        d = math.hypot(x - CX, y - CY)
        if d < 13.6:
            grain = (x * 2 + y * 3) % 4
            if grain == 0:
                base_col = P["G_MID"]
            elif grain == 1:
                base_col = P["G_BASE"]
            elif grain == 2:
                base_col = P["G_DULL"]
            else:
                base_col = P["G_SHADOW1"]
            set_p(x, y, base_col)

# Cutaway shadow cavities beneath gears
for y in range(37, 44):
    for x in range(41, 48):
        if math.hypot(x - 44, y - 41) < 3.5:
            set_p(x, y, P["G_BLACK"])

for y in range(37, 44):
    for x in range(27, 35):
        if math.hypot(x - 31, y - 41) < 3.2:
            set_p(x, y, P["G_BLACK"])

for y in range(23, 28):
    for x in range(39, 45):
        if math.hypot(x - 42, y - 26) < 2.8:
            set_p(x, y, P["G_BLACK"])

for y in range(30, 36):
    for x in range(26, 32):
        if math.hypot(x - 29, y - 33) < 2.8:
            set_p(x, y, P["G_BLACK"])

# -------------------------------------------------------------
# 6. Intricate Golden Bridges (Anglage & Screws)
# -------------------------------------------------------------
barrel_bridge = [
    (34, 22), (35, 22), (36, 22), (37, 22), (38, 22), (39, 22), (40, 22), (41, 22), (42, 22), (43, 22),
    (34, 23), (35, 23), (36, 23), (37, 23), (38, 23), (39, 23), (40, 23), (41, 23), (42, 23), (43, 23), (44, 23),
    (43, 24), (44, 24), (45, 24), (45, 25), (46, 25), (46, 26),
    (45, 27), (46, 27), (45, 28)
]
for bx, by in barrel_bridge:
    if math.hypot(bx - CX, by - CY) < 13.2:
        set_p(bx, by, P["G_LIGHT"])
for bx, by in [(34, 22), (35, 22), (36, 22), (37, 22), (38, 22), (39, 22), (40, 22), (41, 22), (42, 22), (43, 22), (44, 23), (45, 24), (46, 25)]:
    set_p(bx, by, P["G_WHITE"])

train_bridge = [
    (26, 26), (27, 26), (28, 27), (29, 27), (30, 28),
    (25, 27), (26, 27), (27, 27), (28, 28), (29, 28), (30, 29),
    (25, 28), (26, 28), (27, 28), (28, 29),
    (25, 29), (26, 29), (27, 29), (28, 30),
    (26, 30), (27, 30), (28, 31)
]
for bx, by in train_bridge:
    if math.hypot(bx - CX, by - CY) < 13.2:
        set_p(bx, by, P["G_MID"])
for bx, by in [(26, 26), (27, 26), (28, 27), (29, 27), (30, 28)]:
    set_p(bx, by, P["G_PALE"])

balance_cock = [
    (48, 38), (47, 38), (46, 38), (45, 38),
    (48, 39), (47, 39), (46, 39), (45, 39), (44, 39),
    (48, 40), (47, 40), (46, 40), (45, 40), (44, 40), (43, 40),
    (47, 41), (46, 41), (45, 41), (44, 41), (43, 41), (42, 41),
    (46, 42), (45, 42), (44, 42)
]
for bx, by in balance_cock:
    if math.hypot(bx - CX, by - CY) < 13.2:
        set_p(bx, by, P["G_LIGHT"])
for bx, by in [(48, 38), (47, 38), (46, 38), (45, 38), (44, 39), (43, 39), (42, 40)]:
    set_p(bx, by, P["G_WHITE"])

# -------------------------------------------------------------
# 7. Intricate Meshing Gears
# -------------------------------------------------------------
# GEAR 0: Winding Intermediate Gear (Upper-Left, Center (29, 24), Radius 3.5)
for dy in range(-4, 5):
    for dx in range(-4, 5):
        dist = math.hypot(dx, dy)
        px = 29 + dx
        py = 24 + dy
        if math.hypot(px - CX, py - CY) < 13.2 and dist <= 3.6:
            ang = math.atan2(dy, dx)
            tooth = math.cos(ang * 10)
            if dist >= 2.6:
                if tooth > 0.2:
                    set_p(px, py, P["G_PALE"] if dy < 0 else P["G_HI"])
                else:
                    set_p(px, py, P["G_BLACK"])
            elif dist <= 1.0:
                set_p(px, py, P["S_MID"])
            else:
                set_p(px, py, P["G_MID"])

# GEAR 1: Mainspring Barrel / Great Wheel (Upper-Right, Center (41, 26), Radius 5.2)
for dy in range(-5, 6):
    for dx in range(-5, 6):
        dist = math.hypot(dx, dy)
        px = 41 + dx
        py = 26 + dy
        if math.hypot(px - CX, py - CY) < 13.2 and dist <= 5.4:
            ang = math.atan2(dy, dx)
            tooth = math.cos(ang * 14)
            if dist >= 4.4:
                if tooth > 0.2:
                    set_p(px, py, P["G_PALE"] if dy < 0 else P["G_HI"])
                else:
                    set_p(px, py, P["G_BLACK"])
            elif dist <= 1.4:
                set_p(px, py, P["S_MID"])
            else:
                if int(dist * 2) % 2 == 0:
                    set_p(px, py, P["G_LIGHT"])
                else:
                    set_p(px, py, P["G_MID"])

# Steel ratchet click in center of barrel
set_p(41, 26, P["S_HI"])
set_p(40, 26, P["WHITE"])
set_p(41, 25, P["WHITE"])
set_p(42, 26, P["S_DARK"])

# GEAR 2: Center Wheel (Center (37, 34), Radius 4.0)
# Meshes with Gear 1 at (39, 30)!
for dy in range(-4, 5):
    for dx in range(-4, 5):
        dist = math.hypot(dx, dy)
        px = 37 + dx
        py = 34 + dy
        if math.hypot(px - CX, py - CY) < 13.2 and dist <= 4.2:
            ang = math.atan2(dy, dx)
            tooth = math.cos(ang * 12)
            if dist >= 3.2:
                if tooth > 0.2:
                    set_p(px, py, P["G_PALE"] if dy < 0 else P["G_HI"])
                else:
                    set_p(px, py, P["G_BLACK"])
            elif dist <= 1.2:
                set_p(px, py, P["G_MID"])
            else:
                spoke_diff = min(abs((ang - i * (math.pi / 2) + math.pi) % (2 * math.pi) - math.pi) for i in range(4))
                if spoke_diff < 0.25:
                    set_p(px, py, P["G_LIGHT"])

# Interlocking teeth between Gear 1 and Gear 2 at (39, 30):
set_p(40, 29, P["G_PALE"])
set_p(40, 30, P["G_BLACK"])
set_p(39, 30, P["G_WHITE"])
set_p(38, 31, P["G_HI"])

# GEAR 3: Third Wheel (Center-Left, Center (29, 32), Radius 4.6)
# Meshes with Gear 2 at (33, 33)!
for dy in range(-5, 6):
    for dx in range(-5, 6):
        dist = math.hypot(dx, dy)
        px = 29 + dx
        py = 32 + dy
        if math.hypot(px - CX, py - CY) < 13.2 and dist <= 4.6:
            ang = math.atan2(dy, dx)
            tooth = math.cos(ang * 12)
            if dist >= 3.4:
                if tooth > 0.15:
                    set_p(px, py, P["G_PALE"] if dx + dy < 0 else P["G_LIGHT"])
                else:
                    set_p(px, py, P["G_BLACK"])
            elif dist <= 1.2:
                set_p(px, py, P["G_MID"])
            else:
                spoke_diff = min(abs((ang - i * (math.pi / 2) + math.pi) % (2 * math.pi) - math.pi) for i in range(4))
                if spoke_diff < 0.28:
                    set_p(px, py, P["G_LIGHT"])

# Interlocking teeth between Gear 2 and Gear 3 at (33, 33):
set_p(33, 33, P["G_WHITE"])
set_p(34, 33, P["G_BLACK"])
set_p(34, 34, P["G_PALE"])
set_p(33, 34, P["G_HI"])

# GEAR 4: Fourth Wheel (Lower-Left, Center (31, 41), Radius 4.0)
# Meshes with Gear 3 at (30, 37)!
for dy in range(-4, 5):
    for dx in range(-4, 5):
        dist = math.hypot(dx, dy)
        px = 31 + dx
        py = 41 + dy
        if math.hypot(px - CX, py - CY) < 13.2 and dist <= 4.2:
            ang = math.atan2(dy, dx)
            tooth = math.cos(ang * 12)
            if dist >= 3.0:
                if tooth > 0.15:
                    set_p(px, py, P["G_PALE"] if dy < 0 else P["G_HI"])
                else:
                    set_p(px, py, P["G_BLACK"])
            elif dist <= 1.1:
                set_p(px, py, P["G_MID"])
            else:
                spoke_diff = min(abs((ang - i * (math.pi / 2) + math.pi) % (2 * math.pi) - math.pi) for i in range(4))
                if spoke_diff < 0.28:
                    set_p(px, py, P["G_LIGHT"])

# Interlocking teeth between Gear 3 and Gear 4 at (30, 37):
set_p(30, 36, P["G_HI"])
set_p(30, 37, P["G_BLACK"])
set_p(31, 37, P["G_WHITE"])

# GEAR 5: Escape Wheel (Lower-Center, Center (36, 44), Radius 3.2)
escape_teeth = [
    (36, 42, P["S_HI"]), (38, 43, P["S_HI"]),
    (38, 45, P["G_PALE"]), (36, 46, P["G_HI"]),
    (34, 45, P["S_HI"]), (34, 43, P["G_PALE"])
]
for ex, ey, ecol in escape_teeth:
    if math.hypot(ex - CX, ey - CY) < 13.2:
        set_p(ex, ey, ecol)
set_p(36, 44, P["S_LIGHT"])

# GEAR 6: The Balance Wheel (Regulating Organ at (43, 39), Radius 4.8)
for dy in range(-5, 6):
    for dx in range(-5, 6):
        dist = math.hypot(dx, dy)
        px = 43 + dx
        py = 39 + dy
        if math.hypot(px - CX, py - CY) < 13.2:
            if 3.8 <= dist <= 4.7:
                if dx + dy < -1.0:
                    col = P["G_WHITE"]
                elif dx + dy > 2.0:
                    col = P["G_BASE"]
                else:
                    col = P["G_HI"]
                set_p(px, py, col)
            elif dist < 3.8 and (dx == 0 or dy == 0):
                set_p(px, py, P["G_MID"])

# Timing screws along balance rim
for ang_deg in [0, 45, 90, 135, 180, 225, 270, 315]:
    rad = math.radians(ang_deg)
    sx = int(round(43 + 4.9 * math.cos(rad)))
    sy = int(round(39 + 4.9 * math.sin(rad)))
    if math.hypot(sx - CX, sy - CY) < 13.2:
        set_p(sx, sy, P["G_PALE"])

# -------------------------------------------------------------
# 8. Synthetic Ruby Jewels & Heat-Blued Screws
# -------------------------------------------------------------
def set_ruby(jx, jy):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx*dx + dy*dy <= 2:
                set_p(jx + dx, jy + dy, P["R_DARK"])
    set_p(jx - 1, jy,     P["R_MID"])
    set_p(jx + 1, jy,     P["R_BRIGHT"])
    set_p(jx,     jy - 1, P["R_HI"])
    set_p(jx,     jy + 1, P["R_DARK"])
    set_p(jx,     jy,     P["WHITE"])

def set_screw(sx, sy, horiz=True):
    set_p(sx,     sy,     P["B_MID"])
    set_p(sx + 1, sy,     P["B_HI"])
    set_p(sx,     sy + 1, P["B_LIGHT"])
    set_p(sx + 1, sy + 1, P["B_DARK"])
    if horiz:
        set_p(sx,     sy, P["B_BLACK"])
        set_p(sx + 1, sy, P["B_BLACK"])
        set_p(sx, sy - 1, P["B_PALE"])
    else:
        set_p(sx, sy,     P["B_BLACK"])
        set_p(sx, sy + 1, P["B_BLACK"])
        set_p(sx - 1, sy, P["B_PALE"])

set_ruby(43, 39)
set_ruby(29, 32)
set_p(29, 24, P["S_HI"])

set_screw(46, 26, horiz=True)
set_screw(26, 27, horiz=False)
set_screw(46, 42, horiz=True)
set_screw(35, 23, horiz=False)

# -------------------------------------------------------------
# 9. Watch Hands (Crisp Blued Steel Breguet Hands with 3D Depth)
# -------------------------------------------------------------
# Cast subtle 1px drop shadow under hands (+1, +1)
hand_shadows = [
    (39, 34), (40, 33), (41, 33), (42, 32), (43, 32), (44, 31),
    (37, 34), (36, 33), (35, 33), (34, 32), (33, 32)
]
for sx, sy in hand_shadows:
    cur = get_p(sx, sy)
    if cur not in [P["WHITE"], P["R_BRIGHT"], P["R_HI"]]:
        set_p(sx, sy, P["G_SHADOW2"])

# Minute Hand: pointing towards 2 o'clock (~ (45, 29))
for mx, my in [(38, 33), (39, 32), (40, 32), (41, 31), (42, 31)]:
    set_p(mx, my, P["B_LIGHT"])

# Breguet Moon Ring at (43, 30)
set_p(42, 30, P["B_HI"])
set_p(43, 29, P["B_HI"])
set_p(44, 30, P["B_MID"])
set_p(43, 31, P["B_DARK"])
set_p(43, 30, P["G_LIGHT"]) # Golden gear shows through hole!

# Needle tip reaching chapter ring at 2 o'clock
set_p(44, 29, P["B_HI"])
set_p(45, 29, P["B_PALE"])
set_p(46, 28, P["B_BLACK"])

# Hour Hand: pointing towards 10 o'clock (~ (31, 30))
for hx, hy in [(36, 33), (35, 32), (34, 32)]:
    set_p(hx, hy, P["B_LIGHT"])

# Breguet Moon Ring at (33, 31)
set_p(32, 31, P["B_HI"])
set_p(33, 30, P["B_HI"])
set_p(34, 31, P["B_MID"])
set_p(33, 32, P["B_DARK"])
set_p(33, 31, P["G_MID"]) # Golden gear shows through hole!

# Needle tip reaching towards 10 o'clock
set_p(32, 30, P["B_HI"])
set_p(31, 30, P["B_PALE"])
set_p(30, 29, P["B_BLACK"])

# Center Cannon Pinion Cap (37, 34)
set_p(36, 34, P["B_DARK"])
set_p(38, 34, P["B_MID"])
set_p(37, 33, P["B_HI"])
set_p(37, 35, P["B_BLACK"])
set_p(37, 34, P["WHITE"]) # Glistening center pivot highlight

# -------------------------------------------------------------
# 10. Crystal Specular Glint (Domed Glass Reflection)
# -------------------------------------------------------------
glass_glints = [
    (24, 24), (25, 23), (26, 22), (27, 21), (28, 20), (29, 20),
    (30, 19), (31, 19), (32, 19)
]
for gx, gy in glass_glints:
    cur = get_p(gx, gy)
    if cur in [P["D_BRIGHT"], P["D_WHITE"], P["D_CREAM"], P["D_LIGHT"]]:
        set_p(gx, gy, P["WHITE"])
    elif cur in [P["G_LIGHT"], P["G_MID"], P["G_HI"]]:
        set_p(gx, gy, P["G_WHITE"])

# Secondary rim reflection at bottom right
for gx, gy in [(48, 46), (49, 45), (50, 44)]:
    set_p(gx, gy, P["G_PALE"])

# -------------------------------------------------------------
# Transfer buffer into Canvas
# -------------------------------------------------------------
for y in range(64):
    for x in range(64):
        c.set(x, y, fb[y][x])

print(c.stats_text())
view(c)
finish(c)
