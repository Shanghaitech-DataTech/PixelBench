from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64, background=None, name="cheerleader_4view")

OUT = "#211827"
HAIR = "#4a2630"
HAIR_HI = "#74404a"
SKIN = "#efb08f"
SKIN_HI = "#ffd0aa"
RED = "#c92f4b"
RED_HI = "#f04b64"
RED_DK = "#8f2039"
WHITE = "#fff4e8"
SHADE = "#d9c9c3"
SOCK = "#f7e9e2"
SHOE = "#67243b"
EYE = "#30202c"

# Small reusable pixel blocks.
def px(x, y, col):
    c.set(x, y, col)

def front(cx, oy):
    # ponytail behind head
    c.rect(cx+6, oy+5, 3, 8, OUT)
    c.rect(cx+7, oy+6, 3, 6, HAIR)
    c.rect(cx+8, oy+8, 3, 4, OUT)
    c.rect(cx+8, oy+8, 2, 3, HAIR_HI)
    c.rect(cx-5, oy+2, 10, 2, OUT)
    c.rect(cx-6, oy+4, 12, 7, OUT)
    c.rect(cx-5, oy+3, 10, 4, HAIR)
    c.rect(cx-4, oy+4, 8, 2, HAIR_HI)
    # face and bangs
    c.rect(cx-4, oy+6, 8, 6, SKIN)
    c.rect(cx-3, oy+7, 6, 5, SKIN_HI)
    c.rect(cx-5, oy+5, 3, 3, HAIR)
    c.rect(cx+2, oy+5, 3, 3, HAIR)
    px(cx-2, oy+8, EYE); px(cx+2, oy+8, EYE)
    c.rect(cx-1, oy+10, 3, 1, RED_DK)
    # neck
    c.rect(cx-2, oy+12, 4, 2, OUT); c.rect(cx-1, oy+12, 2, 2, SKIN)
    # arms, angled down to hips
    c.line(cx-6, oy+14, cx-8, oy+20, OUT); c.line(cx-7, oy+14, cx-9, oy+20, OUT)
    c.line(cx+6, oy+14, cx+8, oy+20, OUT); c.line(cx+7, oy+14, cx+9, oy+20, OUT)
    c.rect(cx-9, oy+19, 3, 3, SKIN); c.rect(cx+7, oy+19, 3, 3, SKIN)
    # sleeveless V shell
    c.poly([(cx-5,oy+13),(cx+5,oy+13),(cx+6,oy+21),(cx-6,oy+21)], OUT)
    c.poly([(cx-4,oy+14),(cx+4,oy+14),(cx+5,oy+20),(cx-5,oy+20)], RED)
    c.poly([(cx-3,oy+14),(cx,oy+17),(cx+3,oy+14),(cx+1,oy+14),(cx,oy+15),(cx-1,oy+14)], WHITE)
    c.rect(cx-4, oy+18, 8, 2, WHITE)
    c.rect(cx-1, oy+17, 2, 2, RED_HI)
    # pleated skirt
    c.poly([(cx-6,oy+21),(cx+6,oy+21),(cx+8,oy+26),(cx-8,oy+26)], OUT)
    c.poly([(cx-5,oy+21),(cx+5,oy+21),(cx+6,oy+25),(cx-6,oy+25)], RED)
    c.poly([(cx-3,oy+21),(cx-1,oy+21),(cx-2,oy+25),(cx-4,oy+25)], WHITE)
    c.poly([(cx+1,oy+21),(cx+3,oy+21),(cx+4,oy+25),(cx+2,oy+25)], RED_HI)
    # legs, socks, shoes
    for dx in (-4,3):
        c.rect(cx+dx, oy+26, 3, 4, OUT); c.rect(cx+dx+1, oy+26, 2, 3, SKIN)
        c.rect(cx+dx, oy+29, 3, 2, SOCK)
    c.rect(cx-5, oy+30, 5, 2, OUT); c.rect(cx-4, oy+30, 4, 1, SHOE)
    c.rect(cx+2, oy+30, 5, 2, OUT); c.rect(cx+3, oy+30, 4, 1, SHOE)

