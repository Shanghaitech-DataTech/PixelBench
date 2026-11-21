from pixelbench_api import new_canvas, view, finish

# Four-panel expression sheet on a transparent canvas.
c = new_canvas(64, 64, background=None, name="character_emotion_set")

# Compact, high-contrast palette.
OUT = "#211c33"
HAIR_D = "#302753"
HAIR = "#51427a"
HAIR_H = "#7864a3"
SKIN_D = "#c77468"
SKIN = "#f0aa86"
SKIN_H = "#ffd0a4"
WHITE = "#fff3df"
EYE = "#302b43"
TEAL_D = "#164b55"
TEAL = "#247582"
TEAL_H = "#43a2a2"
MOUTH = "#7d3346"
TONGUE = "#ed7180"


def px(x, y, colour):
    c.set(x, y, colour)


def portrait(ox, oy, mood):
    # Hair mass and dark silhouette, identical in every panel.
    c.rect(ox+7, oy+2, 16, 2, OUT)
    c.rect(ox+4, oy+4, 22, 3, OUT)
    c.rect(ox+2, oy+7, 26, 12, OUT)
    c.rect(ox+3, oy+19, 24, 4, OUT)
    c.rect(ox+5, oy+23, 20, 3, OUT)
    c.rect(ox+7, oy+4, 16, 2, HAIR_D)
    c.rect(ox+5, oy+6, 20, 4, HAIR)
    c.rect(ox+4, oy+10, 4, 10, HAIR)
    c.rect(ox+23, oy+10, 3, 11, HAIR_D)
    c.rect(ox+7, oy+7, 16, 4, HAIR_H)
    c.rect(ox+5, oy+8, 3, 3, HAIR_H)
    c.rect(ox+8, oy+5, 9, 1, HAIR_H)

    # Ears, face, jaw and neck.
    c.rect(ox+1, oy+13, 4, 7, OUT)
    c.rect(ox+26, oy+13, 4, 7, OUT)
    c.rect(ox+2, oy+14, 3, 5, SKIN_D)
    c.rect(ox+26, oy+14, 3, 5, SKIN_D)
    c.rect(ox+5, oy+9, 21, 12, OUT)
    c.rect(ox+7, oy+8, 17, 15, SKIN)
    c.rect(ox+6, oy+11, 19, 9, SKIN)
    c.rect(ox+8, oy+20, 15, 4, SKIN)
    c.rect(ox+10, oy+23, 11, 2, OUT)
    c.rect(ox+12, oy+22, 7, 4, SKIN_D)
    # Consistent hair fringe.
    c.rect(ox+6, oy+8, 5, 3, HAIR)
    c.rect(ox+8, oy+10, 3, 2, HAIR)
    c.rect(ox+20, oy+8, 5, 3, HAIR_D)
    c.rect(ox+20, oy+10, 3, 2, HAIR_D)
    px(ox+12, oy+9, HAIR_H)
    # Face light and nose.
    c.rect(ox+9, oy+12, 2, 2, SKIN_H)
    px(ox+16, oy+17, SKIN_D)
    px(ox+17, oy+18, SKIN_H)

    # Outfit and shoulders, identical in all panels.
    c.rect(ox+6, oy+25, 19, 2, OUT)
    c.rect(ox+3, oy+27, 25, 3, OUT)
    c.rect(ox+7, oy+25, 6, 2, TEAL)
    c.rect(ox+18, oy+25, 6, 2, TEAL)
    c.rect(ox+4, oy+28, 24, 2, TEAL_D)
    c.rect(ox+7, oy+27, 6, 3, TEAL)
    c.rect(ox+18, oy+27, 6, 3, TEAL)
    c.rect(ox+13, oy+25, 5, 5, OUT)
    c.rect(ox+14, oy+26, 3, 4, TEAL_H)
    px(ox+7, oy+27, TEAL_H)
    px(ox+23, oy+27, TEAL_H)

    if mood == "calm":
        # Level brows, relaxed half-lidded eyes, small neutral mouth.
        c.rect(ox+9, oy+13, 5, 1, HAIR_D)
        c.rect(ox+18, oy+13, 4, 1, HAIR_D)
        c.rect(ox+9, oy+15, 5, 1, OUT)
        c.rect(ox+18, oy+15, 4, 1, OUT)
        px(ox+11, oy+16, EYE); px(ox+20, oy+16, EYE)
        c.rect(ox+13, oy+20, 6, 1, MOUTH)
        px(ox+19, oy+19, SKIN_D)
    elif mood == "smile":
        # Upturned closed eyes, blush and broad toothy smile.
        c.line(ox+9, oy+16, ox+11, oy+14, OUT)
        c.line(ox+11, oy+14, ox+14, oy+16, OUT)
        c.line(ox+18, oy+16, ox+20, oy+14, OUT)
        c.line(ox+20, oy+14, ox+22, oy+16, OUT)
        c.rect(ox+7, oy+18, 3, 1, SKIN_D); c.rect(ox+22, oy+18, 3, 1, SKIN_D)
        c.rect(ox+12, oy+19, 8, 1, OUT)
        c.rect(ox+13, oy+20, 6, 2, MOUTH)
        c.rect(ox+14, oy+20, 4, 1, WHITE)
        px(ox+15, oy+22, TONGUE); px(ox+16, oy+22, TONGUE)
        px(ox+12, oy+20, OUT); px(ox+19, oy+20, OUT)
    elif mood == "angry":
        # Hard inward brows, narrowed eyes and clenched uneven mouth.
        c.line(ox+8, oy+13, ox+14, oy+15, HAIR_D)
        c.line(ox+18, oy+15, ox+23, oy+13, HAIR_D)
        c.rect(ox+9, oy+16, 5, 2, OUT)
        c.rect(ox+18, oy+16, 5, 2, OUT)
        c.rect(ox+10, oy+16, 3, 1, WHITE); c.rect(ox+19, oy+16, 3, 1, WHITE)
        px(ox+12, oy+17, EYE); px(ox+19, oy+17, EYE)
        c.line(ox+12, oy+22, ox+15, oy+20, MOUTH)
        c.line(ox+15, oy+20, ox+20, oy+22, MOUTH)
        px(ox+7, oy+17, SKIN_D); px(ox+24, oy+17, SKIN_D)
    else:
        # Raised brows, wide eyes and an open round mouth.
        c.line(ox+9, oy+13, ox+13, oy+12, HAIR_D)
        c.line(ox+18, oy+12, ox+22, oy+13, HAIR_D)
        c.rect(ox+9, oy+14, 5, 5, OUT)
        c.rect(ox+18, oy+14, 5, 5, OUT)
        c.rect(ox+10, oy+15, 3, 3, WHITE); c.rect(ox+19, oy+15, 3, 3, WHITE)
        px(ox+12, oy+17, EYE); px(ox+19, oy+17, EYE)
        c.rect(ox+14, oy+20, 4, 4, OUT)
        c.rect(ox+15, oy+21, 2, 2, MOUTH)
        px(ox+15, oy+21, WHITE)


portrait(0, 0, "calm")
portrait(32, 0, "smile")
portrait(0, 32, "angry")
portrait(32, 32, "surprised")

view(c, scale=8, margin=0)
finish(c)
