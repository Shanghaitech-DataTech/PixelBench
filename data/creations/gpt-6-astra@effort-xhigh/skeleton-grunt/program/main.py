# 32 x 32 RPG skeleton grunt; all pixels are opaque or fully transparent.
result = new_canvas(32, 32, name="skeleton_grunt")
c = result
P = {
    'ink':'#252532', 'deep':'#383640', 'joint':'#4d4848',
    'bone_dark':'#797765', 'bone_shade':'#aaa78a', 'bone':'#d6d0aa',
    'light':'#f4e9c4', 'white':'#fff5d8',
    'steel_dark':'#415367', 'steel':'#809caa', 'steel_light':'#c4dce0',
    'edge':'#eef5e9', 'wood_dark':'#4d3029', 'wood_shade':'#734632',
    'wood':'#a66b3b', 'wood_light':'#ca9050', 'wood_glint':'#e2b16b',
    'iron_dark':'#454a48', 'iron':'#767b6b', 'iron_light':'#aeb09a',
    'leather':'#6d5040',
}
for n, col in P.items(): c.color(col, n)
def px(x,y,col): c.set(x,y,col)
def rect(x,y,w,h,col): c.rect(x,y,w,h,col)
def poly(points,col): c.poly(points,col)
def line(x,y,xx,yy,col): c.line(x,y,xx,yy,col)

# Back arm and raised shoulder produce the stooped silhouette.
poly([(17,11),(20,11),(23,14),(24,18),(21,20),(19,17),(18,14)], 'ink')
line(19,12,21,14,'bone_shade')
px(20,12,'bone'); px(21,15,'joint')
line(22,16,22,18,'bone')

# Bent legs, with open negative spaces at the knees and between the shins.
poly([(13,21),(16,22),(14,26),(12,27),(11,29),(13,29),(14,31),(8,31),(8,29),(10,25),(11,23)],'ink')
line(12,23,11,25,'bone'); px(13,23,'light')
px(11,26,'joint'); px(12,26,'bone_dark')
line(10,27,9,29,'bone'); px(10,27,'light')
line(9,30,12,30,'bone_shade'); px(9,29,'light')
poly([(17,21),(20,22),(21,25),(20,27),(23,29),(23,31),(17,31),(17,29),(18,28),(17,25),(16,23)],'ink')
line(18,23,19,25,'bone'); px(18,23,'light')
px(19,26,'joint')
line(19,27,20,29,'bone_shade'); px(19,27,'light')
line(18,30,22,30,'bone'); px(18,29,'light'); px(22,30,'bone_dark')

# Rib cage: black gaps, a bowed spine, and curved ivory ribs.
poly([(14,11),(18,11),(20,13),(21,17),(19,20),(18,22),(13,22),(12,19),(12,14)],'ink')
line(17,12,18,17,'bone_dark')
px(16,12,'bone'); px(18,13,'bone')
line(13,14,16,13,'bone'); px(13,14,'light'); px(17,14,'bone_shade')
line(14,16,17,16,'bone'); px(13,15,'bone_shade'); px(14,16,'light')
line(14,18,17,18,'bone'); px(13,17,'bone_dark'); px(14,18,'light')
px(19,14,'bone_shade'); px(19,16,'bone_shade'); px(18,17,'bone_dark')
px(18,19,'bone_shade'); px(16,19,'bone_dark')
px(16,20,'bone'); px(16,21,'bone_dark')
# Pelvic wings and the hollow at their centre.
line(12,20,13,22,'bone_shade'); px(12,20,'bone')
line(13,22,18,22,'bone'); px(14,23,'bone_dark')
px(18,21,'bone'); px(19,20,'bone_dark'); px(17,23,'bone_shade')

# Forward arm bends toward the sword grip.
poly([(12,12),(14,13),(12,16),(11,18),(8,21),(5,22),(5,19),(8,18),(9,15),(10,13)],'ink')
px(11,13,'light'); line(11,14,10,16,'bone'); px(10,17,'joint')
line(9,18,7,20,'bone'); px(8,19,'light')
px(7,21,'bone_dark')

