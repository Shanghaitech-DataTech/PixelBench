from pixelbench_api import *

# Create a 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None, name="cheerleader_4view")

# Define color palette
skin = c.color("#f5d0b0", "skin")
hair = c.color("#4a3020", "hair")
outfit_main = c.color("#e63946", "outfit_red")
outfit_white = c.color("#ffffff", "outfit_white")
outline = c.color("#1a1a1a", "outline")
shoes = c.color("#2a2a2a", "shoes")
socks = c.color("#ffffff", "socks")
pom_red = c.color("#ff4757", "pom_red")
pom_yellow = c.color("#ffd93d", "pom_yellow")
cheek = c.color("#ffb3a7", "cheek")

# Each quadrant is 32x32, character centered in each
# Top row: front (left), back (right)
# Bottom row: left side (left), right side (right)

def draw_front(cx, cy):
    """Draw front view of cheerleader centered at (cx, cy)"""
    # Hair back (behind head)
    c.rect(cx-6, cy-7, 12, 7, hair)
    c.rect(cx-7, cy-5, 2, 5, hair)
    c.rect(cx+5, cy-5, 2, 5, hair)
    
    # Body/dress
    c.rect(cx-5, cy, 10, 7, outfit_main)  # Main dress
    c.rect(cx-4, cy, 8, 3, outfit_white)  # White collar
    
    # Skirt - triangular shape
    c.poly([(cx-6, cy+6), (cx+6, cy+6), (cx+7, cy+11), (cx+4, cy+12), 
            (cx+1, cy+11), (cx-1, cy+12), (cx-4, cy+11), (cx-7, cy+12)], 
           outfit_main, fill=True)
    
    # Legs
    c.rect(cx-3, cy+11, 3, 5, skin)
    c.rect(cx+1, cy+11, 3, 5, skin)
    
    # Socks
    c.rect(cx-3, cy+14, 3, 3, socks)
    c.rect(cx+1, cy+14, 3, 3, socks)
    
    # Shoes
    c.rect(cx-4, cy+16, 4, 2, shoes)
    c.rect(cx+0, cy+16, 4, 2, shoes)
    
    # Head
    c.circle(cx, cy-4, 6, skin, fill=True)
    
    # Hair front/bangs
    c.rect(cx-6, cy-9, 12, 5, hair)
    c.rect(cx-5, cy-10, 10, 2, hair)
    
    # Eyes
    c.set(cx-2, cy-4, outline)
    c.set(cx-2, cy-3, outline)
    c.set(cx+2, cy-4, outline)
    c.set(cx+2, cy-3, outline)
    
    # Smile
    c.set(cx-2, cy-2, outline)
    c.set(cx-1, cy-1, outline)
    c.set(cx, cy-1, outline)
    c.set(cx+1, cy-1, outline)
    c.set(cx+2, cy-2, outline)
    
    # Cheeks
    c.set(cx-4, cy-3, cheek)
    c.set(cx+4, cy-3, cheek)
    
    # Arms up with pom-poms
    # Left arm
    c.set(cx-5, cy, skin)
    c.set(cx-6, cy-2, skin)
    c.set(cx-7, cy-4, skin)
    c.set(cx-8, cy-5, skin)
    c.set(cx-9, cy-6, skin)
    
    # Right arm
    c.set(cx+5, cy, skin)
    c.set(cx+6, cy-2, skin)
    c.set(cx+7, cy-4, skin)
    c.set(cx+8, cy-5, skin)
    c.set(cx+9, cy-6, skin)
    
    # Pom-poms
    c.circle(cx-9, cy-7, 3, pom_red, fill=True)
    c.circle(cx+9, cy-7, 3, pom_red, fill=True)
    
    # Pom-pom details (yellow highlights)
    c.set(cx-10, cy-7, pom_yellow)
    c.set(cx-9, cy-8, pom_yellow)
    c.set(cx-8, cy-6, pom_yellow)
    c.set(cx+10, cy-7, pom_yellow)
    c.set(cx+9, cy-8, pom_yellow)
    c.set(cx+8, cy-6, pom_yellow)

