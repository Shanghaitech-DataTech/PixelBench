# Two rotated views of the supplied house, reconstructed for a fixed elevated camera.
W = H = 160
T = None
ink = "#161c2e"
ink2 = "#293047"
shadow = "#4c3d35"
wood_dark = "#6c513a"
wood = "#98694e"
wood_light = "#c0804e"
plaster = "#bbae93"
plaster_hi = "#e1dca3"
roof_dark = "#72572f"
roof = "#97763d"
roof_mid = "#bda759"
roof_hi = "#dcaa46"
gold = "#f0c74f"
glass = "#e1d968"
glass_hi = "#fff19a"


def base(name):
    c = new_canvas(W, H, background=T, name=name)
    # Soft blocky ground shadow, matching the source's translucent footprint.
    c.poly([(12,137),(35,126),(112,126),(148,141),(143,151),(25,153)], "#161c2e45")
    c.rect(24,149,112,4,"#161c2e45")
    return c


def line2(c, a, b, color=ink):
    c.line(a[0],a[1],b[0],b[1],color)
    c.line(a[0],a[1]+1,b[0],b[1]+1,color)


def window(c, poly_outer, poly_inner):
    c.poly(poly_outer, ink)
    c.poly(poly_inner, gold)
    # Window shine and central muntins are placed separately by caller.

# FRAME 1: 45-degree rotation, front and right side both visible.
f1 = base("turn_45")
# Foundation silhouettes.
f1.poly([(17,83),(65,91),(124,72),(128,130),(79,148),(17,132)], ink)
f1.poly([(23,83),(67,94),(78,102),(78,140),(23,127)], plaster)
f1.poly([(78,102),(120,82),(121,126),(82,141),(78,140)], wood)
# Front gable wall under the roof.
f1.poly([(23,82),(61,41),(79,92),(78,140),(23,127)], ink)
f1.poly([(29,83),(59,50),(73,93),(72,133),(29,122)], plaster_hi)
f1.poly([(34,83),(59,57),(68,94),(67,126),(34,117)], plaster)
# Timber framing on front.
f1.poly([(55,54),(62,55),(64,112),(57,112)], wood_dark)
f1.poly([(27,91),(70,104),(70,111),(27,98)], wood_dark)
f1.poly([(29,117),(69,128),(69,134),(29,123)], roof_dark)
f1.line(33,91,58,58,wood_dark); f1.line(34,92,59,59,wood_dark)
f1.line(66,65,72,93,wood_dark); f1.line(67,65,73,93,wood_dark)
# Door and arched lintel.
f1.poly([(37,99),(55,91),(69,103),(68,135),(38,127)], ink)
f1.poly([(42,102),(55,97),(64,105),(63,132),(42,126)], wood)
f1.poly([(42,102),(55,95),(65,104),(64,111),(55,104),(42,109)], roof_hi)
f1.rect(52,108,4,20,wood_dark)
f1.line(42,113,64,116,ink); f1.line(42,114,64,117,ink)
f1.set(59,121,gold); f1.set(60,121,gold)
# Right side timber braces.
f1.poly([(78,102),(120,82),(121,89),(80,109)], wood_dark)
f1.poly([(79,132),(120,116),(121,123),(80,140)], wood_dark)
f1.poly([(83,105),(89,102),(88,133),(82,137)], roof_dark)
f1.poly([(114,87),(120,84),(120,124),(114,127)], roof_dark)
f1.poly([(86,107),(91,104),(113,122),(109,126)], roof_dark)
f1.poly([(113,91),(117,89),(96,130),(91,133)], roof_mid)
# Side window, clearly on the right-hand wall.
window(f1,[(91,99),(111,91),(112,113),(91,122)],[(96,102),(106,98),(107,111),(96,115)])
f1.poly([(97,103),(101,101),(101,113),(97,115)],glass)
f1.poly([(102,101),(106,99),(107,106),(102,108)],glass_hi)
f1.line(101,100,101,114,ink); f1.line(94,109,109,104,ink)
# Roof: outlined front gable and broad right roof plane.
f1.poly([(14,79),(60,25),(82,86),(72,99),(57,56),(25,91)], ink)
f1.poly([(21,77),(59,32),(75,85),(70,90),(57,48),(27,84)], roof)
f1.poly([(60,25),(111,48),(131,77),(80,96)], ink)
f1.poly([(62,33),(106,52),(123,74),(81,89)], roof)
# Golden roof bands and tile texture.
f1.poly([(24,72),(57,34),(61,43),(30,78)], roof_mid)
f1.poly([(29,76),(58,43),(60,49),(34,79)], roof_hi)
f1.poly([(66,34),(108,53),(112,59),(69,42)], roof_mid)
f1.poly([(72,45),(115,64),(120,72),(77,54)], roof_hi)
f1.poly([(78,58),(116,73),(108,77),(82,66)], roof_mid)
f1.poly([(40,65),(58,44),(61,53),(44,70)], roof_hi)
f1.line(25,83,66,37,roof_dark); f1.line(72,39,116,59,roof_dark)
f1.line(33,85,64,49,roof_mid); f1.line(80,52,120,70,roof_mid)
# Ridge cap and small chimney.
f1.poly([(55,25),(59,18),(66,19),(66,34),(61,42),(56,40)], ink)
f1.poly([(59,23),(63,23),(63,33),(59,38)], roof_mid)
f1.poly([(58,29),(62,27),(62,31),(58,34)], roof_hi)
f1.poly([(57,27),(60,22),(66,25),(111,46),(108,52),(63,34)], roof_dark)
f1.poly([(61,26),(65,29),(106,47),(103,49),(64,33)], roof_mid)
# Eave accents.
line2(f1,(16,80),(72,99)); line2(f1,(79,95),(129,77))
f1.line(25,88,69,101,roof_hi); f1.line(83,91,124,77,roof_mid)
# Sparse facade highlights.
f1.poly([(30,101),(34,102),(34,114),(30,113)],plaster_hi)
f1.poly([(68,113),(72,114),(72,127),(68,126)],plaster_hi)
f1.set(118,101,wood_light); f1.set(119,101,wood_light)

