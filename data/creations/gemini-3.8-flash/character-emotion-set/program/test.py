from pixelbench_api import *

# Let's test the improved bangs
def test_bangs():
    c = new_canvas(32, 32, background=None, name="test")
    
    # Palette
    C_OUTLINE = "#1a0e08"
    C_SKIN_LIGHT = "#fde2d2"
    C_SKIN_SHADOW = "#cf7c5a"
    C_HAIR_MID = "#b86414"
    C_HAIR_LIGHT = "#ea9423"
    
    # Fill skin
    for y in range(8, 14):
        for x in range(8, 24):
            c.set(x, y, C_SKIN_LIGHT)
            
    # Bangs
    for x in range(7, 25):
        c.set(x, 8, C_HAIR_LIGHT)
        
    # Row 9:
    # Left lock: 7..10
    # Center lock: 14..17
    # Right lock: 21..24
    for x in range(7, 11): c.set(x, 9, C_HAIR_LIGHT)
    for x in range(14, 18): c.set(x, 9, C_HAIR_LIGHT)
    for x in range(21, 25): c.set(x, 9, C_HAIR_LIGHT)
    
    # Row 10:
    for x in range(7, 10): c.set(x, 10, C_HAIR_LIGHT)
    c.set(15, 10, C_HAIR_LIGHT)
    c.set(16, 10, C_HAIR_LIGHT)
    for x in range(22, 25): c.set(x, 10, C_HAIR_LIGHT)
    
    # Row 11 tips:
    c.set(8, 11, C_HAIR_LIGHT)
    c.set(15, 11, C_HAIR_LIGHT)
    c.set(23, 11, C_HAIR_LIGHT)
    
    # Outlines:
    # Left lock:
    c.set(11, 8, C_OUTLINE)
    c.set(10, 9, C_OUTLINE)
    c.set(9, 10, C_OUTLINE)
    c.set(8, 12, C_OUTLINE)
    c.set(7, 11, C_OUTLINE)
    
    # Center lock:
    c.set(13, 8, C_OUTLINE)
    c.set(14, 9, C_OUTLINE)
    c.set(14, 10, C_OUTLINE)
    c.set(15, 12, C_OUTLINE)
    c.set(16, 12, C_OUTLINE)
    c.set(17, 10, C_OUTLINE)
    c.set(17, 9, C_OUTLINE)
    c.set(18, 8, C_OUTLINE)
    
    # Right lock:
    c.set(20, 8, C_OUTLINE)
    c.set(21, 9, C_OUTLINE)
    c.set(22, 10, C_OUTLINE)
    c.set(23, 12, C_OUTLINE)
    c.set(24, 11, C_OUTLINE)
    
    print(c.matrix_text(region=(10, 8, 21, 13)))
    view(c)
    finish(c)

test_bangs()
