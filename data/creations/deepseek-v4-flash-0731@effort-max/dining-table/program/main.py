from pixelbench_api import new_canvas, finish
import math

# ---------- palette ----------
OUTLINE    = "#241510"  # dark outline
WOOD       = "#b4773f"  # table top
WOOD_PLANK = "#9a6533"
WOOD_DARK  = "#8f5527"
WOOD_GRAIN = "#7d4a20"
CHAIR_WOOD = "#8a5427"
CUSHION    = "#d16a3f"
CUSHION_DK = "#b6552f"
CUSHION_HI = "#e0855a"
RUG_OUT    = "#c49a63"
RUG_MID    = "#ecd9b4"
RUG_IN     = "#e0c69c"
PLATE      = "#f2e6cc"
PLATE_RIM  = "#d9c49a"
BOWL       = "#f7f1e3"
BOWL_IN    = "#dcc69a"
RED        = "#d4342b"
RED_HI     = "#f0805e"
GREEN      = "#5c9e3e"
ORANGE     = "#f08c24"
YELLOW     = "#f2d43d"
PURPLE     = "#7d4ba8"

c = new_canvas(64, 64, name="dining_table")

# ---------- rug (cozy floor) ----------
c.ellipse(32, 32, 27, 22, RUG_OUT)
c.ellipse(32, 32, 24, 19, RUG_MID)
c.ellipse(32, 32, 20, 15, RUG_IN)
for t in range(8):
    a = t * (2 * math.pi / 8)
    x = round(32 + 21.5 * math.cos(a))
    y = round(32 + 17.5 * math.sin(a))
    c.ellipse(x, y, 1, 1, RUG_OUT)

# ---------- chairs (drawn before table so they tuck under it) ----------
def chair_h(x, y, w, h, back_top=True):
    # back_top: backrest at y, seat at y+h+1 ; else seat at y, backrest at y+h+1
    if back_top:
        by, sy = y, y + h + 1
    else:
        sy, by = y, y + h + 1
    c.rect(x + 1, by, w - 2, h, CHAIR_WOOD)
    c.rect(x + 1, by, w - 2, h, OUTLINE, fill=False)
    c.rect(x, sy, w - 2, h, CUSHION)
    c.rect(x, sy, w - 2, h, OUTLINE, fill=False)
    c.rect(x, sy, w - 2, 2, CUSHION_HI)

def chair_v(x, y, w, h, back_left=True):
    if back_left:
        bx, sx = x, x + w + 1
    else:
        sx, bx = x, x + w + 1
    c.rect(bx, y + 1, w, h - 2, CHAIR_WOOD)
    c.rect(bx, y + 1, w, h - 2, OUTLINE, fill=False)
    c.rect(sx, y, w, h - 2, CUSHION)
    c.rect(sx, y, w, h - 2, OUTLINE, fill=False)
    c.rect(sx, y, w, 2, CUSHION_HI)

# top chair: backrest y5..10, seat y12..17
chair_h(24, 5, 17, 6, True)
# bottom chair: seat y46..51 (tucked under table), backrest y53..58
chair_h(24, 46, 17, 6, False)
# left chair: backrest x4..8, seat x10..14 (tucked under table)
chair_v(4, 24, 5, 17, True)
# right chair: seat x44..49 (tucked under table), backrest x50..54
chair_v(44, 24, 5, 17, False)

# ---------- table ----------
c.rect(14, 17, 36, 30, WOOD)          # x14..49 y17..46
c.rect(15, 18, 34, 28, WOOD_DARK, fill=False)  # rim shadow
for yy in (23, 29, 35, 41):
    c.line(16, yy, 47, yy, WOOD_PLANK)
c.line(18, 24, 18, 27, WOOD_GRAIN)
c.line(45, 24, 45, 27, WOOD_GRAIN)
c.line(20, 37, 20, 39, WOOD_GRAIN)
c.line(31, 24, 31, 26, WOOD_GRAIN)
c.line(37, 36, 37, 39, WOOD_GRAIN)
c.rect(14, 17, 36, 30, OUTLINE, fill=False)

# ---------- plates ----------
def plate(cx, cy):
    c.ellipse(cx, cy, 3, 3, PLATE)
    c.ellipse(cx, cy, 2, 2, PLATE_RIM, fill=False)
    c.ellipse(cx, cy, 3, 3, OUTLINE, fill=False)

plate(32, 20)
plate(32, 42)
plate(20, 31)
plate(44, 31)

# ---------- bowl of fruit ----------
c.ellipse(32, 31, 9, 7, BOWL)
c.ellipse(32, 31, 7, 5, BOWL_IN)
c.ellipse(32, 31, 9, 7, OUTLINE, fill=False)

def fruit(x, y, col, hi=None):
    c.ellipse(x, y, 2, 2, col)
    c.ellipse(x, y, 2, 2, OUTLINE, fill=False)
    if hi:
        c.set(x - 1, y - 1, hi)

# apple (left)
fruit(29, 30, RED, RED_HI)
c.set(28, 28, GREEN)
# orange (right)
fruit(34, 29, ORANGE)
c.set(34, 28, GREEN)
# apple (bottom)
fruit(31, 33, RED, RED_HI)
# banana (top)
c.ellipse(31, 28, 3, 2, YELLOW)
c.line(28, 28, 29, 28, OUTLINE)
c.line(34, 28, 35, 29, OUTLINE)
# grapes
c.ellipse(34, 32, 1, 1, PURPLE)
c.ellipse(36, 31, 1, 1, PURPLE)
c.ellipse(35, 33, 1, 1, PURPLE)

print(c.stats_text())
print(c.matrix_text(region=(4, 5, 59, 58)))
finish(c)
