c = input_canvas
import numpy as np
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
mp = {0:'.',1:'B',2:'b',3:'W',4:'#',5:'G',6:'Y',7:'y',8:'D',9:'r',10:'R',11:'s',12:'P',13:'Q'}
for y in range(0, 55):
    print(f"{y:3d} " + ''.join(mp.get(v,'?') for v in inds[y]))
