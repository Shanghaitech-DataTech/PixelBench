from pixelbench_api import *

W = H = 32
c = new_canvas(W, H)

# palette
O  = c.color("#161616")  # dark outline
Hl = c.color("#f2f2f2")  # hot highlight
L  = c.color("#dcdcdc")  # light metal
M  = c.color("#bcbcbc")  # mid metal
D  = c.color("#979797")  # dark metal
K  = c.color("#6d6d6d")  # darkest metal
B  = c.color("#202020")  # slot / hole
S  = c.color("#8db8f0")  # strap light
T  = c.color("#4683de")  # strap mid
U  = c.color("#2456a8")  # strap dark
G  = c.color("#43b04e")  # status LED

# ---------- strap loop (bottom layer) ----------
c.rect(11, 26, 12, 6, O)          # loop outline, rows 26..31, cols 11..22
c.rect(12, 27, 10, 4, T)          # blue band rows 27..30, cols 12..21
c.rect(12, 27, 10, 1, S)          # top highlight
c.rect(12, 27, 1, 4, S)           # left highlight
c.rect(21, 27, 1, 4, U)           # right dark
c.rect(14, 28, 6, 2, None)        # loop hole, rows 28..29, cols 14..19

# ---------- keychain ring (in front of loop) ----------
c.circle(16, 24, 3, O)            # ring outer
c.circle(16, 24, 2, D)            # ring metal
c.circle(16, 24, 1, None)         # ring hole

# ---------- metal casing body ----------
c.rect(11, 8, 12, 14, O)          # body outline rows 8..21, cols 11..22
c.rect(12, 9, 10, 12, M)          # interior rows 9..20, cols 12..21
c.rect(12, 8, 10, 1, Hl)          # top cap highlight
c.rect(12, 9, 1, 12, Hl)          # left highlight column
c.rect(13, 9, 1, 12, L)           # col 13
c.rect(18, 9, 4, 12, D)           # cols 18..21 dark
c.rect(20, 9, 2, 12, K)           # cols 20..21 darkest
c.rect(13, 11, 8, 1, K)           # machined groove
# embossed panel
c.rect(13, 13, 8, 3, K)           # recess rows 13..15, cols 13..20
c.rect(14, 14, 6, 2, D)           # recess interior
c.rect(14, 13, 6, 1, L)           # recess top lip
c.rect(14, 14, 1, 2, L)           # recess left lip
c.set(19, 15, B)                  # little screw
c.set(14, 14, B)                  # little screw
c.set(15, 10, G)                  # status LED
# ---------- USB connector ----------
c.rect(13, 2, 8, 7, O)            # shell rows 2..8, cols 13..20
c.rect(14, 3, 6, 5, M)            # shell face
c.rect(14, 3, 6, 1, Hl)           # shell top highlight
c.rect(15, 5, 4, 2, B)            # shell slot
c.rect(14, 7, 6, 1, D)            # shell bottom shade

print(c.stats_text())
print(c.matrix_text(region=(8, 0, 23, 31)))

finish(c)

