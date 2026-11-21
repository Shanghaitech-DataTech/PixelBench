# Sky pirate portrait — hand placed pixel clusters, 64 x 64.
c = new_canvas(64,64,background='#9fc7cb',name='Sky pirate girl')
P = {
'ink':'#25283e','deep':'#34344b','navyd':'#28374e','navy':'#354c68','navyl':'#4e6c86','navyh':'#708e9f',
'haird':'#713d39','hairm':'#a95b3b','hair':'#d18a4c','hairl':'#efb96a','hairh':'#ffe09a',
'skind':'#bc7263','skins':'#df9780','skin':'#f5bd98','skinl':'#ffdbaf',
'redd':'#782f43','red':'#bc3e4c','redl':'#eb6060','redh':'#ff9280',
'brassd':'#885744','brass':'#c18a4e','gold':'#ebc374','goldh':'#ffe6a3',
'lensd':'#315268','lens':'#4e8d9b','lensl':'#95d3d0','white':'#fff2d1','shirt':'#e3d9bc','shirts':'#a59f98',
'leather':'#6c4542','leatherl':'#97624a'
}
def poly(pts,col): c.poly(pts,P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x,y,X,Y,col): c.line(x,y,X,Y,P.get(col,col))
def pix(x,y,col): c.set(x,y,P.get(col,col))
# Quiet broken cloud banks, framing the open sky.
rect(0,14,10,3,'#b6d5d5');rect(0,17,16,2,'#b6d5d5');rect(3,12,5,2,'#b6d5d5')
rect(51,31,13,3,'#c6deda');rect(55,28,9,3,'#c6deda');rect(60,26,4,2,'#c6deda')
rect(0,53,9,2,'#b6d5d5');rect(0,55,13,2,'#b6d5d5')
# Hair silhouette: back of head and swept locks.
poly([(11,17),(17,14),(14,12),(23,11),(21,8),(31,9),(35,6),(40,8),(44,9),(48,14),(49,21),(47,29),(45,34),(39,40),(27,40),(23,37),(17,38),(20,33),(14,33),(18,28),(11,29),(15,23),(8,24),(13,20)],'ink')
poly([(14,18),(22,14),(19,13),(27,12),(25,10),(33,11),(36,8),(42,11),(46,15),(47,23),(43,32),(35,38),(25,37),(23,33),(18,35),(22,29),(17,30),(21,24),(14,26),(18,20)],'hairm')
poly([(17,18),(27,14),(23,13),(32,12),(35,9),(40,12),(44,13),(44,20),(37,26),(26,29),(22,31),(24,24),(18,25),(22,19)],'hair')
poly([(23,16),(31,13),(36,10),(38,12),(34,16),(25,20),(20,22)],'hairl')
line(17,28,24,23,'haird');line(23,34,28,28,'haird')
# Scarf tail streaming left, with two sharp loose ends.
poly([(34,40),(28,38),(23,35),(16,35),(12,32),(7,33),(10,37),(7,40),(15,42),(20,41),(27,45),(34,45)],'ink')
poly([(31,40),(24,37),(16,37),(10,34),(12,38),(10,39),(17,40),(22,39),(27,43),(33,44)],'red')
poly([(12,35),(18,37),(24,37),(28,39),(23,39),(17,38),(14,38)],'redl')
line(15,40,19,40,'redd')
# Upper body silhouette, cropped portrait lower edge.
poly([(29,41),(23,42),(18,45),(15,50),(12,58),(12,63),(54,63),(54,57),(51,49),(47,45),(41,42)],'ink')
poly([(25,44),(20,46),(17,51),(14,59),(14,63),(52,63),(52,57),(49,50),(46,47),(40,44)],'navy')
poly([(20,49),(18,53),(16,60),(17,63),(24,63),(24,52)],'navyd')
poly([(44,46),(48,49),(50,54),(51,60),(48,60),(46,52),(42,50)],'navyl')
line(18,53,16,59,'navyl');line(15,61,15,63,'navyh')
# Neck and cream flight shirt.
poly([(32,35),(41,35),(41,42),(44,45),(40,52),(30,49),(29,43),(33,40)],'ink')
poly([(34,36),(40,36),(39,42),(41,45),(36,48),(31,44),(34,40)],'skins')
poly([(36,37),(40,37),(39,43),(36,45),(34,43)],'skin')
poly([(32,46),(40,46),(43,55),(42,63),(29,63),(29,54)],'shirts')
poly([(34,47),(39,47),(41,55),(39,63),(31,63),(32,54)],'shirt')
line(36,51,36,62,'white')
# Open angular navy lapels.
poly([(27,43),(32,46),(32,53),(29,51),(28,56),(22,49)],'ink')
poly([(27,45),(30,47),(31,51),(28,49),(27,53),(24,49)],'navyl')
line(25,47,27,45,'navyh')
poly([(41,44),(46,47),(45,54),(43,52),(43,59),(38,49)],'ink')
poly([(42,46),(44,48),(44,51),(42,50),(42,54),(40,49)],'navyl')
# Face profile at three quarter angle.
poly([(31,18),(40,17),(45,20),(46,25),(46,28),(49,31),(47,33),(46,36),(42,40),(37,41),(31,38),(28,33),(27,26)],'ink')
poly([(32,19),(40,19),(44,21),(44,27),(45,30),(47,31),(45,33),(45,36),(41,39),(37,39),(32,37),(29,32),(29,26)],'skin')
poly([(33,21),(39,20),(43,22),(43,27),(44,31),(42,34),(43,36),(40,38),(36,37),(33,34)],'skinl')
poly([(30,26),(32,28),(32,34),(35,38),(38,39),(36,39),(31,36),(29,32)],'skins')
line(44,33,46,32,'skind')
pix(43,34,'skins');pix(42,34,'skins')
# Exposed ear and small hanging gold earring.
poly([(27,27),(30,28),(31,32),(29,35),(26,33),(25,30)],'ink')
poly([(27,28),(29,29),(30,32),(28,33),(26,31)],'skin')
line(27,30,28,31,'skind')
pix(28,34,'goldh');line(28,35,28,37,'brass');pix(28,38,'gold');pix(29,37,'goldh')
# Anime eyes, brows and a calm, lifted smile.
line(33,25,37,24,'haird');line(42,24,44,24,'haird')
line(32,27,34,26,'ink');line(34,26,38,26,'ink');pix(38,27,'ink')
rect(33,27,5,3,'white');rect(35,27,2,3,'lensd');pix(35,27,'lensl');pix(36,28,'ink');pix(35,29,'lens')
line(33,30,36,30,'skind');pix(32,27,'ink')
line(42,26,44,26,'ink');rect(42,27,3,2,'white');rect(43,27,2,2,'lensd');pix(43,27,'lensl');pix(44,28,'ink')
pix(41,30,'skins');line(33,32,35,32,'skins')
line(38,35,41,35,'skind');pix(42,34,'skind');line(39,36,41,36,'white')
# Side-swept bangs wrap across forehead; a long flying side lock.
poly([(29,17),(34,18),(33,22),(31,24),(30,28),(28,30),(27,27),(27,23),(23,26),(23,23),(20,24),(23,19)],'haird')
poly([(29,18),(32,19),(30,23),(28,27),(28,22),(24,24),(25,21),(22,22),(25,19)],'hairl')
line(25,22,28,19,'hairh')
poly([(36,18),(43,17),(46,20),(46,25),(44,24),(42,21),(38,20)],'haird')
poly([(37,18),(42,18),(44,20),(44,22),(41,20)],'hairl')
# Broad leather goggle strap across hair.
poly([(19,20),(22,15),(31,13),(42,11),(46,13),(47,17),(43,19),(32,19),(25,23),(20,24)],'ink')
poly([(21,20),(23,17),(31,15),(41,13),(44,14),(45,16),(40,17),(31,17),(24,21),(21,22)],'leather')
line(22,19,26,16,'leatherl')
pix(22,21,'gold')
# Brass goggles perched above the eyes: near large round lens, far foreshortened.
poly([(25,14),(28,12),(33,12),(36,15),(36,20),(33,23),(28,23),(24,20),(24,16)],'ink')
poly([(26,15),(29,13),(32,13),(35,15),(35,19),(32,22),(28,22),(25,19),(25,16)],'brass')
poly([(27,15),(29,14),(32,14),(34,16),(34,19),(32,21),(28,21),(26,19),(26,16)],'gold')
poly([(28,15),(31,15),(33,16),(33,19),(31,20),(28,20),(27,18),(27,16)],'lensd')
poly([(28,16),(31,16),(32,17),(32,19),(29,19),(28,18)],'lens')
line(28,17,30,15,'lensl');pix(31,16,'white');pix(26,15,'goldh');line(28,13,31,13,'goldh')
# Bridge and far lens.
line(36,15,38,15,'ink');line(36,16,38,16,'gold');pix(36,17,'brassd')
poly([(39,11),(43,11),(46,13),(47,16),(45,19),(41,20),(38,18),(37,14)],'ink')
poly([(40,12),(43,12),(45,14),(46,16),(44,18),(41,19),(39,17),(38,14)],'brass')
poly([(40,13),(43,13),(44,14),(45,16),(43,18),(41,18),(39,16),(39,14)],'gold')
poly([(41,14),(43,14),(44,16),(43,17),(41,17),(40,16),(40,14)],'lensd')
pix(41,14,'lensl');pix(42,14,'white');pix(42,15,'lens');pix(43,16,'lens');pix(40,12,'goldh')
# Wrapped red scarf with bright upper rim and knot.
poly([(31,39),(35,41),(40,41),(42,39),(43,43),(40,47),(35,48),(30,45),(29,42)],'ink')
poly([(31,41),(35,43),(40,43),(42,41),(42,43),(39,46),(35,46),(31,44)],'red')
line(31,41,35,43,'redl');line(35,43,39,43,'redl');pix(40,42,'redh')
poly([(32,44),(35,45),(37,46),(34,48),(31,46)],'redd')
poly([(32,44),(34,44),(35,46),(33,47),(31,46)],'redl')
poly([(34,47),(38,47),(38,52),(36,56),(35,53),(32,54)],'ink')
poly([(35,48),(37,48),(37,52),(36,54),(35,51),(34,52)],'red')
line(35,48,35,51,'redl')
# Flight coat gold shoulder piping and insignia.
poly([(20,45),(24,43),(27,44),(25,47),(22,48),(19,47)],'ink')
line(21,45,24,44,'gold');line(20,46,23,46,'brass');pix(25,44,'goldh')
line(46,48,49,51,'gold');pix(48,49,'goldh')
# Diagonal weathered harness, following the torso.
poly([(23,48),(26,48),(42,63),(35,63),(22,51)],'ink')
poly([(24,49),(25,49),(39,63),(36,63),(23,51)],'leather')
line(24,49,38,63,'leatherl')
# Buckle on chest.
poly([(29,53),(32,53),(36,57),(33,60),(29,56)],'brassd')
poly([(30,53),(32,54),(35,57),(33,59),(30,56)],'gold')
line(31,55,33,57,'leather');pix(33,56,'goldh');pix(30,54,'goldh')
# Coat breast aviation badge and small fastenings.
line(42,56,46,56,'brass');line(43,57,45,57,'gold');pix(44,55,'goldh')
pix(27,58,'gold');pix(28,61,'goldh')
line(47,60,49,60,'navyd');line(47,61,50,61,'navyh')
# A few clean hair glints above the goggles.
line(29,10,32,10,'hairl');pix(36,9,'hairh');line(40,10,42,11,'hairl')
# Continue the cropped jacket cleanly through the final canvas row.
c.select(0,62,64,1).copy_to(0,63,c)
# Grouped light on the wind-facing locks.
line(18,26,21,24,'hairl')
line(20,30,22,28,'hair')
pix(31,26,'ink')
print(c.stats_text())
print(c.matrix_text(region=(6,6,54,27)))
print(c.matrix_text(region=(12,40,54,63)))
save('sky-pirate-girl',c)
finish(c)
