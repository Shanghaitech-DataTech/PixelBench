import colorsys
c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
def cls(idx):
    r, g, b, a = pal[idx]
    R, G, B = r/255, g/255, b/255
    h, l, s = colorsys.rgb_to_hls(R, G, B)
    hue = h*360
    if s < 0.22:
        ramp = ".':-=+#@"[:max(1,min(7,int(l*7)+1))]
        return ramp
    if s < 0.45 and l < 0.35:
        ramp = ",:;=+#@"[:max(1,min(7,int(l*7)+1))]
        return ramp
    if hue < 20 or hue >= 340: ch = 'R'
    elif hue < 45: ch = 'O'
    elif hue < 70: ch = 'Y'
    elif hue < 160: ch = 'G'
    elif hue < 200: ch = 'C'
    elif hue < 260: ch = 'B'
    elif hue < 320: ch = 'M'
    else: ch = 'P'
    return ch if l > 0.35 else ch.lower()
lines = []
for y in range(170):
    row = "".join(cls(c.get(x, y)) for x in range(170))
    lines.append(row)
print("    " + "".join(str((i//10)%10) for i in range(170)))
print("    " + "".join(str(i%10) for i in range(170)))
for y, l in enumerate(lines):
    print("%3d "%y + l)
