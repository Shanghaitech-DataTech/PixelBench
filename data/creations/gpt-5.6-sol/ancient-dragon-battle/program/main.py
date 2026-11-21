from pixelbench_api import *

# Ancient dragon battle, 256x256 pixel art
c = new_canvas(256, 256, "#171522", name="ancient-dragon-battle")

# Compact hand-tuned palette
sky0="#24172d"; sky1="#4b2132"; sky2="#873532"; sky3="#d05a32"; sky4="#f28b3b"; sun="#ffd36a"
ink="#171522"; deep="#211b29"; mountain="#362438"; mountain2="#4b2938"; haze="#70403d"
stone0="#272631"; stone1="#383743"; stone2="#4d4b55"; stone3="#69646a"; mortar="#1e1d27"
fire0="#8f2423"; fire1="#e44724"; fire2="#ff8c2a"; fire3="#ffd45b"; smoke0="#29252f"; smoke1="#44323a"; smoke2="#684039"
steel0="#343947"; steel1="#626a76"; steel2="#a6a7a1"; gold="#c28b3b"; red="#8d2630"; red2="#c74235"; leather="#5a3629"; wood="#4a2d26"; wood2="#76452d"; ash="#b67a52"

# Dramatic striped sunset sky
c.rect(0,0,256,35,sky0)
c.rect(0,35,256,28,sky1)
c.rect(0,63,256,26,sky2)
c.rect(0,89,256,25,sky3)
c.rect(0,114,256,31,sky4)
c.rect(0,145,256,18,"#c75a36")
# Pixel cloud bands
c.poly([(0,35),(34,35),(34,31),(67,31),(67,36),(99,36),(99,42),(0,42)],"#302037")
c.poly([(126,48),(154,48),(154,43),(188,43),(188,48),(222,48),(222,54),(256,54),(256,62),(126,62)],"#642a37")
c.poly([(0,76),(27,76),(27,70),(58,70),(58,75),(93,75),(93,82),(0,82)],"#6d2c38")
c.poly([(170,81),(201,81),(201,75),(235,75),(235,80),(256,80),(256,87),(170,87)],"#a44136")
# Sun sinking behind the mountains
c.circle(194,104,23,sun)
c.rect(171,104,47,5,"#f5aa48")
c.rect(176,113,37,4,"#ee8a3d")
# sun glints
for x,y,w in [(224,119,20),(145,123,25),(206,132,31),(155,139,15)]: c.rect(x,y,w,2,"#f7a045")

# Distant mountain ranges
c.poly([(0,131),(19,112),(29,119),(47,97),(70,123),(82,115),(104,139),(126,111),(143,127),(160,101),(179,128),(199,116),(218,133),(238,110),(256,127),(256,166),(0,166)],mountain)
c.poly([(0,139),(24,127),(40,136),(63,118),(82,141),(106,128),(129,147),(153,127),(175,142),(205,125),(229,147),(256,134),(256,170),(0,170)],mountain2)
# mountain highlights and snow chips
c.poly([(42,102),(47,97),(53,106),(49,104),(47,110)],"#76504f")
c.poly([(153,108),(160,101),(168,113),(162,110),(159,116)],"#76504f")
c.poly([(232,117),(238,110),(246,121),(240,118),(238,123)],"#76504f")

# Smoke columns behind dragon/castle
c.circle(89,91,15,smoke1); c.circle(83,79,12,smoke1); c.circle(91,68,10,smoke0); c.circle(85,56,7,smoke0)
c.circle(130,106,16,smoke2); c.circle(137,91,13,smoke1); c.circle(132,77,9,smoke0)
c.dither(72,51,28,53,[smoke0,smoke1],"checker")

# Castle mass and towers, dark outlined
c.rect(53,124,132,70,ink)
c.rect(58,129,122,65,stone0)
# Left tower
c.rect(39,112,34,82,ink); c.rect(44,117,24,77,stone1)
c.rect(36,106,10,12,ink); c.rect(48,106,10,12,ink); c.rect(60,106,11,12,ink)
c.rect(40,112,29,7,stone2)
# Right tower
c.rect(168,108,36,86,ink); c.rect(173,114,26,80,stone1)
c.rect(165,102,11,13,ink); c.rect(179,102,10,13,ink); c.rect(193,102,11,13,ink)
c.rect(170,109,31,7,stone2)
# central keep crenellations
for x in [56,77,98,119,140,161]: c.rect(x,117,13,15,ink)
for x in [60,81,102,123,144,165]: c.rect(x,122,9,12,stone1)
c.rect(57,132,122,8,stone2)
# stone blocks
for x,y,w in [(62,145,18),(88,145,24),(120,145,17),(145,145,27),(46,127,18),(46,151,20),(176,124,20),(176,151,21),(62,166,26),(96,161,18),(126,169,22),(154,160,20),(50,177,15)]:
    c.rect(x,y,w,3,stone2)
