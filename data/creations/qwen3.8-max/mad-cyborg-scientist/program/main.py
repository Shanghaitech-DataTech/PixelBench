try:
    from pixelbench_api import *
except Exception:
    pass

W = H = 64
c = new_canvas(W, H, name="output")

# ==================== palette ====================
BG0 = '#05080c'; BG1 = '#0a121b'; BG2 = '#101d29'; BG3 = '#17303c'; GLOW = '#1e4c55'
PIPE = '#22303c'; PIPE2 = '#2f4351'; GLASS = '#2c6a63'; GLASS2 = '#4fae86'

SK_HI = '#ffe6c8'; SK_LT = '#f3c99e'; SK_MD = '#d9a277'; SK_SH = '#a9714c'
SK_DP = '#71462f'; SK_BK = '#43271a'; SK_RD = '#c4695a'

MT_HI = '#eef5fa'; MT_LT = '#bccad7'; MT_MD = '#8695a5'; MT_SH = '#596574'
MT_DP = '#38414e'; MT_BK = '#212832'; MT_CY = '#7fb9c9'; MT_CY2 = '#4d8494'

EY_W = '#ffffff'; EY_HI = '#ccfbff'; EY_MD = '#54dcff'; EY_DP = '#1b9fd0'; EY_DK = '#0e5f86'

HR_W = '#ffffff'; HR_LT = '#e4ebf2'; HR_MD = '#bac4d0'; HR_SH = '#8b96a5'; HR_DP = '#5d6878'

CT_LT = '#eceadf'; CT_MD = '#cdc9ba'; CT_SH = '#a29c8c'; CT_DP = '#756e5e'
CT_ST1 = '#8d7a48'; CT_ST2 = '#685634'; CT_BL = '#6d2a2c'

LT_HI = '#a76f40'; LT_MD = '#7f512c'; LT_SH = '#5a3620'; LT_DP = '#382113'
BL_MD = '#4a3320'; BL_DP = '#2b1d11'
BR_HI = '#f2d464'; BR_MD = '#c39a2c'; BR_SH = '#87681b'

CB_R = '#b8453c'; CB_Y = '#cfa83a'; CB_G = '#4a9a63'; CB_B = '#3a76a8'; CB_K = '#191d24'

TEETH = '#f4efe2'; TEETH2 = '#cbc2ac'; GOLD = '#d9a94a'; MOUTH = '#2b1418'; BLACK = '#0a0d12'


# ==================== helpers ====================
def R(y, x0, x1, col):
    if x1 < x0:
        return
    for x in range(max(0, x0), min(63, x1) + 1):
        c.set(x, y, col)


def RR(lst, col):
    for (y, x0, x1) in lst:
        R(y, x0, x1, col)


def dots(pts, col):
    for p in pts:
        c.set(p[0], p[1], col)


def segs(lst, col=None):
    for t in lst:
        if len(t) == 5:
            c.line(t[0], t[1], t[2], t[3], t[4])
        else:
            c.line(t[0], t[1], t[2], t[3], col)


# ==================== background ====================
c.rect(0, 0, 64, 64, BG0)
c.ellipse(31, 32, 34, 32, BG1)
c.ellipse(31, 31, 27, 26, BG2)
c.ellipse(31, 30, 21, 20, BG3)
c.ellipse(33, 28, 15, 14, GLOW)

# lab backdrop: pipes, shelf, bottles
RR([(0, 3, 4), (1, 3, 4), (2, 3, 4), (3, 3, 4), (4, 3, 4), (5, 3, 4), (6, 3, 4), (7, 3, 4), (8, 3, 4)], PIPE)
R(0, 4, 4, PIPE2); R(1, 4, 4, PIPE2); R(2, 4, 4, PIPE2); R(3, 4, 4, PIPE2)
RR([(56, 58, 60), (57, 58, 60), (58, 58, 60), (59, 58, 60), (60, 58, 60), (61, 58, 60), (62, 58, 60), (63, 58, 60)], PIPE)
R(57, 59, 59, PIPE2); R(58, 59, 59, PIPE2); R(59, 59, 59, PIPE2); R(60, 59, 59, PIPE2)
R(9, 0, 9, PIPE); R(10, 0, 9, BG1)
c.rect(1, 4, 4, 5, GLASS); c.rect(2, 4, 2, 2, GLASS2); c.rect(1, 3, 4, 1, MT_SH)
c.rect(6, 5, 3, 4, GLASS); c.rect(7, 5, 1, 2, GLASS2); c.rect(6, 4, 3, 1, MT_SH)
R(7, 55, 63, PIPE); R(8, 55, 63, BG1)
c.rect(57, 2, 4, 5, GLASS); c.rect(58, 3, 2, 2, GLASS2); c.rect(57, 1, 4, 1, MT_SH)

