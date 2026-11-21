# Compact neighborhood laundromat, drawn at its native 64-pixel resolution.
result = new_canvas(64, 64, '#c4d8df', name='Neighborhood laundromat')
c = result
P = {
 'ink':'#263b51', 'deep':'#182e43', 'steel':'#64889e', 'rim':'#93b3c4',
 'edge':'#adc6d0', 'body':'#dce8e9', 'white':'#f3f8ed', 'lit':'#e9f4f2',
 'wall':'#d0e2e4', 'shade':'#a8c3ce', 'tile':'#b4cbd2', 'floor':'#91aebb',
 'floorlight':'#acc5ce', 'seam':'#7e9eaf', 'blue':'#38627f', 'glass':'#467f99',
 'gleam':'#a6dce5', 'green':'#76bcae', 'mint':'#c3e1cc', 'amber':'#e9be77',
 'coral':'#cd8586', 'rose':'#eeb3a3', 'cloth':'#f3dfc2', 'wood':'#d5bd97',
 'woodshade':'#9d8877', 'basket':'#719eac', 'basketlight':'#bbd9d9'
}
def rect(x,y,w,h,key): c.rect(x,y,w,h,P.get(key,key))
def line(x,y,X,Y,key): c.line(x,y,X,Y,P.get(key,key))
# Room shell, cool wall tiles, and the receding tiled floor.
rect(0,0,64,3,'ink')
rect(0,3,3,46,'steel')
rect(3,3,58,45,'wall')
rect(61,3,3,47,'shade')
line(61,3,61,48,'rim')
line(3,3,60,3,'lit')
for x in [15,31,47]: line(x,4,x,16,'#c1d7dd')
line(3,8,60,8,'#c1d7dd')
rect(0,48,64,16,'floorlight')
rect(0,48,64,2,'steel')
line(3,50,60,50,'edge')
# Broad tile shapes and restrained perspective joints.
c.poly([(1,51),(17,51),(12,57),(0,57)],P['tile'])
c.poly([(32,51),(46,51),(50,57),(32,57)],P['tile'])
c.poly([(12,58),(32,58),(32,64),(7,64)],P['tile'])
c.poly([(51,58),(63,58),(63,64),(57,64)],P['tile'])
line(0,57,63,57,'seam')
for a,b in [(6,0),(19,8),(32,32),(45,57),(58,63)]: line(a,50,b,63,'seam')
line(0,63,63,63,'steel')
# Fluorescent ceiling fixture, white centre and icy reflector.
rect(8,2,37,4,'steel')
rect(9,2,35,3,'gleam')
rect(10,2,33,2,'white')
line(11,5,42,5,'lit')
# Painted sign and a simple clock.
c.text(5,9,'LAUNDRY',P['blue'])
c.circle(54,10,6,P['shade'])
c.circle(54,9,5,P['ink'])
c.circle(54,9,4,P['white'])
c.set(54,6,P['steel']); c.set(51,9,P['steel']); c.set(57,9,P['steel']); c.set(54,12,P['steel'])
line(54,7,54,9,'ink'); line(54,9,56,10,'ink')
# Dark gaps distinguish the eight independent machines.
rect(3,17,57,32,'ink')
rect(4,32,55,1,'deep')

def washer(x,y,n):
    # Individual cabinet and its one-pixel bevels.
    rect(x,y,13,15,'steel')
    rect(x,y,12,14,'body')
    line(x,y,x+11,y,'white')
    line(x,y+1,x,y+13,'lit')
    line(x+11,y+1,x+11,y+13,'edge')
    line(x+1,y+13,x+10,y+13,'rim')
    # Detergent drawer, knob and lit payment/status display.
    rect(x+2,y+2,3,1,'rim')
    c.set(x+5,y+2,P['steel'])
    rect(x+8,y+1,3,3,'ink')
    rect(x+9,y+2,2,1,'green' if n%3 else 'amber')
    line(x+1,y+4,x+10,y+4,'edge')
    # Circular steel ring and the recessed blue drum.
    c.circle(x+6,y+9,5,P['rim'])
    c.circle(x+6,y+8,4,P['ink'])
    c.circle(x+6,y+8,3,P['blue'])
    c.poly([(x+4,y+7),(x+7,y+6),(x+8,y+7),(x+8,y+9),(x+5,y+10),(x+4,y+9)],P['glass'])
    # A small, different bundle of laundry in every window.
    colors = [('green','mint'),('coral','rose'),('steel','gleam'),('woodshade','cloth')]
    a,b=colors[n%4]
    line(x+4,y+10,x+7,y+10,a)
    c.set(x+7,y+9,P[b]); c.set(x+8,y+9,P[a]); c.set(x+5,y+10,P[b])
    # Window reflection and short rim glint.
    line(x+4,y+7,x+5,y+6,'gleam')
    c.set(x+4,y+8,P['edge'])
    c.set(x+9,y+8,P['white'])
    line(x+4,y+12,x+7,y+12,'lit')
    c.set(x+10,y+8,P['steel'])

for row,y in enumerate([18,34]):
    for i,x in enumerate([4,18,32,46]): washer(x,y,i+row*2)
# Ground contact shadows under furniture.
rect(35,60,27,3,'seam')
rect(9,60,18,2,'seam')
# Folding table, with braced slender metal legs and a warm laminate top.
rect(37,54,2,8,'ink'); rect(38,55,1,6,'rim')
rect(58,54,2,8,'ink'); rect(58,55,1,6,'rim')
line(39,59,57,59,'steel')
c.poly([(37,50),(59,50),(62,53),(34,53)],P['ink'])
c.poly([(38,50),(58,50),(60,52),(36,52)],P['wood'])
line(38,50,58,50,'cloth')
rect(35,53,27,2,'woodshade')
line(35,53,61,53,'cloth')
line(35,55,61,55,'ink')
# Folded towels on top.
rect(40,49,11,3,'blue')
rect(40,49,10,2,'green')
line(41,49,49,49,'mint')
rect(42,47,9,2,'coral')
line(43,47,50,47,'rose')
line(43,49,49,49,'mint')
# A little detergent bottle at the end of the table.
rect(54,47,4,5,'steel')
rect(54,47,3,4,'lit')
rect(55,46,2,1,'blue')
rect(54,49,3,1,'green')
# Basket of soft laundry: dark interior, flared rim, and open weave.
c.ellipse(17,54,9,3,P['ink'])
c.ellipse(17,54,7,2,P['blue'])
c.poly([(10,53),(11,50),(14,50),(16,53),(20,51),(23,53),(22,56),(11,56)],P['cloth'])
line(11,51,13,51,'white')
c.poly([(15,54),(17,51),(20,51),(22,54),(20,56)],P['coral'])
line(17,52,19,52,'rose')
c.poly([(8,54),(26,54),(24,61),(11,61)],P['ink'])
c.poly([(9,55),(25,55),(23,60),(12,60)],P['basket'])
line(9,54,25,54,'basketlight')
line(11,55,24,55,'lit')
for y in [57,59]:
    for x in [12,15,18,21]: rect(x,y,2,1,'blue')
line(12,60,23,60,'basketlight')
# Metal basket handles peek around the rim.
line(8,53,8,55,'steel'); line(26,53,26,55,'steel')
view(result, scale=8, margin=0)
save('neighborhood-laundromat', result)
finish(result)
