from pixelbench_api import new_canvas, view, finish

c = new_canvas(32, 32, name="scooter_final")

# Refined, harmonious color palette
P = {
    # Tires & Wheels
    'T_DARK': '#121316',      # Deep black rubber
    'T_MID': '#23262e',       # Tire tread shade
    'R_SHADOW': '#4a5260',    # Rim shadow
    'R_MID': '#828e9e',       # Alloy silver rim
    'R_BRIGHT': '#d2dbe5',    # Rim highlight
    'R_BOLT': '#ffffff',      # Axle center bolt chrome
    
    # Scooter Frame
    'F_BLACK': '#14171d',     # Frame deepest outline
    'F_DARK': '#22262f',      # Frame dark metal
    'F_MID': '#363d4a',       # Frame primary body metal
    'F_LIGHT': '#5a657a',     # Frame metallic highlight
    'F_DECK': '#2a2f3a',      # Grip tape surface
    
    # Neon Cyan Accent & Lights
    'A_CYAN': '#00f5d4',      # Neon cyan LED underglow
    'A_GLOW': '#70fff0',      # Soft glow
    'L_HOUSING': '#14171d',   # Headlight dark casing
    'L_LAMP': '#fffbe6',      # Bright warm headlight lens
    'L_BEAM': '#80deea',      # Luminous beam cyan
    'L_BEAM_FAINT': '#b2ebf2',# Soft outer beam
    'L_RED': '#ff0054',       # Red taillight LED
    'L_DARK_RED': '#8f002e',  # Taillight base
    'SPEEDO': '#00f5d4',      # Digital speedometer
    'GRIP': '#14171d',        # Rubber handlebar grip
    
    # Helmet - Sporty Sunshine Gold
    'H_LIGHT': '#fff3b0',     # Sun highlight
    'H_YELLOW': '#ffc300',    # Primary yellow
    'H_AMBER': '#f39c12',     # Amber midtone
    'H_ORANGE': '#d35400',    # Orange shadow
    'H_RIM': '#b23b00',       # Dark visor edge
    
    # Hair - Warm Chestnut
    'HAIR_LIGHT': '#965d48',  # Hair highlight
    'HAIR_MID': '#5e3826',    # Hair mid
    'HAIR_DARK': '#361d11',   # Hair shadow
    
    # Skin & Face
    'SKIN_LIGHT': '#ffe3d8',  # Face highlight
    'SKIN_MID': '#fbc4ab',    # Skin tone
    'SKIN_BLUSH': '#ff9e9e',  # Cute blush
    'SKIN_SHADOW': '#d98b6c', # Jaw / neck shadow
    'EYE': '#181e24',         # Pupil
    'SMILE': '#e76f51',       # Warm smile
    
    # Jacket - Cool Cyan / Cobalt Windbreaker
    'J_HIGHLIGHT': '#70d6ff', # Top highlight
    'J_LIGHT': '#38b6ff',     # Bright cyan
    'J_MID': '#0077b6',       # Primary cobalt blue
    'J_DARK': '#023e8a',      # Deep shadow
    'J_SHADOW': '#011c40',    # Creases
    
    # Backpack - Vibrant Coral Crimson
    'B_LIGHT': '#ff758f',     # Highlight
    'B_MID': '#e63946',       # Main crimson
    'B_DARK': '#9d0208',      # Deep crimson
    'B_ZIP': '#ffffff',       # White zipper / reflector
    
    # Pants - Modern Charcoal Denim
    'P_LIGHT': '#6c757d',     # Denim highlight
    'P_MID': '#495057',       # Mid slate
    'P_DARK': '#343a40',      # Dark denim
    'P_BLACK': '#1e222a',     # Shadow seam
    
    # Shoes - High-top Skate Sneakers
    'S_BODY': '#e63946',      # Red sneaker canvas
    'S_LACE': '#ffffff',      # White laces / star
    'S_TOE': '#dcdde1',       # Light toe cap
    'S_SOLE': '#b0b8c4',      # Rubber sole line
    'S_DARK': '#22252c',      # Dark heel / sole tread
}

