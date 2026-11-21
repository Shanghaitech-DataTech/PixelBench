from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="result")

OUT    = c.color("#171425")
SKIN   = c.color("#f7c9a3")
SKIN_D = c.color("#dc9f78")
HAIR   = c.color("#6b3a1e")
HAIR_D = c.color("#40200f")
HAIR_L = c.color("#9a5a2c")
WHITE  = c.color("#f7f8fc")
WHITE_D= c.color("#c9d0e0")
RED    = c.color("#e02b3c")
RED_D  = c.color("#a3162a")
GOLD   = c.color("#f7cf5a")
POM    = c.color("#ff87ad")
POM_L  = c.color("#ffc4d6")


def h(cv, y, x0, x1, col):
    for x in range(x0, x1 + 1):
        cv.set(x, y, col)


def v(cv, x, y0, y1, col):
    for y in range(y0, y1 + 1):
        cv.set(x, y, col)


def box(cv, x0, y0, x1, y1, col):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            cv.set(x, y, col)


def pom(cv, cx, cy, col=POM):
    box(cv, cx - 1, cy - 2, cx + 1, cy + 2, col)
    box(cv, cx - 2, cy - 1, cx + 2, cy + 1, col)


def head_top(cv, rx0, rx1):
    """rounded top of head + red ribbon band (rx0..rx1)"""
    h(cv, 1, rx0 + 1, rx1 - 1, RED)
    h(cv, 2, rx0 - 1, rx1 + 1, HAIR)
    h(cv, 3, rx0 - 3, rx1 + 3, HAIR)
    h(cv, 2, rx0, rx1, RED)
    h(cv, 3, rx0, rx1, RED)


# ---------------------------------------------------------------- shared body
def body(cv):
    box(cv, 12, 14, 19, 18, WHITE)      # torso / sleeveless top
    box(cv, 9, 14, 11, 15, WHITE)       # shoulder puff
    box(cv, 20, 14, 22, 15, WHITE)
    box(cv, 9, 16, 11, 19, SKIN)        # left arm + hand
    box(cv, 20, 16, 22, 19, SKIN)       # right arm + hand
    h(cv, 19, 12, 19, RED)              # waistband
    h(cv, 20, 11, 20, RED)              # pleated skirt
    h(cv, 21, 10, 21, RED)
    h(cv, 22, 9, 22, RED)
    h(cv, 23, 9, 22, RED_D)
    box(cv, 11, 24, 14, 27, SKIN)       # left leg
    box(cv, 17, 24, 20, 27, SKIN)       # right leg
    box(cv, 10, 28, 14, 30, WHITE)      # left shoe
    box(cv, 17, 28, 21, 30, WHITE)      # right shoe
    pom(cv, 6, 18)                      # poms
    pom(cv, 25, 18)


# ---------------------------------------------------------------- front view
def front_base(cv):
    head_top(cv, 13, 18)
    h(cv, 4, 9, 22, HAIR)
    box(cv, 9, 5, 22, 13, HAIR)
    box(cv, 12, 5, 19, 10, SKIN)        # face
    h(cv, 11, 13, 18, SKIN)             # chin
    box(cv, 13, 12, 18, 13, SKIN)       # neck
    body(cv)


def front_detail(cv):
    h(cv, 4, 13, 16, HAIR_L)            # bangs highlight
    h(cv, 3, 11, 12, HAIR_L)            # hair shine beside ribbon
    h(cv, 3, 19, 20, HAIR_L)
    cv.set(15, 2, GOLD)                 # ribbon knot
    cv.set(16, 2, GOLD)
    h(cv, 12, 12, 12, HAIR_D)           # hair shading by neck
    h(cv, 12, 19, 19, HAIR_D)
    h(cv, 13, 12, 12, HAIR_D)
    h(cv, 13, 19, 19, HAIR_D)
    # eyes
    box(cv, 13, 6, 14, 7, OUT)
    box(cv, 17, 6, 18, 7, OUT)
    cv.set(14, 6, WHITE)
    cv.set(18, 6, WHITE)
    # mouth, blush, neck shadow
    h(cv, 9, 15, 16, RED_D)
    cv.set(12, 8, POM_L)
    cv.set(19, 8, POM_L)
    h(cv, 13, 14, 17, SKIN_D)
    # V-neck trim
    h(cv, 14, 15, 16, RED)
    cv.set(14, 15, RED)
    cv.set(17, 15, RED)
    cv.set(13, 16, RED)
    cv.set(18, 16, RED)
    h(cv, 18, 12, 19, WHITE_D)          # shade above waistband
    # skirt pleats
    v(cv, 12, 20, 23, RED_D)
    v(cv, 16, 20, 23, RED_D)
    v(cv, 19, 20, 23, RED_D)
    h(cv, 23, 11, 20, OUT)              # dark hem
    # shoes
    h(cv, 28, 11, 13, RED)
    h(cv, 28, 18, 20, RED)
    # pom shine
    cv.set(6, 18, POM_L)
    cv.set(25, 18, POM_L)


