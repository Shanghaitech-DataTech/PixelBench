import math
import random
from pixelbench_api import new_canvas, view, finish

def draw_cyberpunk_alley():
    c = new_canvas(128, 128, background='#05060b')
    
    # -------------------------------------------------------------------------
    # STRICT COHESIVE PALETTE (Aiming for ~46 total colors, max 86)
    # -------------------------------------------------------------------------
    C_VOID         = '#05060b'
    C_BG1          = '#090c16'
    C_BG2          = '#101422'
    C_BG3          = '#181e30'
    C_BG4          = '#232b42'
    C_BG5          = '#313c59'
    C_BG6          = '#455375'
    C_SKY1         = '#0b0e1c'
    C_SKY2         = '#14182e'
    C_HAZE         = '#241a38'
    C_HAZE_BRIGHT  = '#422459'
    C_HAZE_GLOW    = '#6b337d'
    C_ROAD         = '#080a10'
    C_ROAD_WET     = '#111522'
    C_CURB         = '#333c52'
    
    # Pink / Magenta Neon
    P_SHADOW       = '#240412'
    P_DARK         = '#5c0a32'
    P_MID          = '#b81465'
    P_BRIGHT       = '#ff1f87'
    P_LIGHT        = '#ff6bb0'
    P_PALE         = '#ffb8da'
    P_WHITE        = '#ffeef6'
    
    # Cyan / Electric Blue Neon
    C_CYAN_SHADOW  = '#01121a'
    C_CYAN_DARK    = '#00435c'
    C_CYAN_MID     = '#008ba8'
    C_CYAN_BRIGHT  = '#00d0f0'
    C_CYAN_LIGHT   = '#60e6ff'
    C_CYAN_PALE    = '#b8f5ff'
    WHITE          = '#ffffff'
    
    # Amber / Orange / Warm Shop Glow
    A_SHADOW       = '#200c00'
    A_DARK         = '#4d1e00'
    A_MID          = '#a34700'
    A_BRIGHT       = '#ff7a00'
    A_YELLOW       = '#ffc000'
    A_LIGHT        = '#ffe066'
    A_WHITE        = '#fff7d9'
    
    # Neon Green
    G_DARK         = '#004724'
    G_BRIGHT       = '#00e676'
    G_LIGHT        = '#99ffd0'
    
    # Red Accent
    R_DARK         = '#4a0810'
    R_MID          = '#b81428'
    R_BRIGHT       = '#ff2b44'
    
    # Translucent Umbrella / Glass / Water Specular
    U_TINT_P       = '#221326'
    U_TINT_C       = '#0f202c'
    U_EDGE         = '#50607a'
    U_HIGHLIGHT    = '#8aa0c4'
    U_BRIGHT       = '#c0d6f0'
    U_PALE         = '#e8f2fc'
    
    # Skin
    SKIN           = '#d99379'

    # -------------------------------------------------------------------------
    # 1. SKY & DISTANT MEGACITY (Center alley gap: x=32..94, y=0..76)
    # -------------------------------------------------------------------------
    for y in range(0, 77):
        if y < 18:
            scol = C_SKY1
        elif y < 36:
            scol = C_SKY2
        elif y < 52:
            scol = C_HAZE
        elif y < 64:
            scol = C_HAZE_BRIGHT
        else:
            scol = C_HAZE_GLOW
        c.line(32, y, 94, y, scol)
        
    # Distant towering skyscraper monolith (x: 54..72, y: 0..52)
    c.rect(54, 4, 18, 48, C_BG1)
    c.rect(58, 0, 10, 52, C_BG2)
    c.line(62, 0, 62, 52, C_BG3)
    # Spire aviation lights
    c.set(62, 0, R_BRIGHT)
    c.set(62, 1, R_MID)
    c.set(62, 5, R_BRIGHT)
    
    # Secondary distant spire left
    c.rect(38, 16, 12, 36, C_VOID)
    c.rect(40, 12, 7, 40, C_BG1)
    c.set(43, 11, R_BRIGHT)

    # Windows on distant skyscraper
    for wy in range(8, 46, 3):
        if wy % 6 == 0:
            c.set(56, wy, A_LIGHT)
            c.set(65, wy, C_CYAN_LIGHT)
        elif wy % 9 == 0:
            c.set(60, wy, P_LIGHT)
            c.set(68, wy, A_YELLOW)
        else:
            c.set(55, wy, C_BG4)
            c.set(67, wy, C_BG4)

    # Distant Elevated Monorail Track (y: 45..50)
    c.rect(32, 45, 64, 6, C_BG2)
    c.line(32, 45, 96, 45, C_BG4)
    c.line(32, 50, 96, 50, C_BG1)
    # Distant speeder light trails on monorail
    c.line(42, 47, 54, 47, R_BRIGHT)
    c.line(60, 47, 74, 47, C_CYAN_LIGHT)
    c.line(78, 47, 86, 47, A_YELLOW)

    # Distant Cross-Street / Alley Exit (y: 56..76)
    # Natural architectural silhouettes across the back gap
    c.rect(40, 56, 16, 20, C_BG1) # distant building left
    c.rect(72, 55, 20, 21, C_BG1) # distant building right
    c.line(40, 56, 56, 56, C_BG3)
    c.line(72, 55, 92, 55, C_BG3)
    
    # Distant shop signs in the cross-street gap (x: 54..74, y: 58..74)
    c.rect(53, 62, 6, 9, C_VOID)
    c.rect(53, 62, 6, 9, R_DARK, fill=False)
    c.line(54, 64, 57, 64, R_BRIGHT)
    c.line(55, 66, 57, 66, R_BRIGHT)
    
    c.rect(67, 60, 5, 11, C_VOID)
    c.rect(67, 60, 5, 11, C_CYAN_DARK, fill=False)
    c.line(68, 62, 70, 62, C_CYAN_LIGHT)
    c.line(68, 66, 70, 66, C_CYAN_LIGHT)
    
    # Warm amber glow in distant alley street level
    c.line(56, 72, 68, 72, A_MID)
    c.line(58, 73, 66, 73, A_LIGHT)
    c.line(54, 74, 72, 74, C_HAZE_GLOW)

    # -------------------------------------------------------------------------
    # 2. LEFT BUILDING COMPLEX (x: 0..46)
    # -------------------------------------------------------------------------
    c.rect(0, 0, 36, 128, C_BG1)
    c.poly([(36, 0), (46, 74), (46, 127), (0, 127), (0, 0)], C_BG1)
    
    c.line(16, 0, 16, 127, C_BG2)
    c.line(28, 0, 28, 72, C_BG2)
    c.line(38, 0, 46, 74, C_BG3)
    c.line(39, 0, 47, 74, C_BG2)
    
    for gy in (16, 34, 52):
        c.line(0, gy, 38, gy, C_BG2)

    # Windows on left building
    for wy in (8, 22):
        c.rect(6, wy, 8, 8, C_VOID)
        c.rect(7, wy+1, 6, 6, C_BG2)
        if wy == 8:
            c.line(7, wy+3, 12, wy+3, A_MID)
            c.set(9, wy+2, A_LIGHT)
        else:
            c.line(7, wy+4, 12, wy+4, C_CYAN_DARK)
            c.set(10, wy+3, C_CYAN_MID)

    # AC Unit 1
    c.rect(23, 24, 10, 7, C_BG3)
    c.rect(24, 25, 8, 5, C_BG2)
    c.circle(27, 27, 2, C_BG1)
    c.line(30, 26, 31, 26, C_BG4)
    c.line(30, 28, 31, 28, C_BG4)
    c.line(24, 31, 24, 38, C_BG4)
    c.set(24, 39, C_CYAN_LIGHT)

    # Metal Catwalk / Fire Escape Balcony
    c.rect(14, 39, 22, 2, C_BG4)
    c.line(14, 36, 36, 36, C_BG5)
    for rx in (16, 21, 26, 31, 35):
        c.line(rx, 36, rx, 39, C_BG3)
        
    # Vertical piping
    c.line(34, 0, 34, 70, C_BG4)
    c.line(35, 0, 35, 70, C_BG2)
    for by in (14, 32, 50, 66):
        c.rect(33, by, 3, 2, C_BG6)

    # -------------------------------------------------------------------------
    # 3. RIGHT BUILDING COMPLEX (x: 82..127)
    # -------------------------------------------------------------------------
    c.rect(92, 0, 36, 128, C_BG1)
    c.poly([(92, 0), (82, 72), (82, 127), (127, 127), (127, 0)], C_BG1)
    
    c.line(92, 0, 82, 72, C_BG3)
    c.line(91, 0, 81, 72, C_BG2)
    c.rect(108, 0, 20, 128, C_BG2)
    c.line(108, 0, 108, 127, C_BG4)

    # Roof water tank & antenna
    c.rect(102, 4, 12, 10, C_BG2)
    c.line(101, 3, 114, 3, C_BG4)
    c.line(104, 14, 104, 18, C_BG3)
    c.line(111, 14, 111, 18, C_BG3)
    c.line(120, 0, 120, 14, C_BG5)
    c.set(120, 0, R_BRIGHT)

    # Transformer box
    c.rect(86, 48, 11, 14, C_BG3)
    c.rect(87, 49, 9, 12, C_BG2)
    c.rect(89, 53, 5, 4, A_YELLOW)
    c.set(90, 54, C_VOID); c.set(92, 54, C_VOID)
    c.set(91, 55, C_VOID); c.set(93, 55, C_VOID)
    c.line(88, 62, 88, 72, C_BG4)
    c.line(91, 62, 91, 72, C_BG3)

    # -------------------------------------------------------------------------
    # 4. NEON SHOP SIGNS
    # -------------------------------------------------------------------------
    
    # Left Vertical Neon Sign: "カプセル" (Capsule)
    c.line(26, 17, 34, 17, C_BG5)
    c.line(26, 53, 34, 53, C_BG5)
    c.line(30, 21, 34, 17, C_BG3)
    c.line(30, 49, 34, 53, C_BG3)
    
    c.rect(34, 14, 11, 43, C_VOID)
    c.rect(34, 14, 11, 43, P_DARK, fill=False)
    c.rect(35, 15, 9, 41, P_MID, fill=False)
    
    # 1. カ
    c.line(37, 17, 42, 17, P_LIGHT)
    c.line(40, 17, 39, 23, P_LIGHT)
    c.line(42, 17, 42, 20, P_LIGHT)
    c.set(38, 20, P_LIGHT)
    c.set(40, 17, P_WHITE)
    
    # 2. プ
    c.line(37, 26, 42, 26, C_CYAN_LIGHT)
    c.line(37, 26, 37, 31, C_CYAN_LIGHT)
    c.set(43, 25, C_CYAN_LIGHT)
    c.set(39, 26, WHITE)
    c.set(37, 28, WHITE)
    
    # 3. セ
    c.line(37, 35, 42, 35, P_LIGHT)
    c.line(39, 34, 39, 40, P_LIGHT)
    c.line(42, 35, 42, 40, P_LIGHT)
    c.line(39, 40, 42, 40, P_LIGHT)
    c.set(39, 35, P_WHITE)
    
    # 4. ル
    c.line(38, 43, 38, 47, C_CYAN_LIGHT)
    c.line(41, 43, 41, 48, C_CYAN_LIGHT)
    c.line(41, 48, 43, 48, C_CYAN_LIGHT)
    c.set(41, 45, WHITE)
    
    # Emblem
    c.poly([(39, 51), (41, 49), (43, 51), (41, 53)], P_BRIGHT, fill=False)
    c.set(41, 51, P_WHITE)
    
    for sy in range(14, 57, 2):
        c.set(33, sy, P_DARK)
        if sy % 4 == 0:
            c.set(32, sy, P_SHADOW)

    # Left Lower "24H" Neon Sign
    c.rect(17, 56, 14, 7, C_VOID)
    c.rect(17, 56, 14, 7, G_DARK, fill=False)
    c.line(18, 56, 30, 56, G_BRIGHT)
    c.line(18, 62, 30, 62, G_BRIGHT)
    # 2
    c.line(19, 58, 21, 58, G_LIGHT); c.set(21, 59, G_LIGHT)
    c.line(19, 60, 21, 60, G_LIGHT); c.set(19, 61, G_LIGHT); c.line(19, 61, 21, 61, G_LIGHT)
    # 4
    c.line(23, 58, 23, 60, G_LIGHT); c.line(23, 60, 25, 60, G_LIGHT); c.line(25, 58, 25, 61, G_LIGHT)
    # H
    c.line(27, 58, 27, 61, G_LIGHT); c.set(28, 59, G_LIGHT); c.line(29, 58, 29, 61, G_LIGHT)

    # Right Cyber Holographic Billboard
    c.rect(94, 16, 31, 26, C_VOID)
    c.rect(93, 15, 33, 28, C_CYAN_DARK, fill=False)
    c.rect(94, 16, 31, 26, C_CYAN_MID, fill=False)
    c.line(95, 17, 123, 17, C_CYAN_BRIGHT)
    c.line(95, 40, 123, 40, C_CYAN_BRIGHT)
    
    hex_pts = [(109, 21), (116, 25), (116, 33), (109, 37), (102, 33), (102, 25)]
    c.poly(hex_pts, C_CYAN_SHADOW, fill=True)
    c.poly(hex_pts, C_CYAN_MID, fill=False)
    c.poly([(104, 29), (109, 25), (114, 29), (109, 33)], C_CYAN_LIGHT, fill=False)
    c.rect(108, 28, 3, 3, P_BRIGHT)
    c.set(109, 29, WHITE)
    c.line(96, 21, 100, 21, C_CYAN_DARK)
    c.line(96, 35, 100, 35, C_CYAN_DARK)
    c.line(97, 38, 104, 38, C_CYAN_LIGHT)
    c.line(114, 38, 121, 38, C_CYAN_LIGHT)
    for sy in range(16, 43, 2):
        c.set(92, sy, C_CYAN_DARK)

    # -------------------------------------------------------------------------
    # 5. NOODLE / RAMEN SHOP FRONT (Left: y=68..92, x=0..46)
    # -------------------------------------------------------------------------
    # Clean corrugated awning roof
    c.poly([(2, 68), (44, 71), (46, 77), (2, 74)], A_DARK)
    for ax in range(4, 44, 4):
        c.line(ax, 69, ax + 2, 76, A_MID)
    # Glowing neon edge
    c.line(2, 74, 46, 77, A_YELLOW)
    c.line(2, 75, 46, 78, A_DARK)

    # Warm amber glow pouring from shop interior
    for wy in range(77, 92):
        c.line(4, wy, 44, wy, A_SHADOW)
    for wy in range(78, 88):
        c.line(8, wy, 40, wy, A_DARK)
        
    # Open kitchen window
    c.rect(10, 78, 28, 9, C_VOID)
    c.rect(12, 79, 24, 7, A_MID)
    c.rect(14, 80, 20, 5, A_BRIGHT)
    c.rect(16, 81, 16, 3, A_LIGHT)
    c.line(18, 82, 30, 82, A_WHITE)
    
    # Split Noren curtains
    for nx in (12, 18, 24, 30):
        c.rect(nx, 76, 4, 3, C_BG2)
        c.set(nx + 1, 77, WHITE)
        
    # Silhouettes
    c.circle(21, 81, 2, C_VOID)
    c.rect(18, 83, 6, 4, C_VOID)
    c.rect(28, 83, 4, 2, C_BG4)
    
    # Steam rising
    c.set(26, 79, U_BRIGHT)
    c.set(27, 78, U_HIGHLIGHT)
    c.set(25, 77, U_EDGE)

    # Red Paper Lantern
    c.line(42, 76, 42, 78, C_VOID)
    c.rect(40, 78, 5, 7, R_MID)
    c.rect(41, 79, 3, 5, R_BRIGHT)
    c.set(42, 81, A_LIGHT)
    c.line(40, 85, 44, 85, R_DARK)
    c.set(39, 81, A_DARK); c.set(45, 81, A_DARK)

    # -------------------------------------------------------------------------
    # 6. VENDING MACHINES (Right: x=82..118, y=66..96)
    # -------------------------------------------------------------------------
    c.rect(82, 65, 42, 31, C_BG1)
    c.line(82, 65, 124, 65, C_BG3)
    
    # Machine 1 (Cyan Theme)
    c.rect(84, 67, 15, 28, C_BG2)
    c.rect(84, 67, 15, 28, C_CYAN_DARK, fill=False)
    c.rect(86, 69, 11, 4, C_CYAN_MID)
    c.line(87, 70, 95, 70, C_CYAN_PALE)
    c.line(87, 71, 95, 71, C_CYAN_LIGHT)
    c.rect(86, 75, 11, 10, C_VOID)
    # Cans row 1
    c.set(87, 76, R_BRIGHT); c.set(87, 77, R_BRIGHT)
    c.set(89, 76, C_CYAN_BRIGHT); c.set(89, 77, C_CYAN_BRIGHT)
    c.set(91, 76, A_LIGHT); c.set(91, 77, A_LIGHT)
    c.set(93, 76, G_BRIGHT); c.set(93, 77, G_BRIGHT)
    c.set(95, 76, WHITE); c.set(95, 77, WHITE)
    c.line(86, 78, 96, 78, C_BG3)
    c.set(87, 79, C_CYAN_LIGHT); c.set(89, 79, C_CYAN_LIGHT); c.set(91, 79, C_CYAN_LIGHT); c.set(93, 79, C_CYAN_LIGHT); c.set(95, 79, C_CYAN_LIGHT)
    # Cans row 2
    c.set(87, 81, A_YELLOW); c.set(87, 82, A_YELLOW)
    c.set(89, 81, P_BRIGHT); c.set(89, 82, P_BRIGHT)
    c.set(91, 81, C_CYAN_BRIGHT); c.set(91, 82, C_CYAN_BRIGHT)
    c.set(93, 81, R_BRIGHT); c.set(93, 82, R_BRIGHT)
    c.set(95, 81, G_BRIGHT); c.set(95, 82, G_BRIGHT)
    c.line(86, 83, 96, 83, C_BG3)
    c.set(87, 84, A_LIGHT); c.set(89, 84, P_LIGHT); c.set(91, 84, C_CYAN_LIGHT); c.set(93, 84, C_CYAN_LIGHT); c.set(95, 84, G_LIGHT)
    c.rect(86, 86, 4, 3, C_BG3)
    c.set(87, 87, A_LIGHT)
    c.rect(86, 90, 11, 4, C_VOID)
    c.line(86, 90, 96, 90, C_BG4)
    c.set(91, 92, C_CYAN_LIGHT)

    # Machine 2 (Pink Theme)
    c.rect(101, 69, 15, 26, C_BG2)
    c.rect(101, 69, 15, 26, P_DARK, fill=False)
    c.rect(103, 71, 11, 4, P_MID)
    c.line(104, 72, 112, 72, P_WHITE)
    c.line(104, 73, 112, 73, P_LIGHT)
    c.rect(103, 77, 11, 8, C_VOID)
    c.set(104, 78, P_BRIGHT); c.set(104, 79, P_BRIGHT)
    c.set(106, 78, A_LIGHT); c.set(106, 79, A_LIGHT)
    c.set(108, 78, P_WHITE); c.set(108, 79, P_WHITE)
    c.set(110, 78, C_CYAN_BRIGHT); c.set(110, 79, C_CYAN_BRIGHT)
    c.set(112, 78, P_BRIGHT); c.set(112, 79, P_BRIGHT)
    c.line(103, 80, 113, 80, C_BG3)
    c.set(104, 81, P_LIGHT); c.set(106, 81, A_LIGHT); c.set(108, 81, WHITE); c.set(110, 81, C_CYAN_LIGHT); c.set(112, 81, P_LIGHT)
    c.rect(103, 88, 11, 5, C_VOID)
    c.line(103, 88, 113, 88, P_MID)
    c.set(105, 85, G_BRIGHT)

    c.rect(118, 79, 6, 16, C_BG2)
    c.rect(119, 77, 4, 2, C_BG4)
    c.circle(121, 82, 1, C_VOID)

    # -------------------------------------------------------------------------
    # 7. POWER CABLES & WIRES
    # -------------------------------------------------------------------------
    def draw_smooth_cable(x0, y0, x1, y1, sag, col):
        steps = 60
        prev_x, prev_y = x0, y0
        for i in range(1, steps + 1):
            t = i / float(steps)
            cur_x = int(round(x0 + t * (x1 - x0)))
            cur_y = int(round(y0 + t * (y1 - y0) + 4 * sag * t * (1.0 - t)))
            c.line(prev_x, prev_y, cur_x, cur_y, col)
            prev_x, prev_y = cur_x, cur_y

    draw_smooth_cable(22, 12, 104, 18, 10, C_BG1)
    draw_smooth_cable(22, 13, 104, 19, 10, C_BG3)
    
    draw_smooth_cable(26, 22, 94, 26, 15, C_BG1)
    draw_smooth_cable(26, 23, 94, 27, 15, C_BG4)
    
    draw_smooth_cable(34, 38, 90, 42, 18, C_BG1)
    draw_smooth_cable(34, 39, 90, 43, 18, C_BG3)
    
    draw_smooth_cable(40, 52, 88, 50, 12, C_BG2)
    c.line(36, 17, 36, 32, C_BG3)

    # -------------------------------------------------------------------------
    # 8. GROUND, PAVEMENT & REFLECTIVE PUDDLES (y: 84 to 127)
    # -------------------------------------------------------------------------
    for y in range(84, 128):
        c.line(0, y, 127, y, C_VOID)
        
    # Perspective Curbs
    for y in range(84, 128):
        t = (y - 84) / 44.0
        left_curb = int(44 - t * 28)
        c.rect(0, y, max(0, left_curb), 1, C_BG1)
        if 0 <= left_curb < 128:
            c.set(left_curb, y, C_CURB)
        
        right_curb = int(80 + t * 36)
        if right_curb < 128:
            c.rect(right_curb, y, 128 - right_curb, 1, C_BG1)
            c.set(right_curb, y, C_CURB)

    # Wet asphalt pavement base texture
    for y in range(85, 128, 2):
        c.line(22, y, 108, y, C_ROAD_WET)

    # Storm Drain Grate
    c.rect(38, 116, 9, 7, C_VOID)
    c.rect(38, 116, 9, 7, C_BG3, fill=False)
    for gy in range(117, 122):
        c.line(39, gy, 45, gy, C_BG4)
        c.set(42, gy, C_VOID)

    # -------------------------------------------------------------------------
    # ORGANIC PUDDLE POOLS & NEON REFLECTIONS
    # -------------------------------------------------------------------------
    
    # Puddle 1: Left Puddle (Warm Ramen & Hotel Sign Reflection)
    # y from 86 to 126, x from 22 to 46
    for y in range(86, 126):
        # Amber ramen light reflection (x: 24..34)
        if y < 110:
            rx_a = 29 + int(math.sin(y * 0.5) * 1.5)
            w_a = 3 if y % 2 == 0 else 2
            c.line(rx_a - w_a, y, rx_a + w_a, y, A_MID if y % 2 == 0 else A_DARK)
            if y % 4 == 0:
                c.set(rx_a, y, A_LIGHT)
                c.set(rx_a - w_a - 1, y, A_SHADOW)
                c.set(rx_a + w_a + 1, y, A_SHADOW)

        # Pink / Cyan vertical sign reflection (x: 36..46)
        rx_p = 39 + int(math.sin(y * 0.75) * 2.0)
        is_even = (y % 2 == 0)
        if 88 <= y <= 98:
            col_core, col_light, col_edge = P_MID, P_LIGHT, P_DARK
        elif 99 <= y <= 108:
            col_core, col_light, col_edge = C_CYAN_MID, C_CYAN_LIGHT, C_CYAN_DARK
        elif 109 <= y <= 118:
            col_core, col_light, col_edge = P_MID, P_LIGHT, P_DARK
        else:
            col_core, col_light, col_edge = C_CYAN_MID, C_CYAN_LIGHT, C_CYAN_DARK
            
        w_p = 3 if is_even else 2
        c.line(rx_p - w_p, y, rx_p + w_p, y, col_core if is_even else col_edge)
        if is_even and y % 4 == 0:
            c.set(rx_p, y, col_light)
            c.set(rx_p - w_p - 1, y, col_edge)
            c.set(rx_p + w_p + 1, y, col_edge)

    # Puddle 2: Right Puddle (Vending Machine Reflections)
    # y from 95 to 126, x from 84 to 118
    for y in range(95, 126):
        is_even = (y % 2 == 0)
        # Cyan machine
        rx_c = 91 + int(math.cos(y * 0.65) * 2.0)
        w_c = 3 if is_even else 2
        c.line(rx_c - w_c, y, rx_c + w_c, y, C_CYAN_MID if is_even else C_CYAN_DARK)
        if is_even and y % 4 == 0:
            c.set(rx_c, y, C_CYAN_LIGHT)
            c.set(rx_c - w_c - 1, y, C_CYAN_DARK)
            c.set(rx_c + w_c + 1, y, C_CYAN_DARK)

        # Pink machine
        rx_m = 107 + int(math.sin(y * 0.6) * 1.8)
        if rx_m < 125:
            w_m = 2 if is_even else 1
            c.line(rx_m - w_m, y, min(127, rx_m + w_m), y, P_MID if is_even else P_DARK)
            if is_even and y % 4 == 2:
                c.set(rx_m, y, P_LIGHT)

    # Puddle 3: Central Reflective Pool (x: 48..82, y: 96..124)
    # Specular water sheen and reflections of the distant sky / umbrella rim
    c.line(54, 98, 74, 99, C_BG5)
    c.line(74, 99, 81, 105, C_BG4)
    c.line(50, 118, 68, 122, C_BG4)
    c.line(68, 122, 78, 117, C_BG3)
    
    # Ripple lines in central pool
    c.line(56, 103, 66, 103, U_HIGHLIGHT)
    c.set(61, 103, C_CYAN_LIGHT)
    c.line(53, 112, 63, 112, U_EDGE)
    c.set(58, 112, P_LIGHT)
    c.line(70, 109, 76, 109, C_CYAN_DARK)
    c.set(73, 109, C_CYAN_LIGHT)

    # -------------------------------------------------------------------------
    # 9. ONE PERSON WITH TRANSPARENT UMBRELLA (x: 52..74, y: 72..112)
    # -------------------------------------------------------------------------
    
    # A. Boots & Footstep Splashes
    # Left boot
    c.rect(56, 108, 4, 3, C_VOID)
    c.line(56, 110, 59, 110, C_BG5)
    c.line(59, 100, 58, 109, C_BG1)
    c.line(60, 100, 59, 109, C_BG3)
    
    # Ripple rings where boot splashes in water
    c.ellipse(58, 111, 4, 1, C_CYAN_LIGHT, fill=False)
    c.ellipse(58, 111, 7, 2, C_BG3, fill=False)

    # Right boot
    c.rect(64, 106, 4, 3, C_VOID)
    c.line(64, 108, 67, 108, C_BG5)
    c.line(64, 100, 65, 107, C_BG1)
    c.line(63, 100, 64, 107, C_BG3)

    # B. Cyberpunk Trenchcoat / Jacket (y: 83..102)
    coat_poly = [
        (58, 83), (66, 83),
        (69, 93),
        (73, 101),
        (53, 102),
        (56, 93)
    ]
    c.poly(coat_poly, C_BG1)
    
    # Coat folds & 3D structure
    c.line(59, 84, 55, 101, C_VOID)
    c.line(65, 84, 71, 100, C_VOID)
    c.line(62, 84, 62, 99, C_BG2)
    c.line(61, 85, 60, 96, C_BG3)
    c.line(63, 85, 64, 96, C_BG3)
    
    # Cybernetic glowing circuit data-stripe
    c.line(68, 87, 70, 99, C_CYAN_BRIGHT)
    c.set(70, 100, WHITE)
    c.set(68, 86, C_CYAN_LIGHT)
    
    # Left edge warm / pink rim light
    c.line(55, 96, 54, 101, P_MID)
    c.set(53, 102, P_LIGHT)
    c.set(54, 92, A_MID)

    # C. Torso & High Collar
    c.rect(58, 80, 8, 4, C_BG1)
    c.line(57, 78, 59, 83, C_BG3)
    c.line(67, 78, 65, 83, C_BG3)
    c.set(57, 78, P_LIGHT)
    c.set(67, 78, C_CYAN_LIGHT)

    # D. Head & Hair (visible through transparent umbrella!)
    c.rect(60, 75, 5, 5, C_VOID)
    c.set(59, 76, C_BG1)
    c.set(64, 76, C_BG3)
    c.line(60, 78, 64, 78, C_BG2)
    c.set(64, 77, C_CYAN_BRIGHT) # cyber implant

    # Right arm & umbrella shaft
    c.line(67, 84, 68, 77, C_BG1)
    c.line(68, 77, 65, 74, C_BG3)
    c.line(63, 67, 63, 75, C_BG6)
    c.line(63, 75, 63, 79, C_BG4)
    c.rect(62, 73, 2, 2, SKIN)

    # E. TRANSPARENT UMBRELLA CANOPY (x: 47..79, y: 64..77)
    dome_coords = []
    rim_coords = []
    for x in range(47, 80):
        dx = (x - 63) / 16.0
        yt = int(round(64 + 11 * (dx * dx)))
        yb = int(round(76 - 2 * (1.0 - dx * dx)))
        dome_coords.append((x, yt))
        rim_coords.append((x, yb))

    # Translucent glass tint inside umbrella
    for (x, yt), (_, yb) in zip(dome_coords, rim_coords):
        for y in range(yt + 1, yb):
            if (x + y) % 3 == 0:
                tint_col = U_TINT_P if x < 62 else U_TINT_C
                c.set(x, y, tint_col)

    # Umbrella Ribs
    for t in range(12):
        u = t / 11.0
        rx = int(round(63 + u * (53 - 63)))
        ry = int(round(64 + u * (76 - 64) + 2 * u * (1 - u)))
        c.set(rx, ry, P_DARK)
    for t in range(12):
        u = t / 11.0
        rx = int(round(63 + u * (58 - 63)))
        ry = int(round(64 + u * (77 - 64)))
        c.set(rx, ry, U_EDGE)
    for t in range(12):
        u = t / 11.0
        rx = int(round(63 + u * (68 - 63)))
        ry = int(round(64 + u * (77 - 64)))
        c.set(rx, ry, C_CYAN_DARK)
    for t in range(12):
        u = t / 11.0
        rx = int(round(63 + u * (73 - 63)))
        ry = int(round(64 + u * (76 - 64) + 2 * u * (1 - u)))
        c.set(rx, ry, C_CYAN_DARK)

    # Apex Cap
    c.rect(62, 63, 3, 2, C_BG6)
    c.set(63, 62, WHITE)

    # Outer curved rim of dome
    for x, y in dome_coords:
        if x < 58:
            c.set(x, y, P_LIGHT)
            if x in (49, 50, 54, 55):
                c.set(x, y, P_WHITE)
                c.set(x, y + 1, P_MID)
        elif 58 <= x <= 67:
            c.set(x, y, WHITE)
            c.set(x, y + 1, U_HIGHLIGHT)
        else:
            c.set(x, y, C_CYAN_BRIGHT)
            if x in (70, 71, 75, 76):
                c.set(x, y, WHITE)
                c.set(x, y + 1, C_CYAN_MID)

    # Bottom curved rim of umbrella
    for x, y in rim_coords:
        if x < 58:
            c.set(x, y, P_MID)
        elif x > 67:
            c.set(x, y, C_CYAN_MID)
        else:
            c.set(x, y, U_EDGE)

    # Rib tips
    c.set(47, 75, P_WHITE)
    c.set(53, 76, P_LIGHT)
    c.set(58, 77, U_BRIGHT)
    c.set(68, 77, C_CYAN_LIGHT)
    c.set(73, 76, C_CYAN_LIGHT)
    c.set(79, 75, WHITE)

    # Dripping water droplets
    c.set(47, 77, P_LIGHT); c.set(47, 80, P_DARK)
    c.set(79, 77, C_CYAN_LIGHT); c.set(79, 81, C_CYAN_DARK)
    c.set(68, 79, U_BRIGHT)

    # Raindrops splashing on transparent canopy
    c.set(56, 66, WHITE)
    c.set(57, 65, P_LIGHT)
    c.set(65, 65, WHITE)
    c.set(66, 64, C_CYAN_LIGHT)
    c.set(71, 68, WHITE)

    # -------------------------------------------------------------------------
    # 10. RAIN STREAKS & SPLASHES
    # -------------------------------------------------------------------------
    def draw_rain_streak(rx, ry, length, col):
        for step in range(length):
            px = rx - step // 3
            py = ry + step
            if 0 <= px < 128 and 0 <= py < 128:
                if 34 <= px <= 44 and 14 <= py <= 56:
                    continue
                if 84 <= px <= 116 and 67 <= py <= 96:
                    continue
                if 10 <= px <= 38 and 78 <= py <= 88:
                    continue
                if 53 <= px <= 73 and 83 <= py <= 104:
                    continue
                c.set(px, py, col)

    rng = random.Random(2077)
    
    for _ in range(180):
        rx = rng.randint(0, 134)
        ry = rng.randint(0, 122)
        rlen = rng.randint(3, 5)
        
        if 28 <= rx <= 48 and 10 <= ry <= 65:
            col = rng.choice([P_MID, P_LIGHT, P_DARK])
        elif 90 <= rx <= 126 and 14 <= ry <= 44:
            col = rng.choice([C_CYAN_MID, C_CYAN_LIGHT, C_CYAN_DARK])
        elif 80 <= rx <= 124 and 60 <= ry <= 100:
            col = rng.choice([C_CYAN_LIGHT, P_LIGHT, C_CYAN_MID])
        elif 6 <= rx <= 46 and 68 <= ry <= 92:
            col = rng.choice([A_MID, A_LIGHT, A_DARK])
        elif 46 <= rx <= 80 and 58 <= ry <= 76:
            col = rng.choice([U_BRIGHT, WHITE, U_HIGHLIGHT])
        else:
            col = rng.choice([C_BG4, C_BG5, U_EDGE])
            
        draw_rain_streak(rx, ry, rlen, col)

    # Splashes on ground
    for _ in range(35):
        sx = rng.randint(14, 116)
        sy = rng.randint(86, 126)
        if 34 <= sx <= 46:
            scol = P_LIGHT if rng.random() > 0.5 else P_MID
        elif 84 <= sx <= 114:
            scol = C_CYAN_LIGHT if rng.random() > 0.5 else C_CYAN_MID
        elif 16 <= sx <= 34:
            scol = A_LIGHT
        else:
            scol = C_BG6
        c.set(sx, sy, scol)
        c.set(sx - 1, sy, C_BG3)
        c.set(sx + 1, sy, C_BG3)

    # -------------------------------------------------------------------------
    # 11. FOREGROUND VIGNETTE
    # -------------------------------------------------------------------------
    for y in range(0, 128):
        c.set(0, y, C_VOID)
        c.set(1, y, C_BG1)
        c.set(127, y, C_VOID)
        c.set(126, y, C_BG1)

    return c

c = draw_cyberpunk_alley()
view(c)
print("Stats:", c.stats_text())
finish(c)
