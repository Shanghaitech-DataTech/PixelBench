# Shared palette and enlarged animation stage.
f1=new_canvas(94,70,name='01-ready')
f1.blit(input_canvas,6,4)
f2=new_canvas(94,70,name='02-release')
P={item['index']:item['rgba'] for item in input_canvas.palette()}
def col(x,y): return P[input_canvas.get(x,y)]
black='#010202'; ink='#0b0b13'; dark='#211d2c'; seam='#443d45'; blue='#455363'; red='#4a222d'; brown='#7d423a'; deep='#240b0c'; edge='#0b0102'; skin='#dfb2ac'
# Legs and split coat: rear leg anchors the thrust, left leg steps forward.
f2.poly([(23,35),(32,37),(30,46),(24,52),(17,61),(11,62),(13,55),(17,46)],black)
f2.poly([(23,38),(28,39),(25,47),(20,52),(16,59),(12,59),(16,50),(19,44)],blue)
f2.poly([(26,39),(29,40),(26,47),(23,50),(20,54),(18,54),(21,48)],seam)
f2.poly([(12,57),(17,58),(16,62),(18,64),(19,67),(9,67),(7,66),(10,63)],black)
f2.poly([(12,58),(16,59),(14,63),(17,65),(17,66),(9,66),(11,63)],red)
f2.line(12,59,14,60,deep)
f2.set(10,65,brown)
# Forward thigh, bent knee and shin.
f2.poly([(29,36),(36,37),(39,41),(43,47),(44,51),(41,59),(43,62),(38,64),(34,61),(35,54),(35,50),(30,46),(27,42)],black)
f2.poly([(30,38),(35,39),(37,43),(41,48),(41,52),(38,59),(35,59),(37,50),(32,46),(29,42)],blue)
f2.poly([(35,40),(38,44),(42,48),(42,51),(40,56),(38,58),(38,53),(39,49)],seam)
f2.line(31,41,36,48,'#6a6c6b')
f2.poly([(36,58),(41,59),(41,61),(46,62),(49,64),(50,66),(38,66),(35,64)],black)
f2.poly([(37,59),(40,60),(40,62),(45,63),(47,65),(39,65),(36,63)],red)
f2.line(40,63,44,64,brown)
f2.line(38,66,48,66,dark)
# Flared coat tails in the gap between legs.
f2.poly([(24,36),(32,36),(34,43),(36,48),(31,53),(28,56),(22,56),(24,52),(28,47),(27,43),(22,48),(18,52),(16,52),(19,45)],black)
f2.poly([(25,39),(29,39),(31,44),(32,48),(27,53),(23,54),(27,49),(28,45)],dark)
f2.poly([(29,39),(32,40),(34,47),(30,52),(26,54),(25,53),(30,48)],blue)
f2.line(20,48,18,51,seam)
# Reuse the original hood, cloak and upper body with a forward lean.
for y in range(34):
    lean=round(10*(33-y)/33)
    for x in range(47):
        rgba=col(x,y)
        if not rgba[3] or tuple(rgba[:3]) in [(242,114,25),(244,163,12),(254,211,44)]: continue
        # The casting arm is placed separately, at full extension.
        if x>=29 and 20<=y<=25: continue
        f2.set(x+9+lean,y+6,rgba)
# Extended sleeve, cuff and open casting hand.
f2.poly([(38,25),(43,25),(47,26),(52,25),(54,26),(54,30),(50,32),(45,31),(40,31)],black)
f2.poly([(40,26),(44,26),(47,27),(51,26),(52,29),(49,30),(44,30),(42,29)],red)
f2.line(44,26,47,27,brown)
f2.poly([(48,26),(51,25),(53,26),(53,29),(50,30),(48,29)],blue)
f2.line(49,26,51,26,'#6a6c6b')
f2.line(49,29,52,29,ink)
f2.poly([(53,26),(55,25),(56,23),(57,23),(57,25),(59,25),(59,26),(56,27),(59,27),(59,28),(56,29),(53,28)],seam)
f2.line(54,26,56,25,skin)
f2.line(56,25,58,25,skin)
f2.line(54,27,57,27,skin)
f2.set(56,24,skin)
f2.line(42,26,42,29,ink)
# Fire streak, streaming from the casting hand to a detached blazing head.
orange='#f27219'; gold='#f4a30c'; yellow='#fed32c'; hot='#fff1a1'; ember='#b94020'
f2.poly([(61,27),(66,26),(70,26),(67,23),(72,24),(75,23),(73,20),(78,21),(81,22),(84,24),(87,27),(84,30),(81,32),(76,33),(70,31),(66,31),(69,29),(64,29)],orange)
f2.poly([(64,27),(70,27),(73,26),(77,23),(81,24),(84,26),(85,28),(81,30),(77,31),(73,29),(68,29)],gold)
f2.poly([(69,28),(74,27),(78,24),(80,25),(80,26),(83,27),(82,29),(77,30),(74,28)],yellow)
f2.poly([(75,27),(78,25),(79,26),(79,27),(82,28),(78,29),(75,28)],hot)
# Long, broken trailing tongues emphasize forward travel.
f2.poly([(68,24),(65,21),(69,22),(72,24)],orange)
f2.poly([(73,31),(76,34),(80,34),(78,32)],orange)
f2.line(59,23,62,23,orange)
f2.set(64,21,gold)
f2.line(63,32,67,32,ember)
f2.set(61,30,orange)
f2.set(72,18,orange)
f2.set(82,20,gold)
f2.line(56,31,58,31,ember)
# Small folds echo the original garment's pixel texture.
f2.line(17,50,19,48,ink)
f2.line(15,54,16,52,seam)
f2.set(17,51,'#6a6c6b')
f2.line(21,44,23,42,seam)
f2.line(37,49,39,50,ink)
f2.line(36,55,37,53,seam)
f2.set(39,51,blue)
f2.line(37,60,38,61,seam)
f2.line(38,46,40,48,blue)
f2.set(41,49,ink)
f2.line(39,52,38,54,ink)
f2.set(36,57,'#6a6c6b')
f2.line(36,60,37,62,deep)
f2.set(40,62,seam)
f2.line(37,64,39,64,edge)
f2.line(11,63,12,61,edge)
f2.set(15,64,seam)
f2.set(47,28,deep)
f2.line(44,30,46,30,deep)
f2.set(51,27,seam)
f2.set(56,25,'#f3c58b')
f2.line(77,32,80,31,'#df5b1b')
f2.set(83,29,'#df5b1b')
# Verify the preserved frame pixel-for-pixel inside the larger stage.
for y in range(63):
    for x in range(47):
        assert f1.get(x+6,y+4)==input_canvas.get(x,y)
assert f1.stats()['size']==f2.stats()['size']
save('release-flames-01',f1)
save('release-flames-02',f2)
view(f1,scale=6)
view(f2,scale=6)
finish([f1,f2])
