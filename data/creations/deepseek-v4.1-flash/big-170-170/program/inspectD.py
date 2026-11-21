c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
def lum(x, y):
    r, g, b, a = pal[c.get(x, y)]
    return 0.299*r + 0.587*g + 0.114*b
x0, x1, y0, y1 = 70, 140, 50, 150
print("    " + "".join(str((x//10)%10) for x in range(x0, x1)))
print("    " + "".join(str(x%10) for x in range(x0, x1)))
for y in range(y0, y1):
    row = ""
    for x in range(x0, x1):
        L = lum(x, y)
        row += '#' if L < 40 else ('*' if L < 55 else ('o' if L < 70 else ('+' if L < 90 else ('.' if L < 120 else 'W'))))
    print("%3d " % y + row)
