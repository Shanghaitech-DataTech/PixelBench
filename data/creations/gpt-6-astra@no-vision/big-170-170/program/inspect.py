import numpy as np
w,h,raw=input_canvas.to_rgba()
a=np.frombuffer(raw,dtype=np.uint8).reshape(h,w,4)[:,:,:3].astype(float)
rng=np.random.default_rng(8)
cent=a.reshape(-1,3)[rng.choice(w*h,20,False)]
for i in range(30):
 d=((a[:,:,None,:]-cent)**2).sum(3).argmin(2)
 cent=np.array([a[d==k].mean(0) if np.any(d==k) else cent[k] for k in range(20)])
chars='0123456789ABCDEFGHIJ'
print('Legend',[(chars[k],tuple(cent[k].astype(int))) for k in range(20)])
for y in range(0,170,2):
 print(f'{y:03d} '+''.join(chars[d[y:y+2,x:x+2].flatten()[0]] for x in range(0,170,2)))
print(input_canvas.matrix_text(region=(75,54,117,88),indices=True))
