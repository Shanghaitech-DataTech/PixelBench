from pixelbench_api import *

W, H = 112, 157
ink = '#161c2e'
ink_soft = '#2b2b35'
wood_dark = '#6c513a'
wood = '#97763d'
wood_light = '#bda759'
plaster_shadow = '#bbae93'
plaster = '#e1dca3'
plaster_hi = '#f2edbd'
roof_dark = '#98694e'
roof = '#dcaa46'
roof_hi = '#f9e279'
window = '#7cbbbd'
window_hi = '#d4f0d4'
shadow = '#161c2e45'


def poly(c, pts, col):
    c.poly(pts, col)


def line(c, pts, col):
    for a, b in zip(pts, pts[1:]):
        c.line(a[0], a[1], b[0], b[1], col)


def draw_frame_45():
    c = new_canvas(W, H, name='turn_45')
    # Grounding shadow.
    poly(c, [(10,137),(29,128),(76,130),(105,143),(96,150),(24,150)], shadow)

    # Front and right walls, outlined as two distinct yawed planes.
    poly(c, [(15,72),(65,83),(65,140),(15,130)], ink)
    poly(c, [(20,78),(60,87),(60,134),(20,126)], plaster_shadow)
    poly(c, [(23,80),(58,88),(58,131),(23,124)], plaster)

    poly(c, [(65,83),(101,65),(101,121),(65,140)], ink)
    poly(c, [(70,87),(96,74),(96,117),(70,132)], wood_dark)
    poly(c, [(73,89),(94,78),(94,114),(73,127)], wood)

    # Heavy timber framing on the front plane.
    poly(c, [(18,78),(24,80),(24,126),(18,130)], wood_dark)
    poly(c, [(56,86),(62,84),(62,136),(56,133)], wood_dark)
    poly(c, [(20,101),(59,108),(59,114),(20,107)], wood_dark)
    line(c, [(21,82),(57,129)], wood_dark)
    line(c, [(24,81),(60,124)], wood)

    # Front door with inset golden panels.
    poly(c, [(30,102),(50,106),(50,132),(30,129)], ink)
    poly(c, [(34,107),(47,109),(47,128),(34,126)], roof_dark)
    poly(c, [(36,110),(45,111),(45,118),(36,117)], roof)
    poly(c, [(36,121),(45,122),(45,126),(36,125)], wood_light)
    c.set(44,120,roof_hi)

    # Side timbers and a single window on the right-hand wall.
    poly(c, [(68,86),(73,84),(73,130),(68,134)], ink)
    poly(c, [(93,72),(98,69),(98,118),(93,121)], ink)
    poly(c, [(71,110),(96,97),(96,103),(71,116)], ink)
    line(c, [(72,91),(95,113)], wood_dark)
    poly(c, [(78,86),(91,79),(91,98),(78,105)], ink)
    poly(c, [(81,88),(88,84),(88,95),(81,99)], window)
    line(c, [(84,86),(84,98)], ink)
    line(c, [(80,94),(89,89)], ink)
    c.set(82,89,window_hi)
    c.set(83,89,window_hi)

    # Front gable, then the high visible roof plane running away to the right.
    poly(c, [(8,75),(40,26),(70,83),(65,91),(38,43),(15,82)], ink)
    poly(c, [(16,71),(40,34),(63,80),(39,67)], roof_dark)
    poly(c, [(20,69),(40,39),(58,76),(39,63)], roof)
    poly(c, [(40,26),(75,12),(108,61),(101,73),(69,84)], ink)
    poly(c, [(43,31),(74,18),(101,61),(96,66),(69,77)], roof_dark)
    poly(c, [(48,32),(73,22),(95,58),(91,61),(68,71)], roof)

    # Roof slats/highlights reinforce the unchanged elevated pitch.
    line(c, [(17,72),(40,37),(62,80)], wood_light)
    line(c, [(23,72),(40,45),(57,77)], roof_hi)
    line(c, [(31,66),(41,50),(51,72)], wood_light)
    line(c, [(50,34),(72,25),(94,61)], wood_light)
    line(c, [(57,35),(73,29),(88,56)], roof_hi)
    line(c, [(67,31),(77,30),(94,57)], wood_light)
    poly(c, [(37,24),(42,24),(78,10),(76,17),(43,32)], ink)
    poly(c, [(42,26),(73,14),(73,19),(44,32)], wood_light)

    # Eaves and a few plaster chips.
    line(c, [(9,76),(65,90),(102,72)], ink)
    line(c, [(13,78),(64,92),(99,76)], wood_light)
    c.rect(27,91,5,2,plaster_hi); c.rect(46,96,6,2,plaster_hi)
    c.rect(25,117,4,2,plaster_hi)
    return c


