# 128x128 sports motorcycle sprite, transparent background.
result = new_canvas(128, 128, background=None, name="sport_motorcycle")

# Compact palette.
OUT = "#101216"
TIRE = "#090b0e"
TIRE_HI = "#24282d"
RIM = "#697078"
SILVER = "#b9c0c5"
LIGHT = "#e1e5e7"
METAL = "#8d969d"
DARK = "#24282d"
DARK2 = "#343a40"
BLACK = "#15181c"
MID = "#4a5056"
RED = "#d52b30"
RED_HI = "#f04a43"
RED_DARK = "#861b22"

# Wheels: chunky tires, subtle tread, metal rims, pale spokes.
for cx in (34, 96):
    result.circle(cx, 91, 22, TIRE)
    result.circle(cx, 91, 18, TIRE_HI)
    result.circle(cx, 91, 15, OUT)
    result.circle(cx, 91, 14, RIM)
    result.circle(cx, 91, 11, DARK)
    # Eight spoke star, kept behind hubs.
    for x1, y1 in ((34,77),(34,105),(20,91),(48,91),(24,81),(44,101),(24,101),(44,81)):
        result.line(cx, 91, x1 + (cx-34), y1, LIGHT)
    result.circle(cx, 91, 5, METAL)
    result.circle(cx, 91, 2, OUT)
# Tire edge blocks / tread marks.
for cx in (34, 96):
    result.rect(cx-13, 70, 8, 3, DARK2)
    result.rect(cx+8, 72, 7, 3, DARK2)
    result.rect(cx-22, 84, 4, 7, DARK2)
    result.rect(cx+19, 87, 4, 7, DARK2)
    result.rect(cx-15, 108, 8, 3, DARK2)
    result.rect(cx+7, 108, 8, 3, DARK2)

# Rear swingarm and visible silver tubular chassis.
result.poly([(31,87),(58,78),(82,87),(79,92),(57,84),(36,94)], METAL)
result.poly([(34,88),(58,74),(78,86),(75,89),(58,80),(38,94)], SILVER)
result.poly([(50,63),(63,61),(78,86),(73,88),(59,69),(49,69)], SILVER)
result.poly([(57,66),(66,66),(78,86),(73,86)], METAL)
# Chain and rear axle hardware.
result.line(35,96,70,92,METAL)
result.line(35,99,70,95,OUT)
result.circle(35,96,3,SILVER)

# Front fork, two parallel silver blades, behind fairing.
result.poly([(91,55),(96,55),(101,88),(97,90)], SILVER)
result.poly([(86,57),(90,56),(98,88),(94,90)], METAL)
result.rect(93,58,6,5, LIGHT)
result.circle(96,91,4,SILVER)

# Engine block and cylinder fins.
result.poly([(50,73),(66,68),(80,75),(78,94),(65,102),(49,96),(44,84)], OUT)
result.rect(50,72,19,17,DARK2)
result.rect(53,75,18,3,MID)
result.rect(51,80,21,2,METAL)
result.rect(50,84,21,2,MID)
result.rect(51,88,17,2,METAL)
result.circle(63,91,12,METAL)
result.circle(63,91,9,"#a5adb3")
result.circle(63,91,6,DARK2)
result.circle(63,91,3,SILVER)
result.line(57,94,68,87,LIGHT)
# Exhaust header and upswept muffler.
result.line(73,89,78,99,METAL)
result.line(78,99,94,104,METAL)
result.poly([(77,98),(94,101),(106,94),(108,97),(96,106),(78,102)], DARK2)
result.poly([(95,101),(108,94),(112,96),(99,106)], METAL)
result.rect(108,95,5,3,OUT)

