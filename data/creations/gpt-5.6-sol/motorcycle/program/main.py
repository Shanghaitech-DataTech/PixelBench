# 128x128 side-profile sport motorcycle
c = new_canvas(128, 128, background=None, name="sport_motorcycle")

# Compact palette
OUT = "#080a0c"
TIRE = "#0d1013"
TIRE_HI = "#22272b"
DARK = "#15191d"
BODY = "#20262b"
BODY2 = "#30383e"
METAL_D = "#59636a"
METAL = "#8e999f"
SILVER = "#c4ccd0"
WHITE = "#edf1f2"
RED_D = "#8c1017"
RED = "#e2252f"
RED_HI = "#ff5960"
GLASS = "#11171c"

# Ground-facing wheel silhouettes
for cx, cy in [(32, 91), (96, 91)]:
    c.circle(cx, cy, 21, OUT)
    c.circle(cx, cy, 18, TIRE)
    # Blocky tread glints
    c.rect(cx-11, cy-17, 8, 2, TIRE_HI)
    c.rect(cx+8, cy-13, 5, 2, TIRE_HI)
    c.rect(cx-19, cy-2, 2, 8, TIRE_HI)
    c.rect(cx+17, cy-4, 2, 8, TIRE_HI)
    c.rect(cx-11, cy+15, 7, 2, "#050607")
    # Rim and inner wheel
    c.circle(cx, cy, 13, METAL_D)
    c.circle(cx, cy, 11, DARK)
    # White spokes
    for ex, ey in [(cx,cy-11),(cx+8,cy-8),(cx+11,cy),(cx+8,cy+8),(cx,cy+11),(cx-8,cy+8),(cx-11,cy),(cx-8,cy-8)]:
        c.line(cx, cy, ex, ey, WHITE)
    c.circle(cx, cy, 4, METAL)
    c.circle(cx, cy, 2, SILVER)

# Rear swingarm behind body
c.poly([(31,87),(61,78),(65,82),(36,94)], OUT)
c.poly([(32,87),(61,80),(62,83),(36,92)], METAL)
c.rect(26, 88, 11, 5, DARK)

# Exhaust underbody, rising toward rear
c.poly([(45,91),(70,91),(83,85),(85,89),(72,98),(47,98)], OUT)
c.poly([(48,92),(69,92),(81,87),(82,90),(70,96),(48,96)], METAL_D)
c.rect(44,92,7,6,METAL)

# Main silver tubular frame (black under-stroke + silver inset)
frame_segments = [((39,60),(62,88)),((39,60),(76,58)),((76,58),(62,88)),((62,88),(91,83))]
for (x0,y0),(x1,y1) in frame_segments:
    for off in (-2,-1,0,1,2): c.line(x0, y0+off, x1, y1+off, OUT)
    for off in (-1,0,1): c.line(x0, y0+off, x1, y1+off, SILVER)

# Engine block and round cover
c.poly([(48,65),(67,62),(77,70),(74,87),(62,96),(46,87),(42,75)], OUT)
c.poly([(49,66),(66,64),(74,71),(71,85),(62,92),(48,85),(45,75)], BODY2)
c.rect(52,67,14,4,METAL_D)
c.rect(47,73,8,3,METAL)
c.circle(61,82,12,OUT)
c.circle(61,82,9,METAL)
c.circle(61,82,6,METAL_D)
c.circle(61,82,3,SILVER)
c.line(56,82,66,82,SILVER)
c.line(61,77,61,87,SILVER)

# Upswept tail and seat
c.poly([(14,47),(23,42),(51,45),(62,55),(57,64),(31,60),(20,55)], OUT)
c.poly([(16,47),(25,44),(49,47),(56,53),(51,57),(29,55),(20,52)], BODY2)
# Red tail insert
c.poly([(13,46),(23,42),(26,46),(19,51),(13,50)], RED_D)
c.rect(14,46,7,3,RED)
c.set(14,46,RED_HI)
# seat
c.poly([(27,42),(50,44),(58,50),(54,54),(27,51),(21,47)], OUT)
c.poly([(29,44),(49,46),(54,49),(52,51),(29,49),(24,47)], DARK)
c.line(30,44,48,46,TIRE_HI)