# vignette corners
for i in range(7):
    R(i, 0, 6 - i, BG0)
    R(63 - i, 0, 6 - i, BG0)
    R(i, 57 + i, 63, BG0)
    R(63 - i, 57 + i, 63, BG0)

# ==================== back hair ====================
HAIR_BACK = [
    (2, 30, 34), (3, 27, 37), (4, 24, 40), (5, 22, 42), (6, 20, 44), (7, 18, 46),
    (8, 16, 48), (9, 15, 49), (10, 14, 50), (11, 13, 51), (12, 12, 52), (13, 12, 52),
    (14, 11, 52), (15, 11, 52), (16, 11, 52), (17, 11, 52), (18, 11, 52), (19, 11, 52),
    (20, 11, 52), (21, 12, 52), (22, 12, 52), (23, 12, 52), (24, 12, 52), (25, 12, 52),
    (26, 13, 50), (27, 13, 50), (28, 13, 50), (29, 14, 50), (30, 14, 50),
]
RR(HAIR_BACK, HR_SH)
# wild spikes
segs([(28, 2, 25, 0, HR_MD), (33, 2, 35, 0, HR_MD), (22, 4, 17, 1, HR_MD),
      (40, 4, 45, 1, HR_MD), (18, 7, 13, 4, HR_MD), (46, 7, 52, 4, HR_MD),
      (12, 13, 7, 10, HR_MD), (52, 13, 57, 10, HR_MD),
      (11, 18, 6, 16, HR_MD), (52, 18, 58, 16, HR_MD),
      (11, 23, 6, 25, HR_MD), (52, 22, 57, 24, HR_MD),
      (13, 28, 8, 31, HR_SH)], HR_MD)

# ==================== head base ====================
HEAD = [
    (8, 28, 36), (9, 25, 39), (10, 23, 41), (11, 21, 43), (12, 20, 44), (13, 19, 45),
    (14, 18, 46), (15, 17, 47), (16, 16, 48), (17, 16, 48), (18, 15, 48), (19, 15, 49),
    (20, 15, 49), (21, 15, 49), (22, 15, 49), (23, 15, 49), (24, 15, 49), (25, 15, 49),
    (26, 15, 49), (27, 15, 49), (28, 15, 49), (29, 15, 49), (30, 16, 49), (31, 16, 48),
    (32, 16, 48), (33, 17, 48), (34, 17, 47), (35, 18, 47), (36, 18, 46), (37, 19, 46),
    (38, 19, 45), (39, 20, 45), (40, 21, 44), (41, 22, 43), (42, 23, 42), (43, 24, 41),
    (44, 25, 40), (45, 26, 39), (46, 27, 38), (47, 28, 36), (48, 30, 34),
]
SEAM = 32
for (y, x0, x1) in HEAD:
    for x in range(x0, x1 + 1):
        if x < SEAM:
            d = (((x - 19) ** 2) * 1.0 + ((y - 24) ** 2) * 1.1) ** 0.5
            if d < 6:
                col = SK_HI
            elif d < 10:
                col = SK_LT
            elif d < 14:
                col = SK_MD
            elif d < 18:
                col = SK_SH
            else:
                col = SK_DP
            if y >= 44:
                col = SK_DP if col in (SK_HI, SK_LT, SK_MD) else SK_BK
            c.set(x, y, col)
        else:
            d = (((x - 37) ** 2) * 1.0 + ((y - 20) ** 2) * 1.25) ** 0.5
            if d < 5:
                col = MT_HI
            elif d < 9:
                col = MT_LT
            elif d < 13:
                col = MT_MD
            elif d < 17:
                col = MT_SH
            else:
                col = MT_DP
            if y >= 44:
                col = MT_DP if col in (MT_HI, MT_LT, MT_MD) else MT_BK
            c.set(x, y, col)

