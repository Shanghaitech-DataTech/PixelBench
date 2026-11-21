from pixelbench_api import *

def draw_weapons():
    c = new_canvas(64, 64, name="weapons")
    
    # Colors
    OUTLINE = '#1a1a1a'
    BLADE_LIGHT = '#e8ecef'
    BLADE_MID = '#9ba4b5'
    BLADE_DARK = '#5c677d'
    GOLD_LIGHT = '#fcd53f'
    GOLD_MID = '#d4af37'
    GOLD_DARK = '#997a00'
    WOOD_LIGHT = '#a67c52'
    WOOD_MID = '#704214'
    WOOD_DARK = '#4a2500'
    SHIELD_BLUE = '#2b5c8f'
    SHIELD_BLUE_DARK = '#1a3a5c'
    STRING = '#e0e0e0'
    
    # 1. Sword (Top-Left)
    # Handle
    c.line(7, 25, 11, 21, WOOD_MID)
    c.line(6, 25, 10, 21, WOOD_LIGHT)
    c.line(7, 26, 11, 22, WOOD_DARK)
    # Pommel
    c.circle(6, 26, 1, GOLD_MID)
    c.set(6, 26, GOLD_LIGHT)
    # Blade
    c.poly([(11,19), (23,7), (26,6), (25,9), (13,21)], BLADE_MID)
    c.poly([(11,19), (23,7), (26,6), (12,20)], BLADE_LIGHT)
    c.poly([(13,21), (25,9), (26,6), (12,20)], BLADE_DARK)
    c.line(12, 20, 25, 7, BLADE_MID)
    # Crossguard
    c.poly([(8,16), (9,16), (16,23), (16,24), (15,24), (8,17)], GOLD_MID)
    c.line(8, 16, 15, 23, GOLD_LIGHT)
    
    # 2. Bow (Top-Right)
    # Bow string
    c.line(42, 4, 42, 28, STRING)
    # Bow body
    c.path("M 42 4 Q 52 10 52 16 Q 52 22 42 28 Q 50 22 50 16 Q 50 10 42 4 Z", WOOD_MID)
    c.path("M 42 4 Q 52 10 52 16 Q 52 22 42 28", WOOD_LIGHT, fill=False)
    # Grip
    c.rect(50, 14, 3, 5, WOOD_DARK)
    # Arrow shaft
    c.line(42, 16, 58, 16, WOOD_LIGHT)
    # Arrow fletching
    c.line(44, 16, 42, 14, '#ffffff')
    c.line(44, 16, 42, 18, '#ffffff')
    c.line(46, 16, 44, 14, '#ffffff')
    c.line(46, 16, 44, 18, '#ffffff')
    # Arrowhead
    c.poly([(58,16), (54,13), (54,19)], BLADE_DARK)
    c.poly([(58,16), (55,14), (55,18)], BLADE_MID)
    c.poly([(58,16), (56,15), (56,17)], BLADE_LIGHT)
    
    # 3. Shield (Bottom-Left)
    # Base shield
    c.poly([(6,36), (26,36), (26,46), (23,52), (16,59), (9,52), (6,46)], BLADE_DARK)
    # Inner blue
    c.poly([(7,37), (25,37), (25,46), (22,51), (16,58), (10,51), (7,46)], SHIELD_BLUE)
    # Right side shadow
    c.poly([(16,37), (25,37), (25,46), (22,51), (16,58)], SHIELD_BLUE_DARK)
    # Top highlight
    c.line(7, 37, 25, 37, BLADE_LIGHT)
    c.line(7, 38, 7, 46, BLADE_LIGHT)
    # Cross
    c.rect(15, 41, 3, 11, GOLD_MID)
    c.rect(11, 45, 11, 3, GOLD_MID)
    c.rect(15, 41, 1, 11, GOLD_LIGHT)
    c.rect(11, 45, 11, 1, GOLD_LIGHT)
    
    # 4. Battle Axe (Bottom-Right)
    # Blades
    c.path("M 48 44 L 44 32 Q 32 32 32 44 L 44 48 Z", BLADE_MID)
    c.path("M 44 32 Q 32 32 32 44", BLADE_LIGHT, fill=False)
    c.path("M 48 44 L 60 48 Q 60 60 48 60 L 44 48 Z", BLADE_DARK)
    c.path("M 60 48 Q 60 60 48 60", BLADE_MID, fill=False)
    # Handle
    c.line(36, 56, 56, 36, WOOD_MID)
    c.line(35, 56, 55, 36, WOOD_LIGHT)
    c.line(36, 57, 56, 37, WOOD_DARK)
    # Spike
    c.line(56, 36, 60, 32, BLADE_MID)
    c.line(55, 36, 59, 32, BLADE_LIGHT)
    # Pommel
    c.circle(35, 57, 1, GOLD_MID)
    c.set(35, 57, GOLD_LIGHT)
    # Center attachment
    c.circle(46, 46, 2, BLADE_DARK)
    c.circle(46, 46, 1, GOLD_MID)
    
    # Outline everything
    c.outline(OUTLINE)
    
    return c

result = draw_weapons()
finish(result)
