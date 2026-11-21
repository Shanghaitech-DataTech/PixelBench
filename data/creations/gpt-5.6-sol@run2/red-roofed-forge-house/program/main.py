# Red-roofed forge house, 128x128 isometric RTS tile.
from pixelbench_api import new_canvas, view, finish

c = new_canvas(128, 128, background=None, name="red-roofed-forge-house")

# Compact palette.
outline = "#2b2020"
deep = "#3b2926"
shadow = "#544039"
ground_dark = "#6d6659"
ground = "#898171"
ground_light = "#aaa18d"
grass = "#687451"
grass_light = "#87915f"
plaster_dark = "#816b58"
plaster = "#aa8d6d"
plaster_light = "#c4a77f"
beam_dark = "#4b3025"
beam = "#6b432d"
beam_light = "#8a5b36"
roof_deep = "#582625"
roof_dark = "#7d302b"
roof = "#a94435"
roof_light = "#ca6045"
roof_glint = "#e07a54"
metal = "#4d5554"
metal_light = "#737a72"
soot = "#302a29"
fire_deep = "#a63a20"
fire = "#ef702d"
fire_hot = "#ffd36a"
wood_dark = "#513322"
wood = "#79502d"
wood_light = "#a7773f"
rope = "#c09a5e"

# Ground shadow and worked stone apron.
c.poly([(9,87),(54,65),(118,91),(70,121)], deep)
c.poly([(11,84),(54,64),(117,88),(69,117)], ground_dark)
c.poly([(15,82),(54,66),(112,88),(68,113)], ground)
# Ground facets / stones.
c.poly([(15,82),(29,77),(37,81),(23,87)], ground_light)
c.poly([(76,103),(91,96),(105,101),(89,109)], ground_light)
c.poly([(46,105),(58,100),(69,105),(57,111)], "#777064")
c.line(20,91,34,97,ground_dark); c.line(35,75,44,79,ground_dark)
c.line(87,87,99,92,ground_dark); c.line(66,110,76,114,ground_dark)
c.set(14,95,grass); c.set(15,94,grass_light); c.set(16,95,grass)
c.line(106,82,111,79,grass); c.set(109,79,grass_light)
c.line(26,105,29,101,grass); c.set(30,103,grass_light)

# Building wall mass, outlined first.
c.poly([(21,55),(67,72),(108,59),(108,96),(67,114),(21,96)], outline)
# Left/front wall and right wall.
c.poly([(24,59),(66,75),(66,109),(24,94)], plaster)
c.poly([(69,75),(105,64),(105,94),(69,109)], plaster_dark)
# Wall lighting planes.
c.poly([(27,63),(62,76),(62,84),(27,72)], plaster_light)
c.poly([(72,78),(102,69),(102,76),(72,86)], "#9a7e62")

# Heavy timber frame, all aligned to the isometric faces.
c.poly([(23,72),(66,88),(66,92),(23,76)], beam_dark)
c.poly([(23,91),(66,107),(66,112),(23,96)], beam_dark)
c.poly([(61,73),(68,75),(68,111),(61,109)], beam_dark)
c.poly([(25,60),(29,61),(29,94),(25,93)], beam)
c.poly([(43,67),(48,69),(48,101),(43,99)], beam)
c.poly([(69,84),(105,73),(105,78),(69,89)], beam_dark)
c.poly([(69,103),(105,90),(105,96),(69,111)], beam_dark)
c.poly([(99,64),(105,62),(105,95),(99,98)], beam)
# Pegs.
for x,y in [(28,75),(46,83),(46,98),(64,91),(64,106),(72,86),(86,81),(101,76),(84,102),(101,94)]:
    c.rect(x,y,2,2,deep)

# Furnace housing on right face, framed and dark.
c.poly([(73,80),(97,73),(97,99),(73,108)], outline)
c.poly([(76,82),(94,77),(94,97),(76,103)], metal)
c.poly([(79,84),(91,80),(91,96),(79,100)], soot)
# Arched lip and glow opening.
c.poly([(81,86),(89,84),(92,88),(92,96),(79,100),(79,92)], fire_deep)
c.poly([(82,89),(88,87),(90,90),(90,95),(81,98),(81,92)], fire)
c.poly([(84,91),(88,90),(89,92),(89,95),(83,96),(83,93)], fire_hot)
c.set(86,92,"#fff0a0")
c.line(76,82,94,77,metal_light); c.line(76,103,94,97,deep)
# Small anvil shelf.
c.poly([(68,97),(78,94),(83,96),(73,100)], outline)
c.poly([(69,95),(78,92),(84,94),(74,98)], metal_light)
c.rect(73,98,4,5,metal)

