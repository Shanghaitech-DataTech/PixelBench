from pixelbench_api import new_canvas, view, finish

# Two 32x32 side-view walk frames on one transparent sprite sheet.
c = new_canvas(64, 32, background=None, name="swordsman_walk")

OUT = "#161827"
OUT2 = "#24263a"
CAPE_D = "#172b52"
CAPE = "#23477a"
CAPE_H = "#3767a0"
HAIR_D = "#7d2527"
HAIR = "#c04432"
HAIR_H = "#ed6a3d"
SKIN_D = "#9c5544"
SKIN = "#e39a72"
SKIN_H = "#ffc18b"
TUNIC_D = "#39404d"
TUNIC = "#586273"
TUNIC_H = "#7d8995"
BELT = "#6f3d2b"
LEATHER = "#87513a"
BOOT = "#342b35"
STEEL_D = "#65717d"
STEEL = "#b6c5ca"
STEEL_H = "#eef8ed"
GOLD_D = "#8a5b24"
GOLD = "#d4a33e"


def frame1(o):
    # Cape swept backward, with a raised fold.
    c.poly([(o+8,10),(o+5,12),(o+4,18),(o+2,21),(o+7,21),(o+9,19),(o+12,21),(o+14,15),(o+13,11)], OUT)
    c.poly([(o+8,11),(o+6,13),(o+6,17),(o+4,20),(o+8,19),(o+10,17),(o+12,19),(o+13,14),(o+12,12)], CAPE)
    c.line(o+6,14,o+11,12,CAPE_H)
    c.line(o+7,18,o+11,17,CAPE_D)

    # Rear leg stepping back.
    c.poly([(o+11,21),(o+16,21),(o+15,25),(o+12,28),(o+8,28),(o+8,26),(o+11,25)], OUT)
    c.poly([(o+12,22),(o+15,22),(o+14,24),(o+11,27),(o+9,27),(o+12,24)], TUNIC_D)
    c.rect(o+8,27,6,2,OUT)
    c.rect(o+9,27,5,1,BOOT)

    # Front leg reaching forward.
    c.poly([(o+15,21),(o+20,21),(o+20,25),(o+23,27),(o+27,27),(o+28,29),(o+22,30),(o+18,27),(o+16,25)], OUT)
    c.poly([(o+16,22),(o+19,22),(o+19,25),(o+23,28),(o+26,28),(o+23,29),(o+19,26),(o+17,25)], TUNIC)
    c.rect(o+23,28,5,2,OUT)
    c.rect(o+24,28,3,1,BOOT)

    # Body and belt.
    c.poly([(o+10,12),(o+17,11),(o+21,14),(o+20,21),(o+18,24),(o+11,23),(o+9,19)], OUT)
    c.poly([(o+11,13),(o+16,12),(o+19,14),(o+19,20),(o+17,22),(o+12,22),(o+10,19)], TUNIC)
    c.line(o+12,14,o+12,20,TUNIC_H)
    c.rect(o+10,19,10,3,OUT)
    c.rect(o+11,20,8,1,BELT)
    c.rect(o+15,19,2,2,GOLD)

    # Neck and head, facing right.
    c.rect(o+14,9,4,5,OUT)
    c.rect(o+15,9,3,4,SKIN_D)
    c.poly([(o+11,4),(o+18,3),(o+22,6),(o+22,10),(o+19,13),(o+14,12),(o+11,9)], OUT)
    c.poly([(o+13,5),(o+18,4),(o+21,6),(o+21,9),(o+19,11),(o+15,11),(o+12,9)], SKIN)
    c.set(o+20,7,OUT)
    c.set(o+21,10,SKIN_H)

    # Red hair and wind-tossed back locks.
    c.poly([(o+11,4),(o+14,2),(o+19,3),(o+21,5),(o+18,6),(o+16,5),(o+15,8),(o+12,9),(o+10,7)], OUT)
    c.poly([(o+12,4),(o+15,3),(o+19,4),(o+20,5),(o+17,5),(o+15,4),(o+14,7),(o+11,7)], HAIR)
    c.line(o+13,3,o+17,3,HAIR_H)
    c.poly([(o+12,7),(o+9,8),(o+7,7),(o+9,10),(o+13,10)], OUT)
    c.poly([(o+11,8),(o+9,8),(o+10,9),(o+13,9)], HAIR_D)

    # Forward sword arm, kept compact so the full blade fits the frame.
    c.poly([(o+18,13),(o+21,12),(o+24,15),(o+26,16),(o+26,19),(o+23,19),(o+20,17)], OUT)
    c.poly([(o+19,14),(o+21,14),(o+24,16),(o+25,17),(o+25,18),(o+23,18),(o+20,16)], TUNIC_H)
    c.rect(o+24,16,3,4,OUT)
    c.rect(o+25,17,2,2,SKIN)

    # Long sword rises into the open space ahead of the face.
    c.line(o+24,21,o+27,17,OUT)
    c.line(o+25,20,o+27,18,LEATHER)
    c.line(o+24,16,o+29,20,OUT)
    c.line(o+25,16,o+29,19,GOLD)
    c.poly([(o+27,17),(o+30,7),(o+31,6),(o+30,12),(o+29,18)], OUT)
    c.poly([(o+28,16),(o+30,8),(o+31,7),(o+29,17)], STEEL)
    c.line(o+30,8,o+30,14,STEEL_H)


