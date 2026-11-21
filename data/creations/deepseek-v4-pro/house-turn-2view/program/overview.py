import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
mp = {0:'.',1:'B',2:'b',3:'W',4:'#',5:'G',6:'Y',7:'y',8:'D',9:'r',10:'R',11:'s',12:'P',13:'Q'}
# downsample by 2x2 using first non-transparent? just majority
for y in range(0,H,2):
    line=[]
    for x in range(0,W,2):
        block=inds[y:y+2,x:x+2]
        vals=[v for v in block.flatten() if v!=0]
        if not vals:
            line.append('.')
        else:
            # pick most frequent visible
            v=max(set(vals), key=vals.count)
            line.append(mp.get(v,'?'))
    print(''.join(line))
