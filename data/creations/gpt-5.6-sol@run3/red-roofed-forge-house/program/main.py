from pixelbench_api import *

# 128x128 isometric forge-house on transparency.
c = new_canvas(128, 128, background=None, name="red_roofed_forge_house")

# Palette
outline = "#241b19"
deep = "#392421"
shadow = "#4b3028"
stone_dark = "#5a5149"
stone = "#756c5f"
stone_light = "#958978"
plaster = "#b8a680"
plaster_light = "#d0bd91"
wood_dark = "#4d2c20"
wood = "#75462a"
wood_light = "#a36738"
roof_dark = "#642521"
roof = "#96362c"
roof_light = "#c6533e"
roof_hi = "#e0704d"
metal_dark = "#343237"
metal = "#55545a"
metal_hi = "#89878a"
ember = "#c94524"
orange = "#f07a27"
gold = "#ffb632"
yellow = "#ffe06a"
barrel_band = "#302c2b"

# Ground contact shadow (small, tile-like, not a full base).
c.poly([(25,88),(62,67),(108,91),(69,116)], "#201a1a66")
c.poly([(31,91),(62,74),(101,94),(68,111)], "#3b292455")

# Main building lower walls, clean isometric planes.
# Left/front plane
c.poly([(31,61),(64,78),(64,109),(31,92)], outline)
c.poly([(34,63),(62,78),(62,105),(34,90)], plaster)
# Right plane
c.poly([(64,78),(103,58),(103,91),(64,112)], outline)
c.poly([(67,79),(100,62),(100,89),(67,107)], stone)

# Stone courses on right wall.
c.line(67,87,100,70,stone_dark)
c.line(67,96,100,79,stone_dark)
c.line(69,104,99,88,stone_dark)
for a,b,d,e in [(76,75,76,83),(88,69,88,75),(82,82,82,90),(94,76,94,83),(73,94,73,101),(87,87,87,95)]:
    c.line(a,b,d,e,stone_light)
# Plaster shading and masonry flecks.
c.line(35,88,61,102,"#9b8969")
c.line(35,69,35,88,plaster_light)
c.set(42,77,stone_light); c.set(43,77,stone_light)
c.set(54,92,"#927c60"); c.set(55,93,"#927c60")

# Heavy timber framing.
c.poly([(31,61),(35,63),(35,91),(31,92)],wood_dark)
c.poly([(60,76),(65,78),(65,111),(60,108)],wood_dark)
c.poly([(31,87),(64,104),(64,110),(31,93)],wood_dark)
c.poly([(34,64),(63,79),(63,84),(34,69)],wood)
c.poly([(43,68),(47,70),(47,96),(43,94)],wood)
c.poly([(34,88),(61,102),(61,106),(34,92)],wood)
c.line(35,64,61,78,wood_light)
c.line(47,72,59,78,wood_light)

# Furnace annex/opening on right face.
c.poly([(69,85),(84,77),(96,83),(96,97),(82,105),(69,99)], outline)
c.poly([(72,87),(84,81),(93,85),(93,94),(82,101),(72,97)], stone_dark)
# Arched furnace mouth.
c.poly([(76,91),(78,86),(83,83),(88,85),(91,89),(91,95),(82,100),(76,97)],deep)
c.poly([(79,91),(80,87),(83,86),(87,87),(89,90),(89,94),(82,97),(79,95)],ember)
c.poly([(81,91),(82,88),(85,88),(88,90),(88,93),(83,96),(81,94)],orange)
c.poly([(83,92),(84,89),(87,90),(87,93),(84,94)],yellow)
c.set(88,89,gold); c.set(80,96,roof_light)
# Hearth ledge.
c.poly([(70,98),(82,104),(97,96),(97,100),(82,108),(70,102)],outline)
c.poly([(74,99),(82,103),(94,97),(94,99),(82,105),(74,101)],metal)
c.line(82,103,94,97,metal_hi)

# Roof main outline and planes.
# Left roof plane
c.poly([(24,57),(58,35),(69,75),(63,82)],outline)
c.poly([(28,57),(56,39),(65,74),(62,77)],roof)
# Right roof plane
c.poly([(58,35),(111,57),(69,80),(62,77)],outline)
c.poly([(59,39),(105,58),(69,76),(65,74)],roof_dark)
# Thick eaves.
c.poly([(24,57),(62,77),(69,76),(69,82),(62,84),(23,63)],deep)
c.poly([(28,59),(62,76),(62,80),(28,62)],roof_dark)
c.poly([(69,76),(107,56),(111,58),(70,81)],deep)
c.line(70,77,106,58,roof_light)

