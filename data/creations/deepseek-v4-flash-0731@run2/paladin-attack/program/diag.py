from pixelbench_api import *
c = input_canvas
def dump(y0, y1, x0=0, x1=42):
    print("    " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            idx = c.get(x, y)
            row += chr(64 + idx) if idx else "."
        print(f"{y:3d} {row}")
print("UPPER BODY rows 0-26:")
dump(0, 26)
print("LOWER rows 33-56:")
dump(33, 56)
