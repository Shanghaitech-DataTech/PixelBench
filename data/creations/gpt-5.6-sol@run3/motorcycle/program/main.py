# 128x128 sports motorcycle, side profile facing right.
result = new_canvas(128, 128, background=None, name="sport_motorcycle")

# Compact palette.
OUT = "#101216"
DEEP = "#171a20"
TIRE = "#202329"
TREAD = "#30343b"
DARK = "#282c33"
BODY = "#343941"
MID = "#494f58"
EDGE = "#626a73"
METAL_D = "#737b83"
METAL = "#9aa2a8"
SILVER = "#bcc3c7"
WHITE = "#e1e4e3"
RED_D = "#8f1820"
RED = "#d72832"
RED_HI = "#f05252"
AMBER = "#d68b2b"

# Wheels: dark rubber, subtly faceted inner rims.
for cx in (34, 96):
    result.circle(cx, 91, 20, OUT)
    result.circle(cx, 91, 17, TIRE)
    result.circle(cx, 91, 13, DARK)
    result.circle(cx, 91, 11, "transparent")
    # tread flashes around circumference
    result.rect(cx-12, 73, 7, 2, TREAD)
    result.rect(cx+6, 74, 7, 2, TREAD)
    result.rect(cx-19, 82, 3, 6, TREAD)
    result.rect(cx+17, 83, 3, 6, TREAD)
    result.rect(cx-18, 99, 4, 4, TREAD)
    result.rect(cx+14, 101, 4, 3, TREAD)

# Spokes and hubs (drawn behind chassis).
for cx in (34, 96):
    for ex, ey in ((cx,80),(cx,102),(cx-10,91),(cx+10,91),(cx-7,83),(cx+7,83),(cx-7,99),(cx+7,99)):
        result.line(cx, 91, ex, ey, WHITE)
    result.circle(cx, 91, 5, METAL_D)
    result.circle(cx, 91, 3, SILVER)
    result.set(cx, 91, OUT)

# Rear sprocket and chain.
result.circle(34, 91, 7, METAL_D, fill=False)
result.line(35, 84, 65, 84, METAL_D)
result.line(35, 86, 65, 86, OUT)
result.rect(46, 84, 15, 1, SILVER)

# Tubular frame triangle.
result.line(51, 62, 68, 91, OUT)
result.line(52, 61, 70, 90, SILVER)
result.line(70, 90, 39, 90, OUT)
result.line(68, 88, 41, 88, METAL)
result.line(41, 88, 54, 60, OUT)
result.line(43, 87, 56, 61, SILVER)
result.line(55, 63, 81, 69, OUT)
result.line(55, 65, 80, 71, METAL)

# Rear swingarm.
result.poly([(34,87),(65,82),(68,87),(37,93)], OUT)
result.poly([(37,87),(63,83),(65,86),(38,91)], METAL_D)
result.line(39, 88, 61, 85, SILVER)

# Engine mass and round cover.
result.poly([(54,69),(72,68),(80,77),(75,91),(56,92),(49,82)], OUT)
result.poly([(56,71),(70,70),(77,77),(73,89),(57,89),(52,81)], MID)
result.rect(58, 73, 13, 3, METAL_D)
result.rect(55, 78, 4, 9, DARK)
result.circle(67, 82, 10, OUT)
result.circle(67, 82, 8, METAL_D)
result.circle(67, 82, 6, METAL)
result.circle(67, 82, 3, MID)
result.set(67,79,SILVER)
result.set(70,82,SILVER)
result.rect(72,72,3,4,SILVER)

# Exhaust header and upswept muffler.
result.line(73, 82, 78, 92, OUT)
result.line(75, 81, 80, 90, METAL_D)
result.line(80, 90, 102, 82, OUT)
result.line(80, 88, 100, 81, METAL)
result.poly([(77,87),(96,78),(104,78),(103,83),(81,92)], OUT)
result.poly([(82,86),(97,80),(102,80),(101,82),(83,89)], SILVER)
result.rect(98,80,4,2,METAL_D)

# Main streamlined fairing silhouette.
result.poly([(49,54),(67,48),(87,49),(100,58),(95,69),(82,76),(62,73),(47,66),(42,59)], OUT)
result.poly([(50,55),(67,50),(85,51),(96,58),(91,67),(79,73),(62,70),(48,64),(45,59)], BODY)
# Wide dark-gray lower fairing.
result.poly([(50,64),(62,68),(82,70),(91,65),(88,74),(79,82),(68,77),(54,75)], OUT)
result.poly([(53,65),(63,69),(79,71),(88,67),(84,73),(77,79),(68,75),(56,73)], DARK)
result.poly([(62,69),(83,69),(78,74),(68,74)], MID)
# Fairing vent and angular panel lines.
result.poly([(76,55),(91,57),(86,62),(72,62)], DEEP)
result.poly([(78,56),(89,58),(85,60),(75,60)], TIRE)
result.line(59,53,53,63,EDGE)
result.line(60,54,75,51,MID)
result.line(88,64,80,69,EDGE)
result.rect(51,62,6,2,RED)
result.rect(57,64,5,2,RED_D)

