c = input_canvas
sym = {0:'.',1:'#',2:'@',3:'O',4:'+',5:'&',6:':',7:'g',8:'r',9:'%',10:'S',11:'W',12:'x',13:'x',14:'b',15:'h'}
print('hand/sword region orig x44-61, y33-48')
print('    ' + ''.join(str(x%10) for x in range(44,62)))
for y in range(33, 49):
    print('%3d %s' % (y, ''.join(sym[c.get(x,y)] for x in range(44,62))))
