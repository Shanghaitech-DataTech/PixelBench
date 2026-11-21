import math
W, H = 82, 135
output = input_canvas.copy(name="output")

SNOW_HI = output.color('#f4f8fc')  # bright snow
SNOW_LO = output.color('gt08')     # shaded snow (bluish)

FOLIAGE = {1, 2, 4}
SHADOW = 3

def src(x, y):
    if 0 <= x < W and 0 <= y < H:
        return input_canvas.get(x, y)
    return 0

def h1(x, y):
    return (x * 73856093 ^ y * 19349663) & 0xffff

# Pass 1: snow seeds = foliage pixels whose above neighbour is sky or dark shadow gap
seed = set()
for y in range(H):
    for x in range(W):
        i = src(x, y)
        if i in FOLIAGE:
            above = src(x, y - 1)
            if above == 0 or above == SHADOW:
                seed.add((x, y))

# Pass 2: connected snow blanket under seeds, wavy thickness
snow = set()
for (sx, sy) in seed:
    snow.add((sx, sy))
for y in range(H):
    for x in range(W):
        if src(x, y) not in FOLIAGE:
            continue
        if (x, y) in seed:
            continue
        # distance down to nearest seed in this column
        d = 1
        found = False
        while d <= 4:
            if (x, y - d) in seed:
                found = True
                break
            d += 1
        if not found:
            continue
        # wavy thickness 2..4 based on column
        th = 3 + int(round(math.sin(x * 0.35) * 1.0))  # 2..4
        # snow continuity: only lay deeper snow if the pixel above is snow
        if (x, y - 1) in snow and d <= th:
            if d == 1:
                snow.add((x, y))
            else:
                # stipple the deeper edge
                if h1(x, y) % 3 != 0 or d < th:
                    snow.add((x, y))

# paint: bright on top (seed + first row below), shaded deeper
for (x, y) in snow:
    if (x, y) in seed:
        output.set(x, y, SNOW_HI)
    elif (x, y - 1) in seed:
        output.set(x, y, SNOW_HI)
    else:
        output.set(x, y, SNOW_LO)

view(output, scale=5, margin=0)
save("snowy-pine", output)
finish(output)
