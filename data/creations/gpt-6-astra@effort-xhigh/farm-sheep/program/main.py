# A small, warm farm sheep. Pixel clusters stay on the native 32px grid.
result = new_canvas(32, 32, name="farm-sheep")
c = result
wool_shadow = '#d8cfbc'
wool_mid = '#e9e2d0'
wool_light = '#f6f2e5'
wool_hi = '#fffbee'
deep_wool = '#c6baa5'
face_shadow = '#c9baa6'
face_mid = '#dfd1ba'
face_light = '#efe2ca'
hoof = '#998775'
hoof_light = '#b5a18b'
pink = '#dfafa8'
pink_light = '#efd0c3'
eye = '#655b50'

# Far legs are tucked behind the fleece.
c.rect(11, 21, 3, 6, face_shadow)
c.rect(11, 26, 3, 2, hoof)
c.rect(21, 21, 3, 6, face_shadow)
c.rect(21, 26, 3, 2, hoof)
# Near legs, with small warm hooves.
c.rect(7, 21, 3, 7, face_mid)
c.rect(7, 23, 1, 4, face_light)
c.rect(7, 27, 3, 2, hoof)
c.set(7, 27, hoof_light)
c.rect(18, 22, 3, 6, face_mid)
c.rect(18, 23, 1, 4, face_light)
c.rect(18, 27, 3, 2, hoof)
c.set(18, 27, hoof_light)

# Short woolly tail peeps out at the rump.
c.poly([(3,15),(1,15),(1,18),(3,20),(5,18),(5,16)], wool_shadow)
c.rect(1,15,3,3,wool_light)
c.set(2,18,wool_mid)

# Scalloped fleece silhouette.
c.ellipse(13,16,10,8,wool_shadow)
for x,y,r in [(7,12,4),(11,10,4),(16,10,4),(20,12,4),
              (21,16,4),(20,20,4),(15,21,4),(10,21,4),(6,18,4)]:
    c.circle(x,y,r,wool_shadow)
# Broad, soft flat-shaded masses, no dark contour.
c.ellipse(13,15,9,7,wool_mid)
for x,y,r in [(7,11,3),(11,9,3),(16,9,3),(20,11,3),
              (21,15,3),(6,17,3),(10,20,3),(15,20,3),(20,19,3)]:
    c.circle(x,y,r,wool_mid)
c.ellipse(12,13,8,6,wool_light)
for x,y,r in [(7,11,3),(11,9,3),(16,9,3),(19,11,3),(6,15,3),
              (10,17,3),(15,16,4),(19,15,3)]:
    c.circle(x,y,r,wool_light)
# Sparse upper planes and rounded curl marks.
c.line(10,7,13,7,wool_hi)
c.line(9,8,11,8,wool_hi)
c.line(16,7,17,7,wool_hi)
c.line(5,10,7,10,wool_hi)
c.line(4,11,5,11,wool_hi)
c.line(8,14,10,14,wool_hi)
c.set(8,15,wool_hi)
c.line(14,11,16,11,wool_hi)
c.set(14,12,wool_hi)
c.line(14,18,16,18,wool_mid)
c.set(13,17,wool_mid)
c.line(5,19,6,20,wool_mid)
c.line(10,22,12,22,wool_light)
c.line(17,21,19,21,wool_light)

# Far pink ear, lifted just above the forehead.
c.poly([(24,11),(25,8),(27,6),(29,6),(29,8),(27,11),(26,13)],face_mid)
c.poly([(25,10),(27,7),(28,7),(28,8),(26,11)],pink_light)
c.set(27,8,pink)
# Gently sloped profile and rounded, hanging muzzle.
c.poly([(23,12),(27,12),(29,14),(29,18),(30,20),(30,22),
        (28,24),(25,24),(23,22),(22,17)],face_shadow)
c.poly([(24,13),(27,13),(28,14),(28,18),(29,20),(29,22),
        (27,23),(25,22),(24,20),(23,16)],face_mid)
c.poly([(25,14),(27,14),(28,16),(27,19),(28,21),(26,22),
        (25,20),(24,16)],face_light)
# Soft fleece cap at the brow.
c.circle(24,12,3,wool_shadow)
c.circle(22,11,3,wool_mid)
c.circle(25,11,3,wool_mid)
c.circle(23,10,3,wool_light)
c.rect(25,10,3,3,wool_light)
c.line(22,8,24,8,wool_hi)
c.set(21,9,wool_hi)
# Near ear folds out toward the viewer, blush inset.
c.poly([(24,14),(21,13),(19,14),(20,17),(22,18),(24,16)],face_shadow)
c.poly([(22,14),(20,14),(21,16),(22,17),(23,15)],pink_light)
c.line(21,15,22,16,pink)
# Single calm eye and discreet muzzle details.
c.set(27,16,eye)
c.set(27,17,'#a49580')
c.set(29,21,'#aa9583')
c.line(27,23,28,23,'#b7a48d')

view(result, scale=12, margin=0)
save('farm-sheep', result)
finish(result)
