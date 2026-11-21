# 16x16 chibi female lab researcher (two heads tall)
# grid-driven sprite

PAL = {
    'O': '#151021',   # outline (near black)
    'H': '#272038',   # black hair
    'h': '#4b4169',   # hair highlight
    'S': '#f8d3a8',   # skin
    's': '#dca87b',   # skin shadow
    'R': '#e8907e',   # blush
    'W': '#ffffff',   # eye sparkle
    'E': '#8a5a2b',   # brown iris
    'D': '#402611',   # dark brown pupil
    'M': '#c0655a',   # mouth
    'C': '#f2f5fa',   # lab coat white
    'c': '#c6d1e2',   # lab coat shadow
    'B': '#4fa3c7',   # blouse / top
    'P': '#3b4a6b',   # skirt
    'K': '#2a2438',   # shoes
    'G': '#9fd8c0',   # glass / liquid accent
}

ROWS = [
    "....OOOOOOOO....",  # 0  hair crown
    "...OHhHHHHHHO...",  # 1
    "..OhhHHHHHHHHO..",  # 2
    "..OHHHHHHHHHHO..",  # 3  fringe
    "..OHSWESSWESHO..",  # 4  eyes top
    "..OHSEDSSEDSHO..",  # 5  eyes bottom
    "..OHRSSMMSSRHO..",  # 6  blush cheeks + mouth
    "..HHHOSSSSOHHH..",  # 7  chin
    "..HHOCcsscCOHH..",  # 8  neck / shoulders
    "..HOCCcPPcCCOH..",  # 9  coat + bow at collar
    "..HOCCcBBcCCOH..",  # 10
    "..HOcCcBBcCcOH..",  # 11 coat pockets
    "...OCCcBBcCCO...",  # 12 coat hem
    "..OPPPPPPPPPPO..",  # 13 skirt
    "....OSSOOSSO....",  # 14 legs
    "...OKKKOOKKKO...",  # 15 shoes
]

c = new_canvas(16, 16, name="output")

for y, row in enumerate(ROWS):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch == '.':
            continue
        c.set(x, y, PAL[ch])

print(c.stats_text())
p = view(c, scale=16, margin=1)
print(p)
save("lab_researcher", c)
finish(c)
