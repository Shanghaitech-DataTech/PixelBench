import sys
from pixelbench_api import *

def build_forge():
    c = new_canvas(128, 128)
    
    PAL = {
        # Transparent
        'none': None,
        
        # Ground - Grass & Flowers
        'grass_deep': '#1b2d13',
        'grass_dark': '#29431b',
        'grass_mid': '#3f6327',
        'grass_light': '#5d8c37',
        'grass_hi': '#82b54b',
        'flower_yellow': '#fce844',
        'flower_red': '#e04138',
        
        # Ground - Cobblestones & Dirt
        'dirt_dark': '#2e1e12',
        'dirt_mid': '#4a321f',
        'dirt_light': '#69482d',
        'cobble_dark': '#22242a',
        'cobble_mid': '#3d424e',
        'cobble_light': '#5b6475',
        'cobble_hi': '#7f8c9e',
        'cobble_bright': '#a4b0c2',
        
        # Platform rim
        'rim_dark': '#16181c',
        'rim_mid': '#2c313a',
        
        # Stonework (Walls, Arch, Chimney)
        'stone_darkest': '#181a1f',
        'stone_shadow': '#282d36',
        'stone_mid': '#3f4754',
        'stone_light': '#5c6778',
        'stone_hi': '#818e9f',
        'stone_bright': '#abb7c7',
        'stone_white': '#d5deeb',
        
        # Timber & Wood
        'wood_black': '#170e08',
        'wood_dark': '#2b180d',
        'wood_mid': '#472916',
        'wood_warm': '#693e22',
        'wood_light': '#8f5832',
        'wood_hi': '#b87747',
        'wood_pale': '#dca06b',
        
        # Plaster
        'plaster_shadow': '#575043',
        'plaster_mid': '#7f7462',
        'plaster_light': '#aba08c',
        'plaster_hi': '#d4cab8',
        
        # Red Tiled Roof
        'roof_deep': '#30080e',
        'roof_shadow': '#4f1016',
        'roof_dark': '#731a1e',
        'roof_mid': '#9e2622',
        'roof_bright': '#c73626',
        'roof_light': '#e35136',
        'roof_hi': '#f77c57',
        'roof_peak': '#ffa485',
        
        # Furnace Fire & Coals
        'fire_black': '#180302',
        'fire_dark': '#4f0a05',
        'fire_red': '#8f1406',
        'fire_crimson': '#c92508',
        'fire_orange': '#f25807',
        'fire_amber': '#ff9005',
        'fire_yellow': '#ffcb1c',
        'fire_white': '#ffffff',
        
        # Furnace Ambient Glow (cast onto stone and ground)
        'glow_1': '#3b1b07',
        'glow_2': '#69300c',
        'glow_3': '#994a12',
        'glow_4': '#c76718',
        'glow_5': '#f08d24',
        
        # Metal / Iron / Anvil
        'iron_darkest': '#111316',
        'iron_shadow': '#1e2128',
        'iron_mid': '#313842',
        'iron_light': '#4e5868',
        'iron_hi': '#748294',
        'iron_bright': '#a2b0c2',
        
        # Water
        'water_dark': '#0f2033',
        'water_mid': '#173d66',
        'water_light': '#26629c',
        'water_hi': '#4d98db',
        'water_sparkle': '#bfe1ff',
        
        # Smoke
        'smoke_dark': '#45434d',
        'smoke_mid': '#6c6978',
        'smoke_light': '#9794a3',
        'smoke_hi': '#cac7d6',
        'smoke_white': '#f2f0f7',
    }

    for k, v in PAL.items():
        if v:
            c.color(v, name=k)

    def p(x, y, col):
        if 0 <= x < 128 and 0 <= y < 128:
            c.set(x, y, col)

    # 1. GROUND PLATFORM (Isometric base)
    # Diamond: Top (64, 68), Left (14, 93), Right (114, 93), Bottom (64, 118)
    for y in range(68, 119):
        if y <= 93:
            w = (y - 68) * 2
        else:
            w = (118 - y) * 2
        xl = 64 - w
        xr = 64 + w
        for x in range(xl, xr + 1):
            dist_edge = min(x - xl, xr - x, y - 68, 118 - y)
            noise = ((x * 17) ^ (y * 31)) % 13
            
            # The workshop courtyard is the central area:
            # Grass ONLY on the outer 4-5 pixels of the diamond platform!
            is_outer_rim = (dist_edge <= 4)
            is_dirt_edge = (dist_edge in (5, 6))
            
            if is_outer_rim:
                # Grass border with wildflowers
                if noise == 0 and dist_edge <= 2:
                    col = PAL['flower_yellow']
                elif noise == 1 and dist_edge <= 2:
                    col = PAL['flower_red']
                elif noise < 4:
                    col = PAL['grass_mid']
                elif noise < 7:
                    col = PAL['grass_dark']
                elif noise < 10:
                    col = PAL['grass_light']
                else:
                    col = PAL['grass_hi']
            elif is_dirt_edge:
                # Transition dirt between grass and cobblestone
                if noise < 5:
                    col = PAL['grass_dark']
                elif noise < 9:
                    col = PAL['dirt_mid']
                else:
                    col = PAL['dirt_dark']
            else:
                # Cobblestones with 2:1 isometric grout grid
                cx_cell = (x + 2 * y) // 4
                cy_cell = (x - 2 * y) // 4
                is_grout = ((x + 2 * y) % 4 == 0) or ((x - 2 * y) % 4 == 0)
                if is_grout:
                    col = PAL['cobble_dark']
                else:
                    cell_hash = ((cx_cell * 13) ^ (cy_cell * 29)) % 7
                    if cell_hash < 2:
                        col = PAL['cobble_mid']
                    elif cell_hash < 5:
                        col = PAL['cobble_light']
                    elif cell_hash == 5:
                        col = PAL['cobble_hi']
                    else:
                        col = PAL['cobble_bright']
            p(x, y, col)

    # Base platform rim (vertical drop)
    for x in range(14, 65):
        ey = 93 + (x - 14) // 2
        for h in range(1, 6):
            col = PAL['rim_mid'] if h < 4 else PAL['rim_dark']
            if (x + h) % 7 == 0: col = PAL['rim_dark']
            p(x, ey + h, col)

    for x in range(64, 115):
        ey = 118 - (x - 64) // 2
        for h in range(1, 6):
            col = PAL['rim_dark'] if h > 2 else PAL['rim_mid']
            if (x - h) % 7 == 0: col = PAL['rim_dark']
            p(x, ey + h, col)

    # 2. HOUSE WALLS
    # SE Wall (Shadow side, faces down-right, x from 66 to 98)
    for x in range(66, 99):
        base_y = 88 - (x - 66) // 2
        top_y = base_y - 28
        stone_top = base_y - 13
        
        for y in range(top_y, base_y + 1):
            if y > stone_top:
                is_mortar_h = (base_y - y) % 4 == 0
                is_mortar_v = (x % 6 == 0 if ((base_y - y) // 4) % 2 == 0 else (x + 3) % 6 == 0)
                col = PAL['stone_darkest'] if (is_mortar_h or is_mortar_v) else PAL['stone_shadow']
            else:
                is_timber = (x in (66, 67, 81, 82, 97, 98) or 
                             y in (stone_top, stone_top - 1, top_y, top_y + 1) or
                             (x >= 82 and (x - 82) == (y - top_y)) or
                             (x < 82 and (82 - x) == (y - top_y)))
                col = (PAL['wood_black'] if x % 2 == 0 else PAL['wood_dark']) if is_timber else (PAL['plaster_shadow'] if (x + y) % 5 != 0 else PAL['plaster_mid'])
            p(x, y, col)

    # Gable triangle at SE end
    for x in range(66, 99):
        base_top = 88 - (x - 66) // 2 - 28
        if x <= 82:
            gable_top = 60 - int((x - 66) * 1.5)
        else:
            gable_top = 36 + (x - 82) // 2
            
        for y in range(gable_top, base_top):
            is_timber = (x in (81, 82) or y <= gable_top + 1 or
                         abs(x - 82) * 1.5 + (y - 36) < 4)
            p(x, y, PAL['wood_dark'] if is_timber else PAL['plaster_shadow'])

    # SE Wall Door (x=73..79, base_y from ~84 to ~81)
    for x in range(73, 80):
        base_y = 88 - (x - 66) // 2
        for dy in range(0, 12):
            y = base_y - dy
            if dy == 11:
                col = PAL['wood_black']
            elif x in (73, 79) or dy == 0:
                col = PAL['wood_black']
            elif dy in (3, 8):
                col = PAL['iron_bright'] if x in (75, 77) else PAL['iron_light']
            elif x == 78 and dy == 5:
                col = PAL['iron_bright']
            else:
                col = PAL['wood_mid'] if x % 2 == 0 else PAL['wood_warm']
            p(x, y, col)
            
    # Small stone doorstep
    for x in range(72, 81):
        by = 88 - (x - 66) // 2 + 1
        p(x, by, PAL['stone_mid'])

    # Upper window on SE wall (x=87..92, y=47..53)
    for x in range(86, 93):
        for y in range(47, 54):
            if x in (86, 92) or y in (47, 53):
                col = PAL['wood_black']
            elif x in (87, 91):
                col = PAL['wood_warm']
            else:
                col = PAL['fire_amber'] if (x == 89 and y == 50) else PAL['fire_dark']
            p(x, y, col)

    # SW Wall (Lit side, faces down-left, x from 34 to 66)
    for x in range(34, 67):
        base_y = 72 + (x - 34) // 2
        top_y = base_y - 28
        stone_top = base_y - 13
        
        for y in range(top_y, base_y + 1):
            if y > stone_top:
                is_mortar_h = (base_y - y) % 4 == 0
                is_mortar_v = (x % 6 == 0 if ((base_y - y) // 4) % 2 == 0 else (x + 3) % 6 == 0)
                if is_mortar_h or is_mortar_v:
                    col = PAL['stone_shadow']
                else:
                    col = PAL['stone_light'] if (x + y) % 3 == 0 else PAL['stone_mid']
            else:
                is_timber = (x in (34, 35, 48, 49, 65, 66) or 
                             y in (stone_top, stone_top - 1, top_y, top_y + 1) or
                             (x < 48 and (x - 34) == (y - top_y)) or
                             (x >= 48 and (65 - x) == (y - top_y)))
                if is_timber:
                    col = PAL['wood_mid'] if (x + y) % 2 == 0 else PAL['wood_dark']
                else:
                    col = PAL['plaster_light'] if (x + y) % 4 != 0 else PAL['plaster_hi']
            p(x, y, col)

    # Corner post between SW and SE walls (x=66)
    for y in range(60, 89):
        p(66, y, PAL['wood_black'] if y % 3 == 0 else PAL['wood_dark'])

    # 3. RED TILED ROOF
    # NE slope (in shadow)
    for x in range(50, 99):
        if x <= 82:
            r_top = 18 + (x - 50) // 2
            r_bot = r_top + 8
        else:
            r_top = 34 + (x - 82) // 2
            r_bot = r_top + 4
        for y in range(r_top, min(r_bot, 44)):
            col = PAL['roof_shadow'] if (x + 2 * y) % 3 == 0 else PAL['roof_dark']
            p(x, y, col)

    # SW slope (main brightly lit roof face)
    for x in range(30, 84):
        if x >= 48:
            top_y = 17 + (x - 48) // 2
        else:
            top_y = 17 + int((48 - x) * (30.0 / 18.0))
            
        if x <= 64:
            bot_y = 47 + (x - 30) // 2
        else:
            bot_y = 64 - int((x - 64) * (30.0 / 19.0))
            
        for y in range(top_y, bot_y + 1):
            row_idx = (2 * y - x) // 5
            tile_u = (x + 2 * y) // 3
            
            is_overlap = ((2 * y - x) % 5 == 0)
            is_joint = (tile_u % 4 == 0)
            is_highlight = ((2 * y - x) % 5 == 1)
            
            if is_overlap:
                col = PAL['roof_shadow']
            elif is_joint:
                col = PAL['roof_dark']
            elif is_highlight:
                col = PAL['roof_light'] if (tile_u % 4 == 2) else PAL['roof_hi']
            else:
                col = PAL['roof_bright'] if (tile_u % 4 in (1, 2)) else PAL['roof_mid']
                
            p(x, y, col)

    # Ridge cap tiles
    for x in range(48, 84):
        ry = 17 + (x - 48) // 2
        p(x, ry - 1, PAL['roof_peak'] if x % 3 == 0 else PAL['roof_hi'])
        p(x, ry, PAL['roof_light'])
        p(x, ry + 1, PAL['roof_shadow'])

    # Eaves fascia & bargeboards
    for x in range(30, 65):
        ey = 47 + (x - 30) // 2
        p(x, ey + 1, PAL['wood_dark'])
        p(x, ey + 2, PAL['wood_black'])

    for step in range(0, 20):
        rx = 64 + step
        ry = 64 - int(step * (30.0 / 19.0))
        p(rx + 1, ry, PAL['wood_dark'])
        p(rx, ry, PAL['roof_light'])

    # 4. CHIMNEY ON ROOF
    # Chimney cast shadow on roof
    for cx in range(52, 57):
        for cy in range(24, 38):
            if cy >= 17 + (cx - 48) // 2 and cy <= 47 + (cx - 30) // 2:
                if c.get(cx, cy) in (PAL['roof_bright'], PAL['roof_light'], PAL['roof_hi']):
                    p(cx, cy, PAL['roof_dark'])

    # Chimney stack (x=45..51, y=13..38)
    for x in range(45, 52):
        for y in range(14, 39):
            roof_at_x = 17 + int((48 - x) * (30.0 / 18.0)) if x < 48 else 17 + (x - 48) // 2
            if y < roof_at_x + 16:
                is_joint_h = (y % 4 == 0)
                is_joint_v = (x == 48 if (y // 4) % 2 == 0 else x in (46, 50))
                if x == 45:
                    col = PAL['stone_bright']
                elif x == 51:
                    col = PAL['stone_shadow']
                elif is_joint_h or is_joint_v:
                    col = PAL['stone_darkest']
                elif x < 48:
                    col = PAL['stone_hi']
                else:
                    col = PAL['stone_mid']
                p(x, y, col)
                
    # Chimney cap & flue opening (y=12..14)
    for x in range(44, 53):
        p(x, 14, PAL['stone_darkest'])
        p(x, 13, PAL['stone_bright'] if x < 48 else PAL['stone_mid'])
        if x in (44, 52):
            p(x, 12, PAL['stone_mid'])
        else:
            p(x, 12, PAL['stone_darkest'])

    # Chimney flashing
    for x in range(44, 53):
        flash_y = 17 + (x - 48) // 2 + 10
        p(x, flash_y, PAL['iron_shadow'])

    # Volumetric smoke curling upwards
    smoke_particles = [
        (47, 11, 'smoke_light'), (48, 11, 'smoke_white'), (49, 11, 'smoke_light'),
        (46, 10, 'smoke_mid'), (47, 10, 'smoke_hi'), (48, 10, 'smoke_white'), (49, 10, 'smoke_hi'), (50, 10, 'smoke_mid'),
        (46, 9, 'smoke_light'), (47, 9, 'smoke_white'), (48, 9, 'smoke_white'), (49, 9, 'smoke_hi'), (50, 9, 'smoke_light'), (51, 9, 'smoke_dark'),
        (46, 8, 'smoke_mid'), (47, 8, 'smoke_hi'), (48, 8, 'smoke_white'), (49, 8, 'smoke_hi'), (50, 8, 'smoke_light'), (51, 8, 'smoke_mid'),
        (48, 7, 'smoke_mid'), (49, 7, 'smoke_hi'), (50, 7, 'smoke_white'), (51, 7, 'smoke_hi'), (52, 7, 'smoke_light'),
        (49, 6, 'smoke_light'), (50, 6, 'smoke_white'), (51, 6, 'smoke_white'), (52, 6, 'smoke_hi'), (53, 6, 'smoke_mid'),
        (50, 5, 'smoke_mid'), (51, 5, 'smoke_hi'), (52, 5, 'smoke_white'), (53, 5, 'smoke_hi'), (54, 5, 'smoke_dark'),
        (52, 4, 'smoke_mid'), (53, 4, 'smoke_light'), (54, 4, 'smoke_hi'), (55, 4, 'smoke_light'), (56, 4, 'smoke_dark'),
        (54, 3, 'smoke_mid'), (55, 3, 'smoke_light'), (56, 3, 'smoke_mid'),
        (56, 2, 'smoke_mid'), (57, 2, 'smoke_dark'),
    ]
    for sx, sy, scol in smoke_particles:
        p(sx, sy, PAL[scol])

    # 5. FURNACE & HEARTH (Stone forge hearth built into SW wall)
    # Hearth opening between x=42 and x=54
    for x in range(41, 56):
        base_y = 72 + (x - 34) // 2
        for y in range(base_y - 12, base_y + 1):
            dx = abs(x - 48)
            arch_inner_y = 68 + int((dx * dx) / 6.5)
            if y < arch_inner_y:
                # Stone arch surround
                if dx >= 5:
                    col = PAL['stone_light'] if x < 48 else PAL['stone_mid']
                elif y == arch_inner_y - 1:
                    col = PAL['stone_white'] if dx <= 1 else PAL['stone_bright']
                else:
                    col = PAL['stone_hi'] if (x + y) % 2 == 0 else PAL['stone_light']
                p(x, y, col)
            else:
                p(x, y, PAL['fire_black'])

    # Deep fiery heart of the furnace (fire & glowing coals)
    for x in range(43, 54):
        dx = abs(x - 48)
        base_y = 72 + (x - 34) // 2
        for y in range(base_y - 10, base_y + 1):
            dy = base_y - y
            if dy <= 2:
                # Glowing hot coal bed
                if dy == 0:
                    col = PAL['fire_crimson'] if dx >= 4 else PAL['fire_orange']
                elif dx <= 1:
                    col = PAL['fire_white']
                elif dx <= 3:
                    col = PAL['fire_yellow']
                else:
                    col = PAL['fire_amber']
            elif dy <= 5:
                # Roaring fire core
                if dx == 0:
                    col = PAL['fire_white'] if dy == 3 else PAL['fire_yellow']
                elif dx <= 2:
                    col = PAL['fire_yellow'] if dy <= 4 else PAL['fire_amber']
                elif dx <= 4:
                    col = PAL['fire_orange']
                else:
                    col = PAL['fire_red']
            elif dy <= 8:
                # Flame tips licking up
                if dx <= 1 and dy <= 7:
                    col = PAL['fire_amber']
                elif dx <= 3:
                    col = PAL['fire_orange'] if (x + y) % 2 == 0 else PAL['fire_red']
                else:
                    col = PAL['fire_dark']
            else:
                col = PAL['fire_black']
            p(x, y, col)

    # Ambient light on inner arch jambs
    for y in range(71, 79):
        p(43, y, PAL['glow_4'])
        p(42, y, PAL['glow_3'])
        p(53, y, PAL['glow_3'])
        p(54, y, PAL['glow_2'])

    # Furnace light on cobblestones in front of hearth
    for gx in range(40, 57):
        for gy in range(80, 89):
            dx = gx - 48
            dy = gy - 79
            dist = (dx * dx * 0.9 + dy * dy * 1.8) ** 0.5
            if 1.0 <= dist <= 9.0:
                cur = c.get(gx, gy)
                if cur in (PAL['cobble_dark'], PAL['cobble_mid'], PAL['cobble_light'], PAL['cobble_hi'], PAL['cobble_bright'], PAL['dirt_dark'], PAL['dirt_mid']):
                    if dist <= 3.0:
                        p(gx, gy, PAL['glow_5'] if (gx + gy) % 2 == 0 else PAL['glow_4'])
                    elif dist <= 5.5:
                        p(gx, gy, PAL['glow_4'] if (gx + gy) % 2 == 0 else PAL['glow_3'])
                    elif dist <= 7.5:
                        if (gx + gy) % 2 == 0:
                            p(gx, gy, PAL['glow_2'])
                    elif dist <= 9.0:
                        if (gx + 2 * gy) % 3 == 0:
                            p(gx, gy, PAL['glow_1'])

    # 6. BLACKSMITH ANVIL & LOG STUMP
    # Contact shadow under stump
    for sx in range(43, 51):
        for sy in range(92, 95):
            if abs(sx - 47) + (sy - 93) * 2 <= 4:
                p(sx, sy, PAL['stone_darkest'])

    # Log stump: x=44..49, y=88..93
    for x in range(44, 50):
        for y in range(88, 93):
            if y == 88:
                col = PAL['wood_hi'] if x in (46, 47) else PAL['wood_light']
            else:
                col = PAL['wood_dark'] if x in (44, 49) else (PAL['wood_warm'] if x < 47 else PAL['wood_mid'])
            p(x, y, col)

    # Anvil
    anvil_pts = [
        (44, 87, 'iron_shadow'), (45, 87, 'iron_mid'), (46, 87, 'iron_mid'), (47, 87, 'iron_mid'), (48, 87, 'iron_shadow'), (49, 87, 'iron_darkest'),
        (45, 86, 'iron_shadow'), (46, 86, 'iron_mid'), (47, 86, 'iron_light'), (48, 86, 'iron_shadow'),
        (43, 85, 'iron_mid'), (44, 85, 'iron_light'), (45, 85, 'iron_hi'), (46, 85, 'iron_hi'), (47, 85, 'iron_light'), (48, 85, 'iron_mid'), (49, 85, 'iron_shadow'), (50, 85, 'iron_darkest'),
        (43, 84, 'iron_light'), (44, 84, 'iron_hi'), (45, 84, 'iron_bright'), (46, 84, 'iron_bright'), (47, 84, 'iron_hi'), (48, 84, 'iron_light'), (49, 84, 'iron_mid'),
    ]
    for ax, ay, acol in anvil_pts:
        p(ax, ay, PAL[acol])

    # Glowing red-hot sword blade on anvil
    p(44, 83, PAL['fire_orange'])
    p(45, 83, PAL['fire_amber'])
    p(46, 83, PAL['fire_yellow'])
    p(47, 83, PAL['fire_white'])
    p(48, 83, PAL['fire_amber'])
    # Sparks
    p(46, 81, PAL['fire_yellow'])
    p(48, 80, PAL['fire_amber'])

    # Hammer
    p(49, 88, PAL['wood_pale'])
    p(50, 89, PAL['wood_pale'])
    p(51, 90, PAL['iron_hi'])
    p(51, 89, PAL['iron_light'])

    # 7. WATER QUENCH TROUGH
    # Contact shadow under trough
    for tx in range(32, 40):
        for ty in range(86, 89):
            if abs(tx - 36) + (ty - 87) * 2 <= 4:
                p(tx, ty, PAL['stone_darkest'])

    for x in range(32, 39):
        for y in range(81, 87):
            dx = abs(x - 35)
            dy = y - 81
            if y == 86:
                col = PAL['wood_dark']
            elif x in (32, 38):
                col = PAL['wood_dark'] if dy % 2 == 0 else PAL['wood_mid']
            elif y == 81:
                col = PAL['wood_warm'] if dx <= 1 else PAL['wood_mid']
            else:
                if dx == 0 and dy == 2:
                    col = PAL['water_sparkle']
                elif dy <= 2:
                    col = PAL['water_hi'] if dx <= 1 else PAL['water_light']
                elif dy <= 4:
                    col = PAL['water_mid']
                else:
                    col = PAL['water_dark']
            p(x, y, col)
    for x in range(32, 39):
        p(x, 84, PAL['iron_light'] if x < 35 else PAL['iron_shadow'])

    # 8. STACKED BARRELS (3 wooden barrels beside the door)
    # Contact shadows under barrels
    for sx in range(79, 93):
        for sy in range(83, 86):
            if (sx >= 79 and sx <= 85 and sy in (84, 85)) or (sx >= 85 and sx <= 92 and sy in (82, 83)):
                p(sx, sy, PAL['stone_darkest'])

    def draw_barrel(bx, by):
        for ox in range(-3, 4):
            for oy in range(-7, 2):
                x = bx + ox
                y = by + oy
                abs_ox = abs(ox)
                if abs_ox == 3 and (oy in (-7, 1)):
                    continue
                if oy in (-7, -6):
                    if abs_ox <= 2:
                        col = PAL['wood_warm'] if ox <= 0 else PAL['wood_mid']
                        if abs_ox == 2: col = PAL['wood_dark']
                        p(x, y, col)
                    continue
                is_hoop = (oy in (-4, 0))
                if abs_ox == 3 or oy == 1:
                    col = PAL['wood_black']
                elif is_hoop:
                    col = PAL['iron_light'] if ox < 0 else PAL['iron_shadow']
                else:
                    if ox == -2: col = PAL['wood_hi']
                    elif ox == -1: col = PAL['wood_light']
                    elif ox == 0: col = PAL['wood_warm']
                    elif ox == 1: col = PAL['wood_mid']
                    else: col = PAL['wood_dark']
                p(x, y, col)

    draw_barrel(88, 81) # bottom back
    draw_barrel(82, 84) # bottom front
    draw_barrel(85, 75) # top barrel

    # Firewood logs stacked beside barrels (x=93..98, y=78..82)
    wood_logs = [
        (93, 82, 'wood_pale'), (94, 82, 'wood_warm'), (95, 82, 'wood_mid'), (96, 82, 'wood_dark'),
        (94, 81, 'wood_hi'), (95, 81, 'wood_pale'), (96, 81, 'wood_warm'), (97, 81, 'wood_mid'),
        (94, 80, 'wood_pale'), (95, 80, 'wood_warm'), (96, 80, 'wood_mid'),
    ]
    for lx, ly, lcol in wood_logs:
        p(lx, ly, PAL[lcol])

    # 9. WOODEN SIGN (Blacksmith trade sign)
    # Shadow behind sign on wall
    for sx in range(68, 76):
        p(sx, 65, PAL['stone_darkest'])

    # Ornamental iron bracket
    for bx in range(67, 74):
        p(bx, 55, PAL['iron_light'] if bx in (69, 70) else PAL['iron_mid'])
    p(67, 56, PAL['iron_darkest'])
    p(68, 57, PAL['iron_shadow'])
    p(68, 56, PAL['iron_light'])
    p(68, 57, PAL['iron_mid'])
    p(72, 56, PAL['iron_light'])
    p(72, 57, PAL['iron_mid'])

    # Wooden signboard
    for sx in range(67, 75):
        for sy in range(58, 65):
            if sx in (67, 74) or sy in (58, 64):
                col = PAL['wood_black']
            else:
                col = PAL['wood_light'] if sx < 71 else PAL['wood_warm']
            p(sx, sy, col)

    # Golden Anvil emblem on sign
    p(69, 61, PAL['fire_amber'])
    p(70, 61, PAL['fire_yellow'])
    p(71, 61, PAL['fire_yellow'])
    p(72, 61, PAL['fire_amber'])
    p(70, 62, PAL['fire_amber'])
    p(70, 63, PAL['wood_black'])
    p(71, 63, PAL['wood_black'])

    return c

c = build_forge()
print("Colors used:", c.stats()['colors_used'])
view(c)
finish(c)
