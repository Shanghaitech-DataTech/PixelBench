# Pure-python replay of main.py's drawing calls to probe exact pixels.
src = open("main.py").read()
for kill in ('print(c.stats_text())', 'print(c.matrix_text())',
             'save("dim_sum_chef", c)', 'finish(c)'):
    src = src.replace(kill, 'pass')

class Stub:
    def __init__(self, w, h, background=None, name=None):
        self.w, self.h, self.px, self.names = w, h, {}, {}
    def color(self, spec, name=None):
        if name: self.names[spec] = name
        return spec
    def set(self, x, y, col): self.px[(x, y)] = col
    def outline(self, col):
        op = set(self.px); border = set()
        for (x, y) in op:
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                if (x+dx, y+dy) not in op:
                    border.add((x, y)); break
        for p in border: self.px[p] = col

g = {"new_canvas": Stub}
exec(compile(src, "main", "exec"), g, g)
c = g["c"]
rev = {v: k for k, v in c.names.items()}

def show(x0, y0, x1, y1):
    print("    " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            col = c.px.get((x, y))
            row += "." if col is None else rev.get(col, "?")[0]
        print(f"{y:2d}  {row}")

print("== steamer + hands, cols 3-28 ==")
show(3, 16, 28, 25)
print("== probes (x,y -> colour) ==")
for (x, y) in [(5,18),(6,18),(5,19),(6,19),(7,19),(5,20),(6,20),(7,20),(4,21),(5,21),
               (24,19),(25,19),(24,20),(25,20),(10,20),(13,20),(9,21),(22,21),
               (10,19),(21,19),(11,17),(12,17),(13,17),(14,17)]:
    print((x, y), c.px.get((x, y), "transparent"))