# ears
c.ellipse(14, 31, 2, 4, SK_SH)
c.ellipse(14, 31, 1, 2, SK_DP)
c.ellipse(50, 30, 3, 4, MT_SH)
c.ellipse(50, 30, 2, 3, MT_DP)
c.ellipse(50, 30, 1, 1, MT_BK)
dots([(50, 27), (50, 33)], MT_HI)

# ==================== metal plating ====================
# cranial plate seam
R(17, 32, 48, MT_BK)
R(16, 32, 48, MT_DP)
segs([(38, 8, 38, 16, MT_DP), (39, 8, 39, 16, MT_BK)], MT_BK)
# rivets on cranium
dots([(34, 11), (34, 14), (43, 11), (43, 14), (46, 20), (46, 24), (33, 20)], MT_HI)
dots([(35, 11), (35, 14), (44, 11), (44, 14), (47, 20), (47, 24), (34, 20)], MT_DP)
# cheek plate outline
segs([(33, 32, 33, 38, MT_BK), (33, 38, 41, 42, MT_BK), (41, 42, 46, 38, MT_BK),
      (46, 38, 47, 32, MT_BK)], MT_BK)
# jaw plate line
segs([(32, 43, 42, 43, MT_BK)], MT_BK)
# temple panel lines
segs([(41, 19, 47, 22, MT_BK), (42, 25, 47, 27, MT_BK)], MT_BK)
# cyan bounce light on metal cheek from the eye
dots([(35, 33), (36, 34), (37, 34), (38, 35), (44, 34), (45, 33), (43, 35), (34, 32)], MT_CY2)
dots([(36, 33), (37, 33), (44, 33), (45, 32)], MT_CY)

# ==================== human face shading ====================
dots([(20, 20), (21, 20), (22, 20), (21, 21), (22, 21), (23, 21), (20, 21)], SK_HI)
dots([(19, 31), (20, 31), (19, 32), (20, 32), (21, 32), (18, 31)], SK_HI)
RR([(22, 15, 16), (23, 15, 16), (24, 15, 16), (25, 15, 16), (26, 15, 16), (27, 15, 16),
    (28, 15, 16), (29, 15, 16), (30, 16, 17), (31, 16, 17), (32, 16, 17), (33, 17, 18),
    (34, 17, 18), (35, 18, 19)], SK_DP)
RR([(26, 30, 31), (27, 30, 31), (28, 30, 31), (29, 30, 31), (30, 30, 31), (31, 30, 31),
    (32, 30, 31), (33, 30, 31), (34, 30, 31), (35, 30, 31), (36, 30, 31)], SK_SH)
segs([(18, 35, 26, 37, SK_SH), (19, 36, 26, 38, SK_DP)], SK_DP)
RR([(44, 25, 31), (45, 26, 31), (46, 27, 31), (47, 28, 31)], SK_DP)
R(44, 25, 31, SK_BK)

# scar with stitches across the human cheekbone
segs([(17, 31, 22, 35, SK_RD)], SK_RD)
segs([(18, 30, 19, 32, SK_BK), (20, 32, 21, 34, SK_BK), (22, 33, 23, 35, SK_BK)], SK_BK)

# ==================== eyes ====================
# --- human eye (viewer left), wide & manic ---
RR([(21, 18, 29), (22, 18, 29)], HR_MD)
R(21, 18, 29, HR_W)
segs([(17, 23, 29, 24, HR_LT)], HR_LT)
RR([(23, 20, 29), (24, 20, 29)], SK_DP)
c.rect(20, 25, 9, 5, '#e9e5dc')
R(25, 21, 27, '#cfcbc2')
dots([(21, 27), (27, 28), (21, 28)], CB_R)
c.rect(23, 25, 4, 5, '#3d6a86')
c.rect(24, 26, 2, 3, BLACK)
dots([(23, 26)], EY_W)
R(30, 20, 28, SK_DP)
R(31, 20, 28, SK_SH)
dots([(19, 26), (29, 26)], SK_BK)

