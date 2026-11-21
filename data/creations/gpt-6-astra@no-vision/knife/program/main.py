# The supplied knife is mirrored before rotation: its bright cutting bevel
# must be below the spine in the final horizontal pose.
print(input_canvas.stats_text())
turned=input_canvas.select(0,0,93,128).flip('h').rotate(56,algorithm='rotsprite').preview()
knife=new_canvas(154,32,name='posed_knife')
turned.select(3,61,154,32).copy_to(0,0,knife)

# Restore a clean single-pixel blade contour after the oblique rotation.
# The original metal, bevel, and handle texture are retained inside it.
blade=new_canvas(154,32,name='blade_mask')
points=[(61,8),(72,8),(112,10),(131,11),(135,14),(153,14),
        (151,18),(147,22),(141,26),(132,29),(121,31),(99,31),
        (85,30),(73,29),(69,26),(65,22),(61,21)]
blade.poly(points,'#ffffff').poly(points,'#ffffff',fill=False)
original=knife.copy(name='unpolished_pose')
knife.clear(61,0,93,32)
outline='#26181e'
for y in range(32):
    for x in range(61,154):
        if blade.get(x,y)==0:
            continue
        # A silhouette pixel receives either a clean contour or source steel.
        edge=any(nx<61 or nx>=154 or ny<0 or ny>=32 or blade.get(nx,ny)==0
                 for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
        if edge:
            knife.set(x,y,outline)
        else:
            p=original.get(x,y)
            if p==0 or original.color_name(p)==outline or p==original.color('#26181e'):
                knife.set(x,y,'#ccd3f8' if y>=23 else '#a4add9')
            else:
                knife.set(x,y,p)
# Join the blade to the original guard.
knife.line(61,9,61,20,'#959fd5')

# Independent RGBA copies make the two previous positions truly translucent.
def echo(sprite,alpha,tint):
    e=new_canvas(154,32,name='afterimage')
    pal={p['index']:p['rgba'] for p in sprite.palette()}
    for yy in range(32):
        for xx in range(154):
            idx=sprite.get(xx,yy)
            r,g,b,a=pal[idx]
            if a:
                rgb=tuple(round(v*(1-tint)+t*tint) for v,t in zip((r,g,b),(151,177,231)))
                e.set(xx,yy,(*rgb,round(a*alpha)))
    return e

fx=new_canvas(256,104,name='white_thrust_effect')
# The slash is tapered and asymmetrical, wrapping under the knife and
# converging on a point just in front of it rather than obscuring the blade.
import math
# Two nonintersecting boundaries keep the crescent continuous at pixel scale.
def ribbon(halfwidth,col):
    upper=[]
    lower=[]
    for i in range(65):
        t=i/64
        x=(1-t)**2*16 + 2*(1-t)*t*151 + t*t*251
        y=(1-t)**2*81 + 2*(1-t)*t*119 + t*t*56
        width=halfwidth*(math.sin(math.pi*t)**0.8)
        upper.append((round(x),round(y-width)))
        lower.append((round(x),round(y+width)))
    fx.poly(upper+lower[::-1],col)
ribbon(6.5,'#dceaff33')
ribbon(4.0,'#edf5ff90')
ribbon(2.3,'#ffffff')
# Straight, sharp thrust core and a few trailing wind strands.
fx.poly([(151,57),(239,54),(254,56),(235,59)],'#eaf3ff66')
fx.poly([(173,57),(242,55),(254,56),(238,57)],'#ffffff')
fx.line(6,69,39,69,'#ffffff66')
fx.line(20,72,51,72,'#ffffffaa')
fx.line(47,13,83,13,'#e6eeff66')
fx.line(69,16,119,16,'#ffffff99')
fx.line(120,28,162,28,'#ffffff66')

far=echo(knife,0.18,0.50)
near=echo(knife,0.37,0.25)
echoes=new_canvas(256,104,name='translucent_prior_positions')
echoes.blit(far,9,20).blit(near,44,31)
hero=new_canvas(256,104,name='knife_thrusting_right')
hero.blit(knife,80,43)
result=flatten([fx,echoes,hero],name='result')
# A compact white flare extends the thrust without hiding the original tip.
result.poly([(232,57),(239,55),(251,56),(240,58)],'#ffffff')
result.line(239,52,239,59,'#ffffffbb')
# Give the forward point and lower arc breathing room on every side.
padded=new_canvas(272,120,name='rightward_knife_thrust')
padded.blit(result,8,8)
result=padded
print(result.stats_text())
# Text-only overview by category: translucent echoes, white arc, and solid knife.
pal={p['index']:p['rgba'] for p in result.palette()}
for yy in range(0,104,2):
    row=''
    for xx in range(0,256,2):
        rgba=pal[result.get(xx,yy)]
        r,g,b,a=rgba
        if a==0: char=' '
        elif a<75: char='·'
        elif a<150: char=':'
        elif r>235 and g>235: char='*'
        elif a<255: char='+'
        elif r<65: char='#'
        else: char='K'
        row+=char
    print(row.rstrip())
print(result.matrix_text(region=(75,40,143,72)))
save('knife_thrust_right',result)
finish(result)
