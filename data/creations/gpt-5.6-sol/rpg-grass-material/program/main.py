# 16x16 seamless RPG grass material tile.
result = new_canvas(16, 16, name="rpg-grass-material")

palette = {
    "g": "#4f8b3b",  # main grass
    "m": "#579844",  # mid-light grass
    "l": "#69aa4b",  # sunlit blades
    "d": "#387235",  # shaded grass
    "x": "#285d31",  # deep tuft shadow
    "s": "#84603a",  # bare soil
    "t": "#a87843",  # lit soil
    "y": "#f2cf43",  # flower petals
    "c": "#fff08a",  # flower highlight
}

# Every row is fully opaque. Clusters crossing opposite edges avoid a framed look.
rows = [
    "gmgldggmgglggdmg",
    "lgggmgdggmgggglg",
    "ggdxgglggmgmtsgg",
    "mggddgglgglsttgm",
    "gglggymggdggtggg",
    "dggmyclggmgggglg",
    "gglgmymggggxdggg",
    "gmggdgggglxxgggm",
    "ggdgmlggmgxdglgg",
    "lgggggmgdggggggl",
    "ggmggdgggglgmggg",
    "ggglggggmggdgdgg",
    "gstggxgglggmgygm",
    "sttgxxdgglggycgg",
    "gtggxdgmggdgmygm",
    "gglggggdggmggggg",
]

for y, row in enumerate(rows):
    for x, key in enumerate(row):
        result.set(x, y, palette[key])

# A few crisp blade tips make the darker tufts read as grass, not stones.
for x, y in [(3, 1), (4, 1), (11, 6), (12, 6), (5, 11), (6, 12), (4, 14)]:
    result.set(x, y, palette["d"])

# Tiny stem pixels anchor each three-pixel flower in the turf.
for x, y in [(5, 7), (13, 15)]:
    result.set(x, y, palette["d"])

view(result, scale=24, margin=1, edges="all")
finish(result)
