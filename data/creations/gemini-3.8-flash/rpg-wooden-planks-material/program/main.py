from pixelbench_api import *

def create_wooden_planks():
    # Palette: Warm, rich, classic 16-bit RPG wood palette
    P = {
        # Grooves / Seams
        'G0': '#150904',  # deep corner seam / groove intersection
        'G1': '#261208',  # main seam groove
        'G2': '#3a1b0c',  # seam shadow / crevice
        
        # Dark Board Ramp (Rich Chestnut / Walnut)
        'D0': '#46200e',  # dark board deepest grain
        'D1': '#5c2c14',  # dark board grain line
        'D2': '#73391a',  # dark board shadow / grain edge
        'D3': '#8a4621',  # dark board base body
        'D4': '#9f5128',  # dark board midtone / grain highlight
        'D5': '#b45f30',  # dark board left edge highlight
        'D6': '#c66f39',  # dark board top end bevel highlight
        
        # Light Board Ramp (Warm Amber Oak / Golden Pine)
        'L0': '#683216',  # light board deepest grain
        'L1': '#83421b',  # light board grain line
        'L2': '#9e5324',  # light board shadow / grain edge
        'L3': '#b7672d',  # light board base body
        'L4': '#ce7b37',  # light board midtone / grain highlight
        'L5': '#e38f42',  # light board left edge highlight
        'L6': '#f2a250',  # light board top end bevel highlight
        
        # Knots
        'K0': '#160803',  # knot core (darkest)
    }
    
    # 3 Planks layout:
    # Plank 0: cols 0..4 (wood cols 0..3, seam col 4)
    # Plank 1: cols 5..10 (wood cols 5..9, seam col 10)
    # Plank 2: cols 11..15 (wood cols 11..14, seam col 15)
    
    # Boards & alternating ends:
    # Plank 0:
    #   y=0..4:   Light 0A
    #   y=5:      Groove
    #   y=6..12:  Dark 0B (Knot 2 at (2, 9))
    #   y=13:     Groove
    #   y=14..15: Light 0A
    #
    # Plank 1:
    #   y=0:      Dark 1A
    #   y=1:      Groove
    #   y=2..8:   Light 1B (Knot 1 at (7, 5))
    #   y=9:      Groove
    #   y=10..15: Dark 1A
    #
    # Plank 2:
    #   y=0..6:   Light 2B (top bevel at 0)
    #   y=7:      Groove
    #   y=8..14:  Dark 2A (top bevel at 8, Knot 3 at (12, 11))
    #   y=15:     Groove
    
    grid = [
        # y=0:
        # P0: Light 0A (grain at col 2)
        # P1: Dark 1A (bottom of board, shadow before groove at y=1)
        # P2: Light 2B (top end bevel highlight)
        "L5 L4 L1 L2 G1   D5 D3 D2 D1 D2 G1   L6 L5 L4 L3 G1",
        
        # y=1:
        # P0: Light 0A (grain at col 2)
        # P1: Horizontal groove
        # P2: Light 2B (grain at col 13)
        "L5 L3 L1 L2 G1   G1 G1 G1 G0 G1 G1   L5 L3 L1 L2 G1",
        
        # y=2:
        # P0: Light 0A (grain at col 2)
        # P1: Light 1B (top end bevel highlight)
        # P2: Light 2B (grain at col 13)
        "L5 L3 L1 L2 G1   L6 L5 L4 L4 L3 G1   L5 L3 L1 L2 G1",
        
        # y=3:
        # P0: Light 0A (grain swaying to col 1)
        # P1: Light 1B (grain line at col 7)
        # P2: Light 2B (grain swaying to col 12)
        "L5 L1 L3 L2 G1   L5 L3 L1 L4 L2 G1   L5 L1 L4 L2 G1",
        
        # y=4:
        # P0: Light 0A (bottom of board, shadow before groove at y=5)
        # P1: Light 1B (grain leading into Knot 1: col 7 is L1)
        # P2: Light 2B (grain swaying to col 12)
        "L4 L1 L2 L1 G1   L5 L2 L1 L3 L2 G1   L5 L1 L3 L2 G1",
        
        # y=5:
        # P0: Horizontal groove
        # P1: Light 1B (Knot 1: core K0 at (7, 5), parted grain L1 at col 6 & 8)
        # P2: Light 2B (grain swaying to col 13)
        "G1 G1 G0 G1 G1   L5 L1 K0 L1 L2 G1   L5 L3 L1 L2 G1",
        
        # y=6:
        # P0: Dark 0B (top end bevel highlight)
        # P1: Light 1B (grain trailing from Knot 1: col 7 is L1)
        # P2: Light 2B (bottom of board, shadow before groove at y=7)
        "D6 D5 D4 D3 G1   L5 L2 L1 L3 L2 G1   L4 L2 L1 L1 G1",
        
        # y=7:
        # P0: Dark 0B (grain at col 2)
        # P1: Light 1B (grain line at col 7)
        # P2: Horizontal groove
        "D5 D3 D1 D2 G1   L5 L3 L1 L4 L2 G1   G1 G1 G1 G0 G1",
        
        # y=8:
        # P0: Dark 0B (grain leading into Knot 2: col 2 is D1)
        # P1: Light 1B (bottom of board, shadow before groove at y=9)
        # P2: Dark 2A (top end bevel highlight)
        "D5 D2 D1 D2 G1   L4 L2 D2 D1 D2 G1   D6 D5 D4 D3 G1",
        
        # y=9:
        # P0: Dark 0B (Knot 2: core K0 at (2, 9), parted grain D1 at col 1 & 3)
        # P1: Horizontal groove
        # P2: Dark 2A (grain at col 13)
        "D5 D1 K0 D1 G1   G1 G1 G0 G1 G1 G1   D5 D3 D1 D2 G1",
        
        # y=10:
        # P0: Dark 0B (grain trailing from Knot 2: col 2 is D1)
        # P1: Dark 1A (top end bevel highlight)
        # P2: Dark 2A (grain leading into Knot 3: col 12 is D1)
        "D5 D2 D1 D2 G1   D6 D5 D4 D4 D3 G1   D5 D1 D3 D2 G1",
        
        # y=11:
        # P0: Dark 0B (grain at col 2)
        # P1: Dark 1A (grain line at col 7)
        # P2: Dark 2A (Knot 3: core K0 at (12, 11), parted grain D1 at 13)
        "D5 D3 D1 D2 G1   D5 D3 D1 D4 D2 G1   D5 K0 D1 D2 G1",
        
        # y=12:
        # P0: Dark 0B (bottom of board, shadow before groove at y=13)
        # P1: Dark 1A (grain line at col 7)
        # P2: Dark 2A (grain trailing from Knot 3: col 12 is D1)
        "D4 D2 D1 D1 G1   D5 L2 D1 D3 D2 G1   D5 D1 D3 D2 G1",
        
        # y=13:
        # P0: Horizontal groove
        # P1: Dark 1A (grain swaying to col 8)
        # P2: Dark 2A (grain swaying to col 13)
        "G1 G1 G0 G1 G1   D5 D3 D3 D1 D2 G1   D5 D3 D1 D2 G1",
        
        # y=14:
        # P0: Light 0A (top end bevel highlight)
        # P1: Dark 1A (grain line at col 8)
        # P2: Dark 2A (bottom of board, shadow before groove at y=15)
        "L6 L5 L4 L3 G1   D5 D3 D4 D1 D2 G1   D4 D2 D1 D1 G1",
        
        # y=15:
        # P0: Light 0A (grain at col 2, seamlessly matches y=0)
        # P1: Dark 1A (grain at col 8, shadow edge, seamlessly matches y=0)
        # P2: Horizontal groove (seamlessly leads into bevel at y=0)
        "L5 L4 L1 L2 G1   D5 D3 D2 D1 D2 G1   G1 G1 G1 G0 G1",
    ]
    
    result = new_canvas(16, 16, name="wooden_planks")
    for y, row in enumerate(grid):
        tokens = row.split()
        for x, token in enumerate(tokens):
            result.set(x, y, P[token])
            
    return result

result = create_wooden_planks()
print(result.stats_text())
view(result)
finish(result)
