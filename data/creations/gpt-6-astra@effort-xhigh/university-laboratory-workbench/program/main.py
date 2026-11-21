# University laboratory workbench -- 64 x 64, hand-built pixel clusters.
result = new_canvas(64, 64, background='#9db8b2', name='laboratory_workbench')
c = result
P = {
    'ink':'#243c49', 'deep':'#38535c', 'steel':'#607f87', 'mid':'#8ba5a4',
    'pale':'#c7d8c9', 'white':'#f1efda', 'bluewhite':'#dce8dc',
    'wall':'#9db8b2', 'walllight':'#abc4bb', 'grout':'#8ba9a5',
    'desk':'#b8a582', 'desklight':'#c7b694', 'deskshade':'#a29072',
    'shadow':'#8e8973', 'shadowdeep':'#737b70',
    'wood':'#9c6c4b', 'woodlight':'#ce9b64', 'wooddark':'#6f5141',
    'amber':'#a66938', 'ambershade':'#754e32', 'amberlight':'#d99b4f',
    'green':'#3a7f79', 'greenlight':'#70aca0', 'glass':'#b9d9cc',
    'water':'#55a9a8', 'waterdark':'#397c89',
    'rose':'#b65f64', 'roselight':'#e39887',
    'paper':'#e6ddba', 'paperlight':'#f3edcf', 'paperfold':'#b9b392',
    'writing':'#8e9e92', 'cover':'#547b78', 'cap':'#3f5355'
}
def rect(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def line(x,y,xx,yy,k): c.line(x,y,xx,yy,P.get(k,k))
def poly(pts,k): c.poly(pts,P.get(k,k))
def dot(x,y,k): c.set(x,y,P.get(k,k))
# Quiet tiled wall. Two large tiles keep the background calmer than the tools.
rect(0,0,64,4,'walllight')
line(0,11,63,11,'grout')
line(0,12,63,12,'walllight')
line(0,24,63,24,'grout')
line(23,0,23,10,'grout')
line(24,0,24,10,'walllight')
line(48,12,48,24,'grout')
line(49,12,49,24,'walllight')
# Socket, inset in the backsplash.
rect(3,17,7,7,'grout')
rect(3,16,6,7,'pale')
rect(4,17,4,5,'walllight')
dot(5,19,'deep'); dot(7,19,'deep')
# Back lip, broad working surface and the cabinet front.
rect(0,25,64,3,'deep')
line(0,25,63,25,'mid')
rect(0,28,64,28,'desk')
poly([(0,29),(45,28),(63,39),(63,55),(0,55)],'desklight')
line(0,28,63,28,'deskshade')
rect(0,55,64,3,'wood')
line(0,55,63,55,'woodlight')
line(0,58,63,58,'ink')
rect(0,59,64,5,'deep')
line(1,59,62,59,'steel')
line(31,59,31,63,'ink')
rect(11,60,10,2,'ink'); line(12,60,19,60,'mid')
rect(43,60,10,2,'ink'); line(44,60,51,60,'mid')
# Tiny surface marks, and shaped contact shadows.
line(2,50,6,50,'desk')
line(8,52,18,52,'desk')
line(21,37,25,37,'deskshade')
poly([(5,44),(12,40),(26,41),(33,47),(29,50),(11,50),(5,47)],'shadow')
poly([(29,29),(37,28),(43,32),(39,34),(30,33)],'shadow')
poly([(40,37),(60,35),(63,39),(59,41),(43,41)],'shadow')
# Tall amber reagent bottle, with a large blank paper label.
rect(30,16,6,3,'ink')
line(31,16,34,16,'steel')
rect(31,19,4,3,'ambershade')
poly([(31,21),(35,21),(37,24),(37,31),(30,32),(28,30),(28,24)],'ink')
poly([(31,22),(34,22),(36,24),(36,30),(30,31),(29,29),(29,24)],'amber')
line(30,24,30,28,'amberlight')
line(35,24,35,29,'ambershade')
rect(29,25,7,4,'paper')
rect(30,26,2,2,'wood')
line(33,27,34,27,'paperfold')
dot(30,30,'amberlight')
# Smaller aqua stock bottle, a square shoulder and ribbed dark stopper.
rect(37,21,4,2,'ink')
line(37,21,39,21,'steel')
rect(38,23,2,2,'green')
poly([(37,24),(40,24),(42,26),(42,32),(36,32),(35,30),(35,26)],'ink')
rect(36,26,5,5,'green')
line(36,26,36,29,'greenlight')
rect(36,27,5,3,'paperlight')
rect(37,28,2,1,'waterdark')
# Four glass test tubes. The back rail is partially hidden by the glass.
rect(41,29,20,3,'wooddark')
line(42,29,60,29,'woodlight')
for x,top,liquid,highlight,level in [(43,19,'water','glass',26),(48,20,'rose','roselight',27),(53,18,'amberlight','white',25),(58,21,'greenlight','glass',28)]:
    rect(x-1,top+1,4,35-top,'steel')
    rect(x,top+1,2,35-top,'glass')
    rect(x,level,2,36-level,liquid)
    line(x,top+2,x,level-2,'bluewhite')
    line(x-1,top,x+2,top,'mid')
    line(x,top,x+1,top,'white')
    dot(x,level,highlight)
    line(x,36,x+1,36,'deep')
    dot(x,34,highlight)
# Rack supports and front rail: rounded tube ends hang in its open lower span.
rect(40,31,2,8,'wooddark')
rect(61,31,2,8,'wooddark')
line(40,32,40,37,'woodlight')
line(61,32,61,37,'wood')
rect(40,31,23,3,'wooddark')
rect(40,31,22,1,'woodlight')
rect(41,32,20,1,'wood')
rect(40,37,23,2,'wooddark')
line(41,37,61,37,'woodlight')
for x in (41,61): dot(x,32,'paper')
# Microscope base, substantial and correctly weighted.
poly([(5,44),(10,40),(22,39),(28,42),(29,46),(25,49),(8,49),(5,47)],'ink')
poly([(6,44),(11,41),(22,40),(27,43),(27,46),(24,47),(8,47)],'steel')
poly([(7,43),(12,41),(22,41),(26,43),(25,45),(9,45)],'pale')
line(9,43,15,42,'white')
line(9,46,22,46,'mid')
# The swept arm curves round the open optical path.
poly([(19,18),(24,18),(28,21),(30,26),(30,34),(28,39),(24,43),(19,43),(18,40),(23,35),(24,28),(22,24),(18,23)],'ink')
poly([(21,19),(24,20),(27,23),(28,27),(28,34),(26,38),(23,41),(20,41),(24,35),(26,28),(24,23),(21,22)],'steel')
poly([(21,19),(24,20),(27,24),(27,32),(25,36),(23,39),(21,40),(24,34),(25,28),(23,23),(20,22)],'pale')
line(22,20,25,23,'white')
# Eyepiece at a deliberate diagonal, then the cream optical head.
poly([(10,11),(13,8),(18,12),(15,16)],'ink')
line(11,11,14,9,'steel')
poly([(14,14),(17,11),(20,15),(17,18)],'steel')
poly([(15,16),(19,13),(25,20),(22,25),(17,22)],'ink')
poly([(16,16),(19,14),(23,19),(22,22),(19,22)],'pale')
line(17,16,19,15,'white')
line(18,17,21,20,'white')
line(22,20,22,22,'mid')
# Revolving nosepiece and two objective barrels.
line(16,24,22,24,'deep')
rect(16,25,4,2,'steel')
rect(16,27,3,3,'ink')
line(16,27,16,28,'pale')
rect(21,25,2,3,'ink')
dot(21,26,'mid')
# Stage, slide and a ruby sample. No text is needed to identify them.
rect(8,31,17,3,'ink')
line(9,31,24,31,'steel')
rect(12,30,8,1,'bluewhite')
dot(16,30,'rose')
dot(10,31,'white')
rect(14,34,6,2,'deep')
rect(16,36,3,3,'ink')
line(16,36,16,37,'steel')
# Illuminator in the base.
c.ellipse(17,42,4,2,P['deep'])
line(15,41,19,41,'white')
line(15,42,19,42,'glass')
# Two nested focusing wheels, with a small rim highlight.
c.circle(27,29,3,P['ink'])
c.circle(27,29,2,P['steel'])
line(26,28,27,27,'pale')
c.circle(27,29,1,P['deep'])
dot(27,29,'mid')
# Open laboratory notebook in the foreground, with a visible spine and cover.
poly([(35,46),(43,43),(47,44),(53,43),(58,45),(62,54),(49,58),(45,57),(36,57),(33,48)],'shadow')
poly([(34,45),(42,42),(46,44),(53,42),(58,44),(61,54),(48,58),(44,57),(35,57),(32,47)],'ink')
poly([(34,46),(43,44),(47,45),(55,44),(58,46),(60,54),(48,57),(44,56),(35,56),(33,48)],'cover')
poly([(34,45),(42,43),(46,45),(47,55),(43,54),(35,55),(33,47)],'paper')
poly([(35,45),(42,43),(45,45),(46,53),(42,52),(35,53),(33,47)],'paperlight')
poly([(46,45),(53,43),(57,45),(59,53),(48,56)],'paper')
poly([(47,45),(53,43),(56,45),(58,52),(48,54)],'paperlight')
line(45,45,47,54,'paperfold')
line(36,54,42,53,'paperfold')
line(49,55,57,53,'paperfold')
# A tiny experiment sketch and measured pencil rules, deliberately not tiny text.
line(36,47,41,46,'writing')
line(37,49,42,48,'paperfold')
line(37,51,41,50,'paperfold')
line(50,46,53,45,'writing')
line(51,47,51,49,'waterdark')
line(53,47,55,49,'waterdark')
line(51,50,55,49,'waterdark')
dot(53,49,'water')
line(50,52,56,51,'paperfold')
# Dropper lies diagonally, separate from the book and microscope.
line(27,53,35,45,'shadow')
line(26,52,33,45,'ink')
line(27,51,33,45,'glass')
line(28,50,32,46,'bluewhite')
dot(26,52,'waterdark')
poly([(31,44),(34,41),(36,42),(37,44),(34,47)],'ink')
line(33,43,34,42,'steel')
line(32,45,34,46,'deep')
# Export and inspect the actual submitted pixels.
print(result.stats_text())
assert result.stats()['colors_used'] <= 86
save('university-laboratory-workbench', result)
view(result, scale=8, margin=0)
finish(result)
