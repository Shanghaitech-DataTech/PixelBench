from pixelbench_api import *

# Let's check how the sprite looks on a dark background
test_dark = new_canvas(16, 16, background='#1a1a24')
# We will composite our canvas onto test_dark
# But first let's see stats and colors of our canvas
from main import c, C

test_dark.blit(c, 0, 0)
view(test_dark)
