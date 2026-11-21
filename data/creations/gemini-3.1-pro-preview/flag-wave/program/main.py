import pixelbench_api
from pixelbench_api import input_canvas, new_canvas, finish

def draw_blocks(c, blocks_str):
    colors = {
        '.': None,
        'a': '#141b1bff',
        'b': '#d14b34ff',
        'c': '#e46d3aff',
        'd': '#8f3e56ff',
        'e': '#543c52ff'
    }
    for y, row in enumerate(blocks_str):
        for x, char in enumerate(row):
            color = colors[char]
            if color:
                c.rect(x * 4, y * 4, 4, 4, color)

frame1 = input_canvas

frame2 = new_canvas(48, 56)
frame2_blocks = [
    "............",
    "............",
    ".......aaaa.",
    ".aaaaaacbbba",
    ".addabccbbba",
    "abcbbbccbbba",
    ".aeeabbbbbba",
    ".addabbbbbba",
    "abcbbaabbbba",
    ".aeea..aaaa.",
    ".adda.......",
    ".adda.......",
    ".adda.......",
    ".adda......."
]
draw_blocks(frame2, frame2_blocks)

frame3 = new_canvas(48, 56)
frame3_blocks = [
    "............",
    "............",
    "............",
    ".aaaaaaaa...",
    ".addabbbba..",
    "abcbbbbbbbaa",
    ".aeeabccbbba",
    ".addabccbbba",
    "abcbbaacbbba",
    ".aeea..abbba",
    ".adda...abba",
    ".adda....aaa",
    ".adda.......",
    ".adda......."
]
draw_blocks(frame3, frame3_blocks)

finish([frame1, frame2, frame3])
