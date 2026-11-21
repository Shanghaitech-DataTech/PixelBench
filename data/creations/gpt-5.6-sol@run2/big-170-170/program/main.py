import random

random.seed(170)
out = input_canvas.copy(name='output')

# Remove the character silhouette using nearby background tones before rebuilding objects.
out.poly([(70,61),(80,61),(80,94),(73,96),(68,89),(69,73)], '#0a2e3fff')
out.dither(70,63,9,29,['#0a2e3fff','#0b3245ff'],'checker')
out.poly([(73,91),(82,89),(86,99),(80,108),(71,103)], '#0a293aff')

# Reconstruct the vending machine front where the person stood.
# Outer cabinet and recessed illuminated display.
out.poly([(81,58),(86,55),(111,55),(116,59),(116,100),(111,106),(82,106),(79,101),(79,66)], '#19134fff')
out.rect(84,59,29,43,'#d7c4d6ff')
out.rect(87,61,26,39,'#f2dfdeff')
out.rect(87,64,26,2,'#69485aff')
out.rect(87,78,26,2,'#6a5265ff')
out.rect(87,91,26,2,'#6a5265ff')
out.rect(88,66,2,12,'#b9878fff')
out.rect(88,80,2,11,'#b9878fff')
out.rect(88,93,2,7,'#b9878fff')
# Product rows: colorful cans/bottles in shadowed slots.
products = [
    (92,68,'#c7624cff'),(97,67,'#e58a4dff'),(102,68,'#6bc978ff'),(107,67,'#4eb8caff'),
    (92,82,'#6f5bd0ff'),(97,81,'#d87356ff'),(102,82,'#59b7c9ff'),(107,81,'#e5bd5fff'),
    (92,95,'#ce5d4fff'),(97,94,'#e7a44eff'),(102,95,'#69bd77ff'),(107,94,'#59a9c8ff')]
for x,y,col in products:
    out.rect(x,y,3,7,'#4a3346ff')
    out.rect(x,y,2,6,col)
    out.set(x+1,y,'#f2d6c5ff')
# Machine divider, selection strip, coin slot, lower cabinet.
out.rect(112,59,3,45,'#32205eff')
out.rect(109,69,2,18,'#755178ff')
out.rect(110,72,1,4,'#d7b5cfff')
out.rect(82,103,33,3,'#3a2364ff')
out.poly([(81,106),(115,106),(115,143),(109,146),(82,143)], '#171348ff')
out.rect(86,109,24,13,'#211750ff')
out.rect(89,112,18,7,'#0d2638ff')
out.rect(91,113,14,3,'#152f43ff')
out.rect(84,125,28,2,'#29205dff')
out.rect(84,130,2,10,'#34276aff')
# Restore cabinet's purple side plane.
out.poly([(116,55),(132,61),(135,142),(115,143),(115,60)], '#1c1558ff')
out.poly([(130,65),(135,62),(135,141),(131,142)], '#251961ff')
out.dither(116,126,18,16,['#1c1558ff','#2d206aff'],'checker')

# Restore the bike portions hidden by the character: frame, seat, handle and fairing.
out.line(78,120,94,113,'#071922ff')
out.line(94,113,106,121,'#0a1c28ff')
out.line(79,121,101,130,'#0a1821ff')
out.line(101,130,112,134,'#142b36ff')
out.line(87,119,102,119,'#263a43ff')
out.line(94,114,104,116,'#35434aff')
out.line(98,112,109,113,'#101d25ff')
out.rect(101,111,8,3,'#152630ff')
out.line(102,114,109,124,'#1b3440ff')
out.line(100,115,106,126,'#284653ff')
out.poly([(84,119),(98,118),(108,126),(103,132),(90,128),(79,124)], '#0a1c27ff')
out.poly([(88,121),(99,121),(104,126),(100,129),(91,127)], '#173442ff')
out.line(91,124,100,128,'#315261ff')
out.set(95,123,'#55717aff')
out.set(103,125,'#55717aff')
# A few restored spokes/highlights at the rear edge.
out.line(104,131,111,142,'#0b1a22ff')
out.line(109,133,109,143,'#314650ff')
out.line(106,139,113,136,'#253d48ff')

