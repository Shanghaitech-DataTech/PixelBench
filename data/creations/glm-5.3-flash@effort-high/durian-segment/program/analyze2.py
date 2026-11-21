ic = input_canvas
letters = {1:'.', 2:'#', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}
hdr = "    " + "".join(str(x // 10) for x in range(64))
hdr2 = "    " + "".join(str(x % 10) for x in range(64))
print(hdr)
print(hdr2)
for y in range(0, 64):
    line = "".join(letters[ic.get(x, y)] for x in range(64))
    print(f"{y:3d} {line}")
