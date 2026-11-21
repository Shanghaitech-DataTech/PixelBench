c = new_canvas(64,64,background='#aacbd7',name='offshore')
# sky bands and spare clouds
c.rect(0,22,64,16,'#c0d9df')
c.rect(2,13,13,2,'#dce9e8'); c.rect(5,11,7,2,'#dce9e8')
c.rect(40,6,16,2,'#dce9e8'); c.rect(46,4,7,2,'#dce9e8')
# distant turbines
for x,y,base in [(10,26,41),(52,24,40)]:
 c.line(x,y,x,base,'#7799a6'); c.line(x+1,y+1,x+1,base,'#e4eeee')
 c.line(x,y,x-7,y-4,'#eef3ee'); c.line(x,y,x+6,y-5,'#eef3ee'); c.line(x,y,x+1,y+8,'#eef3ee')
 c.set(x,y,'#668896')
# sea
c.rect(0,39,64,25,'#377b92');c.rect(0,39,64,2,'#649da9')
c.rect(0,49,64,15,'#286479')
for x,y,w in [(0,43,8),(14,42,7),(44,43,9),(56,41,7),(2,47,13),(45,48,13),(13,52,9),(0,57,12),(42,55,14),(51,61,12),(21,61,13)]:
 c.rect(x,y,w,1,'#75afba');c.rect(x+2,y+1,max(1,w-5),1,'#498fa0')
# main tower: huge machine extends beyond frame
c.poly([(26,0),(32,0),(34,52),(24,52)],'#344e5c')
c.poly([(27,0),(31,0),(32,47),(26,47)],'#d3e1df')
c.rect(27,0,2,46,'#edf0df'); c.line(31,0,32,46,'#94adb4')
# foundation, waterline
c.rect(24,43,10,11,'#bb8741'); c.rect(24,44,3,9,'#edbc57'); c.rect(32,43,2,11,'#836344')
c.ellipse(29,55,10,2,'#204e65'); c.line(19,54,24,54,'#a0c7ca');c.line(33,55,40,55,'#8ab9bf')
# steel platform underside and diagonal bracing
c.line(18,40,26,48,'#263d4b');c.line(40,40,33,48,'#263d4b')
c.line(19,40,26,46,'#77909a');c.line(39,40,33,46,'#77909a')
c.rect(17,37,26,3,'#263d4b');c.rect(17,37,26,1,'#c2cdbe');c.rect(19,40,22,1,'#536e77')
# railings, yellow galvanized access rails
c.line(17,30,24,30,'#e9bd60');c.line(34,30,42,30,'#e9bd60')
c.line(17,33,24,33,'#b88943');c.line(34,33,42,33,'#b88943')
for x in [17,23,35,42]: c.line(x,30,x,37,'#e9bd60')
# service panel
c.rect(28,31,4,6,'#5c7780');c.rect(29,32,2,4,'#9fb7b9');c.set(30,34,'#263d4b')
# ladder down right side, dark rails and light rungs
c.line(38,38,38,57,'#203f4f');c.line(43,37,43,57,'#203f4f')
c.line(39,38,39,57,'#b7c6bc');c.line(44,37,44,57,'#b7c6bc')
for y in range(39,58,3): c.line(39,y,44,y,'#8da8ab')
# climber, approximately 11px tall: boots and bent limbs
c.line(40,48,40,51,'#203241');c.line(40,51,42,51,'#203241')
c.line(42,47,44,49,'#243c4a');c.set(44,50,'#182e3d')
c.rect(40,44,3,4,'#e77830');c.line(40,44,39,42,'#f6a044');c.set(39,41,'#e0c1a0')
c.line(42,44,44,43,'#f6a044');c.set(44,42,'#e0c1a0')
# safety harness and helmet
c.line(40,45,42,47,'#f7d96d');c.line(42,45,40,47,'#473b38');c.rect(40,47,3,1,'#233b48')
c.rect(40,42,3,2,'#e3b28a');c.set(42,43,'#695746')
c.rect(40,40,3,2,'#ffd76a');c.line(39,42,43,42,'#f5be45');c.set(40,40,'#fff0ad')
# safety tether to railing
c.line(41,45,37,42,'#d6b65b');c.line(37,42,37,36,'#d6b65b')
view(c)
finish(c)
