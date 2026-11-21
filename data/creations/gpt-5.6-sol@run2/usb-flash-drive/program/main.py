# 32x32 RPG item portrait: metal USB flash drive
c = new_canvas(32, 32, background=None, name="usb_flash_drive")

# Palette
outline = c.color("#151820", "outline")
deep = c.color("#252b35", "deep")
shadow = c.color("#414955", "shadow")
mid = c.color("#69727c", "metal_mid")
light = c.color("#aeb8bd", "metal_light")
shine = c.color("#e2e9e7", "shine")
slot = c.color("#202a36", "usb_slot")
blue = c.color("#397ea2", "usb_blue")
strap_dark = c.color("#25222b", "strap_dark")
strap_mid = c.color("#554b5c", "strap_mid")

# Keychain strap behind the drive: a stepped loop at the lower-right.
c.set(25, 19, outline)
c.rect(26, 19, 3, 2, outline)
c.rect(28, 20, 2, 5, outline)
c.rect(26, 24, 3, 2, outline)
c.rect(23, 25, 4, 2, outline)
c.rect(21, 23, 3, 3, outline)
c.set(22, 22, outline)
# Inner strap colour leaves a dark outer rim.
c.rect(26, 20, 2, 1, strap_mid)
c.rect(28, 21, 1, 3, strap_mid)
c.rect(26, 24, 2, 1, strap_mid)
c.rect(23, 25, 3, 1, strap_mid)
c.rect(22, 23, 1, 2, strap_mid)
c.set(27, 21, strap_dark)
c.set(27, 23, strap_dark)
c.set(24, 24, strap_dark)

# Main drive dark silhouette, angled down toward the right.
c.poly([(10,7),(19,9),(27,15),(27,19),(23,23),(18,22),(8,15)], outline)
# Body shadow base.
c.poly([(11,9),(18,10),(25,15),(25,19),(22,21),(18,20),(10,14)], shadow)
# Upper metal face.
c.poly([(11,9),(18,10),(25,15),(23,17),(17,15),(10,12)], mid)
c.poly([(12,9),(18,11),(23,15),(21,15),(16,13),(11,11)], light)
c.line(13,10,18,12,shine)
c.set(19,12,shine)
# Lower bevel and rear cap.
c.poly([(10,13),(17,16),(23,18),(25,16),(25,19),(22,21),(18,20),(10,14)], deep)
c.poly([(17,16),(23,18),(25,16),(25,19),(22,21),(18,20)], shadow)
c.line(18,17,22,19,mid)
c.set(22,20,light)
c.rect(24,15,2,4, deep)
c.set(25,16, mid)
# Small lanyard hole in the rear cap.
c.rect(23,18,2,2, outline)
c.set(24,18, strap_dark)

# USB connector silhouette protruding to upper-left.
c.poly([(3,5),(12,8),(12,14),(8,17),(2,14),(2,7)], outline)
# Plug metal faces.
c.poly([(4,6),(11,9),(11,13),(8,15),(3,13),(3,8)], mid)
c.poly([(4,6),(11,9),(9,11),(3,9)], light)
c.line(5,7,10,9,shine)
c.poly([(3,9),(9,11),(11,9),(11,13),(8,15),(3,13)], shadow)
c.poly([(4,10),(8,11),(8,14),(4,12)], deep)
# USB contact holes and blue insert.
c.rect(4,8,2,1, slot)
c.rect(8,9,2,1, slot)
c.set(4,7, shine)
c.poly([(4,11),(7,12),(7,14),(4,12)], blue)
c.set(4,11, "#65a9c1")
# Connector/body seam and crisp edge accents.
c.line(11,9,11,13,outline)
c.set(10,9, light)
c.set(10,13, deep)
c.set(8,15, outline)

# A few isolated specular pixels for an RPG-item glint.
c.set(17,10, shine)
c.set(20,13, shine)
c.set(14,9, "#cbd4d3")

result = c
view(result, scale=16, margin=0)
finish(result)
