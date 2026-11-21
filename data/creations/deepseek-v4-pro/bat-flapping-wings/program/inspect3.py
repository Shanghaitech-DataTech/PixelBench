from pixelbench_api import *

c = input_canvas
# print legend with letters
names = {0:'.',1:'k',2:'b',3:'p',4:'P',5:'g',6:'r',7:'y',8:'m'}
for y in range(22):
    row=[]
    for x in range(27):
        i=c.get(x,y)
        row.append(names.get(i,'?'))
    print(f"{y:2d} " + ''.join(row))
