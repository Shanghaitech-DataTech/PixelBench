# cheerleader character - 4 views (front, back, left, right) in a 2x2 grid, 64x64
OUT = "#2b2233"      # dark outline
SKIN = "#ffd9b8"
HAIR = "#5a3620"
HAIR_HI = "#7d4e2a"
RED = "#d9354a"
RED_DK = "#a82838"
WHITE = "#f7f3ee"
SHOE = "#e8e2da"
YELLOW = "#ffcf3f"
YELLOW_DK = "#dba42c"

c = new_canvas(64, 64, background=None, name="cheer4view")


def pom(cv, x, y):
    cv.rect(x, y, 4, 5, YELLOW)
    for px, py in [(x + 1, y + 1), (x + 2, y + 3), (x, y + 2), (x + 3, y + 1), (x + 2, y)]:
        cv.set(px, py, YELLOW_DK)


def front(cv, ox, oy):
    def R(x, y, w, h, col): cv.rect(ox + x, oy + y, w, h, col)
    def S(x, y, col): cv.set(ox + x, oy + y, col)
    # hair
    R(11, 4, 10, 4, HAIR)
    R(10, 7, 2, 6, HAIR)
    R(20, 7, 2, 6, HAIR)
    R(12, 7, 8, 1, HAIR)
    R(12, 5, 4, 1, HAIR_HI)
    # face
    R(12, 8, 8, 5, SKIN)
    S(14, 10, OUT)
    S(17, 10, OUT)
    S(15, 12, RED_DK)
    S(16, 12, RED_DK)
    # neck
    R(15, 13, 2, 1, SKIN)
    # arms
    R(9, 14, 2, 4, SKIN)
    R(22, 14, 2, 4, SKIN)
    # top
    R(11, 14, 10, 5, RED)
    R(11, 16, 10, 1, WHITE)
    # pom-poms
    pom(cv, ox + 5, oy + 14)
    pom(cv, ox + 24, oy + 14)
    # skirt
    R(11, 19, 10, 1, RED)
    R(10, 20, 12, 2, RED)
    R(9, 22, 14, 1, RED)
    for px in (13, 16, 19):
        S(px, 20, WHITE); S(px, 21, WHITE); S(px, 22, WHITE)
    # legs
    R(12, 23, 2, 2, SKIN)
    R(18, 23, 2, 2, SKIN)
    R(12, 25, 2, 2, WHITE)
    R(18, 25, 2, 2, WHITE)
    R(11, 27, 3, 2, SHOE)
    R(18, 27, 3, 2, SHOE)
    S(11, 28, RED); S(13, 28, RED)
    S(18, 28, RED); S(20, 28, RED)


def back(cv, ox, oy):
    def R(x, y, w, h, col): cv.rect(ox + x, oy + y, w, h, col)
    def S(x, y, col): cv.set(ox + x, oy + y, col)
    # hair (back of head)
    R(11, 4, 10, 9, HAIR)
    R(10, 7, 1, 6, HAIR)
    R(21, 7, 1, 6, HAIR)
    R(12, 5, 4, 1, HAIR_HI)
    # arms
    R(9, 14, 2, 4, SKIN)
    R(22, 14, 2, 4, SKIN)
    # top
    R(11, 14, 10, 5, RED)
    R(11, 16, 10, 1, WHITE)
    # ponytail down the back
    R(14, 13, 4, 5, HAIR)
    S(14, 18, HAIR_HI); S(17, 18, HAIR_HI)
    # pom-poms
    pom(cv, ox + 5, oy + 14)
    pom(cv, ox + 24, oy + 14)
    # skirt
    R(11, 19, 10, 1, RED)
    R(10, 20, 12, 2, RED)
    R(9, 22, 14, 1, RED)
    for px in (13, 16, 19):
        S(px, 20, WHITE); S(px, 21, WHITE); S(px, 22, WHITE)
    # legs
    R(12, 23, 2, 2, SKIN)
    R(18, 23, 2, 2, SKIN)
    R(12, 25, 2, 2, WHITE)
    R(18, 25, 2, 2, WHITE)
    R(11, 27, 3, 2, SHOE)
    R(18, 27, 3, 2, SHOE)
    S(11, 28, RED); S(13, 28, RED)
    S(18, 28, RED); S(20, 28, RED)


def side(cv, ox, oy):
    """profile facing left"""
    def R(x, y, w, h, col): cv.rect(ox + x, oy + y, w, h, col)
    def S(x, y, col): cv.set(ox + x, oy + y, col)
    # hair
    R(12, 4, 8, 3, HAIR)      # top of head
    R(18, 5, 3, 8, HAIR)      # back of head
    R(19, 13, 3, 5, HAIR)     # ponytail
    S(20, 18, HAIR_HI)
    R(13, 5, 3, 1, HAIR_HI)
    # face
    R(12, 7, 6, 5, SKIN)
    R(12, 7, 3, 1, HAIR)      # fringe
    S(11, 9, SKIN)            # nose
    S(13, 9, OUT)             # eye
    S(12, 11, RED_DK)         # mouth
    # neck
    R(15, 12, 2, 1, SKIN)
    # body
    R(13, 13, 6, 5, RED)
    R(13, 15, 2, 2, WHITE)    # chest stripe at front edge
    # arm reaching forward + pom-pom
    R(10, 15, 4, 2, SKIN)
    pom(cv, ox + 6, oy + 14)
    # skirt
    R(12, 18, 8, 1, RED)
    R(11, 19, 9, 3, RED)
    for px in (14, 17):
        S(px, 19, WHITE); S(px, 20, WHITE); S(px, 21, WHITE)
    # legs
    R(14, 22, 2, 2, SKIN)
    R(16, 22, 2, 2, SKIN)
    R(14, 24, 2, 2, WHITE)
    R(16, 24, 2, 2, WHITE)
    R(13, 26, 3, 2, SHOE)
    R(16, 26, 3, 2, SHOE)
    S(13, 27, RED); S(16, 27, RED)


# build each view on its own 32x32 layer
front(c, 0, 0)
back(c, 32, 0)
side(c, 0, 32)

# right side = mirrored left side
tmp = new_canvas(32, 32, background=None, name="side_tmp")
side(tmp, 0, 0)
tmp.mirror("h")
c.blit(tmp, 32, 32)

# dark outline around every silhouette
c.outline(OUT)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
