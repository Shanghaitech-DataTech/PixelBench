import math
import numpy as np

# The original sprite is the material and detail source for the turning model.
src = input_canvas
P = {p['name']: p['index'] for p in src.palette()}
ink = P['c3']; brown=P['c0']; ochre=P['c1']; gold=P['c2']; tile=P['c4']
amber=P['c5']; light=P['c6']; yellow=P['c7']; plaster=P['c8']; cream=P['c9']
root2 = math.sqrt(0.5)
source_origin = 118.47
W,H=176,176

# Hand-built right wall. Its oak, plaster and leaded window use the source palette.
side = new_canvas(99,66,name='right_wall_material')
side.rect(0,0,99,66,ink)
side.rect(4,4,91,58,plaster)
side.poly([(7,7),(91,7),(91,44),(82,44),(82,56),(15,56),(15,46),(7,46)],cream)
side.poly([(7,31),(14,34),(14,49),(25,49),(25,57),(7,57)],plaster)
side.poly([(81,12),(91,12),(91,53),(79,53),(79,49),(85,49),(85,25),(81,25)],plaster)
# Squat stone footing and heavy timber frame.
side.rect(5,59,89,4,brown)
side.rect(10,57,79,2,ochre)
for x in [5,84]:
    side.rect(x,3,10,59,brown)
    side.poly([(x+2,4),(x+7,4),(x+7,13),(x+5,25),(x+7,38),(x+7,57),(x+3,60),(x+3,42),(x+1,30)],ochre)
    side.path(f'M {x+4} 6 L {x+5} 15 L {x+3} 26 L {x+5} 36 L {x+4} 53',gold,False)
    side.line(x+8,9,x+8,22,ochre)
side.rect(8,3,82,5,brown)
side.rect(12,4,74,2,ochre)
# Small braces under the eaves.
side.poly([(15,8),(27,8),(15,22)],brown)
side.line(16,17,23,9,ochre)
side.poly([(83,8),(72,8),(83,21)],brown)
side.line(76,9,82,15,ochre)
# One clearly glazed, arched window, above a projecting sill.
side.path('M 28 51 L 28 30 Q 28 12 49 11 Q 70 12 70 30 L 70 51 Z',ink)
side.path('M 31 49 L 31 30 Q 31 15 49 14 Q 67 15 67 30 L 67 49 Z',brown)
side.path('M 33 47 L 33 30 Q 33 17 49 16 Q 65 17 65 30 L 65 47 Z',gold)
side.path('M 36 46 L 36 30 Q 36 20 49 19 Q 62 20 62 30 L 62 46 Z',ink)
side.path('M 39 43 L 39 29 Q 39 22 49 22 Q 59 23 59 30 L 59 43 Z',amber)
side.poly([(39,29),(44,24),(46,24),(46,29),(41,35),(39,35)],light)
side.poly([(53,25),(55,25),(55,31),(52,35),(51,35),(51,31)],yellow)
side.rect(40,38,5,5,gold)
side.rect(54,38,5,5,tile)
side.rect(47,21,4,25,ink)
side.rect(48,23,1,22,ochre)
side.rect(37,34,24,4,ink)
side.rect(39,35,20,1,gold)
side.line(34,28,34,43,ochre)
side.line(63,28,63,43,ochre)
side.path('M 33 25 Q 37 17 47 17',light,False)
side.rect(26,49,47,5,ink)
side.rect(28,49,43,2,gold)
side.rect(30,51,39,3,ochre)
side.rect(32,54,35,2,brown)
side.rect(32,49,31,1,yellow)
# A few broad plaster wear marks, in the same clustered pixel style.
side.rect(18,35,5,2,plaster)
side.rect(20,37,4,5,plaster)
side.rect(74,41,4,6,plaster)
side.rect(72,45,6,2,plaster)

# Unwrap the source's hand-drawn shingle slope onto a continuous roof plane.
# Both ends of each strip are anchored so the original curved silhouette does
# not open a gap over the newly visible wall.
roof_right=new_canvas(112,157,name='right_roof_material')
for u in range(56,111):
    sample_u=min(u,103)
    z=112-(50/55.5)*(u-55.5)
    sample_z=112-(50/55.5)*(sample_u-55.5)
    edge=source_origin+49*root2-root2*sample_z
    first=next((v for v in range(157) if src.get(sample_u,v)!=0),0)
    far=source_origin-root2*(z+52)
    near=source_origin-root2*(z-53)
    for v in range(max(0,math.ceil(far)),min(157,math.floor(near)+1)):
        t=(v-far)/(near-far)
        vv=int(round(first+(edge-first)*t))
        col=src.get(sample_u,vv)
        if col==0: col=ink
        if u>=108: col=ink
        elif u>=106: col=brown
        elif u==105: col=ochre
        if v<far+2: col=ink
        roof_right.set(u,v,col)

