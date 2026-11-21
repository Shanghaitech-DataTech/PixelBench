from pixelbench_api import input_canvas, finish

c = input_canvas
w, h = c.stats()["size"]
pal = {p["index"]: p["rgba"] for p in c.palette()}

def lum(rgba):
    r, g, b = rgba[0], rgba[1], rgba[2]
    return (2 * r + 3 * g + b) / 6.0

def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))

def scale(rgb, f):
    return tuple(max(0, min(255, int(round(rgb[i] * f)))) for i in range(3))

# Skyline: first pixel with luminance < 100 per column = top of the dark
# landscape silhouette. Everything above is sky (including the sunset disc).
skyline = []
for x in range(w):
    sl = h
    for y in range(h):
        if lum(pal[c.get(x, y)]) < 100:
            sl = y
            break
    skyline.append(sl)
HORIZON = max(skyline)  # lowest sky row == 100

# Noon clear-day palette
SKY_TOP = (46, 112, 200)     # deep clear blue
SKY_BOT = (178, 216, 248)    # pale blue at the horizon
G_DARK = (18, 40, 22)        # deep forest green
G_LIT = (112, 172, 98)       # sunlit foliage
HAZE = (170, 205, 190)       # pale green atmospheric haze

out = c.copy(name="output")
for y in range(h):
    sky_t = min(1.0, y / float(max(1, HORIZON - 1)))
    for x in range(w):
        sl = skyline[x]
        if y < sl:
            out.set(x, y, lerp(SKY_TOP, SKY_BOT, sky_t))
        else:
            t = min(1.0, lum(pal[c.get(x, y)]) / 150.0)
            base = lerp(G_DARK, G_LIT, t)
            d = (y - sl) / float(max(1, h - 1 - sl))
            haze_amt = max(0.0, 0.45 * (1.0 - 2.2 * d))   # distant ridge is hazy
            col = lerp(base, HAZE, haze_amt)
            dark = 1.0 - 0.35 * max(0.0, d - 0.15)        # foreground darkens
            col = scale(col, dark)
            out.set(x, y, col)

print(out.stats_text())
finish(out)
