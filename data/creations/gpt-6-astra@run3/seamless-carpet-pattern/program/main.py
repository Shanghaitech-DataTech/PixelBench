result = new_canvas(32,32,background='#612d32',name='warm_carpet')
# Muted wool dyes: oxblood, terracotta, saffron, flax, and olive.
p = {'ink':'#39282b','wine':'#612d32','wine2':'#71363a','red':'#a34d3b','rust':'#be6844','gold':'#d79751','flax':'#ecc78a','light':'#f4dca5','olive':'#77734a','leaf':'#a59b61'}
# Symmetric woven ground: paired edge yarns match in both directions.
for y in range(32):
    for x in range(32):
        u=min(x,31-x); v=min(y,31-y)
        result.set(x,y,p['wine2'] if (u+2*v)%4==0 else p['wine'])
        if u==0 or v==0: result.set(x,y,p['gold'] if (u+v)%4<2 else p['rust'])
        elif u==1 or v==1: result.set(x,y,p['ink'])
# Continuous floral border, hand knotted stems.
for a in range(2,30):
    result.set(a,4,p['olive']); result.set(a,27,p['olive'])
    result.set(4,a,p['olive']); result.set(27,a,p['olive'])
for a in [9,21]:
    for x,y in [(a,3),(a+1,2),(a+1,5),(a+2,6)]:
        for xx,yy in [(x,y),(31-x,31-y),(y,x),(31-y,31-x)]:
            result.set(xx,yy,p['leaf'])
# Four-petalled small carnations around the perimeter.
def flower(cx,cy):
    for dx,dy in [(-1,-2),(0,-2),(1,-1),(2,-1),(2,0),(1,1),(0,2),(-1,2),(-2,1),(-2,0)]:
        result.set(cx+dx,cy+dy,p['rust'])
    for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]: result.set(cx+dx,cy+dy,p['flax'])
    result.set(cx,cy,p['red'])
for cx,cy in [(4,4),(27,4),(4,27),(27,27),(15,4),(16,27),(4,16),(27,15)]: flower(cx,cy)
# Nested stepped diamond, with dark outlines between warm yarn bands.
for y in range(6,26):
    for x in range(6,26):
        d=abs(2*x-31)+abs(2*y-31)
        if d<=20:
            col=p['ink'] if d==20 else p['gold'] if d==18 else p['flax'] if d==16 else p['red'] if d>=10 else p['ink'] if d==8 else p['gold'] if d==6 else p['flax']
            if d in (10,12,14) and (min(x,31-x)+min(y,31-y))%3==0: col=p['rust']
            result.set(x,y,col)
# Central four-petal flower and tiny woven highlights.
for x,y in [(14,14),(17,14),(14,17),(17,17)]: result.set(x,y,p['light'])
result.rect(15,15,2,2,p['red'])
# Small corner sprigs in the field outside the medallion.
for x,y in [(8,9),(9,8),(9,10),(10,9)]:
    for xx,yy in [(x,y),(31-x,y),(x,31-y),(31-x,31-y)]: result.set(xx,yy,p['olive'])
for x,y in [(8,8),(23,8),(8,23),(23,23)]: result.set(x,y,p['gold'])
view(result,scale=12,margin=0)
repeat = new_canvas(96,96,name='repeat_check')
for j in range(3):
    for i in range(3): repeat.blit(result,32*i,32*j)
view(repeat,scale=5,margin=0)
save('warm_carpet',result)
finish(result)
