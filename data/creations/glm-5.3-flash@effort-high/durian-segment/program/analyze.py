ic = input_canvas
pal = {p["index"]: p["name"] for p in ic.palette()}
print(pal)

FLESH = {6, 7, 8}   # f cream, g yellow, h light yellow
RIND = {4, 5, 9, 3} # d, e, i, c browns/oranges
OUT = {2}

# category map
rows = []
for y in range(64):
    line = ""
    for x in range(64):
        idx = ic.get(x, y)
        if idx == 1:
            line += "."
        elif idx == 2:
            line += "#"
        elif idx in FLESH:
            line += "F"
        elif idx in RIND:
            line += "R"
        else:
            line += "?"
    rows.append(line)

# print with ruler
hdr = "    " + "".join(str(x // 10) for x in range(64))
hdr2 = "    " + "".join(str(x % 10) for x in range(64))
print(hdr)
print(hdr2)
for y, line in enumerate(rows):
    print(f"{y:3d} {line}")
