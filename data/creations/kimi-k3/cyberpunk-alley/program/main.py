# cyberpunk-alley: 128x128 rainy neon alley, one-point perspective
# Palette (kept well under 86 visible colours)

SKY      = '#07070f'
SKYGLOW  = '#120b22'
SKYDOT   = '#3a2a55'
BACKW    = '#0b0d1a'
WALL_L   = '#0c0e18'
WALL_R   = '#0e1120'
WIND_D   = '#161a2e'
CABLE    = '#04050a'
SEAM     = '#05060b'
GROUND_F = '#101527'
GROUND_N = '#0a0c16'
GROUND_S = '#070a14'

MAGENTA  = '#ff2bd6'
PINK_L   = '#ff7ae4'
CYAN     = '#22e6ff'
CYAN_L   = '#8ff2ff'
CYAN_D   = '#0e7f96'
AMBER    = '#ffb340'
AMBER_P  = '#ffe08a'
RED      = '#ff3355'
WHITE    = '#eaffff'

WASH_M   = '#2a0b26'
WASH_C   = '#0a2e3d'
WASH_A   = '#2e1f0c'
WASH_D1  = '#12303c'
WASH_D2  = '#1b4a5a'

SIGN_BG  = '#0a0c14'
AC_UNIT  = '#1a1f33'

VEND1    = '#0e3a4a'
VEND1_D  = '#082430'
VEND2    = '#5c1226'
VEND2_D  = '#380a18'
SCREEN1  = '#bff3ff'
SCREEN2  = '#eaffff'
SCR_DIM  = '#5fb8cc'
SCR_AMB  = '#7a5520'

SIL      = '#04050c'
GLASS    = (191, 243, 255, 40)
RIM      = (220, 251, 255, 160)
RIB      = (220, 251, 255, 100)
STEAM    = (159, 216, 232, 48)
RAIN     = (143, 184, 216, 70)
RAIN_L   = (191, 232, 255, 120)

PUDDLE   = '#05070e'
REFL_M   = '#7a1f66'
REFL_C   = '#166878'
REFL_A   = '#7a5520'
PATH_O   = '#123a4a'
PATH_I   = '#1d6b80'

c = new_canvas(128, 128, background=SKY, name='cyberpunk-alley')

# ---------------- sky strip above the alley ----------------
c.rect(44, 0, 40, 9, SKYGLOW)
for x, y in [(50, 3), (58, 6), (70, 2), (78, 5), (64, 7), (86, 3), (40, 5)]:
    c.set(x, y, SKYDOT)

# ---------------- back wall + glowing doorway ----------------
c.rect(46, 20, 36, 32, BACKW)                 # back wall, floor line at y=52
c.rect(48, 23, 32, 27, WASH_D1)               # light wash on wall
c.rect(52, 25, 24, 25, WASH_D2)
c.rect(56, 28, 16, 24, CYAN_D)                # door frame glow
c.rect(58, 30, 12, 22, WHITE)                 # the bright doorway
c.line(64, 30, 64, 51, SCREEN1)               # door split line
c.rect(48, 24, 5, 6, WIND_D)                  # small dark windows on back wall
c.rect(48, 33, 5, 6, WIND_D)
c.rect(74, 30, 7, 5, AC_UNIT)                 # AC unit
c.line(75, 31, 80, 31, SIGN_BG)
c.line(75, 33, 80, 33, SIGN_BG)
c.line(80, 36, 80, 52, CABLE)                 # drainpipe

# ---------------- side walls ----------------
c.poly([(0, 0), (46, 20), (46, 52), (0, 84)], WALL_L)
c.poly([(127, 0), (82, 20), (82, 52), (127, 84)], WALL_R)

# neon light washes on the walls (under the signs)
c.rect(18, 14, 26, 52, WASH_M)                # magenta wash, left
c.rect(84, 10, 26, 52, WASH_C)                # cyan wash, right
c.rect(2, 48, 26, 16, WASH_A)                 # amber wash, left low

# windows (drawn over the washes)
for x, ys in [(8, [10, 24, 38]), (40, [22, 36])]:
    for y in ys:
        c.rect(x, y, 5, 7, WIND_D)
for x, ys in [(106, [10, 24, 38]), (118, [8, 22, 36])]:
    for y in ys:
        c.rect(x, y, 5, 7, WIND_D)
