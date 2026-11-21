from pixelbench_api import *

SRC = input_canvas
W, H = 35, 22
DX = 4

# ---------- frame 1: original picture content, centered on 35x22 ----------
f1 = new_canvas(W, H)
f1.blit(SRC, DX, 0)

# ---------- frame 2: body kept, wings raised & spread ----------
body = SRC.copy()
body.clear(0, 0, 6, H)     # drop the left drooping wing (x0-5)
body.clear(21, 0, 6, H)    # drop the right drooping wing (x21-26)

f2 = new_canvas(W, H)
f2.blit(body, DX, 0)

def wing_color(ch):
    return {'d': '#432f53', 'c': '#b572b1', 'h': '#5c436f'}[ch]

left_rows = [
    "dd........",
    "dccd......",
    "dcchhd.....",
    "dcchd......",
    "dcchhd.....",
    "dchhd......",
    "dchhd......",
    "dchhhd.....",
    ".dchhhd....",
    "..dchhhd...",
    "...dchhd...",
    "....dchd...",
    ".....dhd...",
    "......dd...",
    ".......d..",
]

for y, row in enumerate(left_rows):
    for x, ch in enumerate(row):
        if ch == '.':
            continue
        col = wing_color(ch)
        f2.set(x, y, col)
        f2.set(W - 1 - x, y, col)   # mirrored right wing

print("f1:", f1.stats_text())
print()
print("f2:", f2.stats_text())
print()
print(f2.matrix_text())

finish([f1, f2])
