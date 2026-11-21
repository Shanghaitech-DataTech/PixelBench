import random
from pixelbench_api import *

def draw_scene():
    c = new_canvas(64, 64)

    # -------------------------------------------------------------------------
    # 1. PALETTE (Strictly Opaque Hex - Zero Alpha - Perfectly Harmonious)
    # -------------------------------------------------------------------------
    # Sky & Stormy Night
    C_SKY_DEEP    = '#090c16'
    C_SKY_MID     = '#111524'
    C_SKY_LOW     = '#1a2035'
    C_WIRE        = '#28314a'

    # Upper Building Facade
    C_BLDG_DARK   = '#151825'
    C_BLDG_MID    = '#202436'
    C_BLDG_LIGHT  = '#2f364f'
    C_BLDG_TRIM   = '#3f4766'

    # Store Signboard & Awning
    C_SIGN_BG     = '#fffdf5'
    C_SIGN_FRAME  = '#222638'
    C_SIGN_ORANGE = '#ea580c'
    C_SIGN_GREEN  = '#10b981'
    C_SIGN_TEXT   = '#334155'
    C_AWNING_TOP  = '#191c2b'
    C_AWNING_EDGE = '#383e54'
    C_AWNING_GLOW = '#4a473b'

    # Window Frames & Sills
    C_FRAME_DARK  = '#181c2b'
    C_FRAME_MID   = '#282f44'
    C_FRAME_HI    = '#515e80'
    C_SILL_BODY   = '#222738'

    # Store Interior Glow
    C_INT_WHITE   = '#ffffff'
    C_INT_CREAM   = '#fffde8'
    C_INT_WARM    = '#fef08a'
    C_INT_GOLD    = '#fde047'
    C_INT_AMBER   = '#f59e0b'
    C_INT_WALL    = '#fef3c7'
    C_INT_FLOOR   = '#fde68a'
    C_INT_TILE    = '#facc15'

    # Interior Goods
    C_COOLER_BG   = '#0f172a'
    C_COOLER_CYAN = '#e0f2fe'
    C_COOLER_NEON = '#38bdf8'
    C_WOOD_SHELF  = '#d97706'
    C_ITEM_RED    = '#ef4444'
    C_ITEM_GREEN  = '#22c55e'
    C_ITEM_BLUE   = '#3b82f6'
    C_ITEM_PINK   = '#f472b6'
    C_ITEM_ORANGE = '#f97316'
    C_ITEM_WHITE  = '#ffffff'

    # Person in Raincoat (Luminous Yellow Raincoat)
    C_COAT_RIM    = '#fffde8'
    C_COAT_BRIGHT = '#facc15'
    C_COAT_MID    = '#eab308'
    C_COAT_WARM   = '#ca8a04'
    C_COAT_SHADOW = '#92400e'
    C_COAT_DEEP   = '#5c2c06'
    C_SKIN        = '#fed7aa'
    C_PANTS       = '#0f172a'
    C_BOOT        = '#1e293b'
    C_BOOT_HI     = '#475569'

    # Umbrella Rack & Umbrellas
    C_RACK_METAL  = '#94a3b8'
    C_RACK_SHADOW = '#475569'
    C_RACK_BASE   = '#1e293b'
    C_UMB_CLEAR   = '#e2e8f0'
    C_UMB_BLUE    = '#1d4ed8'
    C_UMB_RED     = '#dc2626'

    # Bicycle (Mamachari)
    C_BIKE_TIRE   = '#090d16'
    C_BIKE_RIM    = '#334155'
    C_BIKE_SPOKE  = '#64748b'
    C_BIKE_SILVER = '#cbd5e1'
    C_BIKE_BLUE   = '#0284c7'
    C_BIKE_CYAN   = '#38bdf8'

    # Sidewalk & Street
    C_CURB_FACE   = '#22283a'
    C_CURB_TOP    = '#3f4864'
    C_CURB_HI     = '#5a678c'
    C_ROAD_DEEP   = '#0b0e17'
    C_ROAD_MID    = '#131726'
    C_ROAD_WET    = '#1c2338'

    # Reflections in Puddles
    C_REFL_WHITE  = '#fffde8'
    C_REFL_WARM   = '#fef08a'
    C_REFL_AMBER  = '#f59e0b'
    C_REFL_DARK   = '#78350f'
    C_REFL_CYAN   = '#38bdf8'
    C_REFL_BLUE   = '#0284c7'

    # Rain & Splashes
    C_RAIN_DARK   = '#38435c'
    C_RAIN_MID    = '#5b6c8f'
    C_RAIN_LIGHT  = '#cbd5e1'
    C_SPLASH      = '#e2e8f0'

    # Initialize canvas background fully opaque
    c.rect(0, 0, 64, 64, C_SKY_DEEP)

    # -------------------------------------------------------------------------
    # 2. SKY & 2ND FLOOR FACADE (y = 0 to 14)
    # -------------------------------------------------------------------------
    for y in range(0, 15):
        col = C_SKY_DEEP if y < 4 else (C_SKY_MID if y < 9 else C_SKY_LOW)
        c.line(0, y, 63, y, col)

    # Wires
    c.line(0, 1, 63, 6, C_WIRE)
    c.line(0, 4, 63, 10, C_WIRE)
    c.line(12, 0, 63, 13, '#1d2334')

    # Upper building facade
    c.rect(2, 3, 60, 12, C_BLDG_MID)
    c.line(2, 3, 61, 3, C_BLDG_TRIM)
    for gy in [6, 9, 12]:
        c.line(2, gy, 61, gy, C_BLDG_DARK)

    # Left window
    c.rect(8, 5, 14, 7, C_BLDG_DARK)
    c.rect(9, 6, 12, 5, '#0c0f1a')
    c.line(9, 8, 20, 8, '#161a29')
    c.line(9, 10, 20, 10, '#161a29')
    c.line(15, 6, 15, 10, C_BLDG_MID)

    # AC compressor
    c.rect(26, 6, 9, 6, '#282d3f')
    c.rect(27, 7, 7, 4, '#171a26')
    c.line(28, 8, 30, 8, C_BLDG_TRIM)
    c.line(28, 9, 30, 9, C_BLDG_TRIM)
    c.circle(32, 9, 1, C_BLDG_TRIM, fill=False)

    # Right window (warm blinds)
    c.rect(39, 5, 14, 7, C_BLDG_DARK)
    c.rect(40, 6, 12, 5, '#281d18')
    c.rect(42, 7, 8, 4, '#4d3725')
    c.line(44, 7, 48, 10, '#735235')
    c.line(46, 6, 46, 10, '#261c17')

    # -------------------------------------------------------------------------
    # 3. STORE SIGNBOARD & AWNING (y = 15 to 23)
    # -------------------------------------------------------------------------
    c.rect(2, 14, 60, 10, C_SIGN_FRAME)
    c.rect(4, 15, 56, 6, C_SIGN_BG)
    c.rect(4, 15, 56, 1, C_SIGN_ORANGE)
    c.rect(4, 20, 56, 1, C_SIGN_GREEN)

    # Logo emblem
    c.poly([(10, 18), (12, 16), (14, 18), (12, 20)], C_SIGN_ORANGE)
    c.poly([(13, 18), (15, 16), (17, 18), (15, 20)], C_SIGN_GREEN)
    c.set(13, 18, C_INT_WHITE)

    # Lettering glyphs
    letter_glyphs = [
        [(21, 17), (21, 18), (21, 19), (22, 17), (23, 17), (23, 18), (23, 19)],
        [(25, 17), (25, 18), (25, 19), (26, 17), (27, 18), (27, 19)],
        [(29, 17), (29, 18), (29, 19), (30, 18), (31, 17), (31, 18), (31, 19)],
        [(33, 17), (33, 18), (33, 19), (34, 17), (35, 17), (35, 18), (35, 19)],
        [(38, 17), (38, 18), (38, 19), (39, 18)],
        [(41, 17), (41, 18), (41, 19), (42, 17), (43, 18), (43, 19)],
        [(48, 17), (48, 18), (49, 19), (50, 19), (50, 18), (50, 17)],
        [(52, 17), (52, 18), (53, 18), (54, 17), (54, 18), (54, 19)]
    ]
    for glyph in letter_glyphs:
        for (gx, gy) in glyph:
            c.set(gx, gy, C_SIGN_TEXT)

    # Awning
    c.rect(1, 21, 62, 2, C_AWNING_TOP)
    c.line(0, 23, 63, 23, C_AWNING_EDGE)
    c.line(4, 23, 59, 23, C_AWNING_GLOW)

    # -------------------------------------------------------------------------
    # 4. STORE INTERIOR (y = 24 to 47) - Radiant Warmth & Vivid Details
    # -------------------------------------------------------------------------
    c.rect(3, 24, 58, 24, C_INT_CREAM)
    c.rect(4, 24, 56, 2, C_INT_WHITE)
    c.line(4, 26, 59, 26, C_INT_WARM)

    # --- LEFT: Drinks Refrigerator (x=5 to 19, y=26 to 43) ---
    c.rect(5, 26, 15, 17, C_COOLER_BG)
    c.rect(6, 27, 13, 15, C_COOLER_CYAN)
    for sy in [31, 36, 41]:
        c.line(6, sy, 18, sy, C_COOLER_NEON)
    drinks_r1 = [C_ITEM_RED, C_ITEM_GREEN, C_ITEM_BLUE, C_ITEM_ORANGE, C_ITEM_RED, C_ITEM_WHITE]
    for i, col in enumerate(drinks_r1):
        c.rect(7 + i*2, 28, 1, 3, col)
    drinks_r2 = [C_ITEM_BLUE, C_ITEM_PINK, C_ITEM_WHITE, C_ITEM_GREEN, C_ITEM_ORANGE, C_ITEM_BLUE]
    for i, col in enumerate(drinks_r2):
        c.rect(7 + i*2, 33, 1, 3, col)
    drinks_r3 = [C_ITEM_GREEN, C_ITEM_RED, C_ITEM_PINK, C_ITEM_WHITE, C_ITEM_GREEN, C_ITEM_ORANGE]
    for i, col in enumerate(drinks_r3):
        c.rect(7 + i*2, 38, 1, 3, col)
    c.line(9, 27, 6, 30, C_INT_WHITE)
    c.line(16, 27, 13, 30, C_INT_WHITE)

    # --- MIDDLE: Shelves (x=21 to 35, y=27 to 43) ---
    c.rect(21, 27, 15, 16, C_INT_WALL)
    for sy in [32, 37, 42]:
        c.line(21, sy, 35, sy, C_WOOD_SHELF)
    c.rect(22, 29, 2, 3, C_ITEM_RED)
    c.rect(25, 29, 2, 3, C_ITEM_GREEN)
    c.rect(28, 29, 2, 3, C_ITEM_BLUE)
    c.rect(31, 29, 2, 3, C_ITEM_ORANGE)
    c.rect(34, 29, 1, 3, C_ITEM_WHITE)

    c.rect(22, 34, 3, 3, '#fed7aa')
    c.rect(26, 34, 3, 3, C_ITEM_PINK)
    c.rect(30, 34, 2, 3, '#bbf7d0')
    c.rect(33, 34, 2, 3, C_ITEM_RED)

    c.rect(22, 39, 2, 3, C_ITEM_GREEN)
    c.rect(25, 39, 2, 3, C_WOOD_SHELF)
    c.rect(28, 39, 2, 3, C_ITEM_RED)
    c.rect(31, 39, 2, 3, C_ITEM_WHITE)
    c.rect(34, 39, 1, 3, C_ITEM_BLUE)

    # --- RIGHT: Checkout Counter & Register (x=49 to 58, y=28 to 44) ---
    c.rect(50, 34, 8, 10, '#e2e8f0')
    c.line(49, 34, 58, 34, C_RACK_METAL)
    c.rect(52, 29, 4, 5, '#334155')
    c.rect(53, 30, 2, 2, C_COOLER_NEON)
    c.set(55, 33, C_ITEM_GREEN)
    c.rect(52, 26, 4, 2, C_ITEM_RED)
    # Clerk silhouette
    c.rect(55, 31, 2, 3, '#475569')
    c.rect(54, 34, 4, 3, '#334155')

    # Floor tiles
    for fy in range(41, 46):
        c.line(4, fy, 58, fy, C_INT_FLOOR if fy % 2 == 0 else C_INT_TILE)

    # -------------------------------------------------------------------------
    # 5. WALLS, FRAMES & ENTRANCE THRESHOLD
    # -------------------------------------------------------------------------
    # Outer pillars
    c.rect(0, 14, 4, 34, '#161926')
    c.line(3, 14, 3, 47, C_BLDG_MID)
    c.rect(59, 14, 5, 34, '#161926')
    c.line(59, 14, 59, 47, C_BLDG_MID)

    # Base kickplate wall under windows (y=44 to 47)
    c.rect(4, 44, 33, 4, C_SILL_BODY)
    c.line(4, 44, 36, 44, C_FRAME_HI)
    c.line(4, 47, 36, 47, C_FRAME_DARK)

    c.rect(53, 44, 6, 4, C_SILL_BODY)
    c.line(53, 44, 58, 44, C_FRAME_HI)
    c.line(53, 47, 58, 47, C_FRAME_DARK)

    # Window Mullions
    c.rect(4, 23, 1, 21, C_FRAME_MID)
    c.rect(20, 24, 1, 20, C_FRAME_MID)
    c.set(20, 24, C_FRAME_HI)

    # Sliding door frame posts
    c.rect(37, 23, 1, 25, C_FRAME_HI)
    c.rect(52, 23, 1, 25, C_FRAME_HI)
    c.rect(58, 23, 1, 21, C_FRAME_MID)

    # Door header & sensor
    c.rect(37, 23, 16, 2, '#2d3345')
    c.line(38, 23, 51, 23, '#4d5570')
    c.set(45, 24, C_ITEM_GREEN)

    # Sliding door glass panel (slid open to right behind x=48..52)
    c.line(48, 25, 48, 45, C_BIKE_SILVER)

    # Threshold & Entrance Welcome Mat (filling y=45..47)
    c.rect(37, 45, 16, 3, '#1c1f2e')
    c.line(38, 45, 51, 45, C_FRAME_DARK)
    c.rect(39, 46, 12, 2, '#78350f')
    c.line(40, 46, 49, 46, '#92400e')

    # Recycling bins outside far right
    c.rect(59, 42, 2, 5, '#1e3a5f')
    c.set(59, 42, C_COOLER_NEON)
    c.rect(61, 42, 2, 5, '#14532d')
    c.set(61, 42, C_ITEM_GREEN)

    # -------------------------------------------------------------------------
    # 6. UMBRELLA RACK OUTSIDE (x=30 to 36, y=38 to 47)
    # -------------------------------------------------------------------------
    # Realistic compact wire stand standing beside door
    c.rect(30, 39, 7, 8, '#1b2030') # dark interior shadow
    # Stainless steel wire frame
    c.rect(30, 39, 7, 8, C_RACK_SHADOW, fill=False)
    c.line(30, 39, 36, 39, C_RACK_METAL) # top silver rim
    c.line(30, 43, 36, 43, C_RACK_SHADOW) # middle wire ring
    c.line(30, 46, 36, 46, C_RACK_METAL) # bottom tray rim
    c.rect(30, 46, 7, 2, C_RACK_BASE) # drip tray
    # Vertical grid wires
    c.line(32, 40, 32, 45, C_RACK_SHADOW)
    c.line(34, 40, 34, 45, C_RACK_SHADOW)

    # Umbrellas neatly placed & slanted inside rack:
    # 1. Clear vinyl umbrella (iconic Japanese konbini umbrella!)
    # Slanted from handle (31, 36) to tip (33, 46)
    c.line(31, 37, 33, 45, C_UMB_CLEAR)
    c.line(32, 38, 33, 44, C_INT_WHITE) # vinyl light sheen
    c.set(31, 36, C_RACK_METAL) # white J-hook handle
    c.set(30, 36, C_RACK_METAL)

    # 2. Navy blue umbrella
    # Slanted from handle (33, 35) to tip (35, 46)
    c.line(33, 36, 35, 45, C_UMB_BLUE)
    c.set(33, 35, '#0f172a') # black hook handle
    c.set(34, 35, '#0f172a')

    # 3. Small red folded umbrella
    c.line(35, 38, 36, 45, C_UMB_RED)
    c.set(35, 37, C_ITEM_RED)

    # -------------------------------------------------------------------------
    # 7. PARKED BICYCLE (MAMACHARI) (x=7 to 29, y=36 to 48)
    # -------------------------------------------------------------------------
    # Rear wheel (center x=11, y=44, r=4)
    c.circle(11, 44, 4, C_BIKE_TIRE, fill=False)
    c.circle(11, 44, 3, C_BIKE_RIM, fill=False)
    c.set(11, 44, C_RACK_METAL) # hub
    # Silver mudguard arc over rear wheel
    c.line(8, 41, 14, 41, C_BIKE_SILVER)
    c.set(7, 42, C_BIKE_SILVER)
    c.set(15, 42, C_BIKE_SILVER)
    # Spokes:
    c.set(11, 41, C_BIKE_SPOKE)
    c.set(11, 47, C_BIKE_SPOKE)
    c.set(8, 44, C_BIKE_SPOKE)
    c.set(14, 44, C_BIKE_SPOKE)

    # Front wheel (center x=25, y=44, r=4)
    c.circle(25, 44, 4, C_BIKE_TIRE, fill=False)
    c.circle(25, 44, 3, C_BIKE_RIM, fill=False)
    c.set(25, 44, C_RACK_METAL) # hub
    # Silver mudguard arc over front wheel
    c.line(22, 41, 28, 41, C_BIKE_SILVER)
    c.set(21, 42, C_BIKE_SILVER)
    c.set(29, 43, C_BIKE_SILVER)
    # Spokes:
    c.set(25, 41, C_BIKE_SPOKE)
    c.set(25, 47, C_BIKE_SPOKE)
    c.set(22, 44, C_BIKE_SPOKE)
    c.set(28, 44, C_BIKE_SPOKE)

    # Blue step-through Mamachari frame:
    c.line(25, 44, 23, 37, C_BIKE_BLUE) # fork
    c.line(23, 37, 23, 35, C_BIKE_CYAN) # headtube
    c.line(23, 37, 20, 41, C_BIKE_BLUE) # swooping down-tube
    c.line(20, 41, 17, 44, C_BIKE_BLUE)
    c.set(21, 39, C_BIKE_CYAN)
    c.line(17, 44, 15, 38, C_BIKE_BLUE) # seat tube
    c.line(15, 38, 11, 44, C_BIKE_BLUE) # seat stay
    c.line(17, 44, 11, 44, C_BIKE_RIM)  # chainstay

    # Saddle
    c.line(13, 37, 16, 37, '#0f172a')
    c.set(14, 36, '#1e293b')
    c.set(15, 36, '#334155')

    # Rear luggage rack
    c.line(10, 39, 15, 39, C_BIKE_SILVER)
    c.line(10, 39, 11, 44, C_BIKE_RIM)

    # Handlebars & Stem
    c.line(23, 35, 23, 33, C_BIKE_SILVER)
    c.line(21, 33, 25, 33, C_BIKE_SILVER)
    c.set(20, 34, '#0f172a')
    c.set(26, 34, '#0f172a')

    # Front wire basket (x=24 to 28, y=35 to 38)
    c.rect(24, 35, 5, 4, C_BIKE_RIM, fill=False)
    c.line(25, 36, 27, 36, C_BIKE_SPOKE)
    c.line(25, 37, 27, 37, C_BIKE_SPOKE)
    # Shopping bag in basket
    c.rect(25, 36, 2, 2, C_INT_CREAM)
    c.set(26, 35, C_ITEM_RED)

    # Kickstand resting on sidewalk
    c.line(17, 44, 16, 48, C_BIKE_RIM)

    # -------------------------------------------------------------------------
    # 8. PERSON IN RAINCOAT ENTERING (x=41 to 48, y=30 to 47)
    # -------------------------------------------------------------------------
    # Naturally proportioned walking silhouette, luminous yellow raincoat!
    # Hood:
    c.set(44, 30, C_COAT_RIM)
    c.line(43, 31, 45, 31, C_COAT_RIM)
    c.rect(42, 32, 5, 3, C_COAT_MID)
    c.set(42, 32, C_COAT_BRIGHT)
    c.set(42, 33, C_COAT_BRIGHT)
    c.set(46, 32, C_COAT_RIM)
    c.set(46, 33, C_COAT_RIM)
    c.set(43, 33, C_COAT_WARM)
    c.set(44, 33, C_COAT_WARM)
    c.line(43, 34, 45, 34, C_COAT_SHADOW)

    # Raincoat Torso & Flared Coat:
    c.rect(42, 35, 5, 2, C_COAT_BRIGHT)
    c.rect(41, 37, 7, 3, C_COAT_MID)
    c.rect(41, 40, 7, 3, C_COAT_BRIGHT)
    # Right-side brilliant rim light (facing interior):
    c.line(47, 35, 47, 42, C_COAT_RIM)
    c.set(48, 38, C_COAT_RIM)
    c.set(48, 39, C_COAT_RIM)
    # Left edge rim light:
    c.line(41, 37, 41, 41, C_COAT_BRIGHT)
    # Natural vertical fold shading on back:
    c.line(44, 35, 44, 41, C_COAT_SHADOW)
    c.line(43, 37, 43, 41, C_COAT_WARM)
    c.set(45, 38, C_COAT_WARM)
    c.set(45, 39, C_COAT_WARM)
    c.line(42, 42, 46, 42, C_COAT_WARM)

    # Left arm: hanging naturally close along body side
    c.line(41, 36, 40, 40, C_COAT_MID)
    c.set(40, 40, C_COAT_BRIGHT)
    c.set(40, 41, C_SKIN) # hand holding umbrella
    # Folded wet clear vinyl umbrella hanging tip-down:
    c.set(39, 41, C_RACK_METAL) # J-handle
    c.line(40, 42, 38, 46, C_UMB_CLEAR)
    c.line(39, 43, 38, 46, C_COOLER_NEON) # wet blue light reflection
    c.set(38, 47, '#1e293b') # umbrella tip
    c.set(38, 48, C_COOLER_NEON) # water droplet dripping onto ground!

    # Right arm: swung naturally forward entering door
    c.line(46, 36, 47, 39, C_COAT_MID)

    # Legs & Boots in walking stride:
    # Left foot forward stepping on mat:
    c.rect(42, 43, 2, 2, C_PANTS)
    c.rect(42, 45, 2, 2, C_BOOT)
    c.set(42, 45, C_BOOT_HI)

    # Right foot trailing behind:
    c.rect(45, 43, 2, 2, C_PANTS)
    c.rect(45, 45, 2, 2, C_BOOT)
    c.set(46, 45, C_BOOT_HI)

    # -------------------------------------------------------------------------
    # 9. SIDEWALK, STREET & REFLECTIVE PUDDLES (y = 48 to 63)
    # -------------------------------------------------------------------------
    # Sidewalk curb
    c.line(0, 48, 63, 48, C_CURB_FACE)
    c.line(0, 49, 63, 49, C_CURB_TOP)
    c.line(0, 50, 63, 50, C_CURB_HI)

    # Wet asphalt roadway
    for y in range(51, 64):
        col = C_ROAD_DEEP if y % 2 == 0 else C_ROAD_MID
        c.line(0, y, 63, y, col)

    # Wet puddle base areas
    for y in range(51, 64):
        for x in range(6, 62):
            if ((x - 20)**2 / 160 + (y - 56)**2 / 20 < 1.0) or \
               ((x - 46)**2 / 180 + (y - 57)**2 / 25 < 1.0):
                if (x + y) % 3 != 0:
                    c.set(x, y, C_ROAD_WET)

    # --- PUDDLE REFLECTIONS ---
    # 1. Warm Doorway Reflection
    refl_data = [
        (51, 40, 49, C_REFL_WHITE, C_REFL_WARM),
        (52, 39, 50, C_REFL_WARM,  C_REFL_AMBER),
        (53, 38, 51, C_REFL_WHITE, C_REFL_WARM),
        (54, 38, 52, C_REFL_AMBER, C_REFL_DARK),
        (55, 37, 53, C_REFL_WARM,  C_REFL_AMBER),
        (56, 36, 54, C_REFL_AMBER, C_REFL_DARK),
        (57, 36, 54, C_REFL_WHITE, C_REFL_WARM),
        (58, 35, 55, C_REFL_AMBER, C_REFL_DARK),
        (59, 36, 54, C_REFL_WARM,  C_REFL_DARK),
        (60, 37, 53, C_REFL_DARK,  C_ROAD_WET),
        (61, 38, 52, C_REFL_AMBER, C_REFL_DARK),
        (62, 39, 51, C_REFL_DARK,  C_ROAD_WET),
        (63, 40, 50, C_REFL_DARK,  C_ROAD_DEEP),
    ]
    for (ry, rx0, rx1, col1, col2) in refl_data:
        for rx in range(rx0, rx1 + 1):
            if (rx + ry * 2) % 4 == 0:
                continue
            dist = abs(rx - 45)
            if dist <= 3:
                c.set(rx, ry, col1 if (rx % 2 == 0) else col2)
            elif dist <= 6:
                c.set(rx, ry, col2 if (rx % 2 == 0) else C_REFL_DARK)
            else:
                if (rx + ry) % 2 == 0:
                    c.set(rx, ry, C_REFL_DARK)

    # 2. Reflected Silhouette of Raincoat in Puddle:
    c.line(43, 51, 45, 51, '#5c2c06')
    c.line(43, 52, 45, 52, '#78350f')
    c.line(44, 53, 45, 53, '#92400e')
    c.line(44, 54, 44, 55, '#5c2c06')

    # 3. Cooler cyan & shelf reflections on left:
    for ry in [52, 54, 55, 57, 59]:
        for rx in range(11, 18):
            if (rx + ry) % 2 == 0:
                c.set(rx, ry, C_REFL_BLUE if (rx % 3 != 0) else C_REFL_CYAN)
    for ry in [53, 54, 56, 58, 60]:
        for rx in range(22, 30):
            if (rx + ry * 3) % 3 != 0:
                c.set(rx, ry, C_REFL_AMBER if (rx % 2 == 0) else C_REFL_DARK)

    # 4. Bicycle reflections:
    c.line(11, 51, 11, 53, C_BIKE_TIRE)
    c.line(25, 51, 25, 53, C_BIKE_TIRE)
    c.set(16, 51, C_REFL_BLUE)
    c.set(17, 52, '#0c4a6e')

    # 5. Concentric ripples with splash droplets:
    c.ellipse(28, 55, 4, 1, C_BLDG_TRIM, fill=False)
    c.set(28, 55, C_SPLASH)

    c.ellipse(48, 58, 5, 2, C_REFL_AMBER, fill=False)
    c.set(48, 58, C_REFL_WHITE)
    c.set(48, 57, C_SPLASH)

    c.ellipse(15, 54, 3, 1, C_REFL_BLUE, fill=False)
    c.set(15, 54, C_REFL_CYAN)

    c.ellipse(38, 61, 4, 1, C_REFL_AMBER, fill=False)
    c.set(38, 61, C_REFL_WARM)

    c.ellipse(55, 53, 3, 1, C_BLDG_TRIM, fill=False)

    # -------------------------------------------------------------------------
    # 10. RAIN STREAKS & SPLASHES
    # -------------------------------------------------------------------------
    rng = random.Random(1337)
    streaks = []
    for _ in range(54):
        sx = rng.randint(1, 68)
        sy = rng.randint(-5, 55)
        length = rng.randint(2, 4)
        streaks.append((sx, sy, length))

    for (sx, sy, length) in streaks:
        for step in range(length):
            px = sx - step
            py = sy + step * 3
            if 0 <= px < 64 and 0 <= py < 64:
                # Keep person clean
                if 30 <= py <= 46 and 40 <= px <= 48:
                    continue
                # Over bright interior windows
                if 24 <= py <= 44 and 5 <= px <= 57:
                    if step == 0:
                        c.set(px, py, C_INT_WHITE)
                # Over dark night sky & upper building
                elif py < 24 or px < 4 or px > 58:
                    c.set(px, py, C_RAIN_MID if step == 0 else C_RAIN_DARK)
                # Over street & puddles
                else:
                    if 35 <= px <= 55:
                        c.set(px, py, C_REFL_WHITE if step == 0 else C_RAIN_LIGHT)
                    else:
                        c.set(px, py, C_RAIN_MID if step == 0 else C_RAIN_DARK)

    # Awning rim splashes & drips
    for ax in [8, 16, 24, 32, 40, 47, 54]:
        c.set(ax, 23, C_SPLASH)
        c.set(ax - 1, 22, C_RAIN_LIGHT)
        c.set(ax, 24, C_RAIN_LIGHT)
        c.set(ax, 25, C_RAIN_DARK)

    # Splashes on bike
    c.set(26, 33, C_SPLASH)
    c.set(24, 34, C_SPLASH)

    return c

c = draw_scene()
view(c)
print(c.stats_text())
finish(c)
