from pixelbench_api import *

c = new_canvas(16, 16, name="wooden_key")

# Palette (6 visible colours: outline, highlight, light/mid/dark wood, grain)
colors = {
    "O": "#33200f",  # dark outline
    "D": "#6e4a20",  # dark wood (shadow)
    "M": "#a5722f",  # mid wood
    "L": "#d3a058",  # light wood
    "H": "#e9bd76",  # bright highlight
    "G": "#8a5c26",  # grain fleck
}

rows = [
    ".....OOOOO......",   # bow top
    "....OHLLLDO.....",   # bow, light top
    "....OH...DO.....",   # hole with highlight glint
    "....OL...DO.....",   # hole
    "....OL...DO.....",   # hole
    "....OLLMMDO.....",   # bow bottom, shadow right
    "....OMMMMDO.....",   # bow bottom
    "....OGLMDO......",   # taper to shaft, grain
    ".....OLMDO......",   # shaft
    ".....OLMDO......",   # shaft
    ".....OLMDO......",   # shaft
    ".....OLMDO......",   # shaft
    ".....OLMDO......",   # shaft
    ".....OMM.DDDO...",   # teeth
    ".....ODM.DDDO...",   # teeth tips
    "................",
]

for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, colors[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
