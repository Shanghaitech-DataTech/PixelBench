from pixelbench_api import *

def draw_masterpiece():
    c = new_canvas(64, 64, name="fast_food_combo")

    # ========================================================
    # PALETTE
    # ========================================================
    # Table (Warm polished wood)
    T_BG     = "#b68252"
    T_LIGHT  = "#c69260"
    T_DARK   = "#986436"
    T_LINE   = "#7c4c22"

    # Tray Drop Shadow on Table
    TR_SHADOW = "#4e2c14"

    # Teal Cafeteria Tray (Glossy molded plastic)
    TR_OUTLINE = "#0c1b22"
    TR_DARK    = "#142c36"
    TR_BASE    = "#1c404e"
    TR_MID     = "#28586a"
    TR_LIGHT   = "#3a7a90"
    TR_HI      = "#5ca4bc"

    # Paper Liner
    P_BG       = "#f6f2e8"
    P_EDGE     = "#ded4c0"
    P_RED      = "#d44444"

    # Soft Contact Shadows on Paper (Warm tinted shadows)
    SH_CONTACT = "#b8ab94"
    SH_SOFT    = "#d2c6b2"

    # ========================================================
    # 1. TABLE BACKGROUND
    # ========================================================
    c.rect(0, 0, 64, 64, T_BG)
    for y in [18, 46]:
        c.line(0, y, 63, y, T_LINE)
        c.line(0, y+1, 63, y+1, T_DARK)
        c.line(0, y+2, 63, y+2, T_LIGHT)

    # Wood grain knots
    c.set(4, 7, T_DARK);   c.set(5, 7, T_LIGHT)
    c.set(22, 5, T_DARK);  c.set(23, 5, T_LIGHT)
    c.set(53, 8, T_DARK);  c.set(54, 8, T_LIGHT)
    c.set(12, 59, T_DARK); c.set(13, 59, T_LIGHT)
    c.set(45, 61, T_DARK); c.set(46, 61, T_LIGHT)

    # ========================================================
    # 2. TRAY WITH 45° FORESHORTENING
    # Tray: x=4..59, y=11..54 (width 56, height 44)
    # ========================================================
    # Cast shadow on table
    c.rect(7, 54, 52, 4, TR_SHADOW)
    c.rect(9, 57, 48, 2, TR_SHADOW)
    c.rect(59, 14, 2, 42, TR_SHADOW)

    # Tray outer outline (smooth rounded rectangle)
    c.rect(5, 12, 54, 42, TR_OUTLINE)
    c.rect(4, 13, 56, 40, TR_OUTLINE)
    c.rect(6, 11, 52, 44, TR_OUTLINE)

    # Tray raised rim
    c.rect(5, 12, 54, 41, TR_BASE)
    c.rect(6, 12, 52, 41, TR_MID)

    # Rim highlights (Top-left lighting)
    c.line(6, 12, 57, 12, TR_HI)
    c.line(6, 13, 57, 13, TR_LIGHT)
    c.line(5, 14, 5, 51, TR_LIGHT)
    c.line(6, 13, 6, 52, TR_HI)

    # Front vertical thickness of tray
    c.rect(5, 51, 54, 3, TR_DARK)
    c.line(6, 51, 57, 51, TR_BASE)
    c.line(6, 54, 57, 54, TR_OUTLINE)
    c.line(58, 14, 58, 53, TR_DARK)

    # Inner tray well
    c.rect(8, 14, 48, 36, TR_DARK)

    # Paper Liner (x=8..55, y=15..49)
    c.rect(8, 15, 48, 35, P_EDGE)
    c.rect(9, 15, 46, 34, P_BG)

    # Classic retro diner checkered border on paper liner
    for bx in range(11, 52, 4):
        c.rect(bx, 16, 2, 1, P_RED)
        c.rect(bx+2, 17, 2, 1, P_RED)
        c.rect(bx, 45, 2, 1, P_RED)
        c.rect(bx+2, 46, 2, 1, P_RED)
    c.line(10, 18, 10, 44, P_RED)
    c.line(53, 18, 53, 44, P_RED)

    # ========================================================
    # 3. FOOD CONTACT SHADOWS ON PAPER LINER (Strictly y <= 49)
    # ========================================================
    c.ellipse(19, 31, 6, 2, SH_SOFT)  # Fries carton
    c.ellipse(49, 31, 5, 2, SH_SOFT)  # Cola cup
    c.ellipse(31, 25, 4, 1, SH_SOFT)  # Sauce tub 1
    c.ellipse(37, 30, 4, 1, SH_SOFT)  # Sauce tub 2
    c.ellipse(21, 48, 11, 2, SH_SOFT) # Burger
    c.ellipse(21, 49, 9, 1, SH_CONTACT)
    c.ellipse(46, 48, 8, 2, SH_SOFT)  # Nuggets
    c.ellipse(46, 49, 6, 1, SH_CONTACT)

    # ========================================================
    # 4. FRENCH FRIES IN RED CARTON (Back-Left: x=11..27, y=9..31)
    # Bountiful overflowing fries fanning out from the carton!
    # ========================================================
    FRY_TIP    = "#5c2404"  # Toasted/burnt crispy tip
    FRY_SHADOW = "#8a4808"  # Dark shadow between fries
    FRY_DARK   = "#ba7814"  # Shadow bevel edge
    FRY_GOLD   = "#f6cc30"  # Golden fried face
    FRY_HI     = "#fff49c"  # Crisp salt/light highlight

    FBOX_OUT   = "#440606"  # Dark red outline
    FBOX_SH    = "#801010"  # Deep red shadow
    FBOX_RED   = "#d42020"  # Fast-food red
    FBOX_HI    = "#f24848"  # Left highlight
    FBOX_GOLD  = "#f8c824"  # Golden arch emblem

    # --- Step A: Carton Back Interior ---
    # Width x=13..25, y=19..23
    c.poly([(13, 20), (14, 19), (24, 19), (25, 20), (24, 23), (14, 23)], FBOX_SH, fill=True)

    # --- Step B: Bountiful crisp fries bursting out ---
    # Fries fan out: x spans from 11 to 27!
    # 1. Background layer of fries (taller, deep)
    c.line(13, 13, 14, 23, FRY_DARK); c.set(13, 13, FRY_TIP)
    c.line(15, 11, 15, 23, FRY_DARK); c.set(15, 11, FRY_TIP)
    c.line(17, 9, 17, 23, FRY_DARK);  c.set(17, 9, FRY_TIP)
    c.line(19, 10, 19, 23, FRY_DARK); c.set(19, 10, FRY_TIP)
    c.line(21, 10, 21, 23, FRY_DARK); c.set(21, 10, FRY_TIP)
    c.line(23, 11, 23, 23, FRY_DARK); c.set(23, 11, FRY_TIP)
    c.line(25, 13, 24, 23, FRY_DARK); c.set(25, 13, FRY_TIP)

    # 2. Main layer of distinct golden fry sticks (with highlights & shadow bevels)
    # Far-left tilted fry
    c.line(11, 15, 13, 23, FRY_GOLD); c.set(11, 15, FRY_HI); c.line(12, 16, 14, 24, FRY_SHADOW)
    # Fry at x=14
    c.line(13, 11, 14, 23, FRY_GOLD); c.set(13, 11, FRY_HI); c.line(14, 12, 15, 23, FRY_DARK)
    # Fry at x=16
    c.line(16, 10, 16, 24, FRY_GOLD); c.set(16, 10, FRY_HI); c.line(17, 11, 17, 24, FRY_SHADOW)
    # Center tall fry at x=18
    c.line(18, 9, 18, 24, FRY_GOLD);   c.set(18, 9, FRY_HI);   c.line(19, 10, 19, 24, FRY_DARK)
    # Fry at x=20
    c.line(20, 10, 20, 24, FRY_GOLD); c.set(20, 10, FRY_HI); c.line(21, 11, 21, 24, FRY_SHADOW)
    # Fry at x=22
    c.line(22, 11, 22, 24, FRY_GOLD); c.set(22, 11, FRY_HI); c.line(23, 12, 23, 24, FRY_DARK)
    # Far-right tilted fry
    c.line(25, 12, 23, 23, FRY_GOLD); c.set(25, 12, FRY_HI); c.line(26, 13, 24, 23, FRY_SHADOW)
    c.line(27, 14, 24, 23, FRY_GOLD); c.set(27, 14, FRY_HI)

    # 3. Foreground fries (spilling forward over front rim)
    c.line(14, 16, 15, 25, FRY_GOLD); c.set(14, 16, FRY_HI); c.set(15, 17, FRY_DARK)
    c.line(16, 14, 17, 25, FRY_GOLD); c.set(16, 14, FRY_HI); c.set(17, 15, FRY_DARK)
    c.line(18, 14, 18, 25, FRY_GOLD); c.set(18, 14, FRY_HI); c.set(19, 15, FRY_DARK)
    c.line(20, 13, 20, 25, FRY_GOLD); c.set(20, 13, FRY_HI); c.set(21, 14, FRY_DARK)
    c.line(22, 15, 21, 25, FRY_GOLD); c.set(22, 15, FRY_HI); c.set(23, 16, FRY_DARK)

    # --- Step C: Red Carton Front Wall ---
    # Smooth tapered silhouette: top width x=13..25 at y=21..23, base width x=15..23 at y=31
    front_pts_out = [
        (13, 21), (15, 22), (18, 23), (20, 23), (23, 22), (25, 21),
        (23, 31), (15, 31)
    ]
    c.poly(front_pts_out, FBOX_OUT, fill=True)

    front_pts_fill = [
        (14, 22), (16, 23), (18, 24), (20, 24), (22, 23), (24, 22),
        (22, 30), (16, 30)
    ]
    c.poly(front_pts_fill, FBOX_RED, fill=True)

    # Left edge highlight
    c.line(14, 22, 16, 30, FBOX_HI)
    c.line(15, 23, 17, 30, FBOX_HI)
    # Right edge & base shadow
    c.line(24, 22, 22, 30, FBOX_SH)
    c.line(23, 23, 21, 30, FBOX_SH)
    c.line(17, 30, 22, 30, FBOX_SH)

    # Golden Arches emblem on carton front (centered at x=19, y=26..27)
    c.poly([(17, 27), (18, 25), (19, 26), (20, 25), (21, 27)], FBOX_GOLD, fill=False)
    c.set(18, 26, FBOX_GOLD)
    c.set(20, 26, FBOX_GOLD)

    # Spilled fry on tray paper beside carton
    c.line(24, 28, 28, 30, FRY_GOLD)
    c.set(24, 28, FRY_HI)
    c.set(28, 30, FRY_TIP)
    c.line(24, 29, 28, 31, SH_SOFT)

    # ========================================================
    # 5. CUP OF COLA WITH ICE AND STRAW (Back-Right: x=43..56, y=4..31)
    # ========================================================
    COLA_DEEP   = "#140602"
    COLA_DARK   = "#2c0c04"
    COLA_AMBER  = "#5c1e08"

    ICE_HI      = "#ffffff"
    ICE_LIGHT   = "#daf0fc"
    ICE_CYAN    = "#88c4dc"
    ICE_DARK    = "#447892"

    LID_HI      = "#ffffff"
    LID_MID     = "#c8d6e0"
    LID_DARK    = "#708490"

    CUP_OUT     = "#200404"
    CUP_RED     = "#d42222"
    CUP_SH      = "#801010"
    CUP_HI      = "#f04848"
    CUP_WHITE   = "#f2f6fa"
    CUP_W_SH    = "#b4c0cc"

    # Cup Body (Tapered cylinder from y=16 to y=30)
    # Top width: x=44..54 (11 px), Base width: x=46..52 (7 px)
    c.poly([(43, 16), (45, 30), (53, 30), (55, 16)], CUP_OUT, fill=True)
    c.poly([(44, 16), (46, 29), (52, 29), (54, 16)], CUP_RED, fill=True)

    # Cylindrical Shading
    c.line(44, 17, 46, 29, CUP_HI)
    c.line(54, 17, 52, 29, CUP_SH)
    c.line(53, 17, 51, 29, CUP_SH)

    # Smooth, clean diagonal wave graphic across cup
    c.poly([(44, 21), (47, 23), (53, 21), (53, 23), (48, 25), (44, 23)], CUP_WHITE, fill=True)
    c.line(51, 21, 53, 21, CUP_W_SH)
    c.line(51, 22, 53, 22, CUP_W_SH)

    # Bottom rim of cup (white rolled paper base)
    c.line(46, 29, 52, 29, CUP_WHITE)
    c.line(46, 30, 52, 30, CUP_OUT)

    # Translucent Lid (Elliptical rim at 45° angle)
    c.ellipse(49, 15, 6, 2, LID_DARK, fill=True)
    c.ellipse(49, 15, 5, 2, LID_MID, fill=True)
    c.line(44, 15, 54, 15, LID_HI)

    # Dark cola liquid surface visible inside lid
    c.ellipse(49, 15, 4, 1, COLA_DARK, fill=True)

    # Floating Ice Cubes:
    # Ice Cube 1 (left): 3x2 px
    c.rect(46, 14, 3, 2, ICE_CYAN)
    c.set(46, 14, ICE_HI)
    c.set(47, 14, ICE_LIGHT)
    c.set(48, 15, ICE_DARK)

    # Ice Cube 2 (right): 2x2 px
    c.rect(50, 15, 2, 2, ICE_CYAN)
    c.set(50, 15, ICE_HI)
    c.set(51, 16, ICE_DARK)

    # Bubbles / carbonation
    c.set(45, 15, COLA_AMBER)
    c.set(49, 14, ICE_LIGHT)
    c.set(52, 14, COLA_AMBER)

    # Glistening condensation droplets on cup
    c.set(46, 18, ICE_LIGHT)
    c.set(47, 26, ICE_LIGHT)

    # Straw (Angles up-left from center of cup (48,14) up to (43,4))
    # Crisp 2px wide straw with red/white candy stripes and dark outline
    straw_pts = [
        (48, 14, True),
        (47, 12, False),
        (46, 10, True),
        (45, 8, False),
        (44, 6, True),
        (43, 4, False),
    ]
    for (sx, sy, _) in straw_pts:
        c.set(sx-1, sy, CUP_OUT)
        c.set(sx+1, sy, CUP_OUT)
        c.set(sx-1, sy+1, CUP_OUT)
        c.set(sx+1, sy+1, CUP_OUT)
    for (sx, sy, is_red) in straw_pts:
        col = "#e82020" if is_red else "#ffffff"
        c.set(sx, sy, col)
        c.set(sx, sy+1, col)
    c.set(43, 3, CUP_OUT)
    c.set(42, 3, CUP_OUT)
    c.set(42, 4, "#ffffff")

    # ========================================================
    # 6. DIPPING SAUCE CUPS (Middle: x=27..42, y=20..31)
    # Clean, distinct 3D miniature fast food sauce tubs!
    # ========================================================
    TUB_OUT = "#283038"
    TUB_HI  = "#ffffff"
    TUB_MID = "#d0d8e0"
    TUB_SH  = "#94a2b0"

    # Tub 1: Honey Mustard / Sweet & Sour (x=27..34, y=20..25)
    # 3D Front wall thickness
    c.rect(27, 24, 8, 2, TUB_OUT)
    c.rect(28, 24, 6, 1, TUB_SH)
    # Top rim
    c.rect(27, 20, 8, 5, TUB_OUT)
    c.rect(28, 20, 6, 4, TUB_HI)
    c.line(28, 23, 33, 23, TUB_MID)
    # Golden mustard sauce well (4x2 px)
    c.rect(29, 21, 4, 2, "#d68810")
    c.set(29, 21, "#ffe454") # Glossy liquid reflection
    c.set(30, 21, "#f8c028")
    c.set(32, 22, "#965408") # Deep shadow corner
    # Foil pull tab on top-left corner
    c.set(27, 20, TUB_MID)
    c.set(26, 19, TUB_HI)
    c.set(26, 20, TUB_OUT)

    # Tub 2: Barbecue / Ketchup (x=33..40, y=25..30)
    # 3D Front wall thickness
    c.rect(33, 29, 8, 2, TUB_OUT)
    c.rect(34, 29, 6, 1, TUB_SH)
    # Top rim
    c.rect(33, 25, 8, 5, TUB_OUT)
    c.rect(34, 25, 6, 4, TUB_HI)
    c.line(34, 28, 39, 28, TUB_MID)
    # Crimson ketchup sauce well
    c.rect(35, 26, 4, 2, "#b41212")
    c.set(35, 26, "#f85858") # Glossy shine
    c.set(36, 26, "#d82020")
    c.set(38, 27, "#640808") # Deep dark depth
    # Foil pull tab on bottom-right corner
    c.set(40, 29, TUB_MID)
    c.set(41, 30, TUB_HI)
    c.set(41, 29, TUB_OUT)

    # ========================================================
    # 7. CHEESEBURGER (Front-Left: x=8..33, y=30..50)
    # Plump rounded dome bun, ruffly lettuce, juicy tomato,
    # melted cheddar cheese drips, grilled beef patty, bottom bun.
    # ========================================================
    B_OUTLINE   = "#2c0e04"
    BUN_HI      = "#fcda88"
    BUN_LIGHT   = "#f2ae46"
    BUN_MID     = "#d2822a"
    BUN_DARK    = "#a45618"
    BUN_DEEP    = "#6e320a"

    SESAME      = "#fff8e0"
    SESAME_SH   = "#8a3c08"

    LET_HI      = "#8ae832"
    LET_MID     = "#44b618"
    LET_DARK    = "#18640c"

    TOMATO      = "#e82424"
    TOMATO_DARK = "#961010"

    PICKLE      = "#2e6414"
    PICKLE_LT   = "#4a8e24"

    CHEESE_HI   = "#ffee48"
    CHEESE_MID  = "#fcb014"
    CHEESE_DARK = "#d46e00"

    MEAT_HI     = "#6e381c"
    MEAT_MID    = "#4a2010"
    MEAT_DARK   = "#260c04"

    # --- Bottom Bun ---
    # y=47 to 50, x=11..31
    c.poly([(13, 47), (11, 48), (12, 50), (29, 50), (30, 48), (28, 47)], B_OUTLINE, fill=True)
    c.poly([(13, 48), (12, 49), (13, 49), (28, 49), (29, 49), (27, 48)], BUN_MID, fill=True)
    c.line(13, 49, 28, 49, BUN_DARK)
    c.line(14, 48, 22, 48, BUN_LIGHT)

    # --- Grilled Beef Patty ---
    # y=43 to 47, x=9..33
    c.poly([(10, 43), (8, 45), (10, 47), (31, 47), (33, 45), (31, 43)], B_OUTLINE, fill=True)
    c.poly([(10, 44), (9, 45), (11, 46), (30, 46), (32, 45), (30, 44)], MEAT_MID, fill=True)
    # Patty texture & grill marks
    c.line(12, 44, 15, 46, MEAT_DARK)
    c.line(18, 44, 21, 46, MEAT_DARK)
    c.line(24, 44, 27, 46, MEAT_DARK)
    c.set(11, 45, MEAT_HI)
    c.set(16, 45, MEAT_HI)
    c.set(22, 45, MEAT_HI)
    c.set(28, 45, MEAT_HI)

    # --- Sliced Tomato (left) & Pickle (right) peeking out ---
    c.poly([(11, 42), (10, 43), (17, 43), (16, 42)], TOMATO, fill=True)
    c.line(11, 43, 16, 43, TOMATO_DARK)
    # Pickle slice
    c.poly([(24, 42), (28, 42), (27, 43), (23, 43)], PICKLE, fill=True)
    c.set(25, 42, PICKLE_LT); c.set(26, 42, PICKLE_LT)

    # --- Melted Cheddar Cheese ---
    # Cheese drapes over the patty and drips down!
    c.poly([(10, 41), (31, 41), (32, 43), (9, 43)], CHEESE_MID, fill=True)
    # Drip 1 (left)
    c.poly([(13, 42), (16, 42), (15, 46), (14, 46)], CHEESE_MID, fill=True)
    c.set(14, 46, CHEESE_DARK)
    # Drip 2 (center, long gooey drip down patty)
    c.poly([(19, 42), (24, 42), (23, 48), (21, 48)], CHEESE_MID, fill=True)
    c.line(21, 48, 23, 48, CHEESE_DARK)
    c.set(21, 43, CHEESE_HI)
    c.set(22, 44, CHEESE_HI)
    # Drip 3 (right)
    c.poly([(27, 42), (31, 42), (30, 45), (28, 45)], CHEESE_MID, fill=True)
    c.set(29, 45, CHEESE_DARK)
    # Cheese highlights and shadow creases
    c.line(10, 41, 30, 41, CHEESE_HI)
    c.line(10, 43, 12, 43, CHEESE_DARK)
    c.line(17, 43, 18, 43, CHEESE_DARK)
    c.line(25, 43, 26, 43, CHEESE_DARK)

    # --- Fresh Crisp Lettuce ---
    # Wavy, ruffled leaf layer peeking out
    c.poly([(9, 39), (32, 39), (33, 42), (8, 42)], LET_MID, fill=True)
    # Ruffles / curls
    ruffles = [
        (8, 41), (10, 42), (12, 41), (15, 42), (18, 41),
        (21, 42), (24, 41), (27, 42), (30, 41), (33, 41)
    ]
    for (rx, ry) in ruffles:
        c.set(rx, ry, LET_HI)
        c.set(rx, ry+1, LET_DARK)

    # --- Top Bun ---
    # Plump, perfectly rounded toasted brioche dome: y=30..40, x=8..33
    bun_outline = [
        (16, 30), (25, 30), (29, 31), (32, 33), (34, 36), (34, 38), (32, 40),
        (9, 40), (7, 38), (7, 36), (9, 33), (12, 31)
    ]
    c.poly(bun_outline, B_OUTLINE, fill=True)

    bun_fill = [
        (16, 31), (25, 31), (28, 32), (31, 34), (33, 36), (33, 38), (31, 39),
        (10, 39), (8, 38), (8, 36), (10, 34), (13, 32)
    ]
    c.poly(bun_fill, BUN_MID, fill=True)

    # Bun 3D Lighting (spherical gradient)
    c.ellipse(18, 33, 7, 2, BUN_LIGHT, fill=True)
    c.ellipse(16, 32, 4, 1, BUN_HI, fill=True)
    c.line(10, 39, 31, 39, BUN_DARK)
    c.line(29, 38, 32, 38, BUN_DARK)
    c.line(30, 36, 32, 36, BUN_DARK)
    c.line(10, 40, 31, 40, BUN_DEEP)

    # Delicate sesame seeds scattered radially across top bun
    sesame_pts = [
        (16, 32), (20, 32), (24, 32),
        (13, 34), (17, 34), (21, 34), (25, 34), (28, 34),
        (11, 36), (15, 36), (19, 36), (23, 36), (27, 36), (31, 36),
        (13, 38), (17, 38), (21, 38), (25, 38), (29, 38)
    ]
    for (sx, sy) in sesame_pts:
        c.set(sx, sy, SESAME)
        c.set(sx, sy+1, SESAME_SH)

    # ========================================================
    # 8. CRISPY CHICKEN NUGGETS (Front-Right: x=36..55, y=37..50)
    # Strictly y <= 50! Clean, crispy, crunchy fried texture.
    # ========================================================
    NUG_HI    = "#ffe494"  # Crunchy light flake
    NUG_CRUST = "#f8be40"  # Crisp golden crust
    NUG_GOLD  = "#d68018"  # Fried midtone
    NUG_DARK  = "#9c4e0a"  # Toasted brown shadow
    NUG_DEEP  = "#502404"  # Dark crevice / outline

    # Nugget 1 (Bottom-Left - Iconic "Boot" / L-shape): x=36..44, y=43..50
    boot_poly = [(38, 43), (44, 43), (44, 48), (42, 50), (37, 50), (36, 48), (36, 46), (38, 45)]
    c.poly(boot_poly, NUG_DEEP, fill=True)
    c.poly([(39, 44), (43, 44), (43, 47), (41, 49), (38, 49), (37, 48), (37, 47), (39, 46)], NUG_GOLD, fill=True)
    c.set(39, 45, NUG_CRUST); c.set(40, 45, NUG_HI); c.set(41, 45, NUG_CRUST)
    c.set(38, 48, NUG_CRUST); c.set(39, 48, NUG_HI)
    c.set(42, 48, NUG_DARK);  c.set(40, 49, NUG_DARK)

    # Nugget 2 (Bottom-Right - "Bell" shape): x=45..54, y=43..50
    bell_poly = [(48, 43), (52, 43), (54, 46), (54, 49), (52, 50), (46, 50), (45, 48), (46, 45)]
    c.poly(bell_poly, NUG_DEEP, fill=True)
    c.poly([(48, 44), (51, 44), (53, 46), (53, 48), (51, 49), (47, 49), (46, 48), (47, 45)], NUG_GOLD, fill=True)
    c.set(49, 45, NUG_HI);    c.set(50, 45, NUG_CRUST)
    c.set(48, 47, NUG_CRUST); c.set(51, 46, NUG_HI)
    c.set(47, 48, NUG_DARK);  c.set(52, 48, NUG_DARK)

    # Nugget 3 (Back - "Bone" / Bowtie shape): x=43..53, y=37..44
    bone_poly = [(45, 37), (51, 37), (53, 39), (52, 42), (50, 44), (45, 44), (43, 42), (43, 39)]
    c.poly(bone_poly, NUG_DEEP, fill=True)
    c.poly([(45, 38), (50, 38), (52, 39), (51, 41), (49, 43), (46, 43), (44, 41), (44, 39)], NUG_GOLD, fill=True)
    c.set(47, 39, NUG_HI);    c.set(48, 39, NUG_CRUST)
    c.set(50, 40, NUG_HI);    c.set(46, 42, NUG_DARK); c.set(49, 42, NUG_DARK)

    # Nugget 4 (Top - Tilted crispy nugget propped across): x=39..48, y=38..45
    top_poly = [(42, 38), (46, 38), (48, 40), (47, 44), (44, 45), (40, 45), (39, 42), (40, 39)]
    c.poly(top_poly, NUG_DEEP, fill=True)
    c.poly([(42, 39), (45, 39), (47, 40), (46, 43), (44, 44), (41, 44), (40, 42), (41, 40)], NUG_GOLD, fill=True)
    c.set(43, 40, NUG_HI);    c.set(44, 40, NUG_CRUST); c.set(45, 41, NUG_HI)
    c.set(42, 42, NUG_CRUST); c.set(43, 42, NUG_HI)
    c.set(42, 43, NUG_DARK);  c.set(45, 43, NUG_DARK)

    # Crispy fried crumbs on the paper liner (y <= 50)
    c.set(36, 49, NUG_CRUST)
    c.set(54, 48, NUG_CRUST)
    c.set(53, 50, NUG_HI)

    print(c.stats_text())
    return c

c = draw_masterpiece()
view(c)
finish(c)
