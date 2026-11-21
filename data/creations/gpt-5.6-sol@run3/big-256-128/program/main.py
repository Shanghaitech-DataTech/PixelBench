from pixelbench_api import *
import random

random.seed(13)
out = input_canvas.copy(name="output")

# Tight demonic palette.
night = out.color("#090812", "night")
void = out.color("#120b18", "void")
plum = out.color("#241126", "plum")
cloud = out.color("#40172d", "cloud")
crimson = out.color("#721c32", "crimson")
red = out.color("#a82735", "blood")
scarlet = out.color("#db3b32", "scarlet")
ember = out.color("#ff7337", "ember")
moon_dark = out.color("#7d1629", "moon_shadow")
moon = out.color("#c72d35", "blood_moon")
moon_hi = out.color("#ef5342", "moon_glow")
stone0 = out.color("#100f18", "stone_black")
stone1 = out.color("#201824", "stone_dark")
stone2 = out.color("#352334", "stone_mid")
stone3 = out.color("#593044", "stone_lit")
ash = out.color("#76505a", "ash")
chain = out.color("#49323d", "chain")
chain_hi = out.color("#8a4a50", "chain_highlight")

# Replace the hopeful alpine sky with layered storm bands.
out.rect(0, 0, 256, 128, night)
out.poly([(0,11),(22,6),(44,14),(67,7),(92,15),(111,9),(137,13),(158,5),(181,13),(202,7),(228,12),(255,4),(255,41),(0,41)], void)
out.poly([(0,26),(25,20),(45,29),(67,20),(91,30),(111,22),(137,27),(159,20),(181,29),(205,19),(230,27),(255,18),(255,53),(0,53)], plum)
out.poly([(0,43),(23,34),(48,42),(70,34),(94,44),(118,36),(144,43),(168,33),(192,45),(218,35),(255,43),(255,62),(0,62)], cloud)
out.poly([(0,51),(30,45),(57,52),(83,43),(107,53),(132,46),(159,53),(186,44),(215,53),(255,47),(255,65),(0,65)], crimson)
# Ragged black clouds.
for pts in [
 [(0,18),(18,14),(31,18),(47,15),(62,21),(52,26),(24,24),(0,28)],
 [(154,14),(173,9),(188,15),(210,11),(233,17),(255,12),(255,27),(231,24),(208,28),(181,23),(159,26)],
 [(0,45),(30,39),(58,46),(82,41),(105,48),(94,55),(64,52),(34,57),(0,53)],
 [(174,45),(195,38),(219,45),(239,40),(255,43),(255,56),(226,54),(201,58),(178,53)]
]: out.poly(pts, void)
# Crimson horizon and rain-like slash texture.
out.rect(0,58,256,5,red)
# Uneven blood-lit cloud shelf, broken up to avoid a flat horizon band.
out.poly([(0,48),(19,45),(37,50),(55,46),(73,52),(91,47),(110,54),(129,49),(149,53),(168,46),(187,52),(207,47),(228,53),(256,46),(256,63),(0,63)],crimson)
out.poly([(0,56),(24,51),(46,57),(68,52),(88,59),(111,53),(132,58),(155,52),(178,59),(202,53),(226,58),(256,52),(256,64),(0,64)],red)
for x in range(2,256,4):
    if random.random() < 0.62:
        out.set(x, 57 + random.randrange(0,6), scarlet)
for _ in range(120):
    x=random.randrange(0,256); y=random.randrange(4,61)
    col=random.choice([cloud,crimson,red,plum])
    out.line(x,y,x-random.choice([1,2,3]),y+random.choice([1,2]),col)

# The hanging blood moon and its blocky halo.
out.circle(128,25,24,cloud)
out.circle(128,25,21,moon_dark)
out.circle(128,25,18,moon)
out.circle(125,22,14,moon_hi)
out.dither(112,11,30,29,[moon,moon_hi],pattern="bayer4")
out.rect(116,14,4,3,scarlet); out.rect(135,17,5,4,moon_dark)
out.rect(123,31,7,4,red); out.rect(111,24,5,5,moon_dark)
# Heavy chains suspending the moon from the unseen ceiling.
def chain_run(points):
    for i in range(len(points)-1):
        x0,y0=points[i]; x1,y1=points[i+1]
        out.line(x0,y0,x1,y1,chain)
        out.line(x0+1,y0,x1+1,y1,chain_hi)
    for x,y in points[::2]:
        out.rect(x-1,y-1,4,3,chain)
        out.set(x,y,chain_hi)
chain_run([(96,0),(98,5),(96,10),(99,15),(101,20),(105,24)])
chain_run([(160,0),(158,5),(160,10),(157,15),(155,20),(151,24)])
# Central vertical chain piercing the moon.
for y in range(0,44,6):
    out.rect(126,y,5,4,chain)
    out.rect(127,y,2,2,chain_hi)
out.line(128,3,128,47,chain_hi)

# Distant volcanic mountains.
out.poly([(0,77),(17,65),(28,73),(45,58),(62,73),(78,63),(92,75),(108,60),(126,75),(143,62),(159,73),(180,57),(199,72),(218,60),(237,73),(255,57),(255,128),(0,128)],stone1)
out.poly([(0,85),(25,69),(48,82),(70,67),(91,84),(112,69),(137,86),(159,68),(185,85),(207,69),(230,85),(255,71),(255,128),(0,128)],stone2)
for x in range(8,250,13):
    y=random.randrange(68,88)
    out.line(x,y,x+random.randrange(3,10),y-6,stone3)
    if random.random()<.55: out.set(x+2,y-2,scarlet)

