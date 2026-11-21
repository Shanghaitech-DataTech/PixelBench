import math
from pixelbench_api import new_canvas, view, save, finish

def draw_cozy_dining_table():
    c = new_canvas(64, 64)
    
    # -------------------------------------------------------------
    # COLOR PALETTE (Handcrafted cohesive warm palette)
    # -------------------------------------------------------------
    # Outlines & Shadows
    OUT = "#160a04"        # Darkest crisp outline
    OUT_SOFT = "#2c1409"   # Soft crevice outline
    SHADOW = "#100603"     # Solid floor contact shadow
    SHADOW_LT = "#220e06"  # Outer floor shadow halo
    SHADOW_AMB = "#1b0b05" # Ambient shadow under table

    # Wood - Warm Golden/Honey Oak (8 tones)
    W_DEEP = "#381708"     # Deepest wood shadow
    W_DARK = "#4f220d"     # Shadow wood
    W_SHD  = "#733514"     # Dark midtone
    W_MID  = "#994a1d"     # Base warm wood midtone
    W_WARM = "#bf6428"     # Light wood
    W_LGT  = "#dc8137"     # Highlight wood
    W_HI   = "#efa354"     # Bright edge highlight
    W_TOP  = "#fbcf80"     # Specular / topmost rim highlight

    # Cushion - Cozy Burgundy Wine Velvet (6 tones)
    C_DEEP = "#22050b"
    C_DARK = "#450c18"
    C_SHD  = "#6b1426"
    C_MID  = "#962139"
    C_LGT  = "#bf3652"
    C_HI   = "#e35976"

    # Linen Table Runner (Warm Ivory Linen)
    R_SHD_DK = "#453a2d"   # Deep fold shadow
    R_SHD  = "#635645"     # Shadow
    R_MID  = "#94846f"     # Midtone
    R_LGT  = "#c7baa5"     # Light linen
    R_CRM  = "#e8decb"     # Warm cream
    R_WHT  = "#fcf9f2"     # Linen highlight
    R_GOLD = "#d4af37"     # Fringe gold
    R_RED  = "#b91c1c"     # Folk red embroidery

    # Ceramic Fruit Compote (Fine porcelain with Delft blue motif)
    B_OUT  = "#0f172a"
    B_DEEP = "#1e293b"
    B_SHD  = "#334155"
    B_MID  = "#64748b"
    B_LGT  = "#94a3b8"
    B_CRM  = "#cbd5e1"
    B_WHT  = "#f1f5f9"
    B_SPEC = "#ffffff"
    B_BLUE = "#1d4ed8"     # Delft blue pattern
    B_BL_DK= "#1e3a8a"

    # Fruits:
    # 1. Red Apple
    A_DK   = "#450a0a"
    A_MID  = "#991b1b"
    A_RED  = "#dc2626"
    A_LGT  = "#ef4444"
    A_HI   = "#fca5a5"
    A_SPEC = "#fee2e2"
    
    # 2. Bananas
    N_TIP  = "#3e1e04"
    N_SHD  = "#78450c"
    N_MID  = "#b47a07"
    N_YEL  = "#eab308"
    N_HI   = "#fde047"
    N_SPEC = "#fef9c3"

    # 3. Purple Grapes
    G_DK   = "#240a47"
    G_SHD  = "#4c1d95"
    G_MID  = "#6d28d9"
    G_LGT  = "#8b5cf6"
    G_HI   = "#c4b5fd"
    G_SPEC = "#f5f3ff"

    # 4. Orange / Tangerine
    O_DK   = "#7c2d12"
    O_MID  = "#c2410c"
    O_ORG  = "#ea580c"
    O_LGT  = "#fb923c"
    O_HI   = "#fdba74"
    O_SPEC = "#ffedd5"

    # 5. Pear & Leaves
    P_DK   = "#14532d"
    P_MID  = "#16a34a"
    P_GRN  = "#4ade80"
    P_LGT  = "#bbf7d0"
    P_STEM = "#451a03"

    def p(x, y, col):
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, col)

    # -------------------------------------------------------------
    # 1. FLOOR CAST SHADOWS (Smooth, grounded oval)
    # -------------------------------------------------------------
    for y in range(43, 56):
        dy = y - 49
        half_w = int(22 * math.sqrt(max(0, 1 - (dy / 6.2) ** 2)))
        for x in range(32 - half_w, 32 + half_w + 1):
            dist = math.hypot((x - 32) / 22.0, dy / 6.2)
            if dist < 0.65:
                p(x, y, SHADOW)
            elif dist < 1.0:
                p(x, y, SHADOW_LT)

    # Crisp contact shadow spots under each foot
    for x in range(8, 12): p(x, 46, SHADOW); p(x, 47, SHADOW)
    for x in range(14, 18): p(x, 46, SHADOW); p(x, 47, SHADOW)
    for x in range(46, 50): p(x, 46, SHADOW); p(x, 47, SHADOW)
    for x in range(52, 56): p(x, 46, SHADOW); p(x, 47, SHADOW)
    for x in range(18, 23): p(x, 49, SHADOW); p(x, 50, SHADOW)
    for x in range(41, 46): p(x, 49, SHADOW); p(x, 50, SHADOW)
    for x in range(24, 28): p(x, 56, SHADOW); p(x, 57, SHADOW)
    for x in range(36, 40): p(x, 56, SHADOW); p(x, 57, SHADOW)

    # -------------------------------------------------------------
    # 2. NORTH CHAIR (Top - behind table)
    # -------------------------------------------------------------
    # Finials
    p(26, 12, OUT); p(26, 13, W_LGT); p(25, 13, OUT); p(27, 13, OUT)
    p(37, 12, OUT); p(37, 13, W_WARM); p(36, 13, OUT); p(38, 13, OUT)
    
    # Top crest rail (Y=14..16)
    for x in range(26, 38): p(x, 14, OUT)
    p(25, 14, OUT); p(38, 14, OUT)
    for x in range(26, 38):
        p(x, 15, W_TOP if 28 <= x <= 33 else (W_HI if x <= 35 else W_WARM))
        p(x, 16, W_WARM if 27 <= x <= 33 else W_MID)
        p(x, 17, OUT_SOFT)

    # Side posts (Y=14..23)
    for y in range(14, 23):
        p(25, y, OUT); p(26, y, W_LGT if y <= 18 else W_WARM); p(27, y, OUT_SOFT)
        p(36, y, OUT_SOFT); p(37, y, W_MID if y <= 18 else W_SHD); p(38, y, OUT)

    # 4 Vertical spindles with lighting
    for x, w_col in [(29, W_LGT), (31, W_WARM), (33, W_MID), (35, W_SHD)]:
        for y in range(18, 22):
            p(x, y, w_col)

    # Wooden Seat / Lower Rail (Y=21..22)
    for x in range(27, 37):
        p(x, 21, W_WARM if x <= 31 else W_MID)
        p(x, 22, W_MID if x <= 31 else W_SHD)

    # -------------------------------------------------------------
    # 3. TABLE LEGS & UNDERSIDE SHADOW
    # -------------------------------------------------------------
    # Back legs (in shadow under table)
    for y in range(32, 43):
        p(21, y, W_SHD); p(22, y, W_DEEP)
        p(41, y, W_SHD); p(42, y, W_DEEP)

    # Ambient deep shadow under table (between legs)
    for y in range(38, 48):
        for x in range(23, 41):
            p(x, y, SHADOW_AMB)

    # Front left leg (X=19..21, Y=36..49) - Turned wood shape
    for y in range(36, 50):
        p(18, y, OUT); p(22, y, OUT)
        if y in [38, 44]:    # turned ring bulge
            p(19, y, W_HI); p(20, y, W_WARM); p(21, y, W_SHD)
        elif y in [39, 45]:  # turned crevice
            p(19, y, W_MID); p(20, y, W_SHD); p(21, y, W_DEEP)
        else:                # leg shaft
            p(19, y, W_WARM); p(20, y, W_MID); p(21, y, W_SHD)
    p(19, 49, OUT); p(20, 49, OUT); p(21, 49, OUT)

    # Front right leg (X=42..44, Y=36..49) - Turned wood shape
    for y in range(36, 50):
        p(41, y, OUT); p(45, y, OUT)
        if y in [38, 44]:
            p(42, y, W_WARM); p(43, y, W_MID); p(44, y, W_DARK)
        elif y in [39, 45]:
            p(42, y, W_SHD); p(43, y, W_DARK); p(44, y, W_DEEP)
        else:
            p(42, y, W_MID); p(43, y, W_SHD); p(44, y, W_DARK)
    p(42, 49, OUT); p(43, 49, OUT); p(44, 49, OUT)

    # -------------------------------------------------------------
    # 4. TABLETOP (Warm Honey Oak with Smooth Horizontal Planks)
    # -------------------------------------------------------------
    table_rows = [
        (23, 22, 41),
        (24, 19, 44),
        (25, 17, 46),
        (26, 16, 47),
        (27, 16, 47),
        (28, 16, 47),
        (29, 16, 47),
        (30, 16, 47),
        (31, 16, 47),
        (32, 16, 47),
        (33, 17, 46),
        (34, 18, 45),
    ]

    for y, xs, xe in table_rows:
        for x in range(xs, xe + 1):
            t = (x - xs) / max(1, (xe - xs))
            
            if y <= 25:
                if t < 0.35: col = W_HI
                elif t < 0.70: col = W_LGT
                else: col = W_WARM
            elif y <= 28:
                if t < 0.35: col = W_LGT
                elif t < 0.70: col = W_WARM
                else: col = W_MID
            elif y <= 31:
                if t < 0.30: col = W_WARM
                elif t < 0.65: col = W_MID
                else: col = W_SHD
            else:
                if t < 0.30: col = W_MID
                elif t < 0.65: col = W_SHD
                else: col = W_DARK

            # Subtle plank seams at y=25, 28, 31
            if y in [25, 28, 31]:
                if col == W_HI: col = W_LGT
                elif col == W_LGT: col = W_WARM
                elif col == W_WARM: col = W_MID
                elif col == W_MID: col = W_SHD

            p(x, y, col)
            
        p(xs, y, OUT)
        p(xe, y, OUT)

    # Top outline of the table
    for x in range(22, 42): p(x, 22, OUT)
    for x in range(19, 22): p(x, 23, OUT)
    for x in range(42, 45): p(x, 23, OUT)
    for x in range(17, 19): p(x, 24, OUT)
    for x in range(45, 47): p(x, 24, OUT)

    # Top rim highlight
    for x in range(23, 41): p(x, 23, W_TOP)
    for x in range(20, 23): p(x, 24, W_HI)
    for x in range(41, 44): p(x, 24, W_LGT)
    p(18, 25, W_HI); p(17, 26, W_HI)

    # Table front rounded bevel edge (Y=35)
    for x in range(17, 47):
        p(x, 35, W_WARM if x < 24 else (W_MID if x < 38 else W_SHD))
    p(17, 35, OUT); p(46, 35, OUT)

    # Table front apron / skirt (Y=36..37)
    for x in range(18, 46):
        p(x, 36, W_DARK if x < 32 else W_DEEP)
        p(x, 37, W_DEEP)
        p(x, 38, OUT)
    p(17, 36, OUT); p(18, 37, OUT)
    p(46, 36, OUT); p(45, 37, OUT)

    # -------------------------------------------------------------
    # 5. LINEN TABLE RUNNER (Draped center runner)
    # -------------------------------------------------------------
    # Width X=26..37, Y=23..38
    for y in range(23, 38):
        for x in range(26, 38):
            if x in [26, 37]:
                col = R_MID
            elif x in [27, 28]:
                col = R_WHT if y <= 27 else R_CRM
            elif x in [29, 30, 31, 32]:
                col = R_CRM if y <= 29 else R_LGT
            else:
                col = R_LGT if y <= 29 else R_MID
            p(x, y, col)
            
    # Hemstitch borders
    for y in range(23, 38):
        p(26, y, R_MID)
        p(37, y, R_SHD)

    # Subtle cross-stitch pattern on runner
    p(31, 24, R_RED); p(32, 24, R_GOLD)
    p(28, 35, R_GOLD); p(30, 35, R_RED); p(33, 35, R_RED); p(35, 35, R_GOLD)

    # Drop shadow under fruit bowl onto runner (Y=31..33)
    for x in range(28, 36):
        p(x, 32, R_SHD)
    for x in range(29, 35):
        p(x, 33, R_SHD)

    # Front drape (Y=38..40) with pointed edge & fringe
    for x in range(26, 38): p(x, 38, R_LGT if x <= 31 else R_MID)
    for x in range(27, 37): p(x, 39, R_MID if x <= 31 else R_SHD)
    for x in range(29, 35): p(x, 40, R_SHD)
    for x in range(30, 34): p(x, 41, R_SHD_DK)
    # Golden fringe tassels
    p(28, 40, R_GOLD); p(30, 42, R_GOLD); p(33, 42, R_GOLD); p(35, 40, R_GOLD)

    # -------------------------------------------------------------
    # 6. WEST CHAIR (Left - Clean, elegant side profile)
    # -------------------------------------------------------------
    # Finial at top
    p(10, 20, OUT); p(10, 21, W_HI); p(9, 21, OUT); p(11, 21, OUT)
    
    # Clean upright back post (X=9..10, Y=22..35)
    for y in range(22, 36):
        p(8, y, OUT)
        p(9, y, W_LGT if y <= 26 else W_WARM)
        p(10, y, W_WARM if y <= 26 else W_MID)
        p(11, y, OUT_SOFT)

    # Plush Burgundy Seat Cushion (X=11..18, Y=32..35)
    for x in range(11, 19):
        p(x, 31, OUT)
        p(x, 32, C_HI if x <= 14 else C_LGT)
        p(x, 33, C_LGT if x <= 14 else C_MID)
        p(x, 34, C_MID if x <= 14 else C_DARK)
        p(x, 35, OUT)
    p(18, 32, OUT); p(18, 33, OUT); p(18, 34, OUT)
    p(12, 32, C_HI); p(13, 32, C_HI)

    # Wooden Seat Rail below cushion (Y=35)
    for x in range(10, 18):
        p(x, 35, W_WARM if x <= 13 else W_MID)
    p(8, 35, OUT); p(18, 35, OUT)

    # Legs (Y=36..46):
    # Rear leg: X=8..10
    for y in range(36, 47):
        p(8, y, OUT)
        p(9, y, W_WARM if y <= 40 else W_MID)
        p(10, y, OUT)
    p(9, 46, OUT)
    
    # Front leg: X=15..17
    for y in range(36, 47):
        p(15, y, OUT)
        p(16, y, W_LGT if y <= 40 else W_WARM)
        p(17, y, OUT)
    p(16, 46, OUT)
    
    # Stretcher (rung connecting legs): Y=42, X=10..15
    for x in range(10, 16):
        p(x, 42, W_WARM if x <= 12 else W_MID)
        p(x, 43, OUT)

    # -------------------------------------------------------------
    # 7. EAST CHAIR (Right - Clean, elegant side profile)
    # -------------------------------------------------------------
    # Finial at top
    p(53, 20, OUT); p(53, 21, W_WARM); p(52, 21, OUT); p(54, 21, OUT)
    
    # Clean upright back post (X=53..54, Y=22..35)
    for y in range(22, 36):
        p(52, y, OUT_SOFT)
        p(53, y, W_MID if y <= 26 else W_SHD)
        p(54, y, W_SHD if y <= 26 else W_DEEP)
        p(55, y, OUT)

    # Plush Burgundy Seat Cushion (X=45..52, Y=32..35)
    for x in range(45, 53):
        p(x, 31, OUT)
        p(x, 32, C_LGT if x >= 49 else C_MID)
        p(x, 33, C_MID if x >= 49 else C_SHD)
        p(x, 34, C_DARK)
        p(x, 35, OUT)
    p(45, 32, OUT); p(45, 33, OUT); p(45, 34, OUT)

    # Wooden Seat Rail below cushion
    for x in range(46, 54):
        p(x, 35, W_MID if x >= 50 else W_SHD)
    p(45, 35, OUT); p(55, 35, OUT)

    # Legs (Y=36..46):
    # Front leg: X=46..48
    for y in range(36, 47):
        p(46, y, OUT)
        p(47, y, W_MID if y <= 40 else W_SHD)
        p(48, y, OUT)
    p(47, 46, OUT)
    
    # Rear leg: X=53..55
    for y in range(36, 47):
        p(53, y, OUT)
        p(54, y, W_SHD if y <= 40 else W_DEEP)
        p(55, y, OUT)
    p(54, 46, OUT)
    
    # Stretcher: Y=42, X=48..54
    for x in range(48, 54):
        p(x, 42, W_SHD)
        p(x, 43, OUT)

    # -------------------------------------------------------------
    # 8. SOUTH CHAIR (Bottom - Back view facing table)
    # -------------------------------------------------------------
    # Centered at X=26..37, Y=41..56
    # Top crest rail (Y=41..43)
    p(25, 41, OUT); p(38, 41, OUT)
    for x in range(26, 38): p(x, 41, OUT)
    for x in range(26, 38):
        p(x, 42, W_TOP if 28 <= x <= 32 else (W_HI if x <= 35 else W_WARM))
        p(x, 43, W_WARM if 27 <= x <= 33 else W_MID)
        p(x, 44, OUT_SOFT)
    p(25, 42, OUT); p(38, 42, OUT)
    p(25, 43, OUT); p(38, 43, OUT)

    # Upright side posts (Y=44..56)
    for y in range(44, 57):
        p(25, y, OUT); p(26, y, W_LGT if y <= 48 else W_WARM); p(27, y, OUT_SOFT)
        p(36, y, OUT_SOFT); p(37, y, W_MID if y <= 48 else W_SHD); p(38, y, OUT)

    # 4 Vertical spindles with nice rounded shading
    for x, w_col, w_shd in [(29, W_LGT, W_WARM), (31, W_WARM, W_MID), (33, W_MID, W_SHD), (35, W_SHD, W_DARK)]:
        for y in range(44, 50):
            p(x, y, w_col)

    # Lower back rail (Y=50..51)
    for x in range(26, 38):
        p(x, 50, W_WARM if x <= 31 else W_MID)
        p(x, 51, W_MID if x <= 31 else W_SHD)
        p(x, 52, OUT)

    # Legs continuing to floor (Y=52..56)
    for y in range(52, 57):
        p(26, y, W_WARM); p(37, y, W_SHD)
    p(26, 56, OUT); p(37, 56, OUT)

    # Stretcher between rear legs (Y=54)
    for x in range(27, 37):
        p(x, 54, W_WARM if x <= 31 else W_MID)
        p(x, 55, OUT)

    # -------------------------------------------------------------
    # 9. FRUIT BOWL (Fine Porcelain Compote Centerpiece)
    # -------------------------------------------------------------
    # 1. Base / Foot (Y=30..32, X=28..35)
    p(28, 31, B_OUT); p(35, 31, B_OUT)
    for x in range(29, 35): p(x, 32, B_OUT)
    p(29, 31, B_SPEC); p(30, 31, B_WHT); p(31, 31, B_CRM); p(32, 31, B_LGT); p(33, 31, B_MID); p(34, 31, B_SHD)
    # Pedestal Stem (Y=30)
    p(29, 30, B_OUT); p(34, 30, B_OUT)
    p(30, 30, B_WHT); p(31, 30, B_CRM); p(32, 30, B_MID); p(33, 30, B_SHD)

    # 2. Bowl Body (Y=28..29, X=25..38)
    p(25, 29, B_OUT); p(38, 29, B_OUT)
    for x in range(26, 38):
        if x <= 27: col = B_SPEC
        elif x <= 29: col = B_WHT
        elif x <= 32: col = B_CRM
        elif x <= 35: col = B_LGT
        else: col = B_MID
        p(x, 29, col)
    # Delft blue decorative band (delicate floral dots)
    p(27, 29, B_BLUE); p(29, 29, B_BLUE); p(31, 29, B_BLUE); p(33, 29, B_BL_DK); p(35, 29, B_BL_DK)

    # Rim (Y=28, X=24..39)
    p(24, 28, B_OUT); p(39, 28, B_OUT)
    for x in range(25, 39):
        if x <= 26: col = B_SPEC
        elif x <= 29: col = B_WHT
        elif x <= 33: col = B_CRM
        elif x <= 36: col = B_LGT
        else: col = B_MID
        p(x, 28, col)
    # Rim top highlight (Y=27)
    p(25, 27, B_SPEC); p(26, 27, B_SPEC); p(37, 27, B_CRM); p(38, 27, B_LGT)

    # 3. FRUITS (Appetizing, 3D, Vibrant)
    # A. Red Apple (X=27..31, Y=23..27)
    # Stem & Leaf
    p(29, 21, P_STEM)     # brown stem
    p(30, 21, P_GRN)      # green leaf
    p(31, 21, P_LGT)      # leaf highlight
    p(27, 23, OUT); p(28, 23, OUT); p(30, 23, OUT)
    p(26, 24, OUT); p(31, 24, OUT)
    # Apple shading
    p(28, 24, A_SPEC); p(29, 24, A_LGT); p(30, 24, A_RED)
    p(27, 25, A_HI); p(28, 25, A_LGT); p(29, 25, A_RED); p(30, 25, A_MID)
    p(27, 26, A_LGT); p(28, 26, A_RED); p(29, 26, A_MID); p(30, 26, A_DK)

    # B. Yellow Bananas (curved bunch arching across back/right, X=31..37, Y=20..24)
    p(31, 20, N_TIP); p(32, 20, N_TIP)
    p(31, 21, OUT)
    p(32, 21, N_SPEC); p(33, 21, N_HI); p(34, 21, N_YEL); p(35, 21, OUT)
    p(33, 22, N_HI); p(34, 22, N_YEL); p(35, 22, N_MID); p(36, 22, OUT)
    p(35, 23, N_YEL); p(36, 23, N_MID); p(37, 23, OUT)
    p(37, 24, N_TIP)

    # C. Green Pear (nestled in center, X=31..33, Y=22..25)
    p(32, 22, P_LGT); p(33, 22, P_GRN)
    p(32, 23, P_GRN); p(33, 23, P_MID)
    p(32, 24, P_MID); p(33, 24, P_DK)

    # D. Juicy Orange (front right of bowl, X=33..37, Y=24..28)
    p(34, 24, OUT); p(35, 24, OUT)
    p(33, 25, OUT); p(34, 25, O_SPEC); p(35, 25, O_HI); p(36, 25, O_ORG); p(37, 25, OUT)
    p(33, 26, O_HI); p(34, 26, O_LGT); p(35, 26, O_ORG); p(36, 26, O_MID); p(37, 26, OUT)
    p(33, 27, O_LGT); p(34, 27, O_ORG); p(35, 27, O_MID); p(36, 27, O_DK); p(37, 27, OUT)
    p(34, 28, OUT); p(35, 28, OUT); p(36, 28, OUT)

    # E. Cascading Purple Grapes (left rim, X=22..26, Y=26..32)
    p(25, 26, G_HI); p(26, 26, G_MID)
    p(23, 27, OUT); p(24, 27, G_SPEC); p(24, 28, G_HI); p(23, 28, G_LGT); p(22, 28, OUT)
    p(25, 27, G_HI); p(26, 27, G_LGT); p(25, 28, G_LGT); p(26, 28, G_MID)
    p(23, 29, OUT); p(24, 29, G_HI); p(25, 29, G_MID); p(26, 29, OUT)
    p(23, 30, OUT); p(24, 30, G_LGT); p(25, 30, G_SHD); p(26, 30, OUT)
    p(24, 31, G_MID); p(25, 31, G_DK); p(24, 32, OUT); p(25, 32, OUT)

    view(c)
    finish(c)
    return c

draw_cozy_dining_table()
