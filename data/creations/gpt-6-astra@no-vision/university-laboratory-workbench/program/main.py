# University laboratory workbench, 64 x 64 pixels
c = new_canvas(64, 64, background='#d3ded7', name='university_lab')
P = {
'ink':'#233b45', 'deep':'#304f57', 'steel':'#577d82', 'mid':'#82a5a3',
'light':'#bfd5cc', 'white':'#f3f1d9', 'wall':'#d3ded7', 'grout':'#b9ccc3',
'wood':'#ae7650', 'woodlight':'#d5a66a', 'woodhi':'#edc88a', 'woodshade':'#80583f',
'bench':'#6f9590', 'benchtop':'#9db8a8', 'edge':'#496d70',
'paper':'#e9dfb8', 'paperhi':'#fff2cb', 'paperline':'#abae98',
'glass':'#bce6db', 'glassdark':'#70b4ae', 'blue':'#488f9c', 'bluehi':'#83c6c1',
'pink':'#bb6469', 'pinkhi':'#e8a293', 'amber':'#a9693e', 'amberhi':'#d99d51',
'gold':'#e8bf67', 'shadow':'#668b85'
}
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(a,b,d,e,col): c.line(a,b,d,e,P.get(col,col))
def poly(pts,col): c.poly(pts,P.get(col,col))
def dot(x,y,col): c.set(x,y,P.get(col,col))
# Quiet tiled wall, with a darker line where it meets the bench.
for y in [10,23,36]:
    line(0,y,63,y,'grout')
for x,y in [(17,0),(46,0),(5,11),(33,11),(60,11),(17,24),(46,24)]:
    line(x,y,x,min(y+11,35),'grout')
# A slim wall shelf and a small storage bottle supply context.
rect(39,8,21,2,'steel'); rect(40,10,19,1,'light')
rect(42,3,5,5,'glassdark'); rect(43,3,3,4,'glass'); rect(42,1,5,2,'deep')
rect(51,4,6,4,'amber'); rect(52,5,4,2,'paper'); rect(52,2,4,2,'deep')
line(42,11,42,13,'steel'); line(57,11,57,13,'steel')
# Bench: back edge, broad work surface, heavy rounded front, cabinets below.
rect(0,36,64,3,'edge')
poly([(2,38),(61,38),(63,55),(0,55)],'benchtop')
line(3,39,60,39,'light')
rect(0,55,64,5,'edge'); rect(0,55,64,1,'light')
rect(0,60,64,4,'woodshade')
rect(2,60,28,4,'wood'); rect(33,60,29,4,'wood')
line(8,61,23,61,'woodlight'); line(41,61,55,61,'woodlight')
rect(12,62,8,1,'ink'); rect(45,62,8,1,'ink')
# Ground shadows bind objects to the tabletop.
c.ellipse(18,48,13,3,P['shadow'])
c.ellipse(48,43,13,2,P['shadow'])
c.ellipse(33,40,6,2,P['shadow'])
# Amber reagent bottle. Distinct shoulders, cap and a broad blank label.
rect(30,24,6,4,'ink'); rect(31,24,4,1,'steel')
poly([(31,28),(35,28),(35,30),(38,32),(38,39),(36,41),(29,41),(28,39),(28,32),(31,30)],'ink')
poly([(31,29),(35,29),(35,31),(37,33),(37,39),(29,39),(29,33),(31,31)],'amber')
line(30,33,30,38,'amberhi'); rect(31,32,5,2,'amberhi')
rect(30,35,7,4,'paper'); rect(32,36,3,1,'woodshade')
# A short blue bottle beside it, its square silhouette distinct from the reagent.
rect(3,37,4,3,'ink'); rect(2,40,6,7,'ink')
rect(3,41,4,5,'blue'); rect(3,43,4,2,'paper'); dot(3,41,'glass')
# Test-tube rack: back rail first, then tubes, then front retaining rail.
rect(39,32,23,3,'woodshade'); rect(40,32,21,1,'woodlight')
for x,top,col,hi,level in [(42,22,'blue','bluehi',30),(49,24,'pink','pinkhi',32),(56,21,'amberhi','gold',29)]:
    # open rims and straight glass walls with rounded bases
    rect(x,top,5,15 if x!=49 else 13,'ink')
    rect(x+1,top+2,3,12 if x!=49 else 10,'glass')
    rect(x+1,level,3,36-level,col)
    line(x+1,level,x+3,level,hi)
    dot(x+1,36,'glassdark'); dot(x+2,37,'ink'); dot(x+3,36,'glassdark')
    line(x,top,x+4,top,'light')
    line(x+1,top+1,x+3,top+1,'deep')
    line(x+1,top+3,x+1,level-1,'white')
    dot(x+3,level+2,hi)
