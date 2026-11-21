from pixelbench_api import *

def build_scene():
    c = new_canvas(64, 64, name="offshore_turbine")

    # =========================================================================
    # COHESIVE 48-COLOR PALETTE
    # =========================================================================
    # Sky tones (Atmospheric marine perspective)
    SKY_0 = "#2d3e52" # dark zenith
    SKY_1 = "#384f66"
    SKY_2 = "#49647d"
    SKY_3 = "#5e7c96"
    SKY_4 = "#7898b0"
    SKY_5 = "#99b6cb"
    SKY_6 = "#c2d8e6" # luminous horizon glow

    # Clouds & Whites
    CLOUD_M = "#8caac0"
    CLOUD_L = "#b5cee0"
    CLOUD_W = "#e2edf5"
    WHITE   = "#ffffff"

    # Distant Turbines
    DT_BLADE = "#dbe8f2"
    DT_TOWER = "#9ab5c8"
    DT_SHAD  = "#628099"
    DT_TP_L  = "#e0a514"
    DT_TP_D  = "#ad7a08"

    # Ocean / Waves
    SEA_0    = "#07141f" # deepest ocean trough
    SEA_1    = "#0c1e2c" # deep foreground
    SEA_2    = "#122a3d" # mid ocean
    SEA_3    = "#18364c" # horizon water
    SEA_SWELL= "#234963" # rolling wave body
    SEA_CREST= "#3c7494" # wave crest / translucency
    SEA_FOAM = "#6eaec9" # spray / aerated water
    SEA_WHT  = "#b8e1f0" # bright sea foam

    # Steel Tower (White cylindrical mast)
    TOW_HI = "#f4f8fb"
    TOW_L  = "#d4e2eb"
    TOW_M  = "#a8bfcd"
    TOW_D  = "#7690a1"
    TOW_DK = "#4b6272"

    # Yellow Transition Piece & Offshore Structure
    YEL_HI = "#ffe042" # specular / catchlight
    YEL_L  = "#f2b502" # safety yellow
    YEL_M  = "#c78600" # amber / shading
    YEL_D  = "#8a5500" # shadow
    YEL_DK = "#4c2c00" # deep shadow

    # Wet Tide Mark & Water Reflections
    TIDE_1   = "#3a3412" # wet algae / barnacle band
    TIDE_2   = "#201e08" # dark splash grime
    SEA_REFL = "#2c3b1c" # subtle green-gold reflection of yellow TP on wet sea

    # Industrial Steel / Structure
    STL_DK = "#141920" # black steel / boots / straps
    STL_M  = "#2a343d" # structural metal
    STL_L  = "#4a5864" # galvanized steel / deck
    STL_HI = "#7a8d9c" # ladder rungs / highlight

    # Technician
    ORG_HI = "#ff7214" # hi-vis highlight
    ORG_M  = "#ff4400" # hi-vis primary orange
    ORG_D  = "#b32c00" # shadow orange
    SKIN   = "#d49774"
    CYAN   = "#38bdf8" # headlamp / carabiner

    # =========================================================================
    # 1. SKY (y = 0 .. 33)
    # Atmospheric marine sky gradient with light, wispy cirrus drifts
    # =========================================================================
    c.rect(0, 0,  64, 4, SKY_0)
    c.rect(0, 4,  64, 5, SKY_1)
    c.rect(0, 9,  64, 6, SKY_2)
    c.rect(0, 15, 64, 6, SKY_3)
    c.rect(0, 21, 64, 5, SKY_4)
    c.rect(0, 26, 64, 4, SKY_5)
    c.rect(0, 30, 64, 4, SKY_6)

    # Gentle wispy clouds positioned away from distant turbine rotors
    c.line(1, 3, 6, 3, CLOUD_M)
    c.line(2, 4, 8, 4, CLOUD_L)

    c.line(25, 3, 33, 3, CLOUD_M)
    c.line(24, 4, 34, 4, CLOUD_L)
    c.line(26, 5, 32, 5, CLOUD_W)

    c.line(27, 9, 34, 9, CLOUD_L)
    c.line(29, 10, 33, 10, CLOUD_W)

    # Soaring seagull on marine updraft
    c.set(24, 7, WHITE)
    c.set(23, 6, CLOUD_W)
    c.set(25, 6, CLOUD_W)

    # =========================================================================
    # 2. TWO DISTANT WIND TURBINES (on sea horizon, y = 34)
    # Believable scale, classic 3-blade offshore turbine silhouettes
    # =========================================================================

    # --- Turbine 1 (Far horizon, x = 6) ---
    # Yellow TP base at waterline (y = 32..33)
    c.rect(5, 32, 2, 2, DT_TP_L)
    c.set(6, 33, DT_TP_D)
    # Slender tower (y = 22..31)
    c.line(6, 22, 6, 31, DT_TOWER)
    # Nacelle at y = 21
    c.rect(5, 21, 3, 1, DT_BLADE)
    c.set(6, 21, WHITE) # Hub
    # 3 Rotor blades (length 5 px, 120 deg symmetry)
    c.line(6, 20, 6, 16, DT_BLADE)  # straight up
    c.line(5, 22, 2, 24, DT_BLADE)  # down-left
    c.line(7, 22, 10, 24, DT_BLADE) # down-right

    # --- Turbine 2 (Mid-distance, x = 14) ---
    # Yellow TP base at waterline (y = 31..33)
    c.rect(13, 31, 2, 3, DT_TP_L)
    c.set(14, 31, DT_TP_D)
    c.set(14, 32, DT_TP_D)
    # Slender tower (y = 15..30)
    c.line(13, 15, 13, 30, TOW_L)
    c.line(14, 15, 14, 30, DT_SHAD)
    # Nacelle at y = 14
    c.rect(12, 14, 4, 1, TOW_HI)
    c.set(13, 14, WHITE) # Hub
    # 3 Rotor blades (length 7 px, oriented cleanly in open sky)
    c.line(14, 13, 18, 8, WHITE)    # blade 1: up-right
    c.line(12, 13, 8, 9, DT_BLADE)  # blade 2: up-left
    c.line(13, 15, 13, 21, DT_BLADE)# blade 3: straight down

    # =========================================================================
    # 3. OCEAN AND WAVES (y = 34 .. 63)
    # Atmospheric deep ocean swells, wave crests, whitecaps, sea foam
    # =========================================================================
    c.rect(0, 34, 64, 4,  SEA_3)
    c.rect(0, 38, 64, 5,  SEA_2)
    c.rect(0, 43, 64, 6,  SEA_1)
    c.rect(0, 49, 64, 7,  SEA_0)
    c.rect(0, 56, 64, 8,  SEA_0)

    # Distant wave ripples (y = 35..39)
    for wx, wy, wl in [
        (1, 35, 7), (11, 35, 8), (22, 35, 7),
        (0, 37, 5), (8, 37, 9),  (19, 37, 8),
        (3, 39, 7), (13, 39, 10), (25, 39, 5),
    ]:
        c.line(wx, wy, wx + wl, wy, SEA_SWELL)
        c.line(wx + 2, wy, wx + wl - 2, wy, SEA_CREST)

    # Midground swells with whitecaps (y = 41..49)
    # Wave 1 (y = 42)
    c.line(1, 42, 13, 42, SEA_SWELL)
    c.line(4, 41, 10, 41, SEA_CREST)
    c.line(6, 41, 8, 41, SEA_FOAM)
    c.set(7, 41, SEA_WHT)

    # Wave 2 (y = 45)
    c.line(5, 45, 20, 45, SEA_SWELL)
    c.line(9, 44, 17, 44, SEA_CREST)
    c.line(12, 44, 15, 44, SEA_FOAM)
    c.set(13, 44, WHITE)

    # Wave 3 (y = 48)
    c.line(0, 48, 12, 48, SEA_SWELL)
    c.line(3, 47, 9, 47, SEA_CREST)
    c.line(5, 47, 7, 47, SEA_FOAM)

    # Foreground surging waves (y = 51..63)
    c.line(1, 53, 19, 53, SEA_SWELL)
    c.line(4, 52, 16, 52, SEA_CREST)
    c.line(7, 52, 12, 52, SEA_FOAM)
    c.line(9, 51, 11, 51, SEA_WHT)
    c.set(10, 51, WHITE)

    c.line(0, 58, 17, 58, SEA_SWELL)
    c.line(3, 57, 14, 57, SEA_CREST)
    c.line(6, 57, 11, 57, SEA_FOAM)
    c.line(8, 56, 10, 56, SEA_WHT)

    c.line(2, 62, 18, 62, SEA_SWELL)
    c.line(6, 61, 15, 61, SEA_CREST)
    c.line(9, 61, 12, 61, SEA_FOAM)

    # =========================================================================
    # 4. MAIN WIND TURBINE: TOWER (White cylindrical mast, x = 33..63, y = 0..26)
    # Cylindrical lighting, panel rings, aviation ID plate, entrance door
    # =========================================================================
    tower_bands = [
        (33, 35, TOW_L),   # left highlight rim
        (35, 41, TOW_HI),  # bright facing surface
        (41, 48, TOW_M),   # curve midtone
        (48, 55, TOW_D),   # shade
        (55, 64, TOW_DK),  # deep shadow
    ]
    for x0, x1, col in tower_bands:
        c.rect(x0, 0, x1 - x0, 26, col)

    # Dithered cylinder curvature transitions
    for y in range(0, 26):
        if y % 2 == 0:
            c.set(41, y, TOW_HI)
            c.set(48, y, TOW_M)
            c.set(55, y, TOW_D)

    # Circumferential weld rings
    for y_seam in [8, 17]:
        c.line(33, y_seam, 63, y_seam, TOW_D)
        c.line(33, y_seam + 1, 46, y_seam + 1, WHITE)

    # Turbine ID plate / hazard sign (y = 11..14, x = 42..48)
    c.rect(42, 11, 7, 4, STL_DK)
    c.rect(43, 12, 5, 2, YEL_M)
    # Letters "OW"
    c.set(44, 12, YEL_HI)
    c.set(46, 12, YEL_HI)
    c.set(44, 13, YEL_HI)
    c.set(45, 13, YEL_HI)
    c.set(46, 13, YEL_HI)

    # Tower Entrance Hatch / Door (platform level, y = 17..25, x = 42..48)
    c.rect(42, 17, 7, 9, STL_DK) # weather-tight door frame
    c.rect(43, 18, 5, 8, STL_M)  # steel hatch door
    c.rect(44, 20, 3, 2, YEL_L)  # hazard warning plate
    c.set(43, 22, TOW_HI)        # stainless latch handle
    # Bulkhead lamp over door
    c.set(45, 16, WHITE)
    c.set(44, 16, YEL_HI)
    c.set(46, 16, YEL_HI)

    # =========================================================================
    # 5. TRANSITION PIECE (Yellow Steel Foundation, y = 26..52, x = 30..63)
    # Monumental cylindrical base, clean metallic gradient
    # =========================================================================
    tp_bands = [
        (30, 32, YEL_L),   # outer left rim
        (32, 38, YEL_HI),  # bright facing highlight
        (38, 46, YEL_M),   # rich amber midtone
        (46, 53, YEL_D),   # deep ochre shadow
        (53, 64, YEL_DK),  # dark bronze shadow
    ]
    for x0, x1, col in tp_bands:
        c.rect(x0, 26, x1 - x0, 26, col)

    # Dithered cylinder transitions
    for y in range(26, 50):
        if y % 2 == 0:
            c.set(38, y, YEL_HI)
            c.set(46, y, YEL_M)
            c.set(53, y, YEL_D)

    # Flange ring weld seam on TP (y = 38)
    c.line(30, 38, 63, 38, YEL_D)
    c.line(30, 39, 45, 39, YEL_HI)

    # Waterline tidal splash band (y = 50..52)
    c.line(30, 50, 63, 50, TIDE_1)
    c.line(30, 51, 63, 51, TIDE_2)
    c.line(30, 52, 63, 52, TIDE_2)

    # Ocean water meeting the foundation (y = 52..63)
    # Realistic waves and curling foam trails around the base
    c.line(26, 52, 63, 52, SEA_SWELL)
    c.line(25, 53, 63, 53, SEA_CREST)
    c.line(24, 54, 42, 54, SEA_FOAM)
    c.line(25, 54, 35, 54, SEA_WHT)

    # Foam ribbon curling around base (y = 55)
    c.line(25, 55, 46, 55, SEA_CREST)
    c.line(26, 55, 34, 55, SEA_WHT)
    c.set(28, 55, WHITE)
    c.set(29, 55, WHITE)

    # Foam ribbon 2 (y = 57)
    c.line(27, 57, 50, 57, SEA_SWELL)
    c.line(28, 57, 40, 57, SEA_FOAM)
    c.line(30, 57, 36, 57, SEA_WHT)

    # Swirling backwash in foreground (y = 59..61)
    c.line(28, 59, 46, 59, SEA_CREST)
    c.line(31, 59, 39, 59, SEA_FOAM)
    c.line(30, 61, 48, 61, SEA_SWELL)

    # Wet sea reflection of yellow TP
    c.line(34, 56, 42, 56, SEA_REFL)
    c.line(35, 58, 41, 58, SEA_REFL)

    # Sea spray droplets splashing against yellow steel
    for sx, sy in [(28, 49), (29, 47), (31, 48), (27, 48), (32, 46)]:
        c.set(sx, sy, SEA_WHT)

    # =========================================================================
    # 6. MAINTENANCE PLATFORM (Deck y = 25..26, Railings y = 20..25)
    # Cantilevered steel grating, yellow railings, davit crane
    # =========================================================================
    # Cantilever support bracket under platform (x = 21..30, y = 26..31)
    c.line(21, 26, 30, 26, STL_M)  # lower girder
    c.line(22, 27, 30, 31, YEL_D)  # diagonal yellow brace to TP
    c.line(23, 28, 30, 32, YEL_DK)

    # Grated platform deck (x = 21..44, y = 25..26)
    c.line(21, 26, 44, 26, YEL_L)  # yellow kick-plate / toe-board
    c.line(21, 25, 44, 25, STL_L)  # steel grating surface
    for gx in range(22, 44, 2):
        c.set(gx, 25, STL_DK)      # open mesh perforations

    # Yellow Safety Railings (Handrail at y = 20, mid-rail at y = 22.5)
    # Stanchions (vertical posts) at x = 21, 31, 41
    for px in [21, 31, 41]:
        c.line(px, 20, px, 25, YEL_L)
        c.set(px, 20, YEL_HI)

    # Handrails (left: 21..25, ladder access gap at 26..30, right: 31..41)
    c.line(21, 20, 25, 20, YEL_HI) # top rail left
    c.line(21, 22, 25, 22, YEL_L)  # mid rail left
    c.line(31, 20, 41, 20, YEL_HI) # top rail right
    c.line(31, 22, 41, 22, YEL_L)  # mid rail right

    # Davit Crane (at outer platform corner x = 20..22, y = 14..25)
    c.line(22, 16, 22, 25, YEL_L)  # vertical mast
    c.set(22, 16, YEL_HI)
    c.line(17, 15, 22, 15, YEL_HI) # horizontal boom extending over sea
    c.line(19, 15, 22, 18, YEL_L)  # triangular gusset brace
    c.set(22, 19, YEL_M)           # winch box
    c.set(17, 16, STL_DK)          # pulley block
    c.line(17, 17, 17, 21, STL_DK) # winch hoist cable
    c.set(17, 22, YEL_HI)          # lifting hook

    # =========================================================================
    # 7. BOAT LANDING FENDERS & VERTICAL LADDER (x = 24..30, y = 25..51)
    # =========================================================================
    # Outer yellow bumper fender pipe (x = 24, y = 26..51)
    c.line(24, 26, 24, 51, YEL_L)
    c.line(23, 27, 23, 51, YEL_M)
    c.set(24, 26, YEL_HI)

    # Horizontal structural bumper braces connecting fender to monopile
    for by in [31, 40, 48]:
        c.line(24, by, 30, by, YEL_M)
        c.set(24, by - 1, YEL_HI)
        c.set(30, by - 1, YEL_HI)

    # Vertical Ladder (x = 26..29, y = 24..49)
    # Steel stringers
    c.line(26, 24, 26, 49, STL_M)
    c.line(29, 24, 29, 49, STL_M)

    # Central safety fall-arrest wire / glide rail (x = 27)
    c.line(27, 23, 27, 49, STL_HI)

    # Ladder rungs (every 2 pixels from y = 24 down to 48)
    for ry in range(24, 50, 2):
        c.line(26, ry, 29, ry, STL_L)
        c.set(27, ry, STL_HI)

    # Safety handholds extending above platform deck (y = 22..24)
    c.line(26, 22, 26, 24, YEL_HI)
    c.line(29, 22, 29, 24, YEL_HI)
    c.line(26, 22, 29, 22, YEL_HI)

    # =========================================================================
    # 8. TECHNICIAN CLIMBING LADDER (y = 31 .. 46, x = 25 .. 31)
    # Believable human scale (~15 px tall), hi-vis orange suit, helmet,
    # full safety harness, fall-arrest carabiner, dynamic climbing pose
    # =========================================================================

    # --- Head & Helmet (y = 32..35) ---
    c.set(27, 32, WHITE)    # helmet crown top
    c.set(28, 32, WHITE)
    c.set(26, 33, YEL_HI)   # helmet brim
    c.set(27, 33, WHITE)
    c.set(28, 33, TOW_L)    # helmet rear curve
    c.set(29, 33, CYAN)     # headlamp lens (cool cyan glow)
    c.set(27, 34, STL_DK)   # chin strap / dark balaclava
    c.set(28, 34, SKIN)     # cheek / neck skin tone

    # --- Arms & Upper Body (y = 31..38) ---
    # Left arm reaching UP to grip rung at y = 30
    c.set(30, 31, STL_DK)   # black work glove gripping rung 30!
    c.set(30, 32, ORG_HI)   # reaching forearm
    c.set(30, 33, ORG_M)    # bicep
    c.set(30, 34, ORG_M)    # shoulder junction

    # Shoulders (y = 35)
    c.set(26, 35, ORG_M)    # left shoulder
    c.set(27, 35, STL_DK)   # harness strap crossing left shoulder
    c.set(28, 35, ORG_HI)   # chest
    c.set(29, 35, ORG_M)

    # Chest & Right arm gripping mid rung (y = 36)
    c.set(25, 36, ORG_D)    # back contour
    c.set(26, 36, ORG_M)    # orange suit
    c.set(27, 36, WHITE)    # silver retroreflective tape across chest!
    c.set(28, 36, ORG_HI)   # chest
    c.set(29, 36, ORG_M)    # right arm
    c.set(30, 36, STL_DK)   # right glove gripping rung 36!

    # Mid-torso & Fall-arrest harness (y = 37)
    c.set(25, 37, ORG_D)    # back shadow
    c.set(26, 37, ORG_M)    # suit
    c.set(27, 37, CYAN)     # steel fall-arrest carabiner clamped to safety cable!
    c.set(28, 37, STL_DK)   # harness center D-ring
    c.set(29, 37, ORG_D)

    # Waist & Work belt (y = 38)
    c.set(25, 38, STL_DK)   # tool pouch / radio holster
    c.set(26, 38, ORG_M)
    c.set(27, 38, STL_M)    # black harness waist belt
    c.set(28, 38, ORG_M)

    # --- Lower Body & Legs (y = 39..46) ---
    # Left leg bent high, foot planted on rung 42!
    # Right leg descending, foot planted on rung 46!

    # Pelvis & Thigh origins (y = 39)
    c.set(26, 39, ORG_D)    # seat
    c.set(27, 39, ORG_M)    # left thigh raising
    c.set(28, 39, ORG_HI)

    # Thighs & Knee action (y = 40)
    c.set(25, 40, ORG_D)    # right thigh back
    c.set(26, 40, STL_DK)   # harness leg loop
    c.set(27, 40, ORG_M)
    c.set(28, 40, STL_DK)   # left knee pad (reinforced black Cordura)
    c.set(29, 40, ORG_HI)   # left shin stepping forward

    # Left foot planted on rung 42, right leg descending (y = 41..42)
    c.set(26, 41, ORG_M)    # right thigh
    c.set(28, 41, STL_DK)   # left work boot heel
    c.set(29, 41, STL_M)    # left boot sole locked onto rung 42!

    # Right leg descending (y = 42..45)
    c.set(26, 42, STL_DK)   # right knee pad
    c.set(27, 42, ORG_D)    # right calf

    c.set(26, 43, ORG_M)    # right calf lower
    c.set(27, 43, ORG_D)

    c.set(27, 44, STL_DK)   # right ankle / boot collar

    # Right foot planted on lower rung 46
    c.set(27, 45, STL_DK)   # right boot heel
    c.set(28, 45, STL_M)    # right boot sole locked onto rung 46!

    # Verification
    stats = c.stats()
    print("Visible colors:", stats["colors_used"])
    print("Stats:", c.stats_text())

    view(c)
    finish(c)

build_scene()
