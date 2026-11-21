from pixelbench_api import *

# ==========================================
# COLOR PALETTE (Strict, cohesive, high-contrast)
# Total colors: ~26 colors (limit is 86)
# ==========================================
C_OUTLINE = "#1a0e08"        # Dark outline for silhouette and hair
C_SKIN_OUT = "#3a1610"       # Dark reddish-brown for skin outline and facial features
C_SKIN_SHADOW = "#cf7c5a"    # Skin shadow
C_SKIN_MID = "#f2a788"       # Skin midtone / shading
C_SKIN_LIGHT = "#fde2d2"     # Base bright skin
C_BLUSH = "#ee6a68"          # Cute pink blush
C_BLUSH_SOFT = "#fba4a0"     # Soft blush glow

# Hair: Warm Honey Chestnut / Golden Amber
C_HAIR_DEEP = "#281206"      # Deepest hair shadow
C_HAIR_SHADOW = "#72360e"    # Hair shadow
C_HAIR_MID = "#b86414"       # Hair mid-tone
C_HAIR_LIGHT = "#ea9423"     # Hair main vibrant warm color
C_HAIR_HL = "#fbc54c"        # Hair highlight
C_HAIR_SHINE = "#fff0a2"     # Hair specular shine

# Eyes: Royal Sapphire Blue
C_EYE_DARK = "#091726"       # Lash line / pupil
C_EYE_NAVY = "#103254"       # Deep iris shadow
C_EYE_BLUE = "#1f6fa8"       # Mid iris blue
C_EYE_CYAN = "#45b8ed"       # Lower iris bright reflection
C_WHITE = "#ffffff"          # Pure white specular
C_SCLERA = "#e2ecf5"         # Sclera base (soft tinted white)
C_SCLERA_SHADOW = "#b8cee0"  # Sclera upper shadow

# Outfit: Adventurer Navy Tunic & White Collar & Gold Pin
C_JACKET_OUT = "#0c1220"
C_JACKET_SHADOW = "#162842"
C_JACKET_MID = "#244670"
C_JACKET_LIGHT = "#3b689e"
C_COLLAR_SHADOW = "#c5c0b8"
C_COLLAR_WHITE = "#fbf9f4"
C_GOLD_DARK = "#8e630c"
C_GOLD_MID = "#d89e1a"
C_GOLD_LIGHT = "#fee04e"

# Emotion specials
C_ANGER_RED = "#e52222"
C_ANGER_DARK = "#6e0808"
C_SWEAT_OUT = "#124268"
C_SWEAT_BLUE = "#3ca2e0"
C_SWEAT_LIGHT = "#c2e8fa"
C_MOUTH_DARK = "#480e18"
C_MOUTH_RED = "#c83244"
C_TEETH_WHITE = "#ffffff"

