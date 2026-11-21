# University laboratory workbench - 64x64 pixel art
# Objects: microscope, test-tube rack, dropper, labeled bottles, open notebook

# ---- palette ----
WALL='#a9b8c2'
PFRAME='#8a6b4a'; PBG='#f2f0ea'
CR='#d98880'; CB='#7fb0d9'; CG='#8fd98c'; CY='#e8d96f'; CP='#c39bd3'
BTOP='#caa06a'; BHI='#e0bd85'; BSH='#a37f4e'; SEAM='#7d5a33'; FRONT='#96683a'; FRD='#7d532b'
SD='#39404c'; SM='#556070'; SL='#8e99a8'; SIL='#cdd3da'; LENS='#57a8cc'; KNOB='#6b7684'
GL='#d5edf0'; GLH='#ffffff'; GLS='#a9cfd6'
LR='#d94a4a'; LB='#3f7fd9'; LG='#45b06c'; LY='#e3c832'
RK='#4a5560'; RKH='#6a7885'
BG='#3e8b5e'; BGD='#2c6443'; BGL='#6fb98b'
AM='#c07a28'; AMD='#8a5418'; AML='#e2a554'
JAR='#a9cdd8'; JARD='#7fa6b3'
CAP='#333944'; BULB='#b03a3a'; BULBL='#d96a5a'
LAB='#f4efe2'; LABL='#6d6d6d'
PAP='#f7f2e4'; LN='#9aa2ab'; COV='#3d5a8c'; COVD='#2c4168'

c = new_canvas(64, 64, WALL, name='lab_workbench')

# ---- wall poster: periodic table (reads by grid shape) ----
c.rect(43, 2, 20, 14, PFRAME)
c.rect(44, 3, 18, 12, PBG)
for x, y, col in [(45,4,CR),(57,4,CP),
                  (45,7,CB),(48,7,CG),(54,7,CY),(57,7,CB),
                  (45,10,CY),(48,10,CR),(51,10,CG),(54,10,CB),(57,10,CG)]:
    c.rect(x, y, 2, 2, col)
c.rect(46, 13, 9, 1, LN)

# ---- wall clock ----
c.circle(31, 9, 5, PFRAME)
c.circle(31, 9, 4, PBG)
c.set(31, 5, SD)                # 12-o'clock tick
c.set(31, 9, SD); c.set(31, 8, SD); c.set(31, 7, SD)   # hour hand
c.set(32, 9, SD); c.set(33, 9, SD)                     # minute hand

# ---- bench ----
c.rect(0, 31, 64, 22, BTOP)     # top surface y31-52
c.rect(0, 31, 64, 1, BHI)       # back edge highlight
c.rect(0, 53, 64, 1, SEAM)
c.rect(0, 54, 64, 10, FRONT)    # front face y54-63
c.rect(0, 60, 64, 4, FRD)
c.rect(21, 55, 1, 8, FRD)       # cabinet seams
c.rect(43, 55, 1, 8, FRD)

# ---- soft shadows on bench top ----
c.rect(4, 47, 13, 1, BSH)       # under microscope
c.rect(22, 46, 18, 1, BSH)      # under rack
c.rect(44, 46, 20, 1, BSH)      # under bottles
c.rect(19, 53, 25, 1, FRD)      # under notebook

# ---- microscope (left) ----
c.rect(5, 22, 4, 21, SD)        # arm column x5-8 y22-42
c.rect(5, 24, 1, 17, SM)        # arm highlight
c.rect(9, 20, 3, 3, SD)         # arm-to-tube joint
c.rect(10, 14, 4, 17, SD)       # body tube y14-30
c.rect(10, 15, 1, 14, SM)       # tube highlight
c.rect(11, 10, 2, 4, SD)        # eyepiece
c.rect(11, 10, 2, 1, SIL)       # eyepiece rim
c.rect(10, 31, 4, 2, SM)        # revolving nosepiece
c.rect(9, 34, 6, 1, GL)         # slide
c.rect(7, 35, 10, 2, SD)        # stage
for px in (10, 12):             # objective lenses
    c.set(px, 33, SIL); c.set(px, 34, SIL)
c.set(9, 33, SM)                # nosepiece side
c.circle(4, 36, 2, KNOB)        # focus knob
c.set(3, 35, SL)
c.rect(10, 38, 3, 3, SM)        # illuminator
c.set(11, 39, LENS)
c.rect(11, 41, 1, 2, SM)        # lamp post
c.set(8, 40, SM)                # arm-to-base brace
c.rect(5, 43, 10, 2, SD)        # base upper step
c.rect(4, 45, 12, 2, SD)        # base foot
c.rect(5, 43, 10, 1, SM)        # base top highlight

