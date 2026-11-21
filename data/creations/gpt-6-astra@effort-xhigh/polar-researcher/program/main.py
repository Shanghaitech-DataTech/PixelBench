# Polar field researcher, leaning into a headwind.
result = new_canvas(48, 48, name="polar_researcher")
c = result
P = {
 'ink':'#162b40', 'deep':'#203c53', 'navy':'#2d5069', 'slate':'#416b80',
 'ice':'#9dd8e7', 'glint':'#e5fbf8', 'blue':'#579fb9',
 'red0':'#713b44', 'red1':'#aa4e48', 'red2':'#d46750', 'red3':'#ef8a61', 'red4':'#ffc08a',
 'fur0':'#8b8079','fur1':'#c0ae97','fur2':'#e1d3b2','fur3':'#fff0ce',
 'skin0':'#9d6c65','skin1':'#d99b80','skin2':'#f4c5a0',
 'case0':'#234b5b','case1':'#346c79','case2':'#58919a','case3':'#a0c6c7',
 'rubber':'#1b2a38'
}
def poly(pts,col): c.poly(pts,P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x1,y1,x2,y2,col): c.line(x1,y1,x2,y2,P.get(col,col))
def px(x,y,col): c.set(x,y,P.get(col,col))

# Scarf tails blown back by the wind.
poly([(26,14),(31,13),(35,15),(39,14),(44,16),(40,18),(34,17),(29,18)],'ink')
poly([(28,15),(33,15),(36,16),(41,16),(39,17),(33,16),(29,17)],'red3')
poly([(29,16),(33,18),(39,19),(42,18),(41,21),(36,21),(30,19)],'ink')
line(32,18,38,20,'red1'); line(38,20,40,19,'red2')

# Expedition pack, visible behind the right shoulder.
poly([(29,17),(34,17),(37,21),(37,29),(35,32),(31,32),(28,24)],'ink')
poly([(31,18),(33,18),(35,21),(35,29),(33,30),(30,25)],'case1')
line(33,20,34,27,'case2')
rect(35,23,2,5,'deep'); rect(35,24,1,2,'slate')
line(32,29,35,29,'case0')

# Far leg planted behind, with a long boot sole.
poly([(27,30),(32,31),(32,35),(35,39),(39,41),(40,44),(29,44),(28,41),(25,37),(24,33)],'ink')
poly([(28,32),(31,33),(30,35),(33,39),(31,41),(28,39),(26,35)],'navy')
line(29,34,31,38,'slate')
poly([(31,39),(34,39),(35,41),(38,42),(38,43),(30,43),(29,41)],'deep')
line(31,40,34,40,'fur1')
line(31,43,38,43,'slate')
px(38,44,'rubber'); line(30,44,39,44,'rubber')

# Near leg strides forward, firmly braced against the wind.
poly([(22,30),(28,31),(28,35),(24,38),(22,42),(23,44),(10,44),(10,41),(15,39),(18,35),(19,32)],'ink')
poly([(22,32),(26,33),(25,36),(21,39),(20,41),(16,41),(18,37)],'navy')
poly([(22,33),(24,33),(22,36),(19,39),(17,39),(19,36)],'slate')
line(23,37,21,39,'deep')
poly([(16,39),(21,40),(21,42),(22,43),(11,43),(12,41)],'deep')
line(15,40,19,40,'fur1'); px(20,41,'fur0')
line(12,42,15,42,'slate')
line(11,44,22,44,'rubber')

# Heavy, sloping parka silhouette.
poly([(21,15),(27,15),(31,18),(32,23),(34,30),(33,33),(28,35),(21,33),(19,29),(18,22),(18,18)],'ink')
poly([(22,17),(27,17),(30,19),(30,23),(32,29),(31,32),(27,33),(22,31),(20,26),(20,21)],'red2')
poly([(27,18),(30,20),(30,25),(32,30),(30,32),(27,32),(26,27)],'red1')
poly([(21,18),(24,18),(25,21),(24,27),(22,29),(20,24)],'red3')
line(22,18,23,21,'red4')
# Lower hem, reinforcement and pocket.
line(22,31,27,33,'red0'); line(28,33,32,31,'red0')
line(23,30,28,31,'red3')
poly([(26,26),(30,25),(31,29),(27,30)],'red0')
line(26,26,29,25,'red4'); line(27,28,29,28,'red2')
# Main zip follows the lean.
line(23,18,25,25,'red0'); line(25,25,27,31,'red0')
line(24,21,24,23,'fur1'); px(25,25,'fur3')
# Backpack shoulder strap.
poly([(27,17),(29,18),(30,22),(30,26),(28,27),(28,22),(26,19)],'deep')
line(28,19,29,23,'slate'); rect(28,23,2,2,'case3'); px(29,24,'deep')

