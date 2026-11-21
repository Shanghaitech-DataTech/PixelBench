import math
import random

W = H = 128
c = new_canvas(W, H, background='#dbe9e9', name='poolcore')
P = {
    'ceil':'#dbe9e9', 'ceilshade':'#c1d8db', 'seam':'#a6c6ce',
    'white':'#f2f6ec', 'glow':'#e5ffff', 'edge':'#d3e5e5',
    'wall':'#bbd8df', 'wall2':'#abcdd6', 'grout':'#89b4c3',
    'tilelight':'#dce9e7', 'tileblue':'#b5d5df', 'tiledark':'#8bb9c9',
    'tilewhite':'#e8efea', 'tilepale':'#c6dfe2', 'groutlight':'#a7c7d0',
    'watergrid':'#7bcbd6', 'watergridlight':'#90d6df', 'underlip':'#76aebf',
    'recess':'#6095aa', 'recessdark':'#4b7d94', 'recesslight':'#8db9c5',
    'floor':'#d2e4e4', 'floorline':'#a1c5ce',
    'coping':'#e9efea', 'copingdark':'#92bcc7',
    'pool':'#8bd4df', 'waterlight':'#b6e5e7', 'waterbright':'#d3f0ea',
    'watermid':'#9eddE4', 'waterdark':'#71c4d5', 'waterdeep':'#66b7cc',
    'ripple':'#a7e0e5', 'refl':'#c7edeb',
    'slide':'#f1f4e9', 'slidehi':'#ffffff', 'slideshadow':'#b0cdd2',
    'slideinner':'#d7e2dd', 'slidedark':'#8faebc',
    'skin':'#d7ad90', 'skinhi':'#edc7a4', 'skinshade':'#b98978',
    'hair':'#4e4249', 'hairshade':'#383844', 'hairlight':'#71605e',
    'swim':'#578491', 'swimdark':'#436b7e',
    'yellow':'#f2d16b', 'yellowlight':'#ffe89a', 'yellowshade':'#d4ad4e',
    'yellowdark':'#b3914e',
}

