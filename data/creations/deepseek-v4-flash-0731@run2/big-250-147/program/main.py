from pixelbench_api import *

out = input_canvas.copy(name='output')
W, H = 250, 147
pal = out.palette()

def rgba(i):
    return tuple(pal[i]['rgba'])

def is_glow(i):
    r, g, b, a = rgba(i)
    return a > 0 and r >= 150 and g >= 108 and (r - b) >= 22

# Remove the sun and its halo from the sky (noon sky: sun is out of frame).
# Repaint only the warm region pixels using clear sky at the same row on the
# right side of the sun, leaving the already-sky pixels untouched so no seam
# is introduced in the textured sky.
for y in range(10, 64):
    for x in range(86, 164):
        if is_glow(out.get(x, y)):
            sx = x + 70
            out.set(x, y, out.get(sx, y))

# check: no bright sun colours remain in the sky band
def sunlike(i):
    r, g, b, a = rgba(i)
    return a > 0 and r > 200 and g > 185 and b > 150
n = 0
for y in range(0, 90):
    for x in range(0, W):
        if sunlike(out.get(x, y)):
            n += 1
print("bright sun pixels left in sky:", n)
print(out.stats_text())

finish(out)
