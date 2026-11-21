from pixelbench_api import *

# Cold expedition palette: warm shell against icy equipment and goggles.
result = new_canvas(48, 48, name="polar_researcher")
c = result
P = {
    'ink':'#172a3a', 'deep':'#233a4c', 'slate':'#365567',
    'steel':'#527587', 'blue':'#7698a4', 'snow':'#d8e8df',
    'furshade':'#859c9b', 'furmid':'#b6c9c1', 'fur':'#ebedcf',
    'ivory':'#fff5d9', 'reddeep':'#713e42', 'redshade':'#a34c43',
    'red':'#cc624b', 'redlight':'#e88560', 'orange':'#f4aa77',
    'glassdark':'#326779', 'glass':'#7ec4d7', 'ice':'#c6f2f3',
    'glint':'#f2ffff', 'skinshade':'#a07160', 'skin':'#d6a284',
    'case':'#718e8d', 'caselight':'#a6bdb2', 'caseshade':'#49666c',
    'yellow':'#e8c677'
}
for name, color in P.items():
    c.color(color, name)

def poly(points, color):
    c.poly(points, color)
def r(x,y,w,h,color):
    c.rect(x,y,w,h,color)
def ln(x,y,x1,y1,color):
    c.line(x,y,x1,y1,color)

# Scarf and hood cords stream downwind to the left.
poly([(22,16),(18,15),(15,16),(11,14),(7,15),(3,13),(5,17),(10,18),(15,18),(20,20)],'ink')
poly([(20,17),(15,17),(11,16),(7,17),(5,15),(10,16),(13,15),(16,16),(20,16)],'redlight')
poly([(20,18),(16,20),(11,20),(9,18),(13,18),(17,17)],'redshade')

# Boots and insulated legs: a long rear brace and planted leading foot.
poly([(16,29),(24,30),(23,34),(19,37),(15,40),(14,43),(6,43),(7,40),(11,37),(14,34)],'ink')
poly([(17,31),(22,32),(19,35),(15,38),(12,40),(9,40),(13,36)],'slate')
ln(17,33,12,38,'steel')
poly([(24,29),(31,29),(31,34),(29,38),(30,41),(36,42),(37,44),(35,45),(25,45),(23,42),(23,37),(25,34)],'ink')
poly([(26,32),(30,31),(29,35),(27,38),(28,42),(25,42),(25,37)],'slate')
ln(27,34,26,38,'steel')
r(7,40,7,3,'deep')
r(6,42,8,2,'ink')
ln(7,41,11,41,'steel')
r(25,41,5,3,'deep')
r(29,42,5,2,'deep')
ln(26,42,29,42,'steel')
r(7,44,6,1,'slate')
r(26,45,10,1,'slate')

# Compact expedition backpack behind the shoulder.
poly([(18,16),(22,18),(23,24),(19,31),(14,30),(12,27),(13,21),(15,18)],'ink')
poly([(16,19),(19,18),(21,21),(18,28),(15,28),(14,26)],'slate')
poly([(15,20),(17,19),(16,24),(14,25)],'steel')
ln(15,27,18,28,'steel')
r(12,23,2,4,'deep')
r(13,23,1,3,'blue')

# Thick parka, pitched forward over the hips.
poly([(25,15),(30,15),(32,18),(31,23),(29,27),(29,31),(26,34),(18,33),(15,30),(17,25),(18,21),(21,18)],'ink')
poly([(23,17),(28,17),(30,19),(28,25),(27,29),(27,32),(20,32),(17,30),(20,24),(20,21)],'red')
poly([(20,22),(23,18),(25,18),(22,24),(21,29),(25,31),(26,33),(19,32),(17,30)],'redshade')
poly([(25,18),(28,17),(30,19),(28,22),(25,22),(23,26),(23,22)],'redlight')
ln(25,18,21,29,'reddeep')
ln(24,20,22,27,'orange')
poly([(18,29),(21,30),(27,30),(27,32),(21,32),(17,31)],'deep')
ln(19,30,24,31,'slate')
r(23,31,2,1,'caselight')
# Lower patch pocket and chest badge.
poly([(23,25),(27,25),(26,28),(22,28)],'reddeep')
ln(24,25,27,25,'orange')
r(27,20,3,3,'snow')
r(28,20,1,3,'redshade')
r(27,21,3,1,'redshade')
# Backpack strap over the jacket.
ln(21,19,18,25,'ink')
ln(22,19,19,25,'slate')
r(18,24,2,2,'steel')
r(18,24,1,1,'caselight')

