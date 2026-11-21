from pixelbench_api import *

src = input_canvas
names = {0:'.',1:'k',2:'b',3:'p',4:'P',5:'g',6:'r',7:'y',8:'m'}

dy = 10
ys = 5.5
W, H = 27, 32
c = new_canvas(W, H, name='frame2proto')

# body copy x in 9..17
for y in range(src.h):
    for x in range(9, 18):
        i = src.get(x, y)
        if i:
            c.set(x, y + dy, i)

# flipped left wing: x in 0..9, y in 5..21
for y in range(5, 22):
    for x in range(0, 10):
        i = src.get(x, y)
        if i:
            ny = dy + int(round(2*ys - y))
            if 0 <= ny < H:
                c.set(x, ny, i)

# flipped right wing: x in 17..26, y in 5..21
for y in range(5, 22):
    for x in range(17, 27):
        i = src.get(x, y)
        if i:
            ny = dy + int(round(2*ys - y))
            if 0 <= ny < H:
                c.set(x, ny, i)

# print with header
print('   ' + ''.join(str(x%10) for x in range(W)))
for y in range(H):
    row=[]
    for x in range(W):
        i=c.get(x,y)
        row.append(names.get(i,'?'))
    print(f"{y:2d} " + ''.join(row))
