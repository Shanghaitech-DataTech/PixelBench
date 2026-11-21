import random
import math

output = input_canvas.copy(name='output')

# Ivy is painted on the masonry, with quiet, cool shadows and olive-jade tips.
vines = new_canvas(144,256,name='climbing_ivy')
VSH = '#263e39'
STEM = '#3b5344'
STEML = '#66765b'
LEAFD = '#2c5145'
LEAFM = '#3c6550'
LEAFL = '#56795c'
LEAFH = '#729077'
rng = random.Random(27)

# Every leaf is a small lobed pixel cluster, with a one-pixel shaded underside.
def leaf(x,y,side=1,size=1,lit=False):
    if size == 0:
        pixels=[(0,0),(side,-1),(side*2,-1),(side,-2)]
    else:
        pixels=[(0,0),(side,-1),(side*2,-1),(side*3,-2),
                (side*2,-2),(side,-2),(side*2,-3),(0,-2)]
    for dx,dy in pixels:
        vines.set(x+dx+1,y+dy+1,VSH)
    for dx,dy in pixels:
        vines.set(x+dx,y+dy,LEAFM if lit else LEAFD)
    vines.set(x+side,y-2,LEAFL if lit else LEAFM)
    if size:
        vines.set(x+side*2,y-2,LEAFH if lit and rng.random()<0.33 else LEAFL if lit else LEAFM)

def branch(points,density=0.75,thick=False):
    for (x0,y0),(x1,y1) in zip(points,points[1:]):
        vines.line(x0+1,y0+1,x1+1,y1+1,VSH)
        vines.line(x0,y0,x1,y1,STEM)
        if thick:
            vines.line(x0-1,y0,x1-1,y1,LEAFD)
        length=math.hypot(x1-x0,y1-y0)
        count=max(1,int(length/3))
        for i in range(count):
            if rng.random()>density:
                continue
            t=(i+0.25+rng.random()*0.45)/count
            x=round(x0+(x1-x0)*t)
            y=round(y0+(y1-y0)*t)
            side=rng.choice([-1,1])
            vines.line(x,y,x+side,y-1,STEM)
            leaf(x+side,y-1,side,rng.choice([0,1,1]),rng.random()<0.58)
            if thick and rng.random()<0.65:
                leaf(x-side,y+2,-side,rng.choice([0,1]),rng.random()<0.4)

# Two climbing colonies leave the arrow slits and most of the stone exposed.
branch([(38,146),(40,137),(38,128),(41,118),(40,108),(42,98),(40,87),(42,79),(40,68)],0.97,True)
branch([(40,133),(46,128),(49,120),(54,116),(57,108)],0.84)
branch([(41,117),(35,112),(36,103),(34,98)],0.9)
branch([(41,99),(47,94),(51,88),(57,86),(63,80)],0.90)
branch([(41,84),(48,79),(54,77),(59,73)],0.90)
branch([(41,76),(37,72),(36,66)],0.8)
branch([(48,94),(52,98),(54,102)],0.8)
branch([(51,89),(55,91),(58,94)],0.8)
branch([(47,129),(52,131),(55,136)],0.65)
branch([(82,145),(85,137),(84,130),(87,120),(86,111),(89,102),(87,95)],0.9,True)
branch([(86,121),(80,117),(80,109),(77,103)],0.85)
branch([(87,111),(92,108),(94,102)],0.9)
branch([(84,134),(79,132),(75,128),(75,122)],0.8)
branch([(85,140),(91,143),(92,149),(89,153)],0.8)
branch([(80,117),(74,115),(70,117)],0.7)

