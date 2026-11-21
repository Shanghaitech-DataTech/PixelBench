w, h, rgba = input_canvas.to_rgba()

def px(x, y):
    i = (y*w + x)*4
    return (rgba[i], rgba[i+1], rgba[i+2], rgba[i+3])

# exact map of sun region x 92-158, y 8-64, 1px blocks, symbols per colour
from collections import defaultdict
sym = {}
order = []
def symbol_for(c):
    if c not in sym:
        s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()"
        sym[c] = s[len(sym) % len(s)]
        order.append(c)
    return sym[c]

lines = []
for y in range(8, 65):
    line = ""
    for x in range(92, 159):
        line += symbol_for(px(x, y))
    lines.append(f"{y:3d} {line}")

for c in order:
    print(sym[c], c)
print()
print("\n".join(lines))
