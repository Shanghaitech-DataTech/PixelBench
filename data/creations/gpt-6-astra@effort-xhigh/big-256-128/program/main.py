import random, math
output = input_canvas.copy(name='output')
# Recast the original image's palette, retaining its architecture and pixel clusters.
colours = ['#190f22','#321829','#612534','#953647','#f39a7f','#090a14','#754047','#63363f','#a55454','#b68991','#fdac8b','#ffd5a0','#45304e','#321e2e','#ed654d','#ed654d','#170f1d','#2a1823','#ffb564','#69415d','#c06b73','#52364e','#b16e7e','#211722','#392735','#ac6570','#e49b8c','#df5f50','#6b4159','#70414c','#ffc27e','#9b5a72','#48303b','#db7167','#190f1c','#d57e76','#e2afa4','#a65c71','#dd8275','#f77860','#ab5c63','#cd6e71','#b76269','#f68562','#794154','#633145','#f89c83','#633445','#321d2c','#492338','#e36450','#9a5263','#28172a','#211523','#100e18','#301c31','#8d5c59','#3e2e3c','#713146','#69444b','#2e1f2c','#8d4053','#573744','#805568','#b34c55','#8b495a','#a64f59','#24182d','#583049','#1d1527','#392138','#2f1d31','#c08a82']
remap = {input_canvas.color('c'+str(i)): output.color(c) for i,c in enumerate(colours)}
for y in range(128):
    for x in range(256):
        output.set(x,y,remap[input_canvas.get(x,y)])
# Cool the masonry and suppress the old white cloud highlights.
cloud_map = {'c11':'#e79182','c4':'#d47778','c26':'#b96d7b','c36':'#c17e89','c37':'#824b65'}
stone_map = {'c25':'#69485c','c29':'#463045','c30':'#aa6b70','c38':'#986374','c72':'#81566c','c32':'#362739','c63':'#64435a'}
for y in range(128):
    for x in range(256):
        old = input_canvas.color_name(input_canvas.get(x,y))
        if old in cloud_map:
            output.set(x,y,cloud_map[old])
        if 98<=x<=164 and 35<=y<=104 and old in stone_map:
            output.set(x,y,stone_map[old])
