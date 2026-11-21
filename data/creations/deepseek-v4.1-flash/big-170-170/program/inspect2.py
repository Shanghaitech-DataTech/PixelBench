c = input_canvas
ramp = " .:-=+*#%@"
h = 170
w = 170
lines = []
for y in range(0, h, 1):
    row = ""
    for x in range(0, w, 1):
        r, g, b = (c.palette()[c.get(x, y)]['rgba'][0], c.palette()[c.get(x, y)]['rgba'][1], c.palette()[c.get(x, y)]['rgba'][2])
        lum = (0.299*r + 0.587*g + 0.114*b) / 255.0
        row += ramp[min(9, int(lum*10))]
    lines.append(row)
print("    " + "".join(str((i//10)%10) for i in range(w)))
print("    " + "".join(str(i%10) for i in range(w)))
for y, l in enumerate(lines):
    print("%3d "%y + l)
