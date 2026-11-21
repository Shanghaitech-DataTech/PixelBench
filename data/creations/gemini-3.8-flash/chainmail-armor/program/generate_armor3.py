from pixelbench_api import *

def build_armor_v3():
    c = new_canvas(32, 32)
    grid = [[None for _ in range(32)] for _ in range(32)]
    
    # 1. Palette:
    OUTLINE     = "#0c0f17"   # Main dark outline
    OUTLINE_SFT = "#161b26"   # Soft crease outline
    
    # Steel shades (polished knight's chainmail):
    S_SPEC  = "#ffffff"       # Pure white specular gleam
    S_HI    = "#e2e8f0"       # Polished highlight
    S_LMID  = "#cbd5e1"       # Light midtone
    S_MID   = "#94a3b8"       # Core steel midtone
    S_DMID  = "#64748b"       # Shaded steel
    S_SHAD  = "#475569"       # Shadow steel
    S_DSHAD = "#334155"       # Deep shadow
    S_HOLE  = "#18202c"       # Ring hole (under-armor void)
    S_DEEP  = "#0f141d"       # Deep crevices
    
    # Leather (collar, cuffs, belt):
    L_SPEC  = "#d97706"       # Leather specular
    L_HI    = "#b45309"       # Leather highlight
    L_MID   = "#78350f"       # Rich brown leather
    L_SHAD  = "#451a03"       # Dark leather shadow
    L_DARK  = "#260e02"       # Deepest leather crevice
    
    # Gold/Brass rivets & buckle:
    G_HI    = "#fef08a"       # Bright gold highlight
    G_MID   = "#eab308"       # Core gold
    G_SHAD  = "#854d0e"       # Gold shadow
    
    # Gambeson / Neck interior:
    GB_MID  = "#2c241e"
    GB_SHAD = "#17120e"

    # Define armor solid shape mask:
    armor_mask = set()
    
    # Row spans:
    rows = {
        4: range(12, 20),      # Top of shoulders & neck
        5: range(10, 22),
        6: range(8, 24),
        7: range(6, 26),
        8: range(4, 28),
        9: range(3, 29),
        10: range(2, 30),
        11: range(2, 30),
        12: range(2, 30),
        13: range(2, 30),
        14: range(2, 30),
        15: list(range(2, 8)) + list(range(9, 23)) + list(range(24, 30)), # Cuffs & chest
        16: range(9, 23),      # Below sleeves
        17: range(9, 23),
        18: range(9, 23),      # Waist
        19: range(9, 23),      # Belt
        20: range(8, 24),      # Hips flare
        21: range(8, 24),
        22: range(7, 25),
        23: range(7, 25),
        24: list(range(7, 15)) + list(range(17, 25)), # Riding split
        25: list(range(7, 15)) + list(range(17, 25)),
        26: list(range(7, 14)) + list(range(18, 25)),
        27: [8, 10, 12, 19, 21, 23],                  # Scalloped hem tips
    }
    
    for y, xs in rows.items():
        for x in xs:
            armor_mask.add((x, y))
            
    # Base fill with under-armor void
    for (x, y) in armor_mask:
        grid[y][x] = S_HOLE

    # Draw interlocking chainmail rings
    for r in range(12):
        cy = 4 + r * 2
        cx_list = [2, 6, 10, 14, 18, 22, 26, 30] if (r % 2 == 0) else [4, 8, 12, 16, 20, 24, 28]
        for cx in cx_list:
            # Distance from top-left light (x=6, y=2):
            hx = (30 - cx) / 30.0  # 1.0 on left, 0.0 on right
            vy = (28 - cy) / 28.0  # 1.0 at top, 0.0 at bottom
            b = 0.25 + 0.52 * hx + 0.23 * vy
            
            # Pectoral swell (chest volume around y=8..12, x=10..21)
            if 8 <= cy <= 12:
                dist_l = ((cx - 12)**2 + (cy - 10)**2)**0.5
                dist_r = ((cx - 19)**2 + (cy - 10)**2)**0.5
                if dist_l < 4.5:
                    b += 0.22 * (1.0 - dist_l / 4.5)
                elif dist_r < 4.5:
                    b += 0.10 * (1.0 - dist_r / 4.5)
                    
            # Waist shadow (y=17..18)
            if 17 <= cy <= 18:
                b -= 0.12
                
            # Skirt hip curvature (y=21..25):
            if 21 <= cy <= 25 and cx <= 13:
                b += 0.08
            if cy >= 23 and cx >= 17:
                b -= 0.12
                
            b = max(0.15, min(1.0, b))
            
            # Palette mapping:
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

    # Color the scalloped hem tips (y=27):
    grid[27][8]  = S_LMID
    grid[27][10] = S_MID
    grid[27][12] = S_MID
    grid[27][19] = S_DMID
    grid[27][21] = S_SHAD
    grid[27][23] = S_SHAD

    # Under-skirt shadow in the riding split (x=14..17, y=24..27):
    grid[24][15] = "#10141d"
    grid[24][16] = "#10141d"
    grid[25][15] = "#0b0e14"
    grid[25][16] = "#0b0e14"
    grid[26][14] = "#0b0e14"
    grid[26][15] = "#080a10"
    grid[26][16] = "#080a10"
    grid[26][17] = "#0b0e14"
    grid[27][14] = "#080a10"
    grid[27][15] = "#05070a"
    grid[27][16] = "#05070a"
    grid[27][17] = "#080a10"
    
    # Highlight the inner edge of the right flap (facing the light):
    grid[24][17] = S_HI
    grid[25][17] = S_LMID
    grid[26][18] = S_LMID

    # Sleeve Cuffs - Reinforced Leather Trim at y=15:
    # Left sleeve cuff (x=2..7):
    grid[15][2] = L_MID
    grid[15][3] = L_HI
    grid[15][4] = G_MID # golden brass cuff rivet!
    grid[15][5] = L_HI
    grid[15][6] = L_MID
    grid[15][7] = L_SHAD
    # Right sleeve cuff (x=24..29):
    grid[15][24] = L_SHAD
    grid[15][25] = L_MID
    grid[15][26] = L_SHAD
    grid[15][27] = G_SHAD # brass cuff rivet
    grid[15][28] = L_SHAD
    grid[15][29] = L_DARK

    # Crease shadow between sleeves and torso (y=14..15):
    grid[14][8]  = OUTLINE_SFT
    grid[15][8]  = OUTLINE_SFT
    grid[14][23] = OUTLINE_SFT
    grid[15][23] = OUTLINE_SFT

    # Neck Opening:
    # Clear neck area from armor_mask and grid:
    for y in range(4, 8):
        for x in range(12, 20):
            armor_mask.discard((x, y))
            grid[y][x] = None
            
    # Back interior of neck (visible gambeson / padded undergarment lining):
    for x in range(13, 19):
        grid[4][x] = GB_SHAD
        grid[5][x] = GB_MID
    for x in range(14, 18):
        grid[6][x] = GB_SHAD

    # Leather Collar Trim:
    # Rim along y=7, x=13..18, and sides at (12, 5..6), (19, 5..6)
    grid[5][12] = L_MID
    grid[6][12] = L_HI
    grid[7][12] = L_MID
    grid[7][13] = L_HI
    grid[7][14] = G_HI   # left collar gold rivet!
    grid[7][15] = L_MID
    grid[7][16] = L_MID
    grid[7][17] = G_MID  # right collar gold rivet!
    grid[7][18] = L_SHAD
    grid[7][19] = L_DARK
    grid[6][19] = L_SHAD
    grid[5][19] = L_DARK

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
    grid[19][15] = L_DARK # buckle inner hole
    grid[19][16] = G_MID  # buckle tongue
    grid[19][17] = G_SHAD
    
    # Cast shadow from belt onto mail skirt (y=20):
    for x in range(9, 23):
        if grid[20][x] is not None:
            if x < 15:
                grid[20][x] = S_DMID
            else:
                grid[20][x] = S_DSHAD

    # Hanging belt strap tip down left thigh (x=13, y=20..22):
    grid[20][13] = L_HI
    grid[21][13] = L_MID
    grid[22][13] = G_HI # golden strap end tip!

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

c = build_armor_v3()
view(c)
