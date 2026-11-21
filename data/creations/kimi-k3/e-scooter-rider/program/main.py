from pixelbench_api import *

c = new_canvas(32, 32, name="escooter")

# ---- palette ----
K  = '#232634'   # near-black outline / grips / shoes
T  = '#2e3342'   # tire
W  = '#4b5263'   # wheel inner
HB = '#aab4c4'   # hub
D  = '#39404f'   # deck base
A  = '#f2c14e'   # deck accent yellow
M  = '#c7d0dd'   # metal column / handlebar
H  = '#e64545'   # helmet red
HL = '#ff8a75'   # helmet highlight
S  = '#f2c9a2'   # skin
J  = '#2f8fd4'   # jacket blue
JD = '#1c639b'   # jacket shade
P  = '#3a4666'   # pants
SH = (20, 22, 34, 70)   # soft ground shadow
GR = '#8a93a8'   # motion lines

# ---- ground shadow ----
c.ellipse(16, 30, 13, 1, SH)

# ---- wheels ----
for cx in (8, 24):
    c.circle(cx, 27, 3, T)
    c.circle(cx, 27, 2, W)
    c.circle(cx, 27, 1, HB)

# ---- deck ----
c.rect(8, 23, 14, 1, A)    # top accent strip
c.rect(8, 24, 14, 1, D)    # base

# ---- steering column, fork, handlebar ----
c.line(22, 24, 25, 11, M)
c.line(22, 24, 24, 27, M)        # fork to front axle
c.line(24, 10, 26, 10, M)        # handlebar
c.set(27, 10, K)                 # grip at bar end

# ---- rider: legs ----
c.line(13, 16, 12, 19, P)        # back thigh
c.line(12, 19, 11, 21, P)        # back shin
c.line(15, 16, 16, 20, P)        # front thigh
c.line(16, 20, 15, 21, P)        # front shin
c.rect(9, 22, 4, 1, K)           # back shoe
c.rect(13, 22, 4, 1, K)          # front shoe

# ---- rider: torso (leaning forward) ----
c.poly([(13, 16), (16, 9), (19, 10), (16, 16)], J)
c.line(13, 16, 16, 9, JD)        # shaded back edge

# ---- rider: arm to handlebar ----
c.line(18, 10, 23, 10, J)
c.line(18, 11, 22, 11, JD)
c.set(24, 10, S)                 # hand on grip
c.set(24, 11, S)

# ---- rider: head + helmet ----
c.set(18, 8, S)                  # neck
c.set(18, 9, S)
# face
c.set(19, 6, S); c.set(20, 6, K); c.set(21, 6, S)   # eye row
c.set(19, 7, S); c.set(20, 7, S); c.set(21, 7, S)
c.set(19, 8, S); c.set(20, 8, S)
# helmet dome
c.rect(18, 3, 3, 1, H)
c.rect(17, 4, 5, 1, H)
c.rect(17, 5, 5, 1, H)
c.rect(17, 6, 2, 1, H)           # helmet back
c.set(17, 7, H)
c.set(22, 5, H)                  # small visor brim
c.set(18, 3, HL)                 # highlights
c.set(17, 4, HL)

# ---- motion lines ----
c.line(2, 25, 4, 25, GR)
c.line(1, 28, 3, 28, GR)

view(c)
finish(c)
