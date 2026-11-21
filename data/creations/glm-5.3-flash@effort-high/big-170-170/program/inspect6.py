import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.array(rgba).reshape(h,w,4)
# print actual colors along some columns/rows
def line(y, x0, x1):
    print('y=%d'%y, ' '.join('#%02x%02x%02x'%tuple(a[y,x][:3]) for x in range(x0,x1)))
def vline(x, y0, y1):
    print('x=%d'%x)
    for y in range(y0,y1):
        print('  %3d #%02x%02x%02x'%(y,*a[y,x][:3]))
line(140, 0, 170)
line(165, 0, 170)
vline(0, 0, 170)
vline(169, 0, 170)
line(0, 0, 170)
line(169, 0, 170)
