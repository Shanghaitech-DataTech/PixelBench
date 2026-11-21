# 64 x 64 sky-pirate portrait; deliberately limited, opaque pixel clusters.
result = new_canvas(64, 64, name='sky_pirate_girl')
c = result
P = {
 'ink':'#20283d', 'deep':'#30304a',
 'hairdark':'#623b40', 'hairshade':'#955047', 'hair':'#c67950',
 'hairlight':'#e9a565', 'hairshine':'#ffd18a',
 'skinshadow':'#bd6960', 'skinshade':'#e39276', 'skin':'#ffc298', 'skinlight':'#ffdbb1',
 'white':'#fff0cd', 'eye':'#447d85', 'eyelight':'#83d3cc',
 'coatdark':'#263449', 'coat':'#344963', 'coatlight':'#4d6781', 'coatshine':'#708d9b',
 'redshadow':'#802f43', 'red':'#be3e4c', 'redlight':'#ee6257', 'redshine':'#ff9771',
 'goldshadow':'#896044', 'gold':'#d69b59', 'goldlight':'#f7cd7e',
 'glassdark':'#35586a', 'glass':'#548c9a', 'glasslight':'#96dbd6'
}
def poly(points, col): c.poly(points, P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x,y,xx,yy,col): c.line(x,y,xx,yy,P.get(col,col))
def dot(x,y,col): c.set(x,y,P.get(col,col))

# Swept silhouette, large shapes first. Hair streams to the left.
poly([(37,5),(42,9),(43,15),(42,21),(43,29),(39,37),(36,43),
      (27,46),(20,43),(12,44),(16,39),(7,39),(12,34),(4,34),(11,28),
      (6,28),(12,22),(10,18),(15,17),(16,12),(22,7),(30,5)], 'ink')
poly([(31,7),(37,7),(40,10),(41,17),(39,25),(39,34),(34,41),(27,43),
      (22,40),(15,42),(19,36),(10,37),(17,31),(8,32),(16,25),
      (13,21),(18,19),(18,14),(24,9)],'hairdark')
poly([(27,8),(34,7),(39,10),(40,16),(35,23),(32,30),(27,35),(19,38),
      (22,32),(13,33),(21,25),(16,25),(20,20),(18,17),(22,12)],'hair')
poly([(28,8),(35,8),(38,10),(29,11),(24,15),(20,21),(17,23),(19,16),(23,12)],'hairlight')
poly([(21,26),(27,19),(33,15),(36,17),(30,25),(25,29),(17,32)],'hairlight')
line(25,11,29,9,'hairshine')
line(21,15,23,13,'hairshine')
poly([(29,30),(35,25),(34,36),(30,40),(24,41)],'hairshade')
line(28,35,24,39,'hair')
# Separated swept locks keep the outer silhouette readable at native size.
poly([(16,24),(20,21),(18,26),(12,30),(14,27)],'hairshade')
line(14,28,17,25,'hair')
poly([(16,33),(20,30),(17,35),(13,36)],'hairshade')
poly([(20,38),(24,36),(23,40),(19,41)],'hair')
line(22,37,21,39,'hairlight')
line(15,21,17,20,'hairlight')
poly([(34,7),(37,7),(39,10),(38,12),(35,10),(31,9)],'hairlight')
line(33,7,35,7,'hairshine')

# Coat silhouette with short, tailored hem and forward shoulder.
poly([(25,41),(33,40),(39,40),(45,43),(49,48),(51,57),(49,62),
      (19,62),(15,60),(16,51),(19,46)],'ink')
poly([(23,44),(29,42),(36,42),(39,44),(44,44),(47,48),(49,57),(47,60),
      (20,60),(18,58),(19,51)],'coat')
