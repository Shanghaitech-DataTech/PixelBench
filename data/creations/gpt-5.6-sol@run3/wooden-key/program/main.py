from pixelbench_api import new_canvas, view, finish

# Five-tone carved wood palette; transparency is not a visible colour.
result = new_canvas(16, 16, background=None, name="wooden_key")
colors = {
    "D": "#2d170f",  # deep outline
    "S": "#59301b",  # shadow
    "M": "#8b4d25",  # wood
    "L": "#c47732",  # lit grain
    "H": "#e1a04c",  # fresh carved edge
}

sprite = [
    "................",
    "................",
    "...DDD..........",
    "..DSMLDD........",
    ".DSLLMSD........",
    ".DLMMLDDDDDDDDD.",
    "DSMDDMLLLLMMHMD.",
    "DMMD.DMMMMMMMMDD",
    "DMLD.DDDDDDDDDD.",
    "DSMMDD....DM.DD.",
    ".DLMMD....DM.DM.",
    "..DSD.....DD.DD.",
    "...DD...........",
    "................",
    "................",
    "................",
]

for y, row in enumerate(sprite):
    for x, mark in enumerate(row):
        if mark != ".":
            result.set(x, y, colors[mark])

view(result, scale=24, margin=1, edges="all")
finish(result)
