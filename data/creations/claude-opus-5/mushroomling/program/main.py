SPRITE = [
    ".....KKKKKK.....",
    "...KKRRRRRRKK...",
    "..KRRRRRRRRRRK..",
    ".KRRWWRRRRWWRRK.",
    "KRRRWWRRRRWWRRRK",
    "KDDDDDDDDDDDDDDK",
    ".KKKKKKKKKKKKKK.",
    "...KWWWWWWWWK...",
    ".KKKWKKWWKKWKKK.",
    "KWWKWKKWWKKWKWWK",
    "KWWKWWWWWWWWKWWK",
    ".KKKWWWWWWWWKKK.",
    "...KWWWWWWWWK...",
    "...KWWKKKKWWK...",
    "...KKKK..KKKK...",
    "................",
]

COLORS = {
    "K": "#2a1a2e",  # dark outline
    "R": "#d94436",  # red cap
    "W": "#f7ece1",  # cream body / cap spots
    "D": "#a32b26",  # cap underside shade
}

result = new_canvas(16, 16, name="mushroomling")
for name, spec in COLORS.items():
    result.color(spec, name=name)

for y, row in enumerate(SPRITE):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            result.set(x, y, ch)

print(result.stats_text())
view(result)
finish(result)
