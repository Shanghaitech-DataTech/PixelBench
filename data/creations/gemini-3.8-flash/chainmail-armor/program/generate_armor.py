from pixelbench_api import *

def build_armor():
    c = new_canvas(32, 32)
    
    # Let's define the armor parts carefully:
    # 1. Torso silhouette:
    # y=3..28
    
    # We will build an image buffer: grid[y][x] = color
    grid = [[None for _ in range(32)] for _ in range(32)]
    
    # Let's define the armor mask
    armor_mask = set()
    
    # Rows for the hauberk:
    # y=3: back of neck (x=13..18)
    # y=4: shoulders (x=11..20)
    # y=5: x=9..22
    # y=6: x=7..24
    # y=7: x=5..26
    # y=8: x=4..27
    # y=9: x=3..28
    # y=10..13: sleeves + chest (x=2..29)
    # y=14: left sleeve (2..7), chest (9..22), right sleeve (24..29)
    # y=15: left sleeve (2..7), chest (9..22), right sleeve (24..29)
    # y=16: chest (x=9..22)
    # y=17: chest (x=9..22)
    # y=18..19: waist (x=9..22)
    # y=20..22: hips (x=8..23)
    # y=23..26: skirt (x=7..24)
    # y=27: split skirt (x=7..14, 17..24)
    
    rows = {
        3: range(13, 19),
        4: range(11, 21),
        5: range(9, 23),
        6: range(7, 25),
        7: range(5, 27),
        8: range(4, 28),
        9: range(3, 29),
        10: range(2, 30),
        11: range(2, 30),
        12: range(2, 30),
        13: range(2, 30),
        14: list(range(2, 8)) + list(range(9, 23)) + list(range(24, 30)),
        15: list(range(2, 8)) + list(range(9, 23)) + list(range(24, 30)),
        16: range(9, 23),
        17: range(9, 23),
        18: range(9, 23),
        19: range(9, 23),
        20: range(8, 24),
        21: range(8, 24),
        22: range(8, 24),
        23: range(7, 25),
        24: range(7, 25),
        25: range(7, 25),
        26: range(7, 25),
        27: list(range(7, 15)) + list(range(17, 25)),
    }
    
    for y, xs in rows.items():
        for x in xs:
            armor_mask.add((x, y))
            
    # Base dark fill
    for (x, y) in armor_mask:
        grid[y][x] = "#111827"
        
    # Draw interlocking rings over the armor!
    # Ring centers:
    # r = 0 to 12
    # cy = 4 + r * 2
    # if r % 2 == 0: cx in [2, 6, 10, 14, 18, 22, 26, 30]
    # if r % 2 == 1: cx in [4, 8, 12, 16, 20, 24, 28]
    
    for r in range(13):
        cy = 4 + r * 2
        cx_list = [2, 6, 10, 14, 18, 22, 26, 30] if (r % 2 == 0) else [4, 8, 12, 16, 20, 24, 28]
        for cx in cx_list:
            # Check if this ring is within or near the armor
            # A ring consists of:
            # hole: (cx, cy)
            # left: (cx - 1, cy)
            # right: (cx + 1, cy)
            # top-left: (cx - 1, cy - 1)
            # top-right: (cx + 1, cy - 1)
            # bottom: (cx, cy + 1)
            
            # Shading calculation based on position and lighting:
            # Light source at top-left (e.g. x=8, y=2)
            # Chest pectorals (y=8..13, x=10..21) have subtle volume
            # Waist (y=17..19) is slightly recessed
            # Hips / skirt (y=22..26) catch light on left
            
            # Base brightness from x and y:
            # Left side (x < 16) is brighter than right side (x >= 16)
            b = 1.0 - (cx / 36.0) * 0.45 - (cy / 36.0) * 0.35
            
            # Pectoral highlight boost:
            if 8 <= cy <= 12:
                if 9 <= cx <= 15:
                    b += 0.22 # bright chest highlight on upper left
                elif 16 <= cx <= 21:
                    b += 0.08
            # Waist shadow dip:
            if 17 <= cy <= 19:
                b -= 0.12
            # Bottom skirt shadow on right:
            if cy >= 24 and cx >= 16:
                b -= 0.15
                
            # Clamp b
            b = max(0.2, min(1.0, b))
            
            # Palette mapping:
            if b > 0.82:
                col_spec = "#ffffff"
                col_hi = "#f1f5f9"
                col_mid = "#cbd5e1"
                col_shad = "#64748b"
                col_hole = "#1e293b"
            elif b > 0.65:
                col_spec = "#f8fafc"
                col_hi = "#e2e8f0"
                col_mid = "#94a3b8"
                col_shad = "#475569"
                col_hole = "#18202c"
            elif b > 0.45:
                col_spec = "#e2e8f0"
                col_hi = "#cbd5e1"
                col_mid = "#64748b"
                col_shad = "#334155"
                col_hole = "#111827"
            else:
                col_spec = "#94a3b8"
                col_hi = "#64748b"
                col_mid = "#475569"
                col_shad = "#1e293b"
                col_hole = "#0b0f17"
                
            # Draw parts of ring if in armor_mask:
            # 1. Hole
            if (cx, cy) in armor_mask:
                grid[cy][cx] = col_hole
            # 2. Left side
            if (cx - 1, cy) in armor_mask:
                grid[cy][cx - 1] = col_mid
            # 3. Right side
            if (cx + 1, cy) in armor_mask:
                grid[cy][cx + 1] = col_shad
            # 4. Top-left prong
            if (cx - 1, cy - 1) in armor_mask:
                grid[cy - 1][cx - 1] = col_spec if (b > 0.75) else col_hi
            # 5. Top-right prong
            if (cx + 1, cy - 1) in armor_mask:
                grid[cy - 1][cx + 1] = col_hi if (b > 0.75) else col_mid
            # 6. Bottom tip
            if (cx, cy + 1) in armor_mask:
                grid[cy + 1][cx] = col_shad

    # Scalloped hem hanging rings at bottom of skirt (y=28):
    # Rings hang down at cx = 8, 10, 12, 14, 18, 20, 22, 24
    for cx in [8, 10, 12, 14, 18, 20, 22, 24]:
        b = 1.0 - (cx / 36.0) * 0.45 - (28 / 36.0) * 0.35
        col = "#94a3b8" if b > 0.55 else "#475569"
        armor_mask.add((cx, 28))
        grid[28][cx] = col

    # Sleeve cuffs scalloped rings at y=16:
    for cx in [3, 5, 7]:
        armor_mask.add((cx, 16))
        grid[16][cx] = "#cbd5e1"
    for cx in [25, 27, 29]:
        armor_mask.add((cx, 16))
        grid[16][cx] = "#475569"

    # Collar / Neckline:
    # Cut out neck hole:
    for x in range(13, 19):
        for y in range(4, 7):
            armor_mask.discard((x, y))
            grid[y][x] = None
    # Neck interior (gambeson / dark lining):
    for x in range(13, 19):
        grid[4][x] = "#12151c"
        grid[5][x] = "#241d19" # dark quilted cloth
    for x in range(14, 18):
        grid[6][x] = "#181412"

    # Padded leather collar trim around the neck:
    collar = [
        (12, 4, "#78350f"), (19, 4, "#451a03"),
        (12, 5, "#b45309"), (19, 5, "#451a03"),
        (12, 6, "#b45309"), (13, 6, "#78350f"), (18, 6, "#451a03"), (19, 6, "#2d1202"),
        (13, 7, "#b45309"), (14, 7, "#78350f"), (17, 7, "#451a03"), (18, 7, "#2d1202"),
        (14, 8, "#d97706"), (15, 8, "#b45309"), (16, 8, "#78350f"), (17, 8, "#451a03"),
    ]
    for x, y, col in collar:
        grid[y][x] = col
        armor_mask.add((x, y))
        
    # Golden rivets on collar:
    grid[6][12] = "#fef08a" # left rivet highlight
    grid[7][13] = "#fde047"
    grid[8][14] = "#fde047"
    grid[8][17] = "#ca8a04" # right rivet shadow
    grid[7][18] = "#a16207"

    # Leather Belt at waist (rows 18 and 19):
    for x in range(9, 23):
        # Belt highlight on left, shadow on right
        if x < 13:
            grid[18][x] = "#b45309"
            grid[19][x] = "#78350f"
        elif x > 18:
            grid[18][x] = "#451a03"
            grid[19][x] = "#270f02"
        else:
            grid[18][x] = "#92400e"
            grid[19][x] = "#5a2407"
            
    # Belt buckle in the center (x=14..17, y=18..19):
    # Golden buckle with tongue
    grid[18][14] = "#fef08a"
    grid[18][15] = "#fde047"
    grid[18][16] = "#ca8a04"
    grid[18][17] = "#854d0e"
    grid[19][14] = "#eab308"
    grid[19][15] = "#1c0b02" # buckle inner hole
    grid[19][16] = "#ca8a04" # buckle prong
    grid[19][17] = "#713f12"

    # Belt hanging strap tip down left hip (x=13, y=20..22):
    grid[20][13] = "#78350f"
    grid[21][13] = "#92400e"
    grid[22][13] = "#b45309" # brass end tip
    armor_mask.add((13, 20))
    armor_mask.add((13, 21))
    armor_mask.add((13, 22))

    # Dark Outline around the armor:
    OUTLINE = "#0f172a"
    all_solid = set()
    for y in range(32):
        for x in range(32):
            if grid[y][x] is not None:
                all_solid.add((x, y))
                
    outline_pixels = set()
    for (x, y) in all_solid:
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 32 and 0 <= ny < 32:
                if (nx, ny) not in all_solid:
                    outline_pixels.add((nx, ny))
                    
    for (x, y) in outline_pixels:
        grid[y][x] = OUTLINE
        
    # Armhole interiors at cuffs (showing dark interior of sleeves):
    # Under left sleeve (x=3..7, y=15):
    grid[15][3] = "#12151c"
    grid[15][4] = "#181d26"
    grid[15][5] = "#181d26"
    grid[15][6] = "#12151c"
    # Under right sleeve (x=24..28, y=15):
    grid[15][25] = "#0b0d13"
    grid[15][26] = "#12151c"
    grid[15][27] = "#12151c"
    grid[15][28] = "#0b0d13"

    # Write to canvas:
    for y in range(32):
        for x in range(32):
            if grid[y][x] is not None:
                c.set(x, y, grid[y][x])
                
    return c

c = build_armor()
view(c)
