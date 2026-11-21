import math
import random
import numpy as np

result = new_canvas(64, 64, background='#101c25', name='Anatomical heart')
# Small, deliberately stepped palettes keep every contour on the pixel grid.
flesh = ['#301625','#451a2b','#591e30','#702338','#89283e','#a23146','#ba3c50','#cd4b5a','#dd6169','#e7797b','#ee9290','#f3aca2','#f8c7b4']
artery = ['#481e2a','#652333','#842c3c','#a13847','#bc4955','#d25e65','#e37879','#ed9691','#f5b9a7']
vein = ['#242333','#303043','#414457','#535c70','#697e91','#8da4ae','#b2c6c7','#d1d9cf']
cut = ['#241b29','#462431','#6a3542','#9e505d','#c77a7d','#e7a39b','#f6c7b3']
fat = ['#61342e','#89503f','#ad7053','#c8916c','#e2b28b','#f2d0a9']
blue = ['#332838','#4a354b','#624758','#805c6b','#a47c85']

def mask_for(d):
    m = new_canvas(64,64)
    m.path(d, '#ffffff')
    w,h,b = m.to_rgba()
    return np.frombuffer(b,dtype=np.uint8).reshape((h,w,4))[:,:,3]>0

def paint(d, ramp, fun):
    a=mask_for(d)
    for y,x in zip(*np.where(a)):
        value=fun(int(x),int(y))
        i=max(0,min(len(ramp)-1,int(value*(len(ramp)-1)+0.5)))
        result.set(int(x),int(y),ramp[i])
    return a

def ellipse_light(x,y,cx,cy,rx,ry,bias=0,bright=1):
    nx=(x-cx)/rx; ny=(y-cy)/ry
    z=math.sqrt(max(0,1-nx*nx-ny*ny))
    return bias+bright*(0.21+0.61*z-0.24*nx-0.19*ny)

def tube(d, points, radius, ramp, boost=0):
    def shade(x,y):
        best=1e9; vx=vy=0
        for (ax,ay),(bx,by) in zip(points[:-1],points[1:]):
            dx=bx-ax;dy=by-ay
            t=max(0,min(1,((x-ax)*dx+(y-ay)*dy)/(dx*dx+dy*dy)))
            qx=x-ax-t*dx;qy=y-ay-t*dy
            ds=qx*qx+qy*qy
            if ds<best: best=ds;vx=qx;vy=qy
        z=math.sqrt(max(0,1-best/(radius*radius)))
        return .22+.58*z-.25*vx/radius-.2*vy/radius+boost
    return paint(d,ramp,shade)

# Back vessels: left superior cava and paired pulmonary veins on the right.
tube('M15 12 Q18 9 23 12 L24 28 L16 30 Q18 22 15 12 Z',[(19,12),(20,21),(20,28)],4.7,vein,-.03)
result.ellipse(19,12,4,2,vein[6])
result.ellipse(19,12,3,1,vein[0])
result.line(17,14,21,14,vein[4])
tube('M43 22 L52 20 L54 23 L45 28 Z',[(45,25),(52,22)],3.0,artery,-.14)
result.ellipse(52,22,2,3,cut[4]); result.ellipse(53,22,1,2,cut[1])
tube('M45 28 L54 27 L55 31 L47 34 Z',[(47,31),(53,29)],3,artery,-.2)
result.ellipse(54,29,2,3,cut[3]);result.ellipse(54,29,1,2,cut[0])

# Aortic arch; the three severed great branches retain their visible lumens.
tube('M24 25 L24 16 Q24 8 31 7 Q40 5 44 12 Q46 17 42 23 L36 22 Q39 17 37 14 Q34 11 32 15 L33 25 Z',[(28,24),(28,16),(30,11),(35,10),(40,13),(40,20)],4.7,artery)
tube('M27 12 L25 5 L29 3 L33 11 Z',[(27,5),(30,11)],3,artery,.02)
tube('M33 10 L33 3 L38 3 L39 11 Z',[(35,3),(36,10)],3,artery)
tube('M39 13 L41 6 L46 8 L44 16 Z',[(43,8),(41,14)],3,artery,-.05)
for x,y,rx in [(27,4,3),(35,3,3),(43,7,3)]:
    result.ellipse(x,y,rx,2,cut[5])
    result.ellipse(x,y,rx-1,1,cut[1])
    result.line(x-1,y-1,x+1,y-1,cut[0])
    result.line(x-1,y+2,x+1,y+2,artery[6])
