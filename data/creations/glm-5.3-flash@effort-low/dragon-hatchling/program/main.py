from pixelbench_api import *

c = new_canvas(64, 64, name="dragon")

OUT    = '#1a1218'
BODY   = '#a83a2a'
BODY_D = '#70241a'
BELLY  = '#e2c493'
BELLY_D= '#b3926a'
WING   = '#8c2c20'
WING_D = '#501610'
HORN   = '#e9e0c4'
EYE    = '#ffd23f'
MOUTH  = '#2a0c0c'
TEETH  = '#f4f0e0'
SPIKE  = '#cfc4a2'

# ---- far wing (right, behind body) ----
c.poly([(40,30),(50,12),(59,6),(56,16),(61,24),(52,30),(46,36)], WING_D)
c.line(50,13,47,30, '#3a0e0a')
c.line(58,8,53,26, '#3a0e0a')

# ---- tail (spiked, curving right-down) ----
c.poly([(42,40),(50,42),(57,47),(63,54),(60,58),(53,52),(46,47),(40,45)], BODY)
c.poly([(50,41),(54,43),(51,45)], SPIKE)   # tail spikes
c.poly([(57,46),(60,49),(56,50)], SPIKE)
c.poly([(62,53),(63,57),(59,55)], SPIKE)

# ---- body ----
c.ellipse(34,38,11,9, BODY)
c.ellipse(32,42,8,6, BELLY)          # pale belly
c.line(26,41,39,40, BELLY_D)
c.line(26,44,39,44, BELLY_D)
c.line(27,47,37,47, BELLY_D)

# ---- legs ----
c.rect(26,44,5,10, BODY)             # front leg
c.rect(24,53,8,4, BODY)
c.rect(40,44,6,9, BODY)              # hind leg
c.rect(39,52,9,4, BODY)
c.set(24,55,HORN); c.set(26,56,HORN); c.set(39,55,HORN); c.set(42,56,HORN)

# ---- neck ----
c.poly([(23,24),(33,26),(35,34),(26,34)], BODY)

# ---- head ----
c.circle(22,23,7, BODY)
c.rect(10,21,13,7, BODY)             # snout / upper jaw
c.set(10,21,BODY); c.set(9,22,BODY); c.set(9,23,BODY)
# open mouth interior
c.poly([(10,28),(23,28),(24,33),(11,32)], MOUTH)
# lower jaw (dropped, growling)
c.poly([(9,32),(23,35),(25,31),(11,30)], BODY)
# teeth
for x in (11,13,15,17,19,21):
    c.set(x,28,TEETH)
c.set(12,32,TEETH); c.set(15,33,TEETH); c.set(18,33,TEETH)
# nostril
c.set(11,23,BODY_D)

# ---- horns ----
c.poly([(19,16),(21,9),(23,16)], HORN)
c.poly([(25,17),(28,11),(29,18)], HORN)

# ---- eye (fierce) ----
c.rect(19,21,3,2, EYE)
c.set(20,21,OUT)

# ---- near wing (left, in front) ----
c.poly([(27,28),(15,9),(5,5),(10,16),(2,21),(13,27),(20,34)], WING)
c.line(16,10,22,28, WING_D)
c.line(8,7,18,26, WING_D)
c.line(4,20,18,30, WING_D)

# ---- silhouette outline ----
c.outline(OUT)

print(c.stats_text())
save("dragon_hatchling", c)
finish(c)
