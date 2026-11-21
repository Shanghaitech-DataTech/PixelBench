# Subway platform, a compact side-on city vignette.
result = new_canvas(64, 64, '#111d30', name='subway_platform')
c = result
ink='#101a2b'; deep='#1c2c42'; steel='#465e70'; light='#9fb7bc'; pale='#d8e6dd'
# Ceiling and long converging architectural bands.
c.rect(0,0,64,3,'#263b50')
c.rect(0,3,64,10,'#1b2b40')
c.line(0,12,63,10,'#536b78')
c.line(0,13,63,11,'#0d192b')
c.rect(0,3,3,7,'#385164')
c.rect(39,2,25,2,'#819c9f')
c.rect(41,2,23,1,'#d5e3d5')
# Suspended station signs, neutral public wayfinding.
c.rect(5,2,1,3,steel); c.rect(33,2,1,3,steel)
c.rect(4,4,32,8,'#0b182a')
c.text(6,5,'EAST','#dbe8d8')
c.line(30,8,34,8,'#e9b85f'); c.line(32,6,34,8,'#e9b85f'); c.line(32,10,34,8,'#e9b85f')
c.rect(46,5,14,7,'#d3a04e'); c.text(48,5,'02','#182b3a')
# Tunnel and far track.
c.rect(0,14,64,29,'#0c192b')
c.rect(0,38,64,5,'#172338')
# Arriving train: pale flank, dark windows, sloping cab at the right.
c.poly([(0,16),(50,16),(55,18),(60,24),(61,34),(57,38),(0,38)],'#778f9e')
c.line(0,16,49,16,'#c6d8d5')
c.rect(0,18,49,2,'#a7bdbe')
c.rect(0,21,49,9,'#284856')
for x in [2,18,34]:
    c.rect(x,21,12,8,'#345d68')
    c.rect(x+1,22,10,2,'#668e92')
    c.line(x+2,27,x+9,27,'#4b7882')
    c.rect(x+12,20,3,11,'#9bafb3')
c.poly([(50,20),(54,21),(58,26),(58,29),(50,29)],'#173444')
c.line(51,21,54,22,'#70999e')
c.line(52,23,56,27,'#416b78')
c.rect(0,31,50,4,'#b7c9c4')
c.rect(0,35,57,2,'#d99750')
c.line(0,37,56,37,'#435c70')
c.rect(57,31,3,2,'#f5df9d')
c.set(58,30,'#d1b984')
# Horizontal speed streaks and window reflections.
c.line(0,19,10,19,'#d5e0d7')
c.line(0,24,7,24,'#90b5b5')
c.line(16,25,24,25,'#70969e')
c.line(0,33,14,33,'#e0e6cf')
c.line(25,33,39,33,'#d8dfd0')
c.line(1,40,32,40,'#395267')
# Screen-door glass, framing, handles and warning marks.
c.rect(0,42,64,3,'#142639')
c.rect(0,15,64,1,'#657e8a')
for x in [2,22,42,62]:
    c.rect(x,16,2,27,'#324c5e')
    c.line(x,17,x,41,'#80989e')
    c.rect(x,40,2,3,'#a1b5b6')
for x in [12,32,52]:
    c.line(x,17,x,41,'#557987')
    c.line(x+1,17,x+1,41,'#1d3b4b')
    c.rect(x-2,30,1,4,'#d1d9c7')
    c.rect(x+3,30,1,4,'#d1d9c7')
for x in [6,16,26,36,46,56]:
    c.rect(x,34,3,1,'#e4c978')
# Subtle reflections slant across the glass.
for x in [6,26,46]:
    c.line(x,18,x+3,21,'#83a4aa')
    c.line(x,19,x+2,21,'#83a4aa')