def back(cx, oy):
    # ponytail centered down back
    c.rect(cx-6, oy+3, 12, 10, OUT)
    c.rect(cx-5, oy+3, 10, 9, HAIR)
    c.rect(cx-4, oy+3, 8, 2, HAIR_HI)
    c.rect(cx+4, oy+8, 4, 7, OUT); c.rect(cx+5, oy+8, 2, 6, HAIR)
    c.rect(cx+5, oy+9, 2, 2, HAIR_HI)
    c.rect(cx-2, oy+12, 4, 2, OUT); c.rect(cx-1, oy+12, 2, 2, SKIN)
    # arms
    c.line(cx-6, oy+14, cx-8, oy+20, OUT); c.line(cx-7, oy+14, cx-9, oy+20, OUT)
    c.line(cx+6, oy+14, cx+8, oy+20, OUT); c.line(cx+7, oy+14, cx+9, oy+20, OUT)
    c.rect(cx-9, oy+19, 3, 3, SKIN); c.rect(cx+7, oy+19, 3, 3, SKIN)
    # back shell
    c.poly([(cx-5,oy+13),(cx+5,oy+13),(cx+6,oy+21),(cx-6,oy+21)], OUT)
    c.poly([(cx-4,oy+14),(cx+4,oy+14),(cx+5,oy+20),(cx-5,oy+20)], RED)
    c.rect(cx-3, oy+14, 6, 1, WHITE)
    c.poly([(cx-4,oy+16),(cx,oy+19),(cx+4,oy+16),(cx+4,oy+18),(cx,oy+20),(cx-4,oy+18)], WHITE)
    # skirt
    c.poly([(cx-6,oy+21),(cx+6,oy+21),(cx+8,oy+26),(cx-8,oy+26)], OUT)
    c.poly([(cx-5,oy+21),(cx+5,oy+21),(cx+6,oy+25),(cx-6,oy+25)], RED_DK)
    c.poly([(cx-4,oy+21),(cx-2,oy+21),(cx-3,oy+25),(cx-5,oy+25)], RED_HI)
    c.poly([(cx+2,oy+21),(cx+4,oy+21),(cx+5,oy+25),(cx+3,oy+25)], WHITE)
    for dx in (-4,3):
        c.rect(cx+dx, oy+26, 3, 4, OUT); c.rect(cx+dx+1, oy+26, 2, 3, SKIN)
        c.rect(cx+dx, oy+29, 3, 2, SOCK)
    c.rect(cx-5, oy+30, 5, 2, OUT); c.rect(cx-4, oy+30, 4, 1, SHOE)
    c.rect(cx+2, oy+30, 5, 2, OUT); c.rect(cx+3, oy+30, 4, 1, SHOE)

def side(cx, oy, facing):
    s = facing
    # back-facing ponytail opposite the nose
    c.rect(cx-5*s, oy+5, 4, 8, OUT)
    c.rect(cx-6*s if s>0 else cx+3, oy+7, 4, 6, OUT)
    # hair/head mass
    c.rect(cx-4, oy+3, 8, 9, OUT)
    c.rect(cx-3, oy+3, 6, 8, HAIR)
    c.rect(cx-2, oy+4, 5, 2, HAIR_HI)
    # profile face projects toward facing
    if s > 0:
        c.rect(cx, oy+6, 5, 6, SKIN); c.rect(cx+1, oy+7, 5, 3, SKIN_HI)
        px(cx+3, oy+7, EYE); px(cx+5, oy+9, RED_DK)
        c.rect(cx-5, oy+6, 3, 6, HAIR); c.rect(cx-6, oy+7, 3, 5, HAIR_HI)
    else:
        c.rect(cx-4, oy+6, 5, 6, SKIN); c.rect(cx-5, oy+7, 5, 3, SKIN_HI)
        px(cx-3, oy+7, EYE); px(cx-6, oy+9, RED_DK)
        c.rect(cx+2, oy+6, 3, 6, HAIR); c.rect(cx+4, oy+7, 3, 5, HAIR_HI)
    c.rect(cx-1, oy+12, 3, 2, OUT); c.rect(cx, oy+12, 2, 2, SKIN)
    # far arm and near arm, hands at waist
    c.line(cx-2*s, oy+14, cx-5*s, oy+20, OUT)
    c.line(cx+2*s, oy+14, cx+5*s, oy+20, OUT)
    c.rect(cx+4*s if s>0 else cx-6, oy+19, 3, 3, SKIN)
    # narrow torso
    c.poly([(cx-4,oy+13),(cx+4,oy+13),(cx+4,oy+21),(cx-4,oy+21)], OUT)
    c.poly([(cx-3,oy+14),(cx+3,oy+14),(cx+3,oy+20),(cx-3,oy+20)], RED)
    c.rect(cx-3, oy+18, 6, 2, WHITE)
    px(cx+2*s, oy+15, RED_HI)
    # side skirt, slightly extended behind
    pts = [(cx-4,oy+21),(cx+4,oy+21),(cx+6,oy+26),(cx-6,oy+26)]
    c.poly(pts, OUT)
    c.poly([(cx-3,oy+21),(cx+3,oy+21),(cx+4,oy+25),(cx-5,oy+25)], RED)
    c.poly([(cx-2*s,oy+21),(cx,oy+21),(cx+1*s,oy+25),(cx-1*s,oy+25)], WHITE)
    # staggered legs reveal profile direction
    c.rect(cx-3, oy+26, 3, 4, OUT); c.rect(cx-2, oy+26, 2, 3, SKIN)
    c.rect(cx+1, oy+26, 3, 4, OUT); c.rect(cx+1, oy+26, 2, 3, SKIN)
    c.rect(cx-3, oy+29, 3, 2, SOCK); c.rect(cx+1, oy+29, 3, 2, SOCK)
    if s > 0:
        c.rect(cx-3, oy+30, 5, 2, OUT); c.rect(cx+1, oy+30, 6, 2, OUT)
        c.rect(cx+2, oy+30, 4, 1, SHOE)
    else:
        c.rect(cx-6, oy+30, 6, 2, OUT); c.rect(cx, oy+30, 5, 2, OUT)
        c.rect(cx-5, oy+30, 4, 1, SHOE)

# Quadrants: front, back / left-facing profile, right-facing profile.
front(16, 0)
back(48, 0)
side(16, 32, -1)
side(48, 32, 1)

view(c, scale=8, margin=0)
finish(c)
