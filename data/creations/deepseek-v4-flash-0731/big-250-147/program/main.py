from pixelbench_api import *

src = input_canvas
w, h = 250, 147

out = src.copy(name='output')
pal = out.palette()

def get_rgba(idx):
    return tuple(pal[idx]['rgba'])

def lum(rgba):
    r, g, b, a = rgba
    return 0.299*r + 0.587*g + 0.114*b

# Clear noon sky gradient (top -> horizon)
sky_top = out.color((88, 152, 224), name='noon_top')
sky_hi  = out.color((120, 178, 234), name='noon_hi')
sky_mid = out.color((150, 200, 240), name='noon_mid')
sky_low = out.color((182, 216, 244), name='noon_low')

def sky_color(y):
    if y < 34:
        return sky_top
    if y < 62:
        return sky_hi
    if y < 82:
        return sky_mid
    return sky_low

for y in range(h):
    if y > 96:
        continue
    for x in range(w):
        idx = out.get(x, y)
        r, g, b, a = get_rgba(idx)
        if a == 0:
            continue
        # keep silhouettes / buildings / the red pagoda body
        if lum((r, g, b, a)) < 60:
            continue
        if r - b >= 55:          # warm red pagoda / building parts in daylight
            continue
        out.set(x, y, sky_color(y))

finish(out)
print(out.stats_text())