def draw_back(cx, cy):
    """Draw back view of cheerleader centered at (cx, cy)"""
    # Hair (long, flowing down back) - main feature of back view
    c.rect(cx-6, cy-8, 12, 14, hair)
    c.rect(cx-7, cy-6, 2, 12, hair)
    c.rect(cx+5, cy-6, 2, 12, hair)
    c.rect(cx-5, cy+4, 10, 3, hair)  # Hair ends
    
    # Body/dress back
    c.rect(cx-5, cy, 10, 7, outfit_main)
    c.rect(cx-4, cy, 8, 2, outfit_white)  # Collar back
    
    # Skirt (same as front)
    c.poly([(cx-6, cy+6), (cx+6, cy+6), (cx+7, cy+11), (cx+4, cy+12), 
            (cx+1, cy+11), (cx-1, cy+12), (cx-4, cy+11), (cx-7, cy+12)], 
           outfit_main, fill=True)
    
    # Legs
    c.rect(cx-3, cy+11, 3, 5, skin)
    c.rect(cx+1, cy+11, 3, 5, skin)
    
    # Socks
    c.rect(cx-3, cy+14, 3, 3, socks)
    c.rect(cx+1, cy+14, 3, 3, socks)
    
    # Shoes
    c.rect(cx-4, cy+16, 4, 2, shoes)
    c.rect(cx+0, cy+16, 4, 2, shoes)
    
    # Arms up with pom-poms (from behind - just arms visible)
    # Left arm
    c.set(cx-5, cy, skin)
    c.set(cx-6, cy-2, skin)
    c.set(cx-7, cy-4, skin)
    c.set(cx-8, cy-5, skin)
    c.set(cx-9, cy-6, skin)
    
    # Right arm
    c.set(cx+5, cy, skin)
    c.set(cx+6, cy-2, skin)
    c.set(cx+7, cy-4, skin)
    c.set(cx+8, cy-5, skin)
    c.set(cx+9, cy-6, skin)
    
    # Pom-poms
    c.circle(cx-9, cy-7, 3, pom_red, fill=True)
    c.circle(cx+9, cy-7, 3, pom_red, fill=True)
    
    # Pom-pom details
    c.set(cx-10, cy-7, pom_yellow)
    c.set(cx-9, cy-8, pom_yellow)
    c.set(cx+10, cy-7, pom_yellow)
    c.set(cx+9, cy-8, pom_yellow)

def draw_side_left(cx, cy):
    """Draw left side view of cheerleader centered at (cx, cy) - facing left"""
    # Hair (side view - flowing back/right)
    c.rect(cx-3, cy-8, 7, 5, hair)
    c.rect(cx+2, cy-5, 3, 8, hair)  # Hair flowing back
    
    # Head (side profile - facing left)
    c.ellipse(cx-1, cy-4, 5, 6, skin, fill=True)
    
    # Eye (side view - just a dot/line)
    c.set(cx-3, cy-4, outline)
    c.set(cx-3, cy-3, outline)
    
    # Small smile
    c.set(cx-2, cy-2, outline)
    c.set(cx-1, cy-1, outline)
    
    # Body (side view - narrower, facing left)
    c.rect(cx-2, cy, 5, 7, outfit_main)
    c.rect(cx-1, cy, 4, 2, outfit_white)
    
    # Skirt (side view)
    c.poly([(cx-3, cy+6), (cx+3, cy+6), (cx+4, cy+11), (cx+2, cy+12),
            (cx, cy+11), (cx-2, cy+12), (cx-3, cy+11)], 
           outfit_main, fill=True)
    
    # Legs (side view - both legs visible, front leg more prominent)
    c.rect(cx-1, cy+11, 3, 5, skin)  # Front leg
    c.rect(cx+2, cy+11, 2, 4, skin)  # Back leg partially visible
    
    # Socks
    c.rect(cx-1, cy+14, 3, 3, socks)
    c.rect(cx+2, cy+14, 2, 2, socks)
    
    # Shoes
    c.rect(cx-2, cy+16, 4, 2, shoes)
    c.rect(cx+1, cy+16, 3, 2, shoes)
    
    # Arms (side view - reaching up)
    # Front arm (left, more visible)
    c.set(cx-2, cy, skin)
    c.set(cx-3, cy-2, skin)
    c.set(cx-4, cy-4, skin)
    c.set(cx-5, cy-5, skin)
    c.set(cx-6, cy-6, skin)
    
    # Back arm (right, partially visible)
    c.set(cx+2, cy, skin)
    c.set(cx+3, cy-2, skin)
    c.set(cx+4, cy-4, skin)
    c.set(cx+5, cy-5, skin)
    c.set(cx+6, cy-6, skin)
    
    # Pom-poms (side view - ellipses)
    c.ellipse(cx-6, cy-7, 3, 3, pom_red, fill=True)
    c.ellipse(cx+6, cy-7, 3, 3, pom_red, fill=True)
    
    # Pom details
    c.set(cx-7, cy-7, pom_yellow)
    c.set(cx-6, cy-8, pom_yellow)
    c.set(cx+7, cy-7, pom_yellow)
    c.set(cx+6, cy-8, pom_yellow)