# Short sword, cool metal with a continuous bright cutting edge.
poly([(3,7),(5,10),(6,17),(7,18),(6,20),(3,19),(3,14),(2,10)],'ink')
line(3,9,4,16,'steel_light')
line(4,11,5,17,'steel')
line(3,10,3,13,'edge'); px(4,14,'edge'); px(4,15,'edge'); px(4,16,'edge')
px(5,18,'steel_dark')
line(2,18,8,18,'ink'); line(2,19,8,19,'ink')
line(3,18,7,18,'iron_light'); px(7,18,'iron'); px(2,18,'iron_dark')
rect(5,20,2,3,'ink'); px(5,20,'leather'); px(5,22,'iron')
# Knuckles crossing the handle.
px(6,20,'light'); px(7,20,'bone'); px(6,21,'bone_shade')

# Compact wooden shield with a weathered metal rim.
poly([(23,13),(26,13),(29,16),(29,21),(27,24),(23,24),(20,21),(20,16)],'ink')
poly([(23,14),(26,14),(28,16),(28,21),(26,23),(23,23),(21,21),(21,16)],'iron_dark')
line(23,14,26,14,'iron_light'); line(22,15,21,17,'iron')
line(21,18,21,20,'iron_light'); line(22,22,24,23,'iron')
px(27,15,'iron'); px(28,17,'iron'); px(27,22,'iron')
poly([(23,15),(26,15),(27,16),(27,21),(26,22),(23,22),(22,21),(22,16)],'wood_shade')
rect(23,15,2,8,'wood'); rect(26,16,1,6,'wood')
line(23,16,23,20,'wood_light'); px(23,21,'wood_glint')
line(25,15,25,22,'wood_dark'); line(26,17,26,21,'wood_light')
px(22,19,'wood_dark'); px(24,16,'wood_light'); px(24,21,'wood_shade')
# Boss and rivets read at native size.
rect(23,17,4,4,'wood_dark')
rect(24,17,2,4,'iron_dark'); rect(23,18,4,2,'iron_dark')
rect(24,18,2,2,'iron'); px(24,18,'iron_light'); px(25,19,'iron_dark')
px(24,14,'light'); px(24,23,'iron_light'); px(28,19,'iron_light')

# Skull projects forward of the shoulder. Broken contours avoid a helmet look.
poly([(12,2),(16,2),(19,4),(20,7),(19,10),(17,11),(17,13),(12,13),(11,11),(9,10),(9,5),(10,3)],'ink')
poly([(12,3),(16,3),(18,4),(19,6),(18,9),(16,10),(16,12),(12,12),(12,10),(10,9),(10,5)],'bone_shade')
poly([(12,3),(16,3),(18,5),(18,7),(16,9),(12,9),(10,8),(10,5)],'bone')
line(12,3,15,3,'light'); line(10,5,10,7,'light'); line(11,4,16,4,'light')
px(17,5,'light'); px(18,6,'bone_dark'); px(19,7,'bone_dark')
# Deep asymmetric sockets, nasal cavity, cheek ridge.
rect(10,7,3,2,'ink'); px(11,6,'bone_dark'); px(13,7,'bone_dark')
rect(15,6,3,3,'ink'); px(15,6,'joint'); px(17,8,'deep')
px(14,9,'ink'); px(14,10,'joint')
px(10,9,'bone_dark'); px(11,9,'light'); px(17,9,'bone_dark')
# Teeth cut into the dark jaw line.
line(12,11,16,11,'ink'); px(12,11,'light'); px(14,11,'bone'); px(16,11,'bone')
line(12,12,16,12,'bone_shade'); px(12,12,'bone')
# Small cranial fracture.
px(15,3,'bone_dark'); px(15,4,'bone_shade'); px(16,5,'bone_dark')

view(result, scale=12, margin=2)
save('skeleton-grunt', result)
finish(result)
