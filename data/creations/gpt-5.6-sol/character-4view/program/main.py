from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64, background=None, name="cheerleader_four_views")

OUT = "#241b2b"
HAIR = "#5b2f32"
HAIR_HI = "#8e4a3d"
SKIN = "#f2b49b"
SKIN_HI = "#ffd0b2"
RED = "#c73b4b"
RED_HI = "#ef5a62"
CREAM = "#fff2d2"
NAVY = "#263552"
BLUE = "#3f5278"
WHITE = "#fffaf0"
SOLE = "#b9c1cf"
EYE = "#30202d"


def r(x,y,w,h,col): c.rect(x,y,w,h,col)
def p(points,col): c.poly(points,col)
def q(x,y,col): c.set(x,y,col)
def line(x0,y0,x1,y1,col): c.line(x0,y0,x1,y1,col)


def legs_front(x, y):
    # separated legs and low-top sneakers
    r(x+7,y+20,4,8,OUT); r(x+14,y+20,4,8,OUT)
    r(x+8,y+20,3,7,SKIN); r(x+14,y+20,3,7,SKIN_HI)
    r(x+6,y+27,6,3,OUT); r(x+13,y+27,6,3,OUT)
    r(x+7,y+27,5,2,WHITE); r(x+14,y+27,5,2,WHITE)
    r(x+7,y+29,5,1,SOLE); r(x+14,y+29,5,1,SOLE)


def skirt_front(x,y, back=False):
    p([(x+6,y+19),(x+19,y+19),(x+21,y+23),(x+4,y+23)],OUT)
    p([(x+7,y+20),(x+18,y+20),(x+19,y+22),(x+6,y+22)],NAVY)
    if back:
        r(x+12,y+20,1,3,BLUE); q(x+8,y+21,BLUE); q(x+16,y+21,BLUE)
    else:
        line(x+9,y+20,x+8,y+22,BLUE); line(x+13,y+20,x+13,y+22,BLUE); line(x+17,y+20,x+18,y+22,BLUE)


def front(x,y):
    # ponytail behind left shoulder
    r(x+3,y+4,4,8,OUT); r(x+2,y+7,4,7,OUT)
    r(x+3,y+7,3,6,HAIR); q(x+4,y+6,HAIR_HI)
    # head and hair cap
    p([(x+7,y+2),(x+17,y+2),(x+20,y+5),(x+19,y+12),(x+16,y+15),(x+9,y+15),(x+6,y+12),(x+5,y+6)],OUT)
    p([(x+7,y+6),(x+18,y+6),(x+18,y+11),(x+15,y+14),(x+10,y+14),(x+7,y+11)],SKIN)
    p([(x+6,y+5),(x+8,y+2),(x+17,y+3),(x+19,y+6),(x+17,y+7),(x+15,y+5),(x+13,y+7),(x+10,y+5),(x+7,y+8)],HAIR)
    q(x+8,y+4,HAIR_HI); q(x+9,y+4,HAIR_HI)
    q(x+9,y+9,EYE); q(x+16,y+9,EYE); r(x+11,y+12,4,1,"#b65d67")
    # arms, hands at hips
    line(x+6,y+15,x+3,y+21,OUT); line(x+3,y+21,x+6,y+23,OUT)
    line(x+19,y+15,x+22,y+21,OUT); line(x+22,y+21,x+19,y+23,OUT)
    line(x+6,y+16,x+4,y+21,SKIN); q(x+5,y+21,SKIN_HI)
    line(x+19,y+16,x+21,y+21,SKIN); q(x+20,y+21,SKIN_HI)
    # varsity top
    p([(x+7,y+14),(x+10,y+13),(x+15,y+13),(x+18,y+14),(x+20,y+19),(x+18,y+20),(x+7,y+20),(x+5,y+19)],OUT)
    p([(x+8,y+14),(x+10,y+14),(x+12,y+16),(x+15,y+14),(x+17,y+14),(x+18,y+19),(x+7,y+19)],RED)
    p([(x+10,y+14),(x+12,y+17),(x+15,y+14),(x+16,y+14),(x+13,y+18),(x+11,y+18),(x+9,y+14)],CREAM)
    r(x+8,y+18,9,1,RED_HI)
    skirt_front(x,y); legs_front(x,y)


