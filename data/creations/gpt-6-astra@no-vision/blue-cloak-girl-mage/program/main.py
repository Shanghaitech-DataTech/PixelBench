# Blue-cloak girl mage, 64 x 64 RPG sprite.
result = new_canvas(64, 64, name="blue_cloak_girl_mage")
c = result
P = {
'ink':'#141d36', 'deep':'#202c50', 'shade':'#273b68',
'blue':'#345585', 'mid':'#426c9e', 'light':'#638db5',
'seam':'#89a8ca', 'hairdark':'#666d91', 'hair':'#a4acc6',
'hairlight':'#d9dfeb', 'white':'#f3f1e8', 'bootshadow':'#a6b8cb',
'bootmid':'#d4dee4', 'skinshade':'#c98780', 'skin':'#efb49c',
'skinlight':'#ffdbc0', 'blush':'#e59991', 'eye':'#42608b',
'wood':'#81503e', 'woodlight':'#ba8050', 'goldshade':'#b97936',
'gold':'#e5ae52', 'amber':'#ffcb64', 'glow':'#fff0b2'
}
for n,v in P.items(): c.color(v,n)
# A small, stepped halo surrounds the staff's light.
c.ellipse(49,13,7,8,'#e7a63d12')
c.ellipse(49,13,5,6,'#ffc85b20')
# Staff shaft, at a slight relaxed angle.
c.line(48,20,46,58,'ink')
c.line(49,20,47,58,'ink')
c.line(47,20,45,58,'ink')
c.line(48,21,46,57,'wood')
c.line(47,23,45,56,'woodlight')
c.set(46,57,'goldshade')
c.set(46,58,'gold')
# Two curved gold prongs cradle a floating crystal.
c.path('M 47 23 L 47 20 Q 41 17 43 11 L 45 8 L 45 13 Q 44 17 49 18 Q 54 16 54 12 L 53 8 L 56 11 Q 58 17 51 21 L 50 24 Z','ink')
c.path('M 48 22 L 48 19 Q 43 17 44 12 L 45 11 L 45 15 L 47 18 L 50 19 L 53 17 L 55 14 L 55 11 L 56 13 L 55 17 L 50 21 L 49 23 Z','goldshade')
c.line(44,13,44,16,'gold')
c.line(45,17,48,19,'amber')
c.line(51,19,54,16,'gold')
c.rect(47,22,3,2,'gold')
c.line(47,24,49,24,'goldshade')
# Tall luminous amber gem.
c.poly([(49,6),(52,11),(51,15),(49,17),(46,13),(47,9)],'goldshade')
c.poly([(49,7),(51,11),(50,15),(49,16),(47,12)],'amber')
c.poly([(49,7),(49,14),(47,12)],'glow')
c.set(50,11,'white')
c.line(58,6,58,8,'amber'); c.line(57,7,59,7,'glow')
c.set(42,8,'gold'); c.set(54,3,'amber')
# Boots behind the coat, clearly separated by a transparent gap.
c.poly([(22,45),(29,45),(29,56),(30,58),(29,60),(21,60),(20,58),(22,55)],'ink')
c.poly([(32,45),(38,45),(38,55),(40,57),(40,59),(32,59),(31,57)],'ink')
c.poly([(23,47),(28,47),(28,56),(27,58),(22,58),(23,55)],'bootmid')
c.poly([(24,48),(27,48),(27,55),(25,56),(23,56)],'white')
c.line(22,59,28,59,'bootshadow')
c.line(23,49,28,49,'bootshadow')
c.poly([(33,47),(37,47),(37,55),(39,57),(38,58),(33,58)],'bootmid')
c.poly([(33,48),(36,48),(36,55),(38,56),(37,57),(33,56)],'white')
c.line(33,49,37,49,'bootshadow')
c.line(33,58,39,58,'bootshadow')
# Broad cloak silhouette; asymmetry gives the relaxed stance some weight.
c.poly([(23,23),(34,23),(39,27),(40,33),(43,46),(41,49),(35,51),(25,51),(18,50),(12,47),(15,38),(17,30)],'ink')
c.poly([(22,25),(28,25),(26,35),(24,47),(22,49),(17,48),(14,46),(17,36),(19,29)],'blue')
c.poly([(18,32),(21,29),(20,39),(17,46),(14,46)],'mid')
c.poly([(22,30),(25,28),(23,41),(22,48),(19,48)],'shade')
c.line(15,47,20,49,'light')
c.poly([(32,25),(36,25),(38,29),(38,37),(41,46),(39,48),(33,50),(30,47),(31,37)],'shade')
c.poly([(35,29),(37,30),(36,38),(39,46),(36,48),(33,43)],'blue')
c.line(38,43,40,47,'mid')
c.line(35,49,39,48,'light')
# Simple pale tunic framed by the open cloak.
c.poly([(25,26),(32,26),(34,37),(32,41),(24,41),(23,36)],'ink')
c.poly([(26,27),(31,27),(32,36),(30,39),(25,38)],'bootmid')
c.poly([(27,28),(30,28),(30,35),(26,35)],'white')
c.poly([(25,36),(32,36),(33,40),(24,40)],'blue')
# Belt and short, flared skirt.
c.rect(24,37,9,3,'deep')
c.rect(28,37,3,3,'goldshade'); c.rect(29,38,1,1,'amber')
c.poly([(24,40),(33,40),(35,47),(32,49),(23,49),(21,47)],'ink')
c.poly([(25,40),(32,40),(33,46),(31,47),(23,47)],'blue')
c.poly([(25,41),(27,41),(26,46),(23,46)],'mid')
c.line(30,42,31,46,'shade')
c.line(23,48,31,48,'seam')
# Left sleeve and dangling hand.
c.poly([(19,28),(22,31),(20,37),(21,39),(17,42),(14,38),(16,31)],'ink')
c.poly([(18,30),(20,31),(18,37),(19,39),(17,40),(15,37)],'blue')
c.line(17,32,16,36,'light')
c.poly([(17,39),(19,39),(20,42),(19,44),(17,43),(16,41)],'skinshade')
c.rect(17,40,2,3,'skin'); c.set(17,40,'skinlight')
c.line(16,38,18,39,'gold')
# Bent right sleeve reaches out to the staff.
c.poly([(35,27),(38,27),(41,31),(44,30),(46,32),(44,36),(39,36),(35,33)],'ink')
c.poly([(36,29),(38,29),(40,33),(43,32),(44,34),(40,35),(37,33)],'blue')
c.line(37,29,40,32,'mid')
c.line(43,32,44,34,'gold')
c.poly([(45,30),(48,30),(49,32),(48,34),(45,34),(44,32)],'skinshade')
c.rect(45,30,3,2,'skin'); c.line(45,30,47,30,'skinlight'); c.set(46,32,'skin')
# Hood outer contour, with one soft drooping tip.
c.path('M 18 24 L 17 18 Q 17 10 23 7 L 28 5 L 33 5 L 36 7 L 40 12 L 39 16 L 36 14 L 37 20 L 36 25 L 32 28 L 24 28 Z','ink')
c.path('M 19 23 L 18 18 Q 19 11 24 8 L 29 6 L 33 7 L 36 10 L 38 13 L 36 12 L 34 11 L 35 20 L 34 24 L 30 26 L 24 26 Z','blue')
c.path('M 20 15 Q 21 10 27 8 L 31 7 L 33 9 L 26 10 L 23 13 L 21 18 L 20 22 Z','mid')
c.line(24,9,29,7,'light')
c.poly([(33,9),(36,11),(38,14),(36,13),(35,14),(35,19),(33,24),(31,24)],'shade')
# Hood opening and hair mass.
c.path('M 20 17 Q 21 11 28 11 Q 34 11 35 17 L 35 24 L 32 27 L 24 27 L 20 24 Z','ink')
c.path('M 21 18 Q 21 13 27 12 Q 33 11 34 17 L 34 24 L 31 26 L 23 25 L 21 23 Z','hairdark')
# Neck beneath the chin.
c.rect(27,24,4,4,'skinshade'); c.rect(28,25,2,3,'skin')
# Face: broad anime proportions and small chin.
c.poly([(23,16),(32,16),(33,19),(32,23),(29,26),(27,26),(23,23),(22,20)],'skinshade')
c.poly([(24,16),(31,16),(32,19),(31,23),(29,25),(27,25),(24,23),(23,20)],'skin')
c.poly([(24,17),(30,17),(31,20),(30,23),(27,24),(24,22)],'skinlight')
# Eyes, a single dark upper lash, cool blue iris, tiny light.
c.line(24,19,26,19,'ink'); c.line(29,19,31,19,'ink')
c.set(24,20,'white'); c.set(25,20,'eye'); c.set(26,20,'ink')
c.set(29,20,'white'); c.set(30,20,'eye'); c.set(31,20,'ink')
c.set(25,21,'eye'); c.set(30,21,'eye')
c.set(23,22,'blush'); c.set(31,22,'blush'); c.set(28,24,'skinshade')
# Chunky silver bangs, sweeping to the side; two face-framing locks.
c.poly([(21,18),(22,15),(25,13),(30,13),(33,15),(34,19),(32,21),(31,17),(29,16),(27,19),(27,17),(24,19),(24,17),(22,21)],'hair')
c.poly([(23,15),(26,13),(30,14),(28,15),(26,17),(26,16),(23,18)],'hairlight')
c.line(30,15,32,17,'hairlight')
c.poly([(21,19),(23,19),(23,23),(25,26),(22,25),(21,23)],'hair')
c.line(22,20,22,23,'hairlight')
c.poly([(33,19),(34,18),(34,23),(32,26),(31,25),(33,23)],'hair')
c.set(33,21,'hairlight')
# Folded hood collar and amber clasp.
c.poly([(22,25),(26,27),(28,28),(25,31),(22,29),(20,26)],'ink')
c.poly([(22,26),(26,28),(25,29),(22,28)],'mid')
c.poly([(32,25),(35,25),(36,27),(33,30),(29,29)],'ink')
c.poly([(33,26),(35,26),(33,28),(30,29)],'blue')
c.line(23,27,25,28,'seam')
c.rect(27,28,3,3,'goldshade'); c.set(28,28,'glow'); c.set(28,29,'amber')
print(c.stats_text())
print(c.matrix_text(region=(10,28,51,60)))
save('blue_cloak_girl_mage', result)
finish(result)