# --- cybernetic eye (viewer right) ---
c.ellipse(40, 27, 6, 5, MT_BK)
c.ellipse(40, 27, 5, 4, MT_DP)
segs([(34, 24, 46, 24, MT_SH), (34, 31, 46, 32, MT_SH)], MT_SH)
c.ellipse(40, 27, 4, 4, EY_DK)
c.ellipse(40, 27, 3, 3, EY_DP)
c.ellipse(40, 27, 2, 2, EY_MD)
c.circle(40, 27, 1, EY_HI)
dots([(40, 27), (39, 26), (41, 26), (40, 26)], EY_W)
dots([(38, 25), (42, 29)], EY_HI)
dots([(37, 27), (43, 27), (40, 24), (40, 30)], EY_DK)
# glow spill
dots([(33, 25), (33, 26), (33, 27), (33, 28), (33, 29), (47, 25), (47, 26), (47, 27),
      (47, 28), (47, 29), (48, 27), (32, 27), (32, 26), (32, 28)], EY_DK)
dots([(34, 22), (35, 22), (45, 22), (46, 22), (34, 33), (35, 34), (45, 33), (46, 33)], MT_CY2)
# lens crack
segs([(42, 25, 44, 27, MT_HI), (44, 27, 43, 29, MT_LT)], MT_HI)
# brow plate over the eye
RR([(20, 34, 47), (21, 33, 48)], MT_SH)
R(20, 34, 47, MT_MD)
segs([(33, 23, 48, 22, MT_BK)], MT_BK)

# ==================== nose ====================
segs([(30, 27, 29, 33, SK_SH), (29, 33, 31, 35, SK_SH)], SK_SH)
segs([(31, 27, 30, 33, SK_HI)], SK_HI)
RR([(35, 28, 33)], SK_DP)
dots([(27, 35), (33, 35)], SK_BK)
dots([(28, 36), (32, 36)], SK_SH)
R(36, 30, 31, SK_MD)
segs([(32, 27, 33, 34, MT_DP), (34, 34, 35, 35, MT_DP)], MT_DP)
dots([(32, 28), (32, 29), (32, 30), (32, 31)], MT_SH)

# ==================== maniacal grin ====================
MOUTH_ROWS = [(35, 40, 42), (36, 33, 42), (37, 24, 43), (38, 22, 43), (39, 22, 42),
              (40, 23, 41), (41, 25, 40), (42, 27, 38), (43, 29, 36)]
RR(MOUTH_ROWS, MOUTH)
# lips
segs([(21, 36, 23, 37, SK_RD), (21, 36, 22, 35, SK_RD)], SK_RD)
segs([(44, 34, 42, 35, SK_RD)], SK_RD)
R(36, 34, 39, SK_DP)
R(35, 26, 32, SK_SH); R(34, 33, 39, SK_DP)
dots([(27, 35), (33, 35)], SK_BK)
dots([(28, 36), (32, 36)], SK_SH)
# upper teeth
R(37, 25, 41, TEETH)
R(38, 23, 42, TEETH)
dots([(24, 38), (27, 38), (30, 38), (33, 38), (36, 38), (39, 38), (42, 38),
      (26, 37), (30, 37), (34, 37), (38, 37)], TEETH2)
dots([(29, 37), (29, 38)], GOLD)
dots([(38, 37), (38, 38), (39, 37), (39, 38)], MT_HI)
R(37, 40, 42, TEETH2)
R(38, 41, 42, '#ded8c8')
# dark gap
R(39, 23, 42, MOUTH)
dots([(24, 39), (28, 39), (32, 39), (36, 39), (40, 39)], BLACK)
# lower teeth
R(40, 24, 40, TEETH2)
R(41, 26, 39, TEETH2)
dots([(26, 40), (30, 40), (34, 40), (38, 40)], TEETH)
R(40, 35, 40, MT_LT)
R(41, 36, 39, MT_MD)
# tongue hint
dots([(27, 39), (28, 39), (29, 39), (30, 39)], SK_RD)
# grin creases
segs([(22, 34, 20, 39, SK_DP), (21, 34, 19, 38, SK_SH)], SK_DP)
segs([(44, 33, 46, 38, MT_BK)], MT_BK)
# metal jaw grille on the right
segs([(44, 37, 46, 39, MT_BK), (45, 39, 46, 42, MT_BK)], MT_BK)
dots([(45, 38), (46, 40), (45, 41)], MT_SH)
# chin
R(44, 27, 31, SK_DP)
R(45, 28, 31, SK_BK)
dots([(28, 45), (29, 45), (30, 45)], SK_SH)
R(44, 32, 38, MT_DP)
R(45, 32, 38, MT_BK)
dots([(34, 45), (35, 45)], MT_SH)
# stubble
dots([(24, 43), (26, 44), (28, 43), (22, 41), (25, 42), (30, 44)], SK_DP)

