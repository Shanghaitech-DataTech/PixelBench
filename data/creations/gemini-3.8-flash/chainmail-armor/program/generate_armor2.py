from pixelbench_api import *

def build_armor_v2():
    c = new_canvas(32, 32)
    grid = [[None for _ in range(32)] for _ in range(32)]
    
    # 1. Palette:
    OUTLINE     = "#0c0f17"   # Crispest dark navy/black outline
    OUTLINE_SFT = "#161b26"   # Softer inner outline
    
    # Steel shades (polished iron/steel):
    S_SPEC  = "#ffffff"       # Specular gleam
    S_HI    = "#e2e8f0"       # Polished highlight
    S_LMID  = "#cbd5e1"       # Light midtone
    S_MID   = "#94a3b8"       # Core metal midtone
    S_DMID  = "#64748b"       # Shaded metal
    S_SHAD  = "#475569"       # Deep metal shadow
    S_DSHAD = "#334155"       # Darkest ring shadow
    S_HOLE  = "#18202c"       # Ring hole (under-armor void)
    S_DEEP  = "#0f141d"       # Deep interior crevices
    
    # Leather:
    L_HI    = "#b45309"       # Warm leather highlight
    L_MID   = "#78350f"       # Rich brown leather
    L_SHAD  = "#451a03"       # Dark leather shadow
    L_DARK  = "#260e02"       # Belt crevice
    
    # Brass/Gold accents:
    G_HI    = "#fef08a"
    G_MID   = "#eab308"
    G_SHAD  = "#854d0e"
    
    # Gambeson / Neck interior:
    GB_MID  = "#2a221b"
    GB_SHAD = "#18130f"
    
    # 2. Hauberk Silhouette Mask
    # Let's sculpt the heroic armor shape:
    # Neck: y=4..7, centered at x=15.5
    # Shoulders slope down from (12, 5) to (3, 10)
    # Sleeves extend down to y=14..15
    # Waist at y=18..19
    # Skirt flares down to y=27, split at center (x=15, 16) up to y=24
    
    armor_mask = set()
    
    # Row spans:
    rows = {
        4: range(12, 20),      # Back collar & top shoulders
        5: range(10, 22),
        6: range(8, 24),
        7: range(6, 26),
        8: range(4, 28),
        9: range(3, 29),
        10: range(2, 30),
        11: range(2, 30),
        12: range(2, 30),
        13: range(2, 30),
        14: list(range(2, 8)) + list(range(9, 23)) + list(range(24, 30)),
        15: list(range(3, 7)) + list(range(9, 23)) + list(range(25, 29)),
        16: range(9, 23),
        17: range(9, 23),
        18: range(9, 23),      # Waist
        19: range(9, 23),      # Belt
        20: range(8, 24),      # Hips flare
        21: range(8, 24),
        22: range(7, 25),
        23: range(7, 25),
        24: list(range(7, 15)) + list(range(17, 25)), # Split starts at y=24
        25: list(range(7, 15)) + list(range(17, 25)),
        26: list(range(7, 14)) + list(range(18, 25)),
        27: list(range(7, 14)) + list(range(18, 25)),
    }
    
    for y, xs in rows.items():
        for x in xs:
            armor_mask.add((x, y))
            
    # Base fill with under-armor void
    for (x, y) in armor_mask:
        grid[y][x] = S_HOLE
        
    # Draw interlocking rings over the armor
    for r in range(13):
        cy = 4 + r * 2
        # cx symmetric around 15.5:
        # even r: [2, 6, 10, 14, 18, 22, 26, 30]
        # odd r:  [4, 8, 12, 16, 20, 24, 28]
        cx_list = [2, 6, 10, 14, 18, 22, 26, 30] if (r % 2 == 0) else [4, 8, 12, 16, 20, 24, 28]
        for cx in cx_list:
            # Lighting model:
            # Light from top-left (e.g. angle ~ -135 deg)
            # Distance from light source (x=6, y=2):
            dx = cx - 6
            dy = cy - 2
            # Horizontal factor:
            hx = (30 - cx) / 30.0  # 1.0 on left, 0.0 on right
            # Vertical factor:
            vy = (28 - cy) / 28.0  # 1.0 at top, 0.0 at bottom
            
            b = 0.25 + 0.50 * hx + 0.25 * vy
            
            # Pectoral swell (chest volume around y=8..12, x=10..21)
            if 8 <= cy <= 12:
                # Curvature of chest
                dist_to_pec_left = ((cx - 12)**2 + (cy - 10)**2)**0.5
                dist_to_pec_right = ((cx - 19)**2 + (cy - 10)**2)**0.5
                if dist_to_pec_left < 4.5:
                    b += 0.20 * (1.0 - dist_to_pec_left / 4.5)
                elif dist_to_pec_right < 4.5:
                    b += 0.10 * (1.0 - dist_to_pec_right / 4.5)
                    
            # Waist shadow (y=17..18)
            if 17 <= cy <= 18:
                b -= 0.10
                
            # Skirt hip curvature (y=21..25):
            if 21 <= cy <= 25 and cx <= 13:
                b += 0.08
            if cy >= 23 and cx >= 17:
                b -= 0.12
                
            b = max(0.15, min(1.0, b))
            
            # Palette levels:
            if b > 0.85:
                col_prong_l = S_SPEC
                col_prong_r = S_HI
                col_left    = S_LMID
                col_right   = S_MID
                col_bot     = S_DMID
                col_hole    = S_HOLE
            elif b > 0.68:
                col_prong_l = S_HI
                col_prong_r = S_LMID
                col_left    = S_LMID
                col_right   = S_DMID
                col_bot     = S_DMID
                col_hole    = S_HOLE
            elif b > 0.50:
                col_prong_l = S_LMID
                col_prong_r = S_MID
                col_left    = S_MID
                col_right   = S_SHAD
                col_bot     = S_SHAD
                col_hole    = S_HOLE
            elif b > 0.35:
                col_prong_l = S_MID
                col_prong_r = S_DMID
                col_left    = S_DMID
                col_right   = S_DSHAD
                col_bot     = S_DSHAD
                col_hole    = S_DEEP
            else:
                col_prong_l = S_DMID
                col_prong_r = S_SHAD
                col_left    = S_SHAD
                col_right   = S_DSHAD
                col_bot     = S_DSHAD
                col_hole    = S_DEEP
                
            # Stamp ring parts:
            if (cx, cy) in armor_mask:
                grid[cy][cx] = col_hole
            if (cx - 1, cy) in armor_mask:
                grid[cy][cx - 1] = col_left
            if (cx + 1, cy) in armor_mask:
                grid[cy][cx + 1] = col_right
            if (cx - 1, cy - 1) in armor_mask:
                grid[cy - 1][cx - 1] = col_prong_l
            if (cx + 1, cy - 1) in armor_mask:
                grid[cy - 1][cx + 1] = col_prong_r
            if (cx, cy + 1) in armor_mask:
                grid[cy + 1][cx] = col_bot

    # Scalloped bottom hem (dangling ringlets at y=28):
    for cx in [8, 10, 12, 18, 20, 22]:
        armor_mask.add((cx, 28))
        grid[28][cx] = S_MID if cx < 15 else S_SHAD

    # Scalloped sleeve cuffs (dangling ringlets at y=16):
    for cx in [3, 5]:
        armor_mask.add((cx, 16))
        grid[16][cx] = S_LMID
    for cx in [26, 28]:
        armor_mask.add((cx, 16))
        grid[16][cx] = S_SHAD

    # Sleeve armhole openings (under the cuffs, showing dark interior):
    grid[15][3] = S_DEEP
    grid[15][4] = S_HOLE
    grid[15][5] = S_HOLE
    grid[15][6] = S_DEEP
    grid[15][25] = S_DEEP
    grid[15][26] = S_HOLE
    grid[15][27] = S_HOLE
    grid[15][28] = S_DEEP

    # Neck Opening:
    # Clear neck area from armor_mask and grid:
    for y in range(4, 8):
        for x in range(12, 20):
            armor_mask.discard((x, y))
            grid[y][x] = None
            
    # Back interior of neck (visible gambeson / undergarment lining):
    for x in range(13, 19):
        grid[4][x] = GB_SHAD
        grid[5][x] = GB_MID
    for x in range(14, 18):
        grid[6][x] = GB_SHAD

    # Leather Collar Trim:
    # A tidy 1-pixel leather rim around the neck:
    collar_trim = [
        (12, 5, L_MID), (19, 5, L_SHAD),
        (12, 6, L_HI),  (19, 6, L_SHAD),
        (13, 7, L_HI),  (14, 7, L_MID), (17, 7, L_SHAD), (18, 7, L_DARK),
        (15, 8, L_MID), (16, 8, L_SHAD)
    ]
    for x, y, col in collar_trim:
        armor_mask.add((x, y))
        grid[y][x] = col
        
    # Brass studs on collar:
    grid[6][12] = G_HI
    grid[7][13] = G_MID
    grid[7][18] = G_SHAD
    grid[6][19] = G_SHAD

    # Leather Belt (y=18..19):
    for x in range(9, 23):
        if x < 14:
            grid[18][x] = L_HI
            grid[19][x] = L_MID
        elif x > 17:
            grid[18][x] = L_SHAD
            grid[19][x] = L_DARK
        else:
            grid[18][x] = L_MID
            grid[19][x] = L_SHAD
            
    # Golden Belt Buckle (x=14..17, y=18..19):
    grid[18][14] = G_HI
    grid[18][15] = G_HI
    grid[18][16] = G_MID
    grid[18][17] = G_SHAD
    grid[19][14] = G_MID
    grid[19][15] = L_DARK # buckle interior hole
    grid[19][16] = G_MID  # buckle prong
    grid[19][17] = G_SHAD
    
    # Cast shadow from belt onto mail skirt (y=20):
    for x in range(9, 23):
        if grid[20][x] is not None and (x, 20) in armor_mask:
            # deepen the shadow of the top row of the skirt
            if x < 16:
                grid[20][x] = S_DMID
            else:
                grid[20][x] = S_DSHAD

    # Hanging belt strap tip down left thigh (x=13, y=20..22):
    grid[20][13] = L_MID
    grid[21][13] = L_MID
    grid[22][13] = G_MID # brass strap tip
    armor_mask.add((13, 20))
    armor_mask.add((13, 21))
    armor_mask.add((13, 22))

    # Riding split shadow between legs (x=14..17, y=24..28):
    # Under-skirt shadow:
    for y in range(24, 28):
        grid[y][15] = "#0a0d14"
        grid[y][16] = "#0a0d14"
    grid[24][14] = "#0f141d"
    grid[24][17] = "#0f141d"
    grid[25][14] = "#0f141d"
    grid[25][17] = "#0f141d"

    # Dark Outline around the whole sprite:
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
        
    # Apply to canvas:
    for y in range(32):
        for x in range(32):
            if grid[y][x] is not None:
                c.set(x, y, grid[y][x])
                
    return c

c = build_armor_v2()
view(c)
