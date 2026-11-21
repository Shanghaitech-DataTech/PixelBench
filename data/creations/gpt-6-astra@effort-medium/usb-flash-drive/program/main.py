result = new_canvas(32,32,name='usb_flash_drive')
c=result
ink='#202838'
shadow='#424f64'
mid='#76899b'
light='#bacbd4'
shine='#eef6ef'
# woven loop behind the drive, with open transparent centre
c.path('M 11 20 L 8 19 L 4 21 L 2 25 L 3 29 L 6 30 L 10 28 L 13 24 Z M 9 22 L 6 22 L 4 25 L 5 28 L 7 28 L 10 25 Z',ink)
c.line(3,25,4,28,shadow)
c.line(4,29,7,29,mid)
c.line(8,28,11,25,shadow)
c.line(4,22,7,20,mid)
# connector extends up-right
c.poly([(19,3),(22,1),(30,9),(30,11),(25,16),(17,8)],ink)
c.poly([(20,4),(22,3),(28,9),(24,13),(18,7)],light)
c.poly([(28,9),(29,10),(24,15),(23,13)],shadow)
c.line(20,4,22,3,shine)
c.line(22,3,27,8,shine)
# rectangular contact retention holes
c.poly([(22,5),(24,7),(22,9),(20,7)],ink)
c.line(21,7,22,8,shadow)
c.poly([(25,8),(27,10),(25,12),(23,10)],ink)
c.line(24,10,25,11,shadow)
# thick bevelled casing
c.poly([(16,7),(19,7),(26,14),(26,17),(15,28),(12,28),(5,21),(5,18)],ink)
c.poly([(16,9),(18,8),(24,14),(24,17),(14,27),(12,26),(6,20),(6,18)],shadow)
c.poly([(16,9),(18,9),(23,14),(23,16),(13,26),(7,20),(7,18)],mid)
c.poly([(16,9),(18,9),(22,13),(22,15),(12,25),(7,20),(7,18)],light)
# polished left bevel and darker right rail
c.line(7,18,16,9,shine)
c.line(7,19,12,24,shine)
c.line(14,25,24,15,shadow)
c.line(15,26,25,16,mid)
# inset brushed-metal panel
c.poly([(16,12),(19,13),(20,15),(12,23),(9,20),(9,19)],mid)
c.line(10,19,16,13,light)
c.line(11,20,17,14,light)
c.line(12,21,18,15,light)
# small activity light and attachment rivet
c.line(18,16,19,15,ink)
c.set(18,16,'#5ce4ce')
c.set(19,15,'#b6ffdf')
c.line(10,23,12,25,ink)
c.set(11,24,shadow)
view(result)
finish(result)
