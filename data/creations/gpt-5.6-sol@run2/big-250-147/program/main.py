output = input_canvas.copy(name="output")

# Capture source pixels before changing the shared-palette copy.
pal = {p["index"]: tuple(p["rgba"]) for p in input_canvas.palette()}
src = [[input_canvas.get(x, y) for x in range(250)] for y in range(147)]

# The mountain skyline, sampled from the original composition.
ridge = [
    (0, 98), (8, 94), (18, 90), (29, 87), (42, 80), (55, 75),
    (61, 76), (70, 83), (79, 89), (92, 94), (101, 98),
    (108, 96), (112, 91), (116, 79), (121, 79), (132, 83), (142, 78),
    (153, 71), (163, 66), (170, 63), (177, 66), (185, 72),
    (197, 79), (204, 81), (210, 72), (215, 71), (223, 76),
    (232, 87), (241, 94), (249, 99)
]

def skyline(x):
    for i in range(len(ridge) - 1):
        x0, y0 = ridge[i]
        x1, y1 = ridge[i + 1]
        if x <= x1:
            return round(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
    return ridge[-1][1]

def reg(hexes, prefix):
    return [output.color(h, name=f"{prefix}{i}") for i, h in enumerate(hexes)]

sky = reg(["#2f88c8", "#368fce", "#4099d5", "#4da3db", "#5baee0",
           "#6bb9e4", "#7bc3e8", "#8bcae9", "#9bd2eb", "#acd9ed"], "noon_sky_")
mount = reg(["#31566f", "#39627c", "#436f89", "#4e7c95", "#5a89a1",
             "#6796ac", "#75a2b7", "#84afc1", "#94bbca", "#a5c7d3"], "mountain_")
far = reg(["#718fa1", "#7898a9", "#82a1b0", "#8cabb8", "#98b4c0",
          "#a5bec8", "#b2c8d0", "#bfd2d8"], "far_ridge_")
forest = reg(["#153126", "#1b3d2d", "#234a35", "#2d5840", "#38664a",
             "#457455", "#538261", "#62906d", "#729e7a"], "forest_")
bark = reg(["#342d24", "#42372a", "#514330", "#625039", "#735e43"], "bark_")

# Clear noon sky. A sparse ordered variation keeps the original pixel-art texture.
for x in range(250):
    top = skyline(x)
    for y in range(top):
        level = min(9, max(0, (y * 10) // 108))
        if ((x + 2 * y) % 7 == 0) and level < 9:
            level += 1
        output.set(x, y, sky[level])

# Re-light the land. Quantized ramps retain the source texture without sunset hues.
for x in range(250):
    top = skyline(x)
    for y in range(top, 147):
        r, g, b, a = pal[src[y][x]]
        lum = (3 * r + 4 * g + b) // 8
        if y < 113:
            # Pale distant pixels recede into atmospheric blue.
            if lum > 125 and (y < 101 or (75 < x < 125 and y < 105)):
                k = min(7, max(0, (lum - 105) // 16))
                output.set(x, y, far[k])
            else:
                k = min(9, max(0, (lum - 35) // 15))
                output.set(x, y, mount[k])
        else:
            # Warm source accents become trunks; the rest becomes sunlit evergreen.
            if r > g * 1.45 and r > 62 and lum > 35:
                k = min(4, max(0, (lum - 30) // 20))
                output.set(x, y, bark[k])
            else:
                k = min(8, max(0, (lum - 15) // 16))
                output.set(x, y, forest[k])

view(output, size=750, margin=0)
finish(output)
