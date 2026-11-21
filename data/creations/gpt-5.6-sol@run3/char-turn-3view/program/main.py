# Three directional views of the supplied character, using only its palette.
# Palette indices are inherited from input_canvas.
K0, K1, K2, K3, K4, K5 = 1, 2, 3, 4, 5, 6
SKIN, SKIN_SH = 7, 8
DARK, ROSE, CYAN, WHITE = 9, 10, 11, 12
BLUE, NAVY, PEACH, GREY = 13, 14, 15, 16
LITE, PURE, ICE, MID = 17, 18, 19, 20
BLUSH, INK, PLUM = 21, 22, 23


def blank(name):
    c = input_canvas.copy(name=name)
    c.clear()
    return c


def hair_texture(c, flip=False):
    # Angular highlight clusters preserve the source's chunky brown hair rendering.
    blocks = [
        (10, 13, 8, 5, K2), (18, 7, 10, 7, K2), (28, 8, 9, 5, K2),
        (38, 9, 10, 8, K1), (49, 15, 7, 10, K3), (7, 23, 8, 9, K3),
        (15, 20, 11, 7, K4), (26, 17, 12, 7, K3), (40, 20, 10, 8, K2),
        (53, 27, 8, 7, K4), (5, 35, 7, 9, K4), (13, 31, 8, 7, K2),
        (23, 28, 12, 6, K1), (45, 31, 9, 7, K4), (55, 39, 8, 5, K5),
    ]
    for x, y, w, h, col in blocks:
        if flip:
            x = 66 - x - w
        c.rect(x, y, w, h, col)