# Fuel tank, strongly arched
c.poly([(47,45),(55,38),(70,35),(82,40),(86,51),(77,61),(58,60),(51,54)], OUT)
c.poly([(50,46),(57,40),(70,37),(79,41),(82,50),(75,57),(59,57),(54,52)], BODY)
c.poly([(57,41),(70,38),(78,42),(78,46),(55,48)], BODY2)
c.line(55,50,77,52,METAL_D)
c.rect(65,39,8,2,METAL_D)

# Broad front fairing and pointed nose
c.poly([(76,43),(88,38),(107,43),(117,52),(115,66),(105,77),(86,75),(74,64),(72,52)], OUT)
c.poly([(78,45),(89,41),(105,45),(113,52),(111,64),(103,72),(87,71),(77,62),(75,53)], BODY)
# fairing facets
c.poly([(88,43),(105,46),(112,53),(109,57),(91,55),(80,49)], BODY2)
c.poly([(78,53),(91,56),(108,58),(105,68),(88,68),(78,61)], DARK)
c.poly([(88,58),(106,59),(103,66),(88,66)], "#272e33")
c.line(87,68,103,68,METAL_D)
# red aerodynamic slash
c.poly([(78,58),(91,60),(86,66),(76,62)], RED_D)
c.poly([(80,59),(90,61),(86,64),(78,62)], RED)
c.line(81,59,89,61,RED_HI)
# lower belly fairing
c.poly([(72,70),(88,72),(105,73),(99,82),(76,87),(68,83)], OUT)
c.poly([(74,72),(88,74),(101,75),(96,79),(77,84),(71,81)], BODY2)
c.line(76,82,96,78,METAL_D)

# Tilted black windscreen
c.poly([(82,43),(87,31),(102,34),(109,43),(103,45),(91,40)], OUT)
c.poly([(87,40),(90,33),(100,35),(106,42),(101,43),(92,39)], GLASS)
c.line(91,34,99,36,BODY2)
c.set(103,40,METAL_D)

# Handlebar and grip
c.line(82,40,88,35,OUT)
c.line(87,35,96,33,OUT)
c.rect(94,31,8,3,DARK)
c.rect(98,31,5,2,TIRE_HI)

# Front fork, set over the fairing edge down to hub
for off in (-2,-1,0,1,2): c.line(106+off,61,97+off,90,OUT)
for off in (-1,0,1): c.line(106+off,61,97+off,90,SILVER)
c.line(108,62,100,89,METAL)
c.rect(94,86,8,7,OUT)
c.rect(96,87,5,5,METAL)

# Front brake disc details
c.circle(96,91,7,METAL,fill=False)
for p in [(96,85),(101,88),(102,93),(97,97),(92,95),(90,90),(93,86)]: c.set(p[0],p[1],OUT)
c.rect(89,85,4,7,OUT)
c.rect(90,86,2,5,RED)

# Exposed upper sections of the silver tubular frame
for (x0,y0),(x1,y1) in [((48,58),(55,69)),((76,58),(69,69))]:
    for off in (-1,0,1): c.line(x0+off,y0,x1+off,y1,OUT)
    c.line(x0,y0,x1,y1,SILVER)
c.circle(55,69,2,OUT)
c.set(55,69,SILVER)
c.circle(69,69,2,OUT)
c.set(69,69,SILVER)

# Small body fasteners and highlights
for x,y in [(78,49),(84,46),(106,51),(80,74),(48,53),(69,57)]: c.set(x,y,SILVER)
c.line(101,47,109,52,METAL_D)
c.rect(108,54,5,2,SILVER)
c.rect(110,55,4,2,WHITE)

# Foot peg and controls
c.rect(66,86,11,3,OUT)
c.rect(68,86,8,2,SILVER)
c.line(70,84,76,90,METAL)

view(c, scale=4, margin=0)
finish(c)