# ==================== front hair ====================
# human side fringe
RR([(14, 13, 31), (13, 14, 31), (12, 16, 31)], HR_MD)
RR([(15, 12, 31), (16, 12, 31)], HR_SH)
R(17, 12, 19, HR_MD); R(17, 21, 26, HR_MD); R(17, 28, 30, HR_MD)
R(18, 12, 17, HR_MD); R(18, 22, 25, HR_MD); R(18, 27, 29, HR_MD)
R(19, 12, 17, HR_MD); R(19, 23, 25, HR_MD); R(19, 27, 28, HR_MD)
R(20, 12, 17, HR_MD); R(20, 23, 24, HR_MD); R(20, 26, 27, HR_MD)
R(21, 13, 17, HR_SH); R(21, 23, 24, HR_SH)
R(22, 13, 17, HR_SH)
R(23, 13, 17, HR_SH)
R(24, 14, 16, HR_SH)
R(25, 14, 16, HR_DP)
R(26, 14, 16, HR_DP)
R(27, 15, 16, HR_DP)
R(28, 15, 16, HR_DP)
R(29, 15, 16, HR_DP)
# metal side: thin receded hair, plate exposed
R(8, 32, 38, HR_MD); R(9, 32, 41, HR_MD); R(10, 44, 47, HR_MD); R(11, 45, 49, HR_MD)
R(12, 46, 51, HR_SH); R(13, 47, 51, HR_SH); R(14, 48, 51, HR_SH); R(15, 49, 52, HR_SH)
R(16, 50, 52, HR_SH); R(17, 50, 52, HR_SH); R(18, 50, 52, HR_SH); R(19, 50, 52, HR_SH)
R(20, 50, 52, HR_DP); R(21, 50, 51, HR_DP); R(22, 50, 51, HR_DP); R(23, 50, 50, HR_DP)
R(24, 50, 50, HR_DP); R(25, 50, 50, HR_DP)
# hair body tones
R(13, 15, 30, HR_LT)
R(12, 17, 30, HR_LT)
R(11, 20, 30, HR_W)
R(10, 23, 30, HR_LT)
R(9, 26, 30, HR_W)
R(8, 28, 36, HR_LT)
R(7, 30, 34, HR_W)
R(6, 30, 34, HR_LT)
R(5, 28, 36, HR_W)
# strand shadows
segs([(19, 14, 16, 18, HR_DP), (25, 13, 23, 18, HR_DP), (31, 12, 30, 17, HR_DP),
      (14, 16, 12, 22, HR_DP), (48, 14, 50, 20, HR_DP)], HR_DP)
segs([(22, 12, 20, 17, HR_W), (28, 11, 26, 16, HR_W), (34, 10, 36, 14, HR_W),
      (44, 12, 46, 16, HR_W)], HR_W)
# wild strands over the forehead
segs([(19, 17, 21, 21, HR_LT), (20, 17, 22, 20, HR_W), (27, 17, 26, 21, HR_MD),
      (28, 17, 29, 20, HR_LT), (30, 17, 31, 20, HR_MD)], HR_MD)

# ==================== brain electrode plugs ====================
# cranial bracket on the metal cranium
c.rect(34, 10, 12, 6, MT_SH)
c.rect(35, 11, 10, 4, MT_MD)
R(10, 34, 45, MT_BK); R(15, 34, 45, MT_BK)
dots([(34, 11), (45, 11), (34, 14), (45, 14)], MT_HI)
# plug sockets
for (px_, py_) in [(36, 11), (40, 11), (44, 11)]:
    c.rect(px_, py_, 2, 3, MT_DP)
    c.set(px_, py_, MT_HI); c.set(px_ + 1, py_, MT_LT)
    c.set(px_, py_ + 2, MT_BK); c.set(px_ + 1, py_ + 2, MT_BK)
