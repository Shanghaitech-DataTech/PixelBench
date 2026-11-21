# 32x32 RPG item portrait: metal USB flash drive with keychain strap
result = new_canvas(32, 32, background=None, name="usb-flash-drive")

# Palette
outline = "#151922"
deep = "#252c38"
shadow = "#4a5663"
mid = "#71808c"
light = "#aebbc2"
shine = "#dce4e6"
plug_dark = "#59636b"
plug_mid = "#929da3"
plug_hi = "#d1d8d9"
slot = "#303741"
strap_dark = "#202630"
strap_mid = "#485462"
strap_hi = "#748391"

# Keychain strap behind the drive: thick angular loop
result.poly([(23,17),(27,17),(27,19),(30,22),(30,26),(27,29),(23,29),(21,27),(21,24),(23,22),(25,22),(23,24),(23,26),(24,27),(27,27),(28,25),(28,23),(25,20),(23,20)], outline)
result.poly([(25,19),(26,19),(29,22),(29,26),(27,28),(24,28),(22,26),(22,24),(23,23),(24,23),(23,25),(24,27),(27,27),(28,25),(28,23),(25,20)], strap_dark)
result.line(26,20,28,22,strap_hi)
result.line(28,23,28,25,strap_mid)
result.line(24,28,27,28,strap_mid)

# USB connector outline, projecting left
result.poly([(2,11),(4,9),(11,9),(13,11),(13,20),(11,22),(4,22),(2,20)], outline)
# Connector metal fill
result.poly([(3,12),(5,10),(10,10),(12,12),(12,19),(10,21),(5,21),(3,19)], plug_mid)
# Connector top highlight and lower shadow
result.poly([(4,11),(5,10),(10,10),(11,11),(11,13),(4,13)], plug_hi)
result.poly([(3,18),(12,18),(12,19),(10,21),(5,21),(3,19)], plug_dark)
result.set(4,14,light)
result.set(4,15,light)
# USB retention holes
result.rect(5,11,2,2,slot)
result.rect(9,11,2,2,slot)
result.set(5,11,deep)
result.set(9,11,deep)

# Main metal casing, chamfered silhouette
result.poly([(10,7),(24,7),(27,10),(27,20),(24,23),(10,23),(8,21),(8,10)], outline)
# Main body base
result.poly([(11,8),(23,8),(26,11),(26,19),(23,22),(11,22),(9,20),(9,11)], mid)
# Upper bevel
result.poly([(11,8),(23,8),(26,11),(24,12),(11,12),(9,11)], light)
result.line(12,9,22,9,shine)
result.set(23,9,shine)
result.set(24,10,shine)
# Face plate
result.poly([(11,12),(24,12),(26,14),(26,19),(23,22),(11,22),(9,20),(9,14)], shadow)
result.poly([(11,13),(23,13),(25,15),(25,18),(22,21),(12,21),(10,19),(10,15)], mid)
# Steel sheen bands
result.line(12,13,22,13,light)
result.line(11,14,18,14,"#8998a2")
result.line(11,15,15,15,light)
result.line(24,15,24,18,deep)
result.line(22,21,12,21,deep)
result.set(11,20,shadow)
# Small status light inset
result.rect(21,16,3,3,outline)
result.set(22,17,"#68cbd0")
result.set(23,17,"#9ce9e5")
# Separation seam at plug/body junction
result.line(9,11,9,20,deep)
result.line(10,10,10,21,"#313946")
result.set(10,11,light)
result.set(10,12,light)

view(result, scale=16, margin=0)
finish(result)
