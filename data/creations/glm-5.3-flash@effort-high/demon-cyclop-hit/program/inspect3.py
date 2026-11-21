f2 = canvas('recoil')
w, h = 44, 38
pal = {}
print('    ' + ''.join(str(i % 10) for i in range(w)))
for y in range(h):
    row = ''
    for x in range(w):
        i = f2.get(x, y)
        row += {0:'.',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}.get(i,'?')
    print(f'{y:3d} {row}')
