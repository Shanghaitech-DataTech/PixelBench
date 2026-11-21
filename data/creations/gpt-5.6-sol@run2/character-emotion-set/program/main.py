from pixelbench_api import new_canvas, view, finish

result = new_canvas(64, 64, background=None, name="character_emotions")

OUT = "#171827"
HAIR_D = "#203044"
HAIR = "#2d4b63"
HAIR_HI = "#47728a"
SKIN_D = "#c97969"
SKIN = "#f0a889"
SKIN_HI = "#ffc0a0"
WHITE = "#fff4e8"
EYE = "#342535"
JACKET_D = "#8f3548"
JACKET = "#cf4d5d"
JACKET_HI = "#ec6b70"
COLLAR = "#f3dfbd"


def px(x, y, colour, ox, oy):
    result.set(ox + x, oy + y, colour)


def rect(x, y, w, h, colour, ox, oy):
    result.rect(ox + x, oy + y, w, h, colour)


def poly(points, colour, ox, oy):
    result.poly([(ox + x, oy + y) for x, y in points], colour)


def line(x0, y0, x1, y1, colour, ox, oy):
    result.line(ox + x0, oy + y0, ox + x1, oy + y1, colour)


def portrait(ox, oy, mood):
    # Shoulders, jacket and collar.
    poly([(3,31),(4,28),(8,26),(12,25),(20,25),(24,26),(28,29),(29,31)], OUT, ox, oy)
    poly([(5,31),(6,28),(11,26),(21,26),(26,28),(27,31)], JACKET, ox, oy)
    rect(6,29,2,3,JACKET_HI,ox,oy)
    rect(24,29,2,3,JACKET_D,ox,oy)
    poly([(11,25),(16,30),(21,25),(20,31),(12,31)], COLLAR, ox, oy)
    poly([(14,24),(18,24),(19,27),(16,29),(13,27)], OUT, ox, oy)
    poly([(15,23),(17,23),(18,26),(16,27),(14,26)], SKIN, ox, oy)
    line(16,28,16,31,JACKET_D,ox,oy)

    # Bob haircut silhouette behind the face.
    poly([(6,12),(7,8),(10,5),(13,3),(20,3),(24,6),(26,10),(27,17),
          (26,23),(23,26),(9,26),(6,23),(5,18)], OUT, ox, oy)
    poly([(7,12),(8,8),(12,5),(19,4),(23,7),(25,11),(25,20),
          (23,24),(9,24),(7,21)], HAIR_D, ox, oy)
    rect(7,15,3,7,HAIR,ox,oy)
    rect(23,13,2,8,HAIR,ox,oy)

    # Ears and large face.
    rect(7,13,4,7,OUT,ox,oy)
    rect(8,14,3,5,SKIN_D,ox,oy)
    rect(22,13,4,7,OUT,ox,oy)
    rect(22,14,3,5,SKIN_D,ox,oy)
    px(8,16,SKIN_HI,ox,oy); px(24,16,SKIN_HI,ox,oy)
    poly([(9,9),(12,6),(20,6),(23,9),(24,14),(23,20),(20,24),
          (16,26),(12,24),(9,20),(8,14)], OUT, ox, oy)
    poly([(10,10),(12,7),(20,7),(22,10),(23,14),(22,20),(19,23),
          (16,24),(13,23),(10,20),(9,14)], SKIN, ox, oy)
    rect(10,11,1,7,SKIN_HI,ox,oy)
    px(11,20,SKIN_HI,ox,oy); px(21,20,SKIN_D,ox,oy)

    # Identical fringe and side locks establish the character.
    poly([(8,11),(9,7),(13,4),(20,4),(24,8),(24,11),(21,10),(20,8),
          (18,10),(16,7),(14,10),(11,9),(10,12)], OUT, ox, oy)
    poly([(9,10),(10,7),(13,5),(19,5),(23,8),(23,9),(20,8),(18,9),
          (16,6),(14,9),(11,8),(10,11)], HAIR, ox, oy)
    line(12,6,15,5,HAIR_HI,ox,oy)
    line(10,12,10,20,OUT,ox,oy); line(22,11,22,20,OUT,ox,oy)
    line(11,12,11,18,HAIR_D,ox,oy); line(21,11,21,18,HAIR_D,ox,oy)

    # Nose remains fixed across the set.
    px(16,17,SKIN_D,ox,oy); px(17,18,SKIN_D,ox,oy)

    if mood == "calm":
        line(12,13,14,13,HAIR_D,ox,oy); line(19,13,21,13,HAIR_D,ox,oy)
        rect(12,15,3,2,WHITE,ox,oy); rect(19,15,3,2,WHITE,ox,oy)
        px(13,15,EYE,ox,oy); px(20,15,EYE,ox,oy)
        line(14,21,18,21,EYE,ox,oy)
        px(13,22,SKIN_HI,ox,oy); px(20,22,SKIN_D,ox,oy)
    elif mood == "smile":
        line(12,13,14,13,HAIR_D,ox,oy); line(19,13,21,13,HAIR_D,ox,oy)
        line(12,16,13,15,EYE,ox,oy); line(13,15,15,16,EYE,ox,oy)
        line(19,16,20,15,EYE,ox,oy); line(20,15,22,16,EYE,ox,oy)
        px(11,19,"#e67f7b",ox,oy); px(21,19,"#e67f7b",ox,oy)
        line(13,20,14,22,EYE,ox,oy); line(14,22,18,23,EYE,ox,oy)
        line(18,23,20,20,EYE,ox,oy)
        line(14,21,19,21,WHITE,ox,oy)
    elif mood == "angry":
        line(12,13,15,14,OUT,ox,oy); line(18,14,21,13,OUT,ox,oy)
        line(12,16,15,16,EYE,ox,oy); line(19,16,22,16,EYE,ox,oy)
        px(14,16,WHITE,ox,oy); px(19,16,WHITE,ox,oy)
        line(13,22,15,20,EYE,ox,oy); line(15,20,18,20,EYE,ox,oy)
        line(18,20,20,22,EYE,ox,oy)
        px(11,19,SKIN_D,ox,oy); px(21,19,SKIN_D,ox,oy)
    else:  # surprised
        line(12,12,14,11,HAIR_D,ox,oy); line(19,11,21,12,HAIR_D,ox,oy)
        rect(12,14,3,4,OUT,ox,oy); rect(19,14,3,4,OUT,ox,oy)
        rect(13,15,1,2,WHITE,ox,oy); rect(20,15,1,2,WHITE,ox,oy)
        px(13,16,EYE,ox,oy); px(20,16,EYE,ox,oy)
        rect(14,20,5,4,OUT,ox,oy); rect(15,21,3,2,"#9e3f50",ox,oy)
        px(11,20,SKIN_HI,ox,oy); px(21,20,SKIN_D,ox,oy)


portrait(0, 0, "calm")
portrait(32, 0, "smile")
portrait(0, 32, "angry")
portrait(32, 32, "surprised")

view(result, scale=8, margin=0)
finish(result)