# ---- test-tube rack (center-left) ----
tubes = [(23, LR, 32), (27, LB, 34), (31, LG, 30), (35, LY, 35)]
for x, liq, lt in tubes:
    c.rect(x, 27, 3, 1, GLH)          # rim
    c.rect(x, 28, 3, 14, GL)          # glass body y28-41
    c.rect(x + 2, 28, 1, 13, GLS)     # right glass shade
    c.rect(x, 29, 1, 10, GLH)         # left highlight
    c.rect(x + 1, lt, 1, 42 - lt, liq)  # liquid column
    c.set(x, 42, GL); c.set(x + 2, 42, GL)   # rounded bottom
    c.set(x + 1, 42, liq); c.set(x + 1, 43, liq)
c.rect(21, 36, 20, 2, RK)       # top rail
c.rect(21, 36, 20, 1, RKH)
c.rect(21, 44, 20, 2, RK)       # bottom rail
c.rect(21, 44, 20, 1, RKH)
c.rect(21, 36, 2, 10, RK)       # side posts
c.rect(39, 36, 2, 10, RK)

# ---- labeled bottles (right) ----
# tall green reagent bottle
c.rect(45, 17, 5, 3, BULB)      # red cap
c.set(45, 17, BULBL)
c.rect(46, 20, 3, 4, BG)        # neck
c.set(46, 21, BGL)
c.set(45, 23, BG); c.set(49, 23, BG)  # shoulder slope
c.rect(44, 24, 7, 22, BG)       # body y24-45
c.rect(44, 25, 1, 20, BGD)
c.rect(50, 25, 1, 20, BGL)
c.rect(45, 26, 1, 4, BGL)       # shine
c.rect(45, 31, 5, 8, LAB)       # label
c.rect(46, 33, 3, 1, LABL)
c.rect(46, 35, 3, 1, LABL)
c.rect(46, 37, 2, 1, LABL)
# amber bottle
c.rect(53, 26, 4, 2, CAP)       # dark cap
c.rect(54, 28, 2, 3, AM)        # neck
c.set(54, 29, AML)
c.rect(53, 31, 4, 1, AM)        # shoulder
c.rect(52, 32, 6, 14, AM)       # body y32-45
c.rect(52, 33, 1, 12, AMD)
c.rect(57, 33, 1, 12, AML)
c.rect(53, 36, 4, 5, LAB)       # label
c.rect(54, 38, 2, 1, LABL)
# small jar with lid
c.rect(58, 36, 6, 2, RK)        # lid
c.rect(58, 36, 6, 1, RKH)
c.rect(59, 38, 5, 8, JAR)       # body y38-45
c.rect(59, 39, 1, 6, JARD)
c.rect(63, 39, 1, 5, GLH)
c.rect(60, 40, 3, 3, LAB)       # label
c.rect(60, 41, 3, 1, LABL)

# ---- open laboratory notebook (front center) ----
c.rect(19, 46, 25, 7, COV)      # cover y46-52
c.rect(20, 47, 11, 5, PAP)      # left page
c.rect(32, 47, 11, 5, PAP)      # right page
c.rect(31, 47, 1, 5, COVD)      # spine
c.rect(19, 52, 25, 1, COVD)     # bottom cover edge
c.rect(21, 47, 1, 5, LR)        # red margin line
c.rect(23, 48, 7, 1, LN)        # writing lines (left page)
c.rect(23, 49, 6, 1, LN)
c.rect(23, 50, 7, 1, LN)
c.rect(34, 48, 8, 1, LN)        # writing lines (right page)
c.rect(34, 49, 7, 1, LN)
c.rect(34, 50, 5, 1, LR)        # highlighted result line
c.set(31, 47, SIL); c.set(31, 49, SIL); c.set(31, 51, SIL)  # spiral rings

# ---- dropper (front right, lying on bench) ----
c.rect(48, 49, 8, 1, GL)        # glass tube top
c.rect(48, 50, 9, 1, LB)        # liquid inside
c.rect(48, 51, 9, 1, GLS)       # glass tube bottom
c.rect(44, 50, 4, 1, GL)        # nozzle
c.set(44, 51, LB)               # droplet
c.circle(60, 50, 2, BULB)       # rubber bulb
c.set(59, 49, BULBL)

print(c.stats_text())
view(c)
finish(c)
