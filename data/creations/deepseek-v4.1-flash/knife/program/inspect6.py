from collections import defaultdict
work = new_canvas(220, 220, background=None, name='wn')
sel = input_canvas.select(0, 0, 93, 128)
r = sel.rotate(125, algorithm='nearest')
r.copy_to(0, 0, work)

def anatomy(c, label):
    w,h,data=c.to_rgba()
    d=defaultdict(list)
    for y in range(h):
        for x in range(w):
            a=data[(y*w+x)*4+3]
            if a>0:
                col=tuple(data[(y*w+x)*4:(y*w+x)*4+4])
                d[col].append((x,y))
    print('==',label)
    for col,pts in sorted(d.items(), key=lambda kv:-len(kv[1])):
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        cx=sum(xs)/len(xs); cy=sum(ys)/len(ys)
        print('#%02x%02x%02x n=%4d bbox=(%3d,%3d)-(%3d,%3d) centroid=(%.1f,%.1f)'%(
            col[0],col[1],col[2],len(pts),min(xs),min(ys),max(xs),max(ys),cx,cy))

anatomy(input_canvas,'INPUT')
anatomy(work,'ROT125')
