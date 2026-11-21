# 64x64 top-down family dining table sprite
c = new_canvas(64, 64, background=None, name="dining-table")

OUT      = '#241610'   # dark outline
SHADOW   = (20, 12, 8, 70)
WOOD_D   = '#5e3a1c'
WOOD     = '#8b5a2b'
WOOD_L   = '#b07a3e'
CUSH     = '#c14a3a'
CUSH_D   = '#93342a'
RUNNER   = '#d9a94e'
RUNNER_D = '#a8742f'
PLATE    = '#f0e6d0'
BOWL     = '#3a6ea5'
BOWL_L   = '#79a8d8'
BOWL_IN  = '#2a4f78'
RED      = '#d43a2f'
ORANGE   = '#e8902a'
YELLOW   = '#ecd23e'
LEAF     = '#4f8a3d'

# ---------- soft ground shadows ----------
c.rect(15, 18, 38, 34, SHADOW)                       # table
for (x, y, w, h) in [(26, 4, 12, 10), (26, 50, 12, 10), (2, 26, 10, 12), (52, 26, 10, 12)]:
    c.rect(x + 1, y + 2, w, h, SHADOW)               # chairs

# ---------- chairs ----------
# top chair (backrest away from table)
c.rect(26, 4, 12, 10, OUT)
c.rect(27, 5, 10, 8, WOOD)
c.rect(27, 5, 10, 3, WOOD_D)
c.rect(27, 5, 10, 1, WOOD_L)
c.rect(28, 9, 8, 3, CUSH)
c.rect(28, 11, 8, 1, CUSH_D)

# bottom chair (mirrored)
c.rect(26, 50, 12, 10, OUT)
c.rect(27, 51, 10, 8, WOOD)
c.rect(27, 56, 10, 3, WOOD_D)
c.rect(27, 58, 10, 1, WOOD_L)
c.rect(28, 52, 8, 3, CUSH)
c.rect(28, 52, 8, 1, CUSH_D)

# left chair (backrest on outer side)
c.rect(2, 26, 10, 12, OUT)
c.rect(3, 27, 8, 10, WOOD)
c.rect(3, 27, 3, 10, WOOD_D)
c.rect(3, 27, 1, 10, WOOD_L)
c.rect(7, 28, 3, 8, CUSH)
c.rect(9, 28, 1, 8, CUSH_D)

# right chair (mirrored)
c.rect(52, 26, 10, 12, OUT)
c.rect(53, 27, 8, 10, WOOD)
c.rect(57, 27, 3, 10, WOOD_D)
c.rect(59, 27, 1, 10, WOOD_L)
c.rect(54, 28, 3, 8, CUSH)
c.rect(54, 28, 1, 8, CUSH_D)

# ---------- table ----------
c.rect(14, 16, 36, 32, OUT)
# rounded corners
for (px, py) in [(14, 16), (49, 16), (14, 47), (49, 47)]:
    c.set(px, py, None)
for (px, py) in [(15, 15), (48, 15), (15, 48), (48, 48)]:
    c.set(px, py, OUT)
c.rect(15, 17, 34, 30, WOOD)
c.rect(15, 17, 34, 1, WOOD_L)          # top light edge
c.rect(15, 46, 34, 1, WOOD_D)          # bottom shade edge
for py in [23, 30, 37, 43]:            # plank seams
    c.rect(15, py, 34, 1, WOOD_D)
# wood grain dashes
c.rect(18, 20, 3, 1, WOOD_D)
c.rect(40, 19, 3, 1, WOOD_D)
c.rect(21, 26, 3, 1, WOOD_D)
c.rect(44, 26, 2, 1, WOOD_D)
c.rect(18, 40, 3, 1, WOOD_D)
c.rect(40, 41, 4, 1, WOOD_D)
c.rect(24, 45, 3, 1, WOOD_D)
c.rect(24, 18, 3, 1, WOOD_L)
c.rect(20, 36, 3, 1, WOOD_L)

# ---------- table runner ----------
c.rect(16, 29, 32, 6, RUNNER)
c.rect(16, 29, 32, 1, RUNNER_D)
c.rect(16, 34, 32, 1, RUNNER_D)
c.set(15, 30, RUNNER_D)
c.set(15, 33, RUNNER_D)
c.set(48, 30, RUNNER_D)
c.set(48, 33, RUNNER_D)

# ---------- bowl of fruit (centre) ----------
c.circle(32, 32, 7, OUT)
c.circle(32, 32, 6, BOWL)
c.circle(32, 33, 5, BOWL_IN)           # offset inner -> top rim crescent
c.set(30, 26, BOWL_L)                  # rim glints
c.set(29, 27, BOWL_L)
c.set(28, 28, BOWL_L)
c.circle(30, 32, 2, RED)               # apple
c.circle(34, 32, 2, ORANGE)            # orange
c.circle(32, 35, 2, YELLOW)            # lemon
c.circle(32, 30, 2, LEAF)              # green apple
c.set(32, 27, WOOD_D)                  # stem
c.set(29, 31, PLATE)                   # fruit glints
c.set(33, 31, PLATE)
c.set(31, 29, PLATE)
c.set(31, 34, PLATE)

# ---------- place settings ----------
# utensils (cream)
c.rect(26, 20, 1, 3, PLATE)
c.rect(38, 20, 1, 3, PLATE)
c.rect(26, 42, 1, 3, PLATE)
c.rect(38, 42, 1, 3, PLATE)
c.rect(19, 27, 3, 1, PLATE)
c.rect(19, 37, 3, 1, PLATE)
c.rect(43, 27, 3, 1, PLATE)
c.rect(43, 37, 3, 1, PLATE)
# plates with a bite of food
def plate(cx, cy, food):
    c.circle(cx, cy, 3, OUT)
    c.circle(cx, cy, 2, PLATE)
    c.set(cx, cy, food)
plate(32, 21, RED)
plate(32, 43, ORANGE)
plate(20, 32, YELLOW)
plate(44, 32, RED)

view(c)
finish(c)
