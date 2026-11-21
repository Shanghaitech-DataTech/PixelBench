from pixelbench_api import *

c = new_canvas(32, 32)

SH = c.color((122, 92, 60, 70))   # soft translucent ground shadow
B  = c.color("#F2E4C2")          # body cream
HL = c.color("#FBF4E0")           # highlight
SD = c.color("#D9C59C")           # body bottom shadow
W1 = c.color("#E4CC9E")           # tail / wing
WD = c.color("#C4A878")           # wing shade
R  = c.color("#C25C44")           # comb & wattle
O  = c.color("#E39B3C")           # beak & legs
E  = c.color("#3A2D24")           # eye


def hrow(y, x0, x1, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)


# --- ground shadow (drawn first, under everything) ---
hrow(25, 11, 20, SH)
hrow(26, 12, 18, SH)

# --- tail feathers (left) ---
hrow(13, 3, 5, W1)
hrow(14, 3, 7, W1)
hrow(15, 3, 8, W1)
hrow(16, 3, 8, W1)
hrow(17, 3, 8, W1)
hrow(18, 4, 7, W1)
hrow(19, 5, 6, W1)

# --- body ---
hrow(14, 8, 26, B)
hrow(15, 8, 26, B)
hrow(16, 7, 26, B)
hrow(17, 7, 26, B)
hrow(18, 7, 26, B)
hrow(19, 7, 25, B)
hrow(20, 7, 25, B)
hrow(21, 7, 25, B)
hrow(22, 8, 24, B)
hrow(23, 9, 23, B)
hrow(24, 10, 22, SD)

# --- head (right side, gently raised) ---
hrow(7, 20, 27, B)
hrow(8, 19, 27, B)
hrow(9, 19, 26, B)
hrow(10, 18, 26, B)
hrow(11, 18, 26, B)
hrow(12, 18, 25, B)
hrow(13, 18, 25, B)

# --- comb (three soft bumps) ---
c.set(24, 4, R)
c.set(22, 5, R); c.set(24, 5, R); c.set(26, 5, R)
hrow(6, 21, 27, R)

# --- beak ---
hrow(11, 27, 29, O)
hrow(12, 26, 28, O)

# --- wattle ---
hrow(13, 26, 28, R)
hrow(14, 26, 27, R)

# --- eye (dark oval with a warm glint) ---
hrow(8, 24, 25, E)
c.set(24, 7, HL)

# --- wing (soft teardrop on the body) ---
hrow(17, 13, 18, W1)
hrow(18, 12, 19, W1)
hrow(19, 11, 19, W1)
hrow(20, 12, 18, W1)
hrow(21, 13, 17, W1)
hrow(20, 15, 18, WD)
hrow(21, 15, 16, WD)

# --- gentle highlights ---
hrow(7, 20, 22, HL)
hrow(8, 19, 21, HL)
hrow(14, 11, 14, HL)
hrow(15, 8, 12, HL)
hrow(16, 7, 10, HL)

# --- legs & feet ---
hrow(25, 14, 15, O)
hrow(25, 20, 21, O)
hrow(26, 14, 15, O)
hrow(26, 20, 21, O)
hrow(27, 13, 17, O)
hrow(27, 19, 23, O)

print(c.stats_text())
print(c.matrix_text())
finish(c)
