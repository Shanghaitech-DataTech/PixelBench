from pixelbench_api import *

c = new_canvas(64, 64)

# Let's draw a subtle visual grid separator or just keep transparent background?
# Prompt says: "transparent background", "2x2 grid", "sword, bow, shield, battle axe"
# "transparent background" means fully transparent background!
# The 2x2 grid is the arrangement of the 4 weapon icons in four quadrants.

# Let's test a simple layout first to verify execution
print("Testing environment...")
view(c)
