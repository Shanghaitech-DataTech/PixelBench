w, h = input_canvas.stats()["size"]
rev = {p["index"]: "abcdefghi"[p["index"] - 1] for p in input_canvas.palette() if p["index"] > 0}

def dump(y0, y1, x0=0, x1=None):
    if x1 is None:
        x1 = w
    for y in range(y0, y1):
        s = ""
        for x in range(x0, x1):
            i = input_canvas.get(x, y)
            s += "." if i == 0 else rev.get(i, "?")
        print("y=%3d %s" % (y, s))

print("=== rows 12-20 (tip) ===")
dump(12, 20, 0, 30)
print("=== rows 40-46 (mid blade) ===")
dump(40, 46, 8, 46)
print("=== rows 68-80 (heel/bolster) ===")
dump(68, 80, 28, 72)
print("=== rows 80-92 (handle start) ===")
dump(80, 92, 44, 76)