# Cool storm tint over the complete scene.
tint = new_canvas(170,170,name='storm_tint')
tint.rect(0,0,170,170,'#061a3340')
out = flatten([out,tint], name='storm_base')

# Lightning behind the foreground subjects: pale core and blue-violet halo.
light = new_canvas(170,170,name='lightning')
bolt = [(67,0),(63,16),(69,16),(61,32),(66,31),(57,51),(61,34),(55,36),(61,18),(57,18),(62,0)]
light.poly(bolt,'#8aa8ff66')
light.poly([(65,0),(62,17),(66,17),(59,34),(63,33),(56,52),(60,31),(57,33),(62,15),(59,15),(63,0)],'#e8f5ffff')
# Branches.
light.line(61,19,51,27,'#a9caffb8')
light.line(51,27,46,38,'#e8f5ffff')
light.line(60,33,72,39,'#a9caffb8')
light.line(72,39,76,48,'#e8f5ffff')
light.line(63,12,72,7,'#dbeaffd0')
# Distant lightning glow in clouds.
light.ellipse(61,25,24,18,'#6982d81f')
out = flatten([out,light],name='storm_scene')

# Rain layer: translucent, wind-driven droplets with varied lengths.
rain = new_canvas(170,170,name='rain')
for i in range(150):
    x = random.randrange(2,170)
    y = random.randrange(4,158)
    length = random.choice([2,2,3,3,4,5])
    col = random.choice(['#9edcf06a','#b9e9f47d','#75bad56b','#d4f4fa70'])
    rain.line(x,y,x-1,y+length,col)
# Brighter drops near the lightning and foreground.
for x,y in [(48,18),(73,23),(55,58),(83,44),(118,32),(145,50),(22,88),(67,92),(123,86),(151,104),(36,121),(61,132),(139,126)]:
    rain.line(x,y,x-2,y+6,'#d9f5ffc0')
    rain.set(x-2,y+7,'#eefcffaa')
out = flatten([out,rain],name='rainy_scene')

# Wet pavement: pooled blue reflections, broken highlights and small splashes.
wet = new_canvas(170,170,name='wet_details')
wet.rect(0,153,170,17,'#071d2d55')
wet.poly([(0,162),(25,160),(47,163),(69,161),(91,164),(113,161),(136,164),(169,161),(169,170),(0,170)],'#0c416078')
wet.poly([(3,166),(31,165),(46,167),(24,169),(2,169)],'#1781a088')
wet.poly([(112,165),(145,163),(165,166),(154,169),(119,169)],'#1e79968c')
wet.poly([(54,158),(73,157),(86,160),(76,162),(59,161)],'#b7dce49c')
wet.poly([(91,160),(105,159),(116,162),(110,165),(96,164)],'#d7edf0a8')
# Broken reflected lightning.
wet.rect(58,153,2,4,'#cbdcffa8')
wet.rect(55,159,5,2,'#dbe7ffba')
wet.rect(51,164,7,2,'#b8d0ffc0')
wet.rect(47,168,8,2,'#dae8ffc8')
# Clinging beads and splash crowns on pavement, bike, pole, and machine.
for x,y in [(8,156),(18,161),(31,154),(43,166),(67,151),(79,163),(121,155),(135,160),(149,154),(160,164),
            (48,142),(53,137),(64,145),(73,139),(91,136),(104,142),(112,131),(116,92),(132,119),(32,105),(33,129)]:
    wet.set(x,y,'#b9edf0b8')
    wet.set(x+1,y+1,'#5eb4cf78')
for x,y in [(14,159),(83,157),(126,160),(154,157)]:
    wet.line(x-2,y+1,x,y-1,'#a9dfe6a0')
    wet.line(x,y-1,x+2,y+1,'#a9dfe6a0')
# Wet edge sheen on machine and bike.
wet.line(115,58,115,101,'#87c8df72')
wet.line(133,72,134,121,'#5da9cd63')
wet.line(82,106,82,139,'#78bdd67a')
wet.line(79,120,98,116,'#8cc2cf62')
wet.line(93,129,103,133,'#a3d2da68')
result = flatten([out,wet],name='thunderstorm_edit')

print(result.stats_text())
view(result,size=680,margin=0)
finish(result)
