from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#18202c")

# Cassette window frame: x = 7 to 22, y = 11 to 21
# Outer silver frame
c.rect(7, 11, 16, 11, "#505763")
c.rect(8, 11, 14, 11, "#2e343d")
c.line(8, 11, 21, 11, "#7d8794")
c.line(8, 11, 8, 21, "#7d8794")

# Inside window: x = 8 to 21, y = 12 to 21
# Background of cassette compartment
c.rect(8, 12, 14, 10, "#0e1117")

# Cassette Shell: Cream / Light Grey
# Width 14, height 10: x=8..21, y=12..21
c.rect(8, 12, 14, 10, "#dcd5c7")
# Shell outline / shading
c.line(8, 12, 21, 12, "#aba294")
c.set(8, 12, "#0e1117")
c.set(21, 12, "#0e1117")

# Label: y = 13..14
c.rect(9, 13, 12, 2, "#f4f0e6")
# Orange/Red vintage label stripe: y=13
c.line(9, 13, 20, 13, "#d9431e")
# Dark line below label
c.line(9, 14, 20, 14, "#44403a")
# Little text marks on label
c.set(10, 14, "#8a8275")
c.set(12, 14, "#8a8275")
c.set(14, 14, "#8a8275")
c.set(18, 14, "#d9431e") # "A" side marker

# Cassette Center Cutout (where tape is visible):
# x = 9 to 20, y = 15 to 18 (4 px tall)
c.rect(9, 15, 12, 4, "#14171d")

# Tape between reels:
# Left Reel center at (11, 16)
# Brown tape spool (lots of tape on left):
c.rect(9, 15, 5, 4, "#462515")
c.set(9, 15, "#14171d")
c.set(13, 15, "#14171d")
c.set(9, 18, "#14171d")
c.set(13, 18, "#14171d")

# Left Hub: white plastic teeth
c.set(11, 16, "#14171d") # center hole
c.set(11, 15, "#ffffff") # top tooth
c.set(10, 17, "#ffffff") # bottom-left tooth
c.set(12, 17, "#ffffff") # bottom-right tooth

# Right Reel center at (18, 16)
# Less tape (thin brown ring around hub):
c.rect(16, 15, 5, 4, "#14171d")
c.circle(18, 16, 1, "#462515")
# Right Hub:
c.set(18, 16, "#14171d")
c.set(18, 15, "#ffffff")
c.set(17, 17, "#ffffff")
c.set(19, 17, "#ffffff")

# Center tape counter / tick marks in cassette middle window (x = 14..15):
c.set(14, 16, "#3a404a")
c.set(15, 16, "#3a404a")
c.line(13, 18, 17, 18, "#5a321a") # tape passing under bridge

# Bottom trapezoid / head area: y = 19..20
# Outer shell bottom
c.rect(8, 19, 14, 3, "#dcd5c7")
c.line(8, 21, 21, 21, "#aba294")
# Trapezoid cutout: y=19 (x=11..18), y=20 (x=12..17)
c.line(11, 19, 18, 19, "#3a2012")
c.line(12, 20, 17, 20, "#26150b")
# Guide rollers
c.set(12, 19, "#c29b4b") # bronze/brass guide roller
c.set(17, 19, "#c29b4b")

# Glass reflection highlight (transparent window effect):
# A clean diagonal reflection line across the glass
c.set(9, 12, "#ffffff")
c.set(10, 13, "#ffffff")
c.set(11, 14, "#92c2e0")
c.set(12, 15, "#92c2e0")

c.set(15, 12, "#92c2e0")
c.set(16, 13, "#ffffff")
c.set(17, 14, "#ffffff")
c.set(18, 15, "#92c2e0")

view(c)
