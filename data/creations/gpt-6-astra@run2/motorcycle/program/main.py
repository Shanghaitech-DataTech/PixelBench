import math
result = new_canvas(128,128,name='motorcycle')
c=result
ink='#101217'
black='#181b21'
dark='#242931'
mid='#353c46'
light='#4a5561'
silver='#98a5af'
bright='#d4dce0'
white='#f0f3ef'
red='#cf2639'
redhi='#fa4a50'
def poly(p,col): c.poly(p,col)
def line(a,b,col): c.line(*a,*b,col)
# Tires, alloy rims and fine radial spokes
for cx,cy in [(28,91),(101,91)]:
    c.circle(cx,cy,21,ink)
    c.circle(cx,cy,19,black)
    c.circle(cx,cy,17,dark)
    c.circle(cx,cy,15,'#080c12')
    c.circle(cx,cy,14,silver)
    c.circle(cx,cy,12,ink)
    # ten white spokes, paired angled metal edges
    for i in range(10):
        a=i*math.pi/5
        x=cx+round(12*math.cos(a)); y=cy+round(12*math.sin(a))
        xx=cx+round(4*math.cos(a+.25)); yy=cy+round(4*math.sin(a+.25))
        c.line(xx,yy,x,y,bright)
    c.circle(cx,cy,7,'#56616c')
    c.circle(cx,cy,5,silver)
    for i in range(6):
        a=i*math.pi/3
        c.set(cx+round(5*math.cos(a)),cy+round(5*math.sin(a)),dark)
    c.circle(cx,cy,3,mid)
    c.circle(cx,cy,1,bright)
    # Broken sidewall glints
    c.path(f'M {cx-17} {cy-5} Q {cx-14} {cy-16} {cx-5} {cy-18}',light,fill=False)
    c.path(f'M {cx+7} {cy+17} L {cx+13} {cy+13}',mid,fill=False)
# far fork and inner mechanical mass
poly([(87,54),(91,54),(104,90),(101,94)],dark)
poly([(37,59),(68,57),(80,75),(69,94),(43,93),(34,80)],ink)
# Rear suspension and chain
poly([(28,87),(49,78),(59,82),(31,95),(26,94)],ink)
poly([(29,88),(48,81),(53,84),(29,92)],silver)
line((32,89),(47,84),bright)
line((28,96),(58,92),dark)
line((29,97),(56,94),silver)
line((29,84),(49,78),light)
# Suspension spring
line((37,63),(47,81),ink)
line((39,63),(49,79),silver)
for y in range(65,78,3):
    x=39+(y-65)//2
    line((x-2,y),(x+4,y+1),red)
# silver trellis tube frame
for a,b in [((35,59),(58,66)),((58,66),(79,57)),((35,59),(46,79)),((46,79),(58,66)),((46,79),(72,83)),((58,66),(72,83)),((72,83),(79,57))]:
    c.line(*a,*b,light)
    c.line(a[0],a[1]-1,b[0],b[1]-1,silver)
    c.set(*a,bright)
