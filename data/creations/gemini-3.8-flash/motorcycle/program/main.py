import math

def build_sport_motorcycle():
    c = new_canvas(128, 128)

    # Palette definition (38 cohesive colors, well under 86 limit)
    P = {
        # Transparent
        'trans': None,

        # Bodywork - Dark Gray & Black (Streamlined)
        'body_deep': '#101216',
        'body_shadow': '#1b1d24',
        'body_dark': '#292d37',
        'body_mid': '#3b414f',
        'body_slate': '#50586b',
        'body_light': '#6a748c',
        'body_hi': '#8894af',
        'body_spec': '#adbad4',

        # Blacks for deep shadows, seat leather, vents
        'black_deep': '#08090b',
        'black_dark': '#111216',
        'black_mid': '#191b21',
        'black_light': '#242630',

        # Tilted Small Black Windscreen (Glossy Tinted Black)
        'wind_black': '#07080b',
        'wind_dark': '#0e1219',
        'wind_mid': '#18202d',
        'wind_hi': '#2a374c',
        'wind_edge': '#465a7a',
        'wind_glint': '#7d98be',

        # Silver / Gray Metal Parts (Fork, Trellis Frame, Engine Cover, Swingarm)
        'metal_black': '#13151a',
        'metal_shadow': '#21262e',
        'metal_dark': '#343b47',
        'metal_mid': '#515b6b',
        'metal_light': '#778496',
        'metal_bright': '#a9b9cc',
        'metal_hi': '#d8e3f0',
        'metal_pure': '#ffffff',

        # Red Accents & Tail Light (Vibrant Racing Red)
        'red_shadow': '#45080c',
        'red_dark': '#730d14',
        'red_mid': '#b0121d',
        'red_bright': '#eb1e2c',
        'red_hi': '#ff4f5d',
        'red_glow': '#ffa1aa',

        # Thick Black Tires & Rubber
        'tire_deep': '#0b0c0f',
        'tire_dark': '#15161b',
        'tire_mid': '#22232c',
        'tire_tread': '#31333f',
        'tire_hi': '#454857',

        # Accent Gold (Chain links, shock reservoir, caliper pin)
        'gold_dark': '#4f3912',
        'gold_mid': '#8a641b',
        'gold_bright': '#c2922c',
        'gold_hi': '#e8cf58',

        # Lights (LED Headlight, Dash)
        'light_cyan': '#96e7fa',
        'light_white': '#effaff',
    }

    def d_line(x0, y0, x1, y1, col):
        c.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), col)

    def d_poly(pts, col):
        c.poly([(int(round(x)), int(round(y))) for x, y in pts], col, fill=True)

    # 3D metallic cylindrical tube
    def d_tube(x0, y0, x1, y1):
        angle = math.atan2(y1 - y0, x1 - x0)
        nx = -math.sin(angle)
        ny = math.cos(angle)
        d_line(x0 + nx*0.9, y0 + ny*0.9, x1 + nx*0.9, y1 + ny*0.9, P['metal_dark'])
        d_line(x0, y0, x1, y1, P['metal_light'])
        d_line(x0 - nx*0.8, y0 - ny*0.8, x1 - nx*0.8, y1 - ny*0.8, P['metal_hi'])

    XR, YR = 27, 83   # Rear wheel center
    XF, YF = 101, 83  # Front wheel center

    # ==========================================
    # 1. WHEELS & TIRES ("thick black tires", "gray hub white spokes")
    # ==========================================
    def draw_wheel(cx, cy, is_front=True):
        # 1. Thick black tire (R=17, diameter 35)
        for dy in range(-18, 19):
            for dx in range(-18, 19):
                d2 = dx*dx + dy*dy
                d = math.sqrt(d2)
                if d <= 17.2:
                    if d >= 11.5:
                        if dy < 0 and 13.5 <= d <= 16.5:
                            col = P['tire_mid']
                            if dy < -5 and abs(dx) < 13:
                                col = P['tire_tread']
                            if dy < -9 and abs(dx) < 9:
                                col = P['tire_hi']
                            c.set(cx + dx, cy + dy, col)
                        elif d >= 16.0:
                            c.set(cx + dx, cy + dy, P['tire_deep'])
                        elif d <= 12.2:
                            c.set(cx + dx, cy + dy, P['tire_deep'])
                        else:
                            c.set(cx + dx, cy + dy, P['tire_dark'])

        # Subtle tire tread sipes
        for angle_deg in range(0, 360, 45):
            rad = math.radians(angle_deg)
            for r in [13, 14, 15]:
                tx = int(cx + r * math.cos(rad))
                ty = int(cy + r * math.sin(rad))
                c.set(tx, ty, P['tire_deep'])

        # 2. Rim outer ring / lip (silver metal)
        for angle_deg in range(0, 360):
            rad = math.radians(angle_deg)
            rx = int(round(cx + 11.5 * math.cos(rad)))
            ry = int(round(cy + 11.5 * math.sin(rad)))
            c.set(rx, ry, P['metal_bright'] if ry < cy else P['metal_mid'])

        # Rim inner wall
        for angle_deg in range(0, 360):
            rad = math.radians(angle_deg)
            rx = int(round(cx + 10.5 * math.cos(rad)))
            ry = int(round(cy + 10.5 * math.sin(rad)))
            c.set(rx, ry, P['metal_shadow'])

        # 3. Brake disc rotor (drilled silver rotor)
        disc_r = 8.2 if is_front else 7.2
        for dy in range(-9, 10):
            for dx in range(-9, 10):
                d = math.sqrt(dx*dx + dy*dy)
                if 4.8 <= d <= disc_r:
                    col = P['metal_mid']
                    if (dx + dy) % 3 == 0:
                        col = P['metal_light']
                    elif (dx - dy) % 4 == 0:
                        col = P['metal_dark']
                    c.set(cx + dx, cy + dy, col)

        # 4. "white spokes" - 10 crisp pure white spokes
        num_spokes = 10
        for i in range(num_spokes):
            angle = i * (2 * math.pi / num_spokes)
            for r_step in range(4, 11):
                sx = int(round(cx + r_step * math.cos(angle)))
                sy = int(round(cy + r_step * math.sin(angle)))
                c.set(sx, sy, P['metal_pure'])
                if r_step >= 5:
                    perp_x = -math.sin(angle) * 0.5
                    perp_y = math.cos(angle) * 0.5
                    c.set(int(round(sx + perp_x)), int(round(sy + perp_y)), P['metal_hi'])

        # 5. "gray hub" - distinct central gray metal hub
        for dy in range(-4, 5):
            for dx in range(-4, 5):
                d = math.sqrt(dx*dx + dy*dy)
                if d <= 4.2:
                    if d <= 1.8:
                        c.set(cx + dx, cy + dy, P['metal_hi'] if dx <= 0 and dy <= 0 else P['metal_dark'])
                    elif dy < 0:
                        c.set(cx + dx, cy + dy, P['metal_light'])
                    elif dy == 0:
                        c.set(cx + dx, cy + dy, P['metal_mid'])
                    else:
                        c.set(cx + dx, cy + dy, P['metal_shadow'])

        # Hub rim perimeter ring
        for angle_deg in range(0, 360, 15):
            rad = math.radians(angle_deg)
            hx = int(round(cx + 4.0 * math.cos(rad)))
            hy = int(round(cy + 4.0 * math.sin(rad)))
            c.set(hx, hy, P['metal_dark'] if hy > cy else P['metal_light'])

    draw_wheel(XR, YR, is_front=False)
    draw_wheel(XF, YF, is_front=True)

    # ==========================================
    # 2. INTERNAL CHASSIS & ENGINE BLOCK
    # ==========================================
    # Radiator
    d_poly([(84, 62), (89, 62), (87, 77), (82, 77)], P['metal_dark'])
    for ry in range(63, 77, 2):
        d_line(83, ry, 88, ry, P['metal_shadow'])
        d_line(83, ry+1, 88, ry+1, P['metal_mid'])

    # Engine block
    d_poly([(54, 73), (68, 65), (78, 65), (82, 73), (78, 83), (60, 86), (53, 81)], P['metal_dark'])
    for fy in range(66, 74, 2):
        d_line(68, fy, 78, fy, P['metal_mid'])
        d_line(68, fy+1, 78, fy+1, P['metal_shadow'])

    # Exhaust header pipes curving down from front cylinders
    h1 = [(76, 68), (81, 71), (83, 76), (81, 82), (73, 86), (62, 87)]
    for i in range(len(h1)-1):
        d_line(h1[i][0], h1[i][1], h1[i+1][0], h1[i+1][1], P['metal_bright'])
        d_line(h1[i][0], h1[i][1]+1, h1[i+1][0], h1[i+1][1]+1, P['metal_mid'])
    h2 = [(74, 67), (79, 70), (81, 75), (78, 81), (70, 85), (59, 87)]
    for i in range(len(h2)-1):
        d_line(h2[i][0], h2[i][1], h2[i+1][0], h2[i+1][1], P['metal_light'])

    # Swingarm (connects rear axle (27, 83) to frame pivot (54, 73))
    swing_pts = [
        (27, 83), (31, 80), (43, 76), (53, 72), (54, 76), (44, 80), (31, 85), (27, 83)
    ]
    d_poly(swing_pts, P['metal_mid'])
    brace_pts = [
        (33, 80), (41, 71), (50, 71), (53, 73), (44, 76), (36, 80)
    ]
    d_poly(brace_pts, P['metal_light'])
    d_line(31, 80, 53, 72, P['metal_bright'])
    d_line(34, 80, 41, 71, P['metal_hi'])
    d_line(41, 71, 50, 71, P['metal_hi'])
    c.rect(25, 82, 5, 3, P['metal_dark'])
    c.set(27, 83, P['metal_hi'])

    # Rear tire hugger fender
    hugger_pts = [(28, 65), (35, 64), (42, 67), (43, 71), (39, 70), (33, 67), (27, 68)]
    d_poly(hugger_pts, P['body_dark'])
    d_line(28, 65, 38, 65, P['body_slate'])

    # Monoshock with red spring
    d_line(44, 71, 49, 64, P['metal_dark'])
    for (sx, sy) in [(45, 70), (46, 68), (47, 66)]:
        c.set(sx-1, sy, P['red_dark'])
        c.set(sx, sy, P['red_bright'])
        c.set(sx+1, sy, P['red_hi'])
    c.rect(48, 63, 3, 2, P['gold_bright'])
    c.set(48, 63, P['gold_hi'])

    # Drive chain
    for x in range(29, 53, 2):
        y = int(76 - (x - 29) * 0.04)
        c.set(x, y, P['metal_dark'])
        c.set(x+1, y, P['gold_mid'])
    for x in range(29, 53, 2):
        y = int(88 - (x - 29) * 0.25)
        c.set(x, y, P['metal_dark'])
        c.set(x+1, y, P['gold_dark'])

    # Upswept Titanium Sport Muffler
    muffler_pts = [
        (48, 85), (44, 82), (25, 71), (23, 73), (25, 76), (42, 87), (48, 87)
    ]
    d_poly(muffler_pts, P['metal_dark'])
    d_line(44, 82, 25, 71, P['metal_hi'])
    d_line(45, 83, 26, 72, P['metal_bright'])
    d_line(46, 84, 27, 73, P['metal_mid'])
    d_line(47, 85, 28, 74, P['metal_shadow'])
    d_line(23, 73, 25, 76, P['metal_bright'])
    c.set(23, 74, P['metal_black'])
    c.set(24, 74, P['metal_black'])
    c.set(24, 75, P['metal_black'])
    d_line(34, 76, 40, 69, P['metal_light'])
    d_line(35, 76, 41, 69, P['metal_shadow'])
    c.rect(33, 77, 4, 2, P['red_bright'])
    c.set(34, 77, P['gold_bright'])

    # ==========================================
    # 3. "round silver gray engine cover"
    # ==========================================
    ecx, ecy = 63, 78
    for dy in range(-7, 8):
        for dx in range(-7, 8):
            d = math.sqrt(dx*dx + dy*dy)
            if d <= 7.2:
                intensity = (-dx - dy) / 9.5
                if d >= 6.0:
                    if intensity > 0.2:
                        col = P['metal_hi']
                    elif intensity > -0.2:
                        col = P['metal_mid']
                    else:
                        col = P['metal_dark']
                elif d >= 4.5:
                    col = P['metal_shadow'] if intensity < 0.2 else P['metal_dark']
                elif d >= 2.2:
                    if intensity > 0.3:
                        col = P['metal_bright']
                    elif intensity > -0.2:
                        col = P['metal_light']
                    else:
                        col = P['metal_mid']
                else:
                    col = P['metal_hi'] if intensity > 0 else P['metal_mid']
                c.set(ecx + dx, ecy + dy, col)

    for b_deg in [0, 60, 120, 180, 240, 300]:
        rad = math.radians(b_deg)
        bx = int(round(ecx + 5.6 * math.cos(rad)))
        by = int(round(ecy + 5.6 * math.sin(rad)))
        c.set(bx, by, P['metal_hi'] if by <= ecy else P['metal_shadow'])

    # ==========================================
    # 4. "silver tubular frame" (Trellis)
    # ==========================================
    # Diamond lattice trellis frame
    # Upper spine
    d_tube(87, 51, 76, 54)
    d_tube(76, 54, 65, 58)
    d_tube(65, 58, 54, 68)

    # Lower spine
    d_tube(87, 56, 77, 60)
    d_tube(77, 60, 66, 65)
    d_tube(66, 65, 54, 73)

    # Cross diagonals
    d_tube(87, 51, 77, 60)
    d_tube(76, 54, 77, 60)
    d_tube(76, 54, 66, 65)
    d_tube(65, 58, 66, 65)
    d_tube(65, 58, 54, 73)
    d_tube(66, 65, 54, 73)

    # Weld joints
    for jx, jy in [(87, 51), (76, 54), (65, 58), (54, 68), (87, 56), (77, 60), (66, 65), (54, 73)]:
        c.set(jx, jy, P['metal_hi'])
        c.set(jx, jy+1, P['metal_shadow'])

    # Subframe tubes under seat
    d_tube(65, 58, 52, 60)
    d_tube(54, 68, 44, 60)

    # ==========================================
    # 5. BODYWORK: FUEL TANK & SEAT & "upswept tail"
    # ==========================================
    # Fuel tank: sculpted dark gray bodywork
    tank_pts = [
        (87, 50), (83, 44), (77, 42), (71, 43), (66, 47), (63, 53), (63, 58),
        (69, 59), (76, 57), (83, 54), (87, 51)
    ]
    d_poly(tank_pts, P['body_dark'])
    d_poly([(86, 49), (82, 44), (77, 43), (71, 44), (67, 47), (68, 52), (75, 50), (82, 48)], P['body_mid'])
    d_poly([(84, 47), (80, 44), (76, 43), (72, 44), (69, 47), (74, 48), (81, 47)], P['body_slate'])

    d_line(80, 43, 73, 43, P['body_spec']) # Specular highlight on tank ridge
    d_line(83, 45, 68, 48, P['body_light'])

    # Aircraft-style fuel cap
    c.rect(75, 41, 4, 2, P['metal_bright'])
    c.set(76, 41, P['metal_hi'])
    c.set(77, 42, P['metal_dark'])

    # Red racing stripe along tank
    d_line(82, 46, 70, 51, P['red_bright'])
    d_line(82, 47, 70, 52, P['red_mid'])

    # Rider seat: deep scooped sport saddle
    seat_pts = [
        (63, 58), (61, 60), (56, 61), (52, 59), (52, 62), (59, 63), (63, 60)
    ]
    d_poly(seat_pts, P['black_deep'])
    d_line(61, 59, 54, 61, P['black_mid'])

    # "upswept tail" - Rising Aerodynamic Wedge!
    # Slants up from seat step (52, 54) to high sharp tip (26, 41)!
    tail_pts = [
        (52, 54), (46, 50), (40, 46), (34, 43), (28, 41), (26, 41),
        (26, 43), (28, 44), (34, 48), (40, 53), (46, 59), (52, 65), (52, 54)
    ]
    d_poly(tail_pts, P['body_dark'])

    # Tail upper facet / cowl volume
    tail_top_facet = [
        (51, 54), (45, 50), (39, 46), (33, 43), (27, 41),
        (27, 42), (33, 44), (39, 47), (45, 52), (51, 56)
    ]
    d_poly(tail_top_facet, P['body_mid'])

    # Upper ridge highlight
    d_line(48, 51, 28, 41, P['body_slate'])
    d_line(42, 47, 27, 41, P['body_light'])
    d_line(36, 44, 27, 41, P['body_spec']) # Specular reflection on tail tip

    # Aerodynamic hollow tail vent / tunnel
    d_poly([(36, 47), (42, 51), (43, 53), (37, 49)], P['black_deep'])
    d_line(36, 46, 42, 50, P['body_slate'])

    # Tail Red Racing Graphic (solid 2px stripe rising with the tail)
    d_poly([(50, 56), (44, 52), (36, 47), (28, 42), (27, 42), (27, 43), (35, 48), (43, 53), (49, 57)], P['red_bright'])
    d_line(49, 57, 27, 43, P['red_mid'])

    # "red tail light":
    # Integrated ruby red LED light at the very tip of the upswept tail (x=24 to 26, y=41 to 44)
    c.rect(24, 41, 3, 3, P['red_bright'])
    c.set(23, 42, P['red_dark'])   # Bezel edge
    c.set(24, 41, P['red_hi'])     # Lens highlight
    c.set(25, 41, P['red_glow'])   # Glowing core
    c.set(24, 42, P['red_glow'])
    c.set(25, 42, P['red_bright'])
    c.set(24, 43, P['red_mid'])
    c.set(26, 41, P['red_hi'])
    c.set(26, 42, P['red_bright'])

    # Undertray & tidy tail bracket
    d_line(30, 46, 27, 51, P['metal_dark'])
    c.rect(26, 50, 3, 3, P['metal_shadow'])
    c.rect(27, 51, 2, 2, P['metal_light'])

    # Footpeg / Rearset at (52, 73)
    c.rect(50, 72, 4, 3, P['metal_light'])
    d_line(49, 72, 47, 72, P['metal_bright'])
    c.set(48, 73, P['metal_dark'])
    c.set(51, 72, P['metal_hi'])

    # ==========================================
    # 6. "wide dark gray fairing" & NOSE
    # ==========================================
    fairing_pts = [
        (92, 48), (102, 50), (111, 53), (119, 56),
        (116, 59), (108, 62), (101, 64), (95, 68), (91, 74), (86, 81), (80, 87),
        (62, 87), (60, 84), (66, 81), (72, 76), (79, 72), (83, 65), (87, 56), (92, 48)
    ]
    d_poly(fairing_pts, P['body_dark'])

    # Upper nose bridge facet
    nose_facet = [(94, 49), (102, 51), (111, 54), (117, 56), (111, 57), (102, 54), (94, 51)]
    d_poly(nose_facet, P['body_mid'])
    d_line(95, 49, 115, 55, P['body_slate'])
    d_line(97, 49, 110, 53, P['body_light'])
    d_line(99, 49, 106, 52, P['body_spec'])

    # Wide fairing flank shading (sculpted volume)
    mid_flank = [
        (100, 56), (109, 58), (106, 62), (99, 65), (93, 70), (87, 73),
        (86, 66), (92, 60), (98, 56)
    ]
    d_poly(mid_flank, P['body_mid'])
    d_line(99, 57, 91, 62, P['body_slate'])
    d_line(98, 58, 92, 62, P['body_light'])

    # Aerodynamic air extraction vent
    d_poly([(96, 62), (100, 62), (97, 67), (93, 67)], P['black_deep'])
    d_poly([(92, 68), (96, 68), (94, 72), (90, 72)], P['black_deep'])
    d_line(96, 61, 100, 61, P['body_slate'])
    d_line(92, 67, 96, 67, P['body_slate'])

    # Aerodynamic Winglet (on fairing nose flank)
    winglet_pts = [(104, 60), (111, 60), (114, 62), (103, 62)]
    d_poly(winglet_pts, P['body_slate'])
    d_line(104, 60, 111, 60, P['body_hi'])
    c.set(113, 61, P['red_bright']) # Red winglet tip
    c.set(114, 62, P['red_bright'])

    # Dynamic Red Accents on Fairing
    d_poly([(114, 56), (106, 59), (98, 64), (89, 72), (83, 80),
            (83, 81), (89, 73), (98, 65), (106, 60), (114, 57)], P['red_bright'])
    d_line(113, 57, 106, 60, P['red_mid'])
    d_line(106, 60, 98, 65, P['red_mid'])
    d_line(98, 65, 89, 73, P['red_mid'])

    # Belly Pan
    d_line(80, 87, 62, 87, P['black_deep'])
    d_poly([(78, 85), (64, 85), (64, 86), (78, 86)], P['red_bright'])
    d_line(78, 86, 64, 86, P['red_mid'])

    # Front Headlight: aggressive LED projector slit at nose tip
    d_line(115, 56, 118, 56, P['light_white'])
    c.set(117, 56, P['light_cyan'])
    c.set(116, 57, P['light_cyan'])
    c.set(114, 55, P['red_bright'])

    # ==========================================
    # 7. "tilted small black windscreen" & COCKPIT
    # ==========================================
    windscreen_pts = [
        (109, 50), (104, 45), (99, 41), (94, 38),
        (91, 42), (90, 47), (95, 48), (102, 50), (109, 50)
    ]
    d_poly(windscreen_pts, P['wind_black'])
    c.poly([(107, 49), (103, 45), (98, 41), (94, 39), (92, 43), (91, 47), (96, 48), (103, 49)],
           P['wind_dark'], fill=True)
    d_line(106, 47, 101, 43, P['wind_mid'])
    d_line(101, 43, 96, 39, P['wind_hi'])
    d_line(98, 41, 94, 38, P['wind_edge'])
    c.set(96, 39, P['wind_glint'])
    c.set(95, 39, P['wind_glint'])
    d_line(109, 51, 95, 49, P['body_deep'])

    # Cockpit screen
    c.rect(89, 46, 3, 2, P['light_cyan'])
    c.set(90, 46, P['light_white'])

    # ==========================================
    # 8. "silver front fork" & FRONT FENDER
    # ==========================================
    # Triple clamps
    d_line(85, 49, 89, 49, P['metal_bright'])
    d_line(85, 50, 89, 50, P['metal_shadow'])
    d_line(88, 56, 92, 56, P['metal_bright'])
    d_line(88, 57, 92, 57, P['metal_shadow'])

    # Clip-on handlebars
    d_line(84, 50, 80, 53, P['metal_mid'])
    d_line(80, 53, 78, 55, P['tire_deep'])
    d_line(79, 53, 77, 55, P['tire_mid'])
    c.set(77, 56, P['metal_bright'])
    d_line(81, 54, 84, 56, P['metal_hi'])

    # Upper inverted fork stanchions (thick silver tubes)
    for y in range(51, 69):
        t = (y - 50) / 33.0
        xc = 86 + t * 15.0
        x_int = int(round(xc))
        c.set(x_int - 1, y, P['metal_hi'])
        c.set(x_int, y, P['metal_bright'])
        c.set(x_int + 1, y, P['metal_mid'])

    # Fork seal collar at y=68
    c.rect(93, 68, 4, 2, P['metal_dark'])
    c.set(94, 68, P['metal_hi'])

    # Lower chrome inner slider tubes
    for y in range(70, 82):
        t = (y - 50) / 33.0
        xc = 86 + t * 15.0
        x_int = int(round(xc))
        c.set(x_int - 1, y, P['metal_pure'])
        c.set(x_int, y, P['metal_hi'])
        c.set(x_int + 1, y, P['metal_light'])

    # Fork bottom axle bracket & radial mount
    c.rect(99, 81, 4, 4, P['metal_dark'])
    c.set(100, 82, P['metal_light'])
    c.set(101, 82, P['metal_bright'])
    c.set(100, 83, P['metal_mid'])
    c.set(101, 83, P['metal_pure']) # Front axle nut

    # Front radial brake caliper (Brembo red caliper)
    caliper_pts = [
        (96, 75), (99, 75), (99, 79), (96, 79), (95, 76)
    ]
    d_poly(caliper_pts, P['red_bright'])
    d_line(96, 75, 99, 75, P['red_hi'])
    c.set(96, 78, P['red_dark'])
    c.set(98, 77, P['gold_bright'])

    # Front fender (mudguard)
    fender_pts = [
        (90, 73), (92, 69), (98, 65), (104, 65), (110, 69), (112, 73),
        (110, 71), (104, 66), (98, 66), (92, 71)
    ]
    d_poly(fender_pts, P['body_dark'])
    d_line(96, 65, 106, 65, P['body_slate'])
    d_line(93, 67, 109, 67, P['red_bright'])
    d_line(97, 68, 97, 71, P['metal_mid'])

    # Finish output
    finish(c)
    return c

c = build_sport_motorcycle()
view(c)
