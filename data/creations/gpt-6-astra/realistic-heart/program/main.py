import math
result = new_canvas(64,64,background='#101b27',name='anatomical-heart')
c=result
# A quiet blue-black field behind the warm organ.
c.ellipse(32,34,25,28,'#13212e')
c.ellipse(32,35,21,25,'#162531')
outline='#301f2b'
reds=['#482130','#5a2535','#6e2939','#822d3c','#98333f','#ad3d47','#bf4b50','#d05c59','#df7267','#ed8c7a','#f5aa8d']
# Each anatomical plane has a small, discrete tonal ramp.
def form(path, palette, lightx, lighty, rx, ry):
    m=new_canvas(64,64)
    m.path(path,'#ffffff')
    for y in range(64):
        for x in range(64):
            if m.get(x,y)==m.color('#ffffff'):
                d=((x-lightx)/rx)**2+((y-lighty)/ry)**2
                v=max(0,min(len(palette)-1,int((1-min(1,d))* (len(palette)-1))))
                c.set(x,y,palette[v])
    c.path(path,outline,fill=False)
# Rear vena cava and leftward atrial attachment.
form('M 16 24 L 16 12 Q 18 9 23 11 L 25 26 Z', ['#253248','#31435a','#435f73','#608293','#83a2aa'],18,13,8,19)
c.ellipse(20,11,4,2,'#263044')
c.line(18,10,22,10,'#94aab1')
c.line(18,12,22,12,'#172131')
# The aortic arch rises behind the pulmonary artery.
form('M 28 28 L 28 15 Q 27 7 35 7 Q 44 7 45 17 L 44 27 L 37 29 L 37 17 Q 37 13 34 15 L 35 28 Z',reds,34,11,14,24)
# Three vessels from the superior arch.
form('M 29 11 L 28 4 L 32 3 L 34 10 Z',reds,30,5,5,13)
form('M 35 9 L 35 2 L 39 2 L 39 10 Z',reds,36,3,5,12)
form('M 40 12 L 42 5 L 46 7 L 44 16 Z',reds,42,7,5,12)
c.line(28,4,31,3,'#ef9984'); c.line(29,5,31,4,'#572332')
c.line(35,2,38,2,'#f1a28b'); c.line(36,3,38,3,'#662737')
c.line(42,5,45,6,'#e48b79');c.line(43,6,45,7,'#662737')
# Small pulmonary vein stubs on the right.
form('M 42 24 L 51 21 L 54 24 L 47 29 L 44 30 Z',reds,48,23,10,9)
c.line(52,22,54,24,'#ee9983');c.line(52,23,53,24,'#542633')
form('M 44 31 L 52 28 L 54 31 L 47 35 Z',reds,48,30,9,8)
c.line(52,29,54,31,'#d8796c')
# Left atrium, dark and folded, tucked under the vessels.
form('M 41 21 Q 48 22 49 29 Q 51 36 44 39 L 34 33 L 35 24 Z',reds,44,25,10,15)
c.path('M 44 23 Q 48 27 45 30 L 47 34 L 42 36','#7b2a3a',False)
# Muscular ventricular silhouette, narrowing to the apex.
form('M 23 23 Q 32 20 40 27 Q 48 32 47 42 Q 47 52 39 59 Q 35 60 28 54 Q 19 49 15 39 Q 12 30 18 26 Z',reds,27,34,24,29)
# Broad right ventricular plane and left ventricular turn.
c.path('M 30 27 Q 32 35 36 40 Q 40 47 39 57 Q 44 52 45 44 Q 47 35 39 29 Z','#a53844')
c.path('M 37 32 Q 44 36 44 44 L 42 49 Q 42 39 37 36 Z','#bf4b50')
c.path('M 17 37 Q 20 47 29 52 L 35 57 Q 26 53 20 46 Z','#98333f')
c.path('M 18 33 Q 19 29 24 28 Q 28 27 29 31 Q 23 29 20 35 Z','#df7267')
c.path('M 20 36 Q 21 40 25 43 L 25 45 Q 20 42 18 37 Z','#d05c59')
# Right auricle wraps around the arterial roots.
form('M 18 22 Q 22 19 28 24 L 30 28 L 26 32 L 22 30 L 20 33 L 16 30 Q 13 26 18 22 Z', reds,20,24,12,12)
c.path('M 16 27 L 19 29 L 22 27 L 24 30 L 28 27','#6e2939',False)
c.path('M 17 24 L 20 23 L 24 25','#ed8c7a',False)
# Blue pulmonary artery: split upper branches and a convex trunk.
blue=['#243044','#2e4257','#3b596e','#4e7284','#6a909d','#8aafb4','#aec9c4']
form('M 28 29 Q 27 25 28 21 L 23 17 L 20 17 L 19 12 L 24 12 L 31 17 L 40 17 L 46 15 L 48 19 L 42 23 L 35 23 L 35 30 Z',blue,29,19,19,13)
c.path('M 29 27 L 30 22 L 27 18 L 23 15','#8aafb4',False)
c.path('M 35 20 L 41 20 L 46 18','#aec9c4',False)
c.line(46,15,48,18,'#6a909d');c.line(47,16,48,18,'#243044')
c.path('M 28 29 Q 31 31 35 29','#172536',False)
# Coronary groove and vessels, following the surface curvature.
c.path('M 30 31 L 32 35 L 32 39 L 36 44 L 37 50 L 39 55','#692638',False)
c.path('M 29 31 L 31 35 L 31 39 L 35 44 L 36 50 L 38 55','#e1846a',False)
c.path('M 29 32 L 30 35 L 30 39 L 34 44','#f1a083',False)
c.path('M 31 35 L 36 32 L 41 32 L 45 35','#6e2939',False)
c.path('M 31 34 L 36 31 L 41 31 L 45 34','#e1846a',False)
c.path('M 31 39 L 26 40 L 23 44 L 22 46','#923240',False)
c.path('M 30 39 L 26 39 L 22 43','#ed8c7a',False)
c.path('M 35 44 L 40 43 L 43 45','#e1846a',False)
c.path('M 36 50 L 33 49 L 30 46','#d8796c',False)
c.path('M 27 32 L 24 34 L 20 34 L 17 32','#f1a083',False)
# Fine companion veins, in the cool shadow of the major grooves.
c.path('M 33 36 L 33 40 L 37 45 L 38 50','#4e5263',False)
c.path('M 24 36 L 22 38 L 20 39','#82414d',False)
c.path('M 41 36 L 42 39 L 41 41','#82414d',False)
# Short, carefully placed wet specular accents.
c.line(22,29,25,29,'#f5aa8d')
c.set(21,30,'#ed8c7a')
c.line(24,35,25,36,'#ed8c7a')
c.set(27,38,'#df7267')
c.line(38,12,39,14,'#f5aa8d')
c.set(40,16,'#df7267')
c.line(18,14,18,17,'#83a2aa')
view(result)
save('realistic-heart',result)
finish(result)
