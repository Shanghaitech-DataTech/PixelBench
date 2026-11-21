from pixelbench_api import *

OUTLINE = '#23213a'
W = H = 64

# ---- Fireball (top-left) ----
fb = new_canvas(32, 32, name="fireball")
# ball core
fb.circle(16, 15, 8, '#e63946')      # red
fb.circle(16, 15, 6, '#f77f00')      # orange
fb.circle(16, 15, 4, '#fcbf49')      # yellow
fb.circle(15, 14, 2, '#fff3b0')      # cream core
# flame tail (three non-crossing shapes that tile)
fb.poly([(15,20),(19,20),(16,26),(15,30),(14,26)], '#f77f00')
fb.poly([(14,22),(12,25),(15,25)], '#f77f00')
fb.poly([(17,22),(18,25),(20,25)], '#f77f00')
# inner flame highlights
fb.line(15,22,16,25, '#fcbf49')
# small sparks around the ball
fb.set(5,12, '#f77f00').set(23,5, '#f77f00').set(26,9, '#fcbf49').set(26,16, '#f77f00')
fb.outline(OUTLINE)

# ---- Ice shield (top-right) ----
sh = new_canvas(32, 32, name="iceshield")
sh.poly([(16,2),(24,5),(26,12),(26,18),(22,23),(16,29),(10,23),(6,18),(6,12),(8,5)], '#48cae4')
sh.poly([(16,6),(21,8),(22,13),(22,18),(19,22),(16,26),(13,22),(10,18),(10,13),(11,8)], '#a8dadc')
sh.line(16,11,16,21,'#f1faee')
sh.line(12,15,20,15,'#f1faee')
sh.line(13,12,19,18,'#f1faee')
sh.line(19,12,13,18,'#f1faee')
sh.set(16,16,'#0077b6')
sh.outline(OUTLINE)

# ---- Healing (bottom-left) ----
he = new_canvas(32, 32, name="healing")
he.circle(11,13,6,'#e63946')
he.circle(21,13,6,'#e63946')
he.poly([(7,16),(16,28),(25,16)], '#e63946')
he.rect(14,12,4,2,'#ffffff')
he.rect(15,10,2,6,'#ffffff')
he.circle(9,10,2,'#ffb3c1')
he.outline(OUTLINE)
he.set(25,7,'#ffffff')

# ---- Lightning (bottom-right) ----
li = new_canvas(32, 32, name="lightning")
# solid bolt as two overlapping non-crossing shapes (same colour)
li.poly([(21,1),(15,11),(20,11),(26,1)], '#ffca3a')   # upper band
li.poly([(14,11),(15,27),(23,14),(19,11)], '#ffca3a') # lower band
# highlights
li.line(21,4,17,9, '#ffe08a')
li.line(19,14,16,22, '#ffe08a')
li.set(8,10, '#ffca3a').set(25,5, '#ffca3a')
li.outline(OUTLINE)

# ---- Compose 2x2 grid ----
result = new_canvas(W, H, name="skill-icons")
result.blit(fb, 0, 0)
result.blit(sh, 32, 0)
result.blit(he, 0, 32)
result.blit(li, 32, 32)

print(result.stats_text())
for c, nm in [(fb,'fireball'),(sh,'iceshield'),(he,'healing'),(li,'lightning')]:
    print('===', nm, c.stats_text())
    print(c.matrix_text())

finish(result)
