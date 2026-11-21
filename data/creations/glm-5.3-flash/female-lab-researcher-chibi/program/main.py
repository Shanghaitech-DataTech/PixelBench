"""16x16 RPG chibi: female lab researcher, white lab coat, black hair, brown eyes.

Proportions: two heads tall -> head occupies rows 0-7, body rows 8-15.
"""

SIZE = 16

# char -> rgba
PALETTE = {
    "H": "#26232b",  # hair, near-black
    "h": "#47424f",  # hair shine
    "S": "#f8d5b5",  # skin
    "s": "#dda87e",  # skin shadow (neck)
    "E": "#8a4f28",  # brown iris
    "W": "#ffffff",  # eye highlight
    "B": "#f2a9a2",  # blush
    "M": "#b8625a",  # mouth
    "C": "#f4f4f6",  # lab coat white
    "c": "#c2c6d1",  # coat shadow (sleeves / hem / pocket)
    "T": "#4f9e97",  # shirt under the coat
    "P": "#c14b4b",  # pen in the breast pocket
    "K": "#7a5238",  # shoes
}

# 16 rows of 16 chars; "." = transparent
ROWS = [
    "....HHHHHHHH....",  # 0  crown
    "...HHHhhhhHHH...",  # 1  shine arc
    "..HHHhhhhhhHHH..",  # 2  shine band
    "..HHHHHHHHHHHH..",  # 3  bangs
    "..HHSSSSSSSSHH..",  # 4  forehead
    "..HHHWESSWEHHH..",  # 5  lashes + eyes (highlight top-left)
    "..HHBEESSEEBHH..",  # 6  eyes (bottom) + blush
    "...HSSSMMSSSH...",  # 7  chin + mouth
    "...HcCCssCCcH...",  # 8  collar + neck
    "...HcCCTTCCcH...",  # 9  open coat, shirt V
    "...HcPCTTCCcH...",  # 10 red pen on the left panel
    "...HcccTTCCcH...",  # 11 breast pocket line
    "...HcCCTTCCcH...",  # 12 coat hem
    ".....SS..SS.....",  # 13 legs
    ".....SS..SS.....",  # 14 legs
    "....KKK..KKK....",  # 15 shoes
]


def build():
    c = new_canvas(SIZE, SIZE, background=None, name="lab-researcher-chibi")
    idx = {ch: c.color(hexv, name=ch) for ch, hexv in PALETTE.items()}
    for y, row in enumerate(ROWS):
        if len(row) != SIZE:
            raise ValueError("row %d has length %d" % (y, len(row)))
        for x, ch in enumerate(row):
            if ch != ".":
                c.set(x, y, idx[ch])
    return c


c = build()
print(c.stats_text())
print(c.matrix_text())

finish(c)
