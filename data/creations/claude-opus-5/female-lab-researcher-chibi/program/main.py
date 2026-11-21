rows = [
    "....KKKKKKKK....",
    "...KKKhKKKKKK...",
    "...KKhKKKKKKK...",
    "...KKKKKKKKKK...",
    "...KKSSSSSSKK...",
    "...KKEWSSWEKK...",
    "...KKEESSEEKK...",
    "...KKbSRRSbKK...",
    "...KKsSSSSsKK...",
    "...KWWwssWWWK...",
    "...KWWwTTwWWK...",
    "...KWWwTTwWWK...",
    "...SWWwTTwWWS...",
    "....WwwwwwwW....",
    ".....PP..PP.....",
    ".....BB..BB.....",
]

legend = {
    "K": "#191320",  # black hair
    "h": "#3f3550",  # hair shine
    "S": "#f3c9a4",  # skin
    "s": "#d9a27e",  # skin shade
    "b": "#e8a68f",  # blush
    "E": "#5d3519",  # brown eye
    "W": "#f6f8fc",  # lab coat / eye glint
    "R": "#b3615b",  # mouth
    "w": "#ccd4e2",  # coat shade
    "T": "#3f8f93",  # shirt
    "P": "#3b4258",  # trousers
    "B": "#26262f",  # shoes
}

result = new_canvas(16, 16, name="researcher")

for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row))
    for x, ch in enumerate(row):
        if ch != ".":
            result.set(x, y, legend[ch])

view(result)
print(result.stats_text())
save("female-lab-researcher-chibi", result)
finish(result)
