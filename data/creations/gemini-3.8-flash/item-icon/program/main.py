from pixelbench_api import *
import math

def build_icon():
    c = new_canvas(32, 32, name="ancient_golden_compass")
    
    # -------------------------------------------------------------
    # COLOR PALETTE
    # -------------------------------------------------------------
    # Outlines
    OUTLINE     = "#0c0603"  # Deepest dark outline
    DARK_CREASE = "#221106"  # Inner bevel / recess shadow
    
    # Rich Antique Gold Ramp (9 tones)
    G_SPEC   = "#fffde8"  # Pure specular glare (white-gold)
    G_SHINE  = "#fef08a"  # Brilliant gold shine
    G_LIGHT  = "#facc15"  # Bright sunny gold
    G_BRIGHT = "#eab308"  # Saturated rich gold
    G_MID    = "#ca8a04"  # Warm golden amber
    G_DARK   = "#935f07"  # Deep bronze-gold
    G_SHADOW = "#5c3804"  # Dark bronze shadow
    G_DEEP   = "#3a2002"  # Crease shadow
    
    # Ancient Dial
    D_BG_DEEP = "#070c14"  # Midnight dark base
    D_BG      = "#0e1724"  # Dark navy slate dial face
    D_BG_LGT  = "#162334"  # Subtle dial sheen
    D_TRACK   = "#1f3148"  # Astronomical graduation ring
    D_TRACK_L = "#2d4462"  # Track highlight
    D_GLASS   = "#223b5c"  # Glass glare arc
    
    # Blue Crystal Center (Magical glowing sapphire, 8 tones)
    B_SPEC   = "#ffffff"  # Sparkle
    B_PALE   = "#d8f8ff"  # Top-left pale cyan facet
    B_CYAN   = "#38cff8"  # Electric cyan
    B_AZURE  = "#0ea5e9"  # Luminous azure
    B_ROYAL  = "#0284c7"  # Deep royal blue
    B_MID    = "#0369a1"  # Medium sapphire
    B_DEEP   = "#074a7a"  # Deep blue
    B_DARK   = "#06263f"  # Dark sapphire facet
    
    # Crystal Ambient Glow on Dial
    GLOW_CYAN = "#122c42"

    cx = 15.5
    cy = 16.5
    r_outer = 11.8

    # -------------------------------------------------------------
    # 1. MAIN CIRCULAR BODY & CASING
    # -------------------------------------------------------------
    for y in range(5, 29):
        for x in range(3, 29):
            dx = x - cx
            dy = y - cy
            d = math.hypot(dx, dy)
            
            if d <= r_outer:
                if d > 10.0:
                    c.set(x, y, OUTLINE)
                elif d > 7.7:
                    # Gold rim shading with directional light from top-left
                    light = -(dx*0.707 + dy*0.707) / d
                    if light > 0.65:
                        col = G_SPEC if d < 9.0 else G_SHINE
                    elif light > 0.25:
                        col = G_SHINE if d < 9.0 else G_LIGHT
                    elif light > -0.15:
                        col = G_LIGHT if d < 9.0 else G_BRIGHT
                    elif light > -0.55:
                        col = G_MID if d < 9.0 else G_DARK
                    else:
                        col = G_DARK if d < 9.0 else G_SHADOW
                    c.set(x, y, col)
                elif d > 7.0:
                    c.set(x, y, DARK_CREASE)
                else:
                    c.set(x, y, D_BG)

    # -------------------------------------------------------------
    # 2. TOP SUSPENSION RING & KNOB
    # -------------------------------------------------------------
    # Outer ring top outline:
    c.set(14, 0, OUTLINE); c.set(15, 0, OUTLINE); c.set(16, 0, OUTLINE); c.set(17, 0, OUTLINE)
    
    # Row 1: Outer corners + Top gold arched rim
    c.set(13, 1, OUTLINE); c.set(18, 1, OUTLINE)
    c.set(14, 1, G_SHINE); c.set(15, 1, G_SPEC); c.set(16, 1, G_SHINE); c.set(17, 1, G_LIGHT)
    
    # Row 2: Ring sides + top of inner hole outline
    c.set(12, 2, OUTLINE); c.set(19, 2, OUTLINE)
    c.set(13, 2, G_SPEC);  c.set(18, 2, G_MID)
    c.set(14, 2, OUTLINE); c.set(17, 2, OUTLINE)
    c.set(15, 2, None);    c.set(16, 2, None) # Hole top
    
    # Row 3: Ring sides + bottom of inner hole
    c.set(12, 3, OUTLINE); c.set(19, 3, OUTLINE)
    c.set(13, 3, G_LIGHT); c.set(18, 3, G_DARK)
    c.set(14, 3, OUTLINE); c.set(17, 3, OUTLINE)
    c.set(15, 3, None);    c.set(16, 3, None) # Hole bottom
    
    # Row 4: Inner bottom outline of hole + Knob top
    c.set(13, 4, OUTLINE); c.set(18, 4, OUTLINE)
    c.set(14, 4, G_LIGHT); c.set(17, 4, G_MID)
    c.set(15, 4, OUTLINE); c.set(16, 4, OUTLINE)
    
    # Row 5: Knob neck connecting to compass body
    c.set(13, 5, OUTLINE); c.set(18, 5, OUTLINE)
    c.set(14, 5, G_LIGHT); c.set(15, 5, G_SHINE); c.set(16, 5, G_MID); c.set(17, 5, G_DARK)

    # -------------------------------------------------------------
    # 3. DIAL TRACK & CARDINAL MARKINGS
    # -------------------------------------------------------------
    for y in range(9, 25):
        for x in range(8, 24):
            d = math.hypot(x - cx, y - cy)
            if 6.0 <= d <= 6.8:
                c.set(x, y, D_TRACK)

    # North Fleur-de-lis / Crown at y=8 on dial track
    c.set(15, 8, G_SPEC); c.set(16, 8, G_SHINE)

    # Cardinal gold pips on track (detached from needle tips)
    c.set(23, 16, G_MID); c.set(23, 17, G_DARK)   # East pip
    c.set(15, 24, G_MID); c.set(16, 24, G_DARK)   # South pip
    c.set(8, 16, G_SHINE); c.set(8, 17, G_LIGHT)  # West pip

    # Ordinal marks (NE, SE, SW, NW)
    c.set(20, 12, D_TRACK_L) # NE
    c.set(20, 21, D_TRACK_L) # SE
    c.set(11, 21, D_TRACK_L) # SW
    c.set(11, 12, D_TRACK_L) # NW

    # Subtle curved glass reflection across top-left dial
    glint_pixels = [(10, 14), (10, 15), (11, 13)]
    for gx, gy in glint_pixels:
        if c.get(gx, gy) == c.color(D_BG):
            c.set(gx, gy, D_GLASS)

    # -------------------------------------------------------------
    # 4. AMBIENT CRYSTAL GLOW ON DIAL
    # -------------------------------------------------------------
    for y in range(12, 22):
        for x in range(11, 21):
            d = math.hypot(x - cx, y - cy)
            if 3.4 <= d <= 5.0:
                if c.get(x, y) == c.color(D_BG):
                    c.set(x, y, GLOW_CYAN)

    # -------------------------------------------------------------
    # 5. FLOATING 8-POINT COMPASS ROSE (SHARP DETACHED NEEDLES)
    # -------------------------------------------------------------
    # North Needle (Sharp spearhead pointing at North Crown)
    # Row 10: Spearhead Tip
    c.set(15, 10, G_SPEC); c.set(16, 10, G_LIGHT)
    # Row 11: Spearhead Blade
    c.set(15, 11, G_SHINE); c.set(16, 11, G_MID)
    # Row 12: Spearhead Base / Shoulders
    c.set(14, 12, G_LIGHT); c.set(15, 12, G_BRIGHT); c.set(16, 12, G_DARK); c.set(17, 12, G_SHADOW)

    # South Needle (Sharp counter-pointer)
    # Row 19: Base / Shoulders
    c.set(14, 19, G_MID); c.set(15, 19, G_MID); c.set(16, 19, G_DARK); c.set(17, 19, G_SHADOW)
    # Row 20: Blade
    c.set(15, 20, G_DARK); c.set(16, 20, G_SHADOW)
    # Row 21: Tip
    c.set(15, 21, G_SHADOW); c.set(16, 21, G_DEEP)

    # West Needle (Points left)
    # Tip at x=10:
    c.set(10, 16, G_SPEC); c.set(10, 17, G_LIGHT)
    # Blade at x=11:
    c.set(11, 16, G_LIGHT); c.set(11, 17, G_MID)
    # Base at x=12:
    c.set(12, 15, G_LIGHT); c.set(12, 16, G_BRIGHT); c.set(12, 17, G_DARK); c.set(12, 18, G_SHADOW)

    # East Needle (Points right, with crisp top highlight & bottom shadow)
    # Base at x=19:
    c.set(19, 15, G_BRIGHT); c.set(19, 16, G_MID); c.set(19, 17, G_DARK); c.set(19, 18, G_SHADOW)
    # Blade at x=20:
    c.set(20, 16, G_MID); c.set(20, 17, G_SHADOW)
    # Tip at x=21:
    c.set(21, 16, G_MID); c.set(21, 17, G_DEEP)

    # Secondary diagonal points (NW, NE, SW, SE)
    c.set(12, 13, G_LIGHT); c.set(11, 13, G_SHINE) # NW
    c.set(19, 13, G_MID);   c.set(20, 13, G_DARK)  # NE
    c.set(12, 18, G_MID);   c.set(11, 18, G_DARK)  # SW
    c.set(19, 18, G_DARK);  c.set(20, 18, G_DEEP)  # SE

    # -------------------------------------------------------------
    # 6. CENTRAL BLUE CRYSTAL (Rounded multifaceted sapphire)
    # -------------------------------------------------------------
    # Golden Bezel setting holding the crystal:
    c.set(13, 14, G_SHINE) # Top-left gold prong
    c.set(18, 14, G_MID)   # Top-right gold prong
    c.set(13, 18, G_MID)   # Bottom-left gold prong
    c.set(18, 18, G_DARK)  # Bottom-right gold prong

    # Round 6x6 Gem Facet Layout:
    # Row 13: 15, 16
    c.set(15, 13, B_PALE)
    c.set(16, 13, B_CYAN)

    # Row 14: 14, 15, 16, 17
    c.set(14, 14, B_SPEC)  # Specular glint corner
    c.set(15, 14, B_PALE)
    c.set(16, 14, B_CYAN)
    c.set(17, 14, B_AZURE)

    # Row 15: 13, 14, 15, 16, 17, 18
    c.set(13, 15, B_CYAN)
    c.set(14, 15, B_SPEC)  # Secondary glint
    c.set(15, 15, B_PALE)
    c.set(16, 15, B_AZURE)
    c.set(17, 15, B_ROYAL)
    c.set(18, 15, B_MID)

    # Row 16: 13, 14, 15, 16, 17, 18
    c.set(13, 16, B_AZURE)
    c.set(14, 16, B_CYAN)
    c.set(15, 16, B_AZURE)
    c.set(16, 16, B_ROYAL)
    c.set(17, 16, B_MID)
    c.set(18, 16, B_DEEP)

    # Row 17: 14, 15, 16, 17
    c.set(14, 17, B_AZURE)
    c.set(15, 17, B_ROYAL)
    c.set(16, 17, B_MID)
    c.set(17, 17, B_DEEP)

    # Row 18: 15, 16
    c.set(15, 18, B_DEEP)
    c.set(16, 18, B_DARK)

    # -------------------------------------------------------------
    # 7. RIM POLISH & HIGHLIGHT ACCENTS
    # -------------------------------------------------------------
    # Specular rim shine top-left:
    c.set(8, 8, G_SPEC)
    c.set(9, 7, G_SPEC)
    c.set(10, 6, G_SPEC)
    c.set(7, 9, G_SPEC)
    c.set(6, 10, G_SPEC)

    # Warm ambient bounce light bottom-right rim:
    c.set(22, 24, G_MID)
    c.set(23, 23, G_MID)
    c.set(24, 22, G_MID)

    return c

icon = build_icon()
view(icon)
finish(icon)
