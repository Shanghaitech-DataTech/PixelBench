out = input_canvas.copy(name="output")
out.mirror(axis="h")
rot = out.select(0, 0, 93, 128).rotate(53, algorithm="rotsprite").preview()
pal = rot.palette()
letters = "abcdefghijklmnopqrstuvwxyz"
rev = {}
for k, q in enumerate(pal):
    if q["index"] > 0:
        rev[q["index"]] = letters[k % len(letters)]

def dump(canvas, x0, x1, y0, y1):
    hdr = "      " + "".join(str((x // 10) % 10) for x in range(x0, x1))
    print(hdr)
    hdr2 = "      " + "".join(str(x % 10) for x in range(x0, x1))
    print(hdr2)
    for y in range(y0, y1):
        row = ""
        for x in range(x0, x1):
            i = canvas.get(x, y)
            row += "." if i == 0 else rev.get(i, "?")
        print("y=%3d %s" % (y, row))

print("=== rotated blade, x 60..159 ===")
dump(rot, 60, 159, 62, 95)
