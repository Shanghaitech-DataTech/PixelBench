from pixelbench_api import *

CREAM    = '#ebdec0'   # body base
CREAM_HI = '#f4ecdc'   # highlight
SHADOW   = '#d3c39d'   # wing/tail/belly shadow
COMB     = '#c45143'   # comb + wattle
BEAK     = '#e2a85c'   # beak + legs
EYE      = '#3a3029'   # dark eye

W = H = 32
c = new_canvas(W, H)

# --- body and head (plump, soft side view facing left) ---
c.ellipse(17, 18, 9, 8, CREAM)      # body
c.circle(8, 9, 4, CREAM)             # head

# --- tail tuft (right, behind body) ---
c.circle(24, 14, 2, SHADOW)
c.circle(26, 11, 2, SHADOW)
c.circle(27, 17, 2, SHADOW)

# --- comb (on top of head) ---
c.circle(5, 3, 2, COMB)
c.circle(8, 2, 2, COMB)
c.circle(11, 3, 2, COMB)

# --- beak (pointing left) ---
c.poly([(2, 8), (5, 7), (5, 10)], BEAK)

# --- eye ---
c.rect(6, 7, 2, 2, EYE)

# --- wattle ---
c.circle(4, 12, 1, COMB)
c.circle(6, 13, 1, COMB)

# --- body shading (roundness) ---
c.ellipse(16, 14, 4, 2, CREAM_HI)    # shoulder highlight
c.ellipse(16, 24, 6, 2, SHADOW)      # belly shadow

# --- wing ---
c.ellipse(17, 20, 4, 3, SHADOW)

# --- legs and feet ---
c.line(15, 26, 15, 31, BEAK)
c.line(20, 26, 20, 31, BEAK)
c.line(12, 31, 15, 31, BEAK)
c.line(20, 31, 23, 31, BEAK)

# --- tiny eye highlight ---
c.set(7, 7, CREAM_HI)

print(c.stats_text())
finish(c)