def back(x,y):
    # ponytail centered down the back
    r(x+9,y+10,8,8,OUT); r(x+10,y+10,6,7,HAIR); r(x+11,y+14,4,4,HAIR_HI)
    p([(x+7,y+2),(x+17,y+2),(x+20,y+6),(x+19,y+12),(x+16,y+15),(x+9,y+15),(x+6,y+12),(x+5,y+6)],OUT)
    p([(x+7,y+5),(x+9,y+3),(x+17,y+3),(x+19,y+6),(x+18,y+12),(x+16,y+14),(x+9,y+14),(x+7,y+11)],HAIR)
    p([(x+8,y+4),(x+13,y+3),(x+18,y+6),(x+18,y+8),(x+13,y+6),(x+7,y+8)],HAIR_HI)
    # visible ears/neck
    r(x+7,y+9,2,3,SKIN); r(x+17,y+9,2,3,SKIN); r(x+11,y+13,4,3,SKIN)
    # arms
    line(x+6,y+15,x+3,y+21,OUT); line(x+3,y+21,x+6,y+23,OUT)
    line(x+19,y+15,x+22,y+21,OUT); line(x+22,y+21,x+19,y+23,OUT)
    line(x+6,y+16,x+4,y+21,SKIN); line(x+19,y+16,x+21,y+21,SKIN)
    # top back
    p([(x+7,y+14),(x+10,y+13),(x+15,y+13),(x+18,y+14),(x+20,y+19),(x+18,y+20),(x+7,y+20),(x+5,y+19)],OUT)
    p([(x+8,y+14),(x+10,y+14),(x+11,y+16),(x+15,y+16),(x+16,y+14),(x+17,y+14),(x+18,y+19),(x+7,y+19)],RED)
    p([(x+10,y+14),(x+11,y+17),(x+15,y+17),(x+16,y+14),(x+15,y+14),(x+14,y+16),(x+12,y+16),(x+11,y+14)],CREAM)
    r(x+8,y+18,9,1,RED_HI)
    skirt_front(x,y,True); legs_front(x,y)


def side(x,y,facing):
    # facing 1 right, -1 left; mirror coordinates by helper
    def X(a): return x+a if facing==1 else x+24-a
    def rect_lr(a,b,w,h,col):
        if facing==1: r(x+a,y+b,w,h,col)
        else: r(x+25-a-w,y+b,w,h,col)
    def poly_lr(pts,col): p([(X(a),y+b) for a,b in pts],col)
    # back ponytail
    rect_lr(5,5,5,9,OUT); rect_lr(5,6,4,7,HAIR); q(X(6),y+7,HAIR_HI)
    # profile head, nose at facing edge
    poly_lr([(8,2),(15,2),(18,5),(19,8),(21,9),(19,11),(17,14),(10,14),(7,11),(7,5)],OUT)
    poly_lr([(10,5),(17,5),(18,8),(20,9),(18,10),(16,13),(11,13),(9,11),(9,7)],SKIN)
    poly_lr([(8,5),(10,2),(16,3),(18,5),(16,7),(13,5),(10,8),(8,8)],HAIR)
    q(X(17),y+8,EYE); q(X(18),y+11,"#b65d67")
    rect_lr(11,13,4,3,SKIN)
    # far arm then torso
    line(X(10),y+16,X(8),y+22,OUT); line(X(8),y+22,X(11),y+23,OUT)
    line(X(10),y+17,X(9),y+21,SKIN)
    poly_lr([(10,14),(16,14),(18,16),(17,20),(9,20),(8,17)],OUT)
    poly_lr([(11,15),(15,15),(17,16),(16,19),(10,19),(9,17)],RED)
    line(X(12),y+15,X(15),y+19,CREAM)
    q(X(11),y+18,RED_HI)
    # near arm angled to hip
    line(X(17),y+16,X(20),y+21,OUT); line(X(20),y+21,X(17),y+22,OUT)
    line(X(17),y+17,X(19),y+21,SKIN_HI)
    # side skirt
    poly_lr([(9,19),(17,19),(19,23),(7,23)],OUT)
    poly_lr([(10,20),(16,20),(17,22),(9,22)],NAVY)
    line(X(12),y+20,X(11),y+22,BLUE)
    # one leg prominent, second offset
    rect_lr(9,22,4,7,OUT); rect_lr(10,22,3,6,SKIN)
    rect_lr(14,22,4,7,OUT); rect_lr(14,22,3,6,SKIN_HI)
    rect_lr(8,28,7,2,OUT); rect_lr(9,28,6,1,WHITE)
    rect_lr(13,28,7,2,OUT); rect_lr(14,28,6,1,WHITE)

front(3,1)
back(35,1)
side(3,33,-1)
side(35,33,1)

view(c, scale=8, margin=0)
finish(c)