def draw_character_base(c, ox, oy):
    """Draws back hair, neck, outfit, face base, and ears."""
    
    # ----------------------------------------------------
    # 1. Back Hair (soft layered hair behind ears and neck)
    # ----------------------------------------------------
    back_hair = [
        (13, 5, 7, 24, 26),
        (14, 4, 8, 23, 27),
        (15, 4, 8, 23, 27),
        (16, 4, 8, 23, 27),
        (17, 5, 8, 23, 26),
        (18, 5, 9, 22, 26),
        (19, 6, 9, 22, 25),
        (20, 6, 10, 21, 25),
        (21, 7, 10, 21, 24),
        (22, 8, 11, 20, 23),
    ]
    for y, xl0, xl1, xr0, xr1 in back_hair:
        for x in range(xl0, xl1 + 1):
            c.set(ox + x, oy + y, C_HAIR_SHADOW)
        for x in range(xr0, xr1 + 1):
            c.set(ox + x, oy + y, C_HAIR_SHADOW)
        c.set(ox + xl0, oy + y, C_OUTLINE)
        c.set(ox + xr1, oy + y, C_OUTLINE)

    # ----------------------------------------------------
    # 2. Shoulders & Outfit (y: 25 to 31)
    # ----------------------------------------------------
    jacket_rows = [
        (26, 9, 22),
        (27, 7, 24),
        (28, 5, 26),
        (29, 4, 27),
        (30, 3, 28),
        (31, 3, 28),
    ]
    for y, x0, x1 in jacket_rows:
        for x in range(x0, x1 + 1):
            c.set(ox + x, oy + y, C_JACKET_MID)
        c.set(ox + x0, oy + y, C_JACKET_OUT)
        c.set(ox + x1, oy + y, C_JACKET_OUT)

    # Bottom border
    for x in range(3, 29):
        c.set(ox + x, oy + 31, C_JACKET_OUT)

    # Jacket highlights and folds
    for y in range(28, 31):
        c.set(ox + 5, oy + y, C_JACKET_SHADOW)
        c.set(ox + 6, oy + y, C_JACKET_LIGHT)
        c.set(ox + 26, oy + y, C_JACKET_SHADOW)
        c.set(ox + 25, oy + y, C_JACKET_LIGHT)

    # ----------------------------------------------------
    # 3. Neck & Collar
    # ----------------------------------------------------
    for y in range(22, 27):
        for x in range(12, 20):
            c.set(ox + x, oy + y, C_SKIN_SHADOW)
    for y in range(23, 26):
        for x in range(14, 18):
            c.set(ox + x, oy + y, C_SKIN_MID)

    # White V-collar
    collar_pixels = [
        (26, 12, C_COLLAR_SHADOW), (26, 13, C_COLLAR_WHITE), (26, 18, C_COLLAR_WHITE), (26, 19, C_COLLAR_SHADOW),
        (27, 11, C_COLLAR_SHADOW), (27, 12, C_COLLAR_WHITE), (27, 13, C_COLLAR_WHITE),
        (27, 18, C_COLLAR_WHITE), (27, 19, C_COLLAR_WHITE), (27, 20, C_COLLAR_SHADOW),
        (28, 12, C_COLLAR_WHITE), (28, 13, C_COLLAR_SHADOW), (28, 14, C_COLLAR_WHITE),
        (28, 17, C_COLLAR_WHITE), (28, 18, C_COLLAR_SHADOW), (28, 19, C_COLLAR_WHITE),
        (29, 13, C_COLLAR_WHITE), (29, 14, C_COLLAR_SHADOW), (29, 17, C_COLLAR_SHADOW), (29, 18, C_COLLAR_WHITE),
        (30, 14, C_COLLAR_WHITE), (30, 17, C_COLLAR_WHITE),
    ]
    for y, x, col in collar_pixels:
        c.set(ox + x, oy + y, col)
        
    c.line(ox + 12, oy + 26, ox + 14, oy + 30, C_JACKET_OUT)
    c.line(ox + 19, oy + 26, ox + 17, oy + 30, C_JACKET_OUT)

    # Gold Brooch in center
    c.rect(ox + 15, oy + 27, 2, 2, C_GOLD_MID)
    c.set(ox + 15, oy + 27, C_GOLD_LIGHT)
    c.set(ox + 16, oy + 28, C_GOLD_DARK)
    c.set(ox + 14, oy + 27, C_JACKET_OUT)
    c.set(ox + 17, oy + 27, C_JACKET_OUT)
    c.set(ox + 14, oy + 28, C_JACKET_OUT)
    c.set(ox + 17, oy + 28, C_JACKET_OUT)
    c.set(ox + 15, oy + 29, C_JACKET_OUT)
    c.set(ox + 16, oy + 29, C_JACKET_OUT)

    # ----------------------------------------------------
    # 4. Face Base & Jawline
    # ----------------------------------------------------
    face_rows = [
        (8, 11, 20),
        (9, 10, 21),
        (10, 9, 22),
        (11, 8, 23),
        (12, 8, 23),
        (13, 7, 24),
        (14, 7, 24),
        (15, 7, 24),
        (16, 7, 24),
        (17, 7, 24),
        (18, 8, 23),
        (19, 9, 22),
        (20, 10, 21),
        (21, 11, 20),
        (22, 12, 19),
        (23, 13, 18),
        (24, 14, 17), # Chin tip at y=24
    ]
    for y, x0, x1 in face_rows:
        for x in range(x0, x1 + 1):
            c.set(ox + x, oy + y, C_SKIN_LIGHT)

    # Clean jawline outline
    jaw_outline = [
        (19, 7), (19, 24),
        (20, 8), (20, 23),
        (21, 9), (21, 22),
        (22, 10), (22, 21),
        (23, 11), (23, 20),
        (24, 12), (24, 19),
        (25, 13), (25, 14), (25, 15), (25, 16), (25, 17), (25, 18),
    ]
    for y, x in jaw_outline:
        c.set(ox + x, oy + y, C_SKIN_OUT)

    # Chin soft shading
    c.set(ox + 14, oy + 24, C_SKIN_MID)
    c.set(ox + 15, oy + 24, C_SKIN_MID)
    c.set(ox + 16, oy + 24, C_SKIN_MID)
    c.set(ox + 17, oy + 24, C_SKIN_MID)

    # Ears
    # Left Ear
    c.set(ox + 6, oy + 14, C_SKIN_OUT)
    c.set(ox + 5, oy + 15, C_SKIN_OUT)
    c.set(ox + 5, oy + 16, C_SKIN_OUT)
    c.set(ox + 6, oy + 17, C_SKIN_OUT)
    c.set(ox + 6, oy + 15, C_SKIN_MID)
    c.set(ox + 6, oy + 16, C_SKIN_SHADOW)
    # Right Ear
    c.set(ox + 25, oy + 14, C_SKIN_OUT)
    c.set(ox + 26, oy + 15, C_SKIN_OUT)
    c.set(ox + 26, oy + 16, C_SKIN_OUT)
    c.set(ox + 25, oy + 17, C_SKIN_OUT)
    c.set(ox + 25, oy + 15, C_SKIN_MID)
    c.set(ox + 25, oy + 16, C_SKIN_SHADOW)

    # Subtle anime nose
    c.set(ox + 15, oy + 18, C_SKIN_SHADOW)
    c.set(ox + 15, oy + 19, C_SKIN_OUT)

