import math
ANG = 125

def build(alg, ang, name):
    work = new_canvas(220, 220, background=None, name=name)
    sel = input_canvas.select(0, 0, 93, 128)
    r = sel.rotate(ang, algorithm=alg)
    r.copy_to(0, 0, work)
    return work

def bbox(c):
    w,h,data=c.to_rgba()
    xs=[];ys=[]
    for y in range(h):
        for x in range(w):
            if data[(y*w+x)*4+3]>0: xs.append(x); ys.append(y)
    return (min(xs),min(ys),max(xs),max(ys))

def crop(c, bb, name):
    x0,y0,x1,y1 = bb
    nc = new_canvas(x1-x0+1, y1-y0+1, background=None, name=name)
    w,h,ind, pal = c.to_indexed()
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            i = ind[y*w+x]
            if i: nc.set(x-x0, y-y0, i)
    return nc

wo = build('nearest', ANG, 'wn')
bb = bbox(wo); print('bbox', bb)
cr = crop(wo, bb, 'crn')
print(cr.stats_text())
print(cr.matrix_text())
