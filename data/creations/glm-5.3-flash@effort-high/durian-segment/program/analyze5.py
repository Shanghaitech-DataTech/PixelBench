ic = input_canvas
letters = {1:'.', 2:'#', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}
print("Bottom segment region (y 50-58, x 8-42):")
hdr = "     " + "".join(str(x // 10) for x in range(8, 43))
hdr2 = "     " + "".join(str(x % 10) for x in range(8, 43))
print(hdr)
print(hdr2)
for y in range(50, 59):
    line = "".join(letters[ic.get(x, y)] for x in range(8, 43))
    print(f"{y:3d} {line}")
print()
print("Rind colors used in upper rind region (y 8-11, x 44-56):")
for y in range(8, 12):
    line = "".join(letters[ic.get(x, y)] for x in range(44, 56))
    print(f"{y:3d} {line}")
print()
print("Rind colors used at right edge of flesh (y 20-24, x 50-58):")
for y in range(20, 25):
    line = "".join(letters[ic.get(x, y)] for x in range(50, 58))
    print(f"{y:3d} {line}")
