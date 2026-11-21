from pixelbench_api import *

W, H = 260, 140

def draw_knife(c, tx, ty, alpha=255):
    """Draw a knife pointing RIGHT with tip at (tx, ty). Cutting edge faces DOWN."""
    
    # --- BLADE ---
    # The blade is a wedge shape: 
    # - Spine at the top, nearly horizontal
    # - Cutting edge at the bottom - this is the sharp part facing DOWN
    # - The tip at (tx, ty) - the knife POINTS to the RIGHT
    
    # Blade main surface (light blue)
    c.poly([(tx-80, ty+4), (tx, ty), (tx-80, ty+18)], (204, 211, 248, alpha))
    
    # Cutting edge line (darker - this is the SHARP EDGE at the BOTTOM)
    c.line(tx-78, ty+16, tx-3, ty+3, (149, 159, 213, alpha))
    
    # Spine highlight on top
    c.line(tx-77, ty+6, tx-4, ty+2, (164, 173, 217, alpha))

    # --- GUARD ---
    c.rect(tx-88, ty+3, 9, 19, (124, 128, 149, alpha))
    
    # --- GRIP ---
    c.poly([(tx-88, ty+4), (tx-132, ty+6), (tx-130, ty+21), (tx-87, ty+22)], (92, 96, 115, alpha))
    
    # Grip texture
    c.line(tx-84, ty+10, tx-127, ty+12, (51, 55, 77, alpha))
    c.line(tx-84, ty+14, tx-125, ty+16, (51, 55, 77, alpha))
    c.line(tx-84, ty+18, tx-123, ty+20, (51, 55, 77, alpha))

def draw_hand(c, tx, ty):
    """Draw a hand gripping the knife handle."""
    h1 = (59, 63, 85, 255)
    h2 = (51, 55, 77, 255)
    c.poly([(tx-135, ty+4), (tx-130, ty+2), (tx-128, ty+32), (tx-134, ty+34)], h1)
    c.poly([(tx-126, ty+3), (tx-121, ty+2), (tx-119, ty+30), (tx-124, ty+31)], h1)
    c.poly([(tx-118, ty+5), (tx-114, ty+3), (tx-113, ty+30), (tx-117, ty+31)], h1)
    c.line(tx-95, ty+8, tx-113, ty+10, (51, 55, 77, 255))
    c.line(tx-95, ty+12, tx-111, ty+14, h2)

def draw_knife_and_hand(c, tx, ty):
    """Draw the complete knife thrusting RIGHT with hand."""
    draw_knife(c, tx, ty, 255)
    draw_hand(c, tx, ty)

# === Afterimages (from back to front, increasingly transparent) ===
after4 = new_canvas(W, H)
draw_knife(after4, 115, 62, 55)

after3 = new_canvas(W, H)
draw_knife(after3, 148, 58, 95)

after2 = new_canvas(W, H)
draw_knife(after2, 178, 54, 140)

after1 = new_canvas(W, H)
draw_knife(after1, 200, 51, 200)

# === White slash effect ===
sl = new_canvas(W, H)
sl.line(40, 30, 242, 44, (255, 255, 255, 200))
sl.line(50, 20, 235, 36, (255, 255, 255, 160))
sl.line(35, 48, 225, 40, (255, 255, 255, 180))
sl.line(55, 16, 218, 38, (255, 255, 255, 140))

# === Main knife + hand ===
main_knife = new_canvas(W, H)
draw_knife_and_hand(main_knife, 220, 48)

# === Final result ===
result = flatten([after4, after3, after2, after1, sl, main_knife], name='output')

print(result.stats_text())
finish(result)
