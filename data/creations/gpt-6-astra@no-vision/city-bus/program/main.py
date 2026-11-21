# Modern low-floor city bus. Native-size, hard-edged pixel clusters.
result = new_canvas(64, 32, name="city_bus")
c = result
P = {
    'ink':'#142b38', 'rubber':'#263b48', 'tirelit':'#3b5260',
    'steel':'#647f8a', 'rim':'#b6cbd0', 'shine':'#edf1df',
    'white':'#d9e3d8', 'shade':'#afc4bf', 'trim':'#849fa5',
    'glass':'#294b60', 'glasslow':'#365e70', 'reflection':'#517b8a',
    'glint':'#789ba4', 'deepglass':'#1c394b',
    'teal':'#298e91', 'tealshade':'#236b76', 'mint':'#73cebd',
    'grille':'#1c525f', 'black':'#10232e',
    'amber':'#f4c26a', 'dimamber':'#b98143',
    'red':'#d96c62', 'redlight':'#f3ae83', 'lamp':'#fff2c4'
}
for key,value in list(P.items()):
    P[key] = c.color(value, name=key)
def rect(x,y,w,h,col):
    c.rect(x,y,w,h,P[col])
def line(x0,y0,x1,y1,col):
    c.line(x0,y0,x1,y1,P[col])
def poly(points,col):
    c.poly(points,P[col])
def dot(x,y,col):
    c.set(x,y,P[col])

# Shallow roof-mounted climate/battery housing, tucked into the roof line.
poly([(17,6),(17,5),(19,3),(37,3),(40,5),(40,6)],'steel')
line(20,3,36,3,'shine')
rect(19,4,19,2,'shade')
line(20,4,35,4,'white')
for x in range(23,35,3):
    line(x,5,x+1,5,'steel')

# Rounded coachwork and its continuous one-pixel perimeter.
poly([(5,6),(55,6),(58,7),(60,9),(61,12),(61,24),(59,26),
      (4,26),(2,24),(2,10),(3,8)], 'ink')
poly([(5,7),(55,7),(57,8),(59,10),(60,12),(60,23),(58,25),
      (4,25),(3,23),(3,10),(4,8)], 'white')
line(6,7,54,7,'shine')
line(3,11,3,18,'shade')
line(4,8,55,8,'white')
dot(56,8,'shine')

# Turquoise skirt, pale belt rail, and the darker underbody.
rect(3,20,57,5,'teal')
line(4,20,59,20,'mint')
line(4,24,59,24,'tealshade')
line(5,25,58,25,'ink')
line(4,19,59,19,'shine')

# Continuous dark window band, with individually glazed panes.
rect(4,9,54,9,'ink')
poly([(58,9),(59,10),(60,12),(60,18),(58,18)],'ink')

def window(x,y,w,h):
    rect(x,y,w,h,'glass')
    rect(x,y+h-3,w,3,'glasslow')
    line(x,y,x+w-1,y,'reflection')
    # Broad oblique reflected sky, not noisy single-pixel texture.
    poly([(x+1,y+1),(min(x+4,x+w-1),y+1),(x+1,y+5),(x,y+5)],'reflection')
    line(x,y+h-1,x+w-1,y+h-1,'deepglass')
window(5,10,6,7)
window(13,10,9,7)
window(35,10,7,7)
window(43,10,8,7)
# Uprights between the large passenger windows.
line(12,9,12,17,'trim')
line(23,9,23,18,'shade')
line(34,9,34,18,'shade')
line(42,9,42,17,'trim')
line(52,9,52,24,'white')

# Rear engine-access panel and quiet coachwork seams.
rect(5,20,4,4,'tealshade')
for y in (21,23):
    line(5,y,8,y,'grille')
line(22,20,22,24,'tealshade')
rect(36,21,4,3,'tealshade')
rect(37,21,3,2,'teal')
dot(39,21,'mint')

