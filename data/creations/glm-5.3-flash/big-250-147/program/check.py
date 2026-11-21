import colorsys

# find the output canvas by name
out = canvas("output")
w, h, rgba = out.to_rgba()

def px(x, y):
    i = (y*w + x)*4
    return rgba[i], rgba[i+1], rgba[i+2], rgba[i+3]

# 1) any remaining warm pixels (r - g > 25) anywhere?
warm = []
for y in range(h):
    for x in range(w):
        r, g, b, a = px(x, y)
        if r - g > 25:
            warm.append((x, y, (r, g, b)))
print("warm pixels left:", len(warm))
for t in warm[:20]:
    print("   ", t)

# 2) sky uniformity: for each row, min/max G among sky-ish (blue) pixels
print("\nsky row stats (blue pixels only, b > r):")
for y in range(0, 70, 4):
    gs = [px(x, y)[1] for x in range(w) if px(x, y)[2] > px(x, y)[0]]
    if gs:
        print(" y=%3d minG=%3d maxG=%3d meanG=%3d n=%d" % (y, min(gs), max(gs), sum(gs)//len(gs), len(gs)))

# 3) fine map of sky y 0..64 at 2x2 to spot mottling / ring
def char_for(c):
    r, g, b, a = c
    hh, ll, ss = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    if ll > 0.90: return "W"
    if ll > 0.78: return "w"
    if ll > 0.66: return "-"
    if ll < 0.15: return "#"
    if ll < 0.30: return "%"
    if ss < 0.15: return "0"
    deg = hh * 360
    if deg < 20 or deg >= 340: return "R"
    if deg < 45: return "O"
    if deg < 70: return "Y"
    if deg < 160: return "G"
    if deg < 200: return "C"
    if deg < 260: return "B"
    if deg < 300: return "P"
    return "M"

print("\nresult sky map (2x2 blocks), x 0-250:")
for by in range(0, 66, 2):
    line = ""
    for bx in range(0, 250, 2):
        rs = gs = bs = n = 0
        for y in range(by, by+2):
            for x in range(bx, bx+2):
                r, g, b, a = px(x, y)
                rs += r; gs += g; bs += b; n += 1
        line += char_for((rs//n, gs//n, bs//n, 255))
    print("%3d %s" % (by, line))
