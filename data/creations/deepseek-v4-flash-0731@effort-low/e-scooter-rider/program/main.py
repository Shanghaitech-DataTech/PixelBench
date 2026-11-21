from pixelbench_api import *

c = input_canvas.copy(name="out")
c.clear()

def newcol(rgb, name):
    return c.color(rgb, name)

black = newcol('#2a2a34', 'black')
gray  = newcol('#9aa0ac', 'gray')
dark  = newcol('#525761', 'dark')
frame = newcol('#e0563f', 'frame')
skin  = newcol('#f2b98b', 'skin')
white = newcol('#f6f6f4', 'white')
blue  = newcol('#3f6fd0', 'blue')
pants = newcol('#26345f', 'pants')
shoe  = newcol('#1d1f29', 'shoe')
shadow= newcol('#9ba1ad', 'shadow')
visor = newcol('#cfe0ef', 'visor')

# ---- scooter ----
c.rect(8, 23, 16, 2, dark)          # deck
c.rect(8, 23, 16, 1, frame)         # deck top rim
c.circle(5, 25, 3, black)           # rear wheel
c.circle(26, 25, 3, black)          # front wheel
c.circle(5, 25, 1, gray)
c.circle(26, 25, 1, gray)
c.line(3, 23, 8, 23, dark)          # rear fender
c.line(24, 23, 29, 23, dark)        # front fender
c.line(24, 23, 24, 14, dark)        # stem
c.rect(19, 14, 8, 1, dark)          # handlebar
c.rect(26, 13, 3, 3, black)         # grip
# ---- rider (leaning forward, riding right) ----
c.line(15, 19, 13, 22, pants)       # rear leg
c.line(16, 20, 17, 22, pants)       # front leg
c.rect(10, 22, 3, 2, shoe)
c.rect(16, 22, 3, 2, shoe)
c.poly([(16,14),(19,14),(15,20),(13,20)], blue)   # torso
c.line(18, 13, 21, 14, blue)        # far arm
c.line(19, 14, 23, 15, blue)        # near arm
c.circle(23, 15, 1, skin)           # hand on grip
c.circle(18, 10, 2, skin)           # head
c.circle(18, 7, 2, frame)           # helmet
c.line(16, 8, 20, 8, white)         # helmet stripe
c.circle(19, 10, 1, visor)          # visor
c.circle(5, 29, 1, shadow)
c.circle(26, 29, 1, shadow)

finish(c)
