from pixelbench_api import input_canvas, finish

c = input_canvas
w, h = c.stats()["size"]
pal = {p["index"]: p["rgba"] for p in c.palette()}

def lum(rgba):
    r, g, b = rgba[0], rgba[1], rgba[2]
    return (2 * r + 3 * g + b) / 6.0

skyline = []
for x in range(w):
    sl = h
    for y in range(h):
        if lum(pal[c.get(x, y)]) < 100:
            sl = y
            break
    skyline.append(sl)

print("skyline min,max:", min(skyline), max(skyline))
# downsampled silhouette (every 4 cols)
chars = []
for x in range(0, w, 4):
    chars.append("%3d" % skyline[x])
print(' '.join(chars))
print("skyline:", skyline)
