from pixelbench_api import *

def build_sewing_machine():
    c = new_canvas(48, 48, name="vintage_sewing_machine")

    # --- PALETTE DEFINITION ---
    # Background: transparent (None)

    # Wood Base Palette (Polished heirloom walnut/mahogany)
    w_darkest  = "#180a03"
    w_shadow   = "#2c1207"
    w_deep     = "#441d0b"
    w_base     = "#5e2a11"
    w_mid      = "#7a3919"
    w_light    = "#9a4c23"
    w_hi       = "#be6432"
    w_accent   = "#d97b44"
    w_grain    = "#4d210c"
    w_occl     = "#240e05"

    # Cast Iron Body Palette (Deep lustrous black enamel)
    i_black    = "#0a0b0e"
    i_deep     = "#12141a"
    i_shadow   = "#1a1d26"
    i_dark     = "#242735"
    i_mid      = "#33384a"
    i_light    = "#474e64"
    i_hi       = "#636d8a"
    i_gleam    = "#8b96b8"
    i_white    = "#c2cbdf"

    # Vintage Singer Gold Decals & Filigree
    g_dark     = "#4f3806"
    g_shade    = "#78580f"
    g_mid      = "#ab8219"
    g_light    = "#d4a72d"
    g_hi       = "#edc751"
    g_pale     = "#fcf09d"

    # Chrome / Steel / Silver Hardware
    s_black    = "#15171d"
    s_shadow   = "#282c36"
    s_dark     = "#434a57"
    s_mid      = "#667082"
    s_light    = "#929eb0"
    s_bright   = "#beccde"
    s_white    = "#ecf2fa"

    # Red Fabric Palette (Vibrant rich crimson)
    r_darkest  = "#2a0105"
    r_deep     = "#4d040e"
    r_shadow   = "#700816"
    r_base     = "#990e21"
    r_mid      = "#c2152c"
    r_light    = "#e3223c"
    r_hi       = "#f5405a"
    r_rim      = "#ff7087"
    stitch_col = "#fff6c9"

    # Thread, Felt & Spool
    felt_green = "#1a472a"
    felt_hi    = "#2e693f"
    th_dark    = "#857354"
    th_mid     = "#c4b38e"
    th_light   = "#eadeb8"
    th_white   = "#faf7eb"
    sp_wood    = "#452811"
    sp_wood_hi = "#6e421d"
    c_belt     = "#2e1c10"

    # =========================================================================
    # 1. BASE: POLISHED HARDWOOD PLINTH
    # =========================================================================
    for x in range(7, 41):
        c.set(x, 31, w_deep)
    for x in range(6, 42):
        c.set(x, 32, w_base)
    for x in range(5, 42):
        c.set(x, 33, w_mid)
    for x in range(4, 43):
        c.set(x, 34, w_mid)
    for x in range(4, 43):
        c.set(x, 35, w_light)
    for x in range(3, 44):
        c.set(x, 36, w_hi)

    # Wood grain details on top:
    c.line(8, 33, 23, 33, w_grain)
    c.line(26, 32, 39, 32, w_grain)
    c.line(25, 34, 40, 34, w_base)
    c.line(9, 35, 23, 35, w_light)

    # Ambient cast shadow on the wood bed under the throat:
    c.line(18, 32, 28, 32, w_occl)
    c.line(19, 33, 27, 33, w_deep)

    # Front chamfer/bevel highlight (y=37):
    for x in range(3, 44):
        c.set(x, 37, w_accent)
    c.set(3, 37, w_hi)
    c.set(43, 37, w_hi)

    # Front vertical plinth face (y=38..42):
    for y in range(38, 43):
        for x in range(3, 44):
            if y == 38:
                col = w_mid
            elif y == 39:
                col = w_base
            elif y == 40:
                col = w_deep
            elif y == 41:
                col = w_shadow
            else:
                col = w_darkest
            c.set(x, y, col)

    # Bevel top highlight line:
    c.line(4, 38, 42, 38, w_light)
    # Side shadow edges:
    for y in range(37, 43):
        c.set(3, y, w_deep)
        c.set(43, y, w_darkest)

    # Cove moulding groove at y=41..42:
    c.line(4, 41, 42, 41, w_darkest)
    c.line(4, 42, 42, 42, w_shadow)

    # Brass / carved feet at corners:
    for fx in [5, 6, 7]:
        c.set(fx, 43, g_mid)
        c.set(fx, 44, g_dark)
    c.set(6, 43, g_hi)
    c.set(5, 44, w_darkest)
    c.set(7, 44, w_darkest)

    for fx in [39, 40, 41]:
        c.set(fx, 43, g_mid)
        c.set(fx, 44, g_dark)
    c.set(40, 43, g_hi)
    c.set(39, 44, w_darkest)
    c.set(41, 44, w_darkest)

    # Contact shadow under base between feet:
    c.line(8, 43, 38, 43, w_darkest)

    # =========================================================================
    # 2. THROAT PLATE / NEEDLE PLATE (Polished Silver Steel Plate)
    # =========================================================================
    for y in range(32, 36):
        for x in range(11, 24):
            c.set(x, y, s_mid)
    c.line(11, 32, 23, 32, s_white)
    c.line(11, 32, 11, 35, s_bright)
    c.line(23, 32, 23, 35, s_dark)
    c.line(12, 35, 23, 35, s_shadow)

    # Polished steel reflections on exposed right half:
    c.line(18, 33, 22, 33, s_bright)
    c.line(18, 34, 22, 34, s_light)
    c.set(19, 34, s_dark)
    c.set(21, 34, s_dark)
    c.set(21, 33, s_shadow)
    c.set(22, 33, s_white)

    # =========================================================================
    # 3. CAST IRON BODY (Glossy Black Enamel Head, Arm, and Pillar)
    # =========================================================================
    # A. Pillar base flange / mounting foot (x=27..38, y=29..32)
    for y in range(29, 33):
        x0 = 28 - (1 if y >= 31 else 0)
        x1 = 37 + (1 if y >= 31 else 0)
        for x in range(x0, x1 + 1):
            c.set(x, y, i_shadow)
    c.line(28, 29, 37, 29, i_light)
    c.line(28, 30, 37, 30, i_mid)
    c.line(27, 31, 38, 31, i_dark)
    c.line(27, 32, 38, 32, i_black)
    c.line(27, 33, 38, 33, w_darkest)

    # B. Vertical Pillar (x=30..36, y=17..29)
    for py in range(17, 29):
        x0 = 31 if (23 <= py <= 26) else 30
        x1 = 37 if (py >= 27) else 36
        for px in range(x0, x1 + 1):
            c.set(px, py, i_dark)

    # C. Horizontal Arm (x=12..35, y=12..22)
    arm_rows = [
        (12, (17, 31)),
        (13, (14, 34)),
        (14, (12, 35)),
        (15, (11, 35)),
        (16, (11, 35)),
        (17, (11, 34)),
        (18, (11, 32)),
        (19, (11, 22)),
        (20, (11, 18)),
        (21, (11, 18)),
        (22, (11, 18)),
    ]
    for ay, (ax0, ax1) in arm_rows:
        for ax in range(ax0, ax1 + 1):
            c.set(ax, ay, i_dark)

    # Ensure throat open space is completely transparent (above bed y=31):
    for ty in range(18, 31):
        for tx in range(18, 30):
            if ty == 18 and tx <= 32:
                continue
            if ty == 19 and tx <= 22:
                continue
            if ty >= 20 and tx <= 18:
                continue
            if ty >= 21 and tx >= 30:
                continue
            if ty >= 28 and tx >= 28:
                continue
            c.set(tx, ty, None)

    # D. Shading and Specular Gleams on Body:
    c.line(18, 12, 30, 12, i_light)
    c.line(19, 13, 29, 13, i_hi)
    c.line(22, 13, 26, 13, i_gleam)
    c.set(24, 13, i_white)

    c.set(16, 12, i_mid)
    c.set(15, 13, i_mid)
    c.set(14, 13, i_light)
    c.set(13, 14, i_light)
    c.set(12, 14, i_hi)

    c.line(12, 22, 18, 22, i_deep)
    c.line(12, 23, 17, 23, i_black)
    c.set(12, 22, i_mid)

    for py in range(17, 28):
        px_hi = 31 if (23 <= py <= 26) else 30
        c.set(px_hi, py, i_light)
        c.set(px_hi + 1, py, i_mid)
    for py in range(17, 29):
        c.set(36, py, i_deep)
        c.set(35, py, i_shadow)

    c.line(18, 21, 20, 20, i_black)
    c.line(21, 19, 26, 20, i_black)
    c.line(27, 21, 29, 23, i_black)

    # E. Vintage Singer Gold Decals & Filigree:
    c.line(19, 15, 28, 15, g_mid)
    c.set(21, 15, g_light)
    c.set(24, 15, g_hi)
    c.set(26, 15, g_light)

    c.set(18, 16, g_light)
    c.set(19, 16, g_hi)
    c.set(21, 16, g_hi)
    c.set(22, 16, g_mid)
    c.set(23, 16, g_light)
    c.set(24, 16, g_pale)
    c.set(25, 16, g_light)
    c.set(26, 16, g_mid)
    c.set(27, 16, g_hi)
    c.set(29, 16, g_light)

    c.line(19, 17, 28, 17, g_shade)
    c.set(21, 17, g_mid)
    c.set(24, 17, g_light)
    c.set(26, 17, g_mid)

    # Pillar gold decal emblem:
    c.set(33, 22, g_hi)
    c.line(32, 23, 34, 23, g_mid)
    c.set(33, 23, g_pale)
    c.set(32, 24, g_light)
    c.set(34, 24, g_light)
    c.set(33, 24, g_mid)
    c.line(32, 25, 34, 25, g_shade)
    c.set(33, 26, g_dark)

    c.line(30, 29, 36, 29, g_shade)
    c.set(32, 29, g_mid)
    c.set(34, 29, g_mid)

    # F. Faceplate on left side of head (x=10..12, y=14..22):
    for fy in range(14, 23):
        c.set(10, fy, s_mid)
        c.set(11, fy, s_bright)
        c.set(12, fy, s_light)
    c.line(11, 14, 11, 21, s_white)
    c.set(10, 16, s_dark)
    c.set(10, 18, s_dark)
    c.set(10, 20, s_dark)
    c.set(12, 16, s_dark)
    c.set(12, 18, s_dark)
    c.set(12, 20, s_dark)

    # Tension dial assembly on head front:
    c.set(14, 18, s_white)
    c.set(15, 18, s_light)
    c.set(13, 19, s_white)
    c.set(14, 19, s_black)
    c.set(15, 19, s_dark)
    c.set(14, 20, s_mid)
    c.set(15, 20, s_shadow)

    # Fine thread trailing from tension dial down to needle:
    c.set(13, 22, th_mid)
    c.set(13, 25, th_light)

    # =========================================================================
    # 4. HANDWHEEL (Right side: x=38..44, y=14..28)
    # =========================================================================
    c.rect(36, 19, 2, 4, i_deep)
    c.line(36, 19, 37, 19, i_light)

    wheel_rows = {
        14: (40, 42),
        15: (39, 43),
        16: (39, 43),
        17: (38, 44),
        18: (38, 44),
        19: (38, 44),
        20: (38, 44),
        21: (38, 44),
        22: (38, 44),
        23: (38, 44),
        24: (38, 44),
        25: (39, 43),
        26: (39, 43),
        27: (40, 42),
    }
    for wy, (wx0, wx1) in wheel_rows.items():
        for wx in range(wx0, wx1 + 1):
            c.set(wx, wy, i_dark)

    # Quadrant interiors (open dark cutouts between spokes):
    c.set(39, 18, i_black)
    c.set(40, 18, i_deep)
    c.set(39, 19, i_deep)
    c.set(40, 19, i_black)

    c.set(42, 18, i_black)
    c.set(43, 18, i_black)
    c.set(42, 19, i_black)
    c.set(43, 19, i_deep)

    c.set(39, 23, i_deep)
    c.set(40, 23, i_black)
    c.set(39, 24, i_black)
    c.set(40, 24, i_black)

    c.set(42, 23, i_black)
    c.set(43, 23, i_black)
    c.set(42, 24, i_deep)
    c.set(43, 24, i_black)

    # 4 Spokes connecting to hub:
    c.line(41, 16, 41, 19, i_light) # top spoke
    c.line(41, 22, 41, 25, i_dark)  # bottom spoke
    c.line(39, 21, 40, 21, i_light) # left spoke
    c.line(42, 21, 43, 21, i_dark)  # right spoke

    # Polished brass / gold outer rim edge:
    c.line(40, 14, 42, 14, g_light)
    c.set(41, 14, g_hi)

    c.set(39, 15, g_light)
    c.set(40, 15, g_hi)
    c.set(43, 15, g_shade)

    c.set(39, 16, g_hi)
    c.set(43, 16, g_dark)

    c.line(38, 17, 38, 24, g_light)
    c.set(38, 19, g_hi)
    c.set(38, 20, g_pale) # specular glint on wheel rim
    c.set(38, 21, g_pale)
    c.set(38, 22, g_hi)

    c.set(39, 25, g_mid)
    c.set(43, 25, g_dark)
    c.set(39, 26, g_shade)
    c.set(43, 26, g_dark)
    c.line(40, 27, 42, 27, g_dark)

    # Rim outer thickness (right side):
    for wy in range(17, 25):
        c.set(44, wy, i_black)
        c.set(43, wy, i_deep)

    # Center clutch / stop-motion knob:
    c.rect(40, 20, 2, 2, s_bright)
    c.set(40, 20, s_white)
    c.set(41, 20, s_light)
    c.set(40, 21, s_light)
    c.set(41, 21, s_mid)

    # Leather drive belt:
    c.line(37, 21, 37, 28, c_belt)
    c.line(36, 27, 36, 31, c_belt)

    # Bobbin winder:
    c.set(35, 14, s_mid)
    c.set(36, 13, s_bright)
    c.set(37, 13, s_white)
    c.set(36, 14, s_dark)
    c.set(37, 14, i_black)

    # =========================================================================
    # 5. SPOOL OF THREAD ON TOP OF ARM
    # =========================================================================
    c.line(27, 5, 27, 12, s_bright)
    c.set(27, 5, s_white)

    # Green felt washer:
    c.line(25, 12, 29, 12, felt_green)
    c.set(27, 12, felt_hi)

    # Wooden spool:
    c.rect(25, 7, 5, 1, sp_wood_hi)
    c.set(27, 7, s_bright)
    c.rect(25, 11, 5, 1, sp_wood)
    c.set(27, 11, s_mid)

    # Cream cotton thread:
    for ty in range(8, 11):
        c.line(25, ty, 29, ty, th_mid)
        c.set(26, ty, th_white)
        c.set(27, ty, th_light)
        c.set(29, ty, th_dark)

    # Take-up lever:
    c.line(10, 14, 8, 12, s_bright)
    c.set(7, 11, s_white)
    c.set(8, 11, s_shadow)

    # Thread guide pin:
    c.set(17, 12, s_bright)

    # =========================================================================
    # 6. RED FABRIC (Laying on plate, under presser foot, draped over front)
    # =========================================================================
    # A. Back section entering under head (y=31..32):
    for fx in range(11, 18):
        c.set(fx, 31, r_shadow)
        c.set(fx, 32, r_base)
    c.set(11, 31, r_deep)
    c.set(17, 31, r_deep)

    # B. Fabric under presser foot (y=33..34):
    for fx in range(11, 18):
        c.set(fx, 33, r_mid)
        c.set(fx, 34, r_mid)

    # C. Main fabric body spreading across table (y=35..38):
    fabric_bed = [
        (35, (7, 17)),
        (36, (5, 17)),
        (37, (4, 16)),
        (38, (4, 16)),
    ]
    for fy, (fx0, fx1) in fabric_bed:
        for fx in range(fx0, fx1 + 1):
            c.set(fx, fy, r_mid)

    # Folds and textile highlights:
    c.line(8, 35, 15, 35, r_light)
    c.set(11, 35, r_hi)
    c.line(6, 36, 14, 36, r_hi)
    c.set(9, 36, r_rim)
    c.set(10, 36, r_rim)
    c.line(5, 37, 13, 37, r_light)
    c.set(7, 37, r_hi)
    c.set(8, 37, r_hi)

    # Crease / valley shadows in the fabric:
    c.line(14, 35, 17, 35, r_base)
    c.line(13, 36, 17, 36, r_shadow)
    c.line(12, 37, 16, 37, r_deep)
    c.line(11, 38, 16, 38, r_darkest)

    # D. Draping down front face of wooden plinth (y=39..42):
    fabric_drape = [
        (39, (4, 15)),
        (40, (4, 15)),
        (41, (4, 14)),
        (42, (5, 14)),
    ]
    for fy, (fx0, fx1) in fabric_drape:
        for fx in range(fx0, fx1 + 1):
            c.set(fx, fy, r_base)

    # Draped fold highlights:
    c.line(5, 39, 11, 39, r_light)
    c.set(7, 39, r_hi)
    c.set(8, 39, r_hi)
    c.line(5, 40, 10, 40, r_mid)
    c.line(5, 41, 10, 41, r_mid)
    c.line(5, 42, 11, 42, r_shadow)

    # Shadow under right side of draped fold:
    c.line(13, 39, 15, 39, r_deep)
    c.line(12, 40, 15, 40, r_darkest)
    c.line(11, 41, 14, 41, r_darkest)
    c.line(11, 42, 14, 42, r_darkest)

    # Cast shadow of draped fabric onto wooden plinth to its right:
    c.line(16, 39, 17, 39, w_darkest)
    c.line(16, 40, 17, 40, w_darkest)
    c.line(15, 41, 16, 41, w_darkest)
    c.line(15, 42, 16, 42, w_darkest)

    # E. NEAT STITCHED SEAM LINE (Gold/cream stitches):
    stitch_points = [
        (14, 33), # needle pierce point
        (13, 34),
        (12, 35),
        (11, 36),
        (10, 37),
        (9, 38),
        (8, 39),
        (8, 40),
        (8, 41),
        (8, 42),
    ]
    for sx, sy in stitch_points:
        c.set(sx, sy, stitch_col)

    # =========================================================================
    # 7. NEEDLE BAR & PRESSER FOOT (Drawn AFTER fabric so it sits ON TOP!)
    # =========================================================================
    # A. Needle Bar:
    for ny in range(21, 28):
        c.set(14, ny, s_bright)
    c.set(14, 21, s_white)

    # Needle Clamp Block at y=27..28:
    c.set(13, 27, s_dark)
    c.set(14, 27, s_bright)
    c.set(15, 27, s_white)
    c.set(16, 27, s_dark)
    c.set(13, 28, s_shadow)
    c.set(14, 28, s_dark)

    # B. Presser Bar (behind needle bar at x=16, y=22..28):
    for py in range(22, 29):
        c.set(16, py, s_dark)
    c.set(16, 29, s_light)
    c.set(17, 28, s_white)
    c.set(17, 29, s_dark)

    # Presser Foot Shank (y=30):
    c.set(15, 30, s_bright)
    c.set(16, 30, s_light)

    # Presser Foot: Two distinct ski-shaped chrome prongs clamping the fabric!
    # Left toe (x=12..13):
    c.set(12, 31, s_white)
    c.set(13, 31, s_bright)
    c.set(12, 32, s_bright)
    c.set(13, 32, s_white)
    c.set(12, 33, s_dark)
    c.set(13, 33, s_mid)

    # Right toe (x=15..16):
    c.set(15, 31, s_bright)
    c.set(16, 31, s_white)
    c.set(15, 32, s_white)
    c.set(16, 32, s_bright)
    c.set(15, 33, s_mid)
    c.set(16, 33, s_dark)

    # Slot between toes at x=14:
    c.set(14, 29, s_bright)
    c.set(14, 30, s_bright)
    c.set(14, 31, s_white)
    c.set(14, 32, s_white)
    c.set(14, 30, s_light)

    # Compression shadows directly under the soles on row 34:
    c.set(12, 34, r_darkest)
    c.set(13, 34, r_darkest)
    c.set(15, 34, r_darkest)
    c.set(16, 34, r_darkest)

    return c

c = build_sewing_machine()
view(c)
finish(c)