def draw_three_quarter(c):
    # Back hair and crown, weighted to the far (left) side as the face turns right.
    c.poly([(3,42),(5,23),(11,12),(22,4),(43,4),(55,12),(62,25),(65,42),
            (61,52),(51,57),(37,58),(20,56),(9,51)], K0)
    c.rect(8,17,49,30,K1)
    c.poly([(8,16),(16,7),(37,4),(52,11),(60,23),(57,36),(48,31),(40,23),
            (26,21),(18,30),(10,35)], K2)
    hair_texture(c)
    # Side locks behind the jaw.
    c.poly([(8,39),(17,42),(20,57),(17,66),(10,60),(6,48)], K1)
    c.poly([(13,45),(22,48),(25,64),(19,69),(13,60)], K3)
    c.poly([(48,37),(58,39),(61,55),(55,67),(48,59)], K1)
    c.rect(52,45,7,13,K3)

    # Turned face: broad cheek at left, profile and nose projecting right.
    c.poly([(21,28),(42,25),(53,30),(55,38),(61,42),(57,46),(55,55),
            (49,63),(37,68),(25,64),(18,55),(17,40)], SKIN)
    c.rect(21,31,8,8,SKIN_SH)
    c.rect(26,56,9,6,SKIN_SH)
    c.rect(35,63,13,4,PEACH)
    c.rect(49,48,7,8,PEACH)
    c.set(58,43,SKIN_SH); c.set(59,44,SKIN_SH)
    # Bangs sweep across the far temple and crown.
    c.poly([(10,23),(19,17),(35,16),(48,21),(52,28),(43,27),(37,32),
            (30,28),(25,36),(18,34),(17,41),(10,37)], K0)
    c.rect(14,23,12,7,K2)
    c.rect(25,18,12,7,K3)
    c.rect(38,20,9,6,K2)
    c.rect(17,34,8,6,K4)

    # Far eye and prominent near eye, using the original cyan/blue/white colors.
    c.rect(25,39,5,3,DARK)
    c.rect(26,42,5,7,WHITE)
    c.rect(28,44,4,7,BLUE)
    c.rect(39,35,12,4,DARK)
    c.rect(41,39,11,13,WHITE)
    c.rect(45,41,7,12,CYAN)
    c.rect(48,42,4,10,BLUE)
    c.rect(49,42,3,4,ICE)
    c.rect(41,51,11,3,DARK)
    c.set(53,47,INK)
    # Brow, nose, mouth and cheek colors.
    c.rect(39,32,10,3,K1)
    c.rect(54,42,4,3,SKIN_SH)
    c.rect(50,58,6,2,ROSE)
    c.rect(45,60,7,2,BLUSH)
    c.rect(23,51,5,4,PEACH)

    # Neck and the turned shoulders.
    c.rect(31,64,17,13,PEACH)
    c.rect(35,65,13,9,SKIN_SH)
    c.poly([(15,69),(28,65),(34,72),(49,68),(59,75),(58,92),(10,92)], GREY)
    # Far puff sleeve.
    c.poly([(14,69),(7,73),(4,85),(9,91),(19,87),(23,75)], MID)
    c.poly([(9,73),(5,79),(5,86),(11,87),(15,78)], LITE)
    c.rect(5,80,5,8,ICE)
    # Near puff sleeve.
    c.poly([(49,69),(59,72),(65,82),(63,91),(52,91),(45,77)], GREY)
    c.poly([(53,72),(62,77),(65,84),(60,88),(52,82)], LITE)
    c.rect(59,77,5,8,ICE)

    # White bib and collar, offset with the torso rotation.
    c.poly([(25,66),(33,72),(40,74),(49,67),(53,71),(47,80),(54,87),
            (43,88),(35,82),(27,88),(20,83)], ICE)
    c.poly([(29,67),(34,73),(40,74),(46,68),(48,74),(41,80),(34,78),(27,73)], PURE)
    c.rect(31,78,8,8,WHITE)
    c.rect(39,80,8,6,ICE)
    # Bodice seams and waist.
    c.poly([(18,82),(29,84),(35,91),(42,84),(54,84),(57,101),(16,101)], GREY)
    c.rect(24,85,6,13,MID)
    c.rect(44,87,6,12,MID)
    c.rect(31,91,7,10,LITE)
    c.rect(12,98,47,7,MID)
    c.rect(19,98,33,5,NAVY)
    c.rect(29,98,18,5,GREY)

    # Arms and hands: near hand is larger and shifted forward.
    c.poly([(7,84),(14,83),(17,91),(15,101),(11,111),(5,109),(2,100)], SKIN_SH)
    c.poly([(5,91),(13,88),(16,96),(12,101),(14,107),(9,113),(3,108),(1,99)], SKIN)
    c.rect(2,99,6,8,BLUSH)
    c.poly([(57,84),(64,87),(65,97),(65,108),(60,114),(54,110),(53,101)], SKIN_SH)
    c.poly([(56,88),(63,89),(65,98),(63,103),(65,109),(60,114),(54,109),(55,101)], SKIN)
    c.rect(60,98,6,9,BLUSH)

    # Flared dress and apron panels.
    c.poly([(13,101),(57,101),(63,115),(61,118),(6,118),(7,110)], GREY)
    c.poly([(17,101),(26,101),(24,118),(10,118)], MID)
    c.poly([(27,101),(39,101),(43,118),(22,118)], LITE)
    c.poly([(33,102),(42,102),(48,118),(39,118)], ICE)
    c.poly([(45,101),(54,101),(60,118),(49,118)], MID)
    c.poly([(12,105),(18,102),(15,117),(8,117)], ICE)
    c.rect(29,105,6,13,PURE)
    c.rect(41,107,5,11,WHITE)
    c.rect(55,108,5,10,LITE)
    c.line(22,104,20,117,NAVY)
    c.line(49,103,52,117,NAVY)


