"""
Polar Researcher Sprite Generator
Resolution: 48x48
Expert Pixel Art Sprite:
- Forward-leaning pose battling against strong arctic wind
- Heavy cold-weather clothing (bulky arctic parka, coyote fur hood, thick insulated salopettes, heavy bunny boots)
- Rugged scientific sample case with cryo temperature display and corner bumpers
- Pale blue glassy goggle reflections with horizon flare
- Bulky, realistic cold-weather anatomy with clear depth
- Transparent background with grounded snowdrift and wind spindrift
"""

def build_polar_researcher(c):
    palette = {
        # Core & dark shadows
        'black': '#0a0d14',
        'outline': '#101420',
        'shadow_deep': '#141824',
        
        # Parka - Antarctic Expedition High-Vis Red / Orange
        'parka_crease': '#38080e',
        'parka_deep': '#520e16',
        'parka_shadow': '#7c1820',
        'parka_dark': '#a62222',
        'parka_mid': '#ce3628',
        'parka_bright': '#ec5032',
        'parka_hi': '#f8744a',
        'parka_rim': '#ffa474',
        'parka_frost': '#e2eef8',
        
        # 3M Scotchlite Reflective Safety Tape
        'refl_shadow': '#3c5662',
        'refl_dark': '#5e8290',
        'refl_mid': '#98beca',
        'refl_light': '#d8eef4',
        'refl_white': '#ffffff',
        
        # Fur Ruff (Arctic Wolf / Coyote Fur Trim on Hood)
        'fur_crease': '#1e120c',
        'fur_deep': '#322016',
        'fur_shadow': '#4c3222',
        'fur_dark': '#6e4c34',
        'fur_mid': '#966e4a',
        'fur_light': '#c49c74',
        'fur_pale': '#e8d2b6',
        'fur_frost': '#f2f8fc',
        
        # Balaclava / Face Mask
        'mask_deep': '#0e121a',
        'mask_dark': '#181e2a',
        'mask_mid': '#263042',
        'mask_light': '#3a465c',
        
        # Snow / Glacier Goggles (Pale Blue Glassy Horizon Reflection)
        'gog_rim': '#0a0e16',
        'gog_dark': '#122a38',
        'gog_deep_cyan': '#18445a',
        'gog_mid_cyan': '#266c88',
        'gog_cyan': '#42a8c0',
        'gog_pale': '#7ee0f0',
        'gog_ice_white': '#ccf6ff',
        'gog_glint': '#ffffff',
        'gog_strap': '#1a202c',
        
        # Snow Pants (Bulky Arctic Expedition Salopettes - Slate Navy)
        'pant_crease': '#0a0e16',
        'pant_deep': '#121824',
        'pant_shadow': '#1a2234',
        'pant_dark': '#263248',
        'pant_mid': '#364462',
        'pant_light': '#4a5c82',
        'pant_hi': '#687ea2',
        'knee_patch': '#141c2a',
        
        # Polar Extreme-Cold Boots (Bunny / Baffin Boots)
        'boot_sole': '#0a0d14',
        'boot_deep': '#121620',
        'boot_shadow': '#1c2230',
        'boot_dark': '#283244',
        'boot_mid': '#3c4a62',
        'boot_light': '#566684',
        'boot_frost': '#c8ddf0',
        
        # Heavy Insulated Mittens
        'glove_deep': '#0e121a',
        'glove_shadow': '#18202c',
        'glove_dark': '#242e40',
        'glove_mid': '#36445c',
        'glove_light': '#50627e',
        'glove_frost': '#b8d0e6',
        
        # Field Backpack & Radio
        'pack_deep': '#121a18',
        'pack_shadow': '#1c2a28',
        'pack_dark': '#2a3c38',
        'pack_mid': '#3c5450',
        'pack_light': '#54746e',
        'pack_strap': '#101616',
        'antenna_wire': '#222830',
        'antenna_red': '#ff2a2a',
        
        # Rugged Scientific Sample Case (Pelican / Storm Specimen Case)
        'case_bumper': '#0c0f14',
        'case_crease': '#462404',
        'case_deep': '#6e3c06',
        'case_shadow': '#9c5a0c',
        'case_dark': '#c27412',
        'case_mid': '#e0921a',
        'case_bright': '#f2ac26',
        'case_hi': '#ffcc44',
        'case_pale': '#fcee84',
        'case_latch': '#d4e4f0',
        'case_latch_dark': '#526678',
        'case_screen_bg': '#061412',
        'case_screen_led': '#22e49e', # Glowing cryo indicator
        
        # Snow & Ice Particles
        'snow_shadow': '#86a8c4',
        'snow_mid': '#bedaf0',
        'snow_white': '#ffffff',
    }

    # Register colors
    for k, v in palette.items():
        c.color(v, k)

    grid = [[None for _ in range(48)] for _ in range(48)]

    def p(x, y, col):
        if 0 <= x < 48 and 0 <= y < 48:
            grid[y][x] = col

    # -------------------------------------------------------------------------
    # 1. EXPEDITION BACKPACK & RADIO ANTENNA (Mounted on hunched back)
    # -------------------------------------------------------------------------
    # Radio Antenna whipping straight back in the howling gale:
    antenna_pts = [
        (28, 13), (29, 13), (30, 12), (31, 12), (32, 11), (33, 11),
        (34, 10), (35, 10), (36, 9), (37, 9), (38, 9), (39, 9)
    ]
    for x, y in antenna_pts:
        p(x, y, 'antenna_wire')
    p(40, 9, 'antenna_red') # Flashing beacon tip

    # Sleeping mat / survival roll on top of pack:
    for x in range(23, 30):
        p(x, 12, 'pack_deep')
        p(x, 13, 'pack_mid')
        p(x, 14, 'pack_light')
    p(22, 13, 'pack_shadow')
    p(30, 13, 'pack_deep')
    p(24, 12, 'pack_strap'); p(24, 13, 'pack_deep'); p(24, 14, 'pack_strap')
    p(28, 12, 'pack_strap'); p(28, 13, 'pack_deep'); p(28, 14, 'pack_strap')

    # Main backpack body (y = 15 to 24, x = 22 to 31):
    pack_rows = [
        (15, 22, 29),
        (16, 22, 30),
        (17, 23, 31),
        (18, 23, 31),
        (19, 23, 31),
        (20, 23, 31),
        (21, 23, 30),
        (22, 23, 30),
        (23, 23, 29),
        (24, 23, 28),
    ]
    for y, x1, x2 in pack_rows:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'pack_shadow')
            elif x in (x1 + 1, x1 + 2):
                p(x, y, 'pack_light')
            elif x == x2:
                p(x, y, 'pack_deep')
            elif x == x2 - 1:
                p(x, y, 'pack_shadow')
            else:
                p(x, y, 'pack_mid')
    # Pocket seams:
    for x in range(25, 30):
        p(x, 17, 'pack_deep')
        p(x, 20, 'pack_deep')
    p(29, 20, 'refl_mid')

    # -------------------------------------------------------------------------
    # 2. BULKY EXPEDITION SNOW PANTS (Heavy Insulated Salopettes)
    # -------------------------------------------------------------------------
    # Crotch & pelvis solid fill (under coat hem):
    for y in range(28, 33):
        for x in range(18, 28):
            p(x, y, 'pant_deep')

    # Rear Leg (Right leg - bulky insulated pant extending back):
    # Thigh:
    rear_thigh = [
        (29, 22, 28),
        (30, 22, 28),
        (31, 23, 29),
        (32, 23, 29),
        (33, 23, 30),
    ]
    for y, x1, x2 in rear_thigh:
        for x in range(x1, x2 + 1):
            p(x, y, 'pant_deep')

    # Rear Knee & Shin (thick insulated snow pants, natural width):
    rear_shin = [
        (34, 23, 30),
        (35, 23, 31),
        (36, 24, 31),
        (37, 24, 32),
        (38, 24, 32), # Natural calf width, leaves comfortable gap to front leg
        (39, 25, 33),
        (40, 26, 33),
    ]
    for y, x1, x2 in rear_shin:
        for x in range(x1, x2 + 1):
            if y in (37, 38) and x <= 26:
                p(x, y, 'pant_deep') # Cast shadow directly under the sample case
            elif x == x1:
                p(x, y, 'pant_dark')
            elif x in (x1 + 1, x1 + 2):
                p(x, y, 'pant_mid')
            elif x == x2:
                p(x, y, 'pant_crease')
            else:
                p(x, y, 'pant_shadow')

    # Rear Boot (Bulky Bunny Boot pushing into ground, y = 41..43, x = 27..35):
    p(28, 41, 'boot_mid'); p(29, 41, 'boot_light'); p(30, 41, 'boot_mid'); p(31, 41, 'boot_dark'); p(32, 41, 'boot_shadow'); p(33, 41, 'boot_deep'); p(34, 41, 'boot_deep')
    p(27, 42, 'boot_dark'); p(28, 42, 'boot_mid'); p(29, 42, 'boot_light'); p(30, 42, 'boot_mid'); p(31, 42, 'boot_dark'); p(32, 42, 'boot_shadow'); p(33, 42, 'boot_deep'); p(34, 42, 'boot_deep'); p(35, 42, 'boot_deep')
    for x in range(27, 36):
        p(x, 43, 'boot_sole')

    # Lead Leg (Left leg - heavily insulated pant, bent forward):
    # Thigh angled forward:
    front_thigh = [
        (28, 17, 23),
        (29, 16, 22),
        (30, 15, 21),
        (31, 14, 21),
        (32, 13, 20),
        (33, 12, 19),
    ]
    for y, x1, x2 in front_thigh:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'pant_light')
            elif x in (x1 + 1, x1 + 2):
                p(x, y, 'pant_mid')
            elif x == x2:
                p(x, y, 'pant_crease')
            else:
                p(x, y, 'pant_dark')

    # Lead Knee (BENT forward at x=11..18, y=34..36):
    front_knee = [
        (34, 11, 18),
        (35, 11, 18),
        (36, 11, 17),
    ]
    for y, x1, x2 in front_knee:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'pant_hi') # frost/highlight on lead knee
            elif x in (x1 + 1, x1 + 2):
                p(x, y, 'pant_light')
            elif x == x2:
                p(x, y, 'pant_crease')
            else:
                p(x, y, 'pant_dark')
    # Reinforced dark knee patch:
    p(12, 34, 'knee_patch'); p(13, 34, 'knee_patch'); p(14, 34, 'knee_patch')
    p(12, 35, 'knee_patch'); p(13, 35, 'knee_patch'); p(14, 35, 'knee_patch'); p(15, 35, 'knee_patch')
    p(12, 36, 'knee_patch'); p(13, 36, 'knee_patch'); p(14, 36, 'knee_patch')

    # Lead Shin / Calf (drops nearly vertically from bent knee to snow):
    front_shin = [
        (37, 11, 17),
        (38, 11, 17),
        (39, 10, 16),
        (40, 10, 16),
    ]
    for y, x1, x2 in front_shin:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'pant_light')
            elif x in (x1 + 1, x1 + 2):
                p(x, y, 'pant_mid')
            elif x == x2:
                p(x, y, 'pant_deep')
            else:
                p(x, y, 'pant_dark')

    # Lead Boot (Chunky Baffin/Bunny Boot kicking into snowdrift):
    p(10, 40, 'boot_light'); p(11, 40, 'boot_mid'); p(12, 40, 'boot_dark'); p(13, 40, 'boot_dark'); p(14, 40, 'boot_shadow')
    p(9, 41, 'boot_frost')
    p(10, 41, 'boot_light'); p(11, 41, 'boot_mid'); p(12, 41, 'boot_dark'); p(13, 41, 'boot_dark'); p(14, 41, 'boot_shadow'); p(15, 41, 'boot_deep'); p(16, 41, 'boot_deep')

    # Bulky rounded rubber toe:
    p(8, 42, 'boot_frost')
    p(9, 42, 'boot_light'); p(10, 42, 'boot_mid'); p(11, 42, 'boot_dark'); p(12, 42, 'boot_dark'); p(13, 42, 'boot_shadow'); p(14, 42, 'boot_deep'); p(15, 42, 'boot_deep'); p(16, 42, 'boot_deep')

    p(7, 43, 'boot_frost') # toe tip kicking into drift
    p(8, 43, 'boot_light'); p(9, 43, 'boot_mid'); p(10, 43, 'boot_dark'); p(11, 43, 'boot_dark'); p(12, 43, 'boot_shadow'); p(13, 43, 'boot_deep'); p(14, 43, 'boot_deep'); p(15, 43, 'boot_deep')

    # Deep lug tread:
    for x in range(7, 16):
        p(x, 44, 'boot_sole')
    p(9, 44, 'boot_deep'); p(12, 44, 'boot_deep')

    # -------------------------------------------------------------------------
    # 3. EXPEDITION PARKA TORSO (Angled forward into the gale!)
    # -------------------------------------------------------------------------
    torso_data = [
        (16, 14, 22),
        (17, 13, 23),
        (18, 12, 24),
        (19, 12, 24),
        (20, 13, 24),
        (21, 13, 24),
        (22, 14, 24),
        (23, 14, 25),
        (24, 15, 25),
        (25, 16, 25),
        (26, 17, 25),
        (27, 18, 25),
        (28, 19, 25),
    ]
    for y, x1, x2 in torso_data:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'parka_hi')
            elif x == x1 + 1:
                p(x, y, 'parka_bright')
            elif x in (x1 + 2, x1 + 3):
                p(x, y, 'parka_mid')
            elif x in (x2 - 1, x2):
                p(x, y, 'parka_deep')
            else:
                p(x, y, 'parka_dark')

    # Frost rim on windward front edge of chest:
    p(12, 18, 'parka_frost')
    p(12, 19, 'parka_frost')
    p(13, 20, 'parka_rim')
    p(13, 21, 'parka_rim')

    # 3M Scotchlite Reflective Safety Stripe across chest (y=21):
    for x in range(14, 20):
        p(x, 21, 'refl_mid')
    p(14, 21, 'refl_white')
    p(15, 21, 'refl_light')
    p(19, 21, 'refl_dark')

    # Center storm flap & dark zipper seam:
    for y in range(18, 28):
        p(17, y, 'parka_crease')
    # Storm flap snaps:
    p(16, 19, 'refl_light')
    p(16, 23, 'refl_light')

    # Lower hem reflective stripe:
    for x in range(18, 25):
        p(x, 27, 'refl_mid')
    p(18, 27, 'refl_white')
    p(19, 27, 'refl_light')
    p(24, 27, 'refl_dark')

    # Parka drawstrings whipping back in the wind:
    p(19, 26, 'refl_white')
    p(20, 26, 'refl_light')
    p(21, 26, 'refl_mid')
    p(22, 26, 'refl_dark')
    p(23, 26, 'parka_crease')

    # -------------------------------------------------------------------------
    # 4. FAR ARM (Shielding Face/Collar against stinging blizzard ice)
    # -------------------------------------------------------------------------
    # Shoulder & bicep in background:
    p(13, 17, 'parka_deep')
    p(12, 18, 'parka_shadow')
    p(11, 18, 'parka_dark')
    p(10, 19, 'parka_shadow')
    p(11, 19, 'parka_mid')
    # Forearm sleeve:
    p(11, 18, 'parka_bright')
    p(11, 17, 'refl_mid')
    p(12, 17, 'refl_white')
    # Thick mitten gripping collar / shielding face:
    p(10, 16, 'glove_frost')
    p(11, 16, 'glove_light')
    p(12, 16, 'glove_mid')
    p(13, 16, 'glove_dark')
    p(11, 15, 'glove_light')
    p(12, 15, 'glove_mid')
    p(13, 15, 'glove_dark')

    # -------------------------------------------------------------------------
    # 5. NEAR ARM & MITTEN (Carrying sample case with 3D depth separation!)
    # -------------------------------------------------------------------------
    # Shadow line along inner arm contour:
    p(18, 19, 'parka_crease')
    p(18, 20, 'parka_crease')
    p(19, 21, 'parka_crease')
    p(19, 22, 'parka_crease')
    p(20, 23, 'parka_crease')
    p(20, 24, 'parka_crease')
    p(21, 25, 'parka_crease')

    # Near Arm sleeve:
    near_arm = [
        (18, 19, 22),
        (19, 19, 23),
        (20, 20, 24),
        (21, 20, 24),
        (22, 21, 25),
        (23, 21, 25),
        (24, 22, 25),
        (25, 22, 25),
    ]
    for y, x1, x2 in near_arm:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'parka_bright')
            elif x == x1 + 1:
                p(x, y, 'parka_hi')
            elif x == x2:
                p(x, y, 'parka_deep')
            else:
                p(x, y, 'parka_mid')

    # Polar research expedition patch on shoulder (white circle with cyan globe):
    p(20, 18, 'refl_white')
    p(21, 18, 'refl_white')
    p(20, 19, 'gog_cyan')
    p(21, 19, 'refl_light')

    # Reflective band on sleeve (y=23):
    p(21, 23, 'refl_white')
    p(22, 23, 'refl_light')
    p(23, 23, 'refl_mid')
    p(24, 23, 'refl_dark')

    # Forearm cuff & Heavy Insulated Mitten gripping sample case:
    p(22, 25, 'glove_dark'); p(23, 25, 'glove_mid'); p(24, 25, 'glove_dark')
    # Mitten body gripping handle:
    p(22, 26, 'glove_dark'); p(23, 26, 'glove_mid'); p(24, 26, 'glove_light'); p(25, 26, 'glove_shadow')
    p(22, 27, 'glove_dark'); p(23, 27, 'glove_mid'); p(24, 27, 'glove_light'); p(25, 27, 'glove_shadow')
    # Thumb curled securely over handle:
    p(22, 28, 'glove_shadow'); p(23, 28, 'glove_mid'); p(24, 28, 'glove_light')

    # -------------------------------------------------------------------------
    # 6. RUGGED SCIENTIFIC SAMPLE CASE (Pelican/Storm Cryo Specimen Case)
    # -------------------------------------------------------------------------
    # Heavy rubberized top handle:
    p(23, 27, 'case_bumper')
    p(24, 27, 'case_bumper')
    p(25, 27, 'case_bumper')
    p(22, 28, 'case_bumper')
    p(26, 28, 'case_bumper')

    # Case body: x = 19 to 31, y = 29 to 37 (13 pixels wide, 9 pixels tall)
    for y in range(29, 38):
        for x in range(19, 32):
            if x in (19, 31) or y in (29, 37):
                p(x, y, 'case_bumper')
            else:
                p(x, y, 'case_mid')

    # Rounded shock-absorbing black rubber corner bumpers:
    # Top-left
    p(19, 29, 'case_bumper'); p(20, 29, 'case_bumper'); p(21, 29, 'case_bumper')
    p(19, 30, 'case_bumper'); p(20, 30, 'case_deep')
    # Top-right
    p(29, 29, 'case_bumper'); p(30, 29, 'case_bumper'); p(31, 29, 'case_bumper')
    p(30, 30, 'case_deep'); p(31, 30, 'case_bumper')
    # Bottom-left (rounded bumper)
    p(19, 36, 'case_bumper'); p(20, 36, 'case_deep')
    p(19, 37, 'case_bumper'); p(20, 37, 'case_bumper'); p(21, 37, 'case_bumper')
    # Bottom-right (rounded bumper)
    p(30, 36, 'case_deep'); p(31, 36, 'case_bumper')
    p(29, 37, 'case_bumper'); p(30, 37, 'case_bumper'); p(31, 37, 'case_bumper')

    # Shading across the case:
    # Windward top and left face (bright amber highlight & frost crust):
    for y in range(30, 36):
        p(20, y, 'case_hi')
        p(21, y, 'case_bright')
    p(19, 30, 'snow_white') # frost crust on windward corner
    p(19, 31, 'snow_mid')
    p(19, 32, 'snow_white')

    # Top face highlight:
    for x in range(21, 29):
        p(x, 30, 'case_hi')

    # Structural molded ridges (Pelican ribs):
    for y in range(30, 37):
        p(23, y, 'case_bright')
        p(27, y, 'case_bright')

    # Shadow side (bottom and right):
    for y in range(30, 37):
        p(29, y, 'case_dark')
        p(30, y, 'case_shadow')
    for x in range(20, 31):
        p(x, 36, 'case_shadow')

    # Weatherproof gasket / lid split line:
    for x in range(20, 31):
        p(x, 33, 'case_crease')

    # Dual stainless steel draw latches (clamped shut):
    # Latch 1 at x = 22
    p(22, 32, 'case_latch')
    p(22, 33, 'refl_white')
    p(22, 34, 'case_latch_dark')
    # Latch 2 at x = 28
    p(28, 32, 'case_latch')
    p(28, 33, 'refl_white')
    p(28, 34, 'case_latch_dark')

    # Digital Cryo Temperature / Specimen Integrity Display:
    # Shows active cryo containment (-70°C) with glowing mint LED:
    p(24, 31, 'case_screen_bg')
    p(25, 31, 'case_screen_led')
    p(26, 31, 'case_screen_led')
    p(24, 32, 'case_screen_bg')
    p(25, 32, 'case_screen_led')
    p(26, 32, 'case_screen_bg')

    # Hazard / cold specimen diagonal stripe on lower lid:
    p(24, 34, 'case_bumper'); p(25, 34, 'case_hi'); p(26, 34, 'case_bumper')
    p(24, 35, 'case_hi'); p(25, 35, 'case_bumper'); p(26, 35, 'case_hi')

    # -------------------------------------------------------------------------
    # 7. HEAD, HOOD & PALE BLUE GOGGLE REFLECTIONS (The Crown Jewel!)
    # -------------------------------------------------------------------------
    # Rounded hood dome (red parka fabric):
    hood_data = [
        (6, 16, 20),
        (7, 14, 22),
        (8, 13, 23),
        (9, 12, 24),
        (10, 11, 25),
        (11, 11, 25),
        (12, 12, 24),
        (13, 13, 24),
        (14, 14, 23),
        (15, 15, 23),
    ]
    for y, x1, x2 in hood_data:
        for x in range(x1, x2 + 1):
            if x == x1:
                p(x, y, 'parka_hi')
            elif x in (x1 + 1, x1 + 2):
                p(x, y, 'parka_bright')
            elif x in (x2 - 1, x2):
                p(x, y, 'parka_deep')
            else:
                p(x, y, 'parka_mid')

    # Coyote / Wolf Fur Ruff framing face, organically blown back by wind:
    fur_pixels = [
        # Windward front edge (compressed by wind, with frost tips):
        (9, 7, 'fur_frost'), (10, 7, 'fur_pale'), (11, 7, 'fur_light'),
        (8, 8, 'fur_frost'), (9, 8, 'fur_pale'), (10, 8, 'fur_light'), (11, 8, 'fur_mid'),
        (7, 9, 'fur_frost'), (8, 9, 'fur_pale'), (9, 9, 'fur_light'), (10, 9, 'fur_dark'),
        (7, 10, 'fur_frost'), (8, 10, 'fur_pale'), (9, 10, 'fur_light'), (10, 10, 'fur_shadow'),
        (8, 11, 'fur_frost'), (9, 11, 'fur_pale'), (10, 11, 'fur_light'),
        (8, 12, 'fur_pale'), (9, 12, 'fur_light'), (10, 12, 'fur_mid'),
        (9, 13, 'fur_frost'), (10, 13, 'fur_pale'), (11, 13, 'fur_light'),
        (10, 14, 'fur_pale'), (11, 14, 'fur_light'), (12, 14, 'fur_mid'),
        (11, 15, 'fur_frost'), (12, 15, 'fur_pale'), (13, 15, 'fur_light'), (14, 15, 'fur_shadow'),

        # Fur blown back over top of hood (y=5..6, x=14..23):
        (14, 5, 'fur_frost'), (15, 5, 'fur_pale'), (16, 5, 'fur_light'),
        (17, 5, 'fur_frost'), (18, 5, 'fur_pale'), (19, 5, 'fur_light'), (20, 5, 'fur_mid'),
        (21, 5, 'fur_pale'), (22, 6, 'fur_light'), (23, 6, 'fur_mid'), (24, 6, 'fur_dark'),
        (16, 6, 'fur_light'), (17, 6, 'fur_mid'), (18, 6, 'fur_light'),

        # Fur blown back under chin / collar (y=15..17, x=14..21):
        (14, 16, 'fur_mid'), (15, 16, 'fur_light'), (16, 16, 'fur_pale'), (17, 16, 'fur_frost'),
        (18, 16, 'fur_light'), (19, 16, 'fur_pale'), (20, 16, 'fur_frost'),
        (15, 17, 'fur_dark'), (16, 17, 'fur_mid'), (17, 17, 'fur_light'),
    ]
    for x, y, col in fur_pixels:
        p(x, y, col)

    # Dark neoprene balaclava / face mask covering lower face:
    mask_pixels = [
        (11, 13, 'mask_dark'), (12, 13, 'mask_mid'), (13, 13, 'mask_mid'), (14, 13, 'mask_dark'),
        (12, 14, 'mask_deep'), (13, 14, 'mask_dark'), (14, 14, 'mask_mid'), (15, 14, 'mask_dark'),
        (13, 15, 'mask_deep'), (14, 15, 'mask_dark'),
    ]
    for x, y, col in mask_pixels:
        p(x, y, col)

    # -------------------------------------------------------------------------
    # PALE BLUE GOGGLE REFLECTIONS (Glass Horizon Reflection)
    # -------------------------------------------------------------------------
    # Glacier goggle frame: rounded wraparound aerodynamic shape
    gog_frame = [
        (10, 10), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9), (16, 10),
        (10, 11), (16, 11),
        (10, 12), (11, 13), (12, 13), (13, 12), (14, 13), (15, 13), (16, 12),
    ]
    for x, y in gog_frame:
        p(x, y, 'gog_rim')

    # Goggle strap wrapping around hood:
    for x in range(17, 24):
        p(x, 10, 'gog_strap')
    p(20, 10, 'refl_mid') # buckle adjuster
    p(21, 10, 'refl_white')

    # Glassy Pale Blue Reflections on twin lenses:
    # Front lens (x=11..13, y=10..12), Rear lens (x=14..15, y=10..12)
    # Top row (10): Sky reflection with specular glint
    p(11, 10, 'gog_glint')       # Specular flare
    p(12, 10, 'gog_ice_white')   # Icy sky white
    p(13, 10, 'gog_pale')        # Pale cyan
    p(14, 10, 'gog_glint')       # Secondary glint
    p(15, 10, 'gog_ice_white')   # Icy sky white

    # Middle row (11): Horizon line flare (pure white and pale cyan)
    p(11, 11, 'gog_ice_white')   # Bright horizon reflection
    p(12, 11, 'gog_glint')       # Bright horizon flare
    p(13, 11, 'gog_pale')        # Pale cyan
    p(14, 11, 'gog_pale')        # Pale cyan
    p(15, 11, 'gog_cyan')        # Vibrant cyan

    # Bottom row (12): Shadowed ice landscape reflection
    p(11, 12, 'gog_pale')        # Lower rim
    p(12, 12, 'gog_cyan')        # Cyan
    p(13, 12, 'gog_mid_cyan')    # Deep cyan
    p(14, 12, 'gog_deep_cyan')   # Shadowed ice base
    p(15, 12, 'gog_mid_cyan')    # Deep cyan

    # Frost clinging to windward upper edge of goggle frame:
    p(10, 9, 'snow_white')
    p(11, 8, 'snow_mid')

    # -------------------------------------------------------------------------
    # 8. GROUND SNOWDRIFT & REFINED SPINDRIFT PARTICLES
    # -------------------------------------------------------------------------
    # Ground snowdrift packed under feet:
    ground_drift = [
        # Mound packed in front of lead boot:
        (4, 43, 'snow_white'), (5, 43, 'snow_white'), (6, 43, 'snow_mid'),
        (3, 44, 'snow_mid'), (4, 44, 'snow_white'), (5, 44, 'snow_white'), (6, 44, 'snow_mid'),
        (2, 45, 'snow_shadow'), (3, 45, 'snow_mid'), (4, 45, 'snow_white'), (5, 45, 'snow_white'), (6, 45, 'snow_mid'),
        # Ground crust under lead boot:
        (7, 45, 'snow_shadow'), (8, 45, 'snow_mid'), (9, 45, 'snow_white'), (10, 45, 'snow_mid'),
        (11, 45, 'snow_shadow'), (12, 45, 'snow_mid'), (13, 45, 'snow_white'), (14, 45, 'snow_mid'),
        (15, 45, 'snow_shadow'), (16, 45, 'snow_mid'), (17, 45, 'snow_shadow'),
        # Drift between boots:
        (18, 44, 'snow_shadow'), (19, 44, 'snow_mid'), (20, 44, 'snow_white'), (21, 44, 'snow_mid'),
        (22, 44, 'snow_shadow'), (23, 44, 'snow_mid'), (24, 44, 'snow_white'), (25, 44, 'snow_mid'),
        (26, 44, 'snow_shadow'),
        # Ground snow under rear boot:
        (27, 44, 'snow_mid'), (28, 44, 'snow_white'), (29, 44, 'snow_mid'), (30, 44, 'snow_shadow'),
        (31, 44, 'snow_mid'), (32, 44, 'snow_white'), (33, 44, 'snow_mid'), (34, 44, 'snow_shadow'),
        # Drift trailing off behind rear boot:
        (35, 43, 'snow_white'), (36, 43, 'snow_mid'),
        (35, 44, 'snow_white'), (36, 44, 'snow_mid'), (37, 44, 'snow_shadow'),
        (37, 45, 'snow_mid'), (38, 45, 'snow_shadow'),
    ]
    for x, y, col in ground_drift:
        p(x, y, col)

    # Fine wind-blown snow crystals streaming off feet/coat (1px fine spindrift):
    spindrift = [
        # Off lead boot & snow mound:
        (1, 42, 'snow_mid'), (2, 42, 'snow_white'),
        (2, 41, 'snow_shadow'),
        # Streaming past waist / case:
        (32, 33, 'snow_mid'), (33, 33, 'snow_white'),
        (36, 35, 'snow_mid'), (37, 35, 'snow_white'),
        # Whipping off hood:
        (1, 8, 'snow_mid'), (2, 8, 'snow_white'),
        (25, 5, 'snow_white'), (26, 5, 'snow_mid'),
    ]
    for x, y, col in spindrift:
        p(x, y, col)

    # Render into canvas
    for y in range(48):
        for x in range(48):
            if grid[y][x] is not None:
                c.set(x, y, grid[y][x])

    return c
