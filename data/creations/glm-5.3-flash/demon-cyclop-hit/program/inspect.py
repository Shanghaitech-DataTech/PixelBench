c = input_canvas
w, h = 37, 33
print("    " + "".join(str(i % 10) for i in range(w)))
for y in range(h):
    row = []
    for x in range(w):
        idx = c.get(x, y)
        if idx == 0 or idx is None:
            row.append(".")
        else:
            row.append(chr(ord('a') + idx - 1))
    print(f"{y:3d} " + "".join(row))
print()
print("palette:", c.palette())
