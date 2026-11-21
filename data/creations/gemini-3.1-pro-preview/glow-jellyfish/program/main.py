from pixelbench_api import new_canvas, save, finish

def draw():
    c = new_canvas(16, 16)
    
    palette = {
        'O': '#1a1c2c',
        'S': '#3b5dc9',
        'B': '#41a6f6',
        'H': '#73eff7',
        'W': '#ffffff',
        '.': None
    }
    
    art = [
        "................",
        "......OOOO......",
        "....OOSHHSOO....",
        "...OSHHHHHHS....",
        "..OSHHBWWBHHS...",
        "..OSHHWBBWHHS...",
        ".OSHHBWBBWHHS..",
        ".OSHHBBWWBBHHS..",
        ".OSHHBBBBBBHHS..",
        "..OSBOBHHBOBS...",
        "..OHO.OBBO.OHO..",
        "...OHOBBO.OHO...",
        "..OHO.OBBO.OHO..",
        "...OHO.OBBOHO...",
        "...OOO.OOOOOO...",
        "................"
    ]
    
    for y, row in enumerate(art):
        for x, char in enumerate(row):
            color = palette.get(char)
            if color:
                c.set(x, y, color)
                
    return c

if __name__ == "__main__":
    c = draw()
    finish(c)
