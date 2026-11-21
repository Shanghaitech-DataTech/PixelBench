# A single inventory portrait, built at its native pixel resolution.
result = new_canvas(32, 32, name="usb_flash_drive")
c = result
ink = '#17212f'
deep = '#304455'
shade = '#536c7e'
steel = '#819ba9'
mid = '#aabdc4'
light = '#d4e0df'
glint = '#f4f6e9'

# Woven keychain loop, behind the metal housing.
c.path('M 7 21 L 10 24 L 10 27 L 7 30 L 3 30 L 1 28 L 1 25 L 4 22 Z M 5 25 L 3 27 L 4 28 L 6 28 L 8 26 L 7 24 Z', ink)
c.path('M 7 21 L 10 24 L 10 27 L 7 30 L 3 30 L 1 28 L 1 25 L 4 22 Z', ink, fill=False)
c.path('M 5 23 L 3 25 L 2 27 L 2 28 L 4 29 L 6 29 L 9 26', shade, fill=False)
c.line(2,26,2,27, steel)
c.line(4,29,6,29, steel)
c.line(7,28,9,26, deep)

# USB-A plug: exposed silver shell, with a dark bevel on its right edge.
c.poly([(17,8),(24,1),(26,1),(30,5),(30,8),(23,15)], ink)
c.poly([(18,8),(24,2),(25,2),(29,6),(23,12)], light)
c.poly([(23,12),(29,6),(29,8),(23,14)], shade)
c.line(19,8,24,3,glint)
c.line(25,2,29,6,glint)
c.line(24,12,29,7,steel)
# Two punched retention windows in the connector's broad face.
c.rect(22,5,2,2,deep)
c.set(22,5,ink)
c.set(22,7,glint)
c.rect(25,8,2,2,deep)
c.set(25,8,ink)
c.set(25,10,glint)
# The mouth of the connector and its bright rolled lip.
c.line(24,2,29,7,shade)
c.line(25,2,29,6,glint)

# Beveled metal casing.
c.poly([(4,19),(16,7),(18,7),(24,13),(24,15),(12,27),(10,27),(4,21)], ink)
c.poly([(5,19),(16,8),(18,8),(23,13),(23,15),(12,26),(10,26),(5,21)], shade)
c.poly([(5,19),(16,8),(18,8),(22,12),(22,14),(11,25),(9,24)], mid)
c.poly([(5,19),(16,8),(17,8),(21,12),(10,23),(8,22)], light)
c.line(5,19,16,8,glint)
c.line(6,20,17,9,glint)
c.line(10,25,22,13,steel)
c.line(12,25,23,14,mid)
c.line(13,25,23,15,deep)
# A dark collar separates casing and plug.
c.line(17,8,23,14,deep)
c.line(17,9,22,14,steel)
c.set(18,9,light)

# Tiny engraved USB fork, turned along the drive's axis.
c.line(10,20,16,14,steel)
c.line(12,18,11,17,steel)
c.line(11,17,11,15,steel)
c.set(11,15,shade)
c.line(13,17,15,19,steel)
c.set(16,19,steel)
c.set(16,18,shade)
c.line(14,14,16,14,steel)
c.set(16,15,steel)
c.set(10,20,shade)
c.set(10,21,steel)
# A small blue status lamp inset into the lower bevel.
c.line(16,21,18,19,deep)
c.line(16,20,18,18,'#479dad')
c.set(17,19,'#a9e5db')

# Riveted strap eyelet at the back corner; strap enters the slot.
c.poly([(5,21),(7,21),(10,24),(9,26),(7,26),(5,24)], deep)
c.line(6,21,9,24,light)
c.line(6,23,8,25,ink)
c.set(6,24,shade)
c.set(7,25,steel)
c.set(9,25,steel)

view(result, scale=12, margin=0)
save('usb-flash-drive', result)
finish(result)