def draw_hair_front(c, ox, oy):
    """Draws natural rounded crown, dynamic layered tufts, bangs, and ahoge."""
    
    # ----------------------------------------------------
    # 1. Crown Base & Volume
    # ----------------------------------------------------
    crown_layers = [
        (3, 11, 20),
        (4, 9, 22),
        (5, 7, 24),
        (6, 5, 26),
        (7, 4, 27),
        (8, 4, 27),
    ]
    for y, x0, x1 in crown_layers:
        for x in range(x0, x1 + 1):
            c.set(ox + x, oy + y, C_HAIR_LIGHT)

    # Shading along top and sides
    for y, x0, x1 in crown_layers:
        c.set(ox + x0, oy + y, C_HAIR_MID)
        c.set(ox + x1, oy + y, C_HAIR_MID)
        c.set(ox + x0 + 1, oy + y, C_HAIR_MID)
        c.set(ox + x1 - 1, oy + y, C_HAIR_MID)

    # Natural curved hair highlights (soft halo shine)
    for x in range(11, 21):
        c.set(ox + x, oy + 4, C_HAIR_HL)
    for x in range(9, 23):
        c.set(ox + x, oy + 5, C_HAIR_HL)
    for x in range(13, 19):
        c.set(ox + x, oy + 4, C_HAIR_SHINE)
        c.set(ox + x, oy + 5, C_HAIR_SHINE)

    # Crown smooth outline
    crown_outline = [
        (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (2, 19),
        (3, 10), (3, 21),
        (4, 8), (4, 23),
        (5, 6), (5, 25),
        (6, 4), (6, 27),
        (7, 3), (7, 28),
        (8, 3), (8, 28),
    ]
    for y, x in crown_outline:
        c.set(ox + x, oy + y, C_OUTLINE)

    # Cute singular Ahoge / Cowlick at center
    ahoge_pixels = [
        (0, 16, C_OUTLINE),
        (1, 15, C_OUTLINE), (1, 16, C_HAIR_SHINE), (1, 17, C_OUTLINE),
        (2, 14, C_OUTLINE), (2, 15, C_HAIR_HL), (2, 16, C_HAIR_LIGHT),
    ]
    for y, x, col in ahoge_pixels:
        c.set(ox + x, oy + y, col)

    # ----------------------------------------------------
    # 2. Side Tufts / Locks (fluffy, curved, framing the face)
    # ----------------------------------------------------
    left_side = [
        (9, 2, 6),
        (10, 2, 6),
        (11, 2, 6),
        (12, 2, 6),
        (13, 3, 6),
        (14, 3, 6),
        (15, 2, 6),  # flare
        (16, 2, 6),
        (17, 3, 6),
        (18, 4, 6),
        (19, 4, 5),
    ]
    for y, x0, x1 in left_side:
        for x in range(x0, x1 + 1):
            c.set(ox + x, oy + y, C_HAIR_LIGHT)
        c.set(ox + x0, oy + y, C_OUTLINE)
        c.set(ox + x0 + 1, oy + y, C_HAIR_MID)
    # Left lock inner boundary & tip
    c.line(ox + 7, oy + 9, ox + 7, oy + 17, C_OUTLINE)
    c.set(ox + 6, oy + 18, C_OUTLINE)
    c.set(ox + 5, oy + 19, C_OUTLINE)
    c.set(ox + 4, oy + 20, C_OUTLINE)
    c.set(ox + 3, oy + 17, C_OUTLINE)

    right_side = [
        (9, 25, 29),
        (10, 25, 29),
        (11, 25, 29),
        (12, 25, 29),
        (13, 25, 28),
        (14, 25, 28),
        (15, 25, 29),  # flare
        (16, 25, 29),
        (17, 25, 28),
        (18, 25, 27),
        (19, 26, 27),
    ]
    for y, x0, x1 in right_side:
        for x in range(x0, x1 + 1):
            c.set(ox + x, oy + y, C_HAIR_LIGHT)
        c.set(ox + x1, oy + y, C_OUTLINE)
        c.set(ox + x1 - 1, oy + y, C_HAIR_MID)
    # Right lock inner boundary & tip
    c.line(ox + 24, oy + 9, ox + 24, oy + 17, C_OUTLINE)
    c.set(ox + 25, oy + 18, C_OUTLINE)
    c.set(ox + 26, oy + 19, C_OUTLINE)
    c.set(ox + 27, oy + 20, C_OUTLINE)
    c.set(ox + 28, oy + 17, C_OUTLINE)

    # ----------------------------------------------------
    # 3. Forehead Bangs (Natural anime locks with center V-strand)
    # ----------------------------------------------------
    # Hair base across row 8
    for x in range(7, 25):
        c.set(ox + x, oy + 8, C_HAIR_LIGHT)
    c.set(ox + 7, oy + 8, C_HAIR_MID)
    c.set(ox + 24, oy + 8, C_HAIR_MID)

    # Bangs row y=9:
    # Left lock: 7..10
    # Center strand: 14..17
    # Right lock: 21..24
    for x in range(7, 11):
        c.set(ox + x, oy + 9, C_HAIR_LIGHT)
    for x in range(14, 18):
        c.set(ox + x, oy + 9, C_HAIR_LIGHT)
    for x in range(21, 25):
        c.set(ox + x, oy + 9, C_HAIR_LIGHT)
    c.set(ox + 7, oy + 9, C_HAIR_MID)
    c.set(ox + 14, oy + 9, C_HAIR_MID)
    c.set(ox + 17, oy + 9, C_HAIR_MID)
    c.set(ox + 24, oy + 9, C_HAIR_MID)

    # Bangs row y=10:
    for x in range(7, 10):
        c.set(ox + x, oy + 10, C_HAIR_LIGHT)
    c.set(ox + 15, oy + 10, C_HAIR_LIGHT)
    c.set(ox + 16, oy + 10, C_HAIR_LIGHT)
    for x in range(22, 25):
        c.set(ox + x, oy + 10, C_HAIR_LIGHT)
    c.set(ox + 7, oy + 10, C_HAIR_MID)
    c.set(ox + 24, oy + 10, C_HAIR_MID)

    # Bangs row y=11 (tips):
    c.set(ox + 8, oy + 11, C_HAIR_LIGHT)
    c.set(ox + 15, oy + 11, C_HAIR_LIGHT)
    c.set(ox + 16, oy + 11, C_HAIR_MID)
    c.set(ox + 23, oy + 11, C_HAIR_LIGHT)

    # Clean Bangs Outlines:
    # Left lock outline
    c.set(ox + 11, oy + 8, C_OUTLINE)
    c.set(ox + 10, oy + 9, C_OUTLINE)
    c.set(ox + 9, oy + 10, C_OUTLINE)
    c.set(ox + 8, oy + 12, C_OUTLINE)
    c.set(ox + 7, oy + 11, C_OUTLINE)

    # Center strand outline
    c.set(ox + 13, oy + 8, C_OUTLINE)
    c.set(ox + 14, oy + 9, C_OUTLINE)
    c.set(ox + 14, oy + 10, C_OUTLINE)
    c.set(ox + 15, oy + 12, C_OUTLINE)
    c.set(ox + 16, oy + 12, C_OUTLINE)
    c.set(ox + 17, oy + 10, C_OUTLINE)
    c.set(ox + 17, oy + 9, C_OUTLINE)
    c.set(ox + 18, oy + 8, C_OUTLINE)

    # Right lock outline
    c.set(ox + 20, oy + 8, C_OUTLINE)
    c.set(ox + 21, oy + 9, C_OUTLINE)
    c.set(ox + 22, oy + 10, C_OUTLINE)
    c.set(ox + 23, oy + 12, C_OUTLINE)
    c.set(ox + 24, oy + 11, C_OUTLINE)

    # Forehead drop shadows under bangs
    c.set(ox + 11, oy + 9, C_SKIN_SHADOW)
    c.set(ox + 12, oy + 9, C_SKIN_SHADOW)
    c.set(ox + 13, oy + 9, C_SKIN_SHADOW)
    c.set(ox + 18, oy + 9, C_SKIN_SHADOW)
    c.set(ox + 19, oy + 9, C_SKIN_SHADOW)
    c.set(ox + 20, oy + 9, C_SKIN_SHADOW)
    c.set(ox + 10, oy + 10, C_SKIN_SHADOW)
    c.set(ox + 21, oy + 10, C_SKIN_SHADOW)

def draw_emotion(c, ox, oy, emotion):
    # Rosy Cheeks Blush (Base across all emotions)
    c.set(ox + 8, oy + 18, C_BLUSH_SOFT)
    c.set(ox + 9, oy + 18, C_BLUSH)
    c.set(ox + 10, oy + 18, C_BLUSH_SOFT)
    c.set(ox + 21, oy + 18, C_BLUSH_SOFT)
    c.set(ox + 22, oy + 18, C_BLUSH)
    c.set(ox + 23, oy + 18, C_BLUSH_SOFT)

    if emotion == "calm":
        # ----------------------------------------------------
        # CALM: Peaceful, composed, friendly forward gaze
        # ----------------------------------------------------
        # Relaxed Eyebrows at y=12 (clean horizontal gentle arch)
        c.line(ox + 10, oy + 12, ox + 13, oy + 12, C_OUTLINE)
        c.line(ox + 18, oy + 12, ox + 21, oy + 12, C_OUTLINE)

        # Eyes: Balanced forward gaze, perfect symmetry
        # Left Eye (x: 10..13)
        c.line(ox + 10, oy + 14, ox + 13, oy + 14, C_EYE_DARK)
        c.set(ox + 9, oy + 15, C_SKIN_OUT)
        # Sclera
        c.set(ox + 10, oy + 15, C_SCLERA_SHADOW)
        c.set(ox + 10, oy + 16, C_SCLERA)
        c.set(ox + 13, oy + 15, C_SCLERA_SHADOW)
        c.set(ox + 13, oy + 16, C_SCLERA)
        # Iris (x=11, 12)
        c.set(ox + 11, oy + 15, C_EYE_NAVY)
        c.set(ox + 12, oy + 15, C_EYE_DARK)
        c.set(ox + 11, oy + 16, C_EYE_BLUE)
        c.set(ox + 12, oy + 16, C_EYE_CYAN)
        # Specular shine
        c.set(ox + 11, oy + 15, C_WHITE)
        # Bottom lid
        c.set(ox + 11, oy + 17, C_SKIN_OUT)
        c.set(ox + 12, oy + 17, C_SKIN_OUT)

        # Right Eye (x: 18..21)
        c.line(ox + 18, oy + 14, ox + 21, oy + 14, C_EYE_DARK)
        c.set(ox + 22, oy + 15, C_SKIN_OUT)
        # Sclera
        c.set(ox + 18, oy + 15, C_SCLERA_SHADOW)
        c.set(ox + 18, oy + 16, C_SCLERA)
        c.set(ox + 21, oy + 15, C_SCLERA_SHADOW)
        c.set(ox + 21, oy + 16, C_SCLERA)
        # Iris (x=19, 20)
        c.set(ox + 19, oy + 15, C_EYE_NAVY)
        c.set(ox + 20, oy + 15, C_EYE_DARK)
        c.set(ox + 19, oy + 16, C_EYE_BLUE)
        c.set(ox + 20, oy + 16, C_EYE_CYAN)
        # Specular shine
        c.set(ox + 19, oy + 15, C_WHITE)
        # Bottom lid
        c.set(ox + 19, oy + 17, C_SKIN_OUT)
        c.set(ox + 20, oy + 17, C_SKIN_OUT)

        # Calm mouth: clean gentle resting smile at y=21
        c.set(ox + 14, oy + 21, C_SKIN_OUT)
        c.set(ox + 15, oy + 21, C_SKIN_OUT)
        c.set(ox + 16, oy + 21, C_SKIN_OUT)
        c.set(ox + 17, oy + 21, C_SKIN_OUT)
        # Lower lip soft accent
        c.set(ox + 15, oy + 22, C_SKIN_SHADOW)
        c.set(ox + 16, oy + 22, C_SKIN_SHADOW)

    elif emotion == "smiling":
        # ----------------------------------------------------
        # SMILING: Joyful happiness, curved smile eyes (^ ^), open laugh
        # ----------------------------------------------------
        # High curved happy eyebrows at y=11
        c.set(ox + 10, oy + 12, C_OUTLINE)
        c.set(ox + 11, oy + 11, C_OUTLINE)
        c.set(ox + 12, oy + 11, C_OUTLINE)
        c.set(ox + 13, oy + 12, C_OUTLINE)

        c.set(ox + 18, oy + 12, C_OUTLINE)
        c.set(ox + 19, oy + 11, C_OUTLINE)
        c.set(ox + 20, oy + 11, C_OUTLINE)
        c.set(ox + 21, oy + 12, C_OUTLINE)

        # Crisp, elegant smiling eye arches (^ ^)
        # Left eye
        c.set(ox + 9, oy + 16, C_EYE_DARK)
        c.set(ox + 10, oy + 15, C_EYE_DARK)
        c.set(ox + 11, oy + 14, C_EYE_DARK)
        c.set(ox + 12, oy + 14, C_EYE_DARK)
        c.set(ox + 13, oy + 15, C_EYE_DARK)
        c.set(ox + 14, oy + 16, C_EYE_DARK)
        c.set(ox + 9, oy + 15, C_EYE_DARK) # Eyelash flick

        # Right eye
        c.set(ox + 17, oy + 16, C_EYE_DARK)
        c.set(ox + 18, oy + 15, C_EYE_DARK)
        c.set(ox + 19, oy + 14, C_EYE_DARK)
        c.set(ox + 20, oy + 14, C_EYE_DARK)
        c.set(ox + 21, oy + 15, C_EYE_DARK)
        c.set(ox + 22, oy + 16, C_EYE_DARK)
        c.set(ox + 22, oy + 15, C_EYE_DARK) # Eyelash flick

        # Cheerful rosy blush with shiny specular dots
        c.rect(ox + 8, oy + 17, 3, 2, C_BLUSH)
        c.rect(ox + 21, oy + 17, 3, 2, C_BLUSH)
        c.set(ox + 9, oy + 17, C_WHITE)
        c.set(ox + 22, oy + 17, C_WHITE)

        # Open cheerful laughing mouth (showing teeth and tongue)
        c.line(ox + 13, oy + 20, ox + 18, oy + 20, C_SKIN_OUT)
        c.set(ox + 13, oy + 21, C_SKIN_OUT)
        c.set(ox + 18, oy + 21, C_SKIN_OUT)
        c.line(ox + 14, oy + 22, ox + 17, oy + 22, C_SKIN_OUT)

        # Inside mouth
        for x in range(14, 18):
            c.set(ox + x, oy + 21, C_TEETH_WHITE)
        c.set(ox + 15, oy + 22, C_MOUTH_RED)
        c.set(ox + 16, oy + 22, C_MOUTH_RED)

        # Joyful sparkle near cheek
        c.set(ox + 26, oy + 12, C_WHITE)
        c.set(ox + 26, oy + 11, C_GOLD_LIGHT)
        c.set(ox + 26, oy + 13, C_GOLD_LIGHT)
        c.set(ox + 25, oy + 12, C_GOLD_LIGHT)
        c.set(ox + 27, oy + 12, C_GOLD_LIGHT)

    elif emotion == "angry":
        # ----------------------------------------------------
        # ANGRY: Furrowed V-brows, fierce glare, gritted snarl, anger vein
        # ----------------------------------------------------
        # Steeply angled V-eyebrows slanting down to center
        c.set(ox + 9, oy + 11, C_OUTLINE)
        c.set(ox + 10, oy + 11, C_OUTLINE)
        c.set(ox + 11, oy + 12, C_OUTLINE)
        c.set(ox + 12, oy + 13, C_OUTLINE)
        c.set(ox + 13, oy + 14, C_OUTLINE)

        c.set(ox + 22, oy + 11, C_OUTLINE)
        c.set(ox + 21, oy + 11, C_OUTLINE)
        c.set(ox + 20, oy + 12, C_OUTLINE)
        c.set(ox + 19, oy + 13, C_OUTLINE)
        c.set(ox + 18, oy + 14, C_OUTLINE)

        # Eyes: Sharp angled fierce glare
        # Left eye
        c.set(ox + 9, oy + 14, C_EYE_DARK)
        c.set(ox + 10, oy + 14, C_EYE_DARK)
        c.set(ox + 11, oy + 15, C_EYE_DARK)
        c.set(ox + 12, oy + 15, C_EYE_DARK)
        c.set(ox + 13, oy + 15, C_EYE_DARK)
        # Sclera
        c.set(ox + 10, oy + 16, C_SCLERA)
        c.set(ox + 13, oy + 16, C_SCLERA)
        # Iris
        c.set(ox + 11, oy + 16, C_EYE_NAVY)
        c.set(ox + 12, oy + 16, C_EYE_BLUE)
        c.set(ox + 11, oy + 15, C_WHITE) # Small glint
        # Lower lid
        c.line(ox + 10, oy + 17, ox + 13, oy + 17, C_SKIN_OUT)

        # Right eye
        c.set(ox + 22, oy + 14, C_EYE_DARK)
        c.set(ox + 21, oy + 14, C_EYE_DARK)
        c.set(ox + 20, oy + 15, C_EYE_DARK)
        c.set(ox + 19, oy + 15, C_EYE_DARK)
        c.set(ox + 18, oy + 15, C_EYE_DARK)
        # Sclera
        c.set(ox + 18, oy + 16, C_SCLERA)
        c.set(ox + 21, oy + 16, C_SCLERA)
        # Iris
        c.set(ox + 19, oy + 16, C_EYE_NAVY)
        c.set(ox + 20, oy + 16, C_EYE_BLUE)
        c.set(ox + 19, oy + 15, C_WHITE) # Small glint
        # Lower lid
        c.line(ox + 18, oy + 17, ox + 21, oy + 17, C_SKIN_OUT)

        # Flushed angry blush across cheeks and nose
        c.line(ox + 12, oy + 18, ox + 19, oy + 18, C_BLUSH)
        c.set(ox + 15, oy + 19, C_ANGER_DARK)

        # Mouth: Fierce downturned snarling grimace
        c.set(ox + 13, oy + 21, C_SKIN_OUT)
        c.set(ox + 14, oy + 20, C_SKIN_OUT)
        c.set(ox + 15, oy + 20, C_SKIN_OUT)
        c.set(ox + 16, oy + 20, C_SKIN_OUT)
        c.set(ox + 17, oy + 20, C_SKIN_OUT)
        c.set(ox + 18, oy + 21, C_SKIN_OUT)
        c.line(ox + 14, oy + 22, ox + 17, oy + 22, C_SKIN_OUT)
        # Clenched teeth
        for x in range(14, 18):
            c.set(ox + x, oy + 21, C_TEETH_WHITE)
        c.set(ox + 15, oy + 21, C_COLLAR_SHADOW)
        c.set(ox + 16, oy + 21, C_COLLAR_SHADOW)

        # Anime Anger Cross/Vein on temple
        vein_pixels = [
            (8, 24, C_ANGER_RED), (9, 24, C_ANGER_RED), (10, 24, C_ANGER_RED), (11, 24, C_ANGER_RED),
            (8, 26, C_ANGER_RED), (9, 26, C_ANGER_RED), (10, 26, C_ANGER_RED), (11, 26, C_ANGER_RED),
            (9, 23, C_ANGER_RED), (9, 25, C_ANGER_RED), (9, 27, C_ANGER_RED),
            (11, 23, C_ANGER_RED), (11, 25, C_ANGER_RED), (11, 27, C_ANGER_RED),
        ]
        for y, x, col in vein_pixels:
            c.set(ox + x, oy + y, col)
        c.set(ox + 24, oy + 7, C_ANGER_DARK)
        c.set(ox + 26, oy + 7, C_ANGER_DARK)
        c.set(ox + 24, oy + 12, C_ANGER_DARK)
        c.set(ox + 26, oy + 12, C_ANGER_DARK)
        c.set(ox + 22, oy + 9, C_ANGER_DARK)
        c.set(ox + 28, oy + 9, C_ANGER_DARK)
        c.set(ox + 22, oy + 11, C_ANGER_DARK)
        c.set(ox + 28, oy + 11, C_ANGER_DARK)

    elif emotion == "surprised":
        # ----------------------------------------------------
        # SURPRISED: Arched high eyebrows, round wide eyes, gasp 'O' mouth, sweat drop
        # ----------------------------------------------------
        # High arched eyebrows up on forehead (y=10..11)
        c.set(ox + 10, oy + 11, C_OUTLINE)
        c.set(ox + 11, oy + 10, C_OUTLINE)
        c.set(ox + 12, oy + 10, C_OUTLINE)
        c.set(ox + 13, oy + 11, C_OUTLINE)

        c.set(ox + 18, oy + 11, C_OUTLINE)
        c.set(ox + 19, oy + 10, C_OUTLINE)
        c.set(ox + 20, oy + 10, C_OUTLINE)
        c.set(ox + 21, oy + 11, C_OUTLINE)

        # Wide round open eyes
        for side, ex in [("L", 10), ("R", 18)]:
            # Round upper lash
            c.set(ox + ex + 1, oy + 13, C_EYE_DARK)
            c.set(ox + ex + 2, oy + 13, C_EYE_DARK)
            c.set(ox + ex, oy + 14, C_EYE_DARK)
            c.set(ox + ex + 3, oy + 14, C_EYE_DARK)

            # Round lower lid
            c.set(ox + ex, oy + 17, C_SKIN_OUT)
            c.set(ox + ex + 3, oy + 17, C_SKIN_OUT)
            c.set(ox + ex + 1, oy + 18, C_SKIN_OUT)
            c.set(ox + ex + 2, oy + 18, C_SKIN_OUT)

            # White sclera filling inside
            for ey in range(14, 18):
                for eex in range(ex, ex + 4):
                    c.set(ox + eex, oy + ey, C_SCLERA)

            # Small shocked contracted pupil
            c.set(ox + ex + 1, oy + 15, C_EYE_NAVY)
            c.set(ox + ex + 2, oy + 15, C_EYE_NAVY)
            c.set(ox + ex + 1, oy + 16, C_EYE_BLUE)
            c.set(ox + ex + 2, oy + 16, C_EYE_CYAN)
            c.set(ox + ex + 1, oy + 15, C_WHITE)

        # Surprised Mouth: Clean rounded 'O' gasp at y=20..23
        c.set(ox + 15, oy + 20, C_SKIN_OUT)
        c.set(ox + 16, oy + 20, C_SKIN_OUT)
        c.set(ox + 14, oy + 21, C_SKIN_OUT)
        c.set(ox + 17, oy + 21, C_SKIN_OUT)
        c.set(ox + 14, oy + 22, C_SKIN_OUT)
        c.set(ox + 17, oy + 22, C_SKIN_OUT)
        c.set(ox + 15, oy + 23, C_SKIN_OUT)
        c.set(ox + 16, oy + 23, C_SKIN_OUT)

        # Dark inside of mouth + pink tongue
        c.set(ox + 15, oy + 21, C_MOUTH_DARK)
        c.set(ox + 16, oy + 21, C_MOUTH_DARK)
        c.set(ox + 15, oy + 22, C_MOUTH_RED)
        c.set(ox + 16, oy + 22, C_MOUTH_RED)

        # Anime Sweat Drop on temple
        sweat_pixels = [
            (9, 26, C_SWEAT_OUT),
            (10, 25, C_SWEAT_OUT), (10, 26, C_SWEAT_LIGHT), (10, 27, C_SWEAT_OUT),
            (11, 25, C_SWEAT_OUT), (11, 26, C_SWEAT_BLUE), (11, 27, C_SWEAT_OUT),
            (12, 26, C_SWEAT_OUT),
        ]
        for y, x, col in sweat_pixels:
            c.set(ox + x, oy + y, col)

def draw_portrait(c, ox, oy, emotion):
    draw_character_base(c, ox, oy)
    draw_hair_front(c, ox, oy)
    draw_emotion(c, ox, oy, emotion)

def main():
    c = new_canvas(64, 64, background=None, name="emotions")
    
    draw_portrait(c, 0, 0, "calm")
    draw_portrait(c, 32, 0, "smiling")
    draw_portrait(c, 0, 32, "angry")
    draw_portrait(c, 32, 32, "surprised")

    view(c)
    finish(c)

main()