# FRAME 2: 90-degree rotation, only the former right wall is visible.
f2 = base("turn_90")
# Straight-on long side wall, still foreshortened vertically by the elevated pitch.
f2.poly([(24,78),(136,78),(132,139),(28,139)], ink)
f2.poly([(31,84),(129,84),(126,133),(34,133)], wood)
f2.poly([(35,88),(125,88),(122,128),(38,128)], plaster)
# Timber frame on the side wall.
f2.rect(31,82,98,7,wood_dark)
f2.rect(31,127,98,7,wood_dark)
f2.rect(39,84,7,48,roof_dark)
f2.rect(114,84,7,48,roof_dark)
f2.poly([(44,89),(50,89),(75,127),(68,127)],wood_dark)
f2.poly([(110,89),(116,89),(91,127),(84,127)],wood_dark)
f2.rect(77,86,7,45,wood_dark)
# One window, centered on the same right-hand wall.
window(f2,[(61,94),(99,94),(99,121),(61,121)],[(67,99),(93,99),(93,116),(67,116)])
f2.rect(68,100,24,15,gold)
f2.rect(70,101,9,6,glass_hi)
f2.rect(81,101,10,6,glass)
f2.rect(70,109,9,5,glass)
f2.rect(81,109,10,5,roof_hi)
f2.rect(78,98,4,19,ink)
f2.rect(66,106,28,4,ink)
# Side sill and small plaster wear.
f2.rect(58,119,44,5,roof_dark)
f2.rect(63,119,34,2,roof_mid)
f2.poly([(49,95),(55,95),(55,101),(51,101)],plaster_hi)
f2.poly([(104,115),(110,115),(108,124),(102,124)],wood_light)
# High-angle roof: near slope remains broad, proving camera pitch did not flatten.
f2.poly([(17,79),(47,36),(80,18),(113,36),(143,79)],ink)
f2.poly([(25,74),(51,41),(80,25),(109,41),(135,74)],roof)
f2.poly([(31,70),(55,44),(80,31),(105,44),(129,70)],roof_mid)
# Roof tile courses follow the same perspective.
f2.poly([(26,68),(134,68),(129,75),(31,75)],roof_dark)
f2.poly([(34,59),(126,59),(131,65),(29,65)],roof_hi)
f2.poly([(40,51),(120,51),(125,57),(35,57)],roof_dark)
f2.poly([(49,42),(111,42),(117,48),(43,48)],roof_hi)
f2.poly([(61,34),(99,34),(107,40),(53,40)],roof_mid)
f2.line(80,26,80,67,roof_dark)
f2.line(60,39,46,70,roof_dark); f2.line(100,39,114,70,roof_dark)
f2.line(45,51,37,70,roof_hi); f2.line(115,51,123,70,roof_hi)
# Ridge, chimney, and heavy eave.
f2.poly([(52,36),(77,19),(83,19),(108,36),(103,42),(80,27),(57,42)],roof_dark)
f2.poly([(59,36),(80,23),(101,36),(98,39),(80,29),(62,39)],roof_hi)
f2.poly([(99,31),(102,17),(112,17),(114,39),(108,42)],ink)
f2.poly([(103,20),(109,20),(110,35),(104,33)],roof_mid)
f2.rect(20,74,120,8,ink)
f2.rect(27,74,106,4,roof_hi)
# Foundation and grounding strokes.
f2.poly([(29,133),(131,133),(137,142),(23,142)],ink)
f2.rect(35,133,90,5,roof_dark)
f2.rect(43,138,74,4,wood_dark)
f2.set(37,94,plaster_hi); f2.set(122,100,wood_light)

finish([f1, f2])
view(f1, scale=3, margin=2, edges="all")
view(f2, scale=3, margin=2, edges="all")
