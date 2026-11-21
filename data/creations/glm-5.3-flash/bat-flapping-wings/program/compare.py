from pixelbench_api import *

COL = {
    'a': '#1d181e', 'b': '#7784a2', 'c': '#b572b1', 'd': '#432f53',
    'e': '#5f5f7b', 'f': '#ae0000', 'g': '#fff9d6', 'h': '#5c436f',
}

W, H, DY = 27, 27, 5

# ---------- candidate B: hand-drawn raised wings (arm = upper edge) ----------
fB = new_canvas(W, H, None, name='candB')
fB.blit(input_canvas, 0, DY)
fB.clear(0, 0, 9, H)
fB.clear(18, 0, 9, H)

LEFT = [
    "..aa......",
    ".ahd......",
    "ahhhd.....",
    "ahhcd.....",
    "ahhecd....",
    "ahhhcd....",
    "ahhhecd...",
    ".ahhhecd..",
    ".ahhhecd..",
    "..ahhhecd.",
    "..ahhhecd.",
    "...ahhhec.",
    "....ahhhc.",
    ".....ahhh.",
    "......ahh.",
    ".......ah.",
    "........a.",
]


def stamp(cv, rows, mirror):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == '.':
                continue
            cv.set((W - 1 - x) if mirror else x, y, COL[ch])


stamp(fB, LEFT, False)
stamp(fB, LEFT, True)
print("=== candidate B (drawn) ===")
print(fB.matrix_text())

# ---------- candidate A: wings mirrored vertically about the shoulder ----------
fA = new_canvas(W, H, None, name='candA')
fA.blit(input_canvas, 0, DY)
fA.clear(0, 0, 9, H)
fA.clear(18, 0, 9, H)
for y in range(6, 22):
    yc = 21 - y
    for x in range(0, 9):
        i = input_canvas.get(x, y)
        if i:
            fA.set(x, yc, i)
        i = input_canvas.get(26 - x, y)
        if i:
            fA.set(26 - x, yc, i)
print("=== candidate A (mirrored) ===")
print(fA.matrix_text())
