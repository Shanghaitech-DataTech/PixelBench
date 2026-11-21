from pixelbench_api import *

def build_bus():
    c = new_canvas(64, 32)

    # ------------------ PALETTE ------------------
    # Crisp, harmonious pixel-art palette for a modern city transit bus

    # Whites & Light Greys (Body & Roof)
    W_SPEC      = "#FFFFFF"
    W_BODY      = "#EDF2F7"
    W_MID       = "#D0DBE5"
    W_SHADOW    = "#9FB0C0"
    W_DARK      = "#758696"

    # Livery: Modern Electric Cyan & Warm Gold
    CYAN_SPEC   = "#6DF0F0"
    CYAN_HI     = "#2ED3E6"
    CYAN_MID    = "#0CA5B8"
    CYAN_DARK   = "#086E7B"
    CYAN_DEEP   = "#054852"
    GOLD_ACCENT = "#FFAA00"
    GOLD_DARK   = "#B87800"

    # Frames, Rubber, Chassis, Louvers
    BLACK       = "#080A0C"
    DARK_FRAME  = "#12161A"
    DARK_SEAL   = "#1A2025"
    BUMPER_DARK = "#242A30"
    BUMPER_MED  = "#343E48"
    SKIRT_GREY  = "#3E4954"
    VENT_SLOT   = "#14181C"

    # Flush-glazed Glass & Reflections
    GLASS_DEEP  = "#0E151C"
    GLASS_DARK  = "#141F2A"
    GLASS_MID   = "#1C2D3B"
    GLASS_LIGHT = "#283E51"
    G_SHEEN_DIM = "#3A566F"
    G_SHEEN_MED = "#527594"
    G_SHEEN_HI  = "#7D9FBE"
    G_SPEC      = "#BED6EC"

    # Interior elements
    INT_SEAT    = "#14202B"
    INT_POLE    = "#D89E08"
    INT_HANDLE  = "#9AAEC0"
    CEIL_GLOW   = "#D0DFEC"

    # Electronic Route Display (Amber LED Matrix)
    LED_BG      = "#0B0904"
    LED_BRIGHT  = "#FFAE00"
    LED_MID     = "#CC7400"
    LED_DIM     = "#543000"

    # Exterior Lights
    LIGHT_WHITE = "#FFFFFF"
    LIGHT_CYAN  = "#D2F2FF"
    LIGHT_AMBER = "#FF9900"
    LIGHT_RED_HI= "#FF2438"
    LIGHT_RED   = "#CC1426"
    LIGHT_RED_DK= "#750813"

    # Wheels & Tires
    TIRE_BLACK  = "#0F1215"
    TIRE_DARK   = "#1C2126"
    TIRE_TREAD  = "#2C343C"
    TIRE_HI     = "#444F5A"
    RIM_DARK    = "#22272D"
    RIM_MED     = "#525E6A"
    RIM_LIGHT   = "#8A99A8"
    RIM_HI      = "#CCD8E4"
    RIM_WHITE   = "#FFFFFF"

    # Ground Shadows
    SHADOW_CORE = "#00000088"
    SHADOW_MID  = "#00000045"
    SHADOW_SOFT = "#00000020"

    # ------------------ 1. GROUND SHADOW ------------------
    for x in range(3, 62):
        c.set(x, 30, SHADOW_SOFT)
    for x in range(5, 60):
        c.set(x, 29, SHADOW_MID)
    # Dense shadow under tires
    for x in range(17, 23):
        c.set(x, 29, SHADOW_CORE)
        c.set(x, 30, SHADOW_MID)
    for x in range(45, 51):
        c.set(x, 29, SHADOW_CORE)
        c.set(x, 30, SHADOW_MID)

    # ------------------ 2. WHEELS & WELLS ------------------
    def draw_wheel(cx, cy):
        # cx = 16 (front), cx = 44 (rear). cy = 21. Tire touches y=28.
        # Wheel well cutout (dark recess behind tire)
        for dy in range(19, 25):
            for dx in range(cx - 1, cx + 9):
                c.set(dx, dy, TIRE_BLACK)

        # 8x8 Tire:
        # Top (cy) & Bottom (cy+7): width 4 (dx = 2..5)
        for dx in range(cx + 2, cx + 6):
            c.set(dx, cy, TIRE_HI)
            c.set(dx, cy + 7, TIRE_BLACK)
        # Shoulders (cy+1 & cy+6): width 6 (dx = 1..6)
        for dx in range(cx + 1, cx + 7):
            c.set(dx, cy + 1, TIRE_TREAD)
            c.set(dx, cy + 6, TIRE_DARK)
        # Sidewalls (cy+2..cy+5): width 8
        for dy in range(cy + 2, cy + 6):
            c.set(cx, dy, TIRE_BLACK)
            c.set(cx + 1, dy, TIRE_DARK)
            c.set(cx + 6, dy, TIRE_DARK)
            c.set(cx + 7, dy, TIRE_BLACK)

        # 4x4 Symmetrical Alloy Rim (cx+2..cx+5, cy+2..cy+5)
        # Circular silver ring with dark center hub & lug nuts
        # cy+2 (top of rim):
        c.set(cx + 2, cy + 2, RIM_LIGHT)
        c.set(cx + 3, cy + 2, RIM_WHITE)
        c.set(cx + 4, cy + 2, RIM_HI)
        c.set(cx + 5, cy + 2, RIM_LIGHT)
        # cy+3:
        c.set(cx + 2, cy + 3, RIM_WHITE)
        c.set(cx + 3, cy + 3, RIM_DARK)
        c.set(cx + 4, cy + 3, RIM_DARK)
        c.set(cx + 5, cy + 3, RIM_MED)
        # cy+4:
        c.set(cx + 2, cy + 4, RIM_HI)
        c.set(cx + 3, cy + 4, RIM_LIGHT) # center hub cap
        c.set(cx + 4, cy + 4, RIM_DARK)
        c.set(cx + 5, cy + 4, RIM_MED)
        # cy+5 (bottom of rim):
        c.set(cx + 2, cy + 5, RIM_MED)
        c.set(cx + 3, cy + 5, RIM_LIGHT)
        c.set(cx + 4, cy + 5, RIM_MED)
        c.set(cx + 5, cy + 5, RIM_DARK)

        # Smooth Wheel Arch Flare (black rubber trim around cutout)
        c.set(cx - 1, cy + 2, DARK_SEAL)
        c.set(cx - 1, cy + 1, DARK_SEAL)
        c.set(cx, cy, DARK_FRAME)
        for dx in range(cx + 1, cx + 7):
            c.set(dx, cy - 1, DARK_FRAME) # arch peak at y=20
        c.set(cx + 7, cy, DARK_FRAME)
        c.set(cx + 8, cy + 1, DARK_SEAL)
        c.set(cx + 8, cy + 2, DARK_SEAL)

    draw_wheel(16, 21)
    draw_wheel(44, 21)

    # ------------------ 3. ROOFTOP FAIRINGS & HVAC/BATTERY POD ------------------
    # Aerodynamic cowl: x=11..50, y=4..7
    c.line(14, 4, 48, 4, W_SPEC)
    c.rect(13, 5, 36, 2, W_BODY)
    c.line(13, 5, 48, 5, W_SPEC)

    # Forward aerodynamic sweep
    c.set(13, 4, W_SPEC)
    c.set(12, 5, W_SPEC)
    c.set(11, 6, W_MID)
    c.set(10, 7, W_MID)

    # Solid aerodynamic rear taper down to roofline
    c.set(48, 4, W_MID)
    c.set(48, 5, W_BODY)
    c.set(48, 6, W_BODY)
    c.set(49, 5, W_MID)
    c.set(49, 6, W_BODY)
    c.set(50, 6, W_SHADOW)

    # Louvered cooling grilles on the roof pod
    for vx in [18, 20, 22, 24, 26, 35, 37, 39, 41, 43]:
        c.set(vx, 5, SKIRT_GREY)
        c.set(vx, 6, VENT_SLOT)

    # Main bus roof edge: y=7..8
    c.line(6, 7, 58, 7, W_SPEC)
    c.line(5, 8, 58, 8, W_BODY)
    c.set(59, 7, W_MID)
    c.set(59, 8, W_SHADOW)

    # ------------------ 4. FRONT END & DRIVER CABIN (x=1..6) ------------------
    # Aerodynamic front curvature
    c.set(4, 8, W_SPEC)
    c.set(3, 9, W_BODY)
    c.set(3, 10, DARK_FRAME)
    c.set(3, 11, DARK_FRAME)
    c.set(3, 12, DARK_FRAME)
    c.set(3, 13, DARK_FRAME)
    c.set(3, 14, DARK_FRAME)
    c.set(3, 15, DARK_FRAME)
    c.set(3, 16, W_BODY)
    c.set(3, 17, W_BODY)
    c.set(2, 18, DARK_FRAME) # headlight bezel
    c.set(2, 19, BUMPER_MED) # front bumper profile
    c.set(2, 20, BUMPER_MED)
    c.set(2, 21, BUMPER_MED)
    c.set(2, 22, BUMPER_DARK)
    c.set(3, 23, DARK_FRAME) # lower front splitter

    # Front Windshield Glass (x=4..5, y=9..16)
    for y in range(9, 17):
        c.set(4, y, GLASS_MID)
        c.set(5, y, GLASS_DARK)
    # Windshield sheen reflection
    c.set(4, 11, G_SHEEN_MED)
    c.set(4, 12, G_SHEEN_HI)
    c.set(5, 13, G_SHEEN_DIM)

    # Front Destination Display (Amber LED sign inside front header at y=9..10, x=4..5)
    c.set(4, 9, LED_BRIGHT)
    c.set(5, 9, LED_MID)
    c.set(4, 10, LED_MID)
    c.set(5, 10, LED_DIM)

    # A-Pillar (vertical black structural divider): x=6, y=8..18
    for y in range(8, 19):
        c.set(6, y, DARK_FRAME)

    # Modern Side Transit Mirror (hanging rabbit-ear mirror)
    c.set(2, 8, DARK_FRAME)
    c.set(1, 9, DARK_FRAME)
    c.set(1, 10, DARK_FRAME)
    c.set(1, 11, BUMPER_DARK)
    c.set(1, 12, BUMPER_DARK)
    c.set(2, 11, G_SHEEN_HI) # reflective glass
    c.set(2, 12, G_SHEEN_DIM)

    # Headlight Cluster (x=3..5, y=17..19)
    c.set(4, 17, W_BODY)
    c.set(5, 17, W_BODY)

    c.set(3, 18, LIGHT_WHITE)   # Modern LED Projector Beam
    c.set(4, 18, LIGHT_CYAN)    # Daytime Running Light (DRL)
    c.set(5, 18, DARK_FRAME)    # Headlight bezel

    c.set(3, 19, LIGHT_AMBER)   # Front turn indicator
    c.set(4, 19, BUMPER_MED)
    c.set(5, 19, BUMPER_MED)

    # Front bumper lower area
    c.set(3, 20, BUMPER_MED)
    c.set(4, 20, BUMPER_MED)
    c.set(5, 20, BUMPER_MED)

    c.set(3, 21, CYAN_HI)
    c.set(4, 21, CYAN_HI)
    c.set(5, 21, CYAN_HI)

    c.set(3, 22, CYAN_MID)
    c.set(4, 22, CYAN_MID)
    c.set(5, 22, CYAN_MID)

    c.set(4, 23, DARK_FRAME)
    c.set(5, 23, DARK_FRAME)

    # Amber front corner marker reflector
    c.set(3, 20, LIGHT_AMBER)

    # ------------------ 5. FRONT PASSENGER ENTRANCE DOOR (x=7..14, y=8..23) ------------------
    # Outer frame & header
    for x in range(7, 15):
        c.set(x, 8, DARK_FRAME)
        c.set(x, 9, DARK_FRAME)

    # Vertical frames & center split seal
    for y in range(9, 24):
        c.set(7, y, DARK_FRAME)
        c.set(10, y, DARK_SEAL)
        c.set(11, y, DARK_SEAL)
        c.set(14, y, DARK_FRAME)

    # Glass panels in door leaves:
    # Leaf 1: cols 8..9, Leaf 2: cols 12..13, rows 10..21
    for y in range(10, 22):
        c.set(8, y, GLASS_MID)
        c.set(9, y, GLASS_DARK)
        c.set(12, y, GLASS_MID)
        c.set(13, y, GLASS_DARK)

    # Crisp diagonal glass sheens across door leaves
    c.set(8, 11, G_SHEEN_MED)
    c.set(9, 12, G_SHEEN_HI)
    c.set(8, 12, G_SHEEN_DIM)

    c.set(12, 13, G_SHEEN_MED)
    c.set(13, 14, G_SHEEN_HI)
    c.set(12, 14, G_SHEEN_DIM)

    # Yellow vertical safety grab pole inside front entrance (in left leaf near partition)
    for y in range(13, 19):
        c.set(8, y, INT_POLE)

    # Waist-height door push handles / safety touch-edges
    c.set(9, 16, INT_HANDLE)
    c.set(12, 16, INT_HANDLE)

    # Door bottom kick plates (y=22..23)
    for x in [8, 9, 12, 13]:
        c.set(x, 22, CYAN_DARK)
        c.set(x, 23, BUMPER_MED)

    # ------------------ 6. CONTINUOUS BODY PANELS & LIVERY ------------------
    # Lower window sill (y=18)
    for x in range(15, 56):
        c.set(x, 18, DARK_FRAME)

    # White body band (y=19)
    for x in range(15, 59):
        c.set(x, 19, W_BODY)
    c.set(15, 19, W_SPEC)
    c.set(24, 19, W_SPEC)
    c.set(35, 19, W_SPEC)
    c.set(43, 19, W_SPEC)
    c.set(52, 19, W_SPEC)

    # Gold accent line (y=20)
    for x in range(24, 36):
        c.set(x, 20, GOLD_ACCENT)
    for x in range(52, 59):
        c.set(x, 20, GOLD_ACCENT)
    c.set(15, 20, GOLD_ACCENT)
    c.set(24, 20, GOLD_ACCENT)
    c.set(43, 20, GOLD_ACCENT)
    c.set(52, 20, GOLD_ACCENT)

    # Electric Teal Livery (y=21..22) & Skirt (y=23)
    for x in range(25, 36):
        c.set(x, 21, CYAN_HI)
        c.set(x, 22, CYAN_MID)
        c.set(x, 23, SKIRT_GREY)

    for x in range(52, 56):
        c.set(x, 21, CYAN_HI)
        c.set(x, 22, CYAN_MID)
        c.set(x, 23, SKIRT_GREY)

    # Mid-body amber side marker reflector
    c.set(30, 21, LIGHT_AMBER)
    c.set(30, 22, LIGHT_AMBER)

    # ------------------ 7. PASSENGER WINDOWS ------------------
    # Top flush-glaze header: y=8
    for x in range(15, 56):
        c.set(x, 8, DARK_FRAME)

    # --- A) Window over Front Wheel (x=15..23, y=9..17) ---
    for y in range(9, 18):
        c.set(15, y, DARK_FRAME)
        c.set(19, y, DARK_FRAME) # center mullion
        for x in list(range(16, 19)) + list(range(20, 24)):
            c.set(x, y, GLASS_MID)

    # Soft ceiling light glow
    c.line(16, 9, 23, 9, CEIL_GLOW)
    c.set(19, 9, DARK_FRAME)

    # Passenger seats visible through tinted glass
    for x in [17, 18, 21, 22]:
        c.set(x, 15, INT_SEAT)
        c.set(x, 16, INT_SEAT)
        c.set(x, 17, INT_SEAT)

    # Diagonal glass sheen
    c.set(17, 11, G_SHEEN_MED)
    c.set(18, 12, G_SHEEN_HI)
    c.set(21, 11, G_SHEEN_MED)
    c.set(22, 12, G_SHEEN_HI)

    # --- B) Mid-Cabin Windows & Electronic Route Display (x=24..35, y=9..17) ---
    # Vertical pillars at x=24, 30, 35
    for y in range(9, 18):
        c.set(24, y, DARK_FRAME)
        c.set(30, y, DARK_FRAME)
        c.set(35, y, DARK_FRAME)

    # Base tinted glass
    for y in range(9, 18):
        for x in list(range(25, 30)) + list(range(31, 35)):
            c.set(x, y, GLASS_MID)

    # Soft ceiling light glow
    c.line(25, 9, 29, 9, CEIL_GLOW)
    c.line(31, 9, 34, 9, CEIL_GLOW)

    # *** SIMPLIFIED ELECTRONIC ROUTE DISPLAY (SIDE) ***
    # Mounted in upper window transom: y=10..12, x=25..34 (skipping pillar at x=30)
    # Deep black LED matrix housing box
    for y in range(10, 13):
        for x in list(range(25, 30)) + list(range(31, 35)):
            c.set(x, y, LED_BG)

    # Left pane (x=25..29): Route number "8" in crisp 3x3 amber LED matrix dots:
    # Row 10: # # #
    c.set(26, 10, LED_BRIGHT)
    c.set(27, 10, LED_BRIGHT)
    c.set(28, 10, LED_BRIGHT)
    # Row 11: # . #
    c.set(26, 11, LED_BRIGHT)
    c.set(27, 11, LED_DIM)
    c.set(28, 11, LED_BRIGHT)
    # Row 12: # # #
    c.set(26, 12, LED_BRIGHT)
    c.set(27, 12, LED_BRIGHT)
    c.set(28, 12, LED_BRIGHT)

    # Right pane (x=31..34): Scrolling destination text (two crisp amber LED dot rows):
    # Line 1 (Row 10):
    c.set(31, 10, LED_BRIGHT)
    c.set(32, 10, LED_MID)
    c.set(33, 10, LED_BRIGHT)
    c.set(34, 10, LED_MID)
    # Line 2 (Row 12):
    c.set(31, 12, LED_MID)
    c.set(32, 12, LED_BRIGHT)
    c.set(33, 12, LED_MID)
    c.set(34, 12, LED_BRIGHT)

    # Mid-cabin seats & interior grab rails
    for x in [26, 28, 32, 34]:
        c.set(x, 15, INT_SEAT)
        c.set(x, 16, INT_SEAT)
        c.set(x, 17, INT_SEAT)

    # Diagonal glass reflections across mid-cabin
    c.set(27, 14, G_SHEEN_MED)
    c.set(28, 15, G_SHEEN_HI)
    c.set(29, 16, G_SPEC)
    c.set(32, 14, G_SHEEN_MED)
    c.set(33, 15, G_SHEEN_HI)
    c.set(34, 16, G_SPEC)

    # ------------------ 8. REAR PASSENGER EXIT DOOR (x=36..43, y=8..23) ------------------
    # Outer frame & header
    for x in range(36, 44):
        c.set(x, 8, DARK_FRAME)
        c.set(x, 9, DARK_FRAME)

    # Vertical frames & center split
    for y in range(9, 24):
        c.set(36, y, DARK_FRAME)
        c.set(39, y, DARK_SEAL)
        c.set(40, y, DARK_SEAL)
        c.set(43, y, DARK_FRAME)

    # Glass panels: Leaf 1: cols 37..38, Leaf 2: cols 41..42, rows 10..21
    for y in range(10, 22):
        c.set(37, y, GLASS_MID)
        c.set(38, y, GLASS_DARK)
        c.set(41, y, GLASS_MID)
        c.set(42, y, GLASS_DARK)

    # Diagonal glass sheens
    c.set(37, 12, G_SHEEN_MED)
    c.set(38, 13, G_SHEEN_HI)
    c.set(37, 13, G_SHEEN_DIM)

    c.set(41, 14, G_SHEEN_MED)
    c.set(42, 15, G_SHEEN_HI)
    c.set(41, 15, G_SHEEN_DIM)

    # Yellow vertical safety grab pole inside rear door (in right leaf near partition)
    for y in range(13, 19):
        c.set(42, y, INT_POLE)

    # Waist handles
    c.set(38, 16, INT_HANDLE)
    c.set(41, 16, INT_HANDLE)

    # Door bottom kick plates
    for x in [37, 38, 41, 42]:
        c.set(x, 22, CYAN_DARK)
        c.set(x, 23, BUMPER_MED)

    # ------------------ 9. REAR WINDOWS (x=44..55) ------------------
    # Window over rear wheel (x=44..51, y=9..17)
    for y in range(9, 18):
        c.set(44, y, DARK_FRAME)
        c.set(48, y, DARK_FRAME)
        c.set(51, y, DARK_FRAME)
        for x in list(range(45, 48)) + list(range(49, 51)):
            c.set(x, y, GLASS_MID)

    c.line(45, 9, 50, 9, CEIL_GLOW)
    c.set(48, 9, DARK_FRAME)

    for x in [46, 47, 49, 50]:
        c.set(x, 15, INT_SEAT)
        c.set(x, 16, INT_SEAT)
        c.set(x, 17, INT_SEAT)

    c.set(46, 12, G_SHEEN_MED)
    c.set(47, 13, G_SHEEN_HI)
    c.set(49, 12, G_SHEEN_MED)
    c.set(50, 13, G_SHEEN_HI)

    # Rear quarter window (x=52..55, y=9..17)
    for y in range(9, 18):
        c.set(55, y, DARK_FRAME)
        for x in range(52, 55):
            c.set(x, y, GLASS_MID)

    for x in range(52, 55):
        c.set(x, 15, INT_SEAT)
        c.set(x, 16, INT_SEAT)
        c.set(x, 17, INT_SEAT)

    c.set(53, 12, G_SHEEN_MED)
    c.set(54, 13, G_SHEEN_HI)

    # ------------------ 10. REAR ENGINE SECTION & TAILLIGHTS (x=56..60) ------------------
    # Rear body panels
    for y in range(8, 24):
        c.set(56, y, W_BODY if y < 20 else (CYAN_MID if y in [21, 22] else SKIRT_GREY))
        c.set(57, y, W_BODY if y < 20 else (CYAN_MID if y in [21, 22] else SKIRT_GREY))
        c.set(58, y, W_MID if y < 20 else (CYAN_DARK if y in [21, 22] else BUMPER_MED))

    # Engine cooling louvers (radiator air intake)
    for vy in [11, 13, 15, 17]:
        c.set(56, vy, BUMPER_MED)
        c.set(57, vy, VENT_SLOT)

    # Rear amber marker light
    c.set(57, 21, LIGHT_AMBER)

    # Rear end vertical structure & modern LED taillights (x=59..60)
    for y in range(8, 14):
        c.set(59, y, W_SHADOW)
        c.set(60, y, W_MID)

    # Modern vertical LED taillight bar:
    c.set(59, 14, DARK_FRAME)
    c.set(60, 14, DARK_FRAME)

    c.set(59, 15, LIGHT_RED_HI)   # Bright LED brake light
    c.set(60, 15, LIGHT_RED)

    c.set(59, 16, LIGHT_RED_HI)
    c.set(60, 16, LIGHT_RED)

    c.set(59, 17, LIGHT_RED_DK)
    c.set(60, 17, LIGHT_RED_DK)

    c.set(59, 18, LIGHT_AMBER)    # Amber turn indicator
    c.set(60, 18, LIGHT_AMBER)

    c.set(59, 19, LIGHT_WHITE)    # White reverse lamp
    c.set(60, 19, LIGHT_WHITE)

    c.set(59, 20, LIGHT_RED_DK)   # Lower red reflector
    c.set(60, 20, LIGHT_RED_DK)

    # Rear bumper
    c.set(59, 21, BUMPER_MED)
    c.set(60, 21, BUMPER_MED)
    c.set(59, 22, BUMPER_MED)
    c.set(60, 22, BUMPER_MED)
    c.set(59, 23, DARK_FRAME)
    c.set(60, 23, DARK_FRAME)

    return c

c = build_bus()
view(c)
finish(c)
print("Stats:", c.stats())
