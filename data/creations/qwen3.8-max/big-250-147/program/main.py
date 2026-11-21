from pixelbench_api import *

W, H = 250, 147
output = input_canvas.copy(name="output")

# ---------- colour classification ----------
def classify(r, g, b):
    """Return 'sky', 'snow', 'mountain', 'tree'."""
    # sun-lit snow slope (sunset pink) -> snow
    if r >= 200 and 100 <= g <= 135 and 120 <= b <= 140:
        return "snow"
    # terrain darks
    if g <= 60 and r <= 130:
        if b >= 40 and g >= 30:
            return "mountain"
        return "tree"
    return "sky"

# ---------- noon sky gradient (banded + checker dither at band edges) ----------
EDGES = [15, 30, 45, 60, 75]
BANDS = [
    (56, 118, 198),
    (74, 138, 212),
    (98, 162, 224),
    (126, 184, 232),
    (154, 202, 238),
    (182, 218, 244),
]

def sky_col(y, x):
    bi = 0
    for i, B in enumerate(EDGES):
        if y >= B:
            bi = i + 1
    c = BANDS[bi]
    for i, B in enumerate(EDGES):
        if y == B - 1 or y == B:
            a, b = BANDS[i], BANDS[i + 1]
            c = a if (x + y) % 2 == 0 else b
    return c

# ---------- daylight remaps ----------
def mountain_col(r, g, b):
    L = r + g + b
    if L < 150:
        return (74, 96, 140)
    if L < 215:
        return (96, 120, 164)
    return (122, 146, 188)

def tree_col(r, g, b):
    L = r + g + b
    if L < 60:
        return (16, 44, 30)
    if L < 90:
        return (24, 58, 38)
    if L < 115:
        return (34, 74, 46)
    return (52, 98, 58)

def snow_col(r, g, b):
    if r + g + b < 450:
        return (214, 232, 244)
    return (246, 250, 252)

pal = {p["index"]: tuple(p["rgba"]) for p in input_canvas.palette()}
rgb = {}
for y in range(H):
    for x in range(W):
        rgb[(x, y)] = pal[output.get(x, y)][:3]

# terrain top per column (terrain never starts above y=55 in this scene)
sky_in_terrain = 0
for x in range(W):
    ttop = H
    for y in range(55, H):
        r, g, b = rgb[(x, y)]
        if classify(r, g, b) != "sky":
            ttop = y
            break
    for y in range(0, ttop):
        output.set(x, y, sky_col(y, x))
    for y in range(ttop, H):
        r, g, b = rgb[(x, y)]
        cls = classify(r, g, b)
        if cls == "sky":
            sky_in_terrain += 1
            output.set(x, y, sky_col(y, x))
        elif cls == "snow":
            output.set(x, y, snow_col(r, g, b))
        elif cls == "mountain":
            output.set(x, y, mountain_col(r, g, b))
        else:
            output.set(x, y, tree_col(r, g, b))

print("sky pixels found inside terrain region:", sky_in_terrain)
print(output.stats_text())
view(output, margin=0)
save("noon_clear_day", output)
finish(output)
