W,H=66,119
# palette
OL="#050100"; H1="#160701"; H2="#290e02"; H3="#421603"; H4="#5f1f04"; H5="#792806"
SK="#fdd5b7"; SK2="#eaa377"; SK3="#d28560"; LIP="#9e3e37"
EY="#50d4ec"; EYD="#5187b3"; EYW="#f2f8f9"; EYK="#293d4b"
DO="#545665"; D1="#a8b2c1"; D2="#767b90"; DW="#ffffff"; D3="#e0f4fa"
OUT="#281820"

def dress(c,d):
    # d: -1,0,+1 lateral shift of body volume
    # skirt
    for y in range(70,119):
        t=(y-70)/48.0
        half=int(15+17*t)
        cx=33+int(1.5*d*(1-t))
        c.line(cx-half,y,cx+half,y,D3)
    # bodice
    for y in range(47,71):
        t=(y-47)/24.0
        half=int(14+2*t)
        cx=33+2*d
        c.line(cx-half,y,cx+half,y,D3)
    # shading: light from viewer-left; shadow on side away from turn
    for y in range(47,119):
        if y<71:
            t=(y-47)/24.0; half=int(14+2*t); cx=33+2*d
        else:
            t=(y-70)/48.0; half=int(15+17*t); cx=33+int(1.5*d*(1-t))
        # left highlight band
        c.line(cx-half+1,y,cx-half+max(2,half//3),y,DW)
        # right shadow band
        c.line(cx+half-max(2,half//3),y,cx+half,y,D1)
        c.line(cx+half-1,y,cx+half,y,D2)
        c.set(cx-half,y,DO); c.set(cx+half,y,DO)
    # folds in skirt
    for fx in (-22,-10,2,14,24):
        for y in range(78,118):
            t=(y-70)/48.0
            x=33+int(fx*(0.55+0.9*t))+int(1.5*d*(1-t))
            if 0<=x<W: c.set(x,y,D1)
            if 0<=x+1<W: c.set(x+1,y,D2)
    # hem
    for y in (116,117,118):
        c.line(33-32,y,33+32,y,D2 if y==116 else D1)
    c.line(33-32,118,33+32,118,DO)
    # waist seam
    c.line(33+2*d-14,69,33+2*d+14,69,D2)
    c.line(33+2*d-14,70,33+2*d+14,70,DO)
    # collar / neckline
    c.rect(33+2*d-8,47,17,2,D1)

def sleeves(c,d):
    for s in (-1,1):
        ax=33+2*d+s*17
        c.rect(ax-2,58,5,26,SK2)
        c.rect(ax-2,58,3,26,SK)
        c.ellipse(ax,86,3,4,SK)
        c.ellipse(ax+s*1,86,2,3,SK2)
    for s in (-1,1):
        cx=33+2*d+s*15
        c.ellipse(cx,58,6,7,D3)
        c.ellipse(cx-2,56,3,4,DW if s<0 else D1)
        c.ellipse(cx,58,6,7,DO,fill=False)

def neck(c,d):
    c.rect(33+3*d-4,41,9,7,SK2)
    c.rect(33+3*d-4,41,5,7,SK)
    c.rect(33+3*d-5,41,1,7,OL); c.rect(33+3*d+5,41,1,7,OL)

def hairmass(c,cx,back=False):
    c.ellipse(cx,24,19,23,H2)
    c.ellipse(cx,24,19,23,H1,fill=False)
    # volume highlights
    c.ellipse(cx-8,14,8,7,H3)
    c.ellipse(cx-9,12,5,4,H4)
    c.ellipse(cx+9,16,7,7,H3)
    c.ellipse(cx+11,13,3,3,H4)
    # curl texture
    import random
    rnd=random.Random(7)
    for i in range(130):
        a=rnd.random()*6.2832; r=rnd.random()**0.5
        x=int(cx+r*18*__import__('math').cos(a)); y=int(24+r*22*__import__('math').sin(a))
        col=rnd.choice([H1,H3,H3,H4,H2,H5])
        c.set(x,y,col); c.set(x+1,y,col)

def face(c,d):
    fc=33+4*d
    c.ellipse(fc,27,11,13,SK)
    # cheek shading on far side (opposite turn)
    c.ellipse(fc-7*d,28,5,10,SK2)
    c.ellipse(fc,27,11,13,SK3,fill=False)
    # jaw/chin
    c.ellipse(fc,34,7,5,SK)
    # eyes
    for k,ex in ((1,fc+7*d),(0,fc-2*d)):
        w=3 if k else 2
        c.rect(ex-w,26,2*w+1,4,EYW)
        c.rect(ex-w+1,27,2*w-1,3,EY)
        c.rect(ex-w+1,28,2*w-1,2,EYD)
        c.set(ex-w+1,27,EYW)
        c.rect(ex-w,25,2*w+1,1,H1)
        c.rect(ex-w,30,2*w+1,1,SK3)
        # brow
        c.rect(ex-w,22,2*w+1,2,H2)
    # nose
    c.set(fc+4*d,32,SK3); c.set(fc+4*d+d,31,SK3); c.set(fc+3*d,33,SK2)
    # mouth
    c.line(fc+1*d-2,36,fc+1*d+2,36,LIP)
    c.set(fc+1*d-2,36,SK3); c.set(fc+1*d+2,36,SK3)
    # fringe over forehead
    c.ellipse(fc-2*d,15,12,6,H2)
    c.ellipse(fc-6*d,13,6,4,H3)
    c.ellipse(fc+6*d,14,5,3,H3)
    for i in range(-12,13,2):
        c.line(fc+i,11,fc+i+ (3 if i<0 else -3),19,H1)
    # ear on far side
    ex=fc-10*d
    c.ellipse(ex,28,2,3,SK2); c.ellipse(ex,28,2,3,SK3,fill=False)

def braid(c,bx,top=25,bot=62,wid=5):
    y=top
    i=0
    while y<bot:
        x=bx+int(2*__import__('math').sin((y-top)/5.0))
        c.ellipse(x,y,wid-(y-top)//18,3,H2)
        c.ellipse(x-1,y-1,2,1,H3 if i%2 else H4)
        c.ellipse(x,y,wid-(y-top)//18,3,H1,fill=False)
        y+=5; i+=1
    c.ellipse(bx,bot+2,2,3,H1)

def make(view):
    c=new_canvas(W,H,name="f_"+view)
    d={'left':1,'right':-1,'back':0}[view]
    dress(c,d); sleeves(c,d); neck(c,d)
    if view=='back':
        hairmass(c,33)
        # long hair down the back, narrower so dress/shoulders read
        c.ellipse(33,44,13,12,H2)
        c.ellipse(27,42,5,7,H3); c.ellipse(39,42,4,6,H3)
        c.ellipse(33,44,13,12,H1,fill=False)
        braid(c,33,top=48,bot=74,wid=4)
    else:
        hairmass(c,33+2*d)
        face(c,d)
        # hair falling on the back side (opposite of facing dir)
        bsx=33-13*d
        c.ellipse(bsx,38,8,14,H2)
        c.ellipse(bsx-2,34,4,7,H3)
        c.ellipse(bsx,38,8,14,H1,fill=False)
        braid(c,33-16*d,top=30,bot=66,wid=5)
    c.outline(OUT)
    return c

f1=make('left'); f2=make('right'); f3=make('back')
view(f1); view(f2); view(f3)
finish([f1,f2,f3])
