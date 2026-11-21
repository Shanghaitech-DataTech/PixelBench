from pixelbench_api import *

c = input_canvas
out = c.copy(name='output')
w, h = out.stats()['size']

pal = c.palette()
rgba = {p['index']: tuple(p['rgba']) for p in pal}

def lum(idx):
    r, g, b, a = rgba[idx]
    return (r + g + b) // 3

# Mountain silhouette: first row from the top where the pixel is dark terrain.
horizon = [h] * w
for x in range(w):
    for y in range(h):
        if lum(out.get(x, y)) < 110:
            horizon[x] = y
            break

hmax = max(horizon)
hmax = max(hmax, 1)

# Clear noon sky: deep blue at the zenith, pale blue at the horizon.
TOP = (80, 135, 220)
BOT = (190, 222, 250)
cache = {}

def sky_idx(y):
    if y not in cache:
        t = y / float(hmax)
        if t > 1.0:
            t = 1.0
        r = int(round(TOP[0] + (BOT[0] - TOP[0]) * t))
        g = int(round(TOP[1] + (BOT[1] - TOP[1]) * t))
        b = int(round(TOP[2] + (BOT[2] - TOP[2]) * t))
        cache[y] = out.color((r, g, b))
    return cache[y]

# Repaint the sky (which includes the old sun disc) with the blue gradient.
for x in range(w):
    for y in range(horizon[x]):
        out.set(x, y, sky_idx(y))

print("horizon min/max:", min(horizon), max(horizon))
print(out.stats_text())
finish(out)
