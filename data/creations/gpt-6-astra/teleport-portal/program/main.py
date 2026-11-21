import math
result = new_canvas(48,48,name='teleport_portal_two_frames')
# Two animation cels share the required single, transparent 48 x 48 sheet.
ink='#211238'; deep='#32134f'; shadow='#49166c'; plum='#641b92'
purple='#8129bd'; violet='#a13fe3'; lilac='#c46bfa'; pink='#e5a2ff'; light='#ffe0ff'
for frame,cx in enumerate((11,36)):
    cy=24
    phase=frame*1.05
    # A stepped luminous halo appears on the second cel.
    if frame:
        for y in range(4,45):
            for x in range(25,48):
                dx=(x-cx)/10.5; dy=(y-cy)/18.5
                r=math.hypot(dx,dy); a=math.atan2(dy,dx)
                if .94<r<1.065:
                    col=lilac if math.sin(a*3+.5)>.65 else violet if math.sin(a*3+.5)>.0 else purple
                    result.set(x,y,col)
                elif .86<r<=.94:
                    result.set(x,y,deep)
    # Solid bevel contains the energy and gives the silhouette a crisp pixel edge.
    for y in range(8,41):
        for x in range(cx-10,cx+11):
            if not (0<=x<48): continue
            dx=(x-cx)/8.4; dy=(y-cy)/15.2
            r=math.hypot(dx,dy); a=math.atan2(dy,dx)
            if r<=1.045:
                if r>.95: col=ink
                elif r>.83:
                    t=math.sin(a+phase-.6)
                    col=lilac if t<-.65 else violet if t<.15 else purple
                else:
                    # Three swept arms spiral into a deep central aperture.
                    swirl=(a+phase-3.4*r)*3
                    wave=(math.sin(swirl)+1)/2
                    if r<.16: col=ink
                    elif r<.24: col=deep if wave<.72 else plum
                    elif wave>.94: col=pink if r>.4 else violet
                    elif wave>.8: col=lilac
                    elif wave>.60: col=violet
                    elif wave>.36: col=purple
                    elif wave>.18: col=plum
                    else: col=shadow
                result.set(x,y,col)
    # Split glints on the rim: highlights stay chunky rather than anti-aliased.
    for a0,a1,col in ((3.7,4.65,light),(4.65,5.1,pink),(.65,1.35,lilac)):
        prev=None
        for i in range(24):
            a=a0+(a1-a0)*i/23+phase*.2
            p=(round(cx+7.6*math.cos(a)),round(cy+14.2*math.sin(a)))
            if prev: result.line(*prev,*p,col)
            prev=p
# Loose motes and diamond glints, on the transparent background.
def spark(x,y,col):
    result.line(x-1,y,x+1,y,col)
    result.line(x,y-2,x,y+2,col)
    result.set(x,y,light)
spark(5,8,lilac)
result.set(17,5,purple)
result.rect(18,13,2,2,violet)
result.set(2,33,purple)
result.rect(14,42,2,2,violet)
spark(39,3,pink)
spark(28,37,lilac)
result.set(45,11,lilac)
result.set(31,6,purple)
result.set(42,43,violet)
result.set(33,45,lilac)
view(result,scale=8,margin=0)
save('teleport_portal',result)
finish(result)
