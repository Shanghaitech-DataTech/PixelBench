import random
random.seed(7)
out = input_canvas.copy(name='output')
C = out

def rgb_to_hsv(r,g,b):
    r,g,b = r/255.,g/255.,b/255.
    mx=max(r,g,b); mn=min(r,g,b); d=mx-mn
    v=mx
    if d==0: h=0; s=0
    else:
        s=d/mx
        if mx==r: h=60*(((g-b)/d)%6)
        elif mx==g: h=60*((b-r)/d+2)
        else: h=60*((r-g)/d+4)
    return h,s,v
def hsv_to_rgb(h,s,v):
    c=v*s; x=c*(1-abs((h/60)%2-1)); m=v-c
    if h<60: r,g,b=c,x,0
    elif h<120: r,g,b=x,c,0
    elif h<180: r,g,b=0,c,x
    elif h<240: r,g,b=0,x,c
    elif h<300: r,g,b=x,0,c
    else: r,g,b=c,0,x
    return int(round((r+m)*255)),int(round((g+m)*255)),int(round((b+m)*255))

pal=C.palette()
byid={p['index']:p['rgba'] for p in pal}
# demonic mapping: blood-red hue, keep luminance structure
mapping={}
CRIMSON=(200,20,28)
for i,rgba in byid.items():
    r,g,b,a=rgba
    if a==0:
        mapping[i]=C.color((0,0,0,0)); continue
    h,s,v = rgb_to_hsv(r,g,b)
    # blood red theme
    nh=352
    # darken: scale value based on original lightness so buildings stay readable
    ns=min(1.0, max(0.55, s*1.15))
    nv=v*0.72
    nr,nb,ng = hsv_to_rgb(nh,ns,nv)
    # keep pure black as near-black
    if v<0.10:
        nr,nb,ng = int(r*0.5),0,0
    mapping[i]=C.color((nr,nb,ng,a))

for y in range(128):
    for x in range(256):
        C.set(x,y,mapping[C.get(x,y)])

# Blood red palette entries
BLACK=C.color((10,2,3))
MOON=C.color((216,22,28))
MOON_HI=C.color((255,70,66))
MOON_DK=C.color((150,10,16))
MOON_PALE=C.color((255,140,120))
GLOW1=C.color((90,8,12,90))
GLOW2=C.color((150,14,20,60))
GLOW3=C.color((200,22,30,30))
WIND=C.color((255,90,40))
WIND2=C.color((240,40,24))
CAP=C.color((120,18,20))

# ---- Blood moon with glow ----
cx,cy,cr=132,30,24
for r,g in [(40,GLOW1),(34,GLOW2),(29,GLOW3)]:
    C.circle(cx,cy,r,g,fill=True)
# moon disc with subtle shading
C.circle(cx,cy,cr,MOON,fill=True)
# dark maria patches
C.circle(cx-6,cy-4,5,MOON_DK)
C.circle(cx+7,cy+6,4,MOON_DK)
C.circle(cx+2,cy-9,3,MOON_DK)
C.circle(cx-8,cy+8,3,MOON_DK)
C.circle(cx+9,cy-2,2,MOON_DK)
# bright rim highlight (upper-left)
C.circle(cx-9,cy-7,2,MOON_HI)
C.circle(cx-13,cy-3,2,MOON_HI)
C.circle(cx-10,cy+3,2,MOON_HI)
C.circle(cx-5,cy-11,2,MOON_HI)
C.circle(cx-16,cy-8,2,MOON_PALE)
C.set(cx-16,cy-9,MOON_PALE); C.set(cx-15,cy-9,MOON_PALE)
C.set(cx-15,cy-10,MOON_PALE)

# ---- Demon castle spires (jagged silhouettes over sky) ----
def spire(poly):
    C.poly(poly,BLACK,fill=True)

# Central main keep - tall jagged spikes puncturing the moon
spire([(114,58),(118,40),(122,28),(123,16),(126,8),(129,4),(132,9),(134,18),(136,30),(140,24),(143,10),(147,6),(150,14),(152,28),(157,18),(160,9),(164,15),(167,34),(171,52),(168,58),(160,54),(155,57),(146,52),(138,56),(128,52),(120,57),(114,58)])
# cross-bar / barb on left spike
C.poly([(122,16),(116,13),(120,11),(122,12),(123,8),(125,12),(127,10),(130,14),(128,16),(127,14),(124,17),(122,16)],BLACK)
# small window lights on main keep
for wx,wy in [(118,44),(130,24),(146,26),(152,20),(160,34)]:
    for oy in range(2):
        for ox in range(2):
            C.set(wx+ox,wy+oy,WIND)

# Left tall tower spires
spire([(2,60),(6,46),(12,34),(17,24),(20,12),(23,6),(26,12),(28,24),(33,18),(36,8),(40,16),(43,32),(46,48),(44,56),(38,50),(30,55),(22,50),(14,56),(8,52),(2,60)])
C.poly([(20,12),(16,9),(20,8),(21,5),(23,8),(26,7),(28,11),(25,12),(23,10),(20,13),(20,12)],BLACK)
for wx,wy in [(28,26),(36,20),(16,26),(6,44)]:
    for oy in range(2):
        for ox in range(2): C.set(wx+ox,wy+oy,WIND)

# Right cluster spires
spire([(196,62),(202,44),(205,28),(208,16),(211,8),(214,16),(216,26),(220,12),(224,6),(227,14),(229,28),(234,20),(237,10),(241,16),(244,30),(248,20),(251,12),(255,22),(255,60),(250,52),(242,58),(234,50),(226,56),(218,50),(210,56),(202,60),(196,62)])
for wx,wy in [(211,20),(224,28),(237,22),(244,32)]:
    for oy in range(2):
        for ox in range(2): C.set(wx+ox,wy+oy,WIND2)

# Crenellated battlement caps along a mid building line
for bx in range(30,120,6):
    C.set(bx,63,CAP); C.set(bx+2,63,CAP)
for bx in range(172,196,6):
    C.set(bx,64,CAP); C.set(bx+2,64,CAP)

# ---- scattered glowing demon windows on buildings ----
spots=[(10,76),(14,74),(22,70),(38,72),(50,80),(64,84),(78,82),(86,76),
       (102,80),(108,84),(150,58),(158,60),(166,64),(180,86),(186,90),
       (206,76),(214,78),(228,70),(236,66),(244,60),(252,58)]
for wx,wy in spots:
    C.set(wx,wy,WIND); C.set(wx+1,wy,WIND); C.set(wx,wy+1,WIND2); C.set(wx+1,wy+1,WIND)

print(C.stats_text())
finish(C)
# verify moon and keep pixels
for (x,y) in [(132,30),(132,10),(150,26),(120,30),(130,24),(118,44),(211,20),(224,6),(20,20)]:
    print((x,y), C.color_name(C.get(x,y)), end='  ')
print()
print(C.matrix_text(region=(112,4,172,40)))
