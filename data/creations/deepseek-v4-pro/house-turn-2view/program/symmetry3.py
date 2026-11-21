import numpy as np
c = input_canvas
W,H,inds,pal = c.to_indexed(scale=1)
inds = np.frombuffer(inds, dtype=np.uint8).reshape((H,W))
# binarize: visible = index not 0 and not 11
vis = (inds!=0)&(inds!=11)
diff=0; n=0
for y in range(H):
    for x in range(W//2):
        a=vis[y,x]; b=vis[y,W-1-x]
        if a!=b: diff+=1
        n+=1
print("visible bbox diff:", diff, "/", n, "=", diff/n)
# also per-row structural diff
for y in range(0,H,10):
    d=sum(1 for x in range(W//2) if vis[y,x]!=vis[y,W-1-x])
    print(y,d)
