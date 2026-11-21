# University laboratory workbench - 64x64 pixel art
# microscope | test-tube rack | dropper | labeled bottles | open notebook

c = new_canvas(64, 64, name="lab_bench")

# ---------------------------------------------------------------- palette ---
WALL    = c.color('#dce4e8', 'wall')
WALL_T  = c.color('#c9d5db', 'wall_grout')
WALL_S  = c.color('#aebcc4', 'wall_shade')

WOOD_B  = c.color('#8d5f31', 'wood_back')
WOOD_T  = c.color('#c69359', 'wood_top')
WOOD_G  = c.color('#b7854c', 'wood_grain')
WOOD_G2 = c.color('#d3a56d', 'wood_grain_lt')
LIP     = c.color('#a97a45', 'wood_lip')
APRON   = c.color('#7d5327', 'apron')
APRON_D = c.color('#5d3d1d', 'apron_dk')
CAB     = c.color('#39414c', 'cab')
CAB2    = c.color('#4a5460', 'cab2')
CAB3    = c.color('#6d7885', 'cab3')
SHADOW  = c.color('#a5763f', 'cast_shadow')

MET_D   = c.color('#26303a', 'metal_dk')
MET_M   = c.color('#4e5c69', 'metal_mid')
MET_L   = c.color('#8494a1', 'metal_lt')
MET_H   = c.color('#c3d0d9', 'metal_hi')

GL_O    = c.color('#6f97ab', 'glass_out')
GL_M    = c.color('#b3d8e8', 'glass_mid')
GL_L    = c.color('#e6f4fa', 'glass_hi')

LIQ_R   = c.color('#cf4659', 'liq_red')
LIQ_RL  = c.color('#e2737f', 'liq_red_lt')
LIQ_G   = c.color('#5fbb6b', 'liq_green')
LIQ_GL  = c.color('#8ad694', 'liq_green_lt')
LIQ_B   = c.color('#4a8fd6', 'liq_blue')
LIQ_BL  = c.color('#7fb4e8', 'liq_blue_lt')
LIQ_A   = c.color('#e0a13c', 'liq_amber')

AMB     = c.color('#b5762e', 'amber')
AMB_L   = c.color('#d69c4e', 'amber_lt')
AMB_D   = c.color('#875320', 'amber_dk')

LABEL   = c.color('#f6f0dd', 'label')
LABEL_S = c.color('#d9d0b6', 'label_sh')
INK     = c.color('#5b6a79', 'ink')
CAP_D   = c.color('#31363c', 'cap_dk')
CAP_R   = c.color('#bd4239', 'cap_red')
CAP_RL  = c.color('#e0796e', 'cap_red_lt')

PAGE    = c.color('#faf7ee', 'page')
PAGE_S  = c.color('#ded7c4', 'page_sh')
SPINE   = c.color('#a89f8a', 'spine')
COVER   = c.color('#7c4a3c', 'cover')
COVER_D = c.color('#573126', 'cover_dk')
COVER_L = c.color('#96604e', 'cover_lt')

RACK    = c.color('#a9793f', 'rack')
RACK_L  = c.color('#c9a066', 'rack_lt')
RACK_D  = c.color('#7a5227', 'rack_dk')

WHITE   = c.color('#ffffff', 'white')


# ---------------------------------------------------------------- helpers ---
def SPEC(spec, col):
    """spec = list of (y, x0, x1) inclusive rows."""
    for y, x0, x1 in spec:
        c.rect(x0, y, x1 - x0 + 1, 1, col)

def RW(y, x0, x1, col):
    c.rect(x0, y, x1 - x0 + 1, 1, col)

def R(x0, y0, x1, y1, col):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, col)


# ------------------------------------------------------------------- wall ---
R(0, 0, 63, 31, WALL)
for ty in (7, 15, 23):
    RW(ty, 0, 63, WALL_T)
bands = [(0, 6, (7, 23, 39, 55)), (8, 14, (15, 31, 47, 63)),
         (16, 22, (7, 23, 39, 55)), (24, 30, (15, 31, 47, 63))]
for y0, y1, xs in bands:
    for tx in xs:
        if tx < 64:
            for y in range(y0, y1 + 1):
                c.set(tx, y, WALL_T)
RW(29, 0, 63, WALL_S)
RW(30, 0, 63, WALL_S)
RW(31, 0, 63, WALL_S)

