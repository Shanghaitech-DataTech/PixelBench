import random
import math

result = input_canvas.copy(name='output')
vines = new_canvas(144, 256, name='wall_ivy')
rng = random.Random(19)

stem_dark = '#263d34'
stem_mid = '#486246'
leaf_dark = '#2c4938'
leaf_mid = '#436346'
leaf_light = '#5b7852'
leaf_glint = '#72875d'

# Main rooted stems, with lateral runners following the stone courses.
stems = [
    [(36,220),(38,210),(36,200),(38,189),(35,177),(37,165),(35,153),(37,140),(36,128),(40,115),(38,102),(41,90),(40,77),(44,64),(44,53)],
    [(37,165),(43,164),(47,160),(53,160),(60,163),(65,167),(69,173)],
    [(38,189),(42,181),(43,173),(47,169)],
    [(36,200),(33,194),(34,185)],
    [(37,140),(44,136),(48,130),(54,128),(58,122)],
    [(40,115),(47,111),(54,113),(60,108),(65,106)],
    [(40,77),(47,78),(53,73),(59,75),(64,70)],
    [(44,64),(50,60),(51,52),(56,46),(56,34)],
    [(51,52),(59,54),(65,53),(70,57),(73,64)],
    [(89,57),(87,65),(88,74),(84,82),(85,90),(81,99),(83,108),(80,115)],
    [(87,65),(80,66),(75,69),(69,68)],
    [(84,82),(78,83),(72,88),(67,86)],
    [(85,90),(88,96),(87,102)],
]

for points in stems:
    for (x0,y0),(x1,y1) in zip(points,points[1:]):
        vines.line(x0+1,y0+1,x1+1,y1+1,'#243a32')
        vines.line(x0,y0,x1,y1,stem_mid)

# Small pointed leaves alternate along each woody runner.
def leaf(x, y, direction, size=1):
    dx,dy = direction
    px,py = -dy,dx
    tip=(x+dx*3,y+dy*3)
    shape=[(x,y),(x+dx+px,y+dy+py),(x+dx*2+px,y+dy*2+py),tip,(x+dx*2-px,y+dy*2-py),(x+dx-px,y+dy-py)]
    vines.poly([(a+1,b+1) for a,b in shape],stem_dark)
    vines.poly(shape,leaf_dark)
    vines.line(x+dx,y+dy,x+2*dx,y+2*dy,leaf_mid)
    vines.set(x+dx+px,y+dy+py,leaf_light)
    if rng.random()<0.28:
        vines.set(x+2*dx,y+2*dy,leaf_glint)

