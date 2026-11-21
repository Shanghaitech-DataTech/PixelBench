from pixelbench_api import *

SNOW_LIGHT = '#e6ebf2'   # gt09
SNOW_SHADE = '#c3d2e5'   # gt08

w, h, rgba = input_canvas.to_rgba()

PAL = [(0, 0, 0, 0), (49, 114, 102, 255), (61, 153, 122, 255), (33, 49, 56, 255),
       (45, 86, 86, 255), (61, 33, 48, 255), (104, 48, 57, 255), (142, 72, 57, 255)]

def pindex(x, y):
    i = (y * w + x) * 4
    p = tuple(rgba[i:i + 4])
    return PAL.index(p) if p in PAL else -2

idx = [[pindex(x, y) for x in range(w)] for y in range(h)]
opaque = [[idx[y][x] > 0 for x in range(w)] for y in range(h)]

BRIGHT = {1, 2}          # light greens: lit branch surfaces
DARKISH = {3, 4}         # shadow / mid teal

# upward-facing surfaces: sky-exposed pixels, plus lit greens resting on shadow
surface = [[False] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if not opaque[y][x]:
            continue
        if y == 0 or not opaque[y - 1][x]:
            surface[y][x] = True
        elif idx[y][x] in BRIGHT and idx[y - 1][x] in DARKISH:
            surface[y][x] = True

output = input_canvas.copy(name='output')

# snow caps: two light rows on every upward-facing surface, shaded row beneath
for y in range(h):
    for x in range(w):
        if not surface[y][x]:
            continue
        output.set(x, y, SNOW_LIGHT)
        if y + 1 < h and opaque[y + 1][x]:
            output.set(x, y + 1, SNOW_LIGHT)
        if y + 2 < h and opaque[y + 2][x] and not surface[y + 2][x]:
            output.set(x, y + 2, SNOW_SHADE)

# piled drift: add a snow pixel above where a sky-exposed surface runs on
for y in range(h):
    for x in range(w):
        if (y == 0 or not opaque[y - 1][x]) and opaque[y][x] and y - 1 >= 0:
            left = x - 1 >= 0 and any((yy == 0 or not opaque[yy - 1][x - 1]) and opaque[yy][x - 1]
                                      for yy in (y - 1, y, y + 1) if 0 <= yy < h)
            right = x + 1 < w and any((yy == 0 or not opaque[yy - 1][x + 1]) and opaque[yy][x + 1]
                                      for yy in (y - 1, y, y + 1) if 0 <= yy < h)
            if left and right:
                output.set(x, y - 1, SNOW_LIGHT)

print(output.stats_text())
view(output)
save('snowy-pine', output)
finish(output)