def frame2(o):
    # Cape drops and curls as the body reaches the passing pose.
    c.poly([(o+9,11),(o+6,12),(o+4,16),(o+5,20),(o+2,23),(o+8,22),(o+11,20),(o+13,22),(o+15,16),(o+14,12)], OUT)
    c.poly([(o+9,12),(o+7,13),(o+5,16),(o+6,19),(o+4,21),(o+8,20),(o+11,18),(o+13,20),(o+14,15),(o+13,13)], CAPE)
    c.line(o+6,16,o+12,14,CAPE_H)
    c.line(o+6,20,o+11,18,CAPE_D)

    # Forward leg now planted nearly beneath the body.
    c.poly([(o+12,21),(o+17,21),(o+17,26),(o+16,29),(o+11,29),(o+10,27),(o+13,26)], OUT)
    c.poly([(o+13,22),(o+16,22),(o+16,26),(o+15,28),(o+12,28),(o+14,26)], TUNIC)
    c.rect(o+10,28,7,2,OUT)
    c.rect(o+11,28,5,1,BOOT)

    # Rear leg swings behind with a bent knee.
    c.poly([(o+17,21),(o+21,21),(o+20,24),(o+18,26),(o+21,28),(o+25,28),(o+25,30),(o+20,30),(o+16,27),(o+16,25)], OUT)
    c.poly([(o+18,22),(o+20,22),(o+19,24),(o+17,26),(o+21,29),(o+24,29),(o+21,29),(o+17,27),(o+17,25)], TUNIC_D)
    c.rect(o+21,28,5,2,OUT)
    c.rect(o+22,28,3,1,BOOT)

    # Torso one pixel lower in the stride.
    c.poly([(o+11,13),(o+18,12),(o+22,15),(o+21,22),(o+19,24),(o+12,24),(o+10,20)], OUT)
    c.poly([(o+12,14),(o+17,13),(o+20,15),(o+20,21),(o+18,23),(o+13,23),(o+11,20)], TUNIC)
    c.line(o+13,15,o+13,21,TUNIC_H)
    c.rect(o+11,20,10,3,OUT)
    c.rect(o+12,21,8,1,BELT)
    c.rect(o+16,20,2,2,GOLD)

    # Head shifted down with body bob.
    c.rect(o+15,10,4,5,OUT)
    c.rect(o+16,10,3,4,SKIN_D)
    c.poly([(o+12,5),(o+19,4),(o+23,7),(o+23,11),(o+20,14),(o+15,13),(o+12,10)], OUT)
    c.poly([(o+14,6),(o+19,5),(o+22,7),(o+22,10),(o+20,12),(o+16,12),(o+13,10)], SKIN)
    c.set(o+21,8,OUT)
    c.set(o+22,11,SKIN_H)

    c.poly([(o+12,5),(o+15,3),(o+20,4),(o+22,6),(o+19,7),(o+17,6),(o+16,9),(o+13,10),(o+11,8)], OUT)
    c.poly([(o+13,5),(o+16,4),(o+20,5),(o+21,6),(o+18,6),(o+16,5),(o+15,8),(o+12,8)], HAIR)
    c.line(o+14,4,o+18,4,HAIR_H)
    c.poly([(o+13,8),(o+10,9),(o+8,8),(o+10,11),(o+14,11)], OUT)
    c.poly([(o+12,9),(o+10,9),(o+11,10),(o+14,10)], HAIR_D)

    # Sword arm settles lower and farther forward.
    c.poly([(o+19,14),(o+22,14),(o+24,17),(o+26,18),(o+26,21),(o+23,20),(o+21,18)], OUT)
    c.poly([(o+20,15),(o+22,15),(o+24,18),(o+25,19),(o+24,19),(o+21,17)], TUNIC_H)
    c.rect(o+24,18,3,4,OUT)
    c.rect(o+25,19,2,2,SKIN)

    # Blade settles toward horizontal as the rear leg passes.
    c.line(o+24,23,o+27,19,OUT)
    c.line(o+25,22,o+27,20,LEATHER)
    c.line(o+24,18,o+29,22,OUT)
    c.line(o+25,18,o+29,21,GOLD)
    c.poly([(o+27,19),(o+29,11),(o+31,9),(o+31,13),(o+29,20)], OUT)
    c.poly([(o+28,19),(o+30,12),(o+31,11),(o+30,15),(o+29,19)], STEEL)
    c.line(o+30,12,o+30,16,STEEL_H)


frame1(0)
frame2(32)

view(c, scale=12, margin=0)
finish(c)