# Arch highlights are clustered on the outer turning shoulder.
result.path('M28 15 Q27 11 32 9 L36 9',artery[7],fill=False)
result.line(29,17,29,20,artery[6])
result.path('M39 11 Q42 14 41 17',artery[4],fill=False)

# Whole muscular silhouette, with a thick rounded left ventricle tapering to the apex.
body='M23 22 Q28 21 33 23 Q40 20 46 25 Q52 30 51 38 Q50 49 44 56 Q41 61 36 59 Q26 57 20 50 Q13 44 12 36 Q11 29 16 25 Q19 22 23 22 Z'
paint(body,flesh,lambda x,y:ellipse_light(x,y,31,38,21,23,-.07,.93))
# Right atrium on the viewer\'s left, behind the ventricular ridge.
paint('M20 23 Q25 21 28 25 Q30 31 25 36 Q20 40 15 37 Q11 34 14 28 Q16 24 20 23 Z',flesh,lambda x,y:ellipse_light(x,y,20,29,9,11,-.09,.91))
result.path('M16 29 Q17 25 21 25 L24 26',flesh[9],fill=False)
result.path('M14 35 Q17 39 22 37 L25 34',flesh[3],fill=False)
# Right ventricle: broad, oblique front face.
paint('M22 31 Q28 28 34 30 Q38 34 36 41 L34 48 Q36 54 39 58 Q29 56 22 50 Q15 44 14 37 Q16 33 22 31 Z',flesh,lambda x,y:ellipse_light(x,y,25,38,16,20,.01,.88))
# Left ventricle: the prominent convex wall, separated by the descending groove.
paint('M36 28 Q42 24 47 29 Q52 33 50 42 Q48 51 43 57 Q41 60 37 58 Q35 54 34 49 Q32 44 34 39 Q36 34 36 28 Z',flesh,lambda x,y:ellipse_light(x,y,40,37,11,23,-.02,.99))
# Upper left auricle, folded and creased above the muscular wall.
paint('M38 22 Q43 20 46 23 L49 28 L45 31 L40 28 L36 28 L35 25 Z',flesh,lambda x,y:ellipse_light(x,y,41,24,9,7,-.09,.83))
result.path('M39 25 L42 24 L46 27 L43 27 L45 29',flesh[3],fill=False)
result.line(40,23,43,23,flesh[8])
result.line(46,26,47,27,flesh[7])

# Pulmonary trunk passes in front of the aorta and turns laterally.
tube('M26 29 Q25 24 29 20 Q32 16 38 15 L48 13 L51 15 L50 19 L40 21 Q35 21 34 25 L34 29 Z',[(30,28),(30,24),(34,19),(40,18),(49,16)],4.1,vein)
result.ellipse(49,16,3,4,vein[4])
result.ellipse(50,16,2,3,vein[0])
result.line(50,14,51,15,vein[1])
result.line(48,14,48,17,vein[6])
result.path('M29 26 Q29 22 33 20 L37 18 L43 17',vein[6],fill=False)
result.path('M33 27 Q33 23 36 22 L42 21',vein[2],fill=False)
# Short left pulmonary branch disappears behind the trunk.
tube('M29 20 L23 18 L20 20 L22 23 L28 24 Z',[(22,20),(28,22)],2.7,vein,-.02)
result.line(22,19,26,20,vein[5])
# The root wraps in a warm muscular collar.
paint('M25 27 Q29 29 34 27 L35 30 L31 33 L26 31 L24 29 Z',flesh,lambda x,y:.70-.065*(y-28)-.035*(x-27))
result.path('M25 28 Q29 31 33 29',flesh[10],fill=False)

