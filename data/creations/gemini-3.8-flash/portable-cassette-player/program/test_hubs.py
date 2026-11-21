from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#18202c")

# Test 4-tooth cross:
# Left reel center (10, 16)
c.circle(10, 16, 2, "#462515")
c.set(10, 16, "#14171d") # center
c.set(10, 15, "#ffffff") # N
c.set(10, 17, "#ffffff") # S
c.set(9, 16, "#ffffff")  # W
c.set(11, 16, "#ffffff") # E

# Test 3x3 ring with black center (solid hub with teeth):
# Right reel center (20, 16)
c.circle(20, 16, 2, "#462515")
c.rect(19, 15, 3, 3, "#ffffff")
c.set(19, 15, "#462515") # cut corners
c.set(21, 15, "#462515")
c.set(19, 17, "#462515")
c.set(21, 17, "#462515")
c.set(20, 16, "#14171d") # black center hole

view(c)
