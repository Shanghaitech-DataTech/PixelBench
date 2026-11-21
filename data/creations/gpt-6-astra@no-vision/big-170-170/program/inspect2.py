import numpy as np
w,h,raw=input_canvas.to_rgba(); a=np.frombuffer(raw,dtype=np.uint8).reshape(h,w,4)[:,:,:3].astype(float)
rng=np.random.default_rng(4); cent=a.reshape(-1,3)[rng.choice(w*h,50,False)]
for i in range(35):
 d=((a[:,:,None,:]-cent)**2).sum(3).argmin(2)
 cent=np.array([a[d==k].mean(0) if np.any(d==k) else cent[k] for k in range(50)])
chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn'
print('Legend',[(chars[k],tuple(cent[k].astype(int))) for k in range(50)])
for y in range(108,163):
 print(f'{y:03d} '+''.join(chars[d[y,x]] for x in range(40,123)))