poly([(19,51),(24,47),(27,51),(26,60),(19,60),(17,58)],'coatdark')
poly([(41,45),(45,46),(47,50),(49,58),(46,60),(43,57)],'coatlight')
line(45,48,47,54,'coatshine')
poly([(28,45),(35,44),(39,47),(38,60),(27,60)],'coatdark')
# Shirt glimpsed between lapels.
poly([(31,46),(36,45),(38,50),(34,58),(31,53)],'white')
poly([(35,48),(37,49),(34,57),(33,52)],'gold')
# Broad angular lapels.
poly([(25,43),(31,45),(30,50),(33,54),(27,52),(24,47)],'coatlight')
line(25,44,29,46,'coatshine')
poly([(38,44),(40,45),(42,50),(37,56),(38,49),(35,47)],'coatlight')
line(40,49,38,52,'coatshine')
# Small brass shoulder tabs echo the goggle rims.
line(20,48,23,45,'goldshadow')
line(20,47,22,45,'goldlight')
line(43,45,46,48,'coatdark')
line(43,44,46,47,'gold')
dot(43,44,'goldlight')
# Leather cross-body strap and metal buckle.
poly([(22,46),(24,46),(41,60),(37,60),(22,49)],'ink')
poly([(23,47),(24,48),(39,60),(37,60),(23,49)],'hairdark')
line(26,50,35,57,'goldshadow')
rect(29,53,5,5,'goldshadow'); rect(29,53,4,4,'goldlight'); rect(30,54,2,2,'hairdark')
dot(31,55,'gold')
# Hem, sleeve cuff, and coat buttons.
line(20,59,27,59,'coatlight')
line(42,59,47,59,'coatdark')
rect(44,57,5,2,'coatdark'); line(45,57,48,57,'gold')
dot(39,55,'goldlight'); dot(41,58,'gold')

# Scarf tail lifted behind the head, swept leftward.
poly([(31,42),(26,39),(21,38),(16,40),(11,42),(4,40),(7,45),(5,48),
      (13,47),(20,44),(27,46)],'ink')
poly([(28,42),(24,40),(20,40),(15,42),(9,44),(6,42),(8,45),(7,46),
      (13,45),(21,42),(26,44)],'red')
line(9,44,14,43,'redlight')
line(16,42,21,40,'redlight')
line(22,40,25,41,'redshine')
poly([(13,45),(20,42),(24,42),(27,44),(23,43),(17,44)],'redshadow')

# Neck, in front of the trailing scarf.
poly([(32,34),(41,35),(40,41),(43,43),(37,48),(29,44)],'ink')
poly([(33,36),(39,37),(38,41),(40,43),(36,45),(31,43)],'skinshade')
poly([(35,39),(39,38),(38,42),(36,44),(33,42)],'skin')

# Three-quarter face: small projecting nose and a softly angular jaw.
poly([(30,15),(37,15),(42,18),(45,23),(45,29),(47,31),(46,33),
      (44,34),(43,38),(39,41),(35,42),(30,39),(27,35),(26,29),(27,22)],'ink')
poly([(31,17),(37,17),(41,19),(43,23),(43,29),(45,31),(45,32),
      (42,33),(42,37),(38,40),(35,40),(31,38),(29,34),(28,28),(29,22)],'skin')
poly([(36,18),(40,20),(42,25),(41,29),(44,31),(41,34),(40,37),(36,39),
      (34,37),(31,34),(30,28),(31,23)],'skinlight')
poly([(29,24),(31,27),(30,32),(32,36),(35,39),(38,40),(35,40),(31,38),(29,35),(27,29)],'skinshade')
line(42,31,44,32,'skinshade')
dot(44,31,'skinlight')
# Ear tucked under the near temple, with a brass hoop.
poly([(28,28),(25,27),(23,29),(24,33),(27,35),(29,33)],'ink')
poly([(26,29),(25,29),(25,32),(27,33),(28,31)],'skinshade')
line(25,30,26,31,'skinshadow')
dot(27,29,'skinlight')
rect(25,33,3,5,'goldshadow'); rect(24,34,4,3,'gold'); rect(25,34,2,2,'hairdark'); dot(25,37,'goldlight'); dot(24,34,'white')

