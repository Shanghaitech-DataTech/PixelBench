from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

def col(spec):
    return c.color(spec)

BLACK = col((18, 18, 26))
DARKG = col((55, 55, 66))
GRAY = col((140, 140, 150))
LGRAY = col((205, 205, 215))
SKIN = col((242, 192, 148))
SKIND = col((208, 152, 110))
HEL = col((248, 248, 252))
HELD = col((90, 120, 200))
RED = col((206, 60, 56))
BLU = col((58, 58, 150))
SHOE = col((32, 32, 42))
SHAD = col((70, 70, 80, 70))

# ground shadow
c.ellipse(16, 28, 12, 2, SHAD)

# wheels (rear + front), rider rides to the right
c.circle(9, 24, 3, DARKG)
c.circle(9, 24, 1, LGRAY)
c.circle(24, 24, 3, DARKG)
c.circle(24, 24, 1, LGRAY)

# deck + fenders
c.rect(6, 24, 12, 2, GRAY)
c.rect(6, 24, 12, 1, LGRAY)
c.rect(8, 20, 4, 2, DARKG)
c.rect(22, 20, 4, 2, DARKG)

# stem + handlebar
c.line(16, 24, 19, 11, DARKG)
c.line(17, 24, 20, 11, DARKG)
c.rect(17, 10, 9, 1, BLACK)
c.rect(15, 10, 3, 2, BLACK)
c.rect(24, 10, 3, 2, BLACK)

# rider legs + shoes (standing on the deck)
c.rect(10, 16, 2, 6, BLU)
c.rect(13, 16, 2, 6, BLU)
c.rect(9, 23, 3, 2, SHOE)
c.rect(13, 23, 3, 2, SHOE)

# torso leaning forward
c.poly([(11, 16), (17, 10), (19, 12), (13, 18)], RED)

# arm reaching to the handlebar + hand
c.line(18, 11, 24, 11, RED)
c.rect(23, 10, 3, 2, SKIN)

# head + helmet (open-face, facing right)
c.circle(18, 6, 3, HEL)
c.rect(20, 4, 2, 2, HELD)      # visor
c.rect(20, 7, 3, 2, SKIN)      # face
c.rect(18, 9, 2, 2, SKIN)      # neck

print(c.stats_text())
print(c.matrix_text())

finish(c)
