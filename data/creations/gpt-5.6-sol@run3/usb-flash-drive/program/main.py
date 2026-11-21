# 32x32 RPG item portrait: metal USB flash drive
c = new_canvas(32, 32, background=None, name="usb-flash-drive")

# Palette
outline = "#17202b"
deep = "#24303d"
shadow = "#465563"
mid = "#71808a"
metal = "#aeb9bf"
light = "#dbe2e4"
shine = "#f4f7f5"
slot = "#303b45"
slot_hi = "#687783"
strap_dark = "#3a2635"
strap = "#80485c"
strap_hi = "#bd7182"

# USB connector, angled toward the upper-left.
c.poly([(2,7),(7,4),(15,7),(15,14),(10,17),(2,13)], outline)
c.poly([(3,7),(7,5),(14,8),(14,12),(9,15),(3,12)], mid)
# Top plane and bevels.
c.poly([(3,7),(7,5),(14,8),(10,10)], light)
c.poly([(10,10),(14,8),(14,12),(10,14)], shadow)
c.line(4,12,9,15,deep)
c.set(3,11,metal)
# Connector contact holes.
c.poly([(6,7),(8,7),(10,8),(8,9)], slot)
c.poly([(10,8),(12,9),(12,10),(10,9)], slot)
c.set(7,7,slot_hi)
c.set(11,9,slot_hi)

# Neck between plug and casing.
c.poly([(10,13),(14,10),(18,12),(18,17),(14,20),(10,17)], outline)
c.poly([(11,14),(14,12),(17,13),(17,16),(14,18),(11,16)], shadow)
c.poly([(11,14),(14,12),(17,13),(14,15)], metal)

# Main metal casing: broad diagonal RPG-item silhouette.
c.poly([(15,10),(19,9),(29,15),(29,21),(20,28),(14,25),(12,19)], outline)
c.poly([(16,11),(19,10),(28,16),(28,20),(20,26),(15,24),(14,19)], metal)
# Bright top face.
c.poly([(16,11),(19,10),(28,16),(25,18),(16,14)], light)
c.poly([(18,11),(20,11),(27,16),(26,16)], shine)
# Dark lower and right bevels.
c.poly([(15,20),(20,23),(28,18),(28,20),(20,26),(15,24)], shadow)
c.line(20,24,27,19,deep)
c.poly([(14,18),(16,14),(25,18),(20,22),(15,20)], mid)
# Brushed metal texture and specular chips.
c.line(17,15,22,18,"#c6d0d3")
c.line(18,19,21,21,"#88969f")
c.line(22,20,25,18,"#d1d9db")
c.set(16,17,light)
c.set(17,17,light)
c.set(19,22,"#65737e")
c.set(24,17,shine)
c.set(25,17,light)

# Small status inset on casing.
c.poly([(19,14),(21,14),(23,16),(21,17),(19,16)], deep)
c.set(20,15,"#58c6b8")
c.set(21,15,"#8bf0d8")

# Keychain eyelet cut/detail near the tail.
c.poly([(23,22),(26,20),(28,21),(28,23),(25,25),(23,24)], outline)
c.poly([(24,22),(26,21),(27,22),(27,23),(25,24),(24,23)], light)
c.set(25,22,deep)
c.set(26,22,deep)

# Keychain strap curling below the drive.
c.line(27,23,30,25,outline)
c.line(30,25,29,29,outline)
c.line(29,29,24,30,outline)
c.line(24,30,21,28,outline)
c.line(27,24,29,25,strap)
c.line(29,25,28,28,strap)
c.line(28,28,24,29,strap)
c.line(24,29,22,28,strap)
c.set(29,26,strap_hi)
c.set(27,29,strap_hi)

# Crisp silhouette accents.
c.set(2,8,deep)
c.set(2,12,deep)
c.set(7,4,deep)
c.set(29,16,deep)
c.set(29,20,deep)
c.set(14,24,deep)

result = c
view(result, scale=16, margin=0)
finish(result)
