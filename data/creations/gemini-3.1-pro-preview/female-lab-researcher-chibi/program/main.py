from pixelbench_api import new_canvas, finish

def draw():
    c = new_canvas(16, 16)
    
    palette = {
        '1': '#1a1a1a',
        '2': '#2b2b2b',
        '3': '#555555',
        'S': '#ffdfc4',
        'N': '#e5b39e',
        'E': '#6b4c3a',
        'B': '#ff99a8',
        'C': '#ffffff',
        'D': '#d3d3d3',
        'U': '#457b9d',
        'P': '#1d3557',
        'K': '#3a3a3a',
        'A': '#ffd166',
        '_': None
    }
    
    pixels = [
        "________________",
        "_____111111_____",
        "____12222221____",
        "___1233223321___",
        "___122SSSS221___",
        "___12SESSES21___",
        "___12BESSEB21___",
        "___122SSSS221___",
        "____121NN121____",
        "___1CDCUUCDC1___",
        "___1CDAUUCDC1___",
        "___1CDCPPCDC1___",
        "___1SC1PP1CS1___",
        "___1CC1SS1CC1___",
        "____111SS111____",
        "______1KK1______"
    ]

    for y, row in enumerate(pixels):
        for x, char in enumerate(row):
            if char in palette and palette[char] is not None:
                c.set(x, y, palette[char])
                
    finish(c)

draw()
