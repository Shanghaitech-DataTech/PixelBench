import math
result = new_canvas(48,48, name='teleport_portal_two_frames')
# Two 24-pixel-wide animation cells, with a transparent gutter.
ink='#27153f'
deep='#341953'
shadow='#4b206f'
purple='#6b2da3'
mid='#8843c5'
light='#b36bea'
bright='#d99aff'
white='#f9dcff'
cool='#c4baff'

def portal(cx,cy,phase,halo=False):
    # Detached, broken orbit in the energized second pose.
    if halo:
        for y in range(5,43):
            for x in range(cx-11,cx+12):
                dx=(x-cx)/10.6; dy=(y-cy)/17.2
                r=math.hypot(dx,dy); a=math.atan2(dy,dx)
                if .95<r<1.055 and math.sin(a*4+phase)>-.45:
                    result.set(x,y,light if math.sin(a*4+phase)>.35 else purple)
                if 1.065<r<1.13 and math.sin(a*7+phase)>.92:
                    result.set(x,y,shadow)
    # Solid violet funnel. Three curved arms spiral into its bright throat.
    for y in range(cy-15,cy+16):
        for x in range(cx-9,cx+10):
            dx=(x-cx)/9.0; dy=(y-cy)/14.5
            r=math.hypot(dx,dy); a=math.atan2(dy,dx)
            edge=1+.035*math.sin(a*5+phase)
            if r>edge: continue
            spiral=(a*3+9*r-phase)%(2*math.pi)
            band=math.sin(spiral)
            col=deep
            if band>-.45: col=shadow
            if band>.05: col=purple
            if band>.48: col=mid
            if band>.78: col=light
            if band>.95: col=bright
            # Dark cut at the trailing edge creates depth between the arms.
            if -.90<band<-.60: col=ink
            if r>.87:
                rim=math.sin(a*3-phase+1)
                col=purple if rim<-.25 else light if rim<.6 else bright
            if r>.97: col=shadow if math.sin(a*3-phase)<0 else mid
            if r<.17: col=white
            elif r<.27: col=bright if band>0 else mid
            result.set(x,y,col)
    # Selective bright contour pixels, never a continuous white outline.
    for ang in [phase*.45+.25,phase*.45+2.5,phase*.45+4.55]:
        for t in range(4):
            a=ang+t*.085
            x=round(cx+8.25*math.cos(a)); y=round(cy+13.3*math.sin(a))
            result.set(x,y,white if t<2 else bright)

portal(11,24,0,False)
portal(36,24,1.6,True)
# Floating motes and asymmetric glints make the energized pose read at 1x.
for x,y,col in [(6,6,mid),(7,5,light),(17,9,bright),(2,20,mid),(20,33,mid),(5,40,light),(15,42,purple),(29,8,light),(43,6,bright),(46,18,light),(27,38,mid),(40,43,light),(44,39,bright)]:
    result.set(x,y,col)
# Small four-point sparkle above the active portal.
result.set(36,3,light).line(35,4,37,4,bright).set(36,4,white).set(36,5,light)
view(result,scale=8,margin=0)
save('teleport_portal',result)
finish(result)
