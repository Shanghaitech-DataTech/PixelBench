from pixelbench_api import new_canvas, finish, canvas

c = new_canvas(64, 64)

OUT = '#3a2416'      # dark outline brown-black
RUG = '#c66b4c'      # terracotta rug
RUG2 = '#d37a58'     # rug inner
WOOD = '#c99a61'     # tabletop light wood
WOODD = '#a5753c'    # wood dark shade / grain
WOODL = '#e0b87d'    # wood highlight
BACK = '#7a4e2b'     # chair back
CUSH = '#5d3a22'     # chair cushion
BOWL = '#ded8d1'     # light ceramic bowl
BOWLD = '#bfb8ae'
FR_R = '#d32f2f'
FR_G = '#55a53a'
FR_O = '#e89323'
FR_Y = '#f0d43a'
FR_L = '#2e7d32'

# Rug: dark ring then rug
c.ellipse(32, 32, 29, 29, OUT)
c.ellipse(32, 32, 27, 27, RUG)
c.ellipse(32, 32, 23, 23, RUG2)
# rug inner decorative band
c.ellipse(32, 32, 18, 18, RUG)

# Chairs (behind/around table)
# top chair
c.rect(25, 10, 14, 6, OUT); c.rect(26, 11, 12, 4, BACK)
c.rect(25, 16, 14, 8, OUT); c.rect(26, 17, 5, 6, CUSH); c.rect(34, 17, 5, 6, CUSH)
# bottom chair
c.rect(25, 49, 14, 6, OUT); c.rect(26, 50, 12, 4, BACK)
c.rect(25, 41, 14, 8, OUT); c.rect(26, 42, 12, 6, CUSH)
# left chair
c.rect(6, 26, 6, 12, OUT); c.rect(7, 27, 4, 10, BACK)
c.rect(12, 26, 8, 12, OUT); c.rect(13, 27, 6, 10, CUSH)
# right chair
c.rect(52, 26, 6, 12, OUT); c.rect(53, 27, 4, 10, BACK)
c.rect(44, 26, 8, 12, OUT); c.rect(45, 27, 6, 10, CUSH)

# Table: dark outline oval then wood top
c.ellipse(32, 33, 21, 12, OUT)
c.ellipse(32, 33, 19, 10, WOOD)
c.ellipse(32, 33, 12, 6, WOODL)
# wood grain lines
c.line(16, 28, 22, 27, WOODD)
c.line(42, 27, 48, 28, WOODD)
c.line(20, 38, 26, 39, WOODD)
c.line(38, 39, 44, 38, WOODD)
c.line(32, 23, 32, 25, WOODD)
c.line(12, 33, 15, 33, WOODD)
c.line(49, 33, 52, 33, WOODD)

# Center bowl of fruit
c.circle(32, 33, 7, OUT)
c.circle(32, 33, 6, BOWL)
c.circle(32, 33, 4, BOWLD)

def fruit(x, y, col, r=2):
    c.circle(x, y, r, OUT)
    c.circle(x, y, r - 1, col)

fruit(28, 30, FR_R, 3)   # apple
fruit(36, 31, FR_O, 3)   # orange
fruit(33, 37, FR_R, 3)   # apple
fruit(29, 36, FR_G, 2)   # green apple
fruit(37, 35, FR_G, 2)   # grape cluster
fruit(32, 30, FR_Y, 2)   # lemon
fruit(31, 33, FR_L, 1)

finish(c)
