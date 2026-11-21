import pixelbench_api as pba

PALETTE = {
    '.': None, # transparent

    # Outlines (Stardew warm earthy dark espresso)
    'O': '#261309', # Deepest outline (feet bottoms, dark accents)
    'o': '#462312', # Main warm brown outline
    'd': '#6c3a1c', # Secondary soft outline / feather crease
    'p': '#925633', # Soft internal seam

    # Body Ivory / Cream Plumage (warm, cozy, soft)
    'H': '#ffffff', # Specular feather highlight / eye shine
    'h': '#fffdf5', # Warm ivory highlight
    'W': '#faf2de', # Light cream
    'w': '#f3e8cb', # Base warm cream
    '1': '#ebd7b5', # Soft cream shadow
    '2': '#dcbfa8', # Warm sand shadow
    '3': '#c5a06e', # Deeper body shadow
    '4': '#a78253', # Underbelly shadow
    '5': '#886338', # Deepest ambient shadow under belly

    # Wing Plumage (layered soft tones)
    'U': '#fffef8', # Wing specular highlight
    'u': '#f7eed5', # Wing light tone
    'v': '#ebd4ac', # Wing midtone
    'x': '#d7bd8e', # Wing warm shadow
    'z': '#b99767', # Wing feather crease

    # Comb & Wattle (rich farm crimson)
    'k': '#360707', # Comb outline
    'K': '#6a0e0e', # Comb deep shadow
    'r': '#b51e1e', # Comb rich crimson
    'R': '#e03a3a', # Comb bright red
    'q': '#f25e5e', # Comb soft highlight

    # Beak & Feet (warm golden amber)
    'J': '#3e1a02', # Beak/leg outline
    'j': '#944803', # Beak/leg shadow
    'g': '#c97008', # Beak/leg mid amber
    'y': '#f09a12', # Golden yellow
    'Y': '#fed04a', # Bright beak highlight

    # Face details
    'E': '#140c06', # Eye dark pupil
    'e': '#ffffff', # Eye specular highlight
    'B': '#f7aba0', # Cheerful cheek blush
    'b': '#e8877b', # Blush shade
}

# 32x32 Grid
SPRITE = [
    # 01234567890123456789012345678901
    "................................", # 0
    "................................", # 1
    "................................", # 2
    "...................kk...........", # 3
    "..................kqRk...kk.....", # 4
    "......oo........k.krRRkkqRk.....", # 5
    ".....oHHo......kqRkrRRrkRRk.....", # 6
    "....oHHHHo....krRRkrRRrkrRk.....", # 7
    "...oHHhHHHooookKKKKKKKKKKkko....", # 8
    "...oHhWWWHHHHooHHHHHHHhhhhddo...", # 9
    "..oHhwwwwWWHHHHHHHHHHHHHHHeEo...", # 10
    "..ohww11111WWWHHHHHHHHHHHHEEoJJ.", # 11
    ".oWww1111111WWWHHHHHHHHHHBBoYYYJ", # 12
    ".oww111uuuuu111WHHHHhHHHHbboJJyJ", # 13
    ".oww11uUUUUuu111WHHHHHHHHkkRko..", # 14
    "..o11uUUUUUUuu111WHHHHHHWkRRko..", # 15
    "..o11uuuuuuuuuu111WWWWWWkKKkWo..", # 16
    "...o1vvvvvvvvvv111WWWWWkkkWWWo..", # 17
    "...o11vvvvvvvvv111WWWWWWWWWWWo..", # 18
    "....o11xxxxxxxx111WWWWWWWWWWo...", # 19
    ".....o11xxxxxx2222WWWWWWWWWwo...", # 20
    "......o222222222222WWWWWWWWo....", # 21
    ".......o3333333333333WWWWWwo....", # 22
    "........o444444444444444WWwo....", # 23
    ".........o5555555555555544o.....", # 24
    "..........oo555555555555oo......", # 25
    "...........oJJJooooJJJoo........", # 26
    "............JyyJ...JyyJ.........", # 27
    "...........JyyyyJJyyyyJ.........", # 28
    "..........JyyJyyJJyyJyyJ........", # 29
    "...........JJ.JJ..JJ.JJ.........", # 30
    "................................", # 31
]

def main():
    assert len(SPRITE) == 32
    for r in SPRITE:
        assert len(r) == 32

    c = pba.new_canvas(32, 32, name="chicken")
    for y, row in enumerate(SPRITE):
        for x, ch in enumerate(row):
            col = PALETTE.get(ch)
            if col:
                c.set(x, y, col)
    
    pba.finish(c)

if __name__ == "__main__":
    main()
