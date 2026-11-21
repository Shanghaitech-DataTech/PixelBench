from pixelbench_api import *

# Palette from the original image
COLORS = {
    'a': '#141b1b',  # dark outline
    'b': '#d14b34',  # flag red
    'c': '#e46d3a',  # flag orange highlight
    'd': '#8f3e56',  # pole magenta
    'e': '#543c52',  # pole purple
}

# Frame 2: fly end lowered to mid position, wave crest travels right
F2 = [
    "............",
    ".........aaa",
    "........abba",
    ".aaaaaaabbba",
    ".addabbcbbba",
    "abcbbbccbbba",
    ".aeeabccbbba",
    ".addabbbbbba",
    "abcbbaaaaaa.",
    ".aeea.......",
    ".adda.......",
    ".adda.......",
    ".adda.......",
    ".adda.......",
]

# Frame 3: fly end at its lowest point, flag nearly flat
F3 = [
    "............",
    "............",
    ".........aaa",
    ".aaaaaaaabba",
    ".addabccbbba",
    "abcbbbccbbba",
    ".aeeabbbbbba",
    ".addabbbbbba",
    "abcbbaaaabba",
    ".aeea....aa.",
    ".adda.......",
    ".adda.......",
    ".adda.......",
    ".adda.......",
]

def render(grid, name):
    cv = new_canvas(48, 56, name=name)
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch != '.':
                cv.rect(x * 4, y * 4, 4, 4, COLORS[ch])
    return cv

# Frame 1: exact copy of the original picture
f1 = input_canvas.copy(name='output')
f2 = render(F2, 'frame2')
f3 = render(F3, 'frame3')

view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
