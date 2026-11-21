from pixelbench_api import *

c = new_canvas(16, 16, background=None, name="researcher")

WHITE = c.color("#f2f2f2", "coat")
SHAD  = c.color("#c9ccd4", "coat_shadow")
HAIR  = c.color("#26222b", "hair")
HAIRH = c.color("#4a4453", "hair_hi")
SKIN  = c.color("#f5cfa8", "skin")
EYE   = c.color("#6b4326", "eye_brown")
MOUTH = c.color("#a05a4a", "mouth")
BLUE  = c.color("#3f5d8c", "skirt")
SHOE  = c.color("#3a3a42", "shoes")

# Head (rows 1-8), big chibi head
c.rect(4, 1, 8, 2, HAIR)
c.rect(3, 2, 10, 3, HAIR)
c.rect(3, 5, 2, 3, HAIR)
c.rect(11, 5, 2, 3, HAIR)
c.rect(3, 7, 1, 2, HAIR)
c.rect(12, 7, 1, 2, HAIR)
c.rect(5, 8, 1, 2, HAIR)
c.rect(10, 8, 1, 2, HAIR)
c.set(4, 2, HAIRH); c.set(6, 1, HAIRH); c.set(8, 1, HAIRH)
# face
c.rect(5, 5, 6, 3, SKIN)
c.rect(5, 8, 1, 1, SKIN); c.rect(10, 8, 1, 1, SKIN)
c.set(6, 8, SKIN); c.set(9, 8, SKIN)
# eyes + mouth
c.set(6, 6, EYE); c.set(9, 6, EYE)
c.set(7, 8, MOUTH)

# Body (rows 10-13): white lab coat
c.rect(4, 10, 8, 4, WHITE)
c.rect(5, 10, 1, 4, SHAD)
c.rect(3, 10, 1, 3, WHITE)
c.rect(12, 10, 1, 3, WHITE)
c.set(3, 13, SKIN); c.set(12, 13, SKIN)
c.set(6, 10, SHAD); c.set(9, 10, SHAD)
c.set(7, 10, SKIN); c.set(8, 10, SKIN)
# skirt under coat
c.rect(5, 13, 6, 1, BLUE)
# legs & shoes
c.rect(6, 14, 1, 1, SKIN)
c.rect(9, 14, 1, 1, SKIN)
c.rect(5, 15, 2, 1, SHOE)
c.rect(9, 15, 2, 1, SHOE)

print(c.stats_text())
finish(c)
