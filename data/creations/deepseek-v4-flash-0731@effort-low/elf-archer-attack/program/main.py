from pixelbench_api import *
import math

W,H = 54,56

# ---- frame 1: original content kept, on the shared canvas ----
f1 = new_canvas(W, H, name='output')
f1.blit(input_canvas, 0, 0)

# ---- frame 2: elf archer, bow fully drawn to max, no arrow ----
f2 = new_canvas(W, H, name='output2')

def pl(c, x0,y0,x1,y1,col,w):
    dx=x1-x0; dy=y1-y0
    L=math.hypot(dx,dy) or 1.0
    px=-dy/L; py=dx/L
    for i in range(w):
        o=i-(w-1)/2.0
        c.line(round(x0+px*o), round(y0+py*o), round(x1+px*o), round(y1+py*o), col)
    return c

# palette
SKIN='#c5956a'; SKIN2='#7b4231'; SKIND='#422110'
HAIRC='#ef5ba1'; HAIRD='#55002a'
GRN='#529439'; GRND='#4f7229'; GRNL='#9cde5a'
DARK='#121311'; DARK2='#252a23'; BOWO='#2b1a10'; BOWI='#965a32'
SHW='#17003599'; EYEW='#ffffff'

# ground shadow
f2.ellipse(27,49,22,4, SHW)

# ----- bow crescent (vertical, belly bulging right) -----
f2.path("M43,4 C50,13 52,23 52,27 C52,32 49,41 43,51 L42,51 C48,38 50,31 50,27 C50,22 49,12 42,4 Z", BOWO)
f2.path("M43,6 C48,13 50,22 50,27 C50,31 48,40 43,49", BOWI, fill=False)
# grip
f2.circle(44,26,2, BOWI)

# ----- string (taut between tips and draw hand) -----
f2.line(43,4,21,16, DARK)
f2.line(21,16,43,51, DARK)

# ----- back arm holding the bow (extends right to grip) -----
pl(f2, 19,20, 42,26, SKIN2, 2)
f2.circle(43,26,2, SKIN)

# ----- draw arm from shoulder to cheek anchor -----
pl(f2, 17,19, 21,16, SKIN2, 2)
f2.circle(21,16,2, SKIN)
f2.circle(21,16,1, SKIND)

# ----- head -----
f2.ellipse(15,12, 3,4, SKIN)
f2.poly([(16,10),(21,6),(18,12)], SKIN)
f2.poly([(17,10),(20,8),(18,11)], SKIN2)
f2.ellipse(14,9, 4,3, HAIRC)
pl(f2, 18,8, 24,4, HAIRC, 2)
f2.circle(17,8,1, HAIRC)
# face looking left
f2.set(12,11, DARK)
f2.set(11,10, EYEW)
f2.set(11,12, SKIND)
f2.set(10,13, SKIND)

# ----- torso (green tunic, leaning forward) -----
f2.poly([(12,17),(19,17),(18,27),(12,26)], GRN)
pl(f2, 14,18, 17,19, GRNL,1)
f2.poly([(12,24),(18,25),(18,27),(12,26)], DARK2)
pl(f2, 13,26, 17,26, GRND,1)

# ----- legs: straddled, crouched stance -----
# back leg (right, extended back)
pl(f2, 16,26, 26,33, GRN, 2)
pl(f2, 26,32, 28,40, GRN, 2)
pl(f2, 27,32, 29,40, SKIN2, 2)
pl(f2, 28,40, 29,45, DARK2, 3)
# front leg (left, forward/left)
pl(f2, 13,25, 8,33, GRN, 2)
pl(f2, 8,32, 6,40, SKIN2, 1)
pl(f2, 6,40, 5,45, DARK2, 3)

finish([f1, f2])
print("submitted", len(canvases()), "canvases")
