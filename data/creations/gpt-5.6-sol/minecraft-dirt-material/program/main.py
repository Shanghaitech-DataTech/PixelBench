from pixelbench_api import new_canvas, view, finish

# Seven-colour, fully opaque dirt tile. Edge-adjacent motifs are balanced so
# repeated copies do not form a visible border.
result = new_canvas(16, 16, background="#79502f", name="minecraft-dirt-material")

palette = {
    "0": "#79502f",  # packed earth
    "1": "#3f281c",  # deep crevice
    "2": "#583924",  # dark soil
    "3": "#94623a",  # dry earth
    "4": "#b07a49",  # bright grit
    "5": "#493429",  # cool stone shadow
    "6": "#806044",  # muted mineral
}

texture = [
    "0220033002003310",
    "2200333000022102",
    "2000343000622002",
    "0033300006620030",
    "0033002200000330",
    "0200022211000300",
    "0200022111003002",
    "3300002200333003",
    "3433000000330003",
    "3333005500002200",
    "0000065500222200",
    "2200665000221002",
    "2200600000001002",
    "0000003343000030",
    "0033003443000330",
    "0233003330003310",
]

assert len(texture) == 16 and all(len(row) == 16 for row in texture)
for y, row in enumerate(texture):
    for x, key in enumerate(row):
        result.set(x, y, palette[key])

# Small contrasting grains keep the broad clumps granular at native size.
for x, y, key in [
    (5, 0, "4"), (9, 1, "3"), (0, 3, "3"), (7, 3, "2"),
    (12, 4, "4"), (4, 6, "3"), (14, 6, "2"), (8, 7, "3"),
    (5, 8, "2"), (15, 9, "4"), (9, 10, "3"), (3, 11, "3"),
    (13, 12, "2"), (7, 12, "2"), (1, 14, "2"), (11, 15, "3")
]:
    result.set(x, y, palette[key])
view(result, scale=28, margin=0)
finish(result)
