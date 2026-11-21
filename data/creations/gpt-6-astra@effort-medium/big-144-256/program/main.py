import random
output = input_canvas.copy(name='output')
c=output
# Ivy grows in narrow, branching trails across the masonry.
shadow='#243f37'
stem='#354c3d'
leafdark='#304d3d'
leafmid='#456450'
leaflight='#5a7960'
rng=random.Random(17)
def vine(points, density=0.8):
    for a,b in zip(points,points[1:]):
        c.line(a[0]+1,a[1],b[0]+1,b[1],shadow)
        c.line(*a,*b,stem)
        steps=max(abs(b[0]-a[0]),abs(b[1]-a[1]))
        for i in range(0,steps+1,3):
            if rng.random()>density: continue
            x=round(a[0]+(b[0]-a[0])*i/max(steps,1))
            y=round(a[1]+(b[1]-a[1])*i/max(steps,1))
            side=rng.choice([-1,1]); xx=x+side*2
            c.line(x,y,xx,y-1,stem)
            c.set(xx,y-2,leafmid)
            c.rect(xx-1,y-1,3,2,leafdark)
            c.set(xx+side,y-1,leafmid)
            if rng.random()<0.55: c.set(xx,y-2,leaflight)
            c.set(xx,y+1,shadow)
vine([(38,151),(37,138),(40,129),(39,116),(42,108),(41,97),(45,86),(44,76)])
vine([(39,130),(46,124),(48,115),(54,109),(56,99),(62,93)])
vine([(42,108),(36,103),(35,92)])
vine([(48,115),(51,119),(58,121),(62,128),(62,137)])
vine([(88,83),(86,91),(81,96),(76,97),(74,104),(76,112)],0.9)
vine([(81,96),(81,105),(84,111),(83,120)],0.8)
vine([(33,216),(34,205),(32,194),(34,183),(32,174),(35,165),(42,162),(48,164)])
vine([(34,183),(39,180),(41,174)])
vine([(35,165),(32,160),(36,157),(43,157)],0.8)
# Threshold shadow and feet in a walking pose.
c.ellipse(54,220,9,2,'#243d3a')
c.rect(49,217,3,3,'#182e31')
c.rect(55,216,3,3,'#182e31')
c.set(58,218,'#50635d')
# Back of the hood and shoulders, with a long cloak gathered in folds.
c.poly([(48,201),(50,198),(49,194),(51,189),(54,187),(57,191),(58,196),(57,199),(60,202),(59,208),(62,217),(56,219),(52,218),(46,219),(47,211)],'#203335')
c.poly([(49,202),(52,199),(56,199),(58,202),(57,208),(60,216),(55,217),(51,216),(48,217)],'#48505d')
c.poly([(49,203),(51,202),(51,210),(50,216),(48,217)],'#606371')
c.poly([(54,201),(56,204),(55,210),(57,217),(54,216),(53,208)],'#333f4b')
c.line(52,205,52,214,'#72727b')
c.set(52,215,'#5d6470')
c.poly([(50,195),(52,191),(54,189),(56,192),(57,196),(55,199),(52,198)],'#535b67')
c.line(51,194,53,191,'#7b7b80')
c.poly([(54,191),(56,194),(56,197),(53,197)],'#3a4652')
c.line(51,199,55,200,'#85817d')
# A bent sleeve reaches for the staff to the mage's right.
c.poly([(57,201),(59,202),(60,205),(63,203),(64,206),(59,209),(57,207)],'#303e48')
c.line(59,205,61,206,'#66717b')
c.rect(63,203,2,2,'#ac9c7b')
# Small local staff glow, composited rather than replacing stonework.
glow=new_canvas(144,256,name='staff glow')
glow.circle(65,192,7,'#70dcbe12')
glow.circle(65,192,5,'#7ae7ce1c')
glow.circle(65,192,3,'#8affdf30')
c=flatten([output,glow],name='result')
c.line(64,197,64,219,'#233b38')
c.line(65,197,65,218,'#8b8968')
c.line(65,198,65,206,'#b2aa7d')
c.line(64,198,62,194,'#789888')
c.line(66,198,68,194,'#789888')
c.set(63,195,'#a3cfb0')
c.set(67,195,'#a3cfb0')
c.poly([(65,188),(67,192),(65,195),(63,192)],'#73ccba')
c.line(65,189,65,193,'#e1ffe2')
c.set(64,191,'#b0f7d9')
c.set(69,189,'#76b6a7')
c.set(61,190,'#77b5a4')
c.set(67,185,'#7bb3a2')
view(c,scale=3,margin=0)
finish(c)