def set_px(x, y, col_name):
    if 0 <= x < 32 and 0 <= y < 32:
        c.set(x, y, P[col_name])

# ==========================================
# 1. WHEELS (6x6 Circle, resting at ground y=29)
# ==========================================
def draw_wheel(x0, y0):
    # row 0 (y=24)
    for x in range(x0+1, x0+5):
        set_px(x, y0, 'T_DARK')
    # row 1 (y=25)
    set_px(x0, y0+1, 'T_DARK')
    set_px(x0+1, y0+1, 'T_MID')
    set_px(x0+2, y0+1, 'R_MID')
    set_px(x0+3, y0+1, 'R_MID')
    set_px(x0+4, y0+1, 'T_MID')
    set_px(x0+5, y0+1, 'T_DARK')
    # row 2 (y=26)
    set_px(x0, y0+2, 'T_DARK')
    set_px(x0+1, y0+2, 'R_MID')
    set_px(x0+2, y0+2, 'R_BRIGHT')
    set_px(x0+3, y0+2, 'R_BOLT')
    set_px(x0+4, y0+2, 'R_MID')
    set_px(x0+5, y0+2, 'T_DARK')
    # row 3 (y=27)
    set_px(x0, y0+3, 'T_DARK')
    set_px(x0+1, y0+3, 'R_MID')
    set_px(x0+2, y0+3, 'R_BRIGHT')
    set_px(x0+3, y0+3, 'R_BOLT')
    set_px(x0+4, y0+3, 'R_MID')
    set_px(x0+5, y0+3, 'T_DARK')
    # row 4 (y=28)
    set_px(x0, y0+4, 'T_DARK')
    set_px(x0+1, y0+4, 'T_MID')
    set_px(x0+2, y0+4, 'R_MID')
    set_px(x0+3, y0+4, 'R_MID')
    set_px(x0+4, y0+4, 'T_MID')
    set_px(x0+5, y0+4, 'T_DARK')
    # row 5 (y=29)
    for x in range(x0+1, x0+5):
        set_px(x, y0+5, 'T_DARK')

# Rear wheel at x=3..8, y=24..29
draw_wheel(3, 24)
# Front wheel at x=23..28, y=24..29
draw_wheel(23, 24)

# ==========================================
# 2. FENDERS & LIGHTS
# ==========================================
# Rear fender over rear wheel:
for x in range(3, 8):
    set_px(x, 23, 'F_DARK')
set_px(2, 23, 'L_RED')
set_px(2, 24, 'L_DARK_RED')
set_px(3, 24, 'F_MID')

# Front fender over front wheel:
for x in range(23, 28):
    set_px(x, 23, 'F_DARK')
set_px(24, 23, 'F_LIGHT')
# Fork arm to front axle:
set_px(24, 24, 'F_MID')
set_px(24, 25, 'F_LIGHT')

# ==========================================
# 3. DECK (Footboard)
# ==========================================
# y=25: Flat grip tape surface
for x in range(8, 23):
    set_px(x, 25, 'F_DECK')
# y=26: Glowing neon cyan LED underglow strip
for x in range(8, 22):
    set_px(x, 26, 'A_CYAN')
set_px(7, 26, 'F_BLACK')
set_px(22, 26, 'F_BLACK')
# y=27: Base plate / dark frame
for x in range(7, 23):
    set_px(x, 27, 'F_BLACK')

# ==========================================
# 4. STEERING STEM & CONTROLS
# ==========================================
stem_coords = [
    (22, 22), (23, 22),
    (21, 21), (22, 21),
    (21, 20), (22, 20),
    (20, 19), (21, 19),
    (20, 18), (21, 18),
    (19, 17), (20, 17),
    (19, 16), (20, 16),
    (18, 15), (19, 15),
    (18, 14), (19, 14),
]
for x, y in stem_coords:
    set_px(x, y, 'F_DARK')
# Metallic highlight along right edge:
for y in range(15, 23):
    xs = [x for x, sy in stem_coords if sy == y]
    if xs:
        set_px(max(xs), y, 'F_LIGHT')

