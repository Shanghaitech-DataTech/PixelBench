result = new_canvas(16, 16, name="wooden_key")
palette = {
    'O': '#302327',
    'S': '#69402e',
    'M': '#a66a3b',
    'L': '#d69a54',
    'H': '#f1c77d',
}
# Carved ring handle, long shaft, and two square wards.
rows = [
'................',
'...OOOOO........',
'..OHHLLLO.......',
'.OHLSSSMLO......',
'.OLS...SMO......',
'.OLS...SMO......',
'.OMSSSSSMO......',
'..OMMSSLO.......',
'...OHLLO........',
'....OLMO........',
'....OLMOOOOO....',
'....OLMLLLLO....',
'....OLMSOSMO....',
'....OLMOOOMO....',
'.....OOO.OOO....',
'................',
]
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char != '.':
            result.set(x, y, palette[char])
view(result, scale=24)
finish(result)
