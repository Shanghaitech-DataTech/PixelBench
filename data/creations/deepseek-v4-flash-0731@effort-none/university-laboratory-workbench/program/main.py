# Laboratory workbench at 64x64
# Microscope, test-tube rack, dropper, labeled bottles, open notebook

W, H = 64, 64
c = new_canvas(W, H, background=(0,0,0,255))

# Colors
WHITE    = (240,240,240,255)
BROWN    = (120,80,40,255)
DARKBRN  = (80,50,20,255)
GRAY     = (160,160,160,255)
DKGRAY   = (90,90,90,255)
LIGHT    = (220,220,220,255)
GLASS    = (200,220,240,255)
REDLIQ   = (200,80,60,255)
GREENLIQ = (70,170,90,255)
YELLOWQ  = (220,200,80,255)
BLUELIQ  = (70,120,210,255)
ORANGEQ  = (230,150,50,255)
PAPER    = (235,230,210,255)
INK      = (40,40,90,255)
WOODL    = (150,105,55,255)
WOODD    = (95,65,35,255)
PLASTICW = (250,250,250,255)
PLASTICB = (60,60,90,255)
DRKPLAS  = (100,100,120,255)
RUBBER   = (60,60,60,255)
PAPERGRAY= (200,195,175,255)
PURPLEQ  = (150,90,180,255)

# Background wall
c.rect(0, 0, 64, 38, (95,100,110,255), fill=True)

# Table
c.rect(0, 38, 64, 26, BROWN, fill=True)
c.rect(0, 38, 64, 2, WOODL, fill=True)
c.rect(0, 54, 64, 10, DARKBRN, fill=True)

# ============ MICROSCOPE ============
# Base
c.rect(3, 35, 24, 3, DKGRAY, fill=True)
c.rect(4, 34, 22, 2, GRAY, fill=True)
# Column
c.rect(9, 14, 5, 20, GRAY, fill=True)
# Arm
c.rect(8, 11, 7, 5, DKGRAY, fill=True)
# Eyepiece
c.rect(10, 6, 5, 6, DKGRAY, fill=True)
c.rect(9, 6, 7, 2, GRAY, fill=True)
# Body tube
c.rect(10, 12, 5, 12, DKGRAY, fill=True)
# Objective head
c.rect(9, 24, 7, 2, GRAY, fill=True)
# Stage
c.rect(5, 28, 20, 2, LIGHT, fill=True)
# Focus knobs
c.rect(4, 18, 5, 5, DKGRAY, fill=True)
# Small objective under stage
c.rect(11, 26, 3, 2, DKGRAY, fill=True)

# ============ DROPPER ============
# Glass stem
c.rect(26, 16, 4, 21, GLASS, fill=True)
c.rect(27, 17, 1, 19, WHITE, fill=True)
# Rubber bulb
c.circle(28, 12, 4, RUBBER, fill=True)

# ============ TEST TUBE RACK ============
# Frame
c.rect(35, 18, 25, 3, WOODD, fill=True)
c.rect(35, 32, 25, 3, WOODD, fill=True)
c.rect(34, 16, 3, 21, WOODD, fill=True)
c.rect(58, 16, 3, 21, WOODD, fill=True)
c.rect(34, 37, 3, 2, WOODD, fill=True)
c.rect(58, 37, 3, 2, WOODD, fill=True)
c.rect(35, 18, 25, 1, WOODL, fill=True)
c.rect(35, 32, 25, 1, WOODL, fill=True)
c.rect(34, 16, 1, 21, WOODL, fill=True)

# Tubes
# Red tube
c.rect(38, 13, 5, 18, GLASS, fill=True)
c.rect(38, 27, 5, 6, REDLIQ, fill=True)
c.rect(38, 27, 5, 1, WHITE, fill=True)
c.rect(39, 14, 1, 16, WHITE, fill=True)
# Green tube
c.rect(45, 11, 5, 20, GLASS, fill=True)
c.rect(45, 27, 5, 6, GREENLIQ, fill=True)
c.rect(45, 27, 5, 1, WHITE, fill=True)
c.rect(46, 12, 1, 17, WHITE, fill=True)
# Blue tube (tallest)
c.rect(52, 9, 5, 22, GLASS, fill=True)
c.rect(52, 28, 5, 6, BLUELIQ, fill=True)
c.rect(52, 28, 5, 1, WHITE, fill=True)
c.rect(53, 10, 1, 20, WHITE, fill=True)

# Middle rack rails
c.rect(35, 21, 25, 1, WOODD, fill=True)
c.rect(35, 34, 25, 1, WOODD, fill=True)

# ============ LABELED BOTTLES ============
# White bottle
c.rect(36, 42, 9, 12, PLASTICW, fill=True)
c.rect(36, 42, 9, 3, DRKPLAS, fill=True)
c.rect(37, 45, 7, 1, LIGHT, fill=True)
# Label
c.rect(37, 47, 7, 5, PAPER, fill=True)
c.rect(39, 49, 4, 1, INK, fill=True)
c.rect(39, 51, 3, 1, INK, fill=True)

# Dark blue bottle
c.rect(48, 44, 6, 10, PLASTICB, fill=True)
c.rect(48, 44, 6, 2, DRKPLAS, fill=True)
c.rect(49, 49, 4, 4, PAPER, fill=True)
c.rect(50, 50, 2, 1, INK, fill=True)

# ============ OPEN NOTEBOOK ============
c.rect(2, 42, 17, 12, PAPER, fill=True)
c.rect(4, 42, 2, 12, PAPERGRAY, fill=True)
c.rect(5, 42, 1, 12, (150,140,110,255), fill=True)
# Text marks
for i in range(4):
    c.rect(7, 45+i*3, 6, 1, INK, fill=True)
# Sketch
c.rect(14, 44, 4, 1, INK, fill=True)
c.rect(14, 44, 1, 5, INK, fill=True)
c.rect(17, 44, 1, 3, INK, fill=True)
c.rect(14, 48, 1, 4, INK, fill=True)

# ============ BEAKER ============
c.rect(26, 44, 7, 9, GLASS, fill=True)
c.rect(26, 44, 7, 1, WHITE, fill=True)
c.rect(27, 45, 5, 7, ORANGEQ, fill=True)
c.rect(27, 46, 1, 5, WHITE, fill=True)

# ============ WALL SHELF with small flasks ============
c.rect(14, 4, 42, 1, (110,115,125,255), fill=True)
# Flask 1 (left of dropper)
c.circle(21, 3, 3, GLASS, fill=True)
c.circle(21, 3, 3, GLASS, fill=False)
c.rect(20, 3, 2, 2, GLASS, fill=True)
c.rect(20, 3, 2, 1, PURPLEQ, fill=True)
c.rect(21, 5, 1, 1, GLASS, fill=True)
# Flask 2 (right of dropper)
c.circle(44, 3, 3, GLASS, fill=True)
c.circle(44, 3, 3, GLASS, fill=False)
c.rect(43, 3, 2, 2, GLASS, fill=True)
c.rect(43, 3, 2, 1, YELLOWQ, fill=True)
c.rect(44, 5, 1, 1, GLASS, fill=True)

# ============ Table shadow ============
c.rect(0, 52, 64, 1, (70,45,20,255), fill=True)

result = c
finish(result)