def draw_side_right(cx, cy):
    """Draw right side view of cheerleader centered at (cx, cy) - facing right"""
    # Hair (side view - flowing back/left)
    c.rect(cx-4, cy-8, 7, 5, hair)
    c.rect(cx-5, cy-5, 3, 8, hair)  # Hair flowing back
    
    # Head (side profile - facing right)
    c.ellipse(cx+1, cy-4, 5, 6, skin, fill=True)
    
    # Eye (side view - just a dot/line)
    c.set(cx+3, cy-4, outline)
    c.set(cx+3, cy-3, outline)
    
    # Small smile
    c.set(cx+2, cy-2, outline)
    c.set(cx+1, cy-1, outline)
    
    # Body (side view - narrower, facing right)
    c.rect(cx-3, cy, 5, 7, outfit_main)
    c.rect(cx-2, cy, 4, 2, outfit_white)
    
    # Skirt (side view)
    c.poly([(cx-3, cy+6), (cx+3, cy+6), (cx+4, cy+11), (cx+2, cy+12),
            (cx, cy+11), (cx-2, cy+12), (cx-3, cy+11)], 
           outfit_main, fill=True)
    
    # Legs (side view - both legs visible, front leg more prominent)
    c.rect(cx, cy+11, 3, 5, skin)  # Front leg
    c.rect(cx-3, cy+11, 2, 4, skin)  # Back leg partially visible
    
    # Socks
    c.rect(cx, cy+14, 3, 3, socks)
    c.rect(cx-3, cy+14, 2, 2, socks)
    
    # Shoes
    c.rect(cx-1, cy+16, 4, 2, shoes)
    c.rect(cx-4, cy+16, 3, 2, shoes)
    
    # Arms (side view - reaching up)
    # Front arm (right, more visible)
    c.set(cx+2, cy, skin)
    c.set(cx+3, cy-2, skin)
    c.set(cx+4, cy-4, skin)
    c.set(cx+5, cy-5, skin)
    c.set(cx+6, cy-6, skin)
    
    # Back arm (left, partially visible)
    c.set(cx-2, cy, skin)
    c.set(cx-3, cy-2, skin)
    c.set(cx-4, cy-4, skin)
    c.set(cx-5, cy-5, skin)
    c.set(cx-6, cy-6, skin)
    
    # Pom-poms (side view - ellipses)
    c.ellipse(cx-6, cy-7, 3, 3, pom_red, fill=True)
    c.ellipse(cx+6, cy-7, 3, 3, pom_red, fill=True)
    
    # Pom details
    c.set(cx-7, cy-7, pom_yellow)
    c.set(cx-6, cy-8, pom_yellow)
    c.set(cx+7, cy-7, pom_yellow)
    c.set(cx+6, cy-8, pom_yellow)

# Draw all four views in 2x2 grid
# Top-left: Front view (centered at 16, 14)
draw_front(16, 14)

# Top-right: Back view (centered at 48, 14)
draw_back(48, 14)

# Bottom-left: Left side view (centered at 16, 46)
draw_side_left(16, 46)

# Bottom-right: Right side view (centered at 48, 46)
draw_side_right(48, 46)

# Add dark outline around all opaque pixels
c.outline(outline)

# Check stats
print(c.stats_text())

# Submit the result
finish(c)
