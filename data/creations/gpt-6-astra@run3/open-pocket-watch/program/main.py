import math, random
random.seed(8)
c = new_canvas(64,64,background='#10141a',name='watch')
# subtle background
c.circle(34,33,29,'#171b20')
c.ellipse(32,58,25,3,'#090c10')
# chain curling to the right
for x,y in [(52,7),(56,8),(59,10),(60,14),(59,18),(57,21),(56,24)]:
    c.ellipse(x,y,3,2,'#17110b')
    c.ellipse(x,y,2,1,'#a87932',False)
    c.set(x-1,y-1,'#edc36e')
# lid, hinged above left
c.circle(23,18,16,'#080a0d')
c.circle(23,17,16,'#553815')
c.circle(23,17,15,'#b8883c')
c.circle(23,17,13,'#efd087')
c.circle(23,17,12,'#715329')
c.circle(23,17,11,'#30271d')
c.circle(23,17,10,'#4c3a25')
c.circle(23,17,8,'#5a4228')
# lid interior decorative glints
c.path('M 14 17 Q 14 9 22 8 L 26 8', '#967344',False)
c.path('M 16 22 Q 23 27 30 20', '#836035',False)
c.line(17,12,20,10,'#d2a85f')
c.set(15,14,'#f7d792')
c.line(22,27,28,26,'#1b1714')
# hinge
c.rect(29,27,10,5,'#21170e')
c.rect(30,27,8,3,'#bc8b42')
c.line(31,27,36,27,'#f9d98f')
c.line(33,28,33,30,'#553814')
# main case
c.circle(34,43,21,'#090b0d')
c.circle(34,42,20,'#513411')
c.circle(34,42,19,'#c09142')
c.circle(34,42,18,'#f2d18b')
c.circle(34,42,17,'#75501e')
c.circle(34,42,16,'#dfb667')
c.circle(34,42,15,'#28231c')
c.circle(34,42,14,'#594423')
c.circle(34,42,13,'#221d18')
# outer case rim highlights
c.path('M 16 40 Q 17 27 29 24', '#fff0bd',False)
c.path('M 38 24 Q 50 26 53 38', '#eac77d',False)
c.path('M 17 48 Q 21 58 32 60', '#aa7130',False)
c.path('M 39 60 Q 50 57 53 48', '#f4d082',False)
# plate within dial
c.circle(34,42,12,'#8a6835')
c.circle(34,42,11,'#3b3021')
c.poly([(24,40),(27,32),(34,30),(36,34),(33,38),(29,40)],'#b68c4b')
c.poly([(25,48),(29,43),(35,44),(38,49),(34,53),(28,52)],'#a87e40')
c.poly([(37,35),(42,33),(45,38),(44,45),(40,46),(37,42)],'#ba9250')
# gear function with clear teeth and spokes
def gear(x,y,r,base,light):
    for i in range(12):
        a=2*math.pi*i/12
        c.line(round(x+(r-1)*math.cos(a)),round(y+(r-1)*math.sin(a)),round(x+(r+1)*math.cos(a)),round(y+(r+1)*math.sin(a)),base)
    c.circle(x,y,r,base)
    c.circle(x,y,r-1,'#33281c')
    for i in range(6):
        a=2*math.pi*i/6
        c.line(x,y,round(x+(r-1)*math.cos(a)),round(y+(r-1)*math.sin(a)),light)
    c.circle(x,y,1,base)
    c.set(x,y,'#f6daa0')
gear(29,38,4,'#d2a652','#f4cf7b')
gear(38,40,4,'#c8974a','#f2cf83')
gear(33,47,4,'#d3a34f','#f9d786')
gear(42,48,2,'#c8974a','#f3d48d')
# screws and jewel bearings
for x,y in [(25,44),(35,33),(43,35),(29,51),(39,52)]:
    c.circle(x,y,1,'#ead09a'); c.set(x,y,'#292721')
c.set(38,40,'#9f3634'); c.set(33,47,'#b13e39')
# chapter ring tick marks radial
for i in range(60):
    a=2*math.pi*i/60-math.pi/2
    r0=13 if i%5==0 else 14
    x0=round(34+r0*math.cos(a)); y0=round(42+r0*math.sin(a))
    x1=round(34+14*math.cos(a)); y1=round(42+14*math.sin(a))
    c.line(x0,y0,x1,y1,'#ffe0a0' if i%5==0 else '#a67c3e')
# hands stand out over movement
c.line(34,42,28,35,'#111b21')
c.line(33,41,28,35,'#a8c3bd')
c.line(34,42,42,37,'#101a20')
c.line(35,41,42,37,'#a9c6c1')
c.circle(34,42,1,'#fbe4ac')
c.set(34,42,'#27313a')
# bow and crown on upper right
c.rect(49,27,4,4,'#4a3015')
c.rect(50,26,4,3,'#d5a657')
c.line(51,26,53,26,'#ffe3a0')
c.ellipse(55,24,4,4,'#a57732',False)
c.ellipse(55,24,3,3,'#f5d484',False)
c.set(53,21,'#fff1bf')
view(c)
finish(c)