# wires from plugs arcing up and right
segs([(36, 10, 34, 6, CB_R), (34, 6, 30, 4, CB_R), (30, 4, 26, 6, CB_R)], CB_R)
segs([(41, 10, 43, 5, CB_Y), (43, 5, 48, 3, CB_Y), (48, 3, 53, 5, CB_Y)], CB_Y)
segs([(45, 10, 49, 7, CB_G), (49, 7, 55, 8, CB_G), (55, 8, 58, 11, CB_G)], CB_G)
dots([(26, 6), (25, 7)], CB_R); dots([(53, 5), (54, 6)], CB_Y); dots([(58, 11), (59, 12)], CB_G)
# side plug on the temple
c.rect(47, 20, 3, 3, MT_DP); dots([(47, 20), (48, 20)], MT_HI); dots([(49, 21)], CB_B)
segs([(49, 22, 52, 24, CB_B), (52, 24, 54, 26, CB_B), (54, 26, 55, 28, CB_B)], CB_B)

# ==================== neck (drawn later, after collar) ====================
dots([(31, 46), (33, 46)], MT_BK)

# ==================== body: coat, apron, belt ====================
BODY = [
    (48, 24, 41), (49, 21, 44), (50, 18, 47), (51, 15, 50), (52, 12, 53), (53, 10, 55),
    (54, 8, 57), (55, 6, 59), (56, 4, 61), (57, 3, 62), (58, 2, 62), (59, 1, 63),
    (60, 0, 63), (61, 0, 63), (62, 0, 63), (63, 0, 63),
]
for (y, x0, x1) in BODY:
    for x in range(x0, x1 + 1):
        d = (((x - 16) ** 2) * 1.0 + ((y - 48) ** 2) * 2.2) ** 0.5
        if d < 7:
            col = CT_LT
        elif d < 12:
            col = CT_MD
        elif d < 17:
            col = CT_SH
        else:
            col = CT_DP
        c.set(x, y, col)

# leather apron
APRON = [(50, 25, 39), (51, 24, 40), (52, 23, 41), (53, 23, 41), (54, 22, 42),
         (55, 22, 42), (56, 21, 43), (57, 21, 43), (58, 21, 43), (59, 21, 43),
         (60, 21, 43), (61, 21, 43), (62, 21, 43), (63, 21, 43)]
for (y, x0, x1) in APRON:
    for x in range(x0, x1 + 1):
        d = (((x - 27) ** 2) * 1.0 + ((y - 50) ** 2) * 2.0) ** 0.5
        col = LT_HI if d < 5 else (LT_MD if d < 9 else (LT_SH if d < 14 else LT_DP))
        c.set(x, y, col)
segs([(26, 49, 24, 48, LT_SH), (38, 49, 41, 48, LT_DP)], LT_DP)
R(49, 26, 38, LT_SH)
for yy in range(51, 64, 2):
    dots([(23, yy), (41, yy)], LT_DP)
dots([(28, 54), (29, 54), (28, 55), (33, 58), (34, 58), (34, 59), (26, 60), (27, 60)], CT_ST2)
dots([(30, 53), (31, 53), (35, 56)], CT_BL)
dots([(29, 54)], BLACK)

# coat lapels + collar
segs([(25, 48, 22, 63, CT_DP), (26, 48, 23, 63, CT_SH)], CT_SH)
segs([(39, 48, 43, 63, CT_DP), (38, 48, 42, 63, CT_SH)], CT_DP)
c.poly([(24, 48), (19, 50), (16, 56), (19, 63), (24, 63), (26, 53)], CT_MD)
c.poly([(40, 48), (46, 50), (48, 56), (46, 63), (41, 63), (38, 53)], CT_SH)
segs([(24, 48, 26, 54, CT_DP), (40, 48, 38, 54, CT_DP)], CT_DP)
c.poly([(24, 47), (28, 46), (31, 48), (26, 50)], CT_LT)
c.poly([(40, 47), (36, 46), (33, 48), (38, 50)], CT_MD)
segs([(24, 47, 26, 50, CT_DP), (40, 47, 38, 50, CT_DP)], CT_DP)