# Main tank and broad aerodynamic fairing, stepped pixel silhouette.
result.poly([(42,58),(51,51),(72,49),(84,54),(94,58),(101,67),(96,78),(81,84),(71,77),(54,75),(46,82),(37,78),(39,68)], OUT)
result.poly([(46,58),(54,53),(71,52),(82,56),(87,62),(79,68),(58,66)], DARK2)
result.poly([(40,65),(53,60),(76,61),(91,58),(101,66),(96,76),(79,81),(70,74),(54,72),(45,79),(38,75)], DARK)
# Tank crown and highlight plane.
result.poly([(49,57),(55,50),(70,48),(82,53),(85,58),(76,62),(57,61)], BLACK)
result.poly([(55,53),(69,51),(78,54),(80,57),(60,57)], MID)
result.rect(59,51,12,2,"#5b6268")
# Lower fairing with cutout suggestion around engine.
result.poly([(70,65),(90,60),(102,67),(96,76),(81,84),(76,79),(82,73),(72,72)], DARK2)
result.poly([(86,65),(100,66),(97,72),(85,73),(80,70)], MID)
result.poly([(79,76),(96,74),(89,82),(80,85),(73,80)], BLACK)
# Red speed stripe integrated into fairing.
result.poly([(45,64),(68,62),(89,63),(94,66),(70,67),(49,68)], RED_DARK)
result.poly([(52,63),(72,62),(87,64),(68,65),(50,66)], RED)
result.rect(84,64,8,2,RED_HI)

# Seat and upswept tail unit.
result.poly([(45,57),(32,53),(19,48),(12,49),(17,56),(38,64),(52,63)], OUT)
result.poly([(43,58),(31,55),(18,51),(15,52),(20,56),(40,62)], DARK2)
result.poly([(43,55),(33,51),(22,48),(15,49),(23,53),(44,60)], BLACK)
result.poly([(22,48),(14,45),(10,46),(14,51)], RED_DARK)
result.rect(11,46,8,3,RED)
result.rect(12,46,5,1,RED_HI)
# Rear undertray and small bracket.
result.poly([(24,57),(42,62),(39,67),(20,61)], OUT)
result.line(28,62,33,73,METAL)

# Nose, headlamp slit, handlebar and tilted windscreen.
result.poly([(88,57),(97,52),(110,54),(116,60),(111,68),(101,68),(96,61)], OUT)
result.poly([(97,55),(109,56),(113,60),(109,64),(100,64),(95,60)], DARK2)
result.rect(108,58,7,3,LIGHT)
result.rect(111,61,3,2,METAL)
# Windscreen leans forward to the right.
result.poly([(87,54),(92,41),(103,38),(109,52),(100,54)], OUT)
result.poly([(91,51),(95,43),(102,41),(106,50),(100,52)], "#20252a")
result.line(95,43,101,41,MID)
# Cockpit/clip-on.
result.line(84,53,93,49,SILVER)
result.line(90,48,97,48,OUT)
result.rect(95,47,6,3,BLACK)

# Exposed frame sections remain visible below the bodywork.
result.poly([(48,68),(51,68),(60,77),(58,79)], SILVER)
result.poly([(59,77),(74,69),(77,70),(62,80)], METAL)
result.rect(51,69,3,2,LIGHT)
# Front fender lip follows the top of the tire.
result.poly([(79,76),(86,72),(99,71),(107,76),(105,78),(98,75),(87,75),(81,79)], DARK2)
result.rect(87,73,11,1,MID)

# Pixel highlights, bolts, vents and final silhouette accents.
result.rect(43,69,4,2,MID)
result.rect(46,73,3,2,METAL)
result.rect(91,69,4,2,OUT)
result.rect(88,72,6,2,OUT)
result.circle(76,65,2,SILVER)
result.circle(49,63,1,LIGHT)
result.set(103,57,LIGHT)
# Brake discs and caliper details over spokes.
result.circle(96,91,9,METAL,fill=False)
result.circle(34,91,8,METAL,fill=False)
result.rect(87,86,4,7,RED)
result.rect(88,87,2,4,RED_HI)

view(result, scale=4, margin=2, edges="all")
finish(result)