# Fuel tank, with red sport stripe.
result.poly([(48,52),(57,43),(74,42),(84,48),(79,56),(60,58),(49,55)], OUT)
result.poly([(51,52),(59,45),(72,44),(80,48),(77,53),(60,56),(52,54)], BODY)
result.poly([(57,46),(70,45),(77,48),(72,50),(55,52)], MID)
result.poly([(52,53),(63,51),(78,50),(76,54),(60,56)], RED_D)
result.poly([(57,52),(76,50),(72,53),(60,55)], RED)
result.rect(63,45,7,1,EDGE)

# Seat and upswept tail unit.
result.poly([(47,48),(40,44),(27,45),(18,51),(20,56),(44,55),(54,52)], OUT)
result.poly([(44,49),(39,46),(28,47),(21,51),(22,53),(43,53),(51,51)], DEEP)
result.poly([(37,44),(25,41),(13,46),(11,51),(19,51),(29,47),(43,49)], OUT)
result.poly([(35,45),(25,43),(16,46),(14,49),(20,49),(29,46),(39,48)], BODY)
# Red tail cowl and lamp.
result.poly([(26,43),(17,43),(12,46),(20,47)], RED_D)
result.rect(10,47,6,3,OUT)
result.rect(11,47,5,2,RED)
result.rect(11,47,3,1,RED_HI)

# Rear shock.
result.line(45,60,38,78,OUT)
result.line(47,61,40,79,SILVER)
for y in range(64,77,3):
    result.line(42,y,46,y+1,RED)

# Steering head and silver front fork.
result.poly([(88,53),(96,54),(92,62),(86,61)], OUT)
result.poly([(90,54),(94,55),(91,60),(88,59)], METAL)
result.line(93,59,99,88,OUT)
result.line(96,58,102,88,OUT)
result.line(95,59,100,88,SILVER)
result.line(98,58,103,87,METAL_D)
result.rect(98,85,6,5,OUT)
result.rect(99,86,4,3,METAL)

# Nose cone and tilted small black windscreen.
result.poly([(79,48),(86,41),(101,45),(106,53),(98,60),(91,56)], OUT)
result.poly([(82,48),(88,43),(99,46),(103,52),(97,57),(93,54)], BODY)
result.poly([(85,43),(89,35),(96,35),(102,45),(98,46),(92,40)], OUT)
result.poly([(89,42),(91,36),(95,37),(99,44),(96,44),(92,40)], TIRE)
result.line(92,37,95,38,MID)
# Headlamp and nose accent.
result.poly([(99,48),(104,50),(102,53),(98,52)], SILVER)
result.set(102,50,WHITE)
result.poly([(92,54),(101,53),(98,57),(91,59)], RED_D)
result.line(94,55,99,54,RED_HI)

# Handlebar and controls.
result.line(88,42,83,38,OUT)
result.line(84,38,79,39,OUT)
result.rect(78,38,5,2,TIRE)
result.rect(86,40,3,3,METAL_D)

# Front fender hugs the tire.
result.path("M 82 79 Q 94 67 108 78 L 107 82 Q 96 72 85 82 Z", OUT)
result.path("M 85 79 Q 95 71 105 79 L 104 80 Q 96 74 87 81 Z", BODY)
result.line(88,78,101,75,RED)

# Foot controls and small hardware.
result.rect(72,88,8,3,OUT)
result.rect(73,88,7,1,SILVER)
result.line(57,88,52,95,OUT)
result.rect(48,94,8,2,METAL)
result.circle(51,55,2,SILVER)
result.circle(84,62,1,SILVER)
result.circle(77,72,1,SILVER)

# Crisp scattered highlights that reinforce the pixel-art planes.
result.line(30,43,36,45,EDGE)
result.line(18,50,25,47,MID)
result.rect(48,57,2,5,METAL_D)
result.rect(83,51,6,1,EDGE)
result.set(45,53,WHITE)
result.set(58,45,SILVER)
result.set(81,48,SILVER)

view(result, scale=4, margin=0)
finish(result)
