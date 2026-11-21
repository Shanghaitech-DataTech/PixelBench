# Native 16-pixel RPG sprite, with a large chibi head and white lab coat.
result = new_canvas(16, 16, name="female_lab_researcher")
P = {
    'O': '#242332',
    'H': '#141722',
    'h': '#303344',
    'l': '#4b4b60',
    'S': '#f3c5a1',
    's': '#c88473',
    'L': '#ffe2bc',
    'B': '#603b2b',
    'b': '#b57942',
    'r': '#e9a08f',
    'W': '#fffdf3',
    'w': '#dbe7ec',
    'c': '#94a9bd',
    'T': '#3b8f99',
    't': '#24606f',
    'G': '#45536d',
    'g': '#75819a',
    'A': '#baf9eb',
    'a': '#49babf',
}
rows = [
    '................',
    '.....OOOOOO.....',
    '....OhhhhHHO....',
    '...OhlhhHHHHO...',
    '...OHHHLSSSHO...',
    '...HSWBLSWBSH...',
    '...HrBbSSBbrH...',
    '...OHSSSsSSHO...',
    '...OHOWsSWOHO...',
    '....OWWTWWO..O..',
    '...OwWWtWWwO.A..',
    '...OsWWtWcWsOAO.',
    '....OWWcWWWOAaaO',
    '....OwWWOWWO.OO.',
    '.....OgO.OGO....',
    '.....OOO.OOO....',
]
# Symmetrical eye pairs: ivory catchlight above a warm brown iris.
rows[6] = '...HrBbSSBbrH...'
for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row), row)
    for x, mark in enumerate(row):
        if mark != '.':
            result.set(x, y, P[mark])
view(result, scale=28, margin=1, edges="all")
save("female-lab-researcher-chibi", result)
finish(result)
