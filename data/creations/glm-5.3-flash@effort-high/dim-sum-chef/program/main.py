# Dim sum chef - 32x32 front-facing sprite
# Legend:
#   H hat white, h hat shade, S skin, E eye, M mouth, R blush
#   C coat white, A apron cream, F flour speckle
#   B bamboo light, b bamboo dark rim, U bun, u bun shade
#   P pants, K shoes

COLORS = {
    "H": "#F7F7F2",  # hat / coat white
    "h": "#D9D9D2",  # hat band shade
    "S": "#E8B88A",  # skin
    "E": "#33241C",  # eyes
    "M": "#B5563F",  # mouth
    "R": "#E39B77",  # blush
    "C": "#F7F7F2",  # coat
    "A": "#EDE4CE",  # flour-dusted apron
    "F": "#FFFFFF",  # flour speckles
    "B": "#C89B5A",  # bamboo weave
    "b": "#8F6B35",  # bamboo rims
    "U": "#FBF3E0",  # bun highlight
    "u": "#E6D3AE",  # bun shade
    "P": "#4A4E69",  # pants
    "K": "#2B2B2B",  # shoes
}

ROWS = [
    "................................",  # 0
    "................................",  # 1
    "............HHHHHHHH............",  # 2  hat top puff
    "..........HHHHHHHHHHHH..........",  # 3
    "..........HHHHHHHHHHHh..........",  # 4
    "..........HHHHHHHHHHHH..........",  # 5
    "..........hhhhhhhhhhhh..........",  # 6  hat band
    "...........SSSSSSSSSS...........",  # 7  forehead
    "..........SSSESSSSSESS..........",  # 8  eyes
    "..........SRSESSSSSESR..........",  # 9  eyes + blush
    "..........SSSSMMMMSSSS..........",  # 10 smile
    "...........SSSSSSSSSS...........",  # 11 chin
    "...........CCCCCCCCCC...........",  # 12 collar
    ".........CCCCCCCCCCCCCC.........",  # 13 shoulders
    "........CCCCAAAAAAAACCCC........",  # 14 chest + apron top
    "........CCCCAFAAAFAACCCC........",  # 15 apron + flour
    ".......CCCCuUUuUUuUUuCCCC.......",  # 16 arms + bun tops peeking
    ".......CbbbbbbbbbbbbbbbbC.......",  # 17 steamer top rim
    "......SSbBUuUUuUUuUUuUbSS.......",  # 18 hands + steamer body
    "......SSbbbbbbbbbbbbbbbbSS......",  # 19 weave line
    "......SSbBBBBBBBBBBBBBBbSS......",  # 20 steamer body
    "......SSbbbbbbbbbbbbbbbbSS......",  # 21 bottom rim
    "........CCCAAAAAAAAAACCC........",  # 22 apron below steamer
    "........CCCAAFAAAAFAACCC........",  # 23 flour dust
    "........CCCAFFAAAFFAACCC........",  # 24 apron hem + flour
    "..........PPPPPPPPPPPP..........",  # 25 hips
    "..........PPPPP..PPPPP..........",  # 26 legs
    "..........PPPPP..PPPPP..........",  # 27 legs
    ".........KKKKKK..KKKKKK.........",  # 28 shoes
    ".........KKKKKK..KKKKKK.........",  # 29 shoes
    "................................",  # 30
    "................................",  # 31
]

for i, r in enumerate(ROWS):
    assert len(r) == 32, f"row {i} has length {len(r)}"

c = new_canvas(32, 32, name="dim-sum-chef")
for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, COLORS[ch])

# dark outline around the silhouette so every part reads clearly
c.outline("#3A2A20")

print(c.stats_text())
print(c.matrix_text())
save("dim_sum_chef", c)
finish(c)
