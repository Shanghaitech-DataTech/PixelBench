import random
random.seed(21)
c = new_canvas(128,128,background='#76cffa',name='Summer seaside')
# A compact sunlit palette.
sky='#76cffa'; skylo='#a0e2fa'; cloud='#fffdf0'; cloudshade='#d9f1f7'
sand='#f6d58b'; sandlight='#ffe6a5'; sandshade='#dfb66c'; wet='#c5cda0'
# Sky bands and clear horizon.
c.rect(0,33,128,15,skylo)
c.rect(0,28,128,5,'#8edbfa')
c.circle(106,16,11,'#ffe69a')
c.circle(106,16,8,'#fff4ba')
c.circle(104,14,5,'#fff8d8')
# Soft, stepped cloud silhouettes.
def cloudbank(x,y):
    c.rect(x,y+5,31,5,cloudshade)
    c.ellipse(x+8,y+4,7,4,cloud)
    c.ellipse(x+17,y,8,6,cloud)
    c.ellipse(x+25,y+4,7,4,cloud)
    c.rect(x+3,y+5,27,2,cloud)
    c.line(x+6,y+10,x+27,y+10,cloudshade)
cloudbank(5,16)
cloudbank(62,30)
# Two gulls, each with a pair of bent wings.
for x,y,s in [(44,34,5),(65,13,4)]:
    c.line(x-s,y-2,x-2,y-1,'#42759d')
    c.line(x-2,y-1,x,y+1,'#42759d')
    c.line(x,y+1,x+2,y-1,'#42759d')
    c.line(x+2,y-1,x+s,y-2,'#42759d')
    c.set(x-s,y-3,cloud)
    c.set(x+s,y-3,cloud)
# Sea: deep blue at the horizon, turquoise shallows.
c.rect(0,47,128,42,'#247cba')
c.line(0,47,127,47,'#499dc9')
c.rect(0,52,128,8,'#258fbe')
c.rect(0,60,128,10,'#269fc0')
c.poly([(0,70),(40,68),(79,64),(127,62),(127,88),(0,96)],'#26b3c1')
c.poly([(0,78),(43,74),(80,70),(127,66),(127,91),(0,98)],'#57c9c4')
# Distant little wavelets, kept horizontal.
for y in range(50,78):
    for j in range(4):
        x=random.randrange(128); n=random.randrange(2,10)
        if y<58: col=random.choice(['#4aa7ce','#3c9cc8'])
        elif y<68: col=random.choice(['#50c2d0','#35b1c7'])
        else: col=random.choice(['#86ded3','#42bac2'])
        c.line(x,y,min(127,x+n),y,col)
# Broad arcs of breaking waves behind the shore.
c.path('M 0 71 Q 17 74 32 70 Q 47 66 61 68 M 75 64 Q 92 66 105 62 L 122 61','#a6e9df',fill=False)
c.path('M 2 70 L 14 71 M 25 71 L 35 69 M 42 68 L 52 67 M 86 64 L 99 63','#f4ffed',fill=False)
# Sand edge and wet strip sweep diagonally across the picture.
c.path('M 0 88 Q 20 91 43 83 Q 64 77 83 78 Q 102 78 127 67 L 127 128 L 0 128 Z',wet)
c.path('M 0 92 Q 20 96 44 87 Q 63 81 83 82 Q 107 81 127 72 L 127 128 L 0 128 Z',sandshade)
c.path('M 0 95 Q 18 99 46 90 Q 63 85 84 85 Q 106 83 127 76 L 127 128 L 0 128 Z',sand)
c.path('M 0 103 Q 17 105 39 98 Q 68 88 90 89 Q 108 87 127 82 L 127 128 L 0 128 Z',sandlight)
# Main foamy shore, a thick irregular white rim with turquoise pockets.
c.path('M 0 85 Q 18 89 39 82 Q 61 75 82 76 Q 100 77 127 65 L 127 69 Q 104 81 82 80 Q 61 79 40 86 Q 19 94 0 90 Z','#efffee')
c.path('M 0 85 Q 17 89 39 82 Q 60 75 82 76 Q 103 77 127 65','#c4f6e8',fill=False)
c.path('M 0 90 Q 20 94 40 86 Q 62 79 82 80 Q 104 81 127 69','#fffef1',fill=False)
for x,y in [(5,87),(11,89),(26,87),(32,85),(47,82),(58,79),(72,78),(90,78),(106,74),(116,70)]:
    c.line(x,y,x+3,y,'#77d4c5')
for x,y in [(3,93),(22,94),(29,91),(49,85),(65,83),(85,83),(98,81),(111,77),(123,73)]:
    c.line(x,y,min(x+2,127),y,'#fff7d4')