# Both passenger doors extend down to a low step, with split glass leaves.
# The aft door is wider; the forward door sits ahead of the front wheel.
def door(x,w):
    rect(x,9,w,16,'ink')
    split = x + w//2
    rect(x+1,10,split-x-1,13,'glasslow')
    rect(split+1,10,x+w-split-2,13,'glass')
    line(x+1,10,split-1,10,'glint')
    line(split+1,10,x+w-2,10,'reflection')
    line(x+1,11,x+1,16,'reflection')
    line(split+1,11,split+1,15,'reflection')
    # A short diagonal in each lower pane catches the same light.
    line(x+1,21,min(split-1,x+3),19,'reflection')
    line(split+1,21,x+w-2,20,'glasslow')
    line(x+1,18,x+w-2,18,'ink')
    dot(split-1,19,'shade')
    dot(split+1,19,'shade')
    line(x+1,23,x+w-2,23,'deepglass')
    line(x+1,24,x+w-2,24,'trim')

door(24,10)
door(53,7)
# Thin front windscreen beyond the entrance pillar.
line(60,13,60,17,'glasslow')
dot(60,13,'glint')

# Side-facing electronic destination/route panel, drawn as actual 3x5 LEDs.
rect(40,9,12,7,'black')
for x0,glyph in [(41,["111","001","111","100","111"]),
                 (45,["101","101","111","001","001"])]:
    for yy,row in enumerate(glyph):
        for xx,v in enumerate(row):
            if v == '1': dot(x0+xx,10+yy,'amber')
line(49,11,50,11,'dimamber')
line(49,13,50,13,'amber')

# Body-coloured lips around the two open wheel wells.
def wheel(cx):
    poly([(cx-6,26),(cx-6,23),(cx-5,23),(cx-5,21),
          (cx-3,21),(cx-3,20),(cx+3,20),(cx+3,21),
          (cx+5,21),(cx+5,23),(cx+6,23),(cx+6,26)],'shade')
    line(cx-3,20,cx+3,20,'shine')
    poly([(cx-5,26),(cx-5,23),(cx-4,23),(cx-4,22),
          (cx-3,22),(cx-3,21),(cx+3,21),(cx+3,22),
          (cx+4,22),(cx+4,23),(cx+5,23),(cx+5,26)],'black')
    # Nine-pixel tyres; five-pixel brushed-metal hubs.
    pixels = ["..OOOOO..", ".OTTTTTO.", "OTTSSSTTO",
              "OTSLLLSTO", "OTSLHLSTO", "OTSLLLSTO",
              "OTTSSSTTO", ".OTTTTTO.", "..OOOOO.."]
    colours={'O':'ink','T':'rubber','S':'steel','L':'rim','H':'tirelit'}
    for yy,row in enumerate(pixels):
        for xx,v in enumerate(row):
            if v != '.': dot(cx-4+xx,21+yy,colours[v])
    dot(cx-1,24,'shine')
    line(cx-2,22,cx+1,22,'tirelit')
    line(cx-2,28,cx+2,28,'black')
wheel(15)
wheel(47)

# Road equipment: compact lamps, dark bumpers, marker and wing mirror.
rect(2,19,2,4,'ink')
rect(3,19,1,3,'red')
dot(3,19,'redlight')
rect(2,24,5,2,'steel')
line(3,24,6,24,'trim')
line(3,26,7,26,'ink')
rect(59,19,2,4,'ink')
rect(59,20,2,2,'lamp')
dot(59,22,'amber')
rect(58,24,3,2,'steel')
line(58,24,60,24,'trim')
dot(60,25,'ink')
line(36,19,37,19,'amber')
line(59,18,60,18,'amber')
line(60,10,62,10,'ink')
rect(62,11,1,3,'ink')
dot(62,11,'trim')

print(c.stats_text())
print(c.matrix_text(region=(0,2,63,30)))
save('city_bus', result)
finish(result)