# ---------------------------------------------------------------- back view
def back_base(cv):
    head_top(cv, 13, 18)
    h(cv, 4, 9, 22, HAIR)
    box(cv, 9, 5, 22, 13, HAIR)
    body(cv)


def back_detail(cv):
    h(cv, 3, 11, 12, HAIR_L)
    h(cv, 3, 19, 20, HAIR_L)
    cv.set(15, 2, GOLD)
    cv.set(16, 2, GOLD)
    v(cv, 13, 5, 11, HAIR_L)            # hair strands
    v(cv, 18, 5, 9, HAIR_L)
    h(cv, 12, 10, 21, HAIR_D)
    h(cv, 13, 10, 21, HAIR_D)
    h(cv, 14, 13, 18, RED)              # red yoke
    h(cv, 18, 12, 19, WHITE_D)
    v(cv, 12, 20, 23, RED_D)
    v(cv, 16, 20, 23, RED_D)
    v(cv, 19, 20, 23, RED_D)
    h(cv, 23, 11, 20, OUT)              # dark hem
    h(cv, 28, 11, 13, RED)
    h(cv, 28, 18, 20, RED)
    cv.set(6, 18, POM_L)
    cv.set(25, 18, POM_L)


# ---------------------------------------------------------------- side view
def side_base(cv):
    head_top(cv, 13, 17)
    h(cv, 4, 10, 21, HAIR)
    box(cv, 10, 4, 21, 13, HAIR)
    box(cv, 10, 5, 17, 10, SKIN)        # face profile
    h(cv, 11, 11, 16, SKIN)             # jaw
    box(cv, 13, 12, 16, 13, SKIN)       # neck
    cv.set(9, 7, SKIN)                  # nose
    cv.set(9, 8, SKIN)
    box(cv, 12, 14, 19, 18, WHITE)      # torso
    h(cv, 19, 12, 19, RED)
    h(cv, 20, 11, 20, RED)
    h(cv, 21, 10, 20, RED)
    h(cv, 22, 9, 20, RED)
    h(cv, 23, 9, 20, RED_D)
    box(cv, 13, 16, 15, 19, SKIN)       # near arm
    box(cv, 12, 24, 15, 27, SKIN)       # leg
    box(cv, 9, 28, 16, 30, WHITE)       # shoe
    pom(cv, 10, 18)


def side_detail(cv):
    v(cv, 19, 5, 11, HAIR_L)            # hair shine at back
    h(cv, 4, 12, 15, HAIR_L)            # bangs highlight
    h(cv, 12, 17, 20, HAIR_D)
    h(cv, 13, 17, 20, HAIR_D)
    cv.set(15, 2, GOLD)
    cv.set(9, 7, OUT)                   # nose line
    cv.set(9, 8, OUT)
    box(cv, 12, 6, 13, 7, OUT)          # eye
    cv.set(12, 6, WHITE)
    h(cv, 9, 11, 12, RED_D)             # mouth
    h(cv, 14, 15, 18, RED)              # collar
    h(cv, 18, 16, 18, WHITE_D)
    v(cv, 13, 20, 23, RED_D)
    v(cv, 17, 20, 23, RED_D)
    h(cv, 23, 10, 19, OUT)              # dark hem
    h(cv, 28, 10, 13, RED)
    cv.set(10, 18, POM_L)


def make_view(fb, fd, mirror=False):
    cv = new_canvas(32, 32, background=None)
    fb(cv)
    cv.outline(OUT)
    fd(cv)
    if mirror:
        cv.mirror("h")
    return cv


def dump(cv, x0, y0, w=32, ht=32):
    chars = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    seen = {}
    rows = []
    for y in range(y0, y0 + ht):
        line = ""
        for x in range(x0, x0 + w):
            idx = cv.get(x, y)
            if idx not in seen:
                seen[idx] = chars[len(seen)] if len(seen) < len(chars) else "?"
            line += seen[idx]
        rows.append(line)
    print("    " + "".join(str((x0 + i) % 10) for i in range(w)))
    for i, line in enumerate(rows):
        print("%3d " % (y0 + i) + line)
    for idx, ch in seen.items():
        print("   %s = %s" % (ch, cv.color_name(idx)))


front = make_view(front_base, front_detail)
back = make_view(back_base, back_detail)
side_l = make_view(side_base, side_detail)
side_r = make_view(side_base, side_detail, mirror=True)

c.blit(front, 0, 0)
c.blit(back, 32, 0)
c.blit(side_l, 0, 32)
c.blit(side_r, 32, 32)

print(c.stats_text())
print("=== FRONT ===")
dump(c, 0, 0)
print("=== BACK ===")
dump(c, 32, 0)
print("=== SIDE L ===")
dump(c, 0, 32)
finish(c)