c.rect(8, 24, 5, 7, AMBER)                    # one lit window, left
c.rect(40, 36, 5, 7, CYAN_D)
c.rect(106, 24, 5, 7, MAGENTA)
c.rect(118, 8, 5, 7, AMBER)

# conduit following the left-wall perspective
c.line(0, 72, 44, 44, CABLE)
c.line(0, 74, 44, 46, SIGN_BG)

# fire escape on the right wall
c.rect(106, 30, 18, 2, CABLE)
c.line(106, 24, 124, 24, CABLE)
for x in (108, 112, 116, 120, 123):
    c.line(x, 24, x, 30, CABLE)
c.line(112, 32, 112, 46, CABLE)
c.line(115, 32, 115, 46, CABLE)
for y in (34, 38, 42):
    c.line(112, y, 115, y, CABLE)

# ---------------- ground ----------------
c.poly([(0, 84), (46, 52), (82, 52), (127, 84)], GROUND_F)
c.rect(0, 84, 128, 44, GROUND_N)
c.line(0, 84, 46, 52, SEAM)                   # wall/ground edges
c.line(82, 52, 127, 84, SEAM)
c.line(56, 52, 24, 127, GROUND_S)             # paving seams
c.line(72, 52, 104, 127, GROUND_S)

# door-light reflection path on the wet ground
c.poly([(56, 50), (72, 50), (84, 124), (44, 124)], PATH_O)
c.poly([(61, 50), (67, 50), (73, 120), (53, 120)], PATH_I)
for y in (60, 70, 82, 96, 110):
    c.rect(62, y, 4, 2, CYAN_L)

# neon sign reflections (dashed vertical streaks)
for x in (30, 34, 38):                        # magenta, left
    for y in range(62, 90):
        if y % 3 != 2:
            c.set(x, y, REFL_M)
for x in (86, 90, 94):                        # cyan, right
    for y in range(60, 88):
        if y % 3 != 2:
            c.set(x, y, REFL_C)
for x in (5, 9, 13):                          # left vending screen
    for y in range(97, 104):
        if y % 3 != 2:
            c.set(x, y, REFL_C)
for x in (99, 103, 107):                      # right vending screen
    for y in range(97, 104):
        if y % 3 != 2:
            c.set(x, y, REFL_A)

# puddles
c.poly([(2, 102), (22, 98), (42, 100), (36, 108), (8, 110)], PUDDLE)
c.poly([(70, 110), (92, 104), (116, 106), (124, 112), (108, 119), (80, 119)], PUDDLE)
c.poly([(38, 98), (66, 96), (78, 100), (60, 104), (40, 103)], PUDDLE)
for x in (12, 20, 28):                        # magenta caught in left puddle
    c.line(x, 100, x, 107, REFL_M)
c.rect(10, 100, 6, 1, MAGENTA)
c.rect(22, 99, 5, 1, MAGENTA)
for x in (86, 94, 102):                       # cyan in the big right puddle
    c.line(x, 106, x, 116, REFL_C)
c.rect(84, 106, 6, 1, CYAN)
c.rect(96, 105, 5, 1, CYAN)
c.line(108, 107, 108, 114, REFL_A)            # amber touch
for x in (46, 52, 64, 70):                    # centre puddle under the figure
    c.line(x, 98, x, 102, REFL_C)
c.rect(46, 98, 5, 1, SCR_DIM)
c.rect(66, 98, 5, 1, SCR_DIM)

# ---------------- power cables + festoon bulbs ----------------
c.path('M 8 6 Q 64 22 120 4', CABLE, fill=False)
c.path('M 20 14 Q 64 34 108 12', CABLE, fill=False)
c.path('M 0 26 Q 60 44 127 22', CABLE, fill=False)
c.path('M 4 34 Q 64 52 124 30', CABLE, fill=False)
for x, y, col in [(42, 21, AMBER), (53, 23, MAGENTA), (64, 23, AMBER),
                  (75, 23, MAGENTA), (86, 20, AMBER)]:
    c.set(x, y, col)

# ---------------- neon signs ----------------
# left vertical magenta sign (kanji)
c.rect(24, 18, 14, 42, SIGN_BG)
c.rect(24, 18, 14, 42, MAGENTA, fill=False)
c.text(25, 22, '酒', PINK_L, font='12px')
c.text(25, 36, '電', PINK_L, font='12px')

# right vertical cyan sign
c.rect(90, 16, 14, 44, SIGN_BG)
c.rect(90, 16, 14, 44, CYAN, fill=False)
c.text(91, 20, '脳', CYAN_L, font='12px')
c.text(91, 34, '酒', CYAN_L, font='12px')

