import sys
from pixelbench_api import *

def build_workbench():
    c = new_canvas(64, 64, name="workbench")
    
    # ----------------------------------------------------
    # Unified Curated Palette (Strictly <= 50 colors)
    # ----------------------------------------------------
    # Wall & Tiles
    C_TILE_LGT    = "#dce6eb"
    C_TILE_LINE   = "#b5c4cb"
    C_WALL_SHAD   = "#96a7b0"
    
    # Utility trunking
    C_UTIL_BG     = "#8597a3"
    C_UTIL_HIGH   = "#abbbc6"
    C_UTIL_LINE   = "#667580"
    
    # Benchtop (black/dark charcoal epoxy resin)
    C_BENCH_HIGH  = "#3b424f"
    C_BENCH_SURF  = "#252a34"
    C_BENCH_MID   = "#1e222b"
    C_BENCH_DARK  = "#14171d"
    C_BENCH_BEVEL = "#515a6b"
    C_BENCH_EDGE  = "#101216"
    
    # Wood (Cabinet drawers & Test tube rack share this palette)
    C_WOOD_LGT    = "#dca76a"
    C_WOOD_MID    = "#b47c40"
    C_WOOD_DRK    = "#7a4e22"
    C_WOOD_DEEP   = "#492d11"
    
    # Whites & Greys (Microscope, metals, labels, notebook)
    C_WHITE       = "#ffffff"
    C_OFFWHITE    = "#f3f6f9"
    C_GREY_LGT    = "#ced7df"
    C_GREY_MID    = "#929ea9"
    C_GREY_DRK    = "#4f5864"
    C_GREY_BLACK  = "#22262d"
    C_BLACK       = "#111317"
    
    # Glass tones
    C_GLASS_HI    = "#edf7fb"
    C_GLASS_LGT   = "#bcdde8"
    C_GLASS_MID   = "#7fa7bb"
    C_GLASS_DRK   = "#4a6f81"
    
    # Amber Glass
    C_AMBER_HI    = "#e28638"
    C_AMBER_MID   = "#994518"
    C_AMBER_DRK   = "#512108"
    
    # Accent Colors:
    # Blue
    C_BLUE_HI     = "#56ccf2"
    C_BLUE_MID    = "#1890ff"
    C_BLUE_DRK    = "#0050b3"
    
    # Red
    C_RED_HI      = "#ff6b81"
    C_RED_MID     = "#e63946"
    C_RED_DRK     = "#8c1320"
    
    # Yellow / Orange
    C_YEL_HI      = "#ffd166"
    C_YEL_MID     = "#f39c12"
    C_YEL_DRK     = "#b86400"
    
    # Green / Teal
    C_GRN_HI      = "#52b788"
    C_GRN_MID     = "#2a9d8f"
    C_GRN_DRK     = "#194d3e"
    
    # Specimen stain
    C_PURPLE      = "#ab47bc"

    # ====================================================
    # 1. BACKGROUND & ENVIRONMENT
    # ====================================================
    # Wall background tiles
    c.rect(0, 0, 64, 16, C_TILE_LGT)
    # Horizontal grout lines
    for y in [5, 11, 16]:
        c.line(0, y, 63, y, C_TILE_LINE)
    # Staggered vertical grout lines
    for x in range(0, 64, 12):
        c.line(x, 0, x, 5, C_TILE_LINE)
        c.line((x + 6) % 64, 6, (x + 6) % 64, 11, C_TILE_LINE)
        c.line(x, 12, x, 15, C_TILE_LINE)
        
    # Wall Reagent Shelf (x=24..63, y=2..5)
    c.line(24, 2, 63, 2, C_WHITE)
    c.rect(24, 3, 40, 2, C_GREY_LGT)
    c.line(24, 5, 63, 5, C_WALL_SHAD)
    # Shelf metal brackets
    c.line(26, 5, 26, 7, C_GREY_MID)
    c.line(61, 5, 61, 7, C_GREY_MID)
    # Shelf items
    # Small amber dropper bottle
    c.rect(28, 0, 4, 3, C_AMBER_MID)
    c.rect(29, 0, 2, 1, C_AMBER_DRK)
    c.set(28, 1, C_AMBER_HI)
    # Small glass beaker with green liquid
    c.rect(35, 1, 4, 2, C_GLASS_LGT)
    c.set(35, 1, C_WHITE)
    c.rect(36, 2, 2, 1, C_GRN_MID)
    # Slide / reagent box (blue box with white label stripe)
    c.rect(43, 1, 7, 2, C_BLUE_DRK)
    c.line(44, 1, 48, 1, C_WHITE)
    # Small Erlenmeyer flask on shelf
    c.poly([(55, 3), (53, 1), (57, 1)], C_GLASS_LGT)
    c.set(54, 0, C_GLASS_HI)
    c.line(54, 2, 56, 2, C_BLUE_MID)
    
    # Utility trunking strip (y=16..19)
    c.rect(0, 16, 64, 4, C_UTIL_BG)
    c.line(0, 16, 63, 16, C_UTIL_HIGH)
    c.line(0, 19, 63, 19, C_UTIL_LINE)
    # Gas taps (yellow valve handles and gooseneck nozzles)
    for gx in [34, 58]:
        c.rect(gx, 16, 3, 3, C_GREY_MID)
        c.line(gx+1, 14, gx+1, 16, C_GREY_DRK)
        c.set(gx+1, 13, C_YEL_MID)
    # Duplex power socket
    c.rect(14, 17, 4, 2, C_WHITE)
    c.set(15, 17, C_GREY_BLACK)
    c.set(17, 17, C_GREY_BLACK)

    # Workbench top (y=20..56)
    c.rect(0, 20, 64, 37, C_BENCH_SURF)
    c.line(0, 20, 63, 20, C_BENCH_HIGH)
    c.line(0, 21, 63, 21, C_BENCH_MID)
    # Front edge bevel & underside
    c.line(0, 56, 63, 56, C_BENCH_BEVEL)
    c.line(0, 57, 63, 57, C_BENCH_EDGE)
    
    # Cabinet drawers (y=58..63)
    c.rect(0, 58, 64, 6, C_WOOD_MID)
    c.line(0, 58, 63, 58, C_WOOD_LGT)
    c.line(0, 63, 63, 63, C_WOOD_DRK)
    # Drawer divider vertical seams
    c.line(21, 58, 21, 63, C_WOOD_DEEP)
    c.line(43, 58, 43, 63, C_WOOD_DEEP)
    # Metal drawer pulls
    for hx in [7, 28, 50]:
        c.line(hx, 60, hx+6, 60, C_WHITE)
        c.line(hx, 61, hx+6, 61, C_WOOD_DEEP)

    # ====================================================
    # 2. MICROSCOPE (x=4..23, y=12..51)
    # ====================================================
    # Cast shadow on bench
    c.ellipse(14, 51, 8, 2, C_BENCH_DARK)
    
    # Base (heavy horseshoe foot)
    c.rect(7, 47, 14, 3, C_GREY_MID)
    c.rect(8, 46, 12, 2, C_OFFWHITE)
    c.line(9, 46, 18, 46, C_WHITE)
    c.line(7, 49, 20, 49, C_GREY_BLACK)
    # Rubber foot pads
    c.set(7, 50, C_BLACK)
    c.set(13, 50, C_BLACK)
    c.set(20, 50, C_BLACK)
    
    # Field illuminator lens on base
    c.rect(13, 44, 4, 3, C_GREY_BLACK)
    c.rect(14, 44, 2, 1, C_GLASS_HI)
    
    # Lower Pillar & Stage Bracket
    c.rect(6, 38, 4, 9, C_OFFWHITE)
    c.line(6, 38, 6, 46, C_WHITE)
    c.line(9, 38, 9, 46, C_GREY_MID)
    # Rigid bracket connecting pillar to stage
    c.rect(9, 37, 3, 4, C_GREY_DRK)
    c.line(9, 38, 11, 38, C_GREY_LGT)
    
    # Focus knobs (concentric coarse/fine wheels)
    c.circle(7, 42, 3, C_GREY_DRK)
    c.circle(7, 42, 2, C_GREY_LGT)
    c.circle(7, 42, 1, C_GREY_BLACK)
    c.set(7, 42, C_WHITE)
    
    # Substage condenser & iris diaphragm
    c.rect(13, 39, 4, 4, C_GREY_BLACK)
    c.line(14, 39, 16, 39, C_GLASS_HI)
    c.line(14, 41, 16, 41, C_GREY_LGT)
    c.line(11, 41, 12, 41, C_GREY_LGT)
    
    # Mechanical Stage (x=9..21, y=36..38)
    c.rect(9, 36, 13, 3, C_GREY_BLACK)
    c.line(9, 36, 21, 36, C_GREY_DRK)
    # Glass slide with stained specimen
    c.rect(12, 35, 7, 1, C_GLASS_LGT)
    c.set(15, 35, C_PURPLE)
    c.set(11, 35, C_WHITE)
    c.set(19, 35, C_WHITE)
    # Stage X-Y control knobs hanging on right
    c.line(19, 39, 19, 42, C_GREY_MID)
    c.line(20, 40, 20, 42, C_GREY_DRK)
    
    # Curved Upper Arm (C-frame arching over stage)
    c.rect(6, 24, 4, 14, C_OFFWHITE)
    c.line(6, 24, 6, 37, C_WHITE)
    c.line(9, 24, 9, 37, C_GREY_MID)
    # Arch forward
    c.rect(7, 21, 9, 4, C_OFFWHITE)
    c.line(7, 21, 15, 21, C_WHITE)
    c.line(9, 24, 15, 24, C_GREY_MID)
    
    # Revolving Nosepiece / Turret
    c.rect(13, 25, 6, 3, C_GREY_BLACK)
    c.line(13, 25, 18, 25, C_GREY_LGT)
    # 3 Objective Lenses:
    # Central active objective:
    c.rect(15, 28, 2, 5, C_GREY_LGT)
    c.set(15, 28, C_WHITE)
    c.set(15, 30, C_BLUE_MID)
    c.set(16, 30, C_BLUE_MID)
    c.set(15, 32, C_BLACK)
    c.set(16, 32, C_BLACK)
    # Left objective
    c.line(13, 27, 12, 30, C_GREY_LGT)
    c.set(12, 29, C_RED_MID)
    # Right objective
    c.line(18, 27, 19, 30, C_GREY_LGT)
    c.set(19, 29, C_YEL_MID)
    
    # Binocular Head (prism housing)
    c.rect(7, 18, 9, 4, C_OFFWHITE)
    c.line(7, 18, 15, 18, C_WHITE)
    c.line(7, 21, 15, 21, C_GREY_MID)
    # Dual angled eyepiece tubes
    # Left tube & eyecup
    c.rect(6, 15, 2, 3, C_GREY_LGT)
    c.rect(5, 12, 3, 3, C_GREY_BLACK)
    c.line(5, 12, 7, 12, C_BLACK)
    c.set(6, 12, C_GLASS_HI)
    # Right tube & eyecup
    c.rect(10, 15, 2, 3, C_OFFWHITE)
    c.rect(9, 12, 3, 3, C_GREY_BLACK)
    c.line(9, 12, 11, 12, C_BLACK)
    c.set(10, 12, C_GLASS_HI)

    # ====================================================
    # 3. TEST-TUBE RACK (x=23..43, y=23..43)
    # ====================================================
    # Cast shadow under rack
    c.ellipse(33, 43, 10, 2, C_BENCH_DARK)
    
    # 4 Test Tubes
    tubes = [
        # (center_x, liquid_top_y, col_main, col_hi, col_drk)
        (26, 32, C_BLUE_MID, C_BLUE_HI, C_BLUE_DRK), # Blue
        (30, 30, C_YEL_MID,  C_YEL_HI,  C_YEL_DRK),  # Golden Amber
        (34, 33, C_RED_MID,  C_RED_HI,  C_RED_DRK),  # Crimson Red
        (38, 31, C_GRN_MID,  C_GRN_HI,  C_GRN_DRK)   # Emerald Green
    ]
    
    # Wooden rack rear support rail (behind tubes)
    c.line(24, 35, 40, 35, C_WOOD_DRK)
    
    # Test tubes
    for tx, liq_y, col_main, col_hi, col_drk in tubes:
        # Glass lip / rim at top (y=23)
        c.line(tx-1, 23, tx+1, 23, C_WHITE)
        # Empty glass tube
        for gy in range(24, liq_y):
            c.set(tx-1, gy, C_GLASS_HI)
            c.set(tx, gy, C_GLASS_LGT)
            c.set(tx+1, gy, C_GLASS_MID)
        # Curved Meniscus
        c.set(tx-1, liq_y, col_hi)
        c.set(tx, liq_y+1, col_main)
        c.set(tx+1, liq_y, col_hi)
        # Liquid column down to y=38
        for ly in range(liq_y+1, 39):
            c.set(tx-1, ly, col_hi)
            c.set(tx, ly, col_main)
            c.set(tx+1, ly, col_drk)
        # Rounded test tube bottom (y=39..40)
        c.set(tx-1, 39, col_main)
        c.set(tx, 39, col_drk)
        c.set(tx+1, 39, col_drk)
        c.set(tx, 40, C_GLASS_MID)

    # Wooden Rack Frame (Front rails & uprights)
    # Left end upright (x=23..24, y=28..42)
    c.rect(23, 28, 2, 14, C_WOOD_MID)
    c.line(23, 28, 23, 41, C_WOOD_LGT)
    c.line(24, 29, 24, 42, C_WOOD_DRK)
    # Right end upright (x=41..42, y=28..42)
    c.rect(41, 28, 2, 14, C_WOOD_MID)
    c.line(41, 28, 41, 41, C_WOOD_LGT)
    c.line(42, 29, 42, 42, C_WOOD_DRK)
    
    # Top shelf rail with circular cutouts for tubes (y=28..29)
    c.line(23, 28, 42, 28, C_WOOD_LGT)
    c.line(23, 29, 42, 29, C_WOOD_MID)
    for tx, _, _, _, _ in tubes:
        c.set(tx-1, 28, C_WOOD_DRK)
        c.set(tx, 28, C_WOOD_DRK)
        c.set(tx+1, 28, C_WOOD_DRK)
        
    # Bottom base rail (y=41..42)
    c.rect(22, 41, 22, 2, C_WOOD_MID)
    c.line(22, 41, 43, 41, C_WOOD_LGT)
    c.line(22, 42, 43, 42, C_WOOD_DEEP)

    # ====================================================
    # 4. LABELED BOTTLES (x=44..62, y=21..39)
    # ====================================================
    # Bottle 1: Amber glass Boston round chemical bottle
    c.ellipse(48, 38, 4, 1, C_BENCH_DARK)
    # Black screw cap with vertical grip ridges
    c.rect(46, 22, 5, 3, C_GREY_BLACK)
    c.line(46, 22, 50, 22, C_GREY_MID)
    c.set(47, 23, C_GREY_MID)
    c.set(49, 23, C_GREY_MID)
    # Neck
    c.rect(47, 25, 3, 2, C_AMBER_DRK)
    c.set(47, 25, C_AMBER_MID)
    # Shoulders
    c.poly([(47, 26), (44, 29), (52, 29), (49, 26)], C_AMBER_MID)
    c.line(45, 28, 47, 26, C_AMBER_HI)
    # Body (x=44..52, y=29..37)
    c.rect(44, 29, 9, 8, C_AMBER_MID)
    c.line(44, 29, 44, 36, C_AMBER_HI)
    c.line(52, 29, 52, 36, C_AMBER_DRK)
    c.line(44, 37, 52, 37, C_AMBER_DRK)
    # White paper label with hazard diamond
    c.rect(45, 30, 7, 5, C_WHITE)
    # Red GHS hazard diamond
    c.set(48, 31, C_RED_MID)
    c.line(47, 32, 49, 32, C_RED_MID)
    c.set(48, 33, C_RED_MID)
    # Chemical name black stripe
    c.line(46, 34, 50, 34, C_GREY_BLACK)
    
    # Bottle 2: Clear laboratory media bottle with blue screw cap
    c.ellipse(58, 39, 4, 1, C_BENCH_DARK)
    # Blue polypropylene screw cap
    c.rect(56, 24, 5, 3, C_BLUE_MID)
    c.line(56, 24, 60, 24, C_BLUE_HI)
    c.line(56, 26, 60, 26, C_BLUE_DRK)
    # Glass neck
    c.rect(57, 27, 3, 2, C_GLASS_LGT)
    c.set(57, 27, C_WHITE)
    # Glass Body (x=54..62, y=28..38)
    c.rect(54, 28, 9, 10, C_GLASS_LGT)
    c.line(54, 28, 54, 37, C_WHITE)
    c.line(62, 28, 62, 37, C_GLASS_MID)
    c.line(54, 38, 62, 38, C_GLASS_MID)
    # Solution inside (half full, y=33..37)
    c.rect(55, 33, 7, 5, C_GRN_MID)
    c.line(55, 33, 61, 33, C_GRN_HI)
    # Graduation marks on left
    for gy in [30, 32, 34, 36]:
        c.set(55, gy, C_WHITE)
    # White rectangular label on right (x=57..61, y=30..34)
    c.rect(57, 30, 4, 5, C_WHITE)
    c.line(58, 31, 60, 31, C_GREY_DRK)
    c.line(58, 33, 60, 33, C_GREY_DRK)

    # ====================================================
    # 5. OPEN LABORATORY NOTEBOOK (x=20..44, y=43..56)
    # ====================================================
    # Cast shadow under notebook
    c.rect(20, 56, 25, 2, C_BENCH_DARK)
    
    # Hardcover border
    c.rect(20, 43, 25, 13, C_GREY_BLACK)
    
    # Left open page (x=21..31, y=43..55)
    c.rect(21, 44, 11, 11, C_OFFWHITE)
    c.line(22, 43, 30, 43, C_WHITE)
    c.line(21, 45, 21, 54, C_WHITE)
    
    # Right open page (x=33..43, y=43..55)
    c.rect(33, 44, 11, 11, C_OFFWHITE)
    c.line(33, 43, 42, 43, C_WHITE)
    c.line(43, 45, 43, 54, C_GREY_LGT)
    
    # Center spine crease / gutter (x=32)
    c.line(32, 43, 32, 55, C_GREY_MID)
    c.line(31, 44, 31, 54, C_GREY_LGT)
    c.line(33, 44, 33, 54, C_GREY_LGT)
    
    # Left Page: Data Plot / Curve
    # Grid lines
    c.line(22, 49, 30, 49, C_GREY_LGT)
    c.line(26, 45, 26, 53, C_GREY_LGT)
    # Axes
    c.line(22, 45, 22, 53, C_GREY_MID) # y-axis
    c.line(22, 53, 30, 53, C_GREY_MID) # x-axis
    # Plotted sigmoidal curve
    curve_pts = [(23, 52), (24, 52), (25, 50), (26, 48), (27, 47), (28, 46), (29, 46)]
    for px, py in curve_pts:
        c.set(px, py, C_BLUE_MID)
    # Red data points
    c.set(24, 52, C_RED_MID)
    c.set(26, 48, C_RED_MID)
    c.set(28, 46, C_RED_MID)
    
    # Right Page: Chemical formula & note lines
    # Date header
    c.line(37, 45, 41, 45, C_GREY_MID)
    # Hexagonal benzene ring sketch
    c.line(35, 47, 37, 47, C_GREY_DRK)
    c.set(34, 48, C_GREY_DRK)
    c.set(38, 48, C_GREY_DRK)
    c.line(35, 49, 37, 49, C_GREY_DRK)
    # Reaction arrow
    c.line(40, 48, 42, 48, C_GREY_DRK)
    c.set(42, 47, C_GREY_DRK)
    # Ruled lines
    c.line(35, 51, 42, 51, C_GREY_MID)
    c.line(35, 53, 41, 53, C_GREY_MID)
    
    # Yellow lab pencil beside notebook (x=45, y=44..52)
    c.set(45, 44, C_RED_HI)      # pink eraser
    c.set(45, 45, C_GREY_LGT)    # metal ferrule
    for py in range(46, 51):
        c.set(45, py, C_YEL_MID) # yellow pencil body
    c.set(45, 51, C_YEL_HI)      # sharpened wood
    c.set(45, 52, C_GREY_BLACK)  # lead tip

    # ====================================================
    # 6. BEAKER & DROPPER (Pipette) (x=48..63, y=42..55)
    # ====================================================
    # 50ml Glass Griffin Beaker (x=52..59, y=42..49)
    # Shadow under beaker
    c.ellipse(55, 49, 4, 1, C_BENCH_DARK)
    # Glass Beaker body
    c.rect(52, 43, 8, 6, C_GLASS_LGT)
    # Spout on left rim
    c.set(51, 42, C_WHITE)
    c.line(52, 42, 59, 42, C_WHITE)
    # Left highlight & right shadow wall
    c.line(52, 43, 52, 48, C_WHITE)
    c.line(59, 43, 59, 48, C_GLASS_MID)
    c.line(52, 48, 59, 48, C_GLASS_MID)
    # Blue solution inside beaker (half full, y=45..48)
    c.rect(53, 45, 6, 3, C_BLUE_MID)
    c.line(53, 45, 58, 45, C_BLUE_HI) # meniscus
    # Graduation scale marks on right
    c.set(58, 44, C_WHITE)
    c.set(58, 46, C_WHITE)

    # Dropper (Pasteur Pipette) resting on bench in foreground
    # Position: x=47..62, y=51..54
    # Cast shadow on dark bench
    c.line(48, 54, 62, 54, C_BENCH_DARK)
    
    # Rubber Bulb on the right (x=58..62, y=50..53)
    # Symmetrical bulb shape
    c.line(59, 50, 61, 50, C_RED_HI)   # top round highlight
    c.rect(58, 51, 5, 2, C_RED_MID)     # main bulb body
    c.set(58, 51, C_RED_HI)
    c.set(59, 51, C_RED_HI)
    c.line(58, 53, 62, 53, C_RED_DRK)  # bottom shadow
    c.line(59, 54, 61, 54, C_RED_DRK)
    # Collar where glass tube enters rubber bulb (x=57)
    c.line(57, 51, 57, 53, C_RED_DRK)
    c.set(57, 52, C_RED_MID)
    
    # Glass Cylindrical Tube (x=51..56, y=51..53)
    # Top specular highlight line
    c.line(51, 51, 56, 51, C_WHITE)
    # Blue chemical liquid drawn inside tube
    c.line(53, 52, 56, 52, C_BLUE_MID)
    c.set(51, 52, C_GLASS_LGT)
    c.set(52, 52, C_GLASS_HI)
    # Bottom glass shadow line
    c.line(51, 53, 56, 53, C_GLASS_DRK)
    
    # Fine Tapered Capillary Tip (x=49..50, y=52)
    c.set(50, 52, C_GLASS_LGT)
    c.set(49, 52, C_WHITE)
    
    # Chemical Droplet forming and beading from tip
    c.set(48, 52, C_BLUE_HI)  # drop at tip
    c.set(47, 53, C_BLUE_HI)  # droplet bead
    c.set(47, 54, C_BLUE_MID)
    c.set(48, 54, C_BLUE_DRK) # tiny reflection on benchtop
    
    return c

c = build_workbench()
view(c)
print(c.stats_text())
finish(c)
