from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#18202c")

# Base cassette window
c.rect(8, 12, 14, 10, "#dcd5c7")
c.rect(9, 13, 12, 2, "#f4f0e6")
c.line(9, 13, 20, 13, "#d9431e")
c.rect(9, 15, 12, 4, "#14171d")
c.circle(11, 16, 2, "#462515")
c.circle(18, 16, 1, "#462515")

# Hub teeth
c.set(11, 16, "#14171d")
c.set(11, 15, "#ffffff")
c.set(10, 17, "#ffffff")
c.set(12, 17, "#ffffff")

c.set(18, 16, "#14171d")
c.set(18, 15, "#ffffff")
c.set(17, 17, "#ffffff")
c.set(19, 17, "#ffffff")

# Glass reflection layer
glass = new_canvas(32, 32)
# Draw semi-transparent diagonal streaks
glass.line(10, 12, 14, 16, "#ffffff40")
glass.line(11, 12, 15, 16, "#ffffff25")
glass.line(16, 12, 19, 15, "#ffffff40")

result = flatten([c, glass])
view(result)
