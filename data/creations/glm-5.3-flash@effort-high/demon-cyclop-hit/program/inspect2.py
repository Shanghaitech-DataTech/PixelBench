c = input_canvas
w, h = 37, 33
# print rows with a ruler
ruler = ''.join(str(i % 10) for i in range(w))
print('    ' + ruler)
for y in range(h):
    row = ''.join({0:'.',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f'}.get(c.get(x,y),'?') for x in range(w))
    print(f'{y:3d} {row}')
