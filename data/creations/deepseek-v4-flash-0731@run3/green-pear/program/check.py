from pixelbench_api import new_canvas, finish, canvas

c = canvas("pear")
# column symbols per palette index
cols = {}
for i, info in enumerate(c.palette()):
    cols[info["index"]] = "ABCDEFGH"[(i % 8)]
print("legend:", [(k, c.color_name(k)) for k in cols])
for y in range(0, 30):
    line = ""
    for x in range(0, 32):
        idx = c.get(x, y)
        line += cols.get(idx, ".")
    print(line)