# engine block and cylinder fins
poly([(52,65),(67,63),(73,76),(66,87),(49,86),(45,76)],dark)
poly([(54,65),(63,64),(68,74),(54,77)],light)
for y in [67,70,73]: line((54,y),(65,y-1),silver)
c.circle(55,82,10,ink)
c.circle(55,82,8,silver)
c.circle(55,82,6,'#66737f')
c.path('M 50 84 Q 48 78 54 77 L 58 77',bright,fill=False)
c.circle(55,82,3,light)
for x,y in [(55,75),(62,82),(55,89),(48,82)]: c.set(x,y,bright)
# Exhaust pipe and underslung silencer
c.path('M 67 76 Q 80 85 72 94 L 44 97',ink,fill=False)
c.path('M 68 77 Q 78 86 71 92 L 45 95',silver,fill=False)
poly([(32,84),(50,91),(48,98),(27,91),(25,87)],ink)
poly([(30,85),(46,91),(45,95),(28,90)],light)
line((30,85),(46,91),bright)
poly([(26,85),(30,86),(29,91),(25,90)],silver)
line((26,86),(26,89),ink)
# upswept rear tail fairing
poly([(10,52),(18,51),(38,55),(49,62),(43,68),(26,64),(13,58)],ink)
poly([(13,53),(27,54),(41,58),(45,62),(31,61),(18,57)],mid)
line((15,53),(29,55),light)
poly([(12,55),(21,57),(19,60),(13,58)],red)
line((13,55),(19,57),redhi)
# pillion and rider seat
poly([(20,50),(30,51),(40,55),(48,55),(53,60),(41,61),(31,56),(21,54)],ink)
line((22,50),(30,51),light)
line((35,55),(45,57),mid)
# tank silhouette with faceted highlights
poly([(44,55),(50,46),(61,42),(71,43),(81,51),(80,61),(68,67),(54,63)],ink)
poly([(46,54),(52,47),(62,44),(70,45),(77,51),(74,57),(56,59)],mid)
poly([(50,50),(60,46),(69,46),(73,49),(60,48)],light)
poly([(47,56),(58,59),(75,55),(77,60),(65,64),(54,61)],dark)
line((59,44),(65,44),silver)
# fork: bright telescopic front tubes
poly([(84,55),(89,54),(103,90),(99,93)],ink)
poly([(86,57),(89,57),(100,85),(97,86)],silver)
line((87,58),(97,83),bright)
poly([(97,80),(100,79),(104,91),(100,94),(97,90)],light)
line((99,82),(102,89),silver)
c.circle(101,91,2,bright)
c.set(101,91,mid)
# front fender
poly([(84,79),(89,72),(99,69),(109,72),(115,79),(112,81),(105,76),(95,75),(87,80)],ink)
poly([(86,77),(91,73),(100,71),(108,74),(111,77),(103,74),(95,74)],mid)
line((91,73),(99,71),red)
# Windscreen angled up and back, cockpit
poly([(79,49),(73,34),(78,35),(88,43),(92,50)],ink)
poly([(77,37),(80,39),(87,46),(84,46)],dark)
line((74,34),(79,36),light)
# handlebars and right mirror
line((74,48),(81,45),silver)
line((71,47),(77,48),ink)
line((83,44),(87,38),light)
poly([(85,36),(91,36),(93,38),(90,40),(85,39)],ink)
line((86,36),(90,36),mid)
# broad side fairing, nose wedge and belly
poly([(77,48),(87,47),(99,53),(108,61),(107,67),(97,71),(87,78),(77,94),(62,95),(66,88),(68,73),(64,65)],ink)
poly([(79,50),(87,49),(97,54),(104,60),(94,60),(85,65),(70,68),(68,64)],mid)
poly([(80,51),(88,51),(98,56),(88,54),(77,58)],light)
poly([(72,70),(86,65),(96,62),(103,64),(93,70),(84,80),(75,92),(65,92),(70,81)],dark)
poly([(83,69),(91,65),(94,66),(83,78),(76,88),(73,87)],mid)
# red slash running along the fairing
poly([(68,64),(78,61),(91,59),(99,60),(87,62),(77,66),(71,69)],red)
line((76,63),(88,60),redhi)
poly([(65,91),(75,90),(80,85),(78,91),(75,94),(63,94)],red)
# headlamp and dark air intake
poly([(99,57),(105,61),(103,63),(96,62)],ink)
line((99,58),(104,61),white)
line((98,60),(102,62),silver)
poly([(76,70),(84,67),(79,73),(74,75)],ink)
line((76,70),(82,68),light)
poly([(75,76),(79,74),(75,80),(72,81)],ink)
# exposed fasteners and peg
for x,y in [(72,59),(87,56),(70,86),(77,89),(39,61)]: c.set(x,y,silver)
poly([(41,78),(44,77),(49,87),(46,89)],light)
line((43,79),(47,85),bright)
line((43,88),(49,88),ink)
line((42,87),(48,87),silver)
c.shift(0,-8)
view(c)
save('motorcycle',c)
finish(result)
