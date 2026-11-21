import os
from pixelbench_api import new_canvas, view, save, finish

def draw():
    c = new_canvas(16, 16)
    
    art = [
        ".OOOO...........",
        "OLLHXO..........",
        "OLHOOHXO........",
        "OLO..OHO........",
        "OLO..OHO........",
        "OLHOOSSOHXO.....",
        ".OXSSSOOOHXO....",
        "..OOOOOOOOHXO...",
        ".......OOOOHXO..",
        "......OLHHXXHXO.",
        "........OOOOOHXO",
        ".......OLHHXXXSO",
        "........OOOOOOO.",
        "................",
        "................",
        "................"
    ]
    
    palette = {
        '.': None,
        'O': '#26140c', # Dark outline
        'S': '#5c3a21', # Shadow
        'X': '#8a5a33', # Mid tone
        'H': '#b88655', # Highlight
        'L': '#e3b786', # Bright edge
    }
    
    for y, row in enumerate(art):
        for x, char in enumerate(row):
            if char in palette:
                c.set(x, y, palette[char])
                
    save("wooden_key", c)
    finish(c)

if __name__ == "__main__":
    draw()
