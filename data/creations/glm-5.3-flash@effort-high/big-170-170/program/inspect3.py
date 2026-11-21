import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.array(rgba).reshape(h,w,4)
warm = ((a[:,:,0].astype(int) - a[:,:,2].astype(int)) > 30)

def dump(x0,y0,x1,y1,step=1):
    for y in range(y0,y1,step):
        line=''
        for x in range(x0,x1,step):
            line += '#' if warm[y,x] else '.'
        print('%3d %s'%(y,line))

dump(25,115,125,170)