# Castle mass: cliff and stepped fortress body.
out.poly([(64,113),(72,102),(83,98),(88,87),(101,84),(104,69),(115,67),(120,56),(128,50),(136,57),(140,69),(151,72),(154,86),(168,90),(174,103),(189,111),(197,128),(56,128)],stone0)
out.poly([(77,112),(86,98),(97,96),(99,79),(112,76),(116,61),(127,55),(138,64),(141,78),(157,80),(159,97),(174,101),(184,116)],stone1)
out.poly([(91,111),(100,93),(109,92),(111,73),(121,71),(124,59),(130,57),(136,67),(136,85),(151,87),(152,103),(166,108),(170,120)],stone2)

# Towers helper, with crenellations, slit windows and spires.
def tower(x,y,w,h,spire=10):
    out.rect(x,y,w,h,stone1)
    out.rect(x+2,y,w-4,h,stone2)
    out.line(x+2,y+3,x+2,y+h-1,stone3)
    out.rect(x-2,y-3,w+4,4,stone0)
    for bx in range(x-2,x+w+1,4): out.rect(bx,y-6,3,4,stone1)
    out.poly([(x-1,y-6),(x+w//2,y-6-spire),(x+w,y-6)],stone0)
    out.line(x+w//2,y-7-spire,x+w//2,y-2-spire,chain_hi)
    for wy in range(y+6,y+h-3,9):
        out.rect(x+w//2-1,wy,3,5,ember)
        out.set(x+w//2-1,wy,scarlet)

tower(102,68,13,39,11)
tower(142,70,14,38,13)
tower(118,54,21,55,18)
tower(88,82,11,27,8)
tower(162,85,10,26,9)
# Main horned crown and central gate.
out.poly([(118,54),(112,42),(121,48),(128,36),(135,48),(144,41),(138,57)],stone0)
out.poly([(121,54),(128,40),(135,54)],stone3)
out.rect(121,89,16,27,stone0)
out.path("M123 116 V99 Q128 90 135 99 V116 Z",void,fill=True)
out.rect(127,99,3,17,red)
out.set(128,98,ember)
# Architectural highlights and localized masonry courses.
for x0,x1,y in [(104,114,76),(103,114,90),(119,138,70),(119,138,84),(119,138,96),(143,156,83),(143,157,97),(89,99,94),(162,172,96)]:
    out.line(x0,y,x1,y,stone3)
    for bx in range(x0+2,x1,5): out.set(bx,y,stone0)
for _ in range(110):
    x=random.randrange(82,177); y=random.randrange(60,115)
    if out.get(x,y) in (stone1,stone2,stone3):
        out.rect(x,y,random.choice([1,2,3]),1,random.choice([stone0,stone3,ash]))
# Infernal windows on the keep.
for x,y in [(108,75),(108,88),(148,79),(149,92),(124,66),(132,66),(124,78),(132,78),(94,92),(166,95)]:
    out.rect(x,y,3,5,scarlet); out.set(x+1,y+1,ember)

# Bat-wing buttresses make the castle read as the Demon King's seat.
out.poly([(102,78),(82,67),(89,84),(68,81),(92,97),(105,96)],stone0)
out.poly([(154,79),(174,66),(168,84),(190,80),(164,98),(152,96)],stone0)
out.line(84,69,101,91,stone3); out.line(172,69,155,91,stone3)

# Foreground black valley, glowing river of blood, and bridge.
out.poly([(0,99),(20,93),(42,100),(63,94),(78,104),(98,110),(116,114),(139,114),(157,109),(180,105),(199,97),(220,101),(239,91),(255,96),(255,128),(0,128)],stone0)
out.poly([(105,128),(113,117),(123,112),(132,113),(143,119),(153,128)],red)
out.poly([(116,128),(121,118),(128,115),(137,119),(144,128)],scarlet)
out.dither(120,118,22,10,[scarlet,ember],pattern="checker")
out.line(72,109,184,109,stone3)
out.line(75,107,181,107,ash)
for x in range(77,182,8): out.line(x,106,x,111,stone1)

# Dead trees framing the keep.
def dead_tree(x,ground,h,flip=1):
    out.line(x,ground,x,ground-h,stone0); out.line(x+1,ground,x+1,ground-h,chain)
    y=ground-h+7
    out.line(x,y,x-7*flip,y-7,stone0); out.line(x-6*flip,y-6,x-10*flip,y-4,stone0)
    out.line(x,y+7,x+8*flip,y,stone0); out.line(x+7*flip,y+1,x+12*flip,y-3,stone0)
    out.line(x,y+13,x-6*flip,y+6,stone0)
dead_tree(20,113,28,1); dead_tree(235,107,32,-1); dead_tree(47,112,17,1); dead_tree(215,111,19,-1)
# Foreground spikes and ember motes.
for x in range(2,255,7):
    h=random.randrange(2,10)
    out.poly([(x,125),(x+2,125-h),(x+4,125)],stone1)
for _ in range(42):
    x=random.randrange(10,246); y=random.randrange(61,108)
    out.set(x,y,random.choice([red,scarlet,ember]))

# Black vignette corners.
out.poly([(0,0),(34,0),(20,8),(13,26),(0,35)],stone0)
out.poly([(256,0),(222,0),(237,8),(244,26),(256,35)],stone0)
out.poly([(0,128),(0,105),(12,111),(22,128)],stone0)
out.poly([(256,128),(256,104),(244,111),(234,128)],stone0)

view(out, scale=3, margin=0)
finish(out)