# Roof tile rows and highlights, following isometric axes.
for yoff in [0,7,14,21]:
    # left plane rows
    x0=31+yoff//2; y0=55+yoff
    c.line(x0,y0,62,y0+16-yoff//2,roof_dark)
# left tile seams as short diagonal runs
for x,y in [(38,51),(47,46),(53,43),(35,60),(45,56),(55,52),(39,67),(50,63),(57,60)]:
    c.line(x,y,x+3,y+7,roof_light)
    c.set(x+1,y,roof_hi)
# Right roof courses parallel to edge.
c.line(62,45,101,61,roof)
c.line(64,52,93,64,roof)
c.line(66,60,84,67,roof)
c.line(68,68,76,71,roof)
for x,y in [(67,43),(80,48),(93,54),(72,52),(85,57),(70,60),(78,63)]:
    c.line(x,y,x-5,y+3,roof_light)
c.line(58,38,105,58,roof_hi)
c.line(29,57,56,40,roof_hi)

# Roof ridge cap.
c.poly([(55,35),(59,33),(111,55),(111,59),(106,60),(57,39)],outline)
c.poly([(59,35),(107,55),(107,58),(59,38)],roof_light)
c.line(61,35,106,54,roof_hi)

# Chimney behind roof, with stone cap.
c.poly([(84,38),(93,42),(93,57),(84,53)],outline)
c.poly([(87,39),(91,42),(91,53),(87,51)],stone_dark)
c.poly([(93,42),(99,39),(99,53),(93,57)],outline)
c.poly([(94,43),(97,42),(97,51),(94,53)],stone)
c.poly([(83,37),(91,33),(101,38),(93,43)],outline)
c.poly([(87,37),(91,35),(97,38),(93,40)],stone_light)
c.set(88,37,"#b1a18b"); c.set(96,38,plaster)
# Smoke wisps, blocky and subdued.
c.rect(91,27,5,4,"#776f6a99")
c.rect(94,23,5,5,"#8a817b88")
c.rect(98,19,4,4,"#9b938c66")

# Front door with iron fittings.
c.poly([(47,81),(58,87),(58,105),(47,99)],outline)
c.poly([(49,84),(56,88),(56,101),(49,97)],wood)
c.line(51,84,51,98,wood_light)
c.line(55,87,55,101,wood_dark)
c.set(54,94,gold)

# Hanging wooden sign on front-left.
c.line(33,69,25,73,metal_dark)
c.line(27,71,27,78,metal_dark)
c.poly([(18,76),(28,71),(38,76),(28,82)],outline)
c.poly([(21,76),(28,73),(35,76),(28,79)],wood_light)
c.line(23,76,28,78,plaster_light)
c.set(30,75,gold); c.set(31,76,gold)

# Barrels stacked by left wall, each with readable curved silhouette.
def barrel(cx,cy):
    c.poly([(cx-5,cy-6),(cx,cy-8),(cx+5,cy-6),(cx+5,cy+4),(cx,cy+7),(cx-5,cy+4)],outline)
    c.poly([(cx-3,cy-5),(cx,cy-6),(cx+3,cy-5),(cx+3,cy+3),(cx,cy+5),(cx-3,cy+3)],wood)
    c.line(cx-3,cy-3,cx+3,cy-3,barrel_band)
    c.line(cx-3,cy+2,cx+3,cy+2,barrel_band)
    c.line(cx-2,cy-5,cx+2,cy-5,wood_light)
barrel(28,96)
barrel(39,102)
barrel(27,108)
# Barrel rims and tiny highlights.
c.set(27,89,wood_light); c.set(38,95,wood_light); c.set(26,101,wood_light)

# Anvil beside forge, unmistakable profile.
c.poly([(93,102),(105,96),(111,98),(106,102),(103,103),(104,108),(97,112),(95,110),(98,106),(93,105)],outline)
c.poly([(96,102),(105,98),(108,99),(104,101),(101,102),(102,107),(98,109),(97,108),(100,104),(96,104)],metal)
c.line(98,102,106,99,metal_hi)

# Loose coals/sparks and final high-contrast accents.
c.set(70,104,ember); c.set(73,106,orange); c.set(88,101,gold)
c.set(76,83,roof_hi); c.set(96,65,stone_light)
c.set(31,85,plaster_light); c.set(34,66,plaster_light)

finish(c)
view(c, scale=4, margin=0)
