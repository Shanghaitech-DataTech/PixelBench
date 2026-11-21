from pixelbench_api import *

c = new_canvas(32, 32)
a = c.color((245, 236, 220), "a")
o = c.color((92, 62, 44), "o")
c.ellipse(16, 17, 9, 7, a)
c.rect(13, 10, 7, 3, a)   # flatten top
c.rect(13, 22, 7, 3, a)   # flatten bottom
c.outline(o)
for y in range(8, 26):
    row = ""
    for x in range(32):
        n = c.color_name(c.get(x, y))
        row += "a" if n == "a" else ("o" if n == "o" else ".")
    print(f"{y:02d} {row}")
