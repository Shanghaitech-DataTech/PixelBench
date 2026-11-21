result = new_canvas(32, 32, name='usb_flash_drive')
c = result
ink = '#182330'
shadow = '#3b4c60'
steel = '#8197a6'
light = '#c1d2d9'
shine = '#eff8ee'
# Woven keychain loop, behind the metal housing.
c.poly([(6,20),(9,23),(9,27),(7,30),(3,30),(1,28),(1,24),(3,21)], ink)
c.poly([(5,22),(7,24),(7,27),(6,28),(3,28),(2,26),(3,23)], '#53697c')
c.poly([(5,23),(6,24),(6,26),(5,27),(4,27),(3,26),(4,24)], None)
c.line(2,25,2,27,'#91a3b1')
c.line(4,29,6,29,'#70869a')
# Exposed USB-A plug, with a darker side wall.
c.poly([(22,2),(29,9),(29,12),(23,18),(14,10)], ink)
c.poly([(22,4),(27,9),(22,14),(17,9)], light)
c.poly([(27,10),(28,10),(28,11),(23,16),(22,14)], shadow)
c.line(18,8,22,4,shine)
c.line(23,5,26,8,shine)
c.line(19,12,23,16,'#657f91')
# Two recessed retention holes in the connector.
c.poly([(21,6),(23,8),(21,10),(19,8)], ink)
c.line(21,7,22,8,'#4b6172')
c.poly([(24,9),(26,11),(24,13),(22,11)], ink)
c.line(24,10,25,11,'#4b6172')
# Rounded, chamfered casing silhouette.
c.poly([(14,9),(16,9),(25,18),(25,20),(15,30),(12,30),(3,21),(3,18)], ink)
c.poly([(14,11),(16,11),(23,18),(23,20),(14,29),(12,28),(5,21),(5,18)], steel)
# Side bevel and lower end cap.
c.poly([(22,18),(24,19),(24,20),(15,29),(13,29),(12,27)], shadow)
c.line(15,28,23,20,'#627b8d')
c.poly([(5,19),(13,27),(15,27),(13,29),(5,21)], '#61798a')
# Broad brushed-metal face with a bright top-left bevel.
c.poly([(14,11),(16,11),(21,16),(21,18),(12,27),(5,20),(5,18)], light)
c.line(5,18,14,10,shine)
c.line(5,19,12,26,'#e2ece8')
c.poly([(15,12),(18,15),(9,24),(6,21)], '#d8e4e3')
c.line(18,17,12,23,'#a5bcc6')
c.line(19,18,16,21,'#a5bcc6')
# Collar seam separates shell and connector.
c.line(15,10,24,19,ink)
c.line(14,11,22,19,'#718999')
c.set(15,11,'#e4efeb')
# Small blue status window inset into the shell.
c.line(11,18,14,15,'#40576a')
c.line(12,18,14,16,'#258da7')
c.set(13,17,'#77e0e7')
# Strap attachment eyelet at the rear corner.
c.poly([(6,21),(8,23),(7,25),(5,23)], ink)
c.set(6,22,'#d9e5e5')
c.set(7,23,'#6f8597')
view(result, scale=12)
finish(result)
