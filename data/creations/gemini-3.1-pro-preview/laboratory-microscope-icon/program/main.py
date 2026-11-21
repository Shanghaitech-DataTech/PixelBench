from pixelbench_api import new_canvas, view, save, finish

def draw_microscope():
    palette = {
        '.': None,
        'O': '#1a1c23', # Outline
        'W': '#ffffff', # Highlight
        'L': '#e4e7eb', # Light body
        'M': '#a1aab5', # Mid body
        'D': '#5e6773', # Dark body
        'V': '#383e47', # Very dark
        'C': '#4fc4ff', # Cyan
        'B': '#0078c2', # Blue
        'S': '#a8d5e2', # Slide
        'I': '#e2f3f7', # Light/Highlight
    }

    art = [
        "................................",
        "................................",
        ".............OOO................",
        "...........OOWWMOO..............",
        "..........OWWLLMDDO.............",
        "..........OLLLLMDDO.............",
        "...........OOOOOOO..............",
        "...........OWWLLMO..............",
        "...........OLLLMMO.......OOOO...",
        "...........OLLLMMO.....OOWWMDO..",
        "...........OLLLMMO...OOWWLLMDDO.",
        "...........OLLLMMO...OOWWLLMMDDO",
        "..........OOOOOOOOO..OOWWLLMMDDO",
        ".........OVVVVVVVVVO.OOWWLLMMDDO",
        "........OVVVVVVVVVVVOOWWLLMMDDO",
        "......OVDDO.OVDDO....OOWWLLMMDDO",
        "......OCCCO.OCCCO....OOWWLLMDDO.",
        "......OBBBO.OBBBO....OOWWLLDDO..",
        "......OOOOO.OOOOO....OOWWMMDDO..",
        "....OOVVVVVVWWSSSVDDO.OOWMMDDO..",
        "...OVVVVVVVVSSSSSIVDDO.OOMMDDO..",
        "..OVVVVVVVVVVSSSIVVDDO.OOMMDDO..",
        "..ODDDDDDDDDDDDDDDDDDO.OOMMDDO..",
        "..OOOOOOOOOOOOOOOOOOOO.OOMMDDO..",
        "............OVDDO......OOMMDDO..",
        "...........OVVVDDO....OOWWMMDDO.",
        "........OOOOOOOOOOOOOOWWLLMMDDO",
        "......OOWWLLLLLLLLLLLLLWWLLMMDDO",
        "....OWWLLLLLOOOOOLLLLLLWWLLMMDDO",
        "...OWWLLLLLOIICIIOLLLLLWWLLMMDDO",
        "..OODDDDDDDOICCCIODDDDDDDDDDDO..",
        "..OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    ]
    
    canvas = new_canvas(32, 32)
    for y, row in enumerate(art):
        for x, char in enumerate(row):
            if char in palette and palette[char] is not None:
                canvas.set(x, y, palette[char])
                
    return canvas

if __name__ == "__main__":
    c = draw_microscope()
    finish(c)
