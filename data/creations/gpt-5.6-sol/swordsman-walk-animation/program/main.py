# Two-frame 16-bit RPG swordsman walk cycle, 32x32 per frame.
result = new_canvas(64, 32, background=None, name="swordsman_walk")

# Compact SNES-style palette.
outline = "#171827"
outline2 = "#242238"
cape_dark = "#17284a"
cape_mid = "#24436b"
cape_light = "#35618a"
hair_dark = "#7a251f"
hair = "#bd3b2a"
hair_light = "#e35b35"
skin_dark = "#a9573e"
skin = "#e18a61"
skin_light = "#f3b27c"
tunic_dark = "#3c3c4c"
tunic = "#626276"
leather = "#75452d"
leather_light = "#a66a3c"
metal_dark = "#6d7b8c"
metal = "#b8c7cf"
metal_light = "#eef3e9"
boot = "#30272b"


def px(x, y, w, h, c):
    result.rect(x, y, w, h, c)


def frame(o, phase):
    # Cape: broad, dark, and visibly displaced between steps.
    if phase == 0:
        result.poly([(o+9,10),(o+5,13),(o+4,22),(o+8,25),(o+13,23),(o+14,14)], outline)
        result.poly([(o+9,11),(o+6,14),(o+6,21),(o+9,23),(o+12,21),(o+12,13)], cape_mid)
        px(o+6,18,2,4,cape_dark); px(o+8,13,3,2,cape_light); px(o+8,22,3,1,cape_light)
    else:
        result.poly([(o+9,10),(o+4,13),(o+2,19),(o+5,22),(o+11,23),(o+14,14)], outline)
        result.poly([(o+9,11),(o+5,14),(o+4,18),(o+6,20),(o+11,21),(o+12,13)], cape_mid)
        px(o+4,17,2,3,cape_dark); px(o+6,13,4,2,cape_light); px(o+7,20,4,1,cape_light)

    # Hair mass and ponytail, facing right.
    px(o+9,4,8,2,outline); px(o+7,6,11,5,outline); px(o+8,5,8,6,hair)
    px(o+8,6,3,3,hair_light); px(o+7,8,3,4,hair_dark)
    px(o+5,9,3,3,outline); px(o+4,10,3,2,hair_dark)
    if phase == 0:
        px(o+3,11,3,2,outline); px(o+2,12,3,2,hair)
    else:
        px(o+4,12,3,2,outline); px(o+3,13,3,2,hair)

    # Face and nose profile.
    px(o+12,7,6,5,skin_dark); px(o+13,7,4,4,skin); px(o+17,8,2,2,outline)
    px(o+17,9,3,2,skin); px(o+18,9,2,1,skin_light)
    px(o+15,8,1,1,outline); px(o+13,11,4,2,outline); px(o+14,11,3,1,skin_dark)

    # Torso, belt, shoulder clasp.
    result.poly([(o+10,12),(o+16,12),(o+19,16),(o+17,22),(o+10,22),(o+8,17)], outline)
    result.poly([(o+11,13),(o+15,13),(o+17,16),(o+16,20),(o+10,20),(o+10,15)], tunic)
    px(o+10,14,2,5,tunic_dark); px(o+12,13,3,1,"#858596")
    px(o+9,20,9,3,outline); px(o+10,20,7,1,leather_light); px(o+15,20,2,2,leather)
    px(o+10,12,2,2,metal_light); px(o+10,13,2,1,metal_dark)

    # Sword arm and guard; arm angle changes subtly.
    if phase == 0:
        result.poly([(o+16,14),(o+19,15),(o+22,18),(o+20,20),(o+17,18)], outline)
        px(o+17,15,2,3,skin_dark); px(o+19,17,3,2,skin); px(o+21,18,3,2,outline); px(o+21,18,2,1,skin_light)
        # guard and long blade angled upward
        result.line(o+21,21,o+25,17,leather)
        result.line(o+21,20,o+25,16,outline)
        result.line(o+23,16,o+27,20,metal_dark)
        result.line(o+24,16,o+27,19,metal_light)
        result.poly([(o+25,17),(o+30,12),(o+31,12),(o+28,18)], outline)
        result.poly([(o+26,17),(o+30,13),(o+30,14),(o+27,18)], metal)
        px(o+29,13,1,1,metal_light)
    else:
        result.poly([(o+16,14),(o+20,15),(o+22,17),(o+21,20),(o+18,18)], outline)
        px(o+17,15,3,3,skin_dark); px(o+19,16,3,2,skin); px(o+21,17,3,2,outline); px(o+21,17,2,1,skin_light)
        result.line(o+21,20,o+25,17,leather)
        result.line(o+21,19,o+25,16,outline)
        result.line(o+23,16,o+27,20,metal_dark)
        result.line(o+24,16,o+27,19,metal_light)
        result.poly([(o+25,17),(o+30,13),(o+31,13),(o+28,18)], outline)
        result.poly([(o+26,17),(o+30,14),(o+30,15),(o+27,18)], metal)
        px(o+29,14,1,1,metal_light)

    # Walking legs: swapped extension and planted foot.
    if phase == 0:
        result.poly([(o+10,22),(o+14,22),(o+13,27),(o+10,30),(o+7,30),(o+7,28),(o+10,26)], outline)
        px(o+11,22,2,5,tunic_dark); px(o+8,28,4,1,boot); px(o+7,29,5,2,boot)
        result.poly([(o+14,22),(o+18,22),(o+20,27),(o+23,28),(o+23,30),(o+19,30),(o+16,27),(o+13,26)], outline)
        px(o+15,23,2,4,leather); px(o+17,26,3,2,leather_light); px(o+20,28,4,2,boot)
    else:
        result.poly([(o+10,22),(o+14,22),(o+16,26),(o+19,28),(o+19,30),(o+15,30),(o+12,27),(o+9,26)], outline)
        px(o+11,23,2,4,leather); px(o+13,26,3,2,leather_light); px(o+16,28,4,2,boot)
        result.poly([(o+14,22),(o+18,22),(o+17,27),(o+15,30),(o+11,30),(o+11,28),(o+14,26)], outline)
        px(o+15,22,2,5,tunic_dark); px(o+12,28,4,2,boot); px(o+11,29,5,2,boot)

    # Small grounded contact pixels keep the stance crisp.
    if phase == 0:
        px(o+7,30,5,1,outline); px(o+20,30,4,1,outline)
    else:
        px(o+11,30,5,1,outline); px(o+16,30,4,1,outline)

frame(0, 0)
frame(32, 1)

finish(result)
view(result, scale=12, margin=0)
