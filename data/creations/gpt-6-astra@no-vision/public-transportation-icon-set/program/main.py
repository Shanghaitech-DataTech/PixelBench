# Four public-transport icons in a shared pixel-art tile system.
c = new_canvas(64, 64, '#E8F0ED', name='Transit icons')

INK = '#203244'
PANEL = '#F8FAF4'
EDGE = '#C7D6D4'
TEAL = '#35A89A'
GLASS = '#A9DCD5'
PALE = '#E0F2E8'
GOLD = '#F2BC58'
PURPLE = '#7567C5'
LILAC = '#C7BDF0'
ORANGE = '#E28D52'
SKIN = '#F1C784'
GREEN = '#57A77D'

# Matched, softly rounded square frames.
def tile(x, y):
    pts = [(x+2,y),(x+26,y),(x+28,y+2),(x+28,y+26),
           (x+26,y+28),(x+2,y+28),(x,y+26),(x,y+2)]
    c.poly([(a+1,b+1) for a,b in pts], '#D5E0DC')
    c.poly(pts, PANEL)
    c.poly(pts, EDGE, fill=False)

tile(2, 2)
tile(33, 2)
tile(2, 33)
tile(33, 33)

# BUS — front-facing city bus, with a broad divided windscreen.
bus = [(12,7),(20,7),(23,10),(23,22),(21,24),(11,24),(9,22),(9,10)]
c.poly(bus, INK)
c.poly([(12,9),(20,9),(21,10),(21,22),(20,23),(12,23),(11,22),(11,10)], TEAL)
# side wheels, tucked into the dark body outline
c.rect(8,18,2,4,INK)
c.rect(23,18,2,4,INK)
# destination panel and glass
c.rect(13,9,6,1,GOLD)
c.rect(12,11,9,5,INK)
c.rect(13,12,7,3,GLASS)
c.rect(16,12,1,3,INK)
# front bumper, lamps, and grille
c.rect(12,17,2,2,GOLD)
c.rect(19,17,2,2,GOLD)
c.rect(15,18,3,2,INK)
c.rect(14,21,5,1,PALE)

# SUBWAY — compact railcar front with a luminous divided window and track.
train = [(43,7),(52,7),(55,10),(55,21),(53,24),(42,24),(40,21),(40,10)]
c.poly(train, INK)
c.poly([(43,9),(52,9),(53,10),(53,21),(52,23),(43,23),(42,21),(42,10)], PURPLE)
c.rect(44,10,8,6,INK)
c.rect(45,11,6,4,LILAC)
c.rect(48,11,1,4,INK)
c.rect(43,17,10,3,PALE)
c.rect(44,18,2,1,GOLD)
c.rect(50,18,2,1,GOLD)
c.rect(46,18,4,2,INK)
# track bed and sleepers
c.rect(42,25,12,1,INK)
for x in (43,47,51):
    c.rect(x,26,2,1,INK)

# BICYCLE — two matching wheels, spokes, and a sturdy orange frame.
for cx in (10,24):
    c.circle(cx,52,5,INK)
    c.circle(cx,52,4,PANEL)
# spoke lines and hubs
for cx in (10,24):
    c.line(cx,48,cx,56,EDGE)
    c.line(cx-4,52,cx+4,52,EDGE)
    c.line(cx-3,49,cx+3,55,EDGE)
    c.line(cx-3,55,cx+3,49,EDGE)
    c.circle(cx,52,1,INK)
# dark under-stroke then orange highlights makes the frame read clearly at 1x
# main triangle
def frame_line(x0,y0,x1,y1):
    c.line(x0,y0,x1,y1,INK)
    c.line(x0,y0+1,x1,y1+1,INK)
    c.line(x0,y0,x1,y1,ORANGE)
frame_line(10,52,17,52)
frame_line(17,52,14,45)
frame_line(14,45,10,52)
frame_line(14,45,21,45)
frame_line(21,45,24,52)
frame_line(17,52,24,52)
# seat, stem and handlebars
c.rect(12,43,5,1,INK)
c.rect(13,43,3,1,ORANGE)
frame_line(21,45,22,42)
c.rect(21,41,4,1,INK)
c.rect(22,41,2,1,ORANGE)
c.circle(17,52,1,GOLD)

# PEDESTRIAN — a walking figure in a green jacket, with clear limbs.
# trailing arm is placed behind the torso
c.line(43,46,40,50,INK)
c.line(44,46,41,51,INK)
c.line(50,46,53,49,INK)
c.line(49,46,52,50,INK)
c.circle(40,51,1,SKIN)
c.circle(53,50,1,SKIN)
# head, hair and face
c.circle(47,40,3,INK)
c.circle(47,41,2,SKIN)
c.rect(44,37,6,2,INK)
c.set(45,39,INK)
c.set(49,39,INK)
# jacket silhouette and inset
c.poly([(44,44),(49,44),(51,46),(50,51),(43,51),(42,47)], INK)
c.poly([(45,45),(48,45),(49,47),(48,50),(44,50),(44,47)], GREEN)
c.line(46,45,46,50,PALE)
# moving legs, dark trousers, and small shoe blocks
c.poly([(44,50),(47,50),(46,54),(43,57),(41,57),(42,54)], INK)
c.poly([(48,50),(50,50),(51,54),(54,56),(53,58),(50,57),(47,54)], INK)
c.rect(40,57,4,1,INK)
c.rect(52,57,3,1,INK)

print(c.stats_text())
print(c.matrix_text(region=(0,0,31,31)))
finish(c)
