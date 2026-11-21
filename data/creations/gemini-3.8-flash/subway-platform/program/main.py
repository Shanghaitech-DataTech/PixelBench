from pixelbench_api import *

def draw_subway():
    c = new_canvas(64, 64, background="#090b10", name="subway")

    # ========================================================
    # 1. CURATED PALETTE (Harmonious, strictly < 75 colors)
    # ========================================================
    C_BLACK        = "#090b10"
    C_TUNNEL_BG    = "#10131c"
    C_TUNNEL_PIPE  = "#181f2c"
    C_CEIL_SLAB    = "#181c26"
    C_CEIL_BEAM    = "#222736"
    C_CEIL_HI      = "#2f364a"
    C_WHITE        = "#ffffff"
    C_PALE_GLOW    = "#dce4ed"

    # Headlight Beam in Tunnel & Bay 1 (Luminous progression)
    C_BEAM_FAINT   = "#1f2a3a"
    C_BEAM_MID     = "#31435c"
    C_BEAM_BRIGHT  = "#4a6385"
    C_BEAM_HOT     = "#6d8eb5"
    C_BEAM_CORE    = "#a2c2e2"

    # Train Metal Body
    C_TR_METAL_HI  = "#b0bec5"
    C_TR_METAL_MID = "#78909c"
    C_TR_METAL_LOW = "#455a64"
    C_TR_METAL_DRK = "#263238"
    C_TR_WINDSHIELD= "#131c22"
    C_TR_GLASS_REFL= "#1e323e"
    C_TR_CONSOLE   = "#00cec9"

    # Train Stripe & Neon Cyan Accent
    C_CYAN_HI      = "#81ecec"
    C_CYAN_MID     = "#00cec9"
    C_CYAN_DRK     = "#008b8b"

    # Train Windows & Speed Blur (Warm)
    C_WIN_WHITE    = "#ffffff"
    C_WIN_HOT      = "#fff3b0"
    C_WIN_GOLD     = "#feca57"
    C_WIN_AMBER    = "#e67e22"
    C_WIN_DARK     = "#8c3b12"
    C_WIN_SMR      = "#b35400"

    # Platform Screen Doors (PSD)
    C_PSD_FRAME    = "#1a1e28"
    C_PSD_METAL    = "#282e3c"
    C_PSD_HI       = "#384052"
    C_PSD_FROST    = "#475d78"
    C_PSD_SHEEN    = "#28374a"
    C_LED_GREEN    = "#2ed573"

    # Signs
    C_SIGN_BG      = "#0c0e14"
    C_SIGN_BORDER  = "#282e3c"
    C_SIGN_TXT     = "#d1d8e0"
    C_SIGN_DIM     = "#778ca3"
    C_LED_AMBER    = "#ff9f43"
    C_LED_AMBER_D  = "#7d4814"

    # Tactile Paving & Platform Floor
    C_TACTILE_HI   = "#f1c40f"
    C_TACTILE_MID  = "#b7950b"
    C_TACTILE_DRK  = "#725c04"
    C_FLOOR_LINE   = "#0b0d12"
    C_FLOOR_BASE   = "#1f2430"
    C_FLOOR_TILE   = "#282e3e"
    C_FLOOR_HI     = "#353c50"
    C_FLOOR_REFL_W = "#4c5440"
    C_FLOOR_REFL_Y = "#484232"
    C_FLOOR_REFL_C = "#1e3846"

    # Bench
    C_WOOD_HI      = "#cd853f"
    C_WOOD_MID     = "#a0522d"
    C_WOOD_DRK     = "#6e3518"
    C_BENCH_FRAME  = "#262a36"
    C_BENCH_HI     = "#485064"

    # Passenger 1 (Left - Coat in wind)
    C_P1_HAIR      = "#1c140e"
    C_P1_SKIN      = "#e0a98b"
    C_P1_SKIN_HI   = "#f7d5c3"
    C_P1_SCARF     = "#eb4d4b"
    C_P1_SCARF_HI  = "#ff6b6b"
    C_P1_COAT_DRK  = "#0e1116"
    C_P1_COAT_MID  = "#181e28"
    C_P1_COAT_HI   = "#2e3a4c"
    C_P1_RIM       = "#8fa3be"
    C_P1_PANTS     = "#090b0e"

    # Passenger 2 (Center - Seated, phone)
    C_P2_HAIR      = "#11141c"
    C_P2_SKIN      = "#e0a98b"
    C_P2_SKIN_HI   = "#f7d5c3"
    C_P2_JACKET_D  = "#4a1828"
    C_P2_JACKET_M  = "#7a2842"
    C_P2_JACKET_HI = "#a83b5c"
    C_P2_JEANS_D   = "#223244"
    C_P2_JEANS_M   = "#344a62"

    # Passenger 3 (Right - Backpack, watch)
    C_P3_HAIR      = "#1c140e"
    C_P3_SKIN      = "#e0a98b"
    C_P3_HEADPHONE = "#778ca3"
    C_P3_JACKET_D  = "#8c5310"
    C_P3_JACKET_M  = "#c28522"
    C_P3_JACKET_HI = "#e5a83b"
    C_P3_PACK_D    = "#181c22"
    C_P3_PACK_M    = "#2e343c"
    C_P3_PANTS     = "#18202c"

    # ========================================================
    # 2. CEILING & INDUSTRIAL ARCHITECTURE (Y=0 to 13)
    # ========================================================
    c.rect(0, 0, 64, 13, C_CEIL_SLAB)

    # Overhead concrete beams
    for x in [0, 14, 28, 42, 56]:
        c.rect(x, 0, 3, 5, C_CEIL_BEAM)
        c.line(x, 0, x, 4, C_CEIL_HI)

    c.line(0, 4, 63, 4, C_CEIL_BEAM)

    # Fluorescent lighting tube across ceiling
    c.rect(3, 2, 58, 1, C_WHITE)
    c.line(1, 2, 2, 2, C_PALE_GLOW)
    c.line(61, 2, 62, 2, C_PALE_GLOW)
    c.line(3, 3, 60, 3, C_CEIL_HI)

    # ========================================================
    # 3. TUNNEL & LUMINOUS HEADLIGHT BEAM (Bay 1 to Train at X=24)
    # ========================================================
    c.rect(0, 13, 64, 31, C_TUNNEL_BG)

    # Tunnel conduits on left
    c.line(0, 19, 23, 19, C_TUNNEL_PIPE)
    c.line(0, 24, 23, 24, C_TUNNEL_PIPE)
    c.line(0, 28, 23, 28, C_TUNNEL_PIPE)

    # Luminous headlight beam cone shooting left from X=24 to X=0
    c.poly([(24, 35), (0, 23), (0, 44), (24, 40)], C_BEAM_FAINT, fill=True)
    c.poly([(24, 35), (0, 27), (0, 42), (24, 39)], C_BEAM_MID, fill=True)
    c.poly([(24, 35), (0, 30), (0, 40), (24, 38)], C_BEAM_BRIGHT, fill=True)
    c.poly([(24, 35), (0, 32), (0, 38), (24, 37)], C_BEAM_HOT, fill=True)
    c.poly([(24, 35), (0, 34), (0, 37), (24, 36)], C_BEAM_CORE, fill=True)

    # ========================================================
    # 4. ARRIVING TRAIN (Entering station from right, nose at X=24)
    # ========================================================
    # Train main body block (X=33 to 63, Y=17 to 42)
    c.rect(33, 17, 31, 26, C_TR_METAL_DRK)

    # Sleek aerodynamic train cab / nose (X=24 to 33, Y=17 to 42)
    c.poly([(33, 17), (29, 20), (26, 26), (24, 33), (24, 38), (28, 41), (33, 42)], C_TR_METAL_MID, fill=True)

    # Roof edge highlights
    c.line(33, 17, 63, 17, C_TR_METAL_HI)
    c.line(29, 20, 33, 18, C_TR_METAL_HI)
    c.line(26, 26, 29, 21, C_TR_METAL_HI)

    # Upper metallic panel
    c.rect(33, 18, 31, 3, C_TR_METAL_HI)
    c.rect(33, 21, 31, 2, C_TR_METAL_MID)

    # Front Windshield (curved dark tinted cockpit glass at X=26..32, Y=20..27)
    c.poly([(32, 20), (29, 22), (27, 27), (32, 27)], C_TR_WINDSHIELD, fill=True)
    c.line(31, 21, 28, 25, C_TR_GLASS_REFL)
    c.set(31, 26, C_TR_CONSOLE)

    # Destination display on roof above windshield ("EXP")
    c.rect(29, 19, 4, 1, C_LED_AMBER)

    # Electric Cyan Speed Stripe (running along nose and whole train body)
    c.line(24, 32, 32, 32, C_CYAN_MID)
    c.line(24, 33, 32, 33, C_CYAN_MID)
    c.rect(33, 32, 31, 2, C_CYAN_MID)
    c.line(27, 32, 63, 32, C_CYAN_HI)  # bright stripe highlight
    c.line(24, 34, 63, 34, C_CYAN_DRK) # lower shadow line

    # Lower body & undercarriage skirt
    c.rect(33, 35, 31, 5, C_TR_METAL_LOW)
    c.poly([(24, 35), (33, 35), (33, 41), (25, 41)], C_TR_METAL_LOW, fill=True)
    c.rect(33, 40, 31, 2, C_BLACK)
    c.line(25, 41, 33, 41, C_BLACK)

    # High-Intensity Headlights at front nose (X=24..25, Y=35..36)
    c.rect(24, 35, 2, 2, C_WHITE)
    c.set(23, 35, C_WIN_HOT)
    c.set(23, 36, C_WIN_HOT)

    # PASSENGER WINDOWS WITH STRONG MOTION BLUR (Speed Streaks!)
    # Cab side window:
    c.rect(30, 23, 3, 8, C_WIN_AMBER)
    c.rect(31, 24, 2, 6, C_WIN_GOLD)
    c.rect(32, 25, 1, 4, C_WIN_HOT)

    # Main passenger compartment: continuous motion blur streaks across X=34..63!
    c.rect(34, 23, 30, 8, C_WIN_AMBER)
    c.rect(35, 24, 29, 6, C_WIN_GOLD)
    c.rect(37, 25, 27, 4, C_WIN_HOT)
    c.line(39, 26, 63, 26, C_WIN_WHITE)
    c.line(42, 27, 63, 27, C_WIN_WHITE)

    # Motion-blurred vertical window pillars:
    for px in [43, 53]:
        c.rect(px, 23, 2, 8, C_WIN_DARK)
        c.rect(px+2, 23, 2, 8, C_WIN_SMR)
    c.rect(62, 23, 2, 8, C_WIN_DARK)

    # Blurred passenger silhouettes rushing past inside:
    c.line(36, 26, 39, 26, C_WIN_DARK)
    c.line(46, 26, 49, 26, C_WIN_DARK)
    c.line(56, 25, 59, 25, C_WIN_DARK)

    # High-speed horizontal motion streaks:
    c.line(28, 18, 52, 18, C_WHITE)
    c.line(38, 21, 61, 21, C_TR_METAL_HI)
    c.line(8, 22, 18, 22, C_PALE_GLOW)
    c.line(4, 27, 14, 27, C_BEAM_CORE)
    c.line(2, 38, 12, 38, C_PALE_GLOW)
    c.line(32, 36, 56, 36, C_TR_METAL_MID)
    c.line(42, 39, 63, 39, C_TR_METAL_LOW)

    # ========================================================
    # 5. PLATFORM SCREEN DOORS (PSD)
    # ========================================================
    # Top header beam (Y=13 to 16)
    c.rect(0, 13, 64, 4, C_PSD_FRAME)
    c.line(0, 13, 63, 13, C_PSD_HI)
    c.line(0, 14, 63, 14, C_PSD_METAL)
    c.line(0, 16, 63, 16, C_PSD_FRAME)

    # Door status indicator lights & door numbers on header
    # Door Bay 1 (X=2..20, center X=11):
    c.rect(10, 14, 2, 2, C_LED_GREEN)
    c.set(10, 14, C_WHITE)
    c.set(7, 14, C_PSD_HI)
    c.set(7, 15, C_PSD_HI)

    # Door Bay 2 (X=23..41, center X=32):
    c.rect(31, 14, 2, 2, C_LED_GREEN)
    c.set(31, 14, C_WHITE)
    c.set(27, 14, C_PSD_HI)
    c.set(27, 15, C_PSD_HI)

    # Door Bay 3 (X=44..61, center X=53):
    c.rect(52, 14, 2, 2, C_LED_GREEN)
    c.set(52, 14, C_WHITE)
    c.set(48, 14, C_PSD_HI)
    c.set(48, 15, C_PSD_HI)

    # Vertical Steel Mullions / Pillars (Y=16 to 44)
    for px in [0, 21, 42, 62]:
        c.rect(px, 16, 2, 29, C_PSD_FRAME)
        c.line(px, 16, px, 44, C_PSD_METAL)
        c.line(px+1, 16, px+1, 44, C_PSD_HI)

    # Sliding Door Meeting Seams
    c.line(11, 17, 11, 44, C_PSD_FRAME)
    c.line(32, 17, 32, 44, C_PSD_FRAME)
    c.line(53, 17, 53, 44, C_PSD_FRAME)

    # Subtle Frosted Safety Decals (clean modern dotted safety decal at Y=30)
    for bx in [(2, 20), (23, 41), (44, 61)]:
        for x in range(bx[0], bx[1]+1, 3):
            c.set(x, 30, C_PSD_FROST)

    # Subtle Glass Vertical Sheen
    for sx in [6, 16, 28, 38, 48, 58]:
        c.line(sx, 18, sx, 24, C_PSD_SHEEN)

    # ========================================================
    # 6. OVERHEAD STATION SIGNS (No brand names)
    # ========================================================
    # A. Hanging Station Sign (Center-Left: X=13..36, Y=5..11)
    c.line(17, 0, 17, 5, C_PSD_HI)
    c.line(32, 0, 32, 5, C_PSD_HI)

    c.rect(13, 5, 24, 7, C_SIGN_BG)
    c.rect(13, 5, 24, 7, C_SIGN_BORDER, fill=False)

    # Route color bar
    c.rect(14, 6, 22, 1, C_CYAN_MID)

    # Direction Arrow: ◄
    c.set(15, 8, C_WHITE)
    c.rect(16, 7, 1, 3, C_WHITE)
    c.rect(17, 8, 1, 1, C_WHITE)

    # Fictional station lettering glyphs: "LINE 2  PLATFORM 1"
    c.rect(19, 7, 3, 1, C_SIGN_TXT)
    c.rect(23, 7, 4, 1, C_SIGN_TXT)
    c.rect(28, 7, 3, 1, C_SIGN_TXT)
    c.rect(32, 7, 3, 1, C_SIGN_TXT)
    c.rect(19, 9, 6, 1, C_SIGN_DIM)
    c.rect(26, 9, 8, 1, C_SIGN_DIM)

    # B. Digital LED Arrival Board (Right: X=46..60, Y=5..11)
    c.line(48, 0, 48, 5, C_PSD_HI)
    c.line(58, 0, 58, 5, C_PSD_HI)

    c.rect(46, 5, 15, 7, C_SIGN_BG)
    c.rect(46, 5, 15, 7, C_SIGN_BORDER, fill=False)

    # Train icon:
    c.rect(48, 7, 3, 3, C_LED_AMBER)
    c.set(49, 8, C_SIGN_BG)
    c.set(48, 9, C_LED_AMBER_D)
    c.set(50, 9, C_LED_AMBER_D)

    # Chevrons indicating arrival: "◄◄"
    c.set(53, 8, C_LED_AMBER)
    c.set(54, 7, C_LED_AMBER)
    c.set(54, 9, C_LED_AMBER)

    c.set(56, 8, C_LED_AMBER)
    c.set(57, 7, C_LED_AMBER)
    c.set(57, 9, C_LED_AMBER)

    for x in range(48, 59, 2):
        c.set(x, 11, C_LED_AMBER)

    # ========================================================
    # 7. PLATFORM EDGE & POLISHED FLOOR (Y=44 to 63)
    # ========================================================
    # Door threshold slot (Y=44)
    c.rect(0, 44, 64, 1, C_FLOOR_LINE)

    # Tactile Warning Strip (Y=45 to 47)
    c.rect(0, 45, 64, 3, C_TACTILE_MID)
    for x in range(0, 64, 2):
        c.set(x, 45, C_TACTILE_HI)
        c.set(x+1, 45, C_TACTILE_MID)
        c.set(x+1, 46, C_TACTILE_HI)
        c.set(x, 46, C_TACTILE_DRK)
        c.set(x, 47, C_TACTILE_MID)
        c.set(x+1, 47, C_TACTILE_DRK)

    # Safety boundary line
    c.line(0, 48, 63, 48, C_FLOOR_LINE)

    # Polished Platform Tiles (Y=49 to 63)
    c.rect(0, 49, 64, 15, C_FLOOR_BASE)

    # Horizontal tile joints: Y=53, Y=58
    c.line(0, 53, 63, 53, C_FLOOR_LINE)
    c.line(0, 54, 63, 54, C_FLOOR_HI)
    c.line(0, 58, 63, 58, C_FLOOR_LINE)
    c.line(0, 59, 63, 59, C_FLOOR_HI)

    # Vertical staggered joints
    for x in [0, 16, 32, 48]:
        c.line(x, 49, x, 52, C_FLOOR_LINE)
        c.line(x+8, 54, x+8, 57, C_FLOOR_LINE)
        c.line(x, 59, x, 63, C_FLOOR_LINE)

    # Soft reflections on polished floor:
    # Headlight reflection (X=18..24)
    for y in range(49, 63):
        if (y + 14) % 2 == 0:
            c.set(20, y, C_FLOOR_REFL_W)
            c.set(21, y, C_FLOOR_REFL_W)
        if y % 3 == 0:
            c.set(19, y, C_FLOOR_REFL_W)
            c.set(22, y, C_FLOOR_REFL_W)

    # Window reflections (X=34..42, X=48..58)
    for rx in [35, 37, 39, 41, 49, 51, 55, 57]:
        for y in range(50, 62, 2):
            c.set(rx, y, C_FLOOR_REFL_Y)

    # Cyan speed stripe reflection
    for rx in [26, 27, 43, 52]:
        for y in range(51, 60, 3):
            c.set(rx, y, C_FLOOR_REFL_C)

    # ========================================================
    # 8. PLATFORM BENCH (Center: X=24 to X=40, Y=44 to Y=53)
    # ========================================================
    c.rect(26, 48, 2, 5, C_BENCH_FRAME)
    c.rect(38, 48, 2, 5, C_BENCH_FRAME)
    c.line(26, 48, 26, 52, C_BENCH_HI)
    c.line(38, 48, 38, 52, C_BENCH_HI)
    c.line(25, 53, 28, 53, C_FLOOR_LINE)
    c.line(37, 53, 40, 53, C_FLOOR_LINE)

    # Bench cast shadow
    c.rect(24, 53, 17, 1, C_BLACK)

    # Seat plank (Y=48..49)
    c.rect(24, 48, 17, 2, C_WOOD_MID)
    c.line(24, 48, 40, 48, C_WOOD_HI)
    c.line(24, 49, 40, 49, C_WOOD_DRK)
    c.line(24, 50, 40, 50, C_BENCH_FRAME)

    # Backrest (Y=44..46)
    c.rect(26, 44, 1, 4, C_BENCH_HI)
    c.rect(38, 44, 1, 4, C_BENCH_HI)
    c.rect(25, 44, 15, 2, C_WOOD_MID)
    c.line(25, 44, 39, 44, C_WOOD_HI)
    c.line(25, 45, 39, 45, C_WOOD_DRK)

    # ========================================================
    # 9. THREE PASSENGERS WITH CRISP, READABLE SILHOUETTES
    # ========================================================

    # --------------------------------------------------------
    # PASSENGER 1: Standing Waiting, Wind-Blown Coat (Left: X=6..14, Y=27..51)
    # Framed in dramatic high contrast against the luminous headlight beam!
    # --------------------------------------------------------
    # Floor contact shadow
    c.rect(9, 51, 5, 1, C_BLACK)

    # Legs & Boots (Y=45..51)
    c.rect(10, 45, 2, 6, C_P1_PANTS)
    c.rect(12, 45, 2, 6, C_P1_PANTS)
    c.rect(10, 50, 2, 1, C_BLACK)
    c.rect(12, 50, 3, 1, C_BLACK)

    # Long Trench Coat Body (Y=32..44)
    c.rect(10, 32, 4, 12, C_P1_COAT_DRK)
    c.rect(11, 32, 3, 11, C_P1_COAT_MID)
    # Subtle crisp rim light along the front edge from oncoming train!
    c.line(14, 32, 14, 44, C_P1_RIM)

    # Dynamic billowing coat tail to the left (wind from train)
    c.poly([(10, 36), (6, 36), (4, 40), (7, 41), (10, 40)], C_P1_COAT_DRK, fill=True)
    c.line(4, 37, 9, 37, C_P1_COAT_HI)
    c.set(3, 38, C_P1_COAT_DRK)
    c.set(3, 39, C_P1_COAT_DRK)

    # Fluttering Red Scarf (blowing back in wind)
    c.set(10, 31, C_P1_SCARF)
    c.set(9, 31, C_P1_SCARF)
    c.set(8, 32, C_P1_SCARF)
    c.set(7, 32, C_P1_SCARF_HI)
    c.set(6, 32, C_P1_SCARF)

    # Head & Face (Y=27..30, X=10..14)
    c.rect(11, 28, 3, 3, C_P1_SKIN)
    # Face profile facing right towards oncoming train:
    c.set(14, 29, C_P1_SKIN_HI)
    c.set(13, 29, C_P1_SKIN_HI)
    c.set(13, 30, C_P1_SKIN)
    # Hair blowing back to the left
    c.rect(10, 27, 4, 2, C_P1_HAIR)
    c.set(9, 27, C_P1_HAIR)
    c.set(8, 28, C_P1_HAIR)
    c.set(7, 28, C_P1_HAIR)

    # --------------------------------------------------------
    # PASSENGER 2: Seated on Bench, Phone Glow (Center: X=28..36, Y=34..52)
    # Sitting naturally ON the bench, head down, glowing phone screen.
    # --------------------------------------------------------
    # Floor contact shadow
    c.rect(33, 52, 4, 1, C_BLACK)

    # Torso: leaning forward onto seat (Y=37 to Y=47)
    c.rect(28, 37, 4, 10, C_P2_JACKET_D)
    c.rect(29, 37, 3, 9, C_P2_JACKET_M)
    c.line(28, 37, 28, 45, C_P2_JACKET_HI)

    # Thighs resting directly ON bench seat (Y=47..48, X=28..33)
    c.rect(28, 47, 6, 2, C_P2_JEANS_D)
    c.line(29, 47, 33, 47, C_P2_JEANS_M)

    # Knees & Calves extending down (Y=49 to Y=52, X=33..35)
    c.rect(33, 49, 2, 3, C_P2_JEANS_D)
    c.rect(34, 49, 2, 3, C_P2_JEANS_M)
    c.rect(34, 52, 3, 1, C_BLACK)
    # Background leg
    c.rect(31, 49, 2, 3, C_BLACK)
    c.rect(31, 52, 2, 1, C_BLACK)

    # Arms holding smartphone
    c.line(30, 40, 32, 43, C_P2_JACKET_M)
    c.set(33, 42, C_P2_SKIN)
    c.set(33, 43, C_P2_SKIN)

    # Glowing smartphone screen
    c.set(34, 42, C_WHITE)
    c.set(34, 43, C_CYAN_HI)
    c.set(35, 42, C_CYAN_HI)

    # Head (tilted down toward phone, Y=34..37)
    c.rect(29, 34, 4, 2, C_P2_HAIR)
    c.set(28, 35, C_P2_HAIR)
    c.rect(30, 35, 3, 2, C_P2_SKIN)
    c.set(32, 36, C_P2_SKIN_HI)

    # --------------------------------------------------------
    # PASSENGER 3: Standing Commuter Checking Watch (Right: X=48..57, Y=27..51)
    # Backpack on, left arm raised checking wristwatch, holding coffee.
    # --------------------------------------------------------
    # Floor contact shadow
    c.rect(51, 51, 5, 1, C_BLACK)

    # Legs & Shoes (Y=43..51)
    c.rect(51, 43, 2, 8, C_P3_PANTS)
    c.rect(54, 43, 2, 8, C_P3_PANTS)
    c.rect(51, 50, 2, 1, C_WHITE)
    c.rect(54, 50, 2, 1, C_WHITE)
    c.set(51, 49, C_BLACK)
    c.set(54, 49, C_BLACK)

    # Backpack on back (left side of commuter, X=48..51, Y=33..42)
    c.rect(48, 34, 3, 8, C_P3_PACK_D)
    c.line(49, 34, 49, 41, C_P3_PACK_M)
    c.set(50, 33, C_P3_PACK_D)

    # Torso & Ochre Jacket (Y=32..42)
    c.rect(51, 33, 4, 10, C_P3_JACKET_D)
    c.rect(52, 33, 3, 9, C_P3_JACKET_M)
    c.line(53, 33, 53, 41, C_P3_JACKET_HI)

    # Right Arm (holding coffee cup)
    c.line(51, 34, 50, 40, C_P3_JACKET_D)
    c.set(50, 41, C_P3_SKIN)
    c.set(50, 42, C_WHITE)
    c.set(50, 43, C_WOOD_MID)
    c.set(50, 44, C_WHITE)

    # Left Arm: RAISED WATCH-CHECKING GESTURE WITH READABLE SILHOUETTE!
    c.set(55, 34, C_P3_JACKET_D)
    c.set(56, 35, C_P3_JACKET_D)
    c.set(57, 36, C_P3_JACKET_M)
    c.set(56, 36, C_P3_JACKET_HI)
    c.set(55, 36, C_P3_JACKET_HI)
    c.set(54, 36, C_CYAN_HI)     # glowing watch face
    c.set(53, 36, C_P3_SKIN)     # hand

    # Head (Y=27..31, tilted down looking at watch)
    c.rect(51, 28, 4, 2, C_P3_HAIR)
    c.set(50, 29, C_P3_HAIR)
    c.rect(52, 29, 3, 3, C_P3_SKIN)
    c.set(54, 30, C_P3_SKIN)

    # Headphones around neck
    c.set(51, 31, C_P3_HEADPHONE)
    c.set(53, 31, C_P3_HEADPHONE)

    # ========================================================
    # 10. ATMOSPHERIC PARTICLES & WIND DRAFT
    # ========================================================
    c.set(12, 24, C_WHITE)
    c.set(7, 26, C_BEAM_CORE)
    c.set(15, 38, C_WHITE)
    c.set(18, 42, C_WIN_HOT)
    c.set(22, 43, C_PALE_GLOW)

    return c

c = draw_subway()
view(c)
print("Visible colors used:", c.stats()["colors_used"])
finish(c)
