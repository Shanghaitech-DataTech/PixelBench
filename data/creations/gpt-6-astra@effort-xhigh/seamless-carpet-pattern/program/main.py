# A 32-pixel carpet repeat, drawn at its native resolution.
result = new_canvas(32, 32, background='#4b292b', name='ember_carpet')

P = {
 'ground': '#512c2e', 'ink': '#342127', 'wine': '#753632',
 'rust': '#ad5136', 'terra': '#cc7448', 'gold': '#cc9750',
 'cream': '#edc884', 'light': '#ffe0a0', 'olive': '#777044',
 'leaf': '#a59a58'
}
# A restrained, mirrored warp/weft texture. Mirroring also gives identical
# opposite edge pixels, including their yarn highlights.
def yarn(base, x, y):
    rgb = tuple(int(base[i:i+2],16) for i in (1,3,5))
    u, v = min(x,31-x), min(y,31-y)
    delta = 3 if (u+v)%2 == 0 else -3
    return tuple(max(0,min(255,k+delta)) for k in rgb)

for y in range(32):
    for x in range(32):
        result.set(x,y,yarn(P['ground'],x,y))

# Vines are laid into the surrounding field, with four small woven rosettes.
# Work one corner and reflect every stitch in both axes.
def stitch(x,y,key):
    for xx,yy in {(x,y),(31-x,y),(x,31-y),(31-x,31-y)}:
        result.set(xx,yy,yarn(P[key],xx,yy))

# Continuous floral edging: each border joins the next tile's border.
for t in range(16):
    stitch(t,1,'ink')
    stitch(1,t,'ink')
    stitch(t,2,'gold')
    stitch(2,t,'gold')
for t in (0,4,8,12):
    stitch(t,2,'wine')
    stitch(2,t,'wine')
# Vines break into leaves along the inner edge.
for x,y in [(3,3),(4,4),(8,4),(9,3),(10,3),(12,3),
            (3,9),(3,10),(4,8),(3,12)]:
    stitch(x,y,'olive')
for x,y in [(4,3),(9,4),(12,2),(3,4),(4,9),(2,12)]:
    stitch(x,y,'leaf')
# A four-petal flower, silhouetted in garnet, highlighted in flax and ochre.
flower = [
 '..rccr..',
 '..cllc..',
 'rcwggwcr',
 'clgssglc',
 'clgssglc',
 'rcwggwcr',
 '..cllc..',
 '..rccr..'
]
keys={'r':'wine','c':'terra','l':'cream','g':'rust','w':'wine','s':'gold'}
for j,row in enumerate(flower):
    for i,ch in enumerate(row):
        if ch!='.': stitch(i+3,j+3,keys[ch])
# Seed-shaped border ornaments at the middle of each edge.
for x,y in [(14,0),(15,0),(13,1),(14,1),(15,1),(14,2),(15,2)]:
    stitch(x,y,'rust')
    stitch(y,x,'rust')
for x,y in [(14,0),(15,1)]:
    stitch(x,y,'cream')
    stitch(y,x,'cream')

# Stepped diamond medallion: dark keyline, flax outline, a gold inner braid.
for y in range(32):
    for x in range(32):
        d=abs(x-15.5)+abs(y-15.5)
        if d <= 13:
            if d==13: key='ink'
            elif d==12: key='gold'
            elif d==11: key='cream'
            elif d==10: key='wine'
            elif d==9: key='terra'
            else: key='rust'
            result.set(x,y,yarn(P[key],x,y))
# Dark sawtooth points emphasize the traditional geometric repeat.
for x,y in [(10,10),(12,8),(8,12)]:
    stitch(x,y,'ink')
    stitch(x+1,y+1,'gold')
# Central eight-point, petal-like geometric jewel.
for y in range(11,21):
    for x in range(11,21):
        dx,dy=abs(x-15.5),abs(y-15.5)
        d=dx+dy
        if d<=5:
            key='cream' if d==5 else 'gold'
            if d<=3: key='wine'
            if d<=1: key='light'
            result.set(x,y,yarn(P[key],x,y))
# Four isolated flax stitches in the red medallion field.
for x,y in [(15,9),(9,15)]:
    stitch(x,y,'cream')

# Inspect both the exact tile and its seamless 3x3 repeat.
repeat = new_canvas(96,96,name='repeat_preview')
for j in range(3):
    for i in range(3): repeat.blit(result,32*i,32*j)
view(result,scale=12,margin=0)
view(repeat,scale=5,margin=0)
assert all(result.get(0,i)==result.get(31,i) for i in range(32))
assert all(result.get(i,0)==result.get(i,31) for i in range(32))
assert result.stats()['colors_used'] <= 86
save('ember_carpet',result)
finish(result)