# Short runners spread on the lower facade and over the arch's outer stones.
branch([(33,218),(35,209),(34,201),(36,194),(34,185),(35,178),(39,170),(44,167),(50,165)],0.9,True)
branch([(35,201),(30,196),(30,189)],0.82)
branch([(35,181),(30,176),(31,170),(33,165)],0.85)
branch([(39,172),(43,176),(44,180)],0.86)
branch([(44,167),(49,170),(54,170),(59,172),(62,176)],0.8)
branch([(87,215),(90,207),(88,197),(91,187),(88,179),(91,170),(93,164)],0.93,True)
branch([(90,206),(94,202),(98,200)],0.85)
branch([(90,188),(85,183),(86,176)],0.8)
branch([(90,174),(96,176),(99,179)],0.8)
branch([(88,197),(84,199),(84,205)],0.8)
# Fuller ivy patches break up the runners; sparse tips still reveal the masonry.
def ivy_leaf(x,y,s=1,bright=False):
    shape=[(x,y+2),(x-2*s,y),(x-2*s,y-1),(x-s,y-1),
           (x-s,y-3),(x,y-2),(x+2*s,y-3),(x+2*s,y-1),
           (x+3*s,y-1),(x+2*s,y+1)]
    vines.poly([(a+1,b+1) for a,b in shape],VSH)
    vines.poly(shape,LEAFM if bright else LEAFD)
    vines.line(x,y+1,x+s,y-2,LEAFL if bright else LEAFM)
    vines.set(x-s,y-1,LEAFL if bright else LEAFM)
    if bright:
        vines.set(x+s,y-2,'#7a9477')

for x,y,s,b in [
    (40,72,-1,False),(44,77,1,True),(40,81,-1,True),
    (46,83,1,False),(37,86,-1,True),(42,88,1,True),
    (39,94,-1,False),(43,96,1,True),(37,99,-1,True),
    (40,104,-1,True),(36,108,-1,False),(41,112,1,True),
    (38,119,-1,False),(42,125,1,True),(39,130,-1,True),
    (49,90,1,True),(53,86,1,True),(50,96,1,False),
    (46,123,-1,True),(50,120,1,False),(54,117,1,True),
    (86,111,1,True),(84,115,-1,False),(88,120,1,False),
    (81,118,-1,True),(86,127,1,True),(82,132,-1,False),
    (85,137,1,True),(81,142,-1,True),(90,146,1,False),
    (35,208,-1,False),(36,198,1,True),(33,188,-1,True),
    (36,177,-1,True),(40,171,1,True),(46,168,1,False),
    (89,211,-1,True),(89,201,-1,True),(92,191,1,False),
    (88,185,-1,True),(91,173,1,False)
]:
    ivy_leaf(x,y,s,b)
branch([(54,77),(62,74),(68,73),(70,76),(70,81)],0.75)
branch([(62,74),(63,69),(66,67)],0.65)
output.blit(vines,0,0)

# A small, stepped halo illuminates the doorway around the staff head.
glow = new_canvas(144,256,name='staff_aura')
for radius,col in [(9,'#8ed8cf0c'),(7,'#8ed8cf16'),(5,'#8ed8cf29'),(3,'#9df2e956')]:
    glow.circle(64,183,radius,col)
output.blit(glow,0,0)

