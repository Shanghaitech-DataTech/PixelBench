import math
W,H=47,43
ox,oy=4,6
f1=new_canvas(W,H,name='01_original')
f1.blit(input_canvas,ox,oy)
ink='#141b1b'; gold='#ffe18d'; green='#adbc3a'; shade='#74a334'; lip='#c8966b'; white='#fce2ca'
body=input_canvas.copy(name='recoil_parts')
# Separate legs from the belly and dangling hands.
for y in range(26,33):
    for x in range(37):
        keep=(y<=28 and (x<=4 or x>=32)) or (y==26 and 11<=x<=25) or (y==27 and 12<=x<=24) or (y==28 and 14<=x<=22) or (y==29 and 16<=x<=20)
        if not keep: body.set(x,y,None)
# Roll the eye upward; retain the original flesh-coloured socket.
body.rect(17,16,3,3,white)
body.rect(17,15,3,2,ink)
body.set(16,16,ink)
body.set(20,16,ink)
# Gaping mouth with a shaded lower lip, upper fangs and tongue.
body.poly([(15,22),(21,22),(23,24),(22,27),(20,28),(16,28),(14,26),(14,24)],shade)
body.poly([(16,22),(20,22),(22,24),(21,26),(19,27),(16,26),(15,24)],ink)
body.line(17,22,19,22,lip)
body.set(16,23,white)
body.set(20,23,white)
body.line(17,26,20,26,lip)
body.line(18,25,20,25,'#a65552')
# Legs drawn behind the tilted torso; the right-side foot stays planted.
f2=new_canvas(W,H,name='02_recoil')
def poly(points,col): f2.poly([(x+ox,y+oy) for x,y in points],col)
def line(x0,y0,x1,y1,col): f2.line(x0+ox,y0+oy,x1+ox,y1+oy,col)
# Hip connections follow the rotated belly into each leg.
poly([(12,21),(17,22),(16,25),(13,27),(10,26)],ink)
poly([(13,22),(16,23),(14,25),(12,26),(11,25)],shade)
poly([(21,23),(25,23),(28,27),(26,29),(22,27),(20,25)],ink)
poly([(22,24),(25,24),(27,27),(26,28),(23,26),(21,25)],shade)
# Planted leg, knee pushed right by the recoil.
poly([(24,25),(28,26),(30,29),(30,31),(32,32),(32,33),(27,33),(27,31),(25,29),(22,28)],ink)
poly([(25,26),(27,27),(29,29),(29,31),(31,32),(28,32),(28,30),(26,29),(24,28)],shade)
line(28,32,29,32,gold)
# Raised right leg bends left, leaving a clear gap below the foot.
poly([(10,23),(14,24),(15,27),(12,29),(8,29),(5,27),(5,25),(8,25),(10,26)],ink)
poly([(10,24),(13,25),(13,27),(11,28),(8,28),(6,26),(8,26),(10,27),(11,26)],shade)
line(6,26,7,27,gold)
f2.set(8+ox,27+oy,green)
# Nearest-pixel rigid tilt around the planted hip.
a=math.radians(13); co=math.cos(a); si=math.sin(a)
for Y in range(H):
    for X in range(W):
        u=X-ox-26; v=Y-oy-28+2
        sx=round(co*u+si*v+26); sy=round(-si*u+co*v+28)
        if 0<=sx<37 and 0<=sy<33:
            idx=body.get(sx,sy)
            rgba=body.palette()[idx]['rgba']
            if rgba[3]: f2.set(X,Y,idx)
# Impact uses a whole-sprite red colour filter, preserving transparency.
f3=new_canvas(W,H,name='03_impact')
pal=f2.palette()
for y in range(H):
    for x in range(W):
        rgba=pal[f2.get(x,y)]['rgba']
        r,g,b,alpha=rgba
        if alpha:
            f3.set(x,y,(round(r*.52+255*.48),round(g*.45),round(b*.45),alpha))
view(f1,scale=10)
view(f2,scale=10)
view(f3,scale=10)
finish([f1,f2,f3])