rect(39,35,2,8,'woodshade'); rect(60,35,2,8,'woodshade')
rect(39,35,23,3,'wood'); line(40,35,60,35,'woodhi')
for x in [43,50,57]: rect(x,36,2,1,'woodshade')
rect(38,42,24,2,'woodshade'); rect(39,41,22,2,'woodlight')
# Microscope: cast metal C-arm, base and angled optical tube.
poly([(21,22),(25,23),(28,27),(29,32),(28,38),(25,42),(24,45),(19,45),(21,40),(24,36),(25,31),(24,28),(20,27)],'ink')
poly([(22,24),(25,26),(27,30),(27,35),(24,40),(22,44),(21,44),(23,38),(25,35),(26,31),(24,27),(21,26)],'steel')
line(26,28,27,31,'mid'); line(26,35,23,40,'mid')
# Rear foot and beveled heavy base
poly([(12,43),(23,43),(27,46),(27,49),(7,49),(7,47)],'ink')
poly([(13,44),(22,44),(25,46),(25,47),(9,47)],'steel')
line(11,45,22,45,'light'); line(8,48,26,48,'deep')
# Light source below the stage
rect(15,40,6,4,'ink'); rect(16,39,4,3,'steel'); rect(16,39,4,1,'white')
# Stage, slide and clips
rect(8,35,16,3,'ink'); line(9,35,23,35,'mid')
rect(11,33,11,2,'glassdark'); rect(12,33,9,1,'glass')
rect(16,33,2,1,'pink'); dot(12,34,'white'); dot(20,34,'white')
# Eyepiece and body tube slope down toward the specimen
poly([(9,19),(12,17),(21,27),(18,30)],'ink')
poly([(12,20),(14,20),(19,26),(17,28)],'mid')
line(12,20,17,25,'light')
poly([(7,18),(10,15),(14,19),(10,22)],'ink')
line(8,18,10,16,'steel'); line(10,19,12,17,'deep')
# Revolving nosepiece with two objective lenses
poly([(17,27),(21,26),(23,29),(20,31),(17,30)],'deep')
rect(17,29,3,4,'ink'); rect(18,29,1,3,'light'); dot(18,32,'woodlight')
line(21,29,23,31,'steel'); dot(23,32,'white')
# Concentric focus knob on the arm
c.circle(26,31,3,P['ink']); c.circle(26,31,2,P['steel']); dot(25,30,'light'); dot(26,31,'deep')
# Notebook shadow and dark cloth cover: an open low book at the front.
poly([(29,46),(39,47),(49,45),(52,55),(40,59),(27,56)],'shadow')
poly([(28,45),(38,46),(48,44),(52,55),(40,59),(26,55)],'ink')
poly([(29,44),(38,46),(47,44),(50,54),(40,57),(28,54)],'paper')
poly([(29,44),(37,46),(39,55),(29,53)],'paperhi')
poly([(39,46),(47,44),(49,53),(40,56)],'paperhi')
line(38,46,40,56,'woodshade')
line(28,54,39,57,'paperline'); line(41,57,50,54,'paperline')
# A few ruled lines and a simple molecular sketch, not illegible text.
line(30,47,35,48,'paperline'); line(30,49,36,50,'paperline'); line(31,51,36,52,'paperline')
line(42,48,45,47,'steel'); line(45,47,47,49,'steel'); line(47,49,44,51,'steel'); line(44,51,42,48,'steel')
dot(42,48,'blue'); dot(45,47,'blue'); dot(47,49,'blue'); dot(44,51,'blue')
line(42,53,47,52,'paperline')
# Dropper lies diagonally at the right of the book, rubber bulb and tapered pipette.
line(52,52,59,46,'shadow')
line(52,51,59,44,'ink')
line(52,51,56,47,'glassdark'); line(53,50,56,47,'glass')
poly([(55,46),(58,43),(61,43),(62,45),(59,48),(57,48)],'ink')
line(58,45,60,44,'steel'); dot(52,52,'glass')
# Small glints, kept sparse to preserve the silhouettes.
dot(34,30,'gold')
print(c.stats_text())
print(c.matrix_text(region=(28,20,63,58)))
save('university_laboratory_workbench', c)
result = c
finish(result)