# ------------------------------------------------------------------ bench ---
RW(32, 0, 63, WOOD_B)
R(0, 33, 63, 49, WOOD_T)
for gx0, gx1, gy, col in ((2, 16, 35, WOOD_G), (20, 40, 34, WOOD_G),
                          (44, 62, 36, WOOD_G), (3, 26, 40, WOOD_G2),
                          (30, 58, 41, WOOD_G), (2, 18, 45, WOOD_G),
                          (22, 44, 47, WOOD_G2), (48, 62, 44, WOOD_G),
                          (5, 30, 49, WOOD_G)):
    RW(gy, gx0, gx1, col)
RW(50, 0, 63, LIP)
RW(51, 0, 63, APRON)
R(0, 52, 63, 55, APRON_D)
R(0, 56, 63, 63, CAB)
R(4, 58, 28, 62, CAB2)
R(34, 58, 58, 62, CAB2)
R(13, 59, 19, 61, CAB3)
R(43, 59, 49, 61, CAB3)
RW(57, 0, 63, CAB)

# ------------------------------------------------------------ cast shadows --
RW(44, 2, 21, SHADOW)      # microscope
RW(40, 21, 45, SHADOW)     # rack
RW(36, 46, 53, SHADOW)     # bottle A
RW(37, 54, 63, SHADOW)     # flask B
RW(48, 46, 55, SHADOW)     # jar C
RW(50, 19, 46, SHADOW)     # notebook
RW(48, 2, 18, SHADOW)      # dropper


# ------------------------------------------------------- microscope (left) --
def microscope():
    # arm (drawn first, behind body)
    R(15, 15, 19, 41, MET_M)
    for y in range(15, 42):
        c.set(19, y, MET_D)
    R(15, 19, 15, 41, MET_L)
    # base
    SPEC([(41, 4, 18), (42, 2, 19), (43, 1, 20)], MET_M)
    RW(43, 1, 20, MET_D)
    RW(42, 2, 19, MET_L)
    c.set(4, 41, MET_L); c.set(18, 41, MET_D)
    c.set(1, 43, MET_D); c.set(20, 43, MET_D)
    # substage mirror
    SPEC([(38, 8, 12), (39, 7, 13), (40, 8, 12)], MET_L)
    c.set(9, 39, MET_H); c.set(10, 39, MET_H); c.set(11, 39, MET_H)
    c.set(8, 40, MET_D); c.set(12, 40, MET_D)
    # stage pillar
    R(14, 38, 18, 40, MET_D)
    # stage
    R(2, 35, 18, 37, MET_M)
    RW(35, 2, 18, MET_L)
    RW(37, 2, 18, MET_D)
    c.set(2, 36, MET_L)
    # glass slide
    R(5, 33, 14, 34, GL_L)
    RW(34, 5, 14, GL_M)
    c.set(9, 33, LIQ_R); c.set(10, 33, LIQ_R)
    c.set(9, 34, LIQ_RL); c.set(10, 34, LIQ_R)
    # nosepiece
    R(7, 27, 15, 29, MET_M)
    RW(27, 7, 15, MET_L)
    RW(29, 7, 15, MET_D)
    # objective lens
    SPEC([(30, 9, 13), (31, 9, 12), (32, 10, 11)], MET_L)
    c.set(13, 30, MET_D); c.set(12, 31, MET_D); c.set(11, 32, MET_D)
    c.set(10, 32, MET_H); c.set(10, 31, MET_H)
    # body tube
    R(8, 19, 14, 26, MET_M)
    R(8, 19, 8, 26, MET_L)
    c.set(9, 20, MET_H); c.set(9, 21, MET_H)
    R(14, 19, 14, 26, MET_D)
    # head
    R(7, 15, 17, 18, MET_M)
    RW(15, 7, 17, MET_L)
    RW(18, 7, 17, MET_D)
    c.set(7, 16, MET_L); c.set(7, 17, MET_L)
    # eyepiece
    R(9, 11, 13, 14, MET_M)
    for y in (11, 12, 13):
        c.set(9, y, MET_L)
        c.set(13, y, MET_D)
    R(8, 9, 14, 10, MET_D)
    RW(9, 9, 13, MET_M)
    c.set(9, 9, MET_L)
    # coarse focus knob
    c.circle(17, 32, 2, MET_L)
    c.circle(17, 32, 1, MET_D)
    c.set(16, 31, MET_H)
    # fine focus knob
    R(17, 36, 18, 37, MET_L)
    c.set(18, 37, MET_D)


