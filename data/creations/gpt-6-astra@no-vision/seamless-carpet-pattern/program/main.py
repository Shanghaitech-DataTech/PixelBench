result = new_canvas(32, 32, background='#48262b', name='warm_floral_carpet')
# A compact rug palette: walnut, madder, terracotta, old gold and flax.
P = {'ink':'#382329','wine':'#642d35','red':'#903d3c','rust':'#b65a43','clay':'#d58152','gold':'#cb9b57','cream':'#ecd097','olive':'#77734b','sage':'#a49b61','brown':'#795039'}
# Folded coordinates make opposing edges pixel-identical, including the weave.
for y in range(32):
    for x in range(32):
        u,v=min(x,31-x),min(y,31-y)
        edge=min(u,v)
        weave=(u+v)%2
        col=P['wine'] if weave else P['red']
        if edge==0:
            col=P['brown'] if max(u,v)%4 in (1,2) else P['ink']
        elif edge<=4:
            col=P['wine'] if weave else P['ink']
        elif edge==5:
            col=P['gold'] if weave else P['brown']
        elif edge==6:
            col=P['ink']
        else:
            col=P['wine'] if weave else P['red']
        result.set(x,y,col)
# The floral ribbon repeats around the frame. Work symmetrically in half-pixel units.
for y in range(32):
    for x in range(32):
        u,v=min(x,31-x),min(y,31-y)
        col=None
        if (v==3 and u>=2) or (u==3 and v>=2): col=P['olive']
        # Small four-petal blossoms, centered in each side's border.
        for center in (7.5,15.5,23.5):
            for cx,cy in ((center,2.5),(center,28.5),(2.5,center),(28.5,center)):
                dx,dy=abs(x-cx),abs(y-cy)
                if dx<=1.5 and dy<=1.5:
                    if dx==.5 and dy==.5: col=P['rust']
                    elif dx+dy==2: col=P['cream'] if dy==1.5 else P['gold']
        # Corner rosettes tie adjacent bands together.
        if u in (2,3) and v in (2,3): col=P['gold']
        if (u==1 and v in (2,3)) or (v==1 and u in (2,3)): col=P['rust']
        if col: result.set(x,y,col)
# Nested stepped diamond, drawn from a discrete Manhattan distance.
for y in range(6,26):
    for x in range(6,26):
        a,b=abs(x-15.5),abs(y-15.5)
        d=int(a+b)
        u,v=min(x,31-x),min(y,31-y)
        col=None
        if d==10: col=P['ink']
        elif d==9: col=P['gold']
        elif d==8: col=P['cream'] if (u+v)%4==0 else P['clay']
        elif d==7: col=P['ink']
        elif d<=6: col=P['rust'] if (u+v)%2 else P['red']
        if col: result.set(x,y,col)
# Eight-point floral jewel inside the diamond, with a flax center.
for y in range(11,21):
    for x in range(11,21):
        a,b=abs(x-15.5),abs(y-15.5)
        col=None
        if (a==.5 and b<=4.5) or (b==.5 and a<=4.5): col=P['gold']
        if (a==1.5 and b==2.5) or (b==1.5 and a==2.5): col=P['cream']
        if a==1.5 and b==1.5: col=P['ink']
        if a==.5 and b==.5: col=P['cream']
        if col: result.set(x,y,col)
# Olive leaf stitches in the four negative-space corners.
for x,y in ((8,8),(9,9),(8,10),(10,8)):
    for xx,yy in ((x,y),(31-x,y),(x,31-y),(31-x,31-y)):
        result.set(xx,yy,P['sage'] if x==y else P['olive'])
print(result.stats_text())
print(result.matrix_text())
assert all(result.get(0,y)==result.get(31,y) for y in range(32))
assert all(result.get(x,0)==result.get(x,31) for x in range(32))
save('warm_floral_carpet',result)
finish(result)
