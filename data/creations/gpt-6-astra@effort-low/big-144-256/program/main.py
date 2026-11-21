import random
output=input_canvas.copy(name='output')
# Wall ivy: woody runners and small overlapping, angular leaves.
rng=random.Random(28)
def vine(points, density=0.85):
    samples=[]
    for (x,y),(xx,yy) in zip(points,points[1:]):
        output.line(x+1,y,xx+1,yy,'#263e37')
        output.line(x,y,xx,yy,'#405344')
        n=max(abs(xx-x),abs(yy-y))
        for i in range(n+1):
            if i%3==0: samples.append((round(x+(xx-x)*i/max(1,n)),round(y+(yy-y)*i/max(1,n))))
    for x,y in samples:
        if rng.random()>density: continue
        side=rng.choice([-1,1]); dx=side*rng.randint(2,4); dy=rng.randint(-3,1)
        output.line(x,y,x+dx,y+dy,'#344c3c')
        lx=x+dx; ly=y+dy
        output.poly([(lx-side*2,ly),(lx,ly-2),(lx+side*2,ly-1),(lx+side*3,ly+1),(lx,ly+2)],rng.choice(['#304b3d','#385440','#3e5b47','#46624c']))
        output.set(lx,ly-1,rng.choice(['#526b51','#48664e','#3e5b47']))
vine([(38,145),(40,133),(38,122),(42,111),(40,101),(44,89),(43,79),(48,70)])
vine([(40,119),(47,115),(51,108),(55,102),(55,94)],0.85)
vine([(42,108),(36,98),(36,87),(39,78)],0.8)
vine([(47,113),(52,117),(59,116),(64,110)],0.7)
vine([(87,144),(85,134),(89,125),(86,117),(89,107),(88,96),(91,86),(89,74),(85,67)])
vine([(88,99),(80,95),(77,87),(78,78)],0.9)
vine([(85,133),(79,129),(77,123)],0.75)
# Ivy climbs the entrance's right masonry, leaving the opening clear.
vine([(73,220),(72,212),(75,204),(71,195),(73,184),(70,177),(72,169),(66,164)])
vine([(72,183),(78,180),(82,174)],0.85)
vine([(35,212),(33,201),(35,191),(32,181),(35,169),(42,163)],0.75)
# Small shadow on the threshold.
output.ellipse(53,220,8,2,'#233b39')
# Boots, staggered in a step into the arch.
output.rect(49,214,3,6,'#202e31')
output.rect(48,219,4,2,'#263134')
output.rect(56,212,3,5,'#202e31')
output.rect(56,216,4,2,'#34413f')
# Full back of the cloak, shoulder to swinging hem.
output.poly([(49,195),(55,194),(59,198),(59,204),(61,217),(55,219),(51,217),(46,219),(47,209),(46,201)],'#222f36')
output.poly([(49,197),(54,196),(57,199),(57,207),(59,216),(54,216),(51,215),(48,217),(49,207)],'#46505b')
output.poly([(49,200),(51,199),(51,208),(49,215),(47,217)],'#59606a')
output.poly([(54,200),(56,201),(56,210),(58,216),(54,215)],'#343e4b')
output.line(52,203,51,213,'#687078')
# Raised sleeve and hand around the staff.
output.poly([(57,199),(59,200),(60,204),(63,202),(64,204),(60,208),(57,206)],'#2a3640')
output.line(59,202,60,205,'#505b61')
# Hood seen from behind; no face visible.
output.poly([(48,196),(48,192),(50,189),(53,188),(56,191),(57,196),(54,200),(51,201)],'#222f37')
output.poly([(49,195),(50,191),(53,190),(55,192),(55,196),(52,199)],'#545e69')
output.line(50,193,51,191,'#717b80')
output.line(50,197,52,199,'#3c4653')
# Amber staff with a soft pixel halo, composited over the masonry.
glow=new_canvas(144,256)
glow.circle(64,192,6,'#e4ba5920')
glow.circle(64,192,4,'#efc76d30')
output=flatten([output,glow],name='output_glow')
output.line(63,197,63,218,'#283833')
output.line(64,196,64,217,'#8a7751')
output.set(64,211,'#b09b67')
output.rect(62,203,2,2,'#a69a77')
output.line(64,198,61,194,'#9d8b53')
output.line(64,198,67,193,'#9d8b53')
output.poly([(64,188),(66,191),(65,195),(63,195),(62,192)],'#edce7e')
output.line(64,190,64,193,'#fff0ba')
output.set(63,191,'#fff5ce')
output.set(68,188,'#baad70')
output.set(60,190,'#b2a46c')
view(output,scale=4,margin=0)
finish(output)