# Coronary sulcus: deep occlusion, small deposits of warm epicardial fat.
result.path('M16 35 L21 32 L26 32 L31 34 L35 32 L38 29 L43 30 L47 32',flesh[2],fill=False)
result.path('M16 36 L21 33 L26 33 L30 35 L34 34',flesh[4],fill=False)
result.path('M36 32 L35 37 L33 42 L34 47 L37 52 L38 56',flesh[1],fill=False)
result.path('M37 34 L36 38 L34 43 L35 47 L38 52',flesh[4],fill=False)
for x,y,k in [(18,34,2),(20,33,3),(22,32,3),(23,33,2),(26,33,3),(28,34,2),(31,34,3),(34,33,3),(35,34,2),(35,36,3),(34,38,2),(33,40,2),(34,44,2),(36,49,1),(38,30,3),(41,30,2),(44,31,2),(46,32,1)]:
    result.set(x,y,fat[k])
# Descending coronary artery and its clean, increasingly fine branches.
result.path('M36 30 L34 34 L34 38 L32 42 L33 47 L36 52 L38 56',artery[2],fill=False)
result.path('M36 30 L35 34 L35 37 L33 42 L34 47 L37 52 L38 55',artery[7],fill=False)
result.line(35,33,35,36,fat[4])
result.path('M34 39 L29 39 L26 37 L22 37 L19 39',flesh[4],fill=False)
result.path('M34 38 L29 38 L26 36 L22 36 L19 38',artery[7],fill=False)
result.path('M29 38 L27 42 L27 45 L24 47',artery[5],fill=False)
result.path('M33 44 L29 47 L30 51 L33 54',artery[6],fill=False)
result.path('M35 35 L40 34 L44 35 L47 38',flesh[3],fill=False)
result.path('M36 34 L40 33 L44 34 L47 37',artery[7],fill=False)
result.path('M40 34 L40 38 L43 41 L43 45 L42 48',artery[6],fill=False)
result.path('M35 46 L39 44 L41 44',artery[6],fill=False)
# A companion vein, kept subdued so the central artery remains legible.
result.path('M37 33 Q38 38 35 42 Q35 46 38 49 L40 54',blue[1],fill=False)
result.path('M37 34 Q38 37 36 40',blue[3],fill=False)
result.path('M36 43 Q39 40 42 40 Q45 39 47 42',blue[2],fill=False)
result.path('M21 34 Q19 39 22 43 L25 46',blue[2],fill=False)
result.path('M20 39 L17 40 L17 42',blue[2],fill=False)
# Finer tapering branches follow the rounded wall.
result.path('M44 35 L46 34 L47 34',artery[5],fill=False)
result.path('M43 42 L46 43 L46 45',artery[4],fill=False)
result.path('M39 44 L39 47 L40 48',artery[5],fill=False)
result.path('M27 43 L24 42 L23 42',artery[6],fill=False)
result.path('M29 49 L27 50 L26 50',artery[4],fill=False)
result.path('M22 36 L22 34 L21 33',artery[5],fill=False)
# Sparse muscular striations follow the ventricle, with no random noise.
for d,col in [
    ('M16 41 L19 45 L23 48',flesh[6]),
    ('M19 42 L21 45 L24 47',flesh[8]),
    ('M25 48 L28 51 L31 53',flesh[7]),
    ('M24 50 L27 52',flesh[5]),
    ('M42 50 L44 46 L46 44',flesh[6]),
    ('M41 53 L44 49',flesh[7]),
    ('M45 41 L47 38',flesh[8]),
    ('M44 32 L46 34',flesh[9]),
    ('M27 35 L29 36',flesh[10]),
    ('M23 39 L25 40',flesh[10])]:
    result.path(d,col,fill=False)
# Tiny wet specular reflections are selective and asymmetric.
result.line(38,29,40,29,flesh[10])
result.line(39,30,41,30,flesh[11])
result.set(40,31,flesh[10])
result.line(19,29,20,28,flesh[11])
result.line(22,40,23,41,flesh[11])
result.set(24,42,flesh[10])
result.set(29,24,vein[7])

view(result,scale=8,margin=0)
save('realistic-heart', result)
finish(result)
