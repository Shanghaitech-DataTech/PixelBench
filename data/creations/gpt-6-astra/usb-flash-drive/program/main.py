result = new_canvas(32, 32, name='usb_flash_drive')
# Compact palette: blue-black contours and cool brushed steel.
ink='#172333'
dark='#33465a'
shade='#596f82'
mid='#8aa1b1'
light='#bdced5'
shine='#edf5ed'
# The fabric key strap loops out from the bottom of the metal housing.
result.poly([(11,22),(14,23),(13,26),(10,29),(6,30),(3,28),(3,25),(6,22),(9,21)],ink)
result.poly([(8,23),(11,23),(10,25),(7,28),(5,27),(5,26)],shade)
result.poly([(8,24),(10,24),(8,26),(6,27),(6,26)],None)
result.line(4,25,4,27,mid)
result.line(6,29,9,28,dark)
# Exposed USB-A plug, angled up and to the right.
result.poly([(18,3),(21,2),(29,10),(29,12),(23,18),(13,8)],ink)
result.poly([(19,4),(21,3),(28,10),(27,12),(22,16),(15,9)],mid)
result.poly([(19,4),(21,4),(27,10),(25,12),(18,6)],light)
result.line(18,5,25,12,shine)
result.poly([(25,12),(28,10),(28,12),(23,17),(21,15)],shade)
# Two dark rectangular retention apertures in the connector shell.
result.poly([(20,6),(22,8),(20,10),(18,8)],dark)
result.line(20,7,21,8,ink)
result.poly([(24,10),(26,12),(24,14),(22,12)],dark)
result.line(24,11,25,12,ink)
# Metal body with a heavy stepped silhouette.
result.poly([(13,9),(16,9),(24,17),(24,20),(14,29),(11,29),(3,21),(3,18)],ink)
result.poly([(13,10),(15,10),(23,18),(23,20),(13,28),(11,27),(4,20),(4,18)],shade)
result.poly([(13,10),(15,10),(22,17),(12,27),(4,19)],light)
result.poly([(13,12),(15,11),(21,17),(12,26),(6,20),(6,18)],mid)
result.line(4,18,13,10,shine)
result.line(5,20,11,26,light)
result.line(13,27,22,18,dark)
result.line(15,26,23,19,mid)
# Dark collar between body and plug.
result.poly([(13,9),(15,8),(25,18),(23,20)],ink)
result.line(14,9,23,18,shade)
result.line(15,9,23,17,light)
# Brushed bevel catches and engraved detail.
result.line(8,17,11,14,light)
result.line(8,18,13,13,light)
result.line(9,20,15,14,light)
result.line(12,22,17,17,shade)
result.line(13,23,18,18,light)
# Small blue activity light recessed into the shell.
result.line(9,23,11,25,dark)
result.line(9,22,11,24,'#247e9b')
result.set(10,23,'#71d8e4')
# Strap attachment at the foot of the housing.
result.poly([(5,20),(8,23),(6,25),(3,22)],ink)
result.line(4,21,6,23,mid)
result.set(5,22,shine)
view(result)
finish(result)
