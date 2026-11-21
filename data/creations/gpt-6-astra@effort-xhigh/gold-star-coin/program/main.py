result = new_canvas(16, 16, name="gold-star-coin")
# Six opaque colors; the corners remain transparent.
inks = {
    'o': '#75441f',
    's': '#ba771c',
    'g': '#eda82e',
    'y': '#ffd65a',
    'h': '#fff3b0',
    '*': '#a96720',
}
# A rounded silhouette, a lit upper-left rim, and a thick lower bevel.
rows = [
    '................',
    '......oooo......',
    '....oohhhhoo....',
    '...ohhyyyyggo...',
    '..ohyyyyyyyygo..',
    '.ohyyyyyyyyygso.',
    '.ohyyyyyyyyygso.',
    '.ohyyyyyyyyygso.',
    '.oyyyyyyyyyygso.',
    '.ogyyyyyyyyygso.',
    '.ogyyyyyyyyygso.',
    '..ogyyyyyyygso..',
    '...ogggggggso...',
    '....osssssoo....',
    '......oooo......',
    '................',
]
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char != '.':
            result.set(x, y, inks[char])
# The five-point emblem uses a solid contrasting gold tone for legibility.
star = [
    '...##...',
    '...##...',
    '########',
    '.######.',
    '..####..',
    '.######.',
    '.##..##.',
]
for y, row in enumerate(star, 4):
    for x, char in enumerate(row, 4):
        if char == '#':
            result.set(x, y, inks['*'])
view(result, scale=24, margin=0)
save("gold-star-coin", result)
finish(result)
