result = new_canvas(32,32,name='usb_flash_drive')
c=result
ink='#172032'
shadow='#37465c'
steel='#7e94a8'
light='#c3d4de'
shine='#f0f5ec'
# Woven loop trailing from the base, with transparent opening.
c.path('M 12 22 L 9 24 L 6 24 L 4 26 L 4 29 L 6 31 L 10 31 L 13 28 L 15 25 L 14 23 Z',ink)
c.path('M 11 24 L 8 26 L 6 26 L 6 29 L 9 29 L 12 26 L 13 24 Z','#51677d')
c.path('M 8 26 L 7 27 L 7 28 L 9 28 L 11 26 L 12 24 L 10 25 Z',None)
c.line(5,27,5,29,'#9baab5')
c.line(10,29,12,27,'#7e94a8')
# Connector protrudes from upper-right end.
c.poly([(19,7),(24,2),(26,2),(30,6),(30,9),(25,14)],ink)
c.poly([(20,7),(25,3),(29,7),(29,9),(24,13)],steel)
c.poly([(20,7),(25,3),(29,7),(24,12)],light)
c.line(25,3,29,7,shine)
c.line(25,12,29,8,'#536a80')
# Two punched contact windows.
c.line(23,6,24,7,ink)
c.line(24,5,25,6,ink)
c.line(26,9,27,10,ink)
c.line(27,8,28,9,ink)
# Body silhouette with a bevelled metal rim.
c.poly([(17,8),(20,8),(26,14),(26,17),(16,27),(13,27),(5,19),(5,16),(14,7)],ink)
c.poly([(15,9),(18,9),(24,15),(24,17),(15,26),(13,25),(7,19),(7,16)],shadow)
c.poly([(15,9),(18,9),(24,15),(15,24),(13,24),(7,18),(7,16)],steel)
c.poly([(15,9),(18,9),(23,14),(14,23),(8,17)],light)
c.poly([(15,9),(17,9),(9,17),(8,17)],shine)
c.line(9,19,13,23,'#e3e9e5')
c.line(16,24,24,16,'#536a80')
c.line(17,24,24,17,'#a2b7c5')
# Inset brushed panel and subtle diagonal grain.
c.poly([(16,12),(18,12),(21,15),(14,22),(10,18)],'#91a7b8')
c.line(12,18,17,13,'#afc2ce')
c.line(15,20,20,15,'#70879b')
# Blue activity lamp, housed in a dark recess.
c.line(15,19,18,16,ink)
c.line(15,18,17,16,'#37b8cc')
c.set(16,17,'#a0f4e7')
# Keyring eyelet near the tail.
c.line(10,21,12,23,ink)
c.set(11,22,'#d6e4e7')
c.line(11,24,12,23,'#71869b')
view(result,scale=12)
finish(result)