# neck stub between collar tips
RR([(46, 28, 36), (47, 28, 36), (48, 29, 35)], SK_DP)
R(46, 32, 36, MT_DP); R(47, 32, 36, MT_DP); R(48, 32, 35, MT_DP)
R(46, 28, 31, SK_BK)
R(47, 28, 31, SK_SH); R(48, 29, 31, SK_SH)
R(47, 32, 36, MT_SH); R(48, 32, 35, MT_SH)
dots([(31, 46), (33, 46)], MT_BK)

# coat shading + dirt
RR([(58, 2, 6), (59, 1, 5), (60, 0, 4), (61, 0, 3)], CT_DP)
RR([(56, 56, 61), (57, 57, 62), (58, 58, 62), (59, 59, 63), (60, 60, 63), (61, 61, 63)], CT_DP)
dots([(12, 54), (13, 55), (11, 56), (14, 53), (10, 58), (12, 59), (15, 57)], CT_ST1)
dots([(13, 54), (11, 55), (14, 54)], CT_ST2)
dots([(50, 53), (52, 55), (51, 57), (54, 58), (49, 60), (56, 60)], CT_ST1)
dots([(51, 53), (52, 56), (50, 60)], CT_ST2)
dots([(17, 59), (18, 60), (16, 61), (46, 59), (47, 60)], CT_BL)
dots([(18, 58), (48, 58)], CT_ST2)
segs([(14, 52, 11, 58, CT_DP), (16, 51, 14, 56, CT_SH)], CT_DP)
segs([(51, 51, 54, 57, CT_DP)], CT_DP)

# tool belt
R(56, 10, 54, BL_MD)
R(57, 9, 55, BL_MD)
R(58, 8, 56, BL_DP)
dots([(12, 56), (16, 57), (22, 56), (28, 57), (34, 56), (40, 57), (46, 56), (50, 57)], BL_DP)
c.rect(28, 55, 7, 5, BR_MD)
c.rect(29, 56, 5, 3, BR_SH)
c.rect(28, 55, 7, 1, BR_HI)
dots([(28, 55), (34, 55), (28, 59)], BR_HI)
c.rect(30, 57, 2, 1, BR_HI)
c.rect(15, 59, 2, 3, MT_MD); c.rect(15, 59, 1, 3, MT_LT); c.rect(14, 60, 4, 1, MT_SH)
c.rect(42, 59, 2, 3, '#8a5a34'); c.rect(42, 61, 2, 1, MT_HI)
segs([(20, 59, 20, 63, CB_Y), (21, 59, 21, 63, MT_MD)], CB_Y)
segs([(39, 59, 39, 63, CB_R)], CB_R)

# ==================== robotic arm + prosthetic hand ====================
# torn sleeve on the viewer's right
c.poly([(45, 48), (53, 50), (57, 56), (55, 63), (47, 63), (44, 54)], CT_DP)
c.poly([(46, 49), (51, 51), (54, 56), (52, 62), (48, 62), (45, 54)], CT_SH)
segs([(45, 50, 49, 52, CT_DP), (50, 53, 53, 57, CT_DP)], CT_DP)
dots([(46, 48), (48, 49), (50, 50), (52, 51), (53, 53), (54, 55)], CT_ST2)

# shoulder ball joint
c.circle(51, 53, 4, MT_DP)
c.circle(51, 53, 3, MT_MD)
c.circle(50, 52, 1, MT_LT)
dots([(51, 53)], MT_HI)
# upper arm
c.poly([(48, 49), (55, 49), (57, 44), (50, 43)], MT_MD)
R(48, 49, 55, MT_SH); R(47, 48, 55, MT_SH)
segs([(49, 49, 55, 48, MT_DP), (50, 46, 56, 45, MT_DP)], MT_DP)
dots([(49, 48), (50, 47), (51, 45), (53, 44)], MT_HI)
# elbow
c.circle(54, 44, 3, MT_DP)
c.circle(54, 44, 2, MT_MD)
dots([(53, 43)], MT_HI)
# forearm
c.poly([(51, 42), (57, 42), (59, 36), (53, 35)], MT_MD)
R(40, 53, 58, MT_SH); R(39, 53, 58, MT_SH)
R(37, 54, 58, MT_LT)
segs([(52, 41, 58, 40, MT_DP), (53, 38, 58, 37, MT_DP)], MT_DP)
dots([(54, 41), (55, 39), (56, 37)], MT_HI)
segs([(53, 41, 55, 36, MT_LT), (54, 41, 56, 36, MT_SH)], MT_SH)
# wrist ring
R(35, 52, 59, MT_DP); R(34, 52, 59, MT_SH)
dots([(53, 34), (56, 34), (58, 34)], MT_HI)

