ic = input_canvas
letters = {1:'.', 2:'#', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}
print("Bottom region 4-58 x 4-44:")
hdr = "     " + "".join(str(x // 10) for x in range(4, 45))
hdr2 = "     " + "".join(str(x % 10) for x in range(4, 45))
print(hdr)
print(hdr2)
for y in range(4, 59):
    line = "".join(letters[ic.get(x, y)] for x in range(4, 45))
    print(f"{y:3d} {line}")
