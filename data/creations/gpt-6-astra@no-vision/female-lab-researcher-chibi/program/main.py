result = new_canvas(16, 16, name="female_lab_researcher")
palette = {
    '.': None,
    'H': '#151723',   # black hair and silhouette
    'h': '#2b2b3d',   # hair sheen
    'j': '#424052',
    's': '#f0bd94',
    'l': '#ffdbb3',
    'k': '#d99383',
    'm': '#b76d69',
    'b': '#30252b',
    'e': '#84502e',   # brown irises
    'O': '#65788a',   # cool coat outline
    'w': '#fff8ed',
    'g': '#c4d6df',
    't': '#367e89',
    'T': '#224e61',
    'a': '#87e0d2',
    'f': '#d6f9ef',
    'B': '#374054',
}
rows = [
    '.....HHHHHH.....',
    '....HhhhhhhH....',
    '...HhjjHHhhhH...',
    '...HhlssssHHH...',
    '...HHbessebHH...',
    '...HHskllksHH...',
    '...HHssmsssHH...',
    '...HHHssssHHH...',
    '....HOwsswOH....',
    '...OwwgtgwwO....',
    '...OwwtTwwgOs...',
    '...OgwgwwggsOf..',
    '....sOwwgwwOaaO.',
    '.....OwwgwwOaaO.',
    '.....OgggggOOOO.',
    '.....HH..HH.....',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, symbol in enumerate(row):
        if symbol != '.':
            result.set(x, y, palette[symbol])
# Coat pocket, badge, and shoe glints remain single-pixel details.
result.set(9, 11, '#65788a')
result.set(9, 10, '#87e0d2')
result.set(6, 15, '#374054')
result.set(9, 15, '#374054')
print(result.stats_text())
print(result.matrix_text())
save('female_lab_researcher', result)
finish(result)
