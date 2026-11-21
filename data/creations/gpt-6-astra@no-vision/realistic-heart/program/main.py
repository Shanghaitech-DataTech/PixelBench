import math
result = new_canvas(64, 64, background='#111b28', name='Anatomical heart')
c = result
# Finite ramps keep the musculature and vessels coherent at native resolution.
red = ['#361d2c','#502331','#692936','#81313d','#9a3b45','#b3484d','#c85856','#d86960','#e57b6b','#ed907b','#f2a48b','#f5b79a']
rose = ['#3d2433','#582a38','#74313f','#8c3b49','#a54853','#bc5960','#ce6d6c','#df827b','#eb9a8a','#f2b29b']
blue = ['#172b3e','#203b50','#294b62','#365c73','#456e85','#58859a','#729eac','#91b8bf','#b1cfd0']
artery = ['#402735','#5b303d','#783e49','#954d54','#af5e60','#c77370','#d98c82','#e7a493','#f1bba5']
fat = ['#79423e','#a0644e','#bf865f','#d5a377','#e6bf91']
# Small cast shadow grounds the isolated study.
c.ellipse(34,59,18,2,'#0c1420')

def shaded(path, ramp, light, radii, base=.3, gain=.65):
    m = new_canvas(64,64)
    m.path(path,'#ffffff')
    _,_,data=m.to_rgba()
    inside={(x,y) for y in range(64) for x in range(64) if data[4*(y*64+x)+3]}
    for x,y in inside:
        dx=(x-light[0])/radii[0]; dy=(y-light[1])/radii[1]
        value=base+gain*max(0,1-dx*dx-dy*dy)
        # Local occlusion at a stepped silhouette, with a soft upper-left rim.
        edge=0
        for dist in (1,2,3):
            if any((x+ox*dist,y+oy*dist) not in inside for ox,oy in [(1,0),(-1,0),(0,1),(0,-1)]):
                edge=4-dist
                break
        value-=edge*.075
        if (x-1,y-1) not in inside: value+=.09
        value+=(((x//2)*7+(y//2)*11)%5-2)*.012
        idx=max(0,min(len(ramp)-1,round(value*(len(ramp)-1))))
        c.set(x,y,ramp[idx])
    return inside

# Superior vena cava, behind the atrium.
shaded('M 17 12 L 24 11 L 26 29 L 18 32 L 16 22 Z',blue,(19,17),(8,19),.25,.65)
c.ellipse(20,12,4,2,blue[5]); c.ellipse(20,12,3,1,blue[0]);c.line(17,11,21,10,blue[7])
# The arch and its three open arterial branches.
shaded('M 28 28 L 28 18 Q 27 11 32 9 L 32 5 L 36 4 L 38 10 L 40 11 L 41 6 L 45 7 L 44 14 L 47 17 L 48 12 L 52 14 L 50 21 Q 48 27 43 29 L 40 24 L 43 20 Q 42 15 37 15 Q 34 15 35 22 L 36 29 Z',artery,(35,10),(18,24),.2,.7)
c.line(32,5,36,4,artery[7]);c.line(33,5,35,5,artery[0])
c.line(41,6,45,7,artery[7]);c.line(42,7,44,7,artery[0])
c.line(48,12,52,14,artery[6]);c.line(49,13,51,14,artery[0])
c.path('M 30 20 Q 29 12 34 11',artery[6],fill=False)
# Rear pulmonary veins entering the left atrium.
shaded('M 43 25 L 52 22 L 54 25 L 47 30 L 51 31 L 50 35 L 42 32 Z',rose,(47,26),(10,10),.28,.6)
c.line(52,23,53,25,rose[1]);c.line(49,32,49,34,rose[2])
# Main ventricular silhouette: broad shoulder to a single downward apex.
shaded('M 23 23 Q 31 19 40 24 Q 48 27 50 37 Q 52 48 43 56 Q 40 60 36 57 Q 26 54 20 46 Q 14 38 16 31 Q 17 26 23 23 Z',red,(29,33),(24,29),.12,.76)
# Right ventricle's rounded anterior face.
shaded('M 23 25 Q 29 24 34 30 Q 34 38 39 51 L 40 56 Q 27 51 20 43 Q 15 36 19 30 Z',rose,(23,33),(19,24),.16,.67)
# Muscular left ventricle bulges on the viewer's right.
shaded('M 36 27 Q 47 27 49 37 Q 51 48 42 56 L 39 58 Q 35 49 33 41 Q 31 33 36 27 Z',red,(39,35),(15,26),.13,.7)
# Pulmonary trunk crossing in front of the ascending aorta.
shaded('M 29 29 Q 28 23 33 20 Q 38 17 43 18 L 51 17 L 53 20 L 50 24 L 43 24 Q 38 22 36 27 L 35 32 Z',blue,(38,20),(19,12),.22,.73)
c.ellipse(51,20,2,3,blue[5]);c.ellipse(52,20,1,2,blue[0]);c.set(51,18,blue[7])
c.path('M 31 27 Q 31 22 37 21 L 44 21',blue[6],fill=False)
# The right atrial appendage curls over the upper myocardium.
shaded('M 19 23 Q 23 20 28 24 L 31 29 L 29 33 L 25 30 L 22 32 L 18 30 L 17 26 Z',rose,(22,25),(12,10),.18,.65)
c.path('M 20 27 L 23 26 L 26 28 L 28 28',rose[3],fill=False)
c.path('M 18 29 L 21 30 L 23 29',rose[2],fill=False)
# Left auricle, a folded muscular lip beneath the blue vessel.
shaded('M 39 25 Q 43 23 47 26 L 48 31 L 44 30 L 42 32 L 38 30 Z',rose,(42,26),(10,9),.22,.65)
c.path('M 40 28 L 43 27 L 46 29',rose[3],fill=False)
# Coronary sulcus: dark creases, warm epicardial fat, and branching vessels.
c.path('M 20 32 Q 26 34 32 30 Q 35 28 39 31',red[1],fill=False)
c.path('M 20 31 Q 25 33 31 29',fat[1],fill=False)
c.path('M 22 31 L 26 31 L 29 30',fat[3],fill=False)
c.path('M 35 30 Q 32 35 35 42 Q 36 48 40 54',red[1],fill=False)
c.path('M 36 31 Q 33 35 36 42 Q 37 48 40 53',fat[1],fill=False)
c.path('M 35 32 L 34 36 L 35 39',fat[3],fill=False)
c.path('M 36 40 L 37 44 L 38 47',fat[2],fill=False)
# Fine coronary artery branches track the curvature of the ventricles.
for p in ['M 35 36 Q 40 34 43 36 L 47 37', 'M 37 43 L 42 42 L 46 44', 'M 28 32 L 27 37 L 23 41 L 23 44', 'M 27 37 L 30 42 L 32 46', 'M 40 48 L 43 48 L 45 47']:
    c.path(p,red[2],fill=False)
for p in ['M 36 35 L 40 34 L 43 35 L 46 36', 'M 38 42 L 42 41 L 45 43','M 27 33 L 26 37 L 22 40', 'M 27 38 L 29 41']:
    c.path(p,red[6],fill=False)
# A cool companion vein runs beside the anterior descending artery.
c.path('M 37 32 L 36 35 L 36 38 L 38 42 L 39 47 L 41 51',blue[2],fill=False)
c.path('M 37 33 L 37 36 L 38 39',blue[4],fill=False)
# Deliberate short pixel clusters suggest wet reflected light and muscle fibres.
for x,y,col in [(21,34,rose[8]),(22,34,rose[8]),(20,35,rose[7]),(21,36,rose[7]),(24,37,rose[7]),(40,32,red[9]),(41,32,red[9]),(42,33,red[8]),(43,34,red[8]),(43,38,red[8]),(44,39,red[7]),(42,46,red[6]),(40,52,red[5]),(30,46,rose[5]),(31,47,rose[5]),(25,43,rose[6])]: c.set(x,y,col)
c.path('M 19 38 L 20 41 L 23 45',rose[3],fill=False)
c.path('M 45 46 L 44 49 L 42 52',red[4],fill=False)
print(c.stats_text())
print(c.matrix_text(region=(15,22,49,44)))
save('realistic-heart',result)
finish(result)