for index, points in enumerate(stems):
    distance=0
    for (x0,y0),(x1,y1) in zip(points,points[1:]):
        length=max(abs(x1-x0),abs(y1-y0))
        for i in range(length):
            if distance % 4 == 0:
                t=i/max(1,length)
                x=round(x0+(x1-x0)*t)
                y=round(y0+(y1-y0)*t)
                side=1 if (distance//4+index)%2 else -1
                if abs(y1-y0)>abs(x1-x0):
                    direction=(side,-1 if rng.random()<0.7 else 0)
                else:
                    direction=(-1 if rng.random()<0.3 else 0,side)
                leaf(x,y,direction)
                if index in (0,1,7,8,9) and rng.random()<0.45:
                    leaf(x+side,y+1,(-side,-1))
            distance+=1

# A handful of wider ivy sprays make the covering read as foliage, not lines.
for x,y in [(38,155),(40,137),(42,111),(42,87),(45,64),(50,55),(56,45),(59,54),(85,74),(83,86),(83,101),(43,164),(50,160),(64,165)]:
    leaf(x,y,(-1,-1))
    leaf(x+1,y+2,(1,-1))
    leaf(x,y+2,(-1,0))

result = flatten([result,vines], name='ivy_tower')
# Keep the original entrance lantern visible in front of the climbing ivy.
for y in range(184,196):
    for x in range(31,39):
        original = input_canvas.get(x,y)
        if original in (80,81,82,83,84,85,86):
            result.set(x,y,original)

# Discrete low-alpha rings preserve the stone texture in the staff's light.
glow = new_canvas(144,256,name='staff_light')
glow.circle(62,185,10,'#7cebd109')
glow.circle(62,185,7,'#7fffe214')
glow.circle(62,185,5,'#80ffe82a')
glow.circle(62,185,3,'#b3fff44b')
glow.ellipse(55,217,9,2,'#78d9c414')
result = flatten([result,glow], name='lit_tower')

# A rear-view silhouette: closed hood, broad back, split swinging hem.
c = result
c.ellipse(54,220,8,2,'#1b302f')
c.line(49,220,58,221,'#203735')
# The advanced foot is higher inside the doorway; the other is trailing.
c.poly([(51,212),(54,212),(54,217),(52,218),(49,218),(49,216)],'#1c252b')
c.line(50,217,52,217,'#566164')
c.poly([(56,214),(59,215),(59,220),(57,221),(54,220),(55,218)],'#1d242b')
c.line(56,220,58,220,'#586263')

# Hood and shoulder outline.
c.poly([(53,188),(56,189),(58,192),(58,195),(60,197),(60,203),(61,207),(60,213),(61,216),(57,217),(53,215),(48,217),(45,216),(47,210),(47,204),(48,198),(50,195),(50,192)],'#222a34')
# The cloak is seen entirely from the back, with no face opening.
c.poly([(51,196),(55,195),(58,197),(59,203),(58,208),(60,215),(56,215),(53,213),(49,215),(47,215),(49,207),(49,200)],'#494557')
c.poly([(50,198),(51,198),(51,205),(49,211),(48,214),(47,215),(48,208)],'#666077')
c.poly([(54,198),(57,198),(57,205),(58,211),(58,215),(55,214),(54,207)],'#535063')
c.poly([(52,199),(54,199),(53,205),(53,212),(51,214),(51,209)],'#363646')
c.line(55,203,56,211,'#686276')
c.set(56,212,'#776f81')
c.line(48,215,50,214,'#82716f')
c.line(57,216,60,215,'#82716f')
c.line(50,201,50,205,'#777183')
# Hood volume and its downward seam establish the back of the head.
c.poly([(53,189),(55,190),(57,193),(57,196),(54,198),(51,196),(51,192)],'#575266')
c.line(53,190,52,192,'#827a8b')
c.line(52,193,52,195,'#6b647a')
c.line(55,191,56,194,'#464254')
c.line(56,195,54,197,'#343643')
c.set(54,196,'#6d677a')
c.line(50,197,53,199,'#353542')
c.line(54,199,57,197,'#2d333f')

# Right sleeve reaches forward to grasp the upright staff.
c.poly([(58,197),(60,198),(60,200),(62,200),(62,203),(59,204),(57,202)],'#353a49')
c.line(59,198,59,200,'#7a7c89')
c.line(60,201,61,201,'#65727c')
# A crooked wooden shaft with a brighter edge facing its crystal.
c.line(62,188,62,204,'#342f2c')
c.line(62,204,63,219,'#342f2c')
c.line(63,190,63,207,'#837b60')
c.line(63,208,64,218,'#676c56')
c.line(62,191,62,198,'#a2bda2')
c.set(63,218,'#9dbba4')
c.rect(61,200,3,2,'#84786a')
c.line(62,200,63,200,'#b5baa0')
c.set(61,202,'#424447')
# Three dark metal prongs cradle the luminous stone.
c.line(60,186,61,189,'#69776a')
c.line(64,186,63,189,'#849b81')
c.line(61,189,63,189,'#aac6ab')
c.poly([(62,181),(64,184),(63,187),(61,188),(60,185),(61,183)],'#4b9f94')
c.poly([(62,182),(63,184),(63,186),(61,187),(61,184)],'#94edcf')
c.line(62,183,62,186,'#e1fff0')
c.set(62,184,'#f0fff6')
c.set(60,184,'#b7fbe1')
# Sparse sharp glints, with no antialiasing.
c.set(58,183,'#82bcab')
c.set(65,181,'#73b1a4')
c.set(65,188,'#8dc5b4')

# Cool reflected light catches only the staff-facing side of the cloth.
c.set(56,191,'#7b9392')
c.line(57,193,57,195,'#71878b')
c.set(58,197,'#82928f')
c.line(59,198,59,199,'#7e938e')
c.set(60,200,'#96a99a')
c.set(58,206,'#66717a')
# Break the hem above the lifted foot and carry a soft fold into the step.
c.line(49,214,50,213,'#736a7c')
c.set(51,213,'#494454')
c.set(50,218,'#66706f')
c.set(51,218,'#3e4d50')
c.set(57,221,'#4c565b')

view(result, scale=4, margin=0)
view(result.select(29,157,45,69).preview(), scale=8, margin=0)
finish(result)