# A gloved arm extends into the wind, supporting the sample case.
poly([(28,18),(31,18),(32,21),(32,24),(35,25),(35,28),(31,28),(28,25),(27,22)],'ink')
poly([(29,19),(31,20),(30,24),(33,25),(32,27),(29,25),(28,22)],'red')
ln(29,20,29,23,'redlight')
ln(30,24,32,25,'redshade')
r(32,25,3,3,'deep')
r(33,25,2,2,'slate')
# Rigid insulated case with a separate visible handle.
poly([(34,28),(34,26),(36,24),(39,24),(41,26),(41,29),(39,29),(39,27),(38,26),(37,26),(36,27),(36,29)],'ink')
ln(36,25,38,25,'steel')
poly([(32,28),(42,28),(44,30),(44,37),(42,39),(32,39),(30,37),(30,30)],'ink')
poly([(32,30),(41,30),(42,31),(42,36),(41,37),(32,37)],'case')
r(32,30,9,2,'caselight')
r(31,32,2,4,'caseshade')
r(33,36,9,2,'caseshade')
r(42,31,1,6,'deep')
ln(32,32,41,32,'caseshade')
r(33,30,2,3,'deep')
r(39,30,2,3,'deep')
r(33,31,1,1,'yellow')
r(39,31,1,1,'yellow')
r(35,34,5,2,'snow')
r(36,34,1,2,'glassdark')
r(38,34,1,2,'glassdark')
c.set(36,34,'glass')
c.set(38,34,'glass')
c.set(32,36,'caselight')
c.set(41,36,'steel')
# The mitten closes over the near corner of the handle.
r(33,25,3,2,'deep')
r(33,25,2,1,'steel')
c.set(35,26,'slate')

# Windward hood, chunky pale fur surrounding a dark face opening.
poly([(25,3),(31,3),(34,5),(36,8),(36,13),(34,16),(31,18),(26,18),(22,16),(21,12),(22,7)],'ink')
poly([(25,5),(30,4),(33,6),(34,9),(33,14),(30,16),(26,17),(23,15),(22,11),(23,8)],'redshade')
poly([(25,5),(28,4),(29,6),(26,8),(24,12),(24,15),(23,14),(23,10)],'redlight')
# Angular fur silhouette keeps the face clearly framed.
poly([(29,4),(32,4),(33,6),(35,6),(35,8),(37,9),(36,12),(36,14),(34,15),(33,17),(30,18),(28,17),(26,17),(25,15),(25,12),(26,9),(27,7)],'furshade')
poly([(29,5),(32,5),(32,7),(34,7),(34,9),(36,9),(35,12),(35,14),(33,14),(32,16),(30,17),(28,16),(27,16),(26,14),(27,10),(28,8)],'furmid')
poly([(29,5),(31,5),(32,7),(33,7),(33,8),(30,8),(28,10),(27,13),(26,13),(27,9)],'fur')
r(34,9,2,2,'fur')
r(33,14,2,1,'fur')
r(29,16,2,1,'fur')
c.set(30,5,'ivory')
c.set(27,10,'ivory')
# Balaclava and cheek, with a wide icy visor.
poly([(30,8),(33,8),(35,10),(34,14),(32,16),(29,15),(28,13),(28,10)],'deep')
poly([(31,12),(34,12),(33,14),(31,15),(29,14)],'skinshade')
r(31,12,3,2,'skin')
c.set(34,12,'skin')
poly([(28,13),(30,14),(33,14),(32,16),(29,15)],'slate')
ln(29,14,31,15,'blue')
# Rubber goggles project out from the hood toward the right.
poly([(29,8),(34,8),(36,9),(36,11),(35,12),(29,12),(28,11),(28,9)],'ink')
r(29,9,6,2,'glass')
r(29,10,1,1,'glassdark')
r(30,9,2,1,'ice')
r(33,9,2,1,'ice')
c.set(30,10,'ice')
c.set(34,9,'glint')
c.set(32,10,'glassdark')
# Hood seam and neck cinch.
ln(25,8,24,11,'reddeep')
c.set(25,6,'orange')
r(26,17,3,2,'deep')
r(27,17,2,1,'furmid')
ln(29,17,31,19,'furmid')
c.set(31,20,'ivory')

view(result, scale=10, margin=3, edges="all")
finish(result)