# Eyes and cocked eyebrows, drawn as designed pixel clusters.
line(31,23,34,22,'hairdark'); line(35,22,37,23,'hairdark')
line(41,23,43,24,'hairdark')
# Near eye: upswept lashes and a bright blue-green iris.
line(30,25,32,26,'ink'); line(32,26,37,26,'ink'); dot(38,27,'ink')
rect(32,27,6,3,'white'); rect(34,27,3,4,'eye'); rect(35,27,2,2,'ink')
dot(34,27,'white'); dot(34,29,'eyelight'); dot(35,30,'eyelight')
line(31,29,32,30,'skinshadow'); dot(33,31,'skinshadow'); dot(37,30,'skinshadow')
# Far eye is narrower in perspective, still clearly separated from the nose.
line(41,26,43,26,'ink'); rect(41,27,3,3,'white'); rect(42,27,2,3,'eye')
dot(43,27,'ink'); dot(42,27,'white'); dot(42,29,'eyelight')
# Nose, cheek and a small, upward-tipped smile.
dot(43,32,'skinshadow'); line(31,33,33,33,'skinshade')
line(37,36,39,36,'skinshadow'); line(40,35,41,35,'hairdark')
line(38,37,40,36,'white'); dot(38,39,'skinshade')

# Wind-driven fringe and side locks overlay the face edge.
poly([(24,17),(29,13),(34,14),(39,17),(41,21),(37,20),(33,18),
      (31,23),(28,27),(29,21),(25,27),(26,22),(22,25)],'hairdark')
poly([(26,17),(30,15),(34,15),(38,18),(39,19),(34,17),(31,18),
      (29,22),(28,23),(29,18),(25,23)],'hair')
line(29,16,32,16,'hairlight')
poly([(22,23),(25,19),(25,26),(22,32),(19,33)],'hairdark')
line(23,24,22,28,'hairlight')

# Goggle strap and paired brass rims sit on the top of her head.
poly([(17,15),(22,12),(34,11),(42,13),(43,17),(38,18),(24,16),(18,19)],'ink')
line(18,16,23,14,'hairdark'); line(18,17,22,15,'goldshadow')
# Left, near lens -- large octagonal housing.
poly([(23,9),(29,8),(33,10),(35,14),(33,18),(27,20),(23,18),(21,14)],'ink')
poly([(24,10),(29,9),(32,11),(33,14),(31,17),(27,18),(24,17),(23,14)],'gold')
line(24,10,29,9,'goldlight'); line(23,11,23,14,'goldlight')
poly([(25,11),(29,11),(31,12),(31,15),(29,17),(26,17),(24,15),(24,12)],'glassdark')
poly([(25,12),(29,12),(30,13),(30,15),(28,16),(25,15)],'glass')
line(25,13,28,12,'glasslight'); dot(25,12,'white'); dot(26,16,'glasslight')
dot(31,17,'goldshadow'); dot(27,19,'goldshadow')
# Bridge and far lens: noticeably narrower in perspective.
line(33,12,35,12,'goldlight'); line(33,13,35,13,'goldshadow')
poly([(36,10),(40,10),(43,12),(44,16),(42,19),(38,19),(35,16),(35,12)],'ink')
poly([(37,11),(40,11),(42,13),(42,16),(41,18),(38,17),(36,15),(36,12)],'gold')
line(37,11,40,11,'goldlight')
poly([(38,12),(40,12),(41,14),(41,16),(39,16),(37,14)],'glassdark')
line(38,13,40,14,'glasslight'); dot(38,12,'white'); dot(40,16,'glass')
dot(42,17,'goldshadow')

# Scarf collar and a compact knot are foremost at the base of the face.
poly([(29,39),(32,41),(37,42),(40,40),(42,42),(39,46),(34,47),(29,44),(27,42)],'ink')
poly([(29,40),(32,42),(36,43),(40,41),(40,43),(37,45),(33,45),(29,43)],'red')
line(30,41,33,43,'redlight'); line(34,43,37,43,'redlight')
line(32,45,35,46,'redshadow')
poly([(36,45),(40,44),(41,47),(38,50),(35,48)],'redshadow')
poly([(37,45),(39,45),(39,47),(37,48),(36,47)],'redlight')
poly([(39,48),(41,49),(41,54),(38,52),(37,49)],'ink')
poly([(39,49),(40,50),(40,52),(38,51)],'red')

# Optical centering leaves breathing room for the face and the streaming scarf.
result.shift(4, -1)
assert result.stats()['size'] == (64, 64) or result.stats()['size'] == [64, 64]
assert result.stats()['colors_used'] <= 86
view(result, scale=8, margin=0)
save('sky-pirate-girl', result)
finish(result)