def rect(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def line(x0,y0,x1,y1,k): c.line(x0,y0,x1,y1,P.get(k,k))
def poly(pts,k): c.poly(pts,P.get(k,k))
def ellipse(x,y,rx,ry,k): c.ellipse(x,y,rx,ry,P.get(k,k))
def path(d,k,fill=True): c.path(d,P.get(k,k),fill=fill)

# Architectural shell: the ceiling leads toward the far, unoccupied hall.
poly([(0,0),(128,0),(128,27),(96,38),(0,30)],'ceil')
poly([(0,29),(95,34),(98,65),(0,72)],'wall')
poly([(95,34),(128,23),(128,75),(96,64)],'wall2')
poly([(0,67),(96,61),(128,69),(128,94),(0,94)],'floor')

# Cool ceiling joints and long fluorescent fixtures.
line(0,15,94,35,'ceilshade')
line(20,0,96,34,'ceilshade')
line(78,0,99,33,'ceilshade')
line(122,0,102,34,'ceilshade')
line(0,27,95,36,'ceilshade')
poly([(9,4),(16,4),(54,22),(48,22)],'seam')
poly([(10,3),(15,3),(53,20),(48,20)],'glow')
line(12,4,49,20,'white')
poly([(65,5),(70,5),(85,23),(81,23)],'seam')
poly([(65,4),(69,4),(84,21),(81,21)],'glow')
poly([(107,8),(112,7),(108,23),(105,24)],'seam')
poly([(108,7),(111,7),(107,22),(105,23)],'glow')
poly([(70,28),(75,28),(84,31),(80,31)],'glow')

# Small square mosaic tiles on the back wall, all hard pixel edges.
random.seed(14)
for y in range(34,69,4):
    for x in range(0,96,4):
        shade=random.choice(['wall','tilepale','tilepale','tilelight','tileblue','tilewhite'])
        rect(x+1,y+1,3,3,shade)
for y in range(34,70,4): line(0,y,95,y,'groutlight')
for x in range(0,96,4): line(x,34,x,68,'groutlight')
# Quiet patches of reflected light on the glazed wall.
for x,y in [(9,39),(25,47),(37,39),(57,55),(61,43),(17,55),(53,39)]:
    line(x,y,x+1,y,'tilewhite')
# A horizontal architectural rail and tiled skirting.
rect(0,60,97,2,'tilelight')
line(0,62,96,62,'grout')
for y in [64,67]: line(0,y,95,y,'grout')

# An empty passage in the far wall adds the second, receding space.
rect(68,41,16,21,'recessdark')
rect(70,42,13,19,'recess')
rect(72,43,10,18,'recesslight')
rect(73,44,9,13,'wall2')
for y in [46,49,52,55]: line(73,y,81,y,'grout')
for x in [75,78,81]: line(x,44,x,57,'grout')
poly([(73,57),(82,55),(82,61),(70,61)],'floorline')
line(73,44,73,57,'recess')
line(73,57,70,61,'recess')
line(68,40,84,40,'tilelight')
line(84,40,84,62,'tilelight')

# Right-hand wall: perspective tile courses and receding vertical joints.
for y0,y1 in [(36,27),(40,34),(44,41),(48,48),(52,55),(56,62),(60,69)]:
    line(96,y0,127,y1,'grout')
for x in [99,103,108,114,121,127]:
    top=34-(x-95)*11//33
    bottom=64+(x-95)*11//33
    line(x,top,x,bottom,'grout')
line(96,62,127,73,'tilelight')
line(96,64,127,75,'recesslight')

# The gridded walkways are defined before the pool opening.
for y in [68,71,75,80,87,94]: line(0,y,127,y,'floorline')
for xb in range(-100,230,13):
    line(87,59,xb,94,'floorline')
# Far coping and the pool itself.
poly([(0,77),(77,67),(101,68),(127,77),(127,127),(0,127)],'copingdark')
poly([(0,75),(78,65),(101,66),(127,75),(127,79),(101,70),(78,69),(0,80)],'coping')
line(0,79,78,69,'waterdeep')
line(78,69,101,70,'waterdeep')
line(101,70,127,79,'waterdeep')
water = new_canvas(128,128,name='water')
water.poly([(0,81),(78,70),(101,71),(127,80),(127,127),(0,127)],P['pool'])
# Square submerged tiles broaden toward the foreground.
for y in [75,79,84,91,101,115]:
    water.line(0,y+5,127,y,P['watergrid'])
for xb in range(-114,251,28):
    water.line(86,67,xb,127,P['watergrid'])
# Refraction breaks up the straight submerged grout lines.
for x,y,w in [(5,99,14),(38,100,12),(78,98,13),(105,113,14),(5,118,16),(43,115,16),(85,115,11),(52,84,9),(95,84,10),(31,90,11)]:
    water.line(x,y,min(127,x+w),y,P['pool'])
    water.line(x+2,y+1,min(127,x+w-1),y+1,P['watergridlight'])
# Keep the grid and caustics inside the pool mask.
for y in range(128):
    for x in range(128):
        if y < (81 - 11*x/78 if x<=78 else 70+(x-78)/23 if x<=101 else 71+9*(x-101)/26):
            water.set(x,y,None)
c.blit(water,0,0)
# Large, broken reflections from the ceiling lights.
poly([(23,84),(28,83),(31,90),(29,96),(34,103),(31,112),(35,122),(30,127),(25,127),(28,119),(24,110),(27,102),(24,94),(25,90)],'watermid')
poly([(88,76),(91,76),(90,83),(93,88),(91,94),(95,102),(92,109),(96,119),(92,125),(88,124),(91,115),(87,107),(90,100),(87,91),(89,83)],'watermid')
poly([(114,85),(117,86),(115,93),(119,102),(117,109),(120,117),(117,127),(112,127),(115,117),(112,110),(115,102),(111,94)],'watermid')
for x,y,w in [(24,85,5),(25,90,7),(26,96,5),(25,104,8),(27,112,8),(28,120,6),(90,79,3),(88,85,5),(90,94,4),(89,103,8),(91,112,7),(90,122,6),(113,91,5),(114,100,5),(115,116,7)]:
    line(x,y,x+w,y,'refl')
    if w>6: line(x+2,y+1,x+w-1,y+1,'waterlight')
# Thin lazy ripples and angular highlights remain sparse and horizontal.
random.seed(8)
for i in range(80):
    x=random.randrange(0,128); y=random.randrange(77,128)
    miny=(81 - 11*x/78 if x<=78 else 70+(x-78)/23 if x<=101 else 71+9*(x-101)/26)
    if y<miny+2: continue
    le=random.choice([2,3,4,5,7])
    col=random.choice(['ripple','watermid','waterlight','pool'])
    line(x,y,min(127,x+le),y,col)
    if i%5==0: line(x+1,y+1,min(127,x+le-1),y+1,'ripple')

# Far square columns stand on the empty deck.
poly([(89,32),(95,33),(95,66),(89,67)],'tilelight')
poly([(95,33),(98,32),(98,65),(95,66)],'tiledark')
for y in range(36,67,4): line(89,y,94,y,'grout')
line(92,34,92,66,'floorline')
line(95,33,95,65,'grout')
line(89,32,95,33,'white')
rect(88,65,8,2,'coping')

# Curving white open flume: broad upper bend, then a steep descent.
# Support post behind the slide.
poly([(40,47),(44,47),(45,71),(42,72)],'slidedark')
line(42,51,43,70,'tilelight')
# Gray outer silhouette.
path('M 0 31 C 10 29 27 29 39 33 C 49 36 53 42 52 49 C 51 57 43 60 38 66 C 34 71 35 76 42 78 L 45 82 C 32 85 23 79 26 69 C 28 61 38 56 41 49 C 44 42 36 39 27 38 C 18 36 8 38 0 39 Z','slidedark')
path('M 0 29 C 13 27 28 28 40 32 C 50 35 54 41 53 47 C 53 55 46 59 41 64 C 35 70 34 75 42 77 L 45 81 C 33 83 26 79 27 71 C 28 63 36 57 41 51 C 47 43 39 38 29 37 C 19 35 9 36 0 38 Z','slide')
# Interior channel, with the two white raised sides.
path('M 0 32 C 14 30 28 31 39 34 C 48 37 51 41 50 47 C 49 54 43 58 38 64 C 32 71 32 76 40 79 L 34 79 C 27 76 29 70 32 65 C 36 59 43 55 45 49 C 48 42 41 37 29 35 C 18 33 8 34 0 36 Z','slideinner')
path('M 0 29 C 15 27 30 29 40 32 C 48 35 53 40 52 46','slidehi',False)
path('M 0 37 C 15 34 30 35 39 39 C 47 43 46 48 41 54 C 34 62 26 67 29 74 C 30 78 35 80 43 80','slidehi',False)
path('M 49 48 C 48 55 40 60 36 66 C 32 72 34 76 40 77','slideshadow',False)
path('M 1 33 C 15 31 30 32 39 35 C 47 38 49 42 48 46','slideshadow',False)
path('M 47 49 C 45 55 39 59 35 65 C 31 71 31 75 36 77','slideinner',False)
line(38,78,44,80,'white')
# Outflow and small rings in the water.
line(34,83,44,83,'waterlight')
line(30,85,37,85,'watermid')
line(42,85,48,85,'waterlight')
line(33,87,45,87,'ripple')
line(34,81,40,82,'glow')

# Near right tiled column, cropped by the frame, reinforces the room's scale.
poly([(118,26),(126,23),(126,76),(118,73)],'tilelight')
poly([(126,23),(127,23),(127,77),(126,76)],'wall2')
for y in range(28,74,5):
    line(118,y+1,125,y-1,'grout')
line(122,25,122,74,'floorline')
line(118,26,118,72,'white')
poly([(116,72),(125,74),(127,77),(120,76),(116,74)],'coping')

# Girl, viewed from behind, floating alone near the middle of the pool.
# A restrained reflection sits directly below the ring.
line(64,102,78,102,'waterdeep')
line(66,104,77,104,'watermid')
line(69,107,74,107,'waterlight')
line(61,100,64,100,'refl')
line(79,100,83,100,'waterlight')
line(63,103,66,103,'ripple')
# Ring shadow and curved yellow tube.
ellipse(71,97,10,5,'yellowdark')
ellipse(71,96,10,4,'yellow')
ellipse(71,95,9,3,'yellowlight')
ellipse(71,95,5,2,'waterdeep')
ellipse(71,96,5,2,'pool')
# Back and shoulder silhouette over the back half of the ring.
poly([(68,87),(74,87),(76,91),(74,96),(68,96),(66,91)],'skinshade')
poly([(68,87),(74,87),(75,92),(73,95),(69,95),(67,91)],'skin')
rect(70,85,3,4,'skin')
line(68,89,66,94,'skinhi')
line(74,89,77,94,'skinhi')
line(65,94,67,95,'skin')
line(76,95,78,94,'skin')
# Muted blue swimsuit across her lower back.
poly([(68,92),(74,92),(75,96),(67,96)],'swim')
line(68,89,69,93,'swimdark')
line(74,89,73,93,'swimdark')
# Dark damp hair, no face visible.
ellipse(71,83,4,5,'hairshade')
ellipse(71,82,3,4,'hair')
rect(68,83,7,5,'hair')
line(68,85,69,89,'hairshade')
line(74,84,74,88,'hairshade')
line(69,80,71,79,'hairlight')
line(68,82,68,84,'hairlight')
# Front tube masks the seated body and reads as a continuous ring.
path('M 61 96 Q 61 101 71 101 Q 81 101 81 96 L 77 96 Q 77 98 71 98 Q 65 98 65 96 Z','yellow')
line(64,99,67,100,'yellowlight')
line(68,100,74,100,'yellowlight')
line(78,98,79,97,'yellowshade')
line(62,97,62,98,'yellowshade')

assert tuple(c.stats()['size']) == (128, 128)
assert c.stats()['colors_used'] <= 86
save('poolcore-water-slide', c)
view(c, scale=4, margin=0)
finish(c)
