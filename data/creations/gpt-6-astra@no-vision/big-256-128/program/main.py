import random
random.seed(21)
out = input_canvas.copy(name='output')
pal = input_canvas.palette()
# Recast the original mountain textures in a dark volcanic palette.
lookup={}
for p in pal:
 r,g,b,a=p['rgba']; lum=(r*0.26+g*0.56+b*0.18)
 if lum<18: col='#100d1b'
 elif lum<40: col='#201523'
 elif lum<65: col='#34202d'
 elif lum<90: col='#4a2934'
 elif lum<120: col='#66333a'
 elif lum<155: col='#84423e'
 elif lum<195: col='#a75949'
 elif lum<225: col='#c47659'
 else: col='#dc9871'
 lookup[p['index']]=col
for y in range(128):
 for x in range(256): out.set(x,y,lookup[input_canvas.get(x,y)])
# Blood moon, suspended by an iron chain.
out.circle(128,29,25,'#55232e')
out.circle(128,29,23,'#b53e3e')
out.circle(127,28,21,'#d55748')
out.circle(124,25,16,'#df6850')
# blocky lunar mottling
for x,y,w,h in [(110,20,7,3),(115,16,9,2),(131,13,7,3),(136,20,8,4),(111,29,8,3),(119,33,11,4),(137,30,6,3),(128,22,5,2),(116,40,6,2),(137,38,5,2),(124,11,5,2)]:
 out.rect(x,y,w,h,'#c94d43')
for x,y,w in [(113,23,4),(133,17,5),(120,27,6),(140,26,4),(125,38,6),(109,33,3)]: out.rect(x,y,w,1,'#e87a58')
out.rect(126,0,5,7,'#19121e')
for y in [0,4,8]:
 out.rect(126,y,5,4,'#241723',fill=False)
 out.set(128,y+1,'#a44b42')
# Distant, serrated city silhouette.
dark='#19111d'; edge='#38202a'; stone='#4a2931'; light='#8f433b'; glow='#ef8b4e'
out.poly([(52,91),(55,76),(58,76),(58,67),(62,63),(66,67),(66,77),(71,77),(71,69),(75,69),(75,65),(80,65),(80,72),(87,72),(87,62),(92,57),(97,62),(97,70),(104,70),(104,64),(151,64),(151,70),(158,70),(158,62),(163,57),(168,62),(168,72),(175,72),(175,65),(180,65),(180,69),(184,69),(184,77),(190,77),(190,67),(194,63),(198,67),(198,76),(201,76),(205,91)],dark)
# fortress body
out.poly([(80,103),(80,76),(91,76),(91,62),(100,62),(100,54),(108,54),(108,48),(148,48),(148,54),(156,54),(156,62),(165,62),(165,76),(176,76),(176,103)],'#21151f')
out.rect(99,60,58,37,'#35202a')
out.rect(103,62,50,34,'#48262e')
# central roof and tall spire
out.poly([(108,54),(114,46),(118,46),(118,39),(128,24),(138,39),(138,46),(142,46),(148,54)],'#1a111c')
out.poly([(121,41),(128,29),(135,41)],'#56262d')
out.line(128,24,128,16,'#22121b')
out.poly([(129,18),(140,20),(130,22)],'#8c3033')
out.rect(116,48,24,27,'#251620')
out.rect(119,49,18,23,'#4a2930')
out.rect(122,55,12,18,'#25151d')
out.poly([(124,60),(128,54),(132,60),(132,70),(124,70)],'#c45138')
out.rect(127,59,2,11,'#f49a53')
# flanking towers with steep pointed roofs
for x in [87,153]:
 out.rect(x,59,16,38,'#271720')
 out.rect(x+2,62,12,31,'#503038')
 out.poly([(x-3,62),(x+8,42),(x+19,62)],'#1a111c')
 out.poly([(x+2,58),(x+8,47),(x+14,58)],'#702e32')
 out.line(x+8,42,x+8,36,'#20121c')
 out.rect(x+5,67,6,12,'#22131c')
 out.poly([(x+6,69),(x+8,65),(x+10,69),(x+10,76),(x+6,76)],'#e46b42')
 out.rect(x+7,82,3,6,'#1d131d')
# outer turrets
for x in [70,172]:
 out.rect(x,77,15,25,'#24151f'); out.rect(x+2,79,11,18,'#503038')
 out.poly([(x-3,78),(x+7,61),(x+17,78)],'#1b121c')
 out.poly([(x+2,75),(x+7,66),(x+12,75)],'#6d3033')
 out.rect(x+5,82,5,9,'#1b121b'); out.rect(x+7,83,1,6,'#f28a4b')
# battlements and walls
out.rect(83,91,90,14,'#301c25')
for x in range(84,171,7): out.rect(x,88,4,5,'#301c25')
out.rect(88,96,80,8,'#43252d')
# gate and doorway
out.poly([(115,107),(115,91),(119,85),(128,81),(137,85),(141,91),(141,107)],'#17121a')
out.poly([(119,106),(119,92),(122,88),(128,85),(134,88),(137,92),(137,106)],'#a34232')
out.poly([(122,106),(122,93),(128,88),(134,93),(134,106)],'#27151c')
out.line(128,89,128,105,'#bc5539')
for x in [124,131]: out.rect(x,95,1,8,'#874032')
# stone details and narrow windows
for x,y in [(105,78),(145,78),(109,87),(141,87),(94,91),(159,91)]:
 out.rect(x,y,2,5,'#dc7045')
for x,y,w in [(104,74,6),(134,77,7),(110,80,4),(142,70,5),(91,84,4),(161,84,4),(98,96,8),(149,98,8)]: out.rect(x,y,w,1,'#704039')
# rocky island / approach, preserving original surrounding mountain textures
out.poly([(71,105),(85,101),(110,103),(146,103),(171,101),(185,106),(176,111),(159,113),(150,119),(104,119),(96,113),(80,111)],'#211720')
out.poly([(105,120),(113,109),(143,109),(151,120),(161,127),(95,127)],'#39222a')
for y,x,w in [(110,115,26),(113,112,32),(117,108,40),(121,104,48),(125,100,56)]:
 out.rect(x,y,w,1,'#a55a48'); out.rect(x+2,y+1,w-4,1,'#5b3435')
# glowing lava seams at the foot of the fortress
for x,y,w in [(61,110,14),(77,114,12),(157,114,13),(180,109,13),(44,119,17),(195,120,18)]:
 out.rect(x,y,w,1,'#9b3e35'); out.rect(x+3,y+1,max(2,w-6),1,'#df6740')
print(out.stats_text())
finish(out)