# prosthetic hand
c.poly([(51, 34), (60, 33), (61, 28), (52, 28)], MT_MD)
c.poly([(52, 33), (59, 32), (60, 29), (53, 29)], MT_LT)
R(31, 53, 59, MT_SH)
# fingers
c.rect(52, 24, 2, 5, MT_MD); c.rect(52, 24, 1, 5, MT_LT); dots([(52, 24), (52, 26)], MT_HI)
c.rect(55, 23, 2, 6, MT_MD); c.rect(55, 23, 1, 6, MT_LT); dots([(55, 23), (55, 26)], MT_HI)
c.rect(58, 24, 2, 5, MT_MD); c.rect(58, 24, 1, 5, MT_LT); dots([(58, 24), (58, 26)], MT_HI)
dots([(53, 26), (56, 25), (59, 26)], MT_DP)
segs([(54, 23, 54, 28, MT_BK), (57, 23, 57, 28, MT_BK)], MT_BK)
# thumb
c.poly([(60, 31), (63, 29), (63, 31), (61, 34)], MT_SH)
dots([(62, 30), (63, 30)], MT_MD)
# knuckle plate
R(28, 52, 60, MT_DP)
dots([(53, 28), (56, 28), (59, 28)], MT_HI)
# glowing palm core
c.circle(56, 31, 1, EY_DK); dots([(56, 31)], EY_MD); dots([(55, 30), (57, 30)], EY_DP)

# cables from the wrist down across the body
segs([(52, 36, 48, 40, CB_K), (48, 40, 45, 45, CB_K), (45, 45, 42, 50, CB_K),
      (42, 50, 39, 54, CB_K)], CB_K)
segs([(51, 37, 47, 41, CB_R), (47, 41, 44, 46, CB_R), (44, 46, 41, 51, CB_R)], CB_R)
dots([(48, 40), (45, 45), (42, 50)], CB_R)
segs([(54, 37, 51, 42, CB_Y), (51, 42, 49, 47, CB_Y)], CB_Y)
segs([(31, 52, 30, 55, CB_K), (30, 55, 32, 59, CB_K)], CB_K)
dots([(30, 53), (31, 57)], CB_B)
c.ellipse(10, 60, 4, 3, CB_K)
c.ellipse(10, 60, 2, 1, BG1)
dots([(7, 59), (13, 61)], CB_R)

# ==================== rim light & contrast pass ====================
segs([(15, 20, 15, 30, SK_HI), (16, 31, 17, 35, SK_HI), (18, 36, 20, 39, SK_HI)], SK_HI)
segs([(12, 14, 11, 20, HR_W), (12, 21, 13, 26, HR_W)], HR_W)
segs([(21, 6, 17, 9, HR_W), (25, 4, 21, 6, HR_W)], HR_W)
segs([(49, 19, 49, 30, MT_LT), (48, 31, 47, 36, MT_LT), (46, 37, 44, 41, MT_MD)], MT_MD)
segs([(52, 14, 52, 20, HR_LT), (52, 21, 52, 25, HR_MD)], HR_MD)
segs([(26, 48, 24, 50, BLACK), (38, 48, 41, 50, BLACK)], BLACK)
R(49, 28, 36, BLACK)
R(48, 28, 31, SK_BK)

dots([(31, 25), (31, 26), (31, 27), (31, 28), (31, 29), (31, 30), (31, 31), (31, 32),
      (31, 33), (31, 34), (31, 35)], SK_DP)
dots([(32, 18), (32, 19), (32, 20)], MT_DP)

print(c.stats_text())
view(c, scale=8)
save("mad_cyborg_scientist", c)
finish(c)
