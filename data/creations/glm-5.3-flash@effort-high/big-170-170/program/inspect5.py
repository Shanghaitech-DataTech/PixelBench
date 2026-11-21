import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.array(rgba).reshape(h,w,4)

def dump(x0,y0,x1,y1,step=1):
    print('cols', list(range(x0,x1,step)))
    for y in range(y0,y1,step):
        line=''
        for x in range(x0,x1,step):
            r,g,b,al = a[y,x]
            ch='.'
            if b>60 and r<40 and g<80: ch='B'
            elif r>200 and g>180: ch='W'
            elif r>150 and g<140 and b<160: ch='w'
            elif abs(int(r)-int(g))<20 and abs(int(g)-int(b))<20 and 60<r<160: ch='g'
            line+=ch
        print('%3d %s'%(y,line))

dump(0,100,170,170,1)
