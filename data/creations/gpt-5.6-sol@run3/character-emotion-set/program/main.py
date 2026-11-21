from pixelbench_api import new_canvas, view, finish

W, H = 64, 64
c = new_canvas(W, H, background=None, name="character_emotions")

# Compact shared palette.
OUT = "#172033"
HAIR_D = "#17606b"
HAIR = "#218997"
HAIR_HI = "#43b0b0"
SKIN_D = "#c96f55"
SKIN = "#f0a078"
SKIN_HI = "#ffc09a"
WHITE = "#fff4de"
HOOD_D = "#9f3f3b"
HOOD = "#d95b45"
HOOD_HI = "#ef7a52"
MOUTH = "#7b2d3e"
TONGUE = "#e66f78"


def px(x, y, color):
    c.set(x, y, color)


def draw_portrait(ox, oy, mood):
    X = lambda x: ox + x
    Y = lambda y: oy + y

    # Hoodie and shoulders, behind the head.
    c.poly([(X(2),Y(31)),(X(3),Y(28)),(X(8),Y(25)),(X(12),Y(24)),
            (X(20),Y(24)),(X(24),Y(26)),(X(29),Y(29)),(X(29),Y(31))], OUT)
    c.poly([(X(4),Y(31)),(X(5),Y(29)),(X(11),Y(26)),(X(21),Y(26)),
            (X(27),Y(29)),(X(28),Y(31))], HOOD)
    c.rect(X(8), Y(29), 16, 3, HOOD_D)
    c.poly([(X(8),Y(27)),(X(12),Y(25)),(X(16),Y(29)),(X(20),Y(25)),
            (X(24),Y(27)),(X(22),Y(31)),(X(10),Y(31))], HOOD)
    c.line(X(7),Y(30),X(10),Y(27),HOOD_HI)
    c.line(X(25),Y(30),X(22),Y(27),HOOD_D)
    px(X(13),Y(29),OUT); px(X(19),Y(29),OUT)

    # Neck.
    c.rect(X(12),Y(22),8,6,OUT)
    c.rect(X(13),Y(22),6,5,SKIN_D)
    c.rect(X(14),Y(22),5,3,SKIN)

    # Shared bob silhouette.
    c.poly([(X(9),Y(3)),(X(21),Y(3)),(X(25),Y(6)),(X(27),Y(11)),
            (X(27),Y(20)),(X(25),Y(25)),(X(21),Y(28)),(X(10),Y(28)),
            (X(6),Y(25)),(X(4),Y(20)),(X(4),Y(11)),(X(6),Y(6))], OUT)
    c.poly([(X(10),Y(4)),(X(21),Y(4)),(X(24),Y(7)),(X(26),Y(12)),
            (X(25),Y(22)),(X(22),Y(26)),(X(19),Y(27)),(X(8),Y(25)),
            (X(5),Y(20)),(X(5),Y(11)),(X(7),Y(7))], HAIR_D)
    c.poly([(X(10),Y(5)),(X(20),Y(5)),(X(23),Y(7)),(X(25),Y(12)),
            (X(24),Y(20)),(X(22),Y(23)),(X(20),Y(22)),(X(9),Y(23)),
            (X(7),Y(20)),(X(6),Y(11)),(X(8),Y(7))], HAIR)
    c.line(X(9),Y(6),X(7),Y(13),HAIR_HI)
    c.line(X(11),Y(5),X(18),Y(5),HAIR_HI)
    px(X(8),Y(8),HAIR_HI); px(X(24),Y(11),HAIR_D)

    # Ears and face, outlined in the same geometry for every portrait.
    c.rect(X(5),Y(14),4,7,OUT)
    c.rect(X(23),Y(14),4,7,OUT)
    c.rect(X(6),Y(15),3,5,SKIN_D)
    c.rect(X(23),Y(15),3,5,SKIN_D)
    px(X(6),Y(17),SKIN); px(X(25),Y(17),SKIN)
    c.poly([(X(9),Y(8)),(X(22),Y(8)),(X(24),Y(12)),(X(24),Y(20)),
            (X(21),Y(24)),(X(17),Y(26)),(X(13),Y(25)),(X(9),Y(22)),
            (X(7),Y(18)),(X(8),Y(11))], OUT)
    c.poly([(X(10),Y(9)),(X(21),Y(9)),(X(23),Y(12)),(X(23),Y(19)),
            (X(20),Y(23)),(X(17),Y(25)),(X(13),Y(24)),(X(9),Y(21)),
            (X(8),Y(17)),(X(9),Y(11))], SKIN)
    c.rect(X(9),Y(12),2,7,SKIN_HI)
    px(X(10),Y(21),SKIN_HI); px(X(21),Y(21),SKIN_D)

    # Chunky asymmetric fringe, always identical.
    c.poly([(X(8),Y(7)),(X(22),Y(7)),(X(23),Y(11)),(X(20),Y(10)),
            (X(20),Y(13)),(X(17),Y(11)),(X(15),Y(14)),(X(13),Y(10)),
            (X(9),Y(12)),(X(8),Y(10))], OUT)
    c.poly([(X(9),Y(7)),(X(21),Y(7)),(X(22),Y(9)),(X(19),Y(9)),
            (X(19),Y(11)),(X(17),Y(9)),(X(15),Y(12)),(X(13),Y(9)),
            (X(9),Y(11))], HAIR)
    c.line(X(10),Y(8),X(16),Y(8),HAIR_HI)

    # Emotion-specific features.
    if mood == "calm":
        c.line(X(10),Y(15),X(13),Y(15),OUT)
        c.line(X(18),Y(15),X(21),Y(15),OUT)
        px(X(11),Y(16),SKIN_D); px(X(20),Y(16),SKIN_D)
        c.line(X(14),Y(21),X(18),Y(21),MOUTH)
        px(X(15),Y(22),SKIN_D); px(X(17),Y(22),SKIN_D)
    elif mood == "smile":
        c.line(X(10),Y(16),X(12),Y(14),OUT); c.line(X(12),Y(14),X(14),Y(16),OUT)
        c.line(X(18),Y(16),X(20),Y(14),OUT); c.line(X(20),Y(14),X(22),Y(16),OUT)
        px(X(10),Y(19),SKIN_D); px(X(21),Y(19),SKIN_D)
        c.poly([(X(12),Y(20)),(X(20),Y(20)),(X(18),Y(24)),(X(14),Y(24))], OUT)
        c.rect(X(13),Y(20),6,1,WHITE)
        c.rect(X(14),Y(22),4,1,TONGUE)
    elif mood == "angry":
        c.line(X(9),Y(14),X(14),Y(16),OUT)
        c.line(X(18),Y(16),X(23),Y(14),OUT)
        c.rect(X(10),Y(17),4,2,WHITE); c.rect(X(18),Y(17),4,2,WHITE)
        px(X(12),Y(17),OUT); px(X(19),Y(17),OUT)
        c.poly([(X(12),Y(23)),(X(14),Y(20)),(X(19),Y(20)),(X(21),Y(23)),
                (X(19),Y(24)),(X(14),Y(24))], OUT)
        c.rect(X(14),Y(21),5,1,WHITE)
        px(X(9),Y(20),SKIN_D); px(X(22),Y(20),SKIN_D)
    elif mood == "surprised":
        c.line(X(10),Y(13),X(14),Y(12),OUT)
        c.line(X(18),Y(12),X(22),Y(13),OUT)
        c.rect(X(10),Y(15),4,4,OUT); c.rect(X(18),Y(15),4,4,OUT)
        c.rect(X(11),Y(16),2,2,WHITE); c.rect(X(19),Y(16),2,2,WHITE)
        px(X(12),Y(17),OUT); px(X(19),Y(17),OUT)
        c.rect(X(14),Y(21),5,4,OUT)
        c.rect(X(15),Y(22),3,2,MOUTH)
        px(X(9),Y(20),SKIN_D); px(X(22),Y(20),SKIN_D)


# Reading order: calm, smiling, angry, surprised.
draw_portrait(0, 0, "calm")
draw_portrait(32, 0, "smile")
draw_portrait(0, 32, "angry")
draw_portrait(32, 32, "surprised")

view(c, scale=8, margin=0)
finish(c)
