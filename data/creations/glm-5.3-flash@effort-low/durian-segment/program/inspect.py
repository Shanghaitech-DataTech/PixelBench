c = input_canvas
# print color-index map rows 40-60, columns 0-55
for y in range(38, 60):
    row = ""
    for x in range(0, 56):
        i = c.get(x, y)
        row += "." if i in (None, 1) else chr(64 + i)
    print(f"{y:2d} {row}")
