# 64px subway platform, a restricted cool/warm palette
result = new_canvas(64,64,background='#172535',name='subway-platform')
c=result
ink='#101b2a'; deep='#223447'; wall='#344b5a'; steel='#66848a'; light='#a4b9ac'; cream='#e6d8a5'; yellow='#edb95c'
# station shell and receding overhead beams
c.rect(0,0,64,9,deep)
c.poly([(0,0),(20,0),(63,8),(63,11)],'#3e5560')
c.line(0,2,63,12,'#6d8182')
c.rect(0,11,64,27,wall)
c.line(0,13,63,13,'#77908d')
c.rect(0,15,64,22,ink)
# arriving train: horizontally stretched shell and swept nose at right
c.poly([(0,17),(49,17),(56,20),(61,27),(61,35),(0,35)],'#91a9a6')
c.rect(0,18,49,1,'#d5d5b7')
c.rect(0,31,59,4,'#526c79')
c.rect(0,29,58,2,'#df9857')
# window band
c.rect(0,20,49,8,'#243f55')
for x in [7,21,35,48]:
    c.rect(x,19,2,10,'#718c92')
for x in [0,12,26,40]:
    c.line(x,21,x+6,21,'#6d99a7')
    c.line(x,25,x+4,25,'#41657b')
c.poly([(50,20),(54,21),(59,27),(51,27)],'#1b3046')
c.line(51,21,55,24,'#7098a1')
c.rect(58,29,3,2,cream)
c.line(0,34,59,34,'#b6c1ae')
# speed streaks, behind the screen doors
for x,y,w in [(0,16,16),(23,16,12),(2,23,11),(16,26,13),(0,30,9),(30,32,14)]:
    c.rect(x,y,w,1,'#b5cac0' if y<20 else '#7097a4')
# platform screen doors - distinct upper rail and repeating dark pillars
c.rect(0,35,64,5,'#293e4c')
c.line(0,37,63,37,'#7c9795')
c.rect(0,23,64,2,'#172c3b')
c.line(0,23,63,23,'#91aaa6')
for x in [3,18,33,48,63]:
    c.rect(x,23,2,16,ink)
    c.line(x,25,x,35,'#64818a')
for x in [11,26,41,56]:
    c.line(x,25,x,35,'#7e9c9e')
    c.rect(x-1,29,3,2,'#e6c473')
    c.line(x-4,26,x-2,28,'#9ab1b0')
# foreground platform, tactile warning edge and depth lines
c.rect(0,40,64,24,'#4d6068')
c.rect(0,40,64,3,'#c79850')
c.line(0,40,63,40,'#f2d284')
for x in range(0,64,4): c.set(x,42,'#806545')
c.line(0,44,63,44,'#253c4b')
c.line(0,52,63,52,'#60727a')
c.line(0,62,63,62,'#60727a')
for a,b in [(6,0),(24,19),(41,44),(56,63)]: c.line(a,45,b,63,'#3b515e')
# station signage, suspended overhead
c.line(26,4,26,8,ink); c.line(48,7,48,8,ink)
c.rect(22,8,31,9,ink)
c.line(23,8,51,8,'#6a8489')
glyphs = ['111100110100111', '010101111101101', '111100111001111', '111010010010010']
for i,g in enumerate(glyphs):
    for k,v in enumerate(g):
        if v=='1': c.set(25+i*4+k%3,10+k//3,cream)
c.line(46,12,50,12,yellow); c.line(48,10,50,12,yellow); c.line(48,14,50,12,yellow)
# platform number panel on left
c.rect(2,6,10,10,'#182c3c'); c.rect(2,6,2,10,yellow)
c.text(5,8,'2',cream)
# ceiling strip lamp
c.line(4,1,21,4,'#e2dcbc'); c.line(5,2,22,5,'#829b99')
# bench and legs
c.ellipse(40,55,10,2,'#354a57')
c.rect(33,43,15,5,ink)
c.rect(34,43,13,2,'#b78961'); c.line(34,46,46,46,'#dbad74')
c.rect(32,49,17,2,ink); c.line(33,49,47,49,'#d1a171')
c.rect(34,51,2,4,ink); c.rect(45,51,2,4,ink)
# passenger 1: waiting, long rust coat and suitcase
c.ellipse(12,57,7,2,'#334855')
c.rect(9,30,5,2,ink); c.rect(8,32,6,5,ink)
c.rect(10,32,4,4,'#d8aa80'); c.set(13,35,'#f0c397')
c.rect(9,36,4,2,'#e6c58f')
c.poly([(8,37),(13,37),(15,47),(14,50),(7,50)],'#b85f4d')
c.line(8,38,8,45,'#e39368'); c.line(12,39,14,45,'#803f43')
c.rect(9,50,2,6,ink); c.rect(13,50,2,6,ink)
c.rect(8,56,4,2,'#111d2b'); c.rect(13,56,4,2,'#111d2b')
c.line(14,43,16,46,'#d8aa80')
c.rect(17,46,3,3,ink,fill=False)
c.rect(16,49,6,7,'#182c3b'); c.line(17,50,17,54,'#668b95')
c.set(17,56,ink); c.set(20,56,ink)
# passenger 2: seated on bench, looking at phone
c.rect(37,34,5,3,ink); c.rect(37,36,4,4,'#b88061'); c.set(41,37,'#b88061')
c.poly([(36,40),(40,40),(42,46),(41,49),(35,48)],'#6e9f96')
c.line(36,41,35,46,'#acd0b1')
c.line(39,42,42,44,'#507a7c'); c.line(42,44,44,41,'#b88061')
c.rect(44,39,2,3,ink); c.set(44,39,'#a9ded0')
c.poly([(36,48),(42,48),(43,51),(43,55),(41,55),(40,51),(36,51)],'#273247')
c.line(37,50,37,55,ink); c.rect(36,55,3,2,ink); c.rect(41,55,4,2,ink)
# passenger 3: walking, asymmetric arms and separated legs
c.ellipse(55,60,8,2,'#334855')
c.rect(54,32,5,3,ink); c.rect(55,34,4,4,'#edbd8d'); c.set(59,35,'#edbd8d')
c.rect(54,37,4,3,'#e1d8b2')
c.poly([(53,39),(58,39),(60,48),(57,51),(52,49)],'#d3bb70')
c.line(54,40,53,47,'#f2d894')
# dark shoulder bag at back
c.line(56,39,52,47,'#4c5360'); c.rect(50,44,4,7,'#3b5264'); c.line(50,45,50,48,'#7c9197')
c.line(58,41,60,45,'#a88957'); c.line(60,45,62,44,'#edbd8d')
c.poly([(53,49),(56,50),(54,55),(51,59),(49,58),(52,53)],'#1c293b')
c.poly([(56,49),(58,49),(58,54),(61,58),(59,60),(56,55)],'#28394d')
c.rect(48,58,4,2,ink); c.rect(59,59,4,2,ink)
assert result.stats()['colors_used'] <= 86
view(result)
finish(result)