# small amber BAR sign, left
c.rect(3, 52, 22, 10, SIGN_BG)
c.rect(3, 52, 22, 10, AMBER, fill=False)
c.text(5, 54, 'BAR', AMBER_P, font='5x7')

# 24H plaque, right wall
c.rect(110, 46, 18, 10, SIGN_BG)
c.rect(110, 46, 18, 10, CYAN_D, fill=False)
c.text(111, 48, '24H', CYAN, font='5x7')

# ---------------- vending machines ----------------
# left (cyan)
c.rect(2, 60, 16, 36, VEND1)
c.rect(2, 60, 16, 2, CYAN)                    # top light strip
c.rect(4, 64, 8, 20, SCREEN1)                 # glowing screen
c.line(5, 68, 11, 68, SCR_DIM)
c.line(5, 72, 11, 72, SCR_DIM)
c.line(5, 76, 11, 76, SCR_DIM)
c.line(5, 80, 9, 80, SCR_DIM)
for i, col in enumerate([MAGENTA, CYAN, AMBER, RED]):
    c.rect(13, 66 + i * 4, 2, 2, col)         # drink buttons
c.rect(4, 88, 12, 6, VEND1_D)                 # pickup slot
# right (red/amber)
c.rect(96, 58, 17, 38, VEND2)
c.rect(96, 58, 17, 2, RED)
c.rect(99, 62, 8, 20, SCREEN2)
c.line(100, 66, 106, 66, SCR_AMB)
c.line(100, 70, 106, 70, SCR_AMB)
c.line(100, 74, 106, 74, SCR_AMB)
c.line(100, 78, 104, 78, SCR_AMB)
for i, col in enumerate([CYAN, MAGENTA, AMBER, CYAN_L]):
    c.rect(109, 64 + i * 4, 2, 2, col)
c.rect(99, 88, 12, 6, VEND2_D)
# small dark unit near the back (depth)
c.rect(74, 44, 7, 8, SIGN_BG)
c.rect(74, 44, 7, 1, CYAN_D)

# trash bags piled at the base of the left wall
c.circle(21, 76, 5, SIGN_BG)
c.circle(28, 79, 4, SIGN_BG)
c.set(22, 70, SIGN_BG)
c.line(18, 73, 23, 72, REFL_M)
c.line(26, 76, 30, 75, REFL_M)

# ---------------- person with transparent umbrella ----------------
# umbrella canopy: wide shallow dome; the door light shows through the plastic
c.path('M 42 58 Q 58 38 74 58 Z', GLASS)
c.path('M 42 58 Q 58 38 74 58', RIB, fill=False)   # pale arc against the dark sky
c.line(42, 58, 74, 58, SIL)                        # dark trim against the bright door
for x in (46, 52, 64, 70):                         # ribs, seen dark against the light
    c.line(58, 48, x, 58, SIL)
c.line(58, 48, 58, 73, SIL)                        # shaft
c.set(59, 74, SIL)                                 # handle hook
# silhouette figure
c.circle(58, 61, 3, SIL)                      # head
c.poly([(52, 66), (64, 66), (66, 87), (50, 87)], SIL)   # coat
c.line(62, 69, 58, 73, SIL)                   # arm to umbrella
c.rect(52, 87, 5, 11, SIL)                    # back leg
c.rect(51, 97, 6, 2, SIL)                     # back foot
c.poly([(60, 87), (64, 87), (66, 96), (62, 97)], SIL)   # front leg
c.rect(62, 96, 6, 2, SIL)                     # front foot
# two-tone rim light on the figure: cyan from the door, magenta from the sign
c.line(64, 67, 65, 85, REFL_C)
c.set(61, 58, REFL_C)
c.set(65, 71, CYAN_L)
c.set(65, 79, CYAN_L)
c.line(51, 68, 51, 75, REFL_M)

# ---------------- rain ----------------
for i in range(48):
    x = (i * 37 + 13) % 127
    y = (i * 23 + 7) % 124
    c.line(x, y, x + 1, y + 4, RAIN)
for i in range(14):                           # brighter streaks in the lit centre
    x = 48 + (i * 11) % 36
    y = (i * 29 + 5) % 108
    c.line(x, y, x + 1, y + 5, RAIN_L)

result = c
print(result.stats()['colors_used'], 'visible colours')
view(result)
finish(result)
