# Wooden key inventory sprite, 16x16 and five visible colours.
result = new_canvas(16, 16, background=None, name="wooden-key")

palette = {
    "D": "#352016",  # deep carved outline
    "S": "#684027",  # dark wood grain
    "M": "#9d6032",  # warm heartwood
    "L": "#ca8742",  # lit wood
    "H": "#edbd67",  # worn golden edge
}

sprite = [
    "................",
    "................",
    "..DDDD..........",
    ".DMMMMD.........",
    "DMLHHMMD........",
    "DMH..LMDDDDDDD..",
    "DMH..HMMMMMMMMD.",
    "DMLHHMLLLLLLLMMD",
    ".DMMMMDDDDDDMMMD",
    "..DDDD.....DMSDD",
    "...........DMSD.",
    "...........DDDD.",
    "................",
    "................",
    "................",
    "................",
]

assert all(len(row) == 16 for row in sprite)
for y, row in enumerate(sprite):
    for x, mark in enumerate(row):
        if mark != ".":
            result.set(x, y, palette[mark])

# A few deliberate grain pixels keep the shaft recognisably wooden.
result.set(8, 6, palette["S"])
result.set(10, 7, palette["M"])
result.set(3, 8, palette["S"])

view(result, scale=24, margin=1, edges="all")
finish(result)
