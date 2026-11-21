result = input_canvas.copy(name='output')
for y in range(52, 58):
    for x in range(64):
        idx = result.get(x, y)
        if idx in (6, 7, 8):
            result.set(x, y, 5)

orig = input_canvas
letters = {1:'.', 2:'#', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}

diff = []
for y in range(64):
    for x in range(64):
        if orig.get(x, y) != result.get(x, y):
            diff.append((x, y, orig.get(x, y), result.get(x, y)))
print(f"Changed pixels: {len(diff)}")
ys = set(y for _, y, _, _ in diff)
xs = set(x for x, _, _, _ in diff)
print(f"y range: {min(ys)}-{max(ys)}, x range: {min(xs)}-{max(xs)}")

print("\nFull result:")
hdr = "     " + "".join(str(x // 10) for x in range(64))
hdr2 = "     " + "".join(str(x % 10) for x in range(64))
print(hdr)
print(hdr2)
for y in range(64):
    line = "".join(letters[result.get(x, y)] for x in range(64))
    print(f"{y:3d} {line}")