# Hood: irregular fur edge breaks up the windward silhouette.
poly([(16,4),(23,4),(23,5),(26,5),(28,7),(29,10),(29,14),(27,17),(23,19),(17,18),(13,16),(11,13),(11,8),(13,6),(16,6)],'ink')
poly([(20,5),(24,6),(27,8),(28,11),(27,15),(25,17),(22,17),(19,14),(18,8)],'red1')
poly([(21,6),(24,7),(26,9),(26,12),(25,14),(23,14),(21,10)],'red2')
line(23,7,25,9,'red3'); px(26,11,'red3')
# Fur ring, with little squared tufts.
poly([(15,6),(18,5),(21,6),(23,8),(24,11),(23,15),(21,17),(17,17),(13,15),(12,12),(12,8)],'fur1')
poly([(15,6),(18,6),(20,7),(22,8),(22,11),(20,14),(17,15),(14,13),(13,10),(13,8)],'fur2')
rect(15,5,3,2,'fur2'); rect(12,8,2,3,'fur3')
px(14,7,'fur3'); line(16,6,18,6,'fur3'); px(20,7,'fur3')
rect(12,12,2,2,'fur2'); px(14,15,'fur2'); rect(17,16,3,2,'fur2')
px(21,15,'fur3'); px(22,13,'fur2'); px(22,16,'fur0')
# Recessed face and balaclava.
poly([(16,8),(19,8),(21,10),(21,14),(19,16),(16,15),(14,13),(14,10)],'deep')
poly([(15,11),(20,11),(20,14),(18,15),(15,13)],'skin1')
rect(14,12,2,1,'skin2'); px(17,13,'skin2'); px(19,14,'skin0')
poly([(15,14),(18,14),(20,13),(21,15),(19,16),(17,16)],'navy')
line(16,15,18,15,'slate')
# Wide, dark-rimmed glacier goggles and pale reflected sky.
poly([(14,8),(19,8),(22,10),(21,12),(15,12),(13,11),(13,9)],'ink')
line(22,10,24,11,'deep')
rect(14,9,6,2,'blue'); line(15,9,18,9,'glint')
line(14,10,16,10,'ice'); px(18,10,'ice'); px(19,10,'glint'); px(20,10,'ice')
px(20,11,'blue'); px(17,11,'ice')
# Padded neck and collar.
poly([(20,17),(23,16),(26,17),(26,19),(23,20),(20,19),(18,17)],'red0')
line(20,17,22,18,'fur1'); line(23,18,25,17,'red3')

# Forward arm, sleeve gathers and mitten clutching the case handle.
poly([(21,19),(24,20),(24,23),(21,26),(17,28),(13,26),(14,23),(17,22),(18,20)],'ink')
poly([(20,20),(22,21),(22,23),(19,25),(16,26),(15,24),(18,23)],'red2')
line(18,21,20,20,'red4'); line(16,24,18,23,'red3')
line(19,25,21,24,'red1')
poly([(14,24),(16,25),(17,27),(15,29),(12,28),(12,26)],'deep')
line(13,25,15,26,'slate'); px(13,27,'navy')

# The hard sample case. Handle is visibly separate from the shell.
poly([(7,28),(8,26),(12,26),(14,28),(14,30),(12,30),(12,28),(9,28),(9,30),(7,30)],'ink')
line(9,27,11,27,'case3')
poly([(5,29),(17,29),(19,31),(19,38),(17,39),(5,39),(4,37),(4,31)],'ink')
rect(5,31,12,7,'case1')
poly([(6,30),(16,30),(18,31),(16,33),(5,33),(5,31)],'case2')
rect(17,32,1,6,'case0')
line(5,33,16,33,'case0'); line(6,30,15,30,'case3')
rect(6,34,1,3,'case2'); line(7,37,15,37,'case0')
# Metal catches and protective corners.
rect(7,32,2,3,'ink'); rect(14,32,2,3,'ink')
rect(7,32,1,2,'fur2'); rect(14,32,1,2,'fur2')
px(5,31,'case0'); px(17,31,'case0'); px(5,37,'case0'); px(16,37,'case0')
# Small sample-vial insignia inset on the case face.
rect(10,34,3,3,'deep'); line(11,34,11,36,'ice'); px(12,36,'ice')

view(result, scale=8, margin=0)
save('polar_researcher', result)
finish(result)