def draw_rear(c):
    # Full back of the same coiffure.
    c.poly([(3,42),(5,23),(12,11),(24,3),(42,3),(55,11),(62,24),(65,43),
            (61,55),(52,64),(14,64),(5,53)], K0)
    c.rect(7,19,52,31,K1)
    c.poly([(8,20),(15,10),(29,5),(44,7),(56,17),(61,31),(56,45),(47,54),
            (18,54),(8,43)], K2)
    hair_texture(c)
    c.rect(5,37,10,14,K3); c.rect(51,35,11,15,K3)
    c.rect(13,47,13,12,K1); c.rect(39,46,15,13,K1)
    c.poly([(18,18),(28,10),(43,12),(54,22),(48,29),(37,25),(28,30),(15,27)], K3)
    c.rect(22,10,10,6,K4); c.rect(41,14,8,7,K4)
    c.rect(9,30,7,8,K4); c.rect(50,27,8,9,K5)
    # Long lower locks and small neck visible beneath the hair.
    c.poly([(9,46),(20,51),(23,70),(16,75),(9,65)], K1)
    c.poly([(46,49),(57,45),(59,65),(52,76),(44,69)], K1)
    c.rect(26,57,15,15,PEACH)
    c.rect(29,59,12,12,SKIN_SH)

    # Shoulders and sleeves from behind.
    c.poly([(15,67),(27,63),(34,69),(42,63),(55,68),(60,83),(55,96),(11,96),(6,82)], GREY)
    c.poly([(13,68),(6,73),(3,84),(8,91),(19,86),(23,72)], MID)
    c.poly([(8,72),(4,79),(6,87),(14,86),(17,77)], LITE)
    c.rect(5,78,5,8,ICE)
    c.poly([(51,68),(60,72),(64,82),(61,91),(51,88),(44,73)], MID)
    c.poly([(56,73),(62,78),(62,86),(55,87),(50,77)], LITE)
    c.rect(60,79,5,7,ICE)

    # Rear white collar and apron straps.
    c.poly([(22,64),(29,70),(34,74),(40,70),(45,64),(50,69),(42,80),(34,83),
            (25,79),(17,69)], ICE)
    c.poly([(24,64),(30,70),(34,73),(39,69),(43,64),(45,69),(39,77),(34,79),
            (28,76),(20,69)], PURE)
    c.poly([(22,75),(29,78),(33,96),(25,97)], WHITE)
    c.poly([(40,77),(47,74),(50,96),(42,97)], ICE)
    # Back bodice panels.
    c.poly([(17,79),(25,78),(29,97),(12,101)], GREY)
    c.poly([(47,77),(55,80),(59,101),(43,97)], GREY)
    c.rect(29,81,12,16,MID)
    c.rect(32,83,5,14,NAVY)
    # Apron bow centered at the back waist.
    c.poly([(33,91),(25,86),(20,89),(24,97),(33,100)], ICE)
    c.poly([(36,91),(44,86),(49,90),(45,98),(36,100)], WHITE)
    c.rect(31,91,8,9,PURE)
    c.poly([(29,98),(34,97),(31,108),(25,112)], ICE)
    c.poly([(37,97),(42,99),(47,112),(39,108)], WHITE)
    c.rect(10,96,49,7,MID)
    c.rect(18,97,32,5,NAVY)
    c.rect(25,97,17,5,GREY)

    # Rear arms and hands.
    c.poly([(7,84),(14,83),(17,92),(14,102),(13,111),(6,113),(2,106),(3,96)], SKIN_SH)
    c.poly([(5,91),(12,88),(15,96),(12,102),(14,108),(9,114),(3,110),(1,101)], SKIN)
    c.rect(2,100,6,8,BLUSH)
    c.poly([(53,85),(61,84),(64,95),(63,104),(65,109),(60,114),(53,110),(51,98)], SKIN_SH)
    c.poly([(55,90),(62,89),(65,100),(62,104),(64,110),(59,114),(53,108),(54,99)], SKIN)
    c.rect(60,100,6,8,BLUSH)

    # Same skirt construction viewed from behind.
    c.poly([(11,101),(57,101),(63,116),(61,118),(6,118),(6,113)], GREY)
    c.poly([(15,101),(25,101),(23,118),(9,118)], MID)
    c.poly([(25,101),(34,102),(36,118),(21,118)], LITE)
    c.poly([(34,102),(43,101),(48,118),(35,118)], ICE)
    c.poly([(44,101),(54,101),(60,118),(48,118)], MID)
    c.rect(12,107,5,11,ICE)
    c.rect(28,106,6,12,PURE)
    c.rect(40,106,5,12,WHITE)
    c.rect(54,108,5,10,LITE)
    c.line(21,103,19,117,NAVY)
    c.line(49,103,52,117,NAVY)


f1 = blank("left_three_quarter")
draw_three_quarter(f1)
f2 = f1.copy(name="right_three_quarter")
f2.mirror("h")
f3 = blank("rear_view")
draw_rear(f3)

view(f1, scale=4, margin=2, edges="all")
view(f2, scale=4, margin=2, edges="all")
view(f3, scale=4, margin=2, edges="all")
finish([f1, f2, f3])
