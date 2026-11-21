import random
rng=random.Random(9)
result=new_canvas(128,128,background='#332e50',name='Ember Tide')
c=result
# A deliberately small sunset palette
sky0='#332e50'; sky1='#59405e'; sky2='#89516c'; sky3='#be6575'; sky4='#e88478'; glow='#f6a276'
cloudDark='#70445f'; cloudMid='#a35c70'; cloudLight='#e08a83'
sun='#ffb34e'; sunLight='#ffce69'; cream='#ffe0a0'
sea='#684760'; sea2='#855268'; seaLight='#bd7479'; reflection='#ed986b'
ink='#202439'; rock='#303047'; rockMid='#454052'; rockLit='#66515c'; grass='#554950'
wall='#9b7880'; wallLight='#c1968b'; wallHi='#e1b098'; wallShade='#755e71'; roof='#3f3c55'; gold='#f3b773'
# sky in broad clean colour bands
for y,h,col in [(0,23,sky0),(23,17,sky1),(40,12,sky2),(52,13,sky3),(65,15,sky4),(80,48,sea)]: c.rect(0,y,128,h,col)
# strata of long sunset clouds
c.poly([(0,28),(17,28),(17,30),(30,30),(30,32),(49,32),(49,34),(20,34),(20,35),(0,35)],cloudDark)
c.poly([(88,30),(102,30),(102,28),(122,28),(122,31),(127,31),(127,36),(75,36),(75,34),(88,34)],cloudDark)
c.rect(100,37,28,2,cloudMid)
c.poly([(0,44),(8,44),(8,41),(23,41),(23,43),(33,43),(33,45),(48,45),(48,48),(30,48),(30,50),(0,50)],cloudMid)
c.rect(0,49,24,2,cloudLight)
c.poly([(54,45),(64,45),(64,43),(78,43),(78,45),(98,45),(98,48),(116,48),(116,51),(61,51),(61,49),(54,49)],cloudDark)
c.rect(62,51,42,1,cloudLight)
# enormous low sun
c.circle(33,65,20,sun)
c.circle(33,65,18,sunLight)
c.rect(15,69,37,5,sun)
c.rect(19,75,29,4,sun)
# soft horizontal clouds crossing the disk
c.poly([(0,56),(12,56),(12,55),(24,55),(24,57),(39,57),(39,59),(18,59),(18,60),(0,60)],sky3)
c.rect(0,60,17,1,glow)
c.rect(42,65,24,2,sky4)
c.rect(48,67,25,1,glow)
c.rect(0,75,22,2,sky4)
# distant islands and horizon
c.poly([(0,80),(9,78),(16,79),(23,77),(31,80),(62,80),(70,76),(80,78),(84,82),(0,83)],'#9b6674')
c.rect(0,83,128,45,sea)
c.rect(0,83,75,1,glow)
c.poly([(0,88),(11,86),(22,86),(22,88),(54,88),(54,90),(77,90),(77,96),(0,96)],sea2)
# broken bands of sunlight on the water
for y in range(85,116):
    span=max(3,int(15-(y-85)*.24))
    if y%3!=1:
        x=33-span+rng.randint(-3,3)
        c.rect(x,y,span*2+rng.randint(-4,3),1,reflection if y<102 else seaLight)
        if y%4==0:c.rect(x+4,y,max(2,span-1),1,sunLight if y<96 else reflection)
for i in range(94):
    x=rng.randrange(0,85); y=rng.randrange(87,124)
    if abs(x-33)<13 and y<107:continue
    c.rect(x,y,rng.randrange(2,10),1,rng.choice([sea2,seaLight,sea,sea]))
# far promontory
c.poly([(118,77),(125,74),(127,74),(127,89),(112,89),(108,84)],rockLit)
# main cliff silhouette and planes
c.poly([(76,84),(88,83),(96,80),(113,81),(127,77),(127,128),(62,128),(62,114),(65,107),(62,101),(68,96),(69,89)],rock)
c.poly([(76,86),(86,85),(82,95),(77,103),(76,112),(68,119),(66,111),(69,104),(66,100),(72,94)],rockLit)
c.poly([(86,88),(100,85),(94,94),(89,98),(88,107),(80,115),(82,99)],rockMid)
c.poly([(104,85),(115,83),(110,93),(105,100),(102,116),(94,122),(97,104)],rockMid)
c.poly([(120,85),(127,82),(127,115),(118,122),(116,105),(119,96)],ink)
c.poly([(74,86),(82,82),(96,81),(109,82),(124,78),(127,78),(127,84),(112,87),(97,86),(83,89),(71,91)],grass)
c.line(74,87,86,85,wallLight);c.line(87,85,100,84,rockLit)
for x,y in [(74,95),(71,102),(82,95),(81,100),(99,92),(96,101),(107,90),(104,106),(72,114),(91,114)]:
    c.line(x,y,x-2,y+4,wallShade if x<85 else rockLit)
