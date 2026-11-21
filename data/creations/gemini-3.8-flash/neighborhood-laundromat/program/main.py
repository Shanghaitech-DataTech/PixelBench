import math
from pixelbench_api import *

def build_laundromat():
    c = new_canvas(64, 64, "#0f172a")

    # =========================================================================
    # PALETTE SPECIFICATION (strictly controlled to stay ~50 colors, well under 86)
    # =========================================================================
    # Darks / Neutrals
    C_BLACK     = "#090d16"
    C_SLATE_DK  = "#151b24"
    C_SLATE_MID = "#1e293b"
    C_STEEL_DK  = "#283341"
    C_STEEL_MID = "#334155"
    C_STEEL_LT  = "#475569"
    C_GREY_MID  = "#64748b"
    C_GREY_LT   = "#94a3b8"
    C_SILVER    = "#cbd5e1"
    C_WHITE_OFF = "#f1f5f9"
    C_WHITE     = "#ffffff"

    # Cool White Lighting & Cyan Accents
    C_GLOW_CYAN = "#bae6fd"
    C_TUBE_LT   = "#e0f2fe"
    C_CYAN_NEON = "#00f0ff"
    C_CYAN_MID  = "#0284c7"
    C_CYAN_DK   = "#0369a1"

    # Wall Mint Tiles
    C_WALL_HI   = "#9fc2cb"
    C_WALL_MID  = "#7da2ab"
    C_WALL_SH   = "#5f838c"
    C_GROUT     = "#44656d"

    # Floor Tiles
    C_FLOOR_DK  = "#2a3443"
    C_FLOOR_MID = "#3d4b5e"
    C_FLOOR_LT  = "#52637a"
    C_FLOOR_GROUT = "#19212d"

    # Machine Bodies
    C_MACH_BODY = "#d5dfe7"
    C_MACH_SH   = "#8496a6"
    C_MACH_DK   = "#4e5e6e"

    # Wood Folding Table
    C_WOOD_HI   = "#f2c794"
    C_WOOD_MID  = "#c68a4c"
    C_WOOD_DK   = "#855325"

    # Plastic Laundry Basket (Teal)
    C_BSK_HI    = "#5eead4"
    C_BSK_MID   = "#14b8a6"
    C_BSK_DK    = "#0f766e"
    C_BSK_HOLE  = "#115e59"

    # Accent Colors for Clothes / Displays / Detergent
    C_RED       = "#ef4444"
    C_RED_LT    = "#fca5a5"
    C_RED_DK    = "#b91c1c"
    C_BLUE      = "#2563eb"
    C_BLUE_LT   = "#93c5fd"
    C_BLUE_DK   = "#1d4ed8"
    C_YELLOW    = "#eab308"
    C_YELLOW_LT = "#fef08a"
    C_GREEN     = "#22c55e"
    C_ORANGE    = "#f97316"
    C_ORANGE_LT = "#fed7aa"
    C_PURPLE    = "#a855f7"
    C_PINK      = "#ec4899"

    # =========================================================================
    # 1. CEILING & LIGHTING (y: 0 .. 7)
    # =========================================================================
    # Ceiling cavity
    c.rect(0, 0, 64, 7, C_SLATE_DK)
    c.line(0, 7, 63, 7, C_STEEL_DK)
    for cx in range(0, 64, 16):
        c.line(cx, 0, cx, 6, C_SLATE_MID)

    # Fluorescent fixture 1 (x: 5..41, y: 1..3)
    c.rect(5, 1, 37, 3, C_STEEL_MID)
    c.rect(6, 2, 35, 2, C_TUBE_LT)
    c.line(7, 2, 39, 2, C_WHITE)
    c.line(9, 0, 9, 1, C_STEEL_LT)
    c.line(37, 0, 37, 1, C_STEEL_LT)

    # Fluorescent fixture 2 (x: 48..61, y: 1..3)
    c.rect(48, 1, 14, 3, C_STEEL_MID)
    c.rect(49, 2, 12, 2, C_TUBE_LT)
    c.line(50, 2, 59, 2, C_WHITE)
    c.line(55, 0, 55, 1, C_STEEL_LT)

    # =========================================================================
    # 2. TILED WALL (y: 8 .. 42)
    # =========================================================================
    wall_y_start = 8
    wall_y_end = 42

    # Vertical light wash from cool white fixtures
    for y in range(wall_y_start, wall_y_end + 1):
        if y < 14:
            c.line(0, y, 63, y, C_WALL_HI)
        elif y < 26:
            c.line(0, y, 63, y, C_WALL_MID)
        else:
            c.line(0, y, 63, y, C_WALL_SH)

    # Light glow patches directly beneath the tubes
    for y in range(8, 20):
        # Fixture 1 light cone
        x_left = max(0, 5 - (y - 8) // 3)
        x_right = min(63, 41 + (y - 8) // 3)
        for x in range(x_left, x_right + 1):
            if y < 12:
                c.set(x, y, C_TUBE_LT)
            else:
                c.set(x, y, C_WALL_HI)
        # Fixture 2 light cone
        x2_left = max(0, 48 - (y - 8) // 3)
        x2_right = min(63, 61 + (y - 8) // 3)
        for x in range(x2_left, x2_right + 1):
            if y < 12:
                c.set(x, y, C_TUBE_LT)
            else:
                c.set(x, y, C_WALL_HI)

    # Wall tile grid (6x5 pixels)
    for ty in range(8, wall_y_end + 1, 5):
        c.line(0, ty, 63, ty, C_GROUT)
    for tx in range(0, 64, 6):
        c.line(tx, 8, tx, wall_y_end, C_GROUT)

    # Bottom cove baseboard
    c.rect(0, 41, 64, 2, C_SLATE_MID)
    c.line(0, 41, 63, 41, C_STEEL_MID)

    # =========================================================================
    # 3. WALL CLOCK (x: 54, y: 14)
    # Clean, beautiful round clock prominently placed above the folding table
    # =========================================================================
    clock_cx = 54
    clock_cy = 14

    # Clear wall tiles behind clock with smooth disc
    clock_rows = [
        (-5, -2, 2, C_SLATE_DK),
        (-4, -3, 3, C_SLATE_DK),
        (-3, -4, 4, C_SLATE_DK),
        (-2, -4, 4, C_SLATE_DK),
        (-1, -5, 5, C_SLATE_DK),
        ( 0, -5, 5, C_SLATE_DK),
        ( 1, -5, 5, C_SLATE_DK),
        ( 2, -4, 4, C_SLATE_DK),
        ( 3, -4, 4, C_SLATE_DK),
        ( 4, -3, 3, C_SLATE_DK),
        ( 5, -2, 2, C_SLATE_DK),
    ]
    for dy, x0, x1, col in clock_rows:
        c.line(clock_cx + x0, clock_cy + dy, clock_cx + x1, clock_cy + dy, col)

    # Clock face interior (white face, 9x9 disc)
    face_rows = [
        (-4, -2, 2),
        (-3, -3, 3),
        (-2, -3, 3),
        (-1, -4, 4),
        ( 0, -4, 4),
        ( 1, -4, 4),
        ( 2, -3, 3),
        ( 3, -3, 3),
        ( 4, -2, 2),
    ]
    for dy, x0, x1 in face_rows:
        c.line(clock_cx + x0, clock_cy + dy, clock_cx + x1, clock_cy + dy, C_WHITE_OFF)

    # Top inner shadow on face
    c.line(clock_cx - 2, clock_cy - 4, clock_cx + 2, clock_cy - 4, C_SILVER)
    c.line(clock_cx - 3, clock_cy - 3, clock_cx + 3, clock_cy - 3, C_SILVER)

    # Hour tick marks at 12, 3, 6, 9
    c.set(clock_cx, clock_cy - 3, C_GREY_MID) # 12
    c.set(clock_cx + 3, clock_cy, C_GREY_MID) # 3
    c.set(clock_cx, clock_cy + 3, C_GREY_MID) # 6
    c.set(clock_cx - 3, clock_cy, C_GREY_MID) # 9

    # Clock hands: 10:10 classic position
    c.set(clock_cx, clock_cy, C_BLACK)         # center pivot
    c.set(clock_cx - 1, clock_cy - 1, C_BLACK) # hour hand pointing to 10
    c.set(clock_cx - 2, clock_cy - 2, C_BLACK)
    c.set(clock_cx + 1, clock_cy - 1, C_RED)   # minute hand pointing to 2
    c.set(clock_cx + 2, clock_cy - 2, C_RED)
    c.set(clock_cx + 3, clock_cy - 3, C_RED)
    # Glass glint
    c.set(clock_cx - 3, clock_cy - 1, C_WHITE)
    c.set(clock_cx - 2, clock_cy + 1, C_WHITE)

    # =========================================================================
    # 4. FLOOR (y: 43 .. 63)
    # Large format glossy commercial tiles with perspective and reflections
    # =========================================================================
    c.rect(0, 43, 64, 21, C_FLOOR_DK)

    # Perspective tile rows
    row_splits = [43, 47, 52, 57, 64]
    col_w = 8

    for r in range(len(row_splits) - 1):
        y0 = row_splits[r]
        y1 = row_splits[r+1]
        c.line(0, y0, 63, y0, C_FLOOR_GROUT)
        for c_idx in range(0, 64, col_w):
            c.line(c_idx, y0, c_idx, y1 - 1, C_FLOOR_GROUT)
            if (r + (c_idx // col_w)) % 2 == 1:
                c.rect(c_idx + 1, y0 + 1, col_w - 1, (y1 - y0) - 1, C_FLOOR_MID)

    # Polished floor sheen / reflections from fluorescent lights
    for fy in range(44, 63):
        for rx in [7, 18, 29, 40, 54]:
            if rx < 64:
                curr = c.get(rx, fy)
                if curr == c.color(C_FLOOR_MID):
                    c.set(rx, fy, C_FLOOR_LT)
                elif curr == c.color(C_FLOOR_DK):
                    c.set(rx, fy, C_FLOOR_MID)

    # =========================================================================
    # 5. TWO ROWS OF FRONT-LOADING WASHING MACHINES
    # Bulkhead frame: x = 1 .. 45, y = 11 .. 44
    # Top Row: 4 machines, y = 12..26
    # Shelf divider: y = 27
    # Bottom Row: 4 machines, y = 28..42
    # Plinth Base: y = 43..44
    # =========================================================================
    # Dark steel bulkhead housing
    c.rect(1, 11, 44, 33, C_SLATE_DK)
    c.line(1, 11, 44, 11, C_STEEL_DK)    # top edge bevel
    c.line(44, 11, 44, 43, C_STEEL_DK)   # right edge bevel
    c.rect(1, 43, 44, 2, C_BLACK)        # solid heavy plinth
    c.line(1, 43, 44, 43, C_STEEL_DK)    # plinth bevel
    c.line(1, 27, 44, 27, C_BLACK)       # heavy horizontal divider shelf
    c.line(1, 28, 44, 28, C_STEEL_DK)    # shelf highlight

    # Vertical dividers between machines:
    for vx in [12, 23, 34]:
        c.line(vx, 11, vx, 42, C_BLACK)

    # Function to draw each individual front-loading washing machine
    def render_washer(mx, my, status, cycle_type):
        mw = 10
        mh = 14
        
        # 1. Main individual machine chassis
        c.rect(mx, my, mw, mh, C_MACH_BODY)
        # Visual separation: Top and left highlights, right and bottom shadows
        c.line(mx, my, mx + mw - 1, my, C_WHITE)          # top highlight
        c.line(mx, my, mx, my + mh - 1, C_WHITE)          # left highlight
        c.line(mx + mw - 1, my, mx + mw - 1, my + mh - 1, C_MACH_SH) # right shadow
        c.line(mx, my + mh - 1, mx + mw - 1, my + mh - 1, C_MACH_DK) # bottom shadow
        
        # 2. Control panel strip at top (y: my+1 .. my+3)
        c.rect(mx + 1, my + 1, mw - 2, 3, C_STEEL_DK)
        c.line(mx + 1, my + 1, mx + mw - 2, my + 1, C_STEEL_MID)
        
        # Detergent dispenser drawer handle (left)
        c.set(mx + 1, my + 2, C_GREY_LT)
        c.set(mx + 2, my + 2, C_STEEL_LT)
        
        # Digital LED display (center)
        if status == "running":
            c.set(mx + 4, my + 2, C_CYAN_NEON)
            c.set(mx + 5, my + 2, C_CYAN_NEON)
            c.set(mx + 7, my + 2, C_GREEN)     # active run LED
        elif status == "done":
            c.set(mx + 4, my + 2, C_GREEN)     # "00" green LED
            c.set(mx + 5, my + 2, C_GREEN)
            c.set(mx + 7, my + 2, C_YELLOW)    # done indicator LED
        else: # idle
            c.set(mx + 4, my + 2, C_STEEL_LT)  # dim display
            c.set(mx + 5, my + 2, C_STEEL_LT)
            c.set(mx + 7, my + 2, C_RED)       # ready red LED
            
        # Coin slot & start knob (right)
        c.set(mx + 8, my + 2, C_SILVER)
        c.set(mx + 8, my + 3, C_BLACK)
        
        # Lower kickplate filter access line
        c.line(mx + 1, my + mh - 2, mx + mw - 2, my + mh - 2, C_MACH_SH)
        
        # 3. Front-loading circular door (8x8 circular porthole)
        door_x = mx + 1
        door_y = my + 4
        
        door_mask = [
            (2,0), (3,0), (4,0), (5,0),
            (1,1), (2,1), (3,1), (4,1), (5,1), (6,1),
            (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2),
            (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3),
            (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4),
            (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5),
            (1,6), (2,6), (3,6), (4,6), (5,6), (6,6),
            (2,7), (3,7), (4,7), (5,7)
        ]
        for dx, dy in door_mask:
            c.set(door_x + dx, door_y + dy, C_STEEL_LT)
            
        # Metallic highlights on door ring
        c.set(door_x + 2, door_y, C_SILVER)
        c.set(door_x + 3, door_y, C_SILVER)
        c.set(door_x + 4, door_y, C_SILVER)
        c.set(door_x + 1, door_y + 1, C_WHITE)
        c.set(door_x, door_y + 2, C_SILVER)
        c.set(door_x, door_y + 3, C_SILVER)
        
        # Door ring shadow
        c.set(door_x + 7, door_y + 4, C_SLATE_DK)
        c.set(door_x + 7, door_y + 5, C_SLATE_DK)
        c.set(door_x + 6, door_y + 6, C_SLATE_DK)
        c.set(door_x + 4, door_y + 7, C_SLATE_DK)
        c.set(door_x + 5, door_y + 7, C_SLATE_DK)
        
        # Door handle on right side
        c.set(door_x + 7, door_y + 3, C_WHITE)
        c.set(door_x + 7, door_y + 4, C_GREY_LT)
        
        # Inner circular drum void
        inner_mask = [
            (2,1), (3,1), (4,1), (5,1),
            (1,2), (2,2), (3,2), (4,2), (5,2), (6,2),
            (1,3), (2,3), (3,3), (4,3), (5,3), (6,3),
            (1,4), (2,4), (3,4), (4,4), (5,4), (6,4),
            (1,5), (2,5), (3,5), (4,5), (5,5), (6,5),
            (2,6), (3,6), (4,6), (5,6)
        ]
        for dx, dy in inner_mask:
            c.set(door_x + dx, door_y + dy, C_BLACK)
            
        # 4. Drum contents: water, spinning laundry, or empty drum
        if status == "running":
            if cycle_type == "blue_red":
                # Swirling blue jeans & red tee with suds
                c.set(door_x + 2, door_y + 4, C_BLUE_DK)
                c.set(door_x + 3, door_y + 5, C_RED)
                c.set(door_x + 4, door_y + 5, C_RED_DK)
                c.set(door_x + 5, door_y + 4, C_GLOW_CYAN)
                c.set(door_x + 2, door_y + 3, C_WHITE)
                c.set(door_x + 3, door_y + 3, C_GLOW_CYAN)
                c.set(door_x + 4, door_y + 4, C_WHITE)
            elif cycle_type == "yellow_green":
                # Spinning yellow & green towels
                c.set(door_x + 2, door_y + 4, C_YELLOW)
                c.set(door_x + 3, door_y + 5, C_YELLOW)
                c.set(door_x + 4, door_y + 5, C_GREEN)
                c.set(door_x + 5, door_y + 3, C_GREEN)
                c.set(door_x + 3, door_y + 2, C_WHITE)
                c.set(door_x + 2, door_y + 3, C_YELLOW_LT)
            elif cycle_type == "white_suds":
                # White linens with crystal blue soapy foam
                c.set(door_x + 2, door_y + 4, C_WHITE_OFF)
                c.set(door_x + 3, door_y + 5, C_SILVER)
                c.set(door_x + 4, door_y + 5, C_WHITE)
                c.set(door_x + 5, door_y + 4, C_CYAN_MID)
                c.set(door_x + 3, door_y + 3, C_WHITE)
                c.set(door_x + 4, door_y + 3, C_GLOW_CYAN)
                c.set(door_x + 2, door_y + 3, C_GLOW_CYAN)
            elif cycle_type == "purple_orange":
                # Swirling purple & orange clothes
                c.set(door_x + 2, door_y + 5, C_PURPLE)
                c.set(door_x + 3, door_y + 5, C_ORANGE)
                c.set(door_x + 4, door_y + 4, C_ORANGE)
                c.set(door_x + 5, door_y + 4, C_GLOW_CYAN)
                c.set(door_x + 3, door_y + 3, C_WHITE)
                c.set(door_x + 4, door_y + 3, C_PURPLE)
            elif cycle_type == "pink_blue":
                # Swirling pink & navy
                c.set(door_x + 2, door_y + 4, C_PINK)
                c.set(door_x + 3, door_y + 5, C_BLUE)
                c.set(door_x + 4, door_y + 5, C_BLUE_DK)
                c.set(door_x + 5, door_y + 4, C_GLOW_CYAN)
                c.set(door_x + 2, door_y + 3, C_WHITE)
                c.set(door_x + 4, door_y + 4, C_WHITE)
        elif status == "done":
            # Laundry settled at bottom
            c.set(door_x + 2, door_y + 5, C_BLUE)
            c.set(door_x + 3, door_y + 5, C_PINK)
            c.set(door_x + 4, door_y + 5, C_WHITE)
            c.set(door_x + 5, door_y + 5, C_YELLOW)
            c.set(door_x + 3, door_y + 3, C_SLATE_MID)
            c.set(door_x + 4, door_y + 3, C_SLATE_MID)
        else: # idle / ready
            # Clean empty stainless steel drum pattern
            c.set(door_x + 2, door_y + 3, C_SLATE_MID)
            c.set(door_x + 3, door_y + 4, C_STEEL_MID)
            c.set(door_x + 4, door_y + 4, C_STEEL_MID)
            c.set(door_x + 5, door_y + 3, C_SLATE_MID)
            c.set(door_x + 3, door_y + 5, C_SLATE_MID)
            c.set(door_x + 4, door_y + 5, C_SLATE_MID)

        # 5. Curved glass reflection highlight (top-left arc)
        c.set(door_x + 2, door_y + 2, C_GLOW_CYAN)
        c.set(door_x + 3, door_y + 2, C_WHITE)
        c.set(door_x + 2, door_y + 3, C_GLOW_CYAN)

    # TOP ROW (Row 1): 4 machines
    top_y = 12
    render_washer(2,  top_y, "running", "blue_red")
    render_washer(13, top_y, "running", "yellow_green")
    render_washer(24, top_y, "idle",    None)
    render_washer(35, top_y, "running", "white_suds")

    # BOTTOM ROW (Row 2): 4 machines
    bot_y = 28
    render_washer(2,  bot_y, "idle",    None)
    render_washer(13, bot_y, "running", "purple_orange")
    render_washer(24, bot_y, "done",    None)
    render_washer(35, bot_y, "running", "pink_blue")

    # =========================================================================
    # 6. FOLDING TABLE (x: 46 .. 62, y: 34 .. 55)
    # =========================================================================
    table_x = 46
    table_w = 17
    table_y = 34
    
    # Smooth beveled tabletop (warm blonde laminate)
    c.rect(table_x, table_y, table_w, 3, C_WOOD_MID)
    c.line(table_x, table_y, table_x + table_w - 1, table_y, C_WOOD_HI) # top bevel
    c.line(table_x, table_y + 2, table_x + table_w - 1, table_y + 2, C_WOOD_DK) # bottom edge
    c.set(table_x, table_y, C_WHITE) # specular reflection corner

    # Table legs: brushed stainless steel
    c.line(49, 37, 49, 51, C_STEEL_LT)
    c.line(59, 37, 59, 51, C_STEEL_LT)
    c.line(47, 37, 47, 54, C_SILVER)
    c.line(48, 37, 48, 54, C_GREY_LT)
    c.line(61, 37, 61, 54, C_SILVER)
    c.line(62, 37, 62, 54, C_GREY_LT)

    # Rubber foot pads
    c.rect(47, 54, 2, 2, C_BLACK)
    c.rect(61, 54, 2, 2, C_BLACK)
    c.set(49, 51, C_BLACK)
    c.set(59, 51, C_BLACK)

    # Lower utility shelf
    c.line(48, 47, 60, 47, C_GREY_LT)
    c.line(48, 48, 60, 48, C_STEEL_MID)

    # Floor shadow under table
    c.rect(46, 55, 4, 1, C_SLATE_DK)
    c.rect(60, 55, 4, 1, C_SLATE_DK)

    # Laundry supplies on lower shelf
    # Big orange Tide-style detergent bottle (x: 53, y: 43..46)
    c.rect(53, 43, 4, 4, C_ORANGE)
    c.line(53, 43, 53, 46, C_ORANGE_LT)
    c.set(54, 42, C_BLUE_DK)            # blue measuring cap
    c.set(55, 42, C_BLUE_DK)
    c.set(55, 44, C_YELLOW)             # yellow target logo
    
    # Blue fabric softener bottle (x: 50, y: 44..46)
    c.rect(50, 44, 2, 3, C_CYAN_MID)
    c.set(50, 44, C_TUBE_LT)

    # =========================================================================
    # 7. LAUNDRY BASKET ON FOLDING TABLE (x: 50 .. 61, y: 25 .. 33)
    # Clean plastic laundry basket with diamond vents and colorful clothes
    # =========================================================================
    # Folded laundry stacks on left side of table (x: 46..49, y: 30..33)
    c.rect(46, 32, 4, 2, C_YELLOW)
    c.line(46, 32, 49, 32, C_YELLOW_LT)
    c.rect(46, 30, 4, 2, C_PURPLE)
    c.line(46, 30, 49, 30, C_WHITE_OFF)

    # Plastic laundry basket body
    b_x = 50
    b_y = 25
    b_w = 12
    
    # Top rim
    c.rect(b_x, b_y, b_w, 2, C_BSK_MID)
    c.line(b_x, b_y, b_x + b_w - 1, b_y, C_BSK_HI)
    c.line(b_x, b_y + 1, b_x + b_w - 1, b_y + 1, C_BSK_DK)
    # Cutout handles on the sides
    c.set(b_x + 1, b_y, C_SLATE_DK)
    c.set(b_x + b_w - 2, b_y, C_SLATE_DK)

    # Tapered basket body
    c.rect(b_x + 1, b_y + 2, b_w - 2, 7, C_BSK_MID)
    c.line(b_x + 1, b_y + 2, b_x + 1, b_y + 8, C_BSK_HI) # left highlight
    c.line(b_x + b_w - 2, b_y + 2, b_x + b_w - 2, b_y + 8, C_BSK_DK) # right shadow
    c.line(b_x + 2, b_y + 8, b_x + b_w - 3, b_y + 8, C_BSK_DK) # bottom rim

    # Ventilation holes (staggered pattern)
    for hx in [b_x + 3, b_x + 6, b_x + 9]:
        c.set(hx, b_y + 3, C_BSK_HOLE)
    for hx in [b_x + 2, b_x + 5, b_x + 8]:
        c.set(hx, b_y + 5, C_BSK_HOLE)
    for hx in [b_x + 3, b_x + 6, b_x + 9]:
        c.set(hx, b_y + 7, C_BSK_HOLE)

    # Overflowing colorful laundry in the basket:
    c.rect(b_x + 2, b_y - 3, 4, 4, C_RED)
    c.line(b_x + 2, b_y - 3, b_x + 5, b_y - 3, C_RED_LT)
    c.rect(b_x + 6, b_y - 2, 4, 3, C_BLUE)
    c.line(b_x + 6, b_y - 2, b_x + 9, b_y - 2, C_BLUE_LT)
    c.rect(b_x + 8, b_y - 3, 3, 3, C_YELLOW)
    c.set(b_x + 9, b_y - 4, C_YELLOW_LT)
    # White cloth/towel folded over the front rim:
    c.rect(b_x + 3, b_y, 3, 5, C_WHITE)
    c.line(b_x + 3, b_y + 4, b_x + 5, b_y + 4, C_SILVER)

    # Basket shadow on table
    c.line(b_x + 1, b_y + 9, b_x + b_w - 2, b_y + 9, C_WOOD_DK)

    # =========================================================================
    # 8. FOREGROUND ROLLING WIRE CART (x: 27 .. 39, y: 47 .. 61)
    # =========================================================================
    cart_x = 27
    cart_w = 12
    cart_y = 47
    
    # Push handle on left side of cart
    c.line(cart_x - 1, cart_y - 2, cart_x - 1, cart_y + 1, C_SILVER)
    c.set(cart_x, cart_y - 2, C_WHITE)
    
    # Chrome upper bumper rim
    c.rect(cart_x, cart_y, cart_w, 2, C_GREY_LT)
    c.line(cart_x, cart_y, cart_x + cart_w - 1, cart_y, C_WHITE)

    # Laundry inside wire cart
    c.rect(cart_x + 1, cart_y + 2, cart_w - 2, 7, C_SLATE_DK)
    c.rect(cart_x + 2, cart_y + 3, 4, 4, C_PINK)       # pink shirt
    c.set(cart_x + 3, cart_y + 2, C_WHITE_OFF)
    c.rect(cart_x + 6, cart_y + 4, 4, 4, C_CYAN_MID)   # cyan towel
    c.set(cart_x + 7, cart_y + 3, C_GLOW_CYAN)

    # Chrome wire grid bars
    for wx in range(cart_x + 1, cart_x + cart_w - 1, 2):
        c.line(wx, cart_y + 2, wx, cart_y + 8, C_SILVER)
    c.line(cart_x + 1, cart_y + 5, cart_x + cart_w - 2, cart_y + 5, C_SILVER)
    c.line(cart_x + 1, cart_y + 8, cart_x + cart_w - 2, cart_y + 8, C_STEEL_LT)

    # Cart tubular legs
    c.line(cart_x, cart_y + 2, cart_x, cart_y + 11, C_GREY_MID)
    c.line(cart_x + cart_w - 1, cart_y + 2, cart_x + cart_w - 1, cart_y + 11, C_GREY_MID)
    c.line(cart_x, cart_y + 11, cart_x + cart_w - 1, cart_y + 11, C_STEEL_MID)

    # Caster wheels
    c.set(cart_x, cart_y + 12, C_BLACK)
    c.set(cart_x + 1, cart_y + 12, C_STEEL_MID)
    c.set(cart_x + cart_w - 2, cart_y + 12, C_STEEL_MID)
    c.set(cart_x + cart_w - 1, cart_y + 12, C_BLACK)

    # Cart shadow on floor
    c.rect(cart_x - 1, cart_y + 13, cart_w + 2, 1, C_BLACK)

    view(c)
    finish(c)
    return c

c = build_laundromat()
