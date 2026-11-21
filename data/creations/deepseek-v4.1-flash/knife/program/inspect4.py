import math
w, h, data = input_canvas.to_rgba()
def rgba(x,y):
    return tuple(data[(y*w+x)*4:(y*w+x)*4+4])

# --- PCA of blade-toned pixels (indices 2,3,4) ---
blade_cols = {(204,211,248,255),(164,173,217,255),(149,159,213,255)}
pts=[(x,y) for y in range(h) for x in range(w) if rgba(x,y) in blade_cols]
n=len(pts); mx=sum(p[0] for p in pts)/n; my=sum(p[1] for p in pts)/n
sxx=sum((p[0]-mx)**2 for p in pts)/n; syy=sum((p[1]-my)**2 for p in pts)/n
sxy=sum((p[0]-mx)*(p[1]-my) for p in pts)/n
th=0.5*math.atan2(2*sxy, sxx-syy)
print('blade n=%d centre=(%.1f,%.1f) axis=%.2f deg'%(n,mx,my,math.degrees(th)))

# --- PCA of whole silhouette ---
pts2=[(x,y) for y in range(h) for x in range(w) if rgba(x,y)[3]>0]
n2=len(pts2); mx2=sum(p[0] for p in pts2)/n2; my2=sum(p[1] for p in pts2)/n2
sxx=sum((p[0]-mx2)**2 for p in pts2)/n2; syy=sum((p[1]-my2)**2 for p in pts2)/n2
sxy=sum((p[0]-mx2)*(p[1]-my2) for p in pts2)/n2
th2=0.5*math.atan2(2*sxy, sxx-syy)
print('silhouette n=%d centre=(%.1f,%.1f) axis=%.2f deg'%(n2,mx2,my2,math.degrees(th2)))

# --- left/right edge per row of the big blade for rows 0..78 ---
for y in range(0,80,4):
    xs=[x for x in range(w) if rgba(x,y)[3]>0]
    if xs:
        print(y, min(xs), max(xs))
print()
for y in range(80,128,4):
    xs=[x for x in range(w) if rgba(x,y)[3]>0]
    if xs:
        print(y, min(xs), max(xs))
