import math
result = new_canvas(48,48, name='teleport_portal_two_frames')
# Two 24x48 animation cells, kept on the required single 48x48 sheet.
core = ['#24103f','#381159','#4e187b','#652399','#8032bd','#a64ce2','#c879fa','#ebacff','#ffe3ff']
for frame,cx in enumerate((11.5,35.5)):
    cy=24
    rot=frame*0.82
    for y in range(3,46):
        for x in range(frame*24,(frame+1)*24):
            dx=(x-cx)/9.0
            dy=(y-cy)/16.0
            r=math.hypot(dx,dy)
            a=math.atan2(dy,dx)
            # Outer aura is made of discrete, intentionally stepped rings.
            if frame==1 and 1.12<r<1.29:
                result.set(x,y,'#422064' if r>1.23 else '#753399')
            if frame==1 and 1.13<r<1.19:
                result.set(x,y,'#cf80f5')
            if frame==0 and 1.02<r<1.14 and math.sin(3*a+0.8)>-0.25:
                result.set(x,y,'#452168')
            if r<=1.035:
                # Three sweeping arms wind into a dark central eye.
                phase=3*a-9*r+rot
                wave=(math.cos(phase)+1)/2
                idx=int(1+wave**3*5)
                if r<0.24:
                    idx=0 if r<0.13 else min(idx,3)
                if r>0.89:
                    rim=(math.sin(a*3+rot)+1)/2
                    idx=4+int(rim*3)
                if 0.77<r<0.88 and wave>0.82:
                    idx=7
                result.set(x,y,core[min(8,idx)])
    # Disconnected motes continue the orbital movement.
    dots=([(4,9),(17,6),(21,16),(2,32),(17,42),(7,44)] if frame==0 else [(5,5),(18,9),(1,19),(21,31),(17,43),(5,41)])
    for j,(xx,yy) in enumerate(dots):
        xx+=frame*24
        result.set(xx,yy,'#bb6ce6' if j%2 else '#713a9d')
    # Small hard-edged flares articulate the rim.
    for xx,yy in ([(5,13),(17,34)] if frame==0 else [(17,13),(5,35)]):
        xx+=frame*24
        result.line(xx-1,yy,xx+1,yy,'#e7b2ff')
        result.line(xx,yy-1,xx,yy+1,'#e7b2ff')
        result.set(xx,yy,'#fff1ff')
view(result,scale=8,margin=0)
save('teleport-portal',result)
finish(result)