# A large, mottled blood moon behind the original central needle.
castle_before_moon = output.copy(name='masonry_reference')
cx,cy,r=128,22,20
moon_palette=['#522033','#742338','#96283d','#bb3746','#dd5052','#ef7062','#ff9579']
craters=[(119,11,5,3,1.5),(131,9,4,2,1.0),(135,18,6,4,1.3),(121,25,4,5,1.2),(132,30,5,3,1.6),(140,28,3,5,1.3),(116,19,3,2,.8)]
for y in range(0,46):
    for x in range(105,152):
        dx,dy=x-cx,y-cy
        d=math.sqrt(dx*dx+dy*dy)
        if d>23: continue
        if d>r:
            if d<=21: output.set(x,y,'#64273b')
            elif d<=22 and (x+y)%2==0: output.set(x,y,'#361c2d')
            continue
        # Deliberately clustered surface details, without antialiasing.
        n=random.Random((x//2)*1009+(y//2)*719).random()
        value=4.0-(dx/20)*.8-(dy/20)*.85+(n-.5)*.8
        for mx,my,rx,ry,depth in craters:
            q=((x-mx)/rx)**2+((y-my)/ry)**2
            if q<1+(n-.5)*.25:
                value-=depth
            elif 1<q<1.25 and y<my:
                value+=.45
        if d>18.2:
            value=5.8 if dx+dy<-6 else 2.2
        output.set(x,y,moon_palette[max(0,min(6,round(value)))])
# Reinsert the original silhouette where its spire crosses the moon.
for y in range(23,46):
    half=0 if y<29 else (1 if y<35 else (2 if y<39 else 4))
    for x in range(128-half,129+half):
        output.set(x,y,castle_before_moon.get(x,y))
# Architectural palette, shaded towards a cold violet-black.
ink='#110e1b'; deep='#211726'; shade='#302238'; stone='#4b334d'; edge='#795063'; rim='#a76270'
ember='#c64242'; fire='#fa7955'; core='#ffd198'
def poly(points,c): output.poly(points,c)
def slit(x,y,h=5):
    poly([(x,y-1),(x-1,y+1),(x-1,y+h),(x+1,y+h),(x+1,y+1)],ink)
    output.line(x,y+1,x,y+h-1,ember)
    if h>=4: output.line(x,y+2,x,y+h-2,fire)
    output.set(x,y+h-1,core)
def turret(x,tip,bottom,half=4,horns=True):
    roof=tip+11
    output.rect(x-half,roof,2*half+1,bottom-roof,deep)
    output.rect(x-half+1,roof,half,bottom-roof,stone)
    output.line(x-half,roof+1,x-half,bottom-1,edge)
    for yy in range(roof+3,bottom,4):
        output.line(x-half+1,yy,x-1,yy,shade)
        if yy+1<bottom: output.set(x+2,yy+1,stone)
    poly([(x-half-2,roof),(x-2,tip+5),(x,tip),(x+2,tip+5),(x+half+2,roof)],ink)
    output.line(x,tip+2,x-half-1,roof-1,edge)
    output.line(x-half-2,roof,x+half+2,roof,shade)
    output.line(x-half,roof+1,x+half,roof+1,edge)
    if horns:
        poly([(x-half,roof),(x-half-3,roof-4),(x-half-4,roof-9),(x-half-1,roof-6),(x-1,roof-3)],ink)
        poly([(x+half,roof),(x+half+3,roof-4),(x+half+4,roof-9),(x+half+1,roof-6),(x+1,roof-3)],ink)
        output.line(x-half-4,roof-9,x-half-3,roof-5,edge)
        output.set(x+half+3,roof-6,ember)
    if bottom-roof>6: slit(x-1,roof+3,min(6,bottom-roof-3))
# Infernal crown on the tallest existing tower.
poly([(126,46),(122,44),(120,40),(119,32),(122,36),(123,40),(127,42)],ink)
poly([(130,46),(134,44),(136,40),(137,32),(134,36),(133,40),(129,42)],ink)
output.line(119,32,120,39,rim)
output.line(120,39,123,43,edge)
output.line(137,32,136,39,edge)
poly([(126,43),(127,31),(128,22),(130,36),(130,43)],ink)
output.line(128,25,127,38,edge)
output.rect(124,44,8,2,deep)
output.line(124,44,131,44,edge)
output.rect(126,46,5,20,shade)
output.line(125,46,125,65,edge)
slit(128,48,6)
slit(128,58,4)
output.set(128,43,fire)
# Spiked subordinate towers retain the original terraced silhouette.
turret(137,54,78,4,False)
turret(106,66,98,4,True)
turret(151,65,96,4,True)
turret(93,84,104,3,False)
turret(162,82,110,3,False)
# Broken crimson pennants.
output.line(140,55,140,63,edge)
poly([(141,55),(147,56),(145,58),(149,59),(141,59)],'#7e263e')
output.line(141,55,145,56,'#bb4654')
output.line(154,67,154,75,edge)
poly([(155,67),(162,68),(159,70),(161,72),(155,71)],'#76243b')
# A pointed gate cut into the lower keep.
poly([(108,104),(108,95),(111,91),(116,87),(121,92),(124,96),(124,104)],deep)
output.line(108,95,116,87,edge)
output.line(116,87,124,96,stone)
poly([(111,104),(111,96),(116,91),(121,96),(121,104)],'#792939')
poly([(113,104),(113,97),(116,94),(119,97),(119,104)],'#da4d43')
poly([(114,104),(114,100),(116,98),(118,100),(118,104)],'#ff9b65')
# Portcullis teeth and its hot threshold.
for x in [113,116,119]:
    output.line(x,97 if x!=116 else 94,x,102,ink)
output.line(111,103,121,103,fire)
output.line(112,104,120,104,core)
output.line(108,97,108,103,edge)
output.line(124,97,124,103,shade)
# Angular horns flank the gate's keystone.
poly([(113,92),(109,91),(106,86),(109,88),(113,89)],ink)
poly([(119,92),(123,91),(126,86),(123,88),(119,89)],ink)
output.set(114,91,fire); output.set(118,91,fire)
# Lit lancet windows on the original keep.
for x,y,h in [(119,75,5),(125,80,4),(136,84,5),(144,92,4),(131,96,4),(157,103,3)]: slit(x,y,h)
# Tiny forked-wing bats, silhouetted against the storm.
def bat(x,y,wide=4):
    poly([(x-wide,y-1),(x-2,y),(x-1,y+2),(x,y+1),(x+1,y+2),(x+2,y),(x+wide,y-1),(x+wide-1,y+2),(x+2,y+2),(x,y+4),(x-2,y+2),(x-wide+1,y+2)],ink)
    output.set(x,y,ink)
bat(89,24,5); bat(172,28,4); bat(76,47,3); bat(184,47,3)
# Weathered brick clusters soften the new tower walls into the source's texture.
wallbands=[(124,46,132,66),(133,67,141,78),(102,79,110,98),(147,78,155,96),(90,97,96,104),(159,95,165,110)]
random.seed(33)
for left,top,right,bottom in wallbands:
    for yy in range(top+1,bottom):
        for xx in range(left+1,right):
            pix=output.get(xx,yy)
            if pix in [output.color(stone),output.color(shade),output.color(deep)] and random.random()<.22:
                output.set(xx,yy,random.choice([shade,stone,'#56394f','#3d293e']))
    for yy in range(top+4,bottom,5):
        xx=left+1+((yy//5)%2)*2
        output.line(xx,yy,xx+2,yy,shade)
# Heavy buttresses, corbels, and small teeth on the terraces.
for x,y,h in [(102,86,12),(109,88,11),(147,86,12),(154,86,15),(159,100,10),(164,101,9)]:
    poly([(x,y),(x+1,y),(x+1,y+h-3),(x+2,y+h),(x-1,y+h)],shade)
    output.line(x,y,x,y+h-2,stone)
for x,y in [(100,97),(104,98),(127,100),(132,102),(136,103),(141,105),(145,106),(150,108),(155,110),(160,111),(164,112)]:
    output.rect(x,y,2,3,ink)
    output.set(x,y,edge)
# A demonic skull seal in the central facade.
poly([(127,72),(129,70),(132,70),(135,72),(134,76),(132,78),(129,78),(128,76)],'#725064')
poly([(128,72),(125,71),(124,68),(127,70),(130,72)],edge)
poly([(133,72),(136,71),(137,68),(134,70),(132,72)],stone)
output.line(128,73,129,74,ink); output.set(129,74,fire)
output.line(132,74,133,73,ink); output.set(132,74,fire)
output.set(131,75,ink)
output.line(129,77,133,77,deep)
output.set(130,77,rim); output.set(132,77,rim)
# Firelight spills onto the existing zigzag road.
road_map={'c30':'#ffad78','c38':'#e16951','c25':'#9e484b','c72':'#bd5b59','c29':'#613340','c36':'#ef9877'}
for y in range(104,128):
    for x in range(68,155):
        original_name=input_canvas.color_name(input_canvas.get(x,y))
        if original_name in road_map:
            output.set(x,y,road_map[original_name])
# Narrow hot fractures interrupt the cliff, away from the road.
for pts in [[(62,126),(65,122),(65,119),(68,116),(70,115)],[(170,126),(169,122),(171,119),(169,115)],[(177,122),(180,118),(179,114)]]:
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        output.line(x0+1,y0,x1+1,y1,'#632638')
        output.line(x0,y0,x1,y1,'#ac3a42')
    output.set(pts[1][0],pts[1][1],fire)
# Two small braziers lead toward the gate.
def flame(x,y):
    output.line(x,y+1,x,y+5,ink)
    output.line(x-2,y,x+2,y,edge)
    poly([(x-2,y-1),(x-2,y-3),(x,y-7),(x,y-4),(x+2,y-5),(x+2,y-1)],ember)
    poly([(x-1,y),(x-1,y-3),(x,y-5),(x+1,y-2),(x+1,y)],fire)
    output.set(x,y-1,core)
flame(96,107); flame(129,116)
# Dead, hooked branches project from the foreground tree and left ruins.
for pts in [[(250,122),(247,111),(241,105),(238,97),(239,92)],[(244,108),(244,100),(249,94),(249,89)],[(240,104),(234,103),(230,97)],[(247,113),(251,108),(254,108)],[(20,124),(18,117),(14,113),(13,107)],[(18,118),(21,112),(21,108)]]:
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        output.line(x0,y0,x1,y1,ink)
        if x0>240: output.line(x0+1,y0,x1+1,y1,ink)
output.line(246,111,249,120,'#3d2638')
# Scattered ember flecks carried across the dark hillside.
for x,y in [(77,113),(83,108),(87,120),(98,115),(136,118),(158,118),(173,108),(180,112),(68,120),(42,117),(187,96),(57,102),(200,98)]:
    output.set(x,y,ember)
    if (x+y)%3==0: output.set(x,y-1,'#f18160')
# Slate roof ridges catch the red moonlight in broken, stepped lines.
for x,tip,half in [(106,66,4),(151,65,4),(137,54,4),(93,84,3),(162,82,3)]:
    output.line(x,tip+3,x-half+1,tip+9,'#5a354b')
    output.set(x,tip+2,'#8b4b5b')
    output.line(x-1,tip+8,x+1,tip+8,'#302135')
    output.line(x-2,tip+10,x+2,tip+10,'#302135')
    output.set(x-half,tip+11,'#a25c6c')
# A steep broken gable on the old central hall.
output.line(116,83,123,76,ink)
output.line(123,76,130,85,ink)
output.line(117,83,123,77,'#6a4358')
output.line(124,79,127,83,shade)
output.set(123,76,rim)
# Distant silhouettes are readable against the lighter storm front.
bat(64,70,3)
bat(192,71,4)
output.set(64,71,'#211726')
view(output, scale=4, margin=0)
save('demon_kings_castle', output)
finish(output)