def draw_frame_90():
    c = new_canvas(W, H, name='turn_90')
    poly(c, [(7,139),(22,130),(91,130),(107,140),(99,149),(17,149)], shadow)

    # Only the right-hand wall is visible at this yaw.
    poly(c, [(13,68),(100,68),(100,134),(13,134)], ink)
    poly(c, [(19,76),(94,76),(94,129),(19,129)], wood_dark)
    poly(c, [(24,79),(89,79),(89,125),(24,125)], wood)

    # Timber skeleton across the long side wall.
    poly(c, [(18,74),(25,74),(25,131),(18,131)], ink)
    poly(c, [(88,74),(95,74),(95,131),(88,131)], ink)
    poly(c, [(52,75),(60,75),(60,129),(52,129)], wood_dark)
    poly(c, [(20,103),(93,103),(93,111),(20,111)], ink)
    line(c, [(23,78),(54,104),(88,79)], wood_dark)
    line(c, [(23,126),(54,110),(90,127)], wood_dark)
    line(c, [(26,80),(54,102)], wood_light)
    line(c, [(61,101),(86,81)], wood_light)

    # The same side window, now broad and centered in the only wall face.
    poly(c, [(63,83),(84,83),(84,101),(63,101)], ink)
    poly(c, [(67,87),(80,87),(80,97),(67,97)], window)
    c.rect(72,87,3,10,ink)
    c.rect(67,91,13,3,ink)
    c.rect(68,88,4,3,window_hi)
    c.rect(76,94,3,2,'#9fd7c8')

    # High-angle roof: broad near plane remains visible at the same pitch.
    poly(c, [(5,69),(34,24),(78,24),(107,69),(99,79),(13,79)], ink)
    poly(c, [(13,66),(37,31),(76,31),(99,66),(94,72),(18,72)], roof_dark)
    poly(c, [(20,64),(40,36),(73,36),(92,64),(88,68),(24,68)], roof)
    # A narrow far roof plane is visible beyond the ridge, proving the camera stays elevated.
    poly(c, [(34,24),(45,13),(68,13),(78,24)], ink)
    poly(c, [(40,24),(47,18),(66,18),(72,24)], wood_light)
    line(c, [(34,25),(78,25)], ink)
    line(c, [(18,66),(39,34)], wood_light)
    line(c, [(29,67),(44,38)], roof_hi)
    line(c, [(42,68),(49,37)], wood_light)
    line(c, [(57,68),(57,36)], roof_hi)
    line(c, [(71,68),(65,37)], wood_light)
    line(c, [(85,67),(70,36)], roof_hi)
    line(c, [(8,70),(104,70)], ink)
    line(c, [(13,74),(99,74)], wood_light)

    # Wall wear and lower sill detail, with no front-door cues.
    c.rect(30,88,5,2,'#c99a4a'); c.rect(35,118,6,2,wood_light)
    c.rect(72,117,7,2,wood_light); c.rect(27,124,4,2,roof_dark)
    poly(c, [(20,129),(94,129),(94,136),(20,136)], ink)
    poly(c, [(25,129),(89,129),(89,133),(25,133)], wood_light)
    return c

f1 = draw_frame_45()
f2 = draw_frame_90()
view(f1, size=420, margin=0)
view(f2, size=420, margin=0)
finish([f1, f2])