# ------------------------------------------------------ test-tube rack ------
def rack():
    # back bar
    R(22, 25, 44, 27, RACK_D)
    tubes = [24, 29, 34, 39]
    liquids = [(LIQ_R, LIQ_RL, 30), (LIQ_B, LIQ_BL, 33),
               (LIQ_A, LIQ_A, 27), (LIQ_G, LIQ_GL, 31)]
    for x0, (liq, liq_l, lv) in zip(tubes, liquids):
        x1 = x0 + 3
        RW(21, x0, x1, GL_O)                 # rim
        R(x0, 22, x1, 38, GL_M)
        for y in range(22, 39):
            c.set(x0, y, GL_O)
            c.set(x1, y, GL_O)
            c.set(x0 + 1, y, GL_L)
        RW(38, x0 + 1, x1 - 1, GL_O)         # rounded bottom
        c.set(x0 + 1, 37, GL_O); c.set(x1 - 1, 37, GL_O)
        R(x0 + 1, lv, x1 - 1, 37, liq)       # liquid
        RW(lv, x0 + 1, x1 - 1, liq_l)
        c.set(x0 + 1, lv + 1, liq_l)
    # front top bar
    RW(26, 22, 44, RACK_L)
    RW(27, 22, 44, RACK)
    # legs
    R(22, 28, 23, 39, RACK)
    R(43, 28, 44, 39, RACK)
    for y in range(28, 40):
        c.set(22, y, RACK_L)
        c.set(44, y, RACK_D)
    # bottom bar
    RW(37, 22, 44, RACK_L)
    RW(38, 22, 44, RACK)
    RW(39, 21, 45, RACK_D)


# ------------------------------------------------- bottle A (tall, amber) ---
def bottle_a():
    R(48, 14, 51, 16, CAP_D)                 # cap
    RW(14, 48, 50, MET_M)
    c.set(51, 16, MET_D); c.set(48, 14, MET_L)
    R(48, 17, 49, 19, AMB_D)                 # neck
    c.set(48, 17, AMB); c.set(48, 18, AMB)
    SPEC([(20, 47, 51), (21, 46, 52)], AMB)  # shoulder
    c.set(47, 20, AMB_L); c.set(46, 21, AMB_L)
    R(46, 22, 52, 34, AMB)                   # body
    R(46, 22, 46, 34, AMB_L)                 # left highlight
    R(52, 22, 52, 34, AMB_D)                 # right shade
    RW(35, 46, 52, AMB_D)                    # base
    c.set(46, 35, AMB)
    # label
    R(47, 25, 51, 31, LABEL)
    RW(31, 47, 51, LABEL_S)
    c.set(47, 25, LABEL_S); c.set(51, 25, LABEL_S)
    RW(27, 48, 50, LIQ_B)                    # colour band = contents key
    RW(29, 48, 50, INK)
    RW(30, 48, 49, LABEL_S)


# --------------------------------------------- bottle B (erlenmeyer flask) --
def flask_b():
    body = [(20, 56, 60), (21, 57, 59), (22, 57, 59), (23, 57, 59),
            (24, 56, 60), (25, 55, 61), (26, 54, 62), (27, 54, 62),
            (28, 54, 62), (29, 54, 62), (30, 54, 62), (31, 54, 62),
            (32, 54, 62), (33, 54, 62), (34, 54, 62), (35, 54, 62),
            (36, 54, 62)]
    SPEC(body, GL_M)
    for y, x0, x1 in body:
        c.set(x0, y, GL_O)
        c.set(x1, y, GL_O)
    RW(20, 55, 61, GL_O)                     # rim
    RW(21, 56, 60, GL_L)
    SPEC([(30, 55, 61), (31, 55, 61), (32, 55, 61), (33, 55, 61),
          (34, 55, 61), (35, 55, 61)], LIQ_G)
    RW(30, 55, 61, LIQ_GL)
    RW(36, 54, 62, GL_O)                     # bottom
    for y in range(22, 26):
        c.set(58, y, GL_L)
    for y in range(31, 36):
        c.set(56, y, LIQ_GL)
    # label band on the cone
    R(55, 26, 61, 29, LABEL)
    RW(29, 55, 61, LABEL_S)
    RW(27, 56, 60, CAP_R)
    c.set(55, 26, LABEL_S); c.set(61, 26, LABEL_S)


