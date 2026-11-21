import math

P = {
 'ink':'#201038', 'void':'#291346', 'deep':'#3e1c67',
 'shade':'#55258a', 'purple':'#7232b1', 'violet':'#9345d2',
 'bright':'#b75eee', 'pink':'#da85fa', 'pale':'#efb1ff',
 'white':'#fff0ff', 'blue':'#6b59c9', 'periwinkle':'#a394f4',
 'halo_dark':'#45236e', 'halo_mid':'#8751bb', 'halo_light':'#c994ed'
}
TAU=math.pi*2
cx,cy=23.5,23.5

def dot(c,x,y,col):
    if 0<=x<48 and 0<=y<48:c.set(x,y,P.get(col,col))

def arc(c,r,start,end,color,thick=1,phase=0):
    # Pixel-stepped orbit fragments.
    n=int(abs(end-start)*r*3)+1
    for i in range(n+1):
        a=start+(end-start)*i/n+phase
        for dr in range(thick):
            x=round(cx+(r+dr)*math.cos(a))
            y=round(cy+(r+dr)*math.sin(a))
            dot(c,x,y,color)

def star(c,x,y):
    for dx,dy in [(-2,0),(2,0),(0,-2),(0,2)]:dot(c,x+dx,y+dy,'violet')
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:dot(c,x+dx,y+dy,'pink')
    dot(c,x,y,'white')

def portal(phase,halo,name):
    c=new_canvas(48,48,name=name)
    if halo:
        # Detached halo with dark purple outer falloff, bright broken inner rim.
        for a,b in [(0.05,1.08),(1.26,2.77),(2.95,4.15),(4.35,6.12)]:
            arc(c,20.7,a,b,'halo_dark',2)
            arc(c,20.7,a+0.04,b-0.04,'halo_mid')
        for a,b in [(0.12,0.8),(1.38,2.62),(3.16,3.95),(4.46,5.85)]:
            arc(c,20.3,a,b,'halo_light')
        for a,b in [(1.5,1.99),(3.45,3.73),(4.6,5.15)]:
            arc(c,20.3,a,b,'pale')
    # Sculpted silhouette; each radial band turns into the next toward the core.
    for y in range(4,44):
        for x in range(4,44):
            dx=x-cx; dy=(y-cy)/1.02
            r=math.hypot(dx,dy)
            a=math.atan2(dy,dx)
            theta=a-phase
            rim=17.4+0.65*math.sin(3*theta+0.5)+0.35*math.sin(5*theta)
            if r>rim:continue
            q=(2*(theta+0.32*r+0.75*math.log(max(r,1))))%TAU/TAU
            if r<2.1:
                col='void'
            elif q<0.18:col='deep'
            elif q<0.35:col='shade'
            elif q<0.53:col='purple'
            elif q<0.66:col='violet'
            elif q<0.75:col='bright'
            elif q<0.81:col='pink'
            elif q<0.855:col='white' if 5<r<13 and math.sin(a+0.7)<-0.2 else 'pale'
            elif q<0.91:col='blue'
            else:col='void'
            # Bright energy breaks around the ragged lip of the opening.
            edge=rim-r
            if edge<0.8:col='shade'
            elif edge<1.65:
                col='bright' if math.sin(theta*3+0.8)>-0.35 else 'violet'
            elif edge<2.25 and q<0.58:col='purple'
            dot(c,x,y,col)
    # Swept-off energy curls make the silhouette directional.
    for j in range(3):
        a=phase+j*TAU/3
        arc(c,18.2,a+0.25,a+0.92,'deep',2)
        arc(c,18.1,a+0.35,a+0.92,'violet')
        arc(c,18.0,a+0.45,a+0.73,'pink')
        arc(c,17.2,a+0.83,a+1.22,'bright')
    # A few selected luminous rim facets.
    for a,b in [(0.95,1.32),(3.0,3.38),(4.65,5.12)]:
        arc(c,16.4,a,b,'pale',phase=phase)
    if halo:
        star(c,37,7)
        star(c,6,31)
        dot(c,43,17,'pink')
        dot(c,42,18,'halo_mid')
        dot(c,30,45,'bright')
        dot(c,29,44,'halo_dark')
    else:
        dot(c,39,12,'bright')
        dot(c,40,11,'deep')
        dot(c,6,28,'violet')
        dot(c,14,43,'bright')
    return c

frame1=portal(0,False,'frame-1-purple-vortex')
frame2=portal(math.pi/3,True,'frame-2-rotated-halo')
view(frame1,scale=8,margin=0)
view(frame2,scale=8,margin=0)
save('teleport-portal-frame-1',frame1)
save('teleport-portal-frame-2',frame2)
result=frame2
finish(result)