# Mage seen from behind, entering the arch. The boots are at different depths.
DARK='#202a32'
DEEP='#303443'
SHADE='#414252'
MID='#555568'
LIGHT='#6e7181'
RIM='#8ba5a8'
output.ellipse(52,219,9,2,'#263e3e')
output.line(46,220,56,220,'#314b49')
# Right boot is already over the threshold; left boot is still trailing.
output.poly([(54,210),(57,210),(56,215),(54,216),(52,215)],DARK)
output.line(54,214,56,214,'#5f655f')
output.poly([(47,212),(50,213),(49,217),(47,220),(44,219),(45,217)],DARK)
output.line(45,219,47,219,'#777b76')
output.set(47,216,'#57545b')
# Full cloak: a forward lean and an uneven, trailing hem.
output.poly([(48,192),(54,192),(58,196),(58,203),(59,211),(57,215),(52,214),(49,217),(43,216),(44,211),(45,202),(45,197)],DARK)
output.poly([(48,194),(53,194),(56,197),(55,202),(57,212),(53,213),(49,216),(44,215),(46,207),(46,199)],SHADE)
output.poly([(49,195),(52,195),(51,201),(50,207),(48,213),(45,214),(47,205),(47,199)],MID)
output.poly([(53,197),(55,198),(54,204),(56,211),(54,212),(52,206)],DEEP)
output.line(49,201,47,210,LIGHT)
output.line(47,210,46,213,LIGHT)
output.line(51,204,50,212,'#5e6073')
output.line(54,212,57,212,'#646a7b')
output.line(44,216,48,217,'#333542')
# Rear shoulder mantle, left arm beneath it, right arm reaching to the staff.
output.poly([(47,193),(53,192),(57,194),(59,197),(58,200),(53,198),(49,199),(45,198),(45,196)],DEEP)
output.poly([(47,193),(53,193),(56,195),(57,197),(52,197),(49,198),(46,196)],MID)
output.line(46,194,49,193,LIGHT)
output.poly([(56,195),(58,196),(59,200),(61,201),(61,204),(57,203),(55,199)],DARK)
output.poly([(56,196),(57,197),(58,201),(60,202),(58,202),(56,200)],MID)
output.line(58,200,60,201,RIM)
# The closed back of the hood, its seam, and its pointed fold make the orientation explicit.
output.poly([(49,184),(52,183),(55,186),(56,190),(54,194),(51,196),(47,193),(46,189),(47,186)],DARK)
output.poly([(49,185),(52,184),(54,187),(54,191),(51,194),(48,192),(47,189)],MID)
output.poly([(52,185),(54,187),(54,191),(51,194),(50,192),(52,189)],SHADE)
output.line(49,186,48,188,LIGHT)
output.line(48,188,48,191,LIGHT)
output.line(52,185,53,188,'#737b89')
output.line(53,188,52,191,'#697183')
output.set(51,193,'#7c8796')
# The wooden staff has a hooked metal crown around a floating, pale crystal.
output.line(60,217,63,193,'#263b3d')
output.line(61,217,64,192,'#6b6b58')
output.line(62,211,64,191,'#a09b76')
output.line(63,197,64,188,'#b2bc92')
output.line(63,192,61,188,'#626f62')
output.line(61,188,61,184,'#93afa1')
output.line(64,190,67,186,'#91aea0')
output.line(67,186,67,183,'#b5cfb2')
output.set(63,191,'#d1cea0')
# Right hand wraps around the staff at waist height.
output.rect(60,201,3,2,'#8e9180')
output.set(62,201,'#c1baa0')
output.set(60,202,'#66736c')
output.set(61,200,'#a0aa99')
# Cyan crystal and crisp light motes.
output.poly([(64,178),(66,181),(66,184),(64,187),(62,184),(62,181)],'#4ea5a9')
output.poly([(64,179),(65,181),(65,184),(64,185),(63,183),(63,181)],'#a7e6dd')
output.line(64,180,64,184,'#effae5')
output.set(63,182,'#d5fff0')
output.set(60,180,'#85bfbc')
output.set(68,179,'#b7ddd0')
output.set(69,185,'#8ac3be')
output.set(63,175,'#6da4a5')
# A few cool reflected edges on the mage and doorway.
output.line(55,188,55,190,'#90b8ba')
output.set(56,195,'#8aa6ac')
output.line(57,196,58,198,'#7d979e')
output.line(64,195,64,198,'#76a4a1')
output.line(61,214,64,214,'#5d817b')

# Show the two boots clearly at different depths under the moving cloak.
output.poly([(53,214),(56,214),(56,216),(54,217),(52,216)],'#273039')
output.line(54,216,56,216,'#6f7168')
output.poly([(46,216),(49,216),(48,219),(46,220),(44,219)],'#282b33')
output.line(44,219,46,219,'#6c6869')
output.set(48,217,'#535362')

view(output,scale=3,margin=0)
view(output.select(28,161,49,63).preview(),scale=6,margin=0)
save('vine_tower_mage',output)
finish(output)