# --------------------------------------------------------- jar C (squat) ----
def jar_c():
    RW(39, 47, 53, CAP_RL)                   # lid
    R(46, 40, 54, 40, CAP_R)
    c.set(46, 40, CAP_D); c.set(54, 40, CAP_D)
    R(47, 41, 53, 41, GL_O)                  # neck ring
    R(46, 42, 54, 46, GL_M)                  # body
    for y in range(42, 47):
        c.set(46, y, GL_L)
        c.set(54, y, GL_O)
    RW(47, 46, 54, GL_O)                     # base
    R(47, 43, 53, 46, LABEL)                 # label
    RW(46, 47, 53, LABEL_S)
    c.set(47, 43, LABEL_S); c.set(53, 43, LABEL_S)
    RW(44, 48, 52, LIQ_A)                    # contents key
    c.set(48, 45, LABEL_S); c.set(49, 45, LABEL_S); c.set(50, 45, LABEL_S)


# ---------------------------------------------------------- open notebook ---
def notebook():
    cover = [(40, 28, 36), (41, 26, 38), (42, 25, 39), (43, 24, 40),
             (44, 23, 41), (45, 22, 42), (46, 21, 43), (47, 20, 44),
             (48, 19, 45), (49, 19, 45)]
    SPEC(cover, COVER)
    for y, x0, x1 in cover:
        c.set(x0, y, COVER_D)
        c.set(x1, y, COVER_D)
    RW(49, 20, 44, COVER_D)
    RW(40, 29, 35, COVER_L)
    lp = [(41, 27, 30), (42, 26, 30), (43, 25, 30), (44, 24, 30),
          (45, 23, 30), (46, 22, 30), (47, 21, 30), (48, 20, 30)]
    rp = [(41, 33, 37), (42, 33, 38), (43, 33, 39), (44, 33, 40),
          (45, 33, 41), (46, 33, 42), (47, 33, 43), (48, 33, 44)]
    SPEC(lp, PAGE)
    SPEC(rp, PAGE)
    for y, x0, x1 in lp:
        c.set(x1, y, PAGE_S)
    for y, x0, x1 in rp:
        c.set(x0, y, PAGE_S)
    RW(48, 20, 30, PAGE_S)
    RW(48, 33, 44, PAGE_S)
    # spine / gutter
    R(31, 41, 32, 48, SPINE)
    for y in range(42, 48):
        c.set(31, y, COVER_D)
    RW(41, 31, 32, PAGE_S)
    # handwriting: left page (three spaced dashed lines read as text)
    RW(43, 26, 27, INK); c.set(29, 43, INK)
    RW(45, 24, 25, INK); RW(45, 27, 28, INK)
    RW(47, 22, 24, INK); RW(47, 26, 27, INK)
    # right page: ruled line + small bar chart
    RW(42, 34, 38, PAGE_S)
    RW(47, 34, 43, INK)                      # axis
    c.set(34, 44, INK); c.set(34, 45, INK); c.set(34, 46, INK)
    R(36, 45, 37, 46, LIQ_B)
    R(38, 44, 39, 46, LIQ_R)
    R(40, 46, 41, 46, LIQ_G)
    c.set(42, 43, INK)


# ---------------------------------------------------------------- dropper ---
def dropper():
    # rubber bulb
    SPEC([(44, 4, 7), (45, 3, 8), (46, 3, 8), (47, 4, 7)], CAP_R)
    c.set(4, 44, CAP_RL); c.set(5, 44, CAP_RL); c.set(4, 45, CAP_RL)
    RW(47, 4, 7, CAP_D)
    c.set(8, 46, CAP_D); c.set(8, 47, CAP_D)
    # metal collar
    R(9, 45, 10, 46, MET_D)
    c.set(9, 45, MET_L); c.set(10, 45, MET_M)
    # glass pipette
    RW(45, 11, 16, GL_L)
    RW(46, 11, 16, GL_M)
    RW(46, 12, 15, LIQ_B)                    # liquid drawn up
    c.set(17, 46, GL_O)                      # tapered tip
    c.set(18, 46, GL_O)
    # falling drop
    c.set(18, 47, LIQ_B)
    c.set(18, 48, LIQ_BL)
    # puddle on the bench
    RW(49, 14, 19, LIQ_B)
    c.set(16, 49, LIQ_BL); c.set(17, 49, LIQ_BL)
    RW(50, 13, 20, LIQ_B)


# ------------------------------------------------------------- draw order ---
microscope()
rack()
bottle_a()
flask_b()
jar_c()
notebook()
dropper()

view(c)
print(c.stats_text())
finish(c)
