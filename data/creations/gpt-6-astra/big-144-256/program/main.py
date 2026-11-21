import random, math
result = input_canvas.copy(name='output')
rng = random.Random(27)
# Ivy clings in branching patches, leaving the windows and much of the masonry exposed.
ivy_dark='#253e35'
ivy_mid='#365641'
ivy_light='#4d7052'
ivy_tip='#668365'
stem='#52634a'
def leaf(x,y,side,size=2):
    # Angular, lobed ivy leaves, with a shaded lower edge.
    result.poly([(x,y),(x+side*2,y-2),(x+side*3,y-1),(x+side*4,y-2),(x+side*4,y+1),(x+side*2,y+3)],ivy_dark)
    result.line(x+side,y,x+side*3,y-1,ivy_mid)
    result.set(x+side*2,y,ivy_light)
    if rng.random()<.45: result.set(x+side*3,y-1,ivy_tip)
def vine(points, density=.7):
    for (x,y),(xx,yy) in zip(points,points[1:]):
        result.line(x+1,y+1,xx+1,yy+1,ivy_dark)
        result.line(x,y,xx,yy,stem)
    count=0
    for (x,y),(xx,yy) in zip(points,points[1:]):
        length=max(abs(xx-x),abs(yy-y))
        for j in range(length):
            if count%3==0 and rng.random()<density:
                px=round(x+(xx-x)*j/max(1,length)); py=round(y+(yy-y)*j/max(1,length))
                leaf(px,py,1 if count%2 else -1)
            count+=1
# Main ivy growing up the left side of the cylindrical wall.
vine([(38,144),(40,135),(39,126),(43,118),(44,110),(41,101),(43,92),(49,85),(50,77),(56,69)],.94)
vine([(42,121),(49,117),(53,109),(56,104),(54,96)],.85)
vine([(42,102),(37,97),(37,88),(39,79),(43,73)],.9)
vine([(48,86),(55,86),(60,81),(64,76)],.8)
vine([(40,135),(47,132),(50,126)],.75)
# A smaller curtain descending from the carved cornice on the right.
vine([(83,65),(85,72),(81,78),(83,84),(80,92),(81,99)],.85)
vine([(84,73),(89,79),(88,85)],.85)
vine([(81,86),(74,90),(71,96)],.65)
# Growth framing the entrance, rooted along the foot of the wall.
vine([(79,219),(76,211),(77,204),(73,198),(74,189),(71,182),(74,174),(79,169)],.9)
vine([(75,206),(83,201),(85,193),(87,189)],.82)
vine([(73,183),(67,179),(64,173),(59,170)],.7)
vine([(36,214),(36,207),(37,200),(35,194)],.7)
# Soft pixel-stepped magical light on the stone and doorway.
glow = new_canvas(144,256,name='staff light')
glow.circle(63,190,9,'#73dfc70a')
glow.circle(63,190,6,'#73dfc714')
glow.circle(63,190,4,'#8ef5dc26')
result = flatten([result,glow],name='output lit')
# Mage seen from behind, one foot already across the threshold.
result.ellipse(54,220,10,2,'#233537')
# Walking legs and boots.
result.poly([(51,213),(55,213),(54,219),(51,220),(49,219)],'#242b36')
result.line(51,219,54,219,'#56515d')
result.poly([(56,213),(59,213),(59,220),(57,223),(54,223),(55,220)],'#202a31')
result.line(55,222,57,222,'#6b6268')
# Broad silhouette, flared asymmetrical cloak and narrow shoulders.
result.poly([(52,197),(57,197),(60,201),(60,207),(62,217),(58,218),(54,216),(49,219),(46,217),(49,207),(49,201)],'#262d3d')
result.poly([(52,198),(56,198),(58,202),(58,209),(60,216),(55,215),(50,217),(48,216),(51,204)],'#514e67')
result.poly([(52,201),(54,202),(53,210),(50,216),(48,216)],'#696078')
result.poly([(55,202),(57,203),(57,211),(59,216),(55,214)],'#3d3d53')
result.line(53,206,52,213,'#7b6b85')
result.line(48,217,51,217,'#877887')
# Right sleeve reaches to the staff, hand visible beyond cuff.
result.poly([(58,200),(60,201),(61,205),(63,204),(64,207),(60,209),(58,206)],'#32394b')
result.line(60,203,61,206,'#66647a')
# Rear of hood: closed cloth with a lit rim and a centre fold, no face.
result.poly([(50,197),(50,193),(53,189),(56,190),(59,194),(59,198),(55,201),(51,199)],'#252d3b')
result.poly([(51,196),(52,192),(54,190),(56,192),(57,195),(57,198),(54,199),(51,198)],'#625970')
result.line(54,192,55,196,'#817088')
result.line(55,197,54,199,'#454255')
result.line(58,194,58,197,'#7d9d9d')
result.set(57,192,'#9bb8ab')
# Tall staff planted ahead of the trailing foot.
result.line(63,197,64,220,'#253a39')
result.line(62,196,63,219,'#857452')
result.line(62,198,62,205,'#b6b581')
result.rect(62,205,2,2,'#b9a186')
result.set(63,205,'#e0c6a1')
# Crook/prongs cradle a brilliant crystal.
result.line(62,197,60,193,'#7d9278')
result.line(60,193,61,190,'#a1c8a3')
result.line(63,197,65,193,'#91b99b')
result.set(65,192,'#c1e6b8')
result.poly([(63,186),(65,190),(63,194),(61,190)],'#6ecbb9')
result.line(63,187,63,192,'#e0ffe4')
result.set(62,189,'#f5ffdf')
result.set(64,190,'#b2f4d0')
result.set(59,187,'#6fae9f')
result.set(67,189,'#8ac9b5')
result.set(64,182,'#8ec9b6')
view(result, scale=4, margin=0)
finish(result)
