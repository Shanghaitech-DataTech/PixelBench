result = new_canvas(32, 32, background='#71332e', name='carpet')
# A small woven palette: oxblood, clay, saffron, flax and muted sage.
bg=['#71332e','#7c3b31']
ink='#472c2a'
rust='#ac5339'
gold='#d39a50'
cream='#efcf8b'
sage='#7d8760'
# Thread alternation is periodic and mirrored on the outermost warp threads.
for y in range(32):
    for x in range(32):
        u=min(x,31-x); v=min(y,31-y)
        result.set(x,y,bg[(u+v)%2])
# Diamond medallion centred between threads; stepped outlines read as weaving.
for y in range(5,27):
    for x in range(5,27):
        d=abs(x-15.5)+abs(y-15.5)
        if d<=11:
            if d>9: c=ink
            elif d>8: c=gold
            elif d>7: c=cream
            elif d>6: c=rust
            else: c=ink if (x+y)%2==0 else '#52332c'
            result.set(x,y,c)
# Eight-point floral diamond at its heart.
for y in range(11,21):
    for x in range(11,21):
        a=abs(x-15.5); b=abs(y-15.5)
        if a+b<=4 and (a<=1.5 or b<=1.5):
            result.set(x,y,gold if (x+y)%2 else cream)
result.rect(15,15,2,2,rust)
# Continuous floral border: split flowers lie on tile boundaries.
def dot(x,y,c): result.set(x%32,y%32,c)
# Double-thread lattice joins opposite edges exactly.
for t in range(32):
    for n in [0,31]:
        dot(t,n,ink); dot(n,t,ink)
    for n in [2,29]:
        dot(t,n,gold if t%4 in (0,3) else rust)
        dot(n,t,gold if t%4 in (0,3) else rust)
# Flowers at the midpoints of all border bands, repeated toroidally.
def flower(cx,cy):
    for dy in range(-4,5):
        for dx in range(-4,5):
            a=abs(dx); b=abs(dy)
            if (a+b<=4 and (a<=1 or b<=1)):
                dot(cx+dx,cy+dy,ink)
    for dx,dy in [(0,-3),(0,-2),(0,2),(0,3),(-3,0),(-2,0),(2,0),(3,0)]:
        dot(cx+dx,cy+dy,cream if abs(dx+dy)==3 else gold)
    for dx,dy in [(-1,-1),(1,-1),(-1,1),(1,1)]: dot(cx+dx,cy+dy,rust)
    dot(cx,cy,cream)
# Place flowers inside frame so the outside rows remain identical.
for cx,cy in [(15,3),(16,28),(3,16),(28,15)]: flower(cx,cy)
# Paired leaves and corner rosettes.
for x,y in [(7,4),(23,4),(8,27),(24,27),(4,8),(4,24),(27,7),(27,23)]:
    dot(x,y,sage); dot(x+1,y, gold); dot(x,y+1,sage)
for cx,cy in [(5,5),(26,5),(5,26),(26,26)]:
    dot(cx,cy,cream)
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]: dot(cx+dx,cy+dy,rust)
# Matching edge threads, including corner crossings.
for i in range(32):
    result.set(i,31,result.get(i,0))
    result.set(31,i,result.get(0,i))
view(result,scale=12,margin=0)
repeat=new_canvas(96,96,name='tiling-check')
for y in range(3):
    for x in range(3): repeat.blit(result,x*32,y*32)
view(repeat,scale=5,margin=0)
finish(result)