# Handlebar crossbar at y=14:
for x in range(16, 21):
    set_px(x, 14, 'F_BLACK')
set_px(16, 14, 'GRIP')
set_px(20, 14, 'GRIP')

# Digital speedometer display:
set_px(19, 13, 'SPEEDO')

# Headlight:
set_px(20, 13, 'L_HOUSING')
set_px(21, 13, 'L_LAMP')
set_px(21, 14, 'L_HOUSING')
# Beam cone:
set_px(22, 13, 'L_BEAM')
set_px(23, 13, 'L_BEAM')
set_px(24, 13, 'L_BEAM_FAINT')
set_px(22, 14, 'L_BEAM')
set_px(23, 14, 'L_BEAM_FAINT')

# ==========================================
# 5. RIDER - SNEAKERS (Resting firmly on deck y=25)
# ==========================================
# Back sneaker: x=9..12
set_px(9, 24, 'S_DARK')
set_px(10, 24, 'S_SOLE')
set_px(11, 24, 'S_SOLE')
set_px(12, 24, 'S_TOE')

set_px(9, 23, 'S_DARK')
set_px(10, 23, 'S_BODY')
set_px(11, 23, 'S_LACE')
set_px(12, 23, 'S_TOE')

# Front sneaker: x=15..18
set_px(15, 24, 'S_DARK')
set_px(16, 24, 'S_SOLE')
set_px(17, 24, 'S_SOLE')
set_px(18, 24, 'S_TOE')

set_px(15, 23, 'S_DARK')
set_px(16, 23, 'S_BODY')
set_px(17, 23, 'S_LACE')
set_px(18, 23, 'S_TOE')

# ==========================================
# 6. RIDER - LEGS (PANTS)
# ==========================================
# Back leg:
set_px(10, 22, 'P_BLACK')
set_px(11, 22, 'P_MID')

set_px(10, 21, 'P_BLACK')
set_px(11, 21, 'P_MID')
set_px(12, 21, 'P_LIGHT')

set_px(11, 20, 'P_BLACK')
set_px(12, 20, 'P_MID')

# Front leg:
set_px(15, 22, 'P_MID')
set_px(16, 22, 'P_LIGHT')

set_px(14, 21, 'P_MID')
set_px(15, 21, 'P_LIGHT')
set_px(16, 21, 'P_LIGHT')

set_px(13, 20, 'P_MID')
set_px(14, 20, 'P_LIGHT')

# Hips (y=19):
set_px(11, 19, 'P_BLACK')
for x in range(12, 15):
    set_px(x, 19, 'P_MID')
set_px(14, 19, 'P_LIGHT')

# ==========================================
# 7. RIDER - TORSO & JACKET
# ==========================================
# Waist (y=18):
set_px(10, 18, 'J_SHADOW')
for x in range(11, 14):
    set_px(x, 18, 'J_MID')
set_px(14, 18, 'J_LIGHT')

# Lower torso (y=17):
set_px(10, 17, 'J_SHADOW')
set_px(11, 17, 'J_DARK')
for x in range(12, 14):
    set_px(x, 17, 'J_MID')
set_px(14, 17, 'J_LIGHT')
set_px(15, 17, 'J_LIGHT')

# Chest (y=16):
set_px(11, 16, 'J_SHADOW')
set_px(12, 16, 'J_DARK')
set_px(13, 16, 'J_MID')
set_px(14, 16, 'J_LIGHT')
set_px(15, 16, 'J_HIGHLIGHT')

# Shoulders (y=15):
set_px(11, 15, 'J_DARK')
set_px(12, 15, 'J_MID')
set_px(13, 15, 'J_LIGHT')
set_px(14, 15, 'J_HIGHLIGHT')
set_px(15, 15, 'J_LIGHT')

# ==========================================
# 8. RIDER - ARMS & HANDS
# ==========================================
set_px(15, 15, 'J_LIGHT')
set_px(16, 15, 'J_LIGHT')
set_px(16, 14, 'J_MID')
# Hands holding handlebar grips:
set_px(17, 14, 'SKIN_LIGHT')
set_px(17, 15, 'SKIN_SHADOW')
set_px(18, 14, 'SKIN_LIGHT')

