from pixelbench_api import new_canvas, flatten, finish

OUT   = (20, 20, 20)
SKIN  = (244, 196, 150)
HAIR  = (236, 184, 64)
RED   = (204, 44, 40)
DRED  = (150, 32, 30)
WHITE = (250, 250, 250)
YEL   = (255, 212, 64)
PINK  = (255, 176, 190)


def body(c):
    # torso / top
    c.rect(10, 15, 12, 5, RED)          # cols10..21, rows15..19
    c.rect(10, 19, 12, 1, WHITE)        # waist band
    # skirt
    c.rect(9, 20, 14, 4, RED)           # rows20..23
    c.rect(10, 20, 1, 4, WHITE)
    c.rect(14, 20, 1, 4, WHITE)
    # legs
    c.rect(12, 23, 3, 6, SKIN)
    c.rect(17, 23, 3, 6, SKIN)
    # socks
    c.rect(12, 27, 3, 2, WHITE)
    c.rect(17, 27, 3, 2, WHITE)
    # shoes
    c.rect(11, 29, 5, 2, WHITE)
    c.rect(16, 29, 5, 2, WHITE)
    c.rect(11, 27, 5, 2, RED)           # shoe tops
    c.rect(16, 27, 5, 2, RED)
    # arms
    c.rect(7, 15, 3, 5, SKIN)
    c.rect(22, 15, 3, 5, SKIN)
    # pom poms
    c.circle(5, 18, 3, YEL)
    c.circle(27, 18, 3, YEL)
    c.circle(5, 18, 2, WHITE)


def draw_front(c):
    # hair
    c.circle(15, 8, 5, HAIR)
    c.circle(8, 9, 3, HAIR)
    c.circle(22, 9, 3, HAIR)
    # face
    c.circle(15, 10, 4, SKIN)
    # eyes
    c.set(13, 10, OUT)
    c.set(17, 10, OUT)
    # cheeks
    c.set(12, 11, PINK)
    c.set(18, 11, PINK)
    # mouth
    c.set(15, 12, DRED)
    c.set(15, 13, DRED)
    # fringe hints already in hair
    body(c)
    c.outline(OUT)


def draw_back(c):
    # full hair (no face)
    c.circle(15, 8, 5, HAIR)
    c.circle(8, 9, 3, HAIR)
    c.circle(22, 9, 3, HAIR)
    body(c)
    # number on back
    c.rect(15, 16, 1, 3, WHITE)         # vertical stroke of "1"
    c.rect(15, 15, 3, 1, WHITE)         # flag on top
    c.outline(OUT)


def draw_side(c):
    # head facing left
    c.circle(24, 8, 4, HAIR)            # back hair
    c.circle(16, 8, 5, HAIR)            # hair mass
    c.circle(13, 9, 4, SKIN)            # face
    c.set(11, 10, OUT)                  # eye
    c.set(11, 12, DRED)                  # mouth
    c.set(10, 11, PINK)                  # cheek
    # torso
    c.rect(12, 15, 10, 5, RED)
    c.rect(12, 19, 10, 1, WHITE)
    # skirt
    c.rect(11, 20, 12, 4, RED)
    c.rect(12, 20, 1, 4, WHITE)
    c.rect(18, 20, 1, 4, WHITE)
    # legs
    c.rect(13, 23, 3, 6, SKIN)
    c.rect(18, 23, 3, 6, SKIN)
    c.rect(13, 27, 3, 2, WHITE)
    c.rect(18, 27, 3, 2, WHITE)
    c.rect(12, 29, 5, 2, WHITE)
    c.rect(17, 29, 5, 2, WHITE)
    c.rect(12, 27, 5, 2, RED)
    c.rect(17, 27, 5, 2, RED)
    # front arm (left/forward)
    c.rect(8, 15, 3, 5, SKIN)
    c.circle(4, 18, 3, YEL)
    c.circle(4, 18, 2, WHITE)
    # back arm (right)
    c.rect(23, 15, 2, 5, SKIN)
    c.circle(26, 18, 3, YEL)
    c.circle(26, 18, 2, WHITE)
    c.outline(OUT)


front = new_canvas(32, 32)
draw_front(front)

back = new_canvas(32, 32)
draw_back(back)

left = new_canvas(32, 32)
draw_side(left)

right = left.copy()
right.mirror("h")

result = new_canvas(64, 64)
result.blit(front, 0, 0)
result.blit(back, 32, 0)
result.blit(left, 0, 32)
result.blit(right, 32, 32)

finish(result)