for x,y,w in [(72,153,12),(102,176,19),(134,151,13),(159,179,16),(47,139,17),(177,137,18)]: c.rect(x,y,w,2,stone3)
# mortar cuts
for y in [154,174]: c.rect(58,y,121,2,mortar)
# arrow slit windows
for x,y in [(51,128),(51,158),(181,126),(181,160),(194,145)]:
    c.rect(x,y,5,12,ink); c.rect(x+2,y+3,2,7,"#e65a27")
# gate arch
c.rect(105,169,27,25,ink); c.circle(118,169,13,ink); c.rect(110,171,17,23,wood)
for x in [113,119,125]: c.rect(x,171,2,23,"#2a2022")

# Fire on battlements and windows
for pts in [((77,132),(82,111),(87,130),(92,116),(96,136)),((139,132),(145,108),(150,126),(155,115),(160,137)),((187,115),(191,91),(196,111),(200,98),(201,120))]:
    a,b,d,e,f=pts
    c.poly([a,b,d,e,f],fire1)
# Flame cores
c.poly([(80,132),(83,118),(87,132),(91,124),(93,136)],fire3)
c.poly([(143,133),(146,117),(150,130),(154,122),(157,137)],fire2)
c.poly([(189,116),(192,101),(196,114),(199,105),(199,119)],fire3)
# ember pixels
for x,y in [(70,103),(76,91),(99,110),(111,92),(121,106),(143,89),(157,100),(204,86),(214,113),(92,99),(166,91),(130,61)]:
    c.rect(x,y,2,2,fire3)

# Knights on ramparts: heads, shields, spears
for x in [69,102,132,162]:
    c.line(x+2,126,x-1,96,ink); c.line(x+3,126,x,97,steel2)
    c.circle(x,129,4,ink); c.circle(x,128,2,steel1)
    c.rect(x-3,132,7,10,ink)
    c.rect(x-2,133,5,8,steel0)
    c.circle(x+5,137,5,ink); c.circle(x+5,137,3,red)
# shield insignia
for x in [74,107,137,167]: c.set(x,137,gold)

# Siege tower at far right
c.poly([(214,135),(244,135),(250,211),(205,211)],ink)
c.poly([(219,140),(239,140),(245,207),(211,207)],wood)
for y in [151,170,190]: c.rect(211,y,34,4,ink)
c.line(215,142,243,207,wood2); c.line(240,142,211,207,wood2)
c.rect(211,126,36,15,ink)
for x in [214,224,234,243]: c.rect(x,122,7,14,ink)
c.rect(216,130,27,7,wood2)
c.circle(215,211,8,ink); c.circle(215,211,4,steel0); c.circle(241,211,8,ink); c.circle(241,211,4,steel0)

# Dragon silhouette: broad wings, serpentine body and long tail
# Back wing
c.poly([(117,61),(92,27),(75,16),(83,42),(55,26),(70,55),(43,48),(70,69),(97,76)],ink)
c.poly([(108,59),(91,34),(81,24),(87,47),(65,35),(76,58),(56,53),(77,67),(98,70)],"#3a202b")
# wing membrane ribs
c.line(108,61,83,42,"#7c3032"); c.line(106,63,70,55,"#7c3032"); c.line(103,67,77,67,"#7c3032")
# Front wing
c.poly([(125,64),(153,28),(183,18),(170,47),(208,32),(184,63),(224,61),(188,78),(151,82)],ink)
c.poly([(133,65),(154,36),(175,24),(165,51),(197,39),(177,65),(211,64),(184,73),(151,77)],"#48232b")
c.line(137,68,165,51,"#8c3432"); c.line(141,72,177,65,"#8c3432"); c.line(147,75,184,73,"#8c3432")
# dragon body and neck
c.poly([(96,65),(108,56),(125,57),(136,66),(153,69),(170,65),(181,69),(174,77),(158,80),(144,89),(127,86),(113,80),(101,81),(91,76)],ink)
c.poly([(101,66),(111,60),(124,61),(135,70),(153,73),(168,69),(174,71),(169,75),(154,76),(142,84),(128,81),(115,75),(103,77),(96,73)],"#55252d")
# neck and head
c.poly([(167,68),(183,58),(198,59),(207,54),(203,64),(214,68),(204,72),(196,80),(181,79),(168,75)],ink)
c.poly([(174,69),(185,62),(198,63),(202,59),(201,66),(208,68),(201,70),(194,76),(181,75)],"#652a30")
# horns, jaw, eye
c.poly([(198,61),(203,50),(205,62)],gold); c.poly([(191,61),(192,52),(196,62)],gold)
c.rect(201,69,10,3,ink); c.set(199,65,fire3); c.set(200,65,"#fff0a0")
# legs and claws
c.poly([(120,79),(115,92),(108,99),(113,101),(121,94),(127,82)],ink)
c.poly([(146,82),(150,96),(158,101),(160,97),(154,91),(153,79)],ink)
for x,y in [(108,99),(114,101),(158,101),(162,98)]: c.line(x,y,x-3,y+4,gold)
# tail curling left
c.path("M104 74 C82 79 67 86 54 80 C43 75 40 68 44 63 C43 72 52 75 61 74 C76 72 85 65 100 67",ink,fill=False)
c.path("M104 75 C83 80 69 86 56 81", "#652a30",fill=False)
# scales/highlights
for x,y in [(111,66),(120,70),(130,74),(140,78),(151,75),(160,73),(181,70)]: c.rect(x,y,3,2,"#9b3b37")

