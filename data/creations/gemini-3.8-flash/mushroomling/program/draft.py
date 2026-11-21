# Experiment with layouts
c = new_canvas(16, 16)

# Palette test:
# 0: outline: #23121e (dark purple-brown)
# 1: red cap: #dc2626 (or #e12c2c)
# 2: white: #ffffff (or #fbf8f0)
# 3: tan: #e8be88 (or #f0ca9c)

DARK = "#22121e"
RED = "#dc2626"
WHITE = "#ffffff"
TAN = "#f0ca9c"

# Let's sketch a grid as text:
# . = transparent
# D = DARK
# R = RED
# W = WHITE
# T = TAN

grid = [
    "................", # 0
    ".....DDDDDD.....", # 1  cap top outline
    "...DDERRRREDD...", # 2  wait, let's use exact letters
]
