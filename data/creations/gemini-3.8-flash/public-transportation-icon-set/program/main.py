import sys
from pixelbench_api import new_canvas, view, finish

def build_art():
    c = new_canvas(64, 64, "#0b0f19", name="transit_icons")
    
    # ----------------- PALETTE -----------------
    C_CANVAS_BG = "#0b0f19"   # Dark obsidian canvas
    
    # Card / Frame colors
    C_CARD_BG = "#131a26"     # Deep transit slate navy
    C_CARD_BORDER = "#222d3d" # Outer edge border
    C_CARD_HI = "#33445c"     # Card top/left highlight bevel
    C_CARD_SH = "#0c111a"     # Card bottom/right shadow bevel
    
    # Shared Icon Palette
    C_WHITE = "#ffffff"       # Crisp primary white
    C_LIGHT_BLUE = "#dbeafe"  # Soft sky white / highlight
    C_CYAN = "#00d2ff"        # Vibrant transit cyan
    C_CYAN_DARK = "#0284c7"   # Deep cyan / metro blue
    C_AMBER = "#f59e0b"       # Transit amber / warm yellow
    C_AMBER_LIGHT = "#fef08a" # Bright yellow highlight
    C_GREEN = "#10b981"       # Subway signal green
    C_RED = "#ef4444"         # Taillight red
    C_GRAY_LIGHT = "#94a3b8"  # Steel / rails / spokes
    C_GRAY_MID = "#475569"    # Mechanical mid slate
    C_GRAY_DARK = "#1e293b"   # Bumper / road / dark slate
    C_BLACK = "#070b12"       # Tires / deep glass / shadows

    # Helper: draw a 28x28 rounded card at (tx, ty)
    def draw_card(tx, ty):
        cuts = {0: 4, 1: 2, 2: 1, 3: 1}
        for dy in range(28):
            cut = cuts.get(dy, cuts.get(27 - dy, 0))
            for dx in range(cut, 28 - cut):
                c.set(tx + dx, ty + dy, C_CARD_BG)
        
        # Bevel / border
        for dy in range(28):
            cut = cuts.get(dy, cuts.get(27 - dy, 0))
            x_left = cut
            x_right = 27 - cut
            
            for dx in range(cut, 28 - cut):
                prev_cut = cuts.get(dy - 1, cuts.get(27 - (dy - 1), 0)) if dy > 0 else 999
                next_cut = cuts.get(dy + 1, cuts.get(27 - (dy + 1), 0)) if dy < 27 else 999
                
                is_edge = (dy == 0 or dy == 27 or dx == x_left or dx == x_right or
                           dx < prev_cut or dx > 27 - prev_cut or
                           dx < next_cut or dx > 27 - next_cut)
                
                if is_edge:
                    if dy <= 2 or (dx <= 2 and dy < 24):
                        c.set(tx + dx, ty + dy, C_CARD_HI)
                    elif dy >= 25 or (dx >= 25 and dy > 3):
                        c.set(tx + dx, ty + dy, C_CARD_SH)
                    else:
                        c.set(tx + dx, ty + dy, C_CARD_BORDER)

    # =========================================================
    # 1. BUS ICON (Top-Left: tx=2, ty=2)
    # =========================================================
    def draw_bus(tx, ty):
        # Road plane baseline at y=21..22
        for x in range(4, 24):
            c.set(tx + x, ty + 22, C_GRAY_DARK)
        # Ground shadow under bus
        for x in range(5, 23):
            c.set(tx + x, ty + 21, C_BLACK)

        # Wheels / Tires (left: 6..8, right: 19..21, y=18..20)
        # Left tire
        for y in range(18, 21):
            for x in range(6, 9):
                c.set(tx + x, ty + y, C_BLACK)
        c.set(tx + 7, ty + 19, C_GRAY_LIGHT) # Hubcap
        
        # Right tire
        for y in range(18, 21):
            for x in range(19, 22):
                c.set(tx + x, ty + y, C_BLACK)
        c.set(tx + 20, ty + 19, C_GRAY_LIGHT) # Hubcap

        # Low chassis undercarriage shadow
        for x in range(9, 19):
            c.set(tx + x, ty + 19, C_BLACK)
            c.set(tx + x, ty + 20, C_BLACK)

        # Bus Roof AC Unit
        for x in range(11, 17):
            c.set(tx + x, ty + 4, C_LIGHT_BLUE)
        c.set(tx + 12, ty + 4, C_WHITE)
        c.set(tx + 15, ty + 4, C_WHITE)

        # Roof outline
        for x in range(8, 20):
            c.set(tx + x, ty + 5, C_WHITE)
        c.set(tx + 7, ty + 6, C_WHITE)
        c.set(tx + 20, ty + 6, C_WHITE)

        # Destination sign box (dy=6..7, dx=9..18)
        for y in [6, 7]:
            for x in range(9, 19):
                c.set(tx + x, ty + y, C_BLACK)
        # LED route text (amber glow)
        for x in [10, 11, 13, 14, 16, 17]:
            c.set(tx + x, ty + 6, C_AMBER)
            c.set(tx + x, ty + 7, C_AMBER_LIGHT)

        # White roof corners flanking destination sign
        for x in range(6, 9):
            c.set(tx + x, ty + 7, C_WHITE)
        for x in range(19, 22):
            c.set(tx + x, ty + 7, C_WHITE)

        # Windshield frame & pillars (dy=8..13)
        for y in range(8, 14):
            c.set(tx + 6, ty + y, C_WHITE)
            c.set(tx + 21, ty + y, C_WHITE)

        # Windshield glass (dy=8..13, dx=7..20)
        for y in range(8, 14):
            for x in range(7, 21):
                c.set(tx + x, ty + y, C_BLACK)

        # Center windshield divider & wipers
        for y in range(8, 14):
            c.set(tx + 13, ty + y, C_GRAY_MID)
            c.set(tx + 14, ty + y, C_GRAY_MID)
        # Wipers resting at bottom
        c.set(tx + 9, ty + 13, C_GRAY_LIGHT)
        c.set(tx + 10, ty + 13, C_GRAY_LIGHT)
        c.set(tx + 17, ty + 13, C_GRAY_LIGHT)
        c.set(tx + 18, ty + 13, C_GRAY_LIGHT)

        # Windshield reflections (cyan streaks)
        c.set(tx + 8, ty + 12, C_CYAN)
        c.set(tx + 9, ty + 11, C_CYAN)
        c.set(tx + 10, ty + 10, C_CYAN)
        c.set(tx + 11, ty + 9, C_LIGHT_BLUE)
        
        c.set(tx + 15, ty + 12, C_CYAN)
        c.set(tx + 16, ty + 11, C_CYAN)
        c.set(tx + 17, ty + 10, C_CYAN)
        c.set(tx + 18, ty + 9, C_LIGHT_BLUE)

        # Side mirrors
        c.set(tx + 4, ty + 9, C_GRAY_LIGHT)
        c.set(tx + 4, ty + 10, C_WHITE)
        c.set(tx + 4, ty + 11, C_WHITE)
        c.set(tx + 5, ty + 10, C_GRAY_MID)
        
        c.set(tx + 23, ty + 9, C_GRAY_LIGHT)
        c.set(tx + 23, ty + 10, C_WHITE)
        c.set(tx + 23, ty + 11, C_WHITE)
        c.set(tx + 22, ty + 10, C_GRAY_MID)

        # Front body panel: Transit stripe (dy=14)
        for x in range(6, 22):
            c.set(tx + x, ty + 14, C_CYAN)

        # Main front white fascia (dy=15..17)
        for y in range(15, 18):
            for x in range(6, 22):
                c.set(tx + x, ty + y, C_WHITE)

        # Dual headlights
        # Left
        c.set(tx + 7, ty + 15, C_WHITE)
        c.set(tx + 8, ty + 15, C_AMBER_LIGHT)
        c.set(tx + 7, ty + 16, C_AMBER_LIGHT)
        c.set(tx + 8, ty + 16, C_AMBER)
        # Right
        c.set(tx + 19, ty + 15, C_AMBER_LIGHT)
        c.set(tx + 20, ty + 15, C_WHITE)
        c.set(tx + 19, ty + 16, C_AMBER)
        c.set(tx + 20, ty + 16, C_AMBER_LIGHT)

        # Grille & transit emblem in center
        for x in range(11, 17):
            c.set(tx + x, ty + 16, C_GRAY_MID)
            c.set(tx + x, ty + 17, C_BLACK)
        c.set(tx + 13, ty + 16, C_CYAN)
        c.set(tx + 14, ty + 16, C_CYAN)
        c.set(tx + 13, ty + 17, C_WHITE)
        c.set(tx + 14, ty + 17, C_WHITE)

        # Heavy transit bumper (dy=18)
        for x in range(6, 22):
            c.set(tx + x, ty + 18, C_GRAY_MID)
        c.set(tx + 6, ty + 18, C_BLACK)
        c.set(tx + 21, ty + 18, C_BLACK)

    # =========================================================
    # 2. SUBWAY ICON (Top-Right: tx=34, ty=2)
    # =========================================================
    def draw_subway(tx, ty):
        # Arched tunnel portal outline framing the train
        tunnel_arch_outline = [
            (3, 9, 18),
            (4, 7, 8), (4, 19, 20),
            (5, 6, 6), (5, 21, 21),
            (6, 5, 5), (6, 22, 22),
            (7, 4, 4), (7, 23, 23),
            (8, 4, 4), (8, 23, 23),
            (9, 4, 4), (9, 23, 23),
            (10, 4, 4), (10, 23, 23),
            (11, 4, 4), (11, 23, 23),
            (12, 4, 4), (12, 23, 23),
            (13, 4, 4), (13, 23, 23),
            (14, 4, 4), (14, 23, 23),
            (15, 4, 4), (15, 23, 23),
            (16, 4, 4), (16, 23, 23),
            (17, 4, 4), (17, 23, 23),
            (18, 4, 4), (18, 23, 23),
        ]
        for item in tunnel_arch_outline:
            y = item[0]
            for i in range(1, len(item), 2):
                x0, x1 = item[i], item[i+1]
                for x in range(x0, x1 + 1):
                    c.set(tx + x, ty + y, C_CARD_HI)

        # Tunnel signal light on left wall (Green LED)
        c.set(tx + 4, ty + 9, C_GRAY_DARK)
        c.set(tx + 4, ty + 10, C_GREEN)
        c.set(tx + 4, ty + 11, C_GRAY_DARK)

        # Pantograph / overhead power contact on roof
        c.set(tx + 13, ty + 3, C_GRAY_LIGHT)
        c.set(tx + 14, ty + 3, C_GRAY_LIGHT)
        c.set(tx + 12, ty + 4, C_GRAY_MID)
        c.set(tx + 15, ty + 4, C_GRAY_MID)
        c.set(tx + 11, ty + 5, C_GRAY_MID)
        c.set(tx + 16, ty + 5, C_GRAY_MID)

        # Train aerodynamic roof dome (dy=5..7)
        for x in range(9, 19):
            c.set(tx + x, ty + 5, C_WHITE)
        for x in range(8, 20):
            c.set(tx + x, ty + 6, C_WHITE)
        for x in range(7, 21):
            c.set(tx + x, ty + 7, C_WHITE)

        # Center route indicator light at top of train
        c.set(tx + 13, ty + 5, C_CYAN)
        c.set(tx + 14, ty + 5, C_CYAN)
        c.set(tx + 12, ty + 6, C_AMBER)
        c.set(tx + 15, ty + 6, C_AMBER)

        # Panoramic aerodynamic train cab windshield (dy=8..13)
        for y in range(8, 14):
            c.set(tx + 6, ty + y, C_WHITE)
            c.set(tx + 21, ty + y, C_WHITE)
        c.set(tx + 7, ty + 8, C_WHITE)
        c.set(tx + 20, ty + 8, C_WHITE)

        for y in range(8, 14):
            for x in range(7, 21):
                if not (y == 8 and (x == 7 or x == 20)):
                    c.set(tx + x, ty + y, C_BLACK)

        # Broad aerodynamic reflection sweeps across the continuous windshield
        c.set(tx + 9, ty + 12, C_CYAN)
        c.set(tx + 10, ty + 11, C_CYAN)
        c.set(tx + 11, ty + 10, C_CYAN)
        c.set(tx + 12, ty + 9, C_LIGHT_BLUE)
        c.set(tx + 13, ty + 9, C_WHITE)
        c.set(tx + 14, ty + 9, C_WHITE)
        c.set(tx + 15, ty + 9, C_LIGHT_BLUE)
        c.set(tx + 16, ty + 10, C_CYAN)
        c.set(tx + 17, ty + 11, C_CYAN)
        c.set(tx + 18, ty + 12, C_CYAN)

        # Lower train front / nose (dy=14..18)
        # Bold transit line chevron stripe
        for x in range(6, 22):
            c.set(tx + x, ty + 14, C_CYAN)
        c.set(tx + 13, ty + 15, C_CYAN)
        c.set(tx + 14, ty + 15, C_CYAN)

        # White lower nose fascia
        for y in range(15, 18):
            for x in range(6, 22):
                if not (y == 15 and (x == 13 or x == 14)):
                    c.set(tx + x, ty + y, C_WHITE)

        # High-intensity twin LED headlights
        # Left
        c.set(tx + 7, ty + 15, C_WHITE)
        c.set(tx + 8, ty + 15, C_AMBER_LIGHT)
        c.set(tx + 7, ty + 16, C_AMBER_LIGHT)
        c.set(tx + 8, ty + 16, C_AMBER)
        # Right
        c.set(tx + 19, ty + 15, C_AMBER_LIGHT)
        c.set(tx + 20, ty + 15, C_WHITE)
        c.set(tx + 19, ty + 16, C_AMBER)
        c.set(tx + 20, ty + 16, C_AMBER_LIGHT)

        # Metro round emblem / logo in center
        c.set(tx + 13, ty + 16, C_CYAN_DARK)
        c.set(tx + 14, ty + 16, C_CYAN_DARK)
        c.set(tx + 13, ty + 17, C_CYAN)
        c.set(tx + 14, ty + 17, C_CYAN)

        # Lower skirt & anti-climber buffer (dy=18)
        for x in range(7, 21):
            c.set(tx + x, ty + 18, C_GRAY_MID)
        # Central coupler
        c.set(tx + 13, ty + 19, C_GRAY_LIGHT)
        c.set(tx + 14, ty + 19, C_GRAY_LIGHT)

        # Train steel wheels / bogie visible on track (dy=19)
        c.set(tx + 8, ty + 19, C_BLACK)
        c.set(tx + 9, ty + 19, C_GRAY_LIGHT)
        c.set(tx + 18, ty + 19, C_GRAY_LIGHT)
        c.set(tx + 19, ty + 19, C_BLACK)

        # Railway Track & Rails in perspective (dy=20..22)
        # Tie 1 at y=20
        for x in range(7, 21):
            c.set(tx + x, ty + 20, C_GRAY_DARK)
        for x in [7, 10, 13, 14, 17, 20]:
            c.set(tx + x, ty + 20, C_GRAY_MID)
            
        # Tie 2 at y=22 (wider in perspective!)
        for x in range(5, 23):
            c.set(tx + x, ty + 22, C_GRAY_DARK)
        for x in [5, 8, 11, 12, 15, 16, 19, 22]:
            c.set(tx + x, ty + 22, C_GRAY_MID)
                
        # Steel rails gleaming in perspective:
        c.set(tx + 8, ty + 20, C_GRAY_LIGHT)
        c.set(tx + 9, ty + 20, C_WHITE)
        c.set(tx + 18, ty + 20, C_WHITE)
        c.set(tx + 19, ty + 20, C_GRAY_LIGHT)

        c.set(tx + 7, ty + 21, C_GRAY_LIGHT)
        c.set(tx + 8, ty + 21, C_WHITE)
        c.set(tx + 19, ty + 21, C_WHITE)
        c.set(tx + 20, ty + 21, C_GRAY_LIGHT)

        c.set(tx + 6, ty + 22, C_GRAY_LIGHT)
        c.set(tx + 7, ty + 22, C_WHITE)
        c.set(tx + 20, ty + 22, C_WHITE)
        c.set(tx + 21, ty + 22, C_GRAY_LIGHT)

    # =========================================================
    # 3. BICYCLE ICON (Bottom-Left: tx=2, ty=34)
    # =========================================================
    def draw_bicycle(tx, ty):
        # Road plane at baseline y=21..22
        for x in range(4, 24):
            c.set(tx + x, ty + 22, C_GRAY_DARK)
        for x in range(4, 9):
            c.set(tx + x, ty + 22, C_BLACK)
        for x in range(19, 24):
            c.set(tx + x, ty + 22, C_BLACK)

        # Helper to draw a crisp 1-pixel thick 9x9 round wheel
        def draw_bike_wheel(cx, cy):
            c.set(tx + cx - 1, ty + cy - 4, C_WHITE)
            c.set(tx + cx,     ty + cy - 4, C_WHITE)
            c.set(tx + cx + 1, ty + cy - 4, C_WHITE)

            c.set(tx + cx - 2, ty + cy - 3, C_WHITE)
            c.set(tx + cx + 2, ty + cy - 3, C_WHITE)

            c.set(tx + cx - 3, ty + cy - 2, C_WHITE)
            c.set(tx + cx + 3, ty + cy - 2, C_WHITE)

            for dy in [-1, 0, 1]:
                c.set(tx + cx - 4, ty + cy + dy, C_WHITE)
                c.set(tx + cx + 4, ty + cy + dy, C_WHITE)

            c.set(tx + cx - 3, ty + cy + 2, C_WHITE)
            c.set(tx + cx + 3, ty + cy + 2, C_WHITE)

            c.set(tx + cx - 2, ty + cy + 3, C_WHITE)
            c.set(tx + cx + 2, ty + cy + 3, C_WHITE)

            c.set(tx + cx - 1, ty + cy + 4, C_WHITE)
            c.set(tx + cx,     ty + cy + 4, C_WHITE)
            c.set(tx + cx + 1, ty + cy + 4, C_WHITE)

            # Center hub (cyan)
            c.set(tx + cx, ty + cy, C_CYAN)
            # Thin subtle spokes
            c.set(tx + cx - 2, ty + cy, C_GRAY_LIGHT)
            c.set(tx + cx - 1, ty + cy, C_GRAY_LIGHT)
            c.set(tx + cx + 1, ty + cy, C_GRAY_LIGHT)
            c.set(tx + cx + 2, ty + cy, C_GRAY_LIGHT)
            c.set(tx + cx, ty + cy - 2, C_GRAY_LIGHT)
            c.set(tx + cx, ty + cy - 1, C_GRAY_LIGHT)
            c.set(tx + cx, ty + cy + 1, C_GRAY_LIGHT)
            c.set(tx + cx, ty + cy + 2, C_GRAY_LIGHT)

        # Wheels:
        # Rear wheel: (cx=6, cy=17)
        # Front wheel: (cx=21, cy=17)
        draw_bike_wheel(6, 17)
        draw_bike_wheel(21, 17)

        # Bicycle Frame (Cyan `#00d2ff`)
        # Chainstay: (6, 17) -> (13, 17)
        for x in range(7, 13):
            c.set(tx + x, ty + 17, C_CYAN)

        # Bottom bracket & crank (13, 17)
        c.set(tx + 13, ty + 17, C_WHITE)
        # Pedals
        c.set(tx + 13, ty + 15, C_WHITE)
        c.set(tx + 12, ty + 15, C_GRAY_LIGHT)
        c.set(tx + 13, ty + 19, C_WHITE)
        c.set(tx + 14, ty + 19, C_GRAY_LIGHT)

        # Seatstay: (6, 17) -> (10, 11)
        c.set(tx + 7, ty + 15, C_CYAN)
        c.set(tx + 8, ty + 14, C_CYAN)
        c.set(tx + 9, ty + 13, C_CYAN)
        c.set(tx + 9, ty + 12, C_CYAN)
        c.set(tx + 10, ty + 11, C_CYAN)

        # Seat tube: (13, 17) -> (10, 11)
        c.set(tx + 12, ty + 15, C_CYAN)
        c.set(tx + 12, ty + 14, C_CYAN)
        c.set(tx + 11, ty + 13, C_CYAN)
        c.set(tx + 11, ty + 12, C_CYAN)

        # Seatpost & Saddle
        c.set(tx + 10, ty + 10, C_GRAY_LIGHT)
        c.set(tx + 10, ty + 9, C_GRAY_LIGHT)
        # Saddle cushion (dy=8)
        for x in range(8, 13):
            c.set(tx + x, ty + 8, C_WHITE)
        c.set(tx + 7, ty + 9, C_GRAY_MID)
        c.set(tx + 13, ty + 9, C_GRAY_MID)

        # Top tube: (10, 11) -> (18, 10)
        c.set(tx + 11, ty + 11, C_CYAN)
        c.set(tx + 12, ty + 11, C_CYAN)
        c.set(tx + 13, ty + 11, C_CYAN)
        c.set(tx + 14, ty + 10, C_CYAN)
        c.set(tx + 15, ty + 10, C_CYAN)
        c.set(tx + 16, ty + 10, C_CYAN)
        c.set(tx + 17, ty + 10, C_CYAN)

        # Down tube: (13, 17) -> (18, 10)
        c.set(tx + 14, ty + 15, C_CYAN)
        c.set(tx + 15, ty + 14, C_CYAN)
        c.set(tx + 16, ty + 13, C_CYAN)
        c.set(tx + 16, ty + 12, C_CYAN)
        c.set(tx + 17, ty + 11, C_CYAN)

        # Head tube: (18, 9..11)
        c.set(tx + 18, ty + 9, C_CYAN)
        c.set(tx + 18, ty + 10, C_CYAN)
        c.set(tx + 18, ty + 11, C_CYAN)

        # Front fork: (18, 11) -> (21, 17)
        c.set(tx + 19, ty + 12, C_CYAN)
        c.set(tx + 19, ty + 13, C_CYAN)
        c.set(tx + 20, ty + 14, C_CYAN)
        c.set(tx + 20, ty + 15, C_CYAN)
        c.set(tx + 21, ty + 16, C_CYAN)

        # Stem & Handlebars
        c.set(tx + 18, ty + 8, C_GRAY_LIGHT)
        c.set(tx + 17, ty + 7, C_WHITE)
        c.set(tx + 18, ty + 7, C_WHITE)
        c.set(tx + 19, ty + 7, C_WHITE)
        c.set(tx + 20, ty + 7, C_WHITE)
        c.set(tx + 21, ty + 8, C_GRAY_MID) # grip

        # Front LED light (amber)
        c.set(tx + 21, ty + 9, C_AMBER_LIGHT)
        c.set(tx + 22, ty + 9, C_AMBER)

        # Rear taillight (red)
        c.set(tx + 8, ty + 11, C_RED)

    # =========================================================
    # 4. PEDESTRIAN ICON (Bottom-Right: tx=34, ty=34)
    # =========================================================
    def draw_pedestrian(tx, ty):
        # 4 zebra crossing stripes (dy=21..22)
        for stripe_x in [5, 10, 15, 20]:
            for x in range(stripe_x, stripe_x + 3):
                c.set(tx + x, ty + 21, C_WHITE)
                c.set(tx + x, ty + 22, C_GRAY_MID)

        # Asphalt underneath
        for x in range(4, 24):
            c.set(tx + x, ty + 23, C_BLACK)

        # FLOATING CIRCULAR HEAD (4x4 disc)
        c.set(tx + 13, ty + 4, C_LIGHT_BLUE)
        c.set(tx + 14, ty + 4, C_LIGHT_BLUE)
        for y in [5, 6]:
            for x in range(12, 16):
                c.set(tx + x, ty + y, C_WHITE)
        c.set(tx + 13, ty + 7, C_WHITE)
        c.set(tx + 14, ty + 7, C_WHITE)

        # dy=8 is empty space (floating head!)

        # TORSO (dy=9..14)
        for y in [9, 10]:
            for x in range(12, 16):
                c.set(tx + x, ty + y, C_CYAN)
        for y in range(11, 15):
            for x in range(13, 17):
                c.set(tx + x, ty + y, C_CYAN)
        # Clean white zipper / collar accent
        c.set(tx + 14, ty + 9, C_WHITE)
        c.set(tx + 14, ty + 10, C_WHITE)
        c.set(tx + 15, ty + 11, C_WHITE)
        c.set(tx + 15, ty + 12, C_WHITE)
        c.set(tx + 15, ty + 13, C_WHITE)
        c.set(tx + 15, ty + 14, C_WHITE)

        # ARMS:
        # Back arm:
        c.set(tx + 11, ty + 10, C_CYAN_DARK)
        c.set(tx + 10, ty + 11, C_CYAN_DARK)
        c.set(tx + 9, ty + 12, C_CYAN)
        c.set(tx + 9, ty + 13, C_WHITE)      # hand

        # Front arm:
        c.set(tx + 16, ty + 10, C_CYAN)
        c.set(tx + 17, ty + 11, C_CYAN)
        c.set(tx + 18, ty + 11, C_CYAN)
        c.set(tx + 19, ty + 12, C_WHITE)     # hand

        # HIPS:
        for x in range(13, 17):
            c.set(tx + x, ty + 15, C_GRAY_MID)

        # LEGS:
        # Forward Leg (stepping forward onto crosswalk):
        c.set(tx + 15, ty + 16, C_WHITE)
        c.set(tx + 16, ty + 16, C_WHITE)
        c.set(tx + 16, ty + 17, C_WHITE)
        c.set(tx + 17, ty + 17, C_WHITE) # knee
        # Shin
        c.set(tx + 16, ty + 18, C_WHITE)
        c.set(tx + 17, ty + 18, C_WHITE)
        c.set(tx + 16, ty + 19, C_WHITE)
        c.set(tx + 17, ty + 19, C_WHITE)
        # Foot stepping firmly onto crosswalk stripe at 15..17
        c.set(tx + 16, ty + 20, C_CYAN)
        c.set(tx + 17, ty + 20, C_WHITE)
        c.set(tx + 18, ty + 20, C_WHITE)

        # Back Leg (trailing with bent knee and pushing off):
        c.set(tx + 13, ty + 16, C_WHITE)
        c.set(tx + 12, ty + 16, C_WHITE)
        c.set(tx + 12, ty + 17, C_WHITE)
        c.set(tx + 11, ty + 17, C_WHITE) # knee
        # Shin
        c.set(tx + 11, ty + 18, C_WHITE)
        c.set(tx + 10, ty + 18, C_WHITE)
        c.set(tx + 10, ty + 19, C_WHITE)
        c.set(tx + 9,  ty + 19, C_WHITE)
        # Foot pushing off at toe (on stripe at 10..12)
        c.set(tx + 9, ty + 20, C_CYAN)
        c.set(tx + 10, ty + 20, C_WHITE)

    # Render cards and icons
    tiles = [
        (2, 2, draw_bus),
        (34, 2, draw_subway),
        (2, 34, draw_bicycle),
        (34, 34, draw_pedestrian),
    ]

    for tx, ty, fn in tiles:
        draw_card(tx, ty)
        fn(tx, ty)

    return c

c = build_art()
view(c)
finish(c)
