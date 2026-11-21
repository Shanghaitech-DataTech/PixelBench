result = new_canvas(32,32)
c=result
ink='#191b26'
shadow='#37343d'
metal='#9ba9ac'
light='#e0e6d7'
# shutter and winding dial
c.rect(23,5,5,3,ink)
c.rect(24,5,3,1,light)
c.rect(24,6,3,2,'#b27849')
c.rect(5,6,5,2,ink)
c.rect(6,6,3,1,metal)
# raised viewfinder housing
c.poly([(11,8),(13,5),(19,5),(22,8)],ink)
c.rect(14,6,5,2,metal)
c.line(14,6,18,6,light)
# main silhouette
c.rect(3,8,26,18,ink)
c.rect(2,10,28,14,ink)
c.rect(5,26,22,1,ink)
# top metal shell
c.rect(4,9,24,6,metal)
c.line(5,9,26,9,light)
c.rect(3,11,2,4,'#6e7b87')
c.rect(27,10,2,5,'#63717d')
c.line(5,14,27,14,'#58616c')
# viewfinder window
c.rect(7,10,6,4,ink)
c.rect(8,11,4,2,'#486778')
c.line(8,11,10,11,'#9dc3c3')
# tiny meter
c.rect(22,11,4,2,shadow)
c.set(23,11,'#ead1a0')
c.set(24,11,'#dca55e')
# leather front
c.rect(4,15,24,10,'#754d3d')
c.rect(4,15,3,9,'#a27450')
c.rect(26,15,2,10,'#513b36')
c.line(5,24,26,24,'#4b3532')
# stippled leather grain
for y in range(16,24):
    for x in range(5,27):
        if (x*3+y*5)%7==0: c.set(x,y,'#956649')
        elif (x*5+y*3)%11==0: c.set(x,y,'#563c33')
# base chrome
c.line(4,25,27,25,'#78868b')
c.line(6,25,11,25,'#bbc5bd')
# strap lugs
c.rect(1,12,3,4,ink)
c.rect(2,13,1,2,metal)
c.rect(28,12,3,4,ink)
c.rect(29,13,1,2,metal)
# circular lens mounting and knurled barrel
c.circle(17,18,8,ink)
c.circle(17,18,7,'#59626e')
c.poly([(11,14),(14,11),(20,11),(23,14),(23,20),(20,24),(14,24),(10,20),(10,16)],'#9ba9ac')
c.line(14,11,20,11,light)
c.line(11,14,12,13,light)
c.line(10,16,10,19,'#ccd6cf')
c.line(14,24,20,24,'#414b5a')
c.circle(17,18,6,ink)
c.circle(17,18,5,'#364b62')
c.circle(17,18,4,'#1d2b42')
c.poly([(14,16),(16,14),(19,15),(20,17),(19,20),(16,21),(14,19)],'#285571')
c.poly([(16,16),(19,16),(20,18),(18,20),(16,19)],'#16364f')
c.line(14,17,16,15,'#76babd')
c.set(15,15,'#dfefde')
c.line(17,21,20,18,'#438497')
c.set(19,20,'#76babd')
# lens ring etched marks
c.set(13,13,light)
c.set(22,16,'#d0d6c9')
c.set(12,22,'#6e7b87')
# front release and seam
c.rect(6,17,2,2,ink)
c.set(6,17,'#d6b26c')
c.set(25,22,'#bf9767')
view(result)
finish(result)
