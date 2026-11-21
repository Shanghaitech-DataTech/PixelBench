c = new_canvas(16, 16, name="female-lab-researcher-chibi")

# Register the palette
pal = {
    'K': c.color('#1b1410', 'outline'),
    'H': c.color('#2e2626', 'hair'),
    'S': c.color('#f6c9a0', 'skin'),
    'E': c.color('#6b4226', 'eye_brown'),
    'e': c.color('#ffffff', 'eye_highlight'),
    'W': c.color('#f8f8f8', 'coat_white'),
    'B': c.color('#4a3f4f', 'dark'),
    'M': c.color('#b07050', 'mouth'),
    'L': c.color('#4a4040', 'hair_shine'),
}

grid = [
    ".....KKKKKK.....",
    "....KLLHHHHK....",
    "...KHLLHHHHHK...",
    "..KHHHHHHHHHHK..",
    "..KHHHHHHHHHHK..",
    "..KHSEeSSeESHK..",
    "..KHSSSMMSSSHK..",
    "...KSSSSSSSSK...",
    ".....KSSSSK.....",
    "....KWWBBWWK....",
    "...KWWWBBWWWK...",
    "...KWWWBBWWWK...",
    "...KWWWWWWWK...",
    "...KWWWWWWWK...",
    ".....KBBBBK.....",
    "....KBBBBBBK....",
]

for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, pal[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