# Arrows streaking through sky
for x,y,dx,dy in [(18,87,18,-7),(27,99,20,-6),(219,91,-18,-5),(229,105,-18,-7),(13,119,19,-4),(235,73,-16,5),(152,45,-12,6)]:
    c.line(x,y,x+dx,y+dy,ink); c.set(x+dx,y+dy,gold)

# Foreground scorched ground
c.poly([(0,190),(28,183),(62,190),(93,185),(124,193),(151,184),(181,192),(211,184),(256,193),(256,256),(0,256)],deep)
c.dither(0,204,256,52,["#211b29","#2e2329"],"checker")
# Fires on field
for x,y in [(31,213),(193,216)]:
    c.poly([(x-7,y),(x-3,y-15),(x,y-7),(x+4,y-20),(x+8,y)],fire1)
    c.poly([(x-3,y),(x,y-11),(x+4,y)],fire3)

# Soldier formation in foreground, alternating depth
soldiers=[(12,203),(29,197),(48,205),(67,198),(86,207),(106,198),(127,207),(148,198),(169,206),(190,198),(212,205),(234,197),
          (3,226),(23,220),(45,229),(66,219),(89,229),(112,219),(136,229),(158,219),(181,229),(205,219),(230,228),(249,218)]
for i,(x,y) in enumerate(soldiers):
    # spear behind body
    c.line(x+1,y+8,x-6,y-28,ink); c.line(x,y+7,x-7,y-28,ash)
    c.poly([(x-9,y-28),(x-5,y-36),(x-3,y-27)],steel2)
    # helmet and plume
    c.circle(x,y,5,ink); c.rect(x-5,y,11,4,ink)
    c.circle(x,y-1,3,steel1); c.rect(x-3,y,7,2,steel2)
    if i%3==0: c.rect(x-1,y-8,3,5,red2)
    # body, legs
    c.poly([(x-5,y+5),(x+5,y+5),(x+7,y+19),(x-7,y+19)],ink)
    c.rect(x-4,y+7,8,11,steel0 if i%2 else red)
    c.line(x-3,y+18,x-5,y+29,ink); c.line(x+3,y+18,x+5,y+29,ink)
    # round shield
    c.circle(x+6,y+10,7,ink); c.circle(x+6,y+10,5,red if i%2 else steel0)
    c.rect(x+5,y+6,2,9,gold); c.rect(x+2,y+9,9,2,gold)

# Foreground commander, larger central silhouette
c.line(128,233,138,194,ink); c.line(129,233,139,194,steel2)
c.poly([(136,195),(140,187),(142,197)],gold)
c.circle(126,218,7,ink); c.circle(126,216,5,steel1); c.rect(119,218,14,4,steel2)
c.poly([(118,223),(132,223),(137,250),(113,250)],ink)
c.poly([(121,225),(130,225),(133,247),(116,247)],red2)
c.circle(137,233,10,ink); c.circle(137,233,8,steel0); c.circle(137,233,3,gold)
# cape blowing left
c.poly([(120,224),(111,228),(99,244),(115,242),(120,250)],red)

# Sparks and ash over the lower scene
for x,y,col in [(18,174,fire2),(28,161,fire3),(76,181,fire1),(93,155,fire2),(117,184,fire3),(151,174,fire2),(188,178,fire3),(222,166,fire1),(239,184,fire2),(15,147,ash),(209,148,ash),(101,119,fire3)]:
    c.rect(x,y,2,2,col)

# Hard dark silhouette edge along ground and a few battlefield rocks
c.line(0,252,255,252,ink)
for x,y,w in [(5,242,13),(54,248,11),(75,239,8),(174,246,12),(218,242,16)]:
    c.poly([(x,y+4),(x+3,y),(x+w-3,y+1),(x+w,y+5)],ink)

view(c, margin=0)
finish(c)
