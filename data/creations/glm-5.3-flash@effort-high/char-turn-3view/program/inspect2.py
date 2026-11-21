c = input_canvas
w, h = 66, 119
rgba = c.to_rgba()[2]

def px(x, y):
    return bytes(rgba[(y*w+x)*4:(y*w+x)*4+4])

# legend by colour
names = {
 b'\x00\x00\x00\x00':'.', b'\x05\x01\x00\xff':'b', b'\xa8\xb2\xc1\xff':'c',
 b'\x54\x56\x65\xff':'d', b'\xe0\xf4\xfa\xff':'e', b'\xfd\xd5\xb7\xff':'f',
 b')\x0e\x02\xff':'g', b'v{\x90\xff':'h', b'B\x16\x03\xff':'i',
 b'\xff\xff\xff\xff':'j', b'(\x18 \xff':'k', b'\x16\x07\x01\xff':'l',
 b'\xea\xa3w\xff':'m', b'\x9e>7\xff':'n', b'\xd2\x85`\xff':'o',
 b'_\x1f\x04\xff':'p', b'y(\x06\xff':'q', b'\xfb\xec\xe6\xff':'r',
 b'\xf2\xf8\xf9\xff':'s', b'\x0b!9\xff':'t', b')=K\xff':'u',
 b'I%D\xff':'v', b'P\xd4\xec\xff':'w', b'Q\x87\xb3\xff':'x'}

# ruler
ruler1 = ''.join(str((x//10)%10) for x in range(w))
ruler2 = ''.join(str(x%10) for x in range(w))
print("    " + ruler1)
print("    " + ruler2)
for y in range(24, 58):
    row = ""
    for x in range(w):
        row += names.get(px(x,y),'?')
    print(f"{y:3d} " + row)
print()
# RLE for key rows
for y in [27, 33, 40, 42, 45, 47, 49, 51, 53]:
    runs = []
    cur = None; start = 0
    for x in range(w):
        ch = names.get(px(x,y),'?')
        if ch != cur:
            if cur is not None:
                runs.append((cur, start, x-1))
            cur = ch; start = x
    runs.append((cur, start, w-1))
    print(y, runs)