# Substantial fascia under the side eave, with one readable long woodgrain.
eave=new_canvas(103,9,name='side_eave_material')
eave.rect(0,0,103,9,ink)
eave.rect(1,1,101,5,brown)
eave.rect(2,1,99,2,ochre)
eave.rect(4,1,94,1,gold)
eave.path('M 5 4 L 21 4 L 30 3 L 45 3 L 52 4 L 73 4 L 83 3 L 97 3',ochre,False)

# Orthographic projection. Only yaw changes; pitch remains exactly 45 degrees.
def projection(theta):
    a=math.radians(theta)
    cs,sn=math.cos(a),math.sin(a)
    def p(v):
        x,y,z=v
        return np.array([88+cs*x+sn*y, 118+root2*(sn*x-cs*y-z)])
    return p

def stamp_plane(dst, texture, to_world, project, mask_fn=None, recolor=None):
    p0=project(to_world(0,0))
    pu=project(to_world(1,0))-p0
    pv=project(to_world(0,1))-p0
    mat=np.array([[pu[0],pv[0]],[pu[1],pv[1]]])
    if abs(np.linalg.det(mat))<0.001: return
    inv=np.linalg.inv(mat)
    tw,th=texture.stats()['size']
    corners=[project(to_world(u,v)) for u,v in [(-.5,-.5),(tw-.5,-.5),(-.5,th-.5),(tw-.5,th-.5)]]
    xa=max(0,int(math.floor(min(p[0] for p in corners))))
    xb=min(W-1,int(math.ceil(max(p[0] for p in corners))))
    ya=max(0,int(math.floor(min(p[1] for p in corners))))
    yb=min(H-1,int(math.ceil(max(p[1] for p in corners))))
    for yy in range(ya,yb+1):
        for xx in range(xa,xb+1):
            u,v=inv @ (np.array([xx,yy])-p0)
            u,v=int(math.floor(u+.5)),int(math.floor(v+.5))
            if 0<=u<tw and 0<=v<th and (mask_fn is None or mask_fn(u,v)):
                col=texture.get(u,v)
                if col!=0:
                    if recolor: col=recolor.get(col,col)
                    dst.set(xx,yy,col)

def roof_world(u,v,right):
    x=u-55.5
    z=112-(50/55.5)*(x if right else -x)
    y=(source_origin-v)/root2-z
    return x,y,z

def front_world(u,v):
    return u-55.5,-49,(source_origin+49*root2-v)/root2

def boundary(u):
    return source_origin+49*root2-root2*(112-(50/55.5)*abs(u-55.5))

# A separate raised ridge lets the original carved grain remain legible at both angles.
def ridge_world(u,v):
    x=u-55.5
    z=115
    y=(source_origin-v)/root2-z
    return x,y,z

def make(theta,name):
    c=new_canvas(W,H,name=name)
    project=projection(theta)
    # Contact shadow follows the footprint, with clipped corners.
    pts=[project((x,y,-2)) for x,y in [(-43,-54),(43,-54),(49,-48),(49,44),(43,50),(-43,50),(-49,44),(-49,-48)]]
    c.poly([(round(p[0]),round(p[1])) for p in pts],P['c10'])
    stamp_plane(c,side,lambda u,v:(44.5,u-49,64-v),project)
    if theta<89:
        stamp_plane(c,src,front_world,project,lambda u,v:v>=boundary(u)-1 and src.get(u,v)!=P['c10'])
    # Fascia projects out beyond the plaster and catches a narrow band of light.
    stamp_plane(c,eave,lambda u,v:(52,u-51,65-v),project)
    # Distant roof slope is hidden when looking squarely at the right side.
    if theta<89:
        stamp_plane(c,src,lambda u,v:roof_world(u,v,False),project,lambda u,v:u<56 and v<boundary(u))
    stamp_plane(c,roof_right,lambda u,v:roof_world(u,v,True),project)
    # Paint a narrow central carved beam as a raised roof element.
    stamp_plane(c,src,ridge_world,project,lambda u,v:49<=u<=62 and v<=77 and src.get(u,v) in [brown,ochre,gold,ink])
    # The original gold finial curls down over the front gable at the ridge end.
    if theta<89:
        stamp_plane(c,src,front_world,project,lambda u,v:47<=u<=64 and 69<=v<=83 and src.get(u,v) in [gold,yellow])
    return c

f1=make(45,'house_45')
f2=make(90,'house_90')
view(f1,scale=4,margin=0)
view(f2,scale=4,margin=0)
save('house_45_degrees',f1)
save('house_90_degrees',f2)
finish([f1,f2])