# White sailboat beyond the surf.
c.line(87,50,87,62,'#755f56')
c.poly([(85,51),(85,60),(77,60)],'#fffdf0')
c.poly([(89,53),(95,60),(89,60)],'#e4f2e8')
c.line(85,53,79,59,'#ffffff')
c.poly([(76,62),(97,62),(93,65),(81,65)],'#f8f4db')
c.line(80,65,93,65,'#325f8b')
c.line(81,67,96,67,'#82d7d7')
c.line(85,69,92,69,'#62c8ce')
# A few sand grains and shell clusters, no uniform noise.
for i in range(73):
    x=random.randrange(128); y=random.randrange(92,128)
    if random.random()<0.7:
        c.line(x,y,min(127,x+random.choice([0,1,2])),y,random.choice([sand,'#edc77e','#f1ce88']))
# Umbrella's cool cast shadow and central pole.
c.ellipse(39,110,23,6,'#dcb975')
c.ellipse(35,108,17,4,'#c9ad72')
c.poly([(35,82),(38,82),(38,109),(35,110)],'#9b7960')
c.line(35,83,35,107,'#fff0bb')
c.line(36,84,36,108,'#d4b183')
# Dome silhouette and alternating radial fabric panels.
c.path('M 8 82 Q 14 66 34 61 Q 53 63 64 80 L 62 85 Q 56 81 51 86 Q 45 82 39 87 Q 31 83 24 87 Q 17 82 10 86 Z','#b9444b')
c.path('M 9 81 Q 17 66 34 62 Q 25 71 24 83 Q 17 79 9 84 Z','#ed5756')
c.path('M 34 62 Q 27 70 24 83 Q 31 80 39 83 Q 39 71 34 62 Z','#fff6de')
c.path('M 34 62 Q 43 65 50 82 Q 45 80 39 83 Q 39 69 34 62 Z','#ef5755')
c.path('M 34 62 Q 51 64 63 80 L 62 83 Q 56 79 50 82 Q 44 66 34 62 Z','#fff4da')
# Crisp folds, sun highlights, scalloped dark undersides.
c.path('M 10 80 Q 19 66 33 63','#ff8a72',fill=False)
c.path('M 25 80 Q 27 69 33 64','#ffffff',fill=False)
c.path('M 35 63 Q 43 68 48 79','#ff8b75',fill=False)
c.path('M 37 64 Q 50 68 60 78','#ffffff',fill=False)
c.path('M 10 84 Q 17 80 24 84 Q 31 81 39 84 Q 44 81 51 83 Q 56 80 62 83','#bd4d51',fill=False)
c.line(34,59,34,61,'#b7444b')
c.set(35,60,'#ffbaa0')
# Striped towel laid out in perspective on the sand.
c.poly([(77,94),(95,90),(109,111),(89,117)],'#dbb36f')
c.poly([(75,93),(93,89),(107,110),(87,116)],'#fff9dc')
# stripe bands follow the perspective of the towel
for p in [[(77,96),(95,92),(98,96),(80,100)],[(82,103),(100,99),(103,103),(85,107)],[(87,110),(105,106),(107,110),(89,114)]]:
    c.poly(p,'#3d9faf')
c.line(75,93,93,89,'#ffffff')
c.line(75,94,87,115,'#e7e8c7')
for x,y in [(88,116),(92,115),(96,114),(100,113),(104,112)]:
    c.line(x,y,x+1,y+2,'#fff9dc')
# A pair of small coral flip-flops with dark straps.
for x,y in [(112,98),(118,105)]:
    c.ellipse(x,y+4,3,6,'#cfaa6e')
    c.ellipse(x,y+3,3,6,'#c94f4e')
    c.ellipse(x,y+2,2,5,'#f97c65')
    c.line(x-2,y+1,x,y+4,'#405c64')
    c.line(x+2,y,x,y+4,'#405c64')
    c.set(x,y+4,'#fff3c9')
# Tiny shells and footprints finish the foreground.
for x,y in [(62,110),(65,116),(57,102)]:
    c.rect(x,y,2,3,'#e4bf7a')
    c.set(x+1,y-1,'#e4bf7a')
c.line(14,120,18,120,'#d6ad73')
c.poly([(14,119),(15,117),(17,117),(19,119)],'#fff8e5')
c.set(16,118,'#efbda0')
c.line(72,122,75,122,'#d6ad73')
c.line(72,121,74,120,'#fff5d7')
print(c.stats_text())
print(c.matrix_text(region=(7,59,64,87)))
save('summer-seaside',c)
finish(c)