c.line(0,42,63,42,'#9cabad')
# Platform: strong horizontal tactile edge and angled tile seams.
c.rect(0,45,64,19,'#4e6275')
c.rect(0,45,64,3,'#c49b55')
c.line(0,45,63,45,'#f0cf7c')
for x in range(1,64,4): c.set(x,47,'#796a4c')
c.line(0,49,63,49,'#73818b')
c.line(0,57,63,57,'#627587')
c.line(22,50,10,63,'#394f65')
c.line(45,50,48,63,'#394f65')
c.line(62,50,63,53,'#394f65')
# Ground shadows anchor furniture and passengers.
c.ellipse(14,55,11,2,'#34495e')
c.ellipse(36,58,6,1,'#34495e')
c.ellipse(53,60,8,1,'#34495e')
# Bench, horizontal slatted back and cantilever supports.
c.rect(4,43,21,2,'#202e3f')
c.rect(5,43,19,1,'#b68b67')
c.rect(5,46,19,2,'#88664f')
c.line(5,46,23,46,'#cfaa7d')
c.rect(4,49,22,3,'#23354a')
c.rect(5,49,20,1,'#c49b71')
c.rect(7,52,2,4,'#1b2b3e'); c.rect(22,52,2,4,'#1b2b3e')
# Passenger one: seated, leaning toward a phone.
c.rect(10,36,4,2,ink)
c.rect(9,38,5,4,'#c98d69'); c.rect(9,37,4,2,'#382b32')
c.set(14,39,'#e2ac7e'); c.rect(11,41,2,2,'#c98d69')
c.poly([(9,42),(13,42),(15,46),(18,46),(18,48),(13,48),(11,46),(11,49),(8,49),(8,44)],'#dbad58')
c.line(9,43,9,47,'#f2ca75')
c.rect(16,44,3,2,'#c98d69'); c.rect(18,42,2,3,ink); c.set(18,42,'#9fc3c5')
c.poly([(9,49),(16,49),(17,51),(16,55),(14,55),(14,52),(9,51)],'#243448')
c.rect(13,55,5,2,'#101e30')
c.rect(10,52,2,3,'#32455a'); c.rect(9,55,4,1,ink)
# Passenger two: standing with a tote, rust coat.
c.rect(33,31,5,2,ink)
c.rect(32,33,6,3,'#322a31')
c.rect(34,33,4,5,'#d6a17f'); c.set(38,35,'#e8b58b')
c.rect(33,33,2,3,'#322a31'); c.rect(35,38,2,1,'#b97e66')
c.poly([(33,38),(37,38),(39,42),(39,49),(32,49),(31,43)],'#b45f54')
c.line(33,39,32,45,'#e18d70'); c.line(37,40,38,46,'#793e45')
c.rect(33,49,2,7,'#18283c'); c.rect(37,49,2,7,'#23374a')
c.rect(32,56,4,2,ink); c.rect(37,56,4,2,ink)
c.line(39,45,40,48,'#e3b18b')
c.rect(40,47,3,3,'#26384a',False); c.rect(39,49,5,5,'#9ba48c'); c.line(40,50,40,53,'#ced0aa')
# Passenger three: walking, backpack and separated stride.
c.rect(51,34,5,2,'#151e2c')
c.rect(51,36,5,4,'#b98168'); c.rect(50,35,3,3,'#202537')
c.set(56,37,'#dba080'); c.rect(53,40,2,1,'#b98168')
c.rect(48,42,4,7,'#162b3c'); c.line(48,43,48,47,'#78989a')
c.poly([(52,40),(55,41),(56,45),(55,50),(50,50),(50,44)],'#73a7a7')
c.line(52,41,51,46,'#acd0be')
c.line(54,42,57,46,'#73a7a7'); c.line(57,46,59,45,'#d59d7b')
c.poly([(51,50),(54,50),(51,55),(49,58),(47,57),(49,54)],'#1b2c40')
c.poly([(53,49),(55,49),(56,54),(59,57),(57,59),(53,55)],'#2d4054')
c.rect(46,58,4,2,ink); c.rect(57,58,4,2,ink)
# Consolidate nearby shades to keep the final sprite within its palette budget.
from collections import Counter
counts = Counter(c.get(x,y) for y in range(64) for x in range(64))
colours = {p['index']:p['rgba'] for p in c.palette()}
remap = {i:i for i in counts}
while len(counts) > 80:
    ids = list(counts)
    def cost(pair):
        a,b = pair
        rgb_a,rgb_b = colours[a],colours[b]
        distance = sum(w*(rgb_a[k]-rgb_b[k])**2 for k,w in enumerate((0.3,0.5,0.2)))
        return distance * (min(counts[a], counts[b]) ** 0.3)
    a,b = min(((a,b) for n,a in enumerate(ids) for b in ids[n+1:]),key=cost)
    if counts[a] > counts[b]: a,b = b,a
    for i in remap:
        if remap[i] == a: remap[i] = b
    counts[b] += counts.pop(a)
for y in range(64):
    for x in range(64):
        c.set(x,y,remap[c.get(x,y)])
view(result)
finish(result)
