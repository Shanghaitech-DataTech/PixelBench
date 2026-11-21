import colorsys
c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
def cls(idx):
    r, g, b, a = pal[idx]
    R, G, B = r/255, g/255, b/255
    h, l, s = colorsys.rgb_to_hls(R, G, B)
    hue = h*360
    if s < 0.20:
        return ".':-=+#@"[max(0, min(6, int(l*7)))]
    if hue < 20 or hue >= 340: ch = 'R'
    elif hue < 45: ch = 'O'
    elif hue < 70: ch = 'Y'
    elif hue < 160: ch = 'G'
    elif hue < 200: ch = 'C'
    elif hue < 260: ch = 'B'
    elif hue < 320: ch = 'M'
    else: ch = 'P'
    return ch if l > 0.30 else ch.lower()
x0, x1, y0, y1 = 68, 146, 48, 160
print("    " + "".join(str((x//10)%10) for x in range(x0, x1)))
print("    " + "".join(str(x%10) for x in range(x0, x1)))
for y in range(y0, y1):
    print("%3d " % y + "".join(cls(c.get(x, y)) for x in range(x0, x1)))