# ==========================================
# 9. RIDER - BACKPACK
# ==========================================
for y in range(14, 19):
    set_px(8, y, 'B_MID')
    set_px(9, y, 'B_MID')
set_px(7, 15, 'B_MID')
set_px(7, 16, 'B_DARK')
set_px(7, 17, 'B_DARK')
set_px(8, 14, 'B_LIGHT')
set_px(9, 14, 'B_LIGHT')
set_px(8, 18, 'B_DARK')
set_px(9, 18, 'B_DARK')
# White reflective reflector:
set_px(8, 16, 'B_ZIP')
# Shoulder straps:
set_px(11, 15, 'B_MID')
set_px(12, 16, 'B_DARK')

# ==========================================
# 10. RIDER - HEAD, FACE & HAIR
# ==========================================
# Neck (y=13):
set_px(12, 13, 'SKIN_SHADOW')
set_px(13, 13, 'SKIN_MID')

# Chin & Jaw (y=12):
set_px(12, 12, 'HAIR_DARK')
set_px(13, 12, 'SKIN_SHADOW')
set_px(14, 12, 'SKIN_LIGHT')

# Mouth & Smile (y=11):
set_px(11, 11, 'HAIR_DARK')
set_px(12, 11, 'SKIN_SHADOW')
set_px(13, 11, 'SKIN_MID')
set_px(14, 11, 'SMILE')

# Nose & Cheeks (y=10):
set_px(11, 10, 'HAIR_DARK')
set_px(12, 10, 'SKIN_MID')
set_px(13, 10, 'SKIN_BLUSH')
set_px(14, 10, 'SKIN_LIGHT')
set_px(15, 10, 'SKIN_MID')

# Eyes & Forehead (y=9):
set_px(11, 9, 'HAIR_DARK')
set_px(12, 9, 'SKIN_MID')
set_px(13, 9, 'EYE')
set_px(14, 9, 'SKIN_LIGHT')

# Hair flowing backwards in the wind:
hair_flow = [
    (10, 8, 'HAIR_LIGHT'), (11, 8, 'HAIR_LIGHT'), (12, 8, 'HAIR_MID'),
    (8, 9, 'HAIR_LIGHT'), (9, 9, 'HAIR_MID'), (10, 9, 'HAIR_DARK'),
    (6, 10, 'HAIR_LIGHT'), (7, 10, 'HAIR_LIGHT'), (8, 10, 'HAIR_MID'), (9, 10, 'HAIR_DARK'),
    (5, 11, 'HAIR_LIGHT'), (6, 11, 'HAIR_MID'), (7, 11, 'HAIR_DARK'),
    (4, 12, 'HAIR_LIGHT'), (5, 12, 'HAIR_MID'),
]
for x, y, col in hair_flow:
    set_px(x, y, col)

# ==========================================
# 11. RIDER - HELMET
# ==========================================
# Top dome (y=4):
for x in range(10, 16):
    set_px(x, 4, 'H_LIGHT')

# Upper curve (y=5):
set_px(9, 5, 'H_LIGHT')
for x in range(10, 15):
    set_px(x, 5, 'H_YELLOW')
set_px(15, 5, 'H_AMBER')
set_px(16, 5, 'H_ORANGE')

# Lower dome (y=6):
set_px(8, 6, 'H_LIGHT')
for x in range(9, 14):
    set_px(x, 6, 'H_YELLOW')
set_px(14, 6, 'H_AMBER')
set_px(15, 6, 'H_ORANGE')
set_px(16, 6, 'H_ORANGE')
set_px(17, 6, 'H_RIM')

# Visor brim (y=7):
set_px(8, 7, 'H_YELLOW')
for x in range(9, 13):
    set_px(x, 7, 'H_AMBER')
for x in range(13, 16):
    set_px(x, 7, 'H_ORANGE')
set_px(16, 7, 'H_RIM')

view(c)
finish(c)
