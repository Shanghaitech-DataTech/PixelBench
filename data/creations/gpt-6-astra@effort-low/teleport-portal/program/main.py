import math
result = new_canvas(48,48)
# Two animation states on a single transparent sprite sheet.
for frame,cx in enumerate((11,36)):
    cy=24
    if frame:
        result.ellipse(cx,cy,10,17,'#38205c',False)
        result.ellipse(cx,cy,9,16,'#8850ce',False)
        result.ellipse(cx,cy,8,15,'#e1a5ff',False)
        result.ellipse(cx,cy,7,14,'#fff0ff',False)
    else:
        result.ellipse(cx,cy,9,15,'#44206b',False)
        result.ellipse(cx,cy,8,14,'#9850da',False)
    # Elliptical void and spiraling energy ribbons, quantized at native resolution.
    for y in range(cy-13,cy+14):
        for x in range(cx-7,cx+8):
            u=(x-cx)/7.5; v=(y-cy)/13.5
            r=math.sqrt(u*u+v*v)
            if r>1: continue
            a=math.atan2(v,u)
            phase=(a+7*r-frame*1.1)%(math.pi*2)
            col='#190e34'
            if r>.83: col='#59248c'
            if phase<1.25 or 3.14<phase<4.39: col='#53218a'
            if phase<.74 or 3.14<phase<3.88: col='#883bd0'
            if phase<.33 or 3.14<phase<3.47: col='#c377f5'
            if (phase<.13 or 3.14<phase<3.27) and r>.38: col='#f0baff'
            if r<.18: col='#100c27'
            result.set(x,y,col)
    # Broken bright rim accents emphasize the orbital motion.
    result.line(cx-7,cy-8,cx-5,cy-12,'#e5a3ff')
    result.line(cx-5,cy-12,cx-2,cy-14,'#fce1ff')
    result.line(cx+7,cy+6,cx+6,cy+10,'#cc7fff')
    result.line(cx+6,cy+10,cx+3,cy+13,'#f5c7ff')
    # Sparse free energy sparks.
    for dx,dy in [(-8,-17),(5,-18),(9,11),(-5,17)]:
        if 0<=cx+dx<48: result.set(cx+dx,cy+dy,'#b66bf0')
    sx=cx+4; sy=cy-17 if frame else cy+16
    result.line(sx-1,sy,sx+1,sy,'#e8b7ff')
    result.line(sx,sy-2,sx,sy+2,'#e8b7ff')
    result.set(sx,sy,'#ffffff')
view(result)
finish(result)