# Roof outline and two planes: ridge runs on a true isometric diagonal.
c.poly([(46,24),(93,42),(110,61),(68,77),(20,59),(37,41)], outline)
c.poly([(47,27),(92,44),(106,60),(62,47)], roof_dark)
c.poly([(47,27),(92,44),(67,74),(23,57)], roof)
# Front roof edge thickness.
c.poly([(23,57),(67,74),(67,79),(22,62)], roof_deep)
c.poly([(67,74),(106,60),(106,64),(67,79)], roof_dark)
# Ridge cap.
c.line(47,26,93,43,roof_deep)
c.line(47,27,92,44,roof_light)
c.line(50,29,90,44,roof_glint)
# Tile courses across the large red plane.
for a,b,d,e in [(42,34,87,51),(37,40,82,57),(32,46,77,63),(27,52,72,69)]:
    c.line(a,b,d,e,roof_dark)
    c.set(a+2,b,roof_light)
# Tile joints, short and staggered.
for x,y in [(55,34),(69,39),(82,44),(47,40),(61,45),(75,50),(39,46),(53,51),(67,56),(31,52),(45,57),(59,62)]:
    c.line(x,y,x-4,y+5,roof_deep)
    c.set(x-1,y+1,roof_light)
# Sparse highlights on rear roof plane.
c.line(65,47,99,59,roof_light)
c.line(70,43,101,55,roof_deep)
c.set(84,49,roof_glint); c.set(85,49,roof_glint)

# Chimney punching through roof.
c.poly([(75,31),(84,28),(91,31),(82,35)], outline)
c.poly([(76,17),(85,14),(85,31),(76,34)], roof_deep)
c.poly([(85,14),(91,17),(91,31),(85,33)], deep)
c.poly([(76,17),(85,14),(91,17),(82,21)], outline)
c.poly([(79,17),(85,15),(89,17),(83,19)], soot)
c.line(78,22,84,20,roof_light)
c.line(86,21,90,20,shadow)
# Soot pixels / restrained smoke.
c.set(87,11,"#625853aa"); c.set(88,10,"#625853aa")
c.set(91,7,"#756b65a0"); c.set(92,7,"#756b65a0")

# Front window tucked under eave.
c.poly([(31,74),(41,78),(41,91),(31,87)], outline)
c.poly([(33,77),(39,79),(39,87),(33,85)], "#5d4839")
c.line(36,78,36,86,wood_light); c.line(33,82,39,84,wood_light)
c.set(34,79,"#d9a655"); c.set(38,85,"#d9a655")

# Wooden hanging sign at left foreground.
c.line(25,73,18,94,beam_dark); c.line(26,73,19,94,beam)
c.line(18,79,31,83,beam_dark); c.set(20,81,rope)
c.poly([(8,82),(27,88),(25,99),(6,93)], outline)
c.poly([(10,83),(25,88),(23,96),(8,92)], wood)
c.line(10,85,24,89,wood_light)
# Hammer mark on sign.
c.line(13,88,19,93,rope); c.line(18,89,21,90,rope); c.set(17,91,rope)

# Stacked barrels at right: dark rims, warm wood staves.
def barrel(cx, cy):
    c.poly([(cx-6,cy-5),(cx,cy-8),(cx+6,cy-5),(cx+6,cy+5),(cx,cy+8),(cx-6,cy+5)], outline)
    c.poly([(cx-4,cy-4),(cx,cy-6),(cx+4,cy-4),(cx+4,cy+4),(cx,cy+6),(cx-4,cy+4)], wood)
    c.line(cx-4,cy-3,cx+4,cy-1,wood_light)
    c.line(cx-5,cy+1,cx+5,cy+3,beam_dark)
    c.line(cx-2,cy-5,cx-2,cy+5,wood_dark)
    c.line(cx+2,cy-5,cx+2,cy+5,wood_dark)
barrel(105,102)
barrel(94,108)
barrel(108,113)
# Metal barrel hoops catch the light.
c.line(100,100,110,103,metal_light); c.line(89,106,99,109,metal_light)

# A few hard pixel accents unify silhouette.
c.set(20,61,outline); c.set(21,63,outline); c.set(68,79,outline)
c.set(67,113,outline); c.set(106,96,outline)

view(c, scale=4, margin=0)
finish(c)