# castle retaining base
c.poly([(78,78),(119,75),(119,84),(109,87),(78,85)],wallShade)
c.rect(80,79,36,5,wall)
c.line(79,85,111,85,wallLight)
# rear keep and roof
c.rect(89,62,18,20,wallShade)
c.poly([(86,63),(98,51),(110,63)],roof)
c.line(88,62,98,52,wallHi)
c.line(98,52,109,63,ink)
c.rect(97,63,9,19,wall)
c.rect(95,67,2,5,ink);c.rect(102,67,2,5,ink)
# two towers: masonry with strong sun-facing sides
for x,top,bottom in [(77,55,84),(107,49,82)]:
    c.rect(x,top,13,bottom-top,wallShade)
    c.rect(x,top,4,bottom-top,wallLight)
    c.rect(x+4,top,6,bottom-top,wall)
    c.line(x,top,x,bottom-1,wallHi)
    c.rect(x-1,top-3,15,5,wall)
    c.rect(x-1,top-3,5,4,wallLight)
    for bx in [x-1,x+5,x+11]: c.rect(bx,top-6,3,4,wallLight if bx==x-1 else wall)
    c.rect(x,top+2,13,1,roof)
    c.line(x,top+3,x+8,top+3,wallHi)
    for yy in range(top+6,bottom-2,5):
        c.rect(x+1,yy,3,1,wall)
        c.rect(x+7+(yy%2),yy+2,3,1,wallShade)
    for yy in [top+7,top+18]:
        if yy+4<bottom:
            c.rect(x+6,yy,3,5,roof);c.set(x+7,yy-1,roof)
            c.rect(x+6,yy+1,1,3,gold)
            c.line(x+6,yy+5,x+9,yy+5,wallLight)
# connecting battlement, arched entry
c.rect(89,73,19,12,wall)
c.rect(89,73,19,2,wallLight)
for x in range(89,108,5): c.rect(x,70,3,4,wallLight)
c.rect(96,79,6,6,roof);c.rect(97,77,4,3,roof);c.rect(98,76,2,1,wallShade)
c.line(96,79,96,84,wallHi)
c.rect(98,80,2,5,ink)
# waving crimson banners
for x,y in [(83,38),(113,31)]:
    c.line(x,y,x,y+14,roof);c.set(x,y,cream)
    c.poly([(x+1,y+1),(x+7,y+2),(x+12,y),(x+11,y+5),(x+7,y+7),(x+1,y+5)],'#a94460')
    c.line(x+1,y+1,x+6,y+2,'#f49b81');c.line(x+7,y+2,x+11,y+1,'#f49b81')
    c.rect(x+2,y+3,2,2,gold)
# descending footpath
c.poly([(102,86),(108,86),(97,90),(87,91),(84,94),(78,94),(83,89)],wallShade)
c.line(85,90,96,88,wallLight)
# flying seabirds, tiny silhouetted wings
for x,y in [(12,68),(58,61),(65,57),(18,71)]:
    c.line(x-2,y-1,x,y,cloudDark);c.line(x,y,x+2,y-1,cloudDark)
# foreground rocks frame the water
c.poly([(0,103),(6,104),(9,108),(15,108),(20,114),(28,116),(33,122),(48,125),(54,128),(0,128)],ink)
c.poly([(0,103),(6,104),(9,109),(4,108),(0,110)],rockMid)
c.poly([(13,110),(17,111),(21,115),(28,117),(30,121),(19,118),(16,114)],rock)
c.poly([(48,128),(53,121),(62,119),(67,114),(76,114),(81,109),(89,110),(95,117),(108,114),(115,118),(127,116),(127,128)],ink)
c.line(65,119,70,115,rockMid);c.line(70,115,76,115,rockMid)
c.poly([(83,111),(88,111),(92,116),(85,115)],rock)
# foreground grass tufts
for x,y in [(4,107),(16,114),(62,120),(77,116),(117,119),(124,118)]:
    c.line(x,y,x-2,y-6,ink);c.line(x,y,x+1,y-8,ink);c.line(x,y,min(127,x+4),y-4,ink)
# Thin surf lines at the foot of the headland
c.line(58,109,63,109,seaLight)
c.line(54,111,61,111,sea2)
c.line(58,115,63,115,seaLight)
c.rect(47,116,7,1,sea2)
# title typography, shadow and gold face, nearest-neighbour bitmap
label=new_canvas(59,7,name='title letters')
label.text(0,0,'EMBER TIDE',cream)
title=label.select(0,0,59,7).resize(118,14).preview()
# draw shadow using the source letter coverage
w,h,rgba=title.to_rgba()
for y in range(h):
    for x in range(w):
        if rgba[(y*w+x)*4+3]:
            c.set(x+6,y+12,ink)
            c.set(x+5,y+10,cream if y<7 else gold)
# restrained ornamental rules
c.line(20,6,55,6,wallShade);c.line(72,6,107,6,wallShade)
c.poly([(61,6),(64,3),(67,6),(64,9)],gold)
c.line(36,28,58,28,wallShade);c.line(69,28,91,28,wallShade)
c.set(63,28,gold);c.set(64,27,gold);c.set(64,29,gold);c.set(65,28,gold)
# title-screen prompt, resting in the dark foreground
c.text(32,119,'PRESS START',wallHi)
view(c)
save('ember-tide',c)
finish(result)
