import colorsys

w, h, rgba = input_canvas.to_rgba()
print("size", w, h, "bytes", len(rgba))

# Coarse ASCII map: 50 cols x ~15 rows
cols, rows = 62, 24
bw = w / cols
bh = h / rows

def char_for(px):
    r, g, b, a = px[0], px[1], px[2], px[3]
    hh, ll, ss = colorsys.rgb_to_hls(r/255, g/255, b/255)
    if a == 0:
        return "."
    if ll > 0.92:
        return "W"  # white
    if ll < 0.18:
        return "#"  # dark
    # hue bucket
    deg = hh * 360
    if ss < 0.12:
        return "0" if ll > 0.5 else "o"
    if deg < 20 or deg >= 340:
        return "R"
    if deg < 45:
        return "O"
    if deg < 70:
        return "Y"
    if deg < 160:
        return "G"
    if deg < 200:
        return "C"
    if deg < 260:
        return "B"
    if deg < 300:
        return "P"
    return "M"

out = []
for ry in range(rows):
    line = ""
    for rx in range(cols):
        x0 = int(rx * bw); x1 = max(x0 + 1, int((rx + 1) * bw))
        y0 = int(ry * bh); y1 = max(y0 + 1, int((ry + 1) * bh))
        # average colour in block
        rs = gs = bs = n = 0
        for y in range(y0, min(y1, h)):
            for x in range(x0, min(x1, w)):
                i = (y * w + x) * 4
                rs += rgba[i]; gs += rgba[i+1]; bs += rgba[i+2]; n += 1
        r = rs // n; g = gs // n; b = bs // n
        line += char_for((r, g, b, 255))
    out.append(line)
print("\n".join(out))
