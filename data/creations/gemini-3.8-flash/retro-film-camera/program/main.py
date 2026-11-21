import sys
import math
from pixelbench_api import new_canvas, view, finish, save

def make_camera():
    c = new_canvas(32, 32)
    
    # --- COLOR PALETTE ---
    # Dark Outlines
    O = "#12141a"       # Main dark outline
    
    # Chrome / Silver
    W = "#ffffff"       # Specular highlight
    S1 = "#f1f5f9"      # Bright silver
    S2 = "#d5dce6"      # Light silver
    S3 = "#9ba7b7"      # Mid silver
    S4 = "#687385"      # Shadow silver
    S5 = "#454d5a"      # Dark steel
    
    # Vintage Warm Brown Leatherette
    L_HI = "#784d39"    # Highlight pebble
    L_LIGHT = "#5e3a2b" # Light leather
    L_BASE = "#46291d"  # Base leather
    L_DARK = "#321c13"  # Dark leather
    L_DEEP = "#20110b"  # Deep shadow / occlusion
    
    # Lens Barrel Metal & Grooves
    B_LIGHT = "#758092" # Barrel light
    B_MID = "#485060"   # Barrel mid
    B_DARK = "#282e38"  # Barrel dark
    B_DEEP = "#161920"  # Barrel deep groove
    
    # Lens Glass & Reflections
    G_CYAN_HI = "#cffafe" # Bright cyan glint
    G_CYAN = "#38bdf8"    # Sky cyan reflection
    G_BLUE = "#1d4ed8"    # Cobalt blue reflection
    G_NAVY = "#0f172a"    # Deep dark navy glass
    G_BLACK = "#060911"   # Deep aperture core
    
    # Multi-coating flare (vintage Carl Zeiss / Leica magenta-violet)
    G_PINK = "#f472b6"
    G_MAG = "#c026d3"
    G_PURP = "#581c87"
    
    # Camera Accents
    RED_HI = "#ef4444"
    RED_MID = "#dc2626"
    RED_DARK = "#991b1b"
    
    VF_FRAME = "#1e293b"
    VF_GLASS = "#38bdf8"
    VF_SHINE = "#e0f2fe"

    # ==========================================
    # 1. BASE BODY & SURFACES
    # ==========================================
    # Leather body: y=13 to 24, x=4 to 27
    for y in range(13, 25):
        for x in range(4, 28):
            pattern = (x * 7 + y * 13) % 11
            if pattern == 0:
                col = L_HI
            elif pattern in (1, 2, 3):
                col = L_LIGHT
            elif pattern in (4, 5, 6, 7):
                col = L_BASE
            else:
                col = L_DARK
            c.set(x, y, col)
            
    # Ambient edge shadows on leather
    for y in range(13, 25):
        c.set(4, y, L_DEEP)
        c.set(5, y, L_DARK)
        c.set(26, y, L_DARK)
        c.set(27, y, L_DEEP)
    for x in range(4, 28):
        c.set(x, 13, L_DEEP)
        c.set(x, 24, L_DEEP)

    # Top Metal Plate: y=9 to 12, x=4 to 27
    c.rect(4, 9, 24, 1, S2)
    c.line(5, 9, 9, 9, W) # specular line
    c.rect(4, 10, 24, 1, S1)
    c.rect(4, 11, 24, 1, S2)
    c.rect(4, 12, 24, 1, S3)
    c.line(4, 9, 4, 12, S4)
    c.line(27, 9, 27, 12, S5)
    c.line(26, 10, 26, 12, S4)

    # Bottom Metal Baseplate: y=25 to 26, x=4 to 27
    c.rect(4, 25, 24, 1, S2)
    c.line(5, 25, 9, 25, W) # specular line
    c.rect(4, 26, 24, 1, S3)
    c.line(4, 25, 4, 26, S4)
    c.line(27, 25, 27, 26, S5)

    # ==========================================
    # 2. DETAILS ON BODY
    # ==========================================
    # Viewfinder window: x=6..9, y=10..12
    c.rect(6, 10, 4, 3, VF_FRAME)
    c.rect(7, 10, 2, 2, VF_GLASS)
    c.set(7, 10, VF_SHINE)
    c.set(8, 11, G_NAVY)
    
    # Leica-style red logo badge: x=11..12, y=10..11
    c.set(11, 10, RED_HI)
    c.set(12, 10, RED_MID)
    c.set(11, 11, RED_MID)
    c.set(12, 11, RED_DARK)
    
    # Rangefinder window: x=21..23, y=10..11
    c.rect(21, 10, 3, 2, VF_FRAME)
    c.set(22, 10, VF_SHINE)
    c.set(22, 11, VF_GLASS)
    c.set(23, 11, G_NAVY)

    # Self-timer lever on front leather: x=7, y=16..19
    c.set(7, 16, W) # silver pivot knob
    c.line(7, 17, 7, 19, S3)
    c.set(7, 19, S2) # bottom handle
    c.line(8, 16, 8, 19, L_DEEP) # drop shadow

    # Lens release button: x=24, y=16
    c.set(24, 16, S1)
    c.set(24, 17, S4)

    # Strap lugs on sides
    # Left lug: x=2..3, y=16..17
    c.set(2, 16, O); c.set(2, 17, O)
    c.set(3, 15, O); c.set(3, 18, O)
    c.set(3, 16, S2); c.set(3, 17, S4)
    
    # Right lug: x=28..29, y=16..17
    c.set(29, 16, O); c.set(29, 17, O)
    c.set(28, 15, O); c.set(28, 18, O)
    c.set(28, 16, S3); c.set(28, 17, S5)

    # ==========================================
    # 3. TOP CONTROLS & MECHANICAL DIALS
    # ==========================================
    # Film rewind crank (left, x=6..9, y=6..8)
    c.line(6, 6, 9, 6, O)
    c.set(5, 7, O); c.set(5, 8, O)
    c.set(10, 7, O); c.set(10, 8, O)
    c.rect(6, 7, 4, 2, S3)
    c.set(6, 7, S2); c.set(7, 7, W); c.set(8, 7, S1); c.set(9, 7, S4)
    c.set(6, 8, S4); c.set(7, 8, S3); c.set(8, 8, S4); c.set(9, 8, S5)

    # Hot shoe / flash mount (center, x=14..17, y=6..8)
    c.line(14, 6, 17, 6, O)
    c.rect(14, 7, 4, 2, S3)
    c.set(14, 7, S1); c.set(17, 7, S4)
    c.rect(15, 7, 2, 2, G_BLACK)
    c.set(15, 8, S5)

    # Shutter speed dial (x=19..21, y=7..8)
    c.line(19, 6, 21, 6, O)
    c.set(18, 7, O); c.set(18, 8, O)
    c.rect(19, 7, 3, 2, S3)
    c.set(19, 7, S1); c.set(20, 7, S2); c.set(21, 7, S4)
    c.set(20, 8, G_BLACK)

    # Prominent Mechanical SHUTTER BUTTON (x=23..25, y=5..8)
    # Silver knurled collar (y=7..8)
    c.rect(23, 7, 3, 2, S3)
    c.set(23, 7, S1); c.set(24, 7, W); c.set(25, 7, S4)
    c.set(23, 8, S3); c.set(24, 8, S2); c.set(25, 8, S5)
    c.set(22, 7, O); c.set(22, 8, O)
    
    # Red soft-release button head (y=5..6, x=23..25)
    c.line(23, 4, 25, 4, O)
    c.set(22, 5, O); c.set(22, 6, O)
    c.set(26, 5, O); c.set(26, 6, O)
    c.rect(23, 5, 3, 2, RED_MID)
    c.set(23, 5, RED_HI); c.set(24, 5, W) # center threaded release glint
    c.set(25, 5, RED_DARK); c.set(25, 6, RED_DARK)

    # Film advance lever (behind shutter button, x=26..27, y=7..8)
    c.set(26, 7, S2); c.set(27, 7, S3)
    c.set(26, 8, S4); c.set(27, 8, S5)
    c.set(26, 6, O); c.set(27, 6, O)
    c.set(28, 7, O); c.set(28, 8, O)

    # Outer camera body dark outline:
    c.line(4, 8, 5, 8, O)
    c.line(10, 8, 13, 8, O)
    c.set(18, 8, O); c.set(22, 8, O)
    c.set(3, 9, O); c.line(3, 10, 3, 14, O); c.line(3, 19, 3, 25, O); c.set(3, 26, O)
    c.set(28, 9, O); c.line(28, 10, 28, 14, O); c.line(28, 19, 28, 25, O); c.set(28, 26, O)
    c.line(4, 27, 27, 27, O)

    # ==========================================
    # 4. THE CIRCULAR RETRO LENS
    # ==========================================
    # 14x14 circular geometry (x=9..22, y=12..25)
    circle_14 = [
        (12, 14, 17), # 4 px
        (13, 12, 19), # 8 px
        (14, 11, 20), # 10 px
        (15, 10, 21), # 12 px
        (16, 10, 21), # 12 px
        (17,  9, 22), # 14 px
        (18,  9, 22), # 14 px
        (19,  9, 22), # 14 px
        (20,  9, 22), # 14 px
        (21, 10, 21), # 12 px
        (22, 10, 21), # 12 px
        (23, 11, 20), # 10 px
        (24, 12, 19), # 8 px
        (25, 14, 17), # 4 px
    ]

    # Ambient drop shadow around the lens onto leather
    lens_ao = [
        (13, 11), (18, 11),
        (11, 12), (20, 12),
        (10, 13), (21, 13),
        (9, 14), (22, 14),
        (8, 15), (23, 15),
        (8, 16), (23, 16),
        (7, 17), (24, 17),
        (7, 18), (24, 18),
        (7, 19), (24, 19),
        (7, 20), (24, 20),
        (8, 21), (23, 21),
        (8, 22), (23, 22),
        (9, 23), (22, 23),
        (10, 24), (21, 24),
        (11, 25), (20, 25),
        (13, 26), (18, 26),
    ]
    for ax, ay in lens_ao:
        if 4 <= ax <= 27 and 13 <= ay <= 24:
            c.set(ax, ay, L_DEEP)

    # Base fill: B_DARK
    for y, x0, x1 in circle_14:
        for x in range(x0, x1 + 1):
            c.set(x, y, B_DARK)

    # Layer 1: Outer focus ring bevel
    # Top rim: subtle silver sheen (row 12)
    c.set(14, 12, S2); c.set(15, 12, S1); c.set(16, 12, S2); c.set(17, 12, S3)
    # Row 13 corners
    c.set(12, 13, S2); c.set(13, 13, B_DEEP); c.set(18, 13, B_MID); c.set(19, 13, B_DARK)
    # Row 14 corners
    c.set(11, 14, S2); c.set(20, 14, B_DEEP)
    # Row 15 & 16 corners
    c.set(10, 15, S2); c.set(21, 15, B_DEEP)
    c.set(10, 16, S2); c.set(21, 16, B_DEEP)
    # Row 17..20 sides
    c.set(9, 17, S1); c.set(22, 17, B_DEEP)
    c.set(9, 18, S1); c.set(22, 18, B_DEEP)
    c.set(9, 19, S2); c.set(22, 19, B_DEEP)
    c.set(9, 20, S3); c.set(22, 20, B_DEEP)
    # Bottom arcs
    c.set(10, 21, S4); c.set(21, 21, B_DEEP)
    c.set(10, 22, S5); c.set(21, 22, B_DEEP)
    c.set(11, 23, B_MID); c.set(20, 23, B_DEEP)
    c.set(12, 24, B_MID); c.set(13, 24, B_DEEP); c.set(18, 24, B_DEEP); c.set(19, 24, B_DEEP)
    c.line(14, 25, 17, 25, B_DEEP)

    # Layer 2: Inner stepped chrome ring (12x12)
    # A crisp circular metallic ridge
    c.line(14, 13, 17, 13, S2)
    c.set(15, 13, W) # small specular glint
    c.set(12, 14, S1); c.set(13, 14, S2); c.set(18, 14, S4); c.set(19, 14, S5)
    c.set(11, 15, S1); c.set(20, 15, S5)
    c.set(11, 16, S1); c.set(20, 16, S5)
    c.set(10, 17, S1); c.set(21, 17, B_DEEP)
    c.set(10, 18, S2); c.set(21, 18, B_DEEP)
    c.set(10, 19, S2); c.set(21, 19, B_DEEP)
    c.set(10, 20, S3); c.set(21, 20, B_DEEP)
    c.set(11, 21, S4); c.set(20, 21, B_DEEP)
    c.set(11, 22, S5); c.set(20, 22, B_DEEP)
    c.set(12, 23, S5); c.set(13, 23, B_DEEP); c.set(18, 23, B_DEEP); c.set(19, 23, B_DEEP)
    c.line(14, 24, 17, 24, B_DEEP)

    # Layer 3: Glass element (10x10 disc)
    glass_10 = [
        (14, 14, 17),
        (15, 13, 18),
        (16, 12, 19),
        (17, 11, 20),
        (18, 11, 20),
        (19, 11, 20),
        (20, 11, 20),
        (21, 12, 19),
        (22, 13, 18),
        (23, 14, 17),
    ]
    for y, x0, x1 in glass_10:
        for x in range(x0, x1 + 1):
            c.set(x, y, G_NAVY)

    # Aperture core / deep pupil
    c.rect(14, 17, 4, 4, G_BLACK)
    c.rect(15, 18, 2, 2, "#000000")

    # Layer 4: Precision optical glass reflections
    # Curved crescent gleam in top-left
    c.set(14, 15, W)
    c.set(15, 15, G_CYAN_HI)
    c.set(16, 15, G_CYAN)
    
    c.set(13, 16, W)
    c.set(14, 16, G_CYAN_HI)
    c.set(15, 16, G_CYAN)
    
    c.set(12, 17, G_CYAN_HI)
    c.set(13, 17, G_CYAN)
    
    c.set(12, 18, G_CYAN)
    c.set(13, 18, G_BLUE)
    
    c.set(12, 19, G_BLUE)

    # Multi-coating flare (vintage Zeiss magenta/purple flare on bottom-right)
    c.set(19, 19, G_PURP)
    c.set(18, 20, G_PURP); c.set(19, 20, G_MAG)
    c.set(16, 21, G_PURP); c.set(17, 21, G_MAG); c.set(18, 21, G_PINK)
    c.set(15, 22, G_PURP); c.set(16, 22, G_MAG)

    # Layer 5: Clean 1-pixel dark outline around 14x14 lens circle
    lens_outline = [
        (11, 14, 17),           # 4 px top
        (12, [12, 13, 18, 19]), # 2 px each side
        (13, [11, 20]),         # 1 px each
        (14, [10, 21]),         # 1 px each
        (15, [9, 22]),          # 1 px each
        (16, [9, 22]),          # 1 px each
        (17, [8, 23]),          # 1 px each (vertical run of 4)
        (18, [8, 23]),
        (19, [8, 23]),
        (20, [8, 23]),
        (21, [9, 22]),          # 1 px each
        (22, [9, 22]),          # 1 px each
        (23, [10, 21]),         # 1 px each
        (24, [11, 20]),         # 1 px each
        (25, [12, 13, 18, 19]), # 2 px each side
        (26, 14, 17),           # 4 px bottom
    ]
    for item in lens_outline:
        if len(item) == 3:
            y, x0, x1 = item
            for x in range(x0, x1 + 1):
                c.set(x, y, O)
        else:
            y, xs = item
            for x in xs:
                c.set(x, y, O)

    return c

c = make_camera()
view(c)
finish(c)
