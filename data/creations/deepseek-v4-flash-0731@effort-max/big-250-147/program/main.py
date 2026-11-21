from pixelbench_api import *

out = input_canvas.copy(name="output")
w, h = 250, 147
pal = {p['index']: p['rgba'] for p in out.palette()}

# ---- terrain silhouette: highest terrain point per column (sky = y < ytop(x)) ----
anchors = [(0,96),(10,84),(18,74),(26,66),(34,60),(42,57),(50,56),(58,58),
           (66,66),(74,78),(82,92),(90,100),(98,103),(106,102),(114,97),
           (122,90),(130,84),(140,78),(150,74),(160,71),(170,70),(180,71),
           (190,74),(196,66),(204,58),(212,53),(220,52),(230,53),(240,57),(249,64)]

def ytop(x):
    if x <= anchors[0][0]:
        return anchors[0][1]
    if x >= anchors[-1][0]:
        return anchors[-1][1]
    for i in range(len(anchors) - 1):
        x0, y0 = anchors[i]
        x1, y1 = anchors[i + 1]
        if x0 <= x <= x1:
            f = (x - x0) / (x1 - x0)
            return y0 + f * (y1 - y0)
    return anchors[-1][1]

def clamp(v):
    return 0 if v < 0 else (255 if v > 255 else int(round(v)))

TOP = (86, 140, 230)
BOT = (176, 208, 246)

def sky_colour(x, y, curve):
    t = y / max(1.0, curve)
    r = TOP[0] + (BOT[0] - TOP[0]) * t
    g = TOP[1] + (BOT[1] - TOP[1]) * t
    b = TOP[2] + (BOT[2] - TOP[2]) * t
    n = ((x * 7 + y * 13) % 5) - 2
    return (clamp(r + n), clamp(g + n), clamp(b + n), 255)

def daylight(r, g, b):
    return (clamp(r * 1.18 + 14), clamp(g * 1.22 + 18), clamp(b * 1.26 + 22), 255)

for y in range(h):
    for x in range(w):
        idx = out.get(x, y)
        r, g, b, a = pal[idx]
        curve = ytop(x)
        if y < curve:
            out.set(x, y, sky_colour(x, y, curve))
        else:
            out.set(x, y, daylight(r, g, b))

# ---- verification ----
print(out.stats_text())
m = out.matrix_text(region=(80, 0, 249, 110), indices=False)
print(m)

finish(out)
