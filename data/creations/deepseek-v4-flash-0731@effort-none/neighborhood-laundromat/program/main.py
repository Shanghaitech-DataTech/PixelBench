from pixelbench_api import *

c = new_canvas(64, 64, name="laundromat")

WALL       = c.color("#d8e4ec", "wall")
WALL_SHADE = c.color("#b8c8d4", "wall_shade")
FLOOR      = c.color("#8a97a3", "floor")
FLOOR_DARK = c.color("#5c6670", "floor_dark")
CEIL       = c.color("#c6d4de", "ceiling")
MBODY   = c.color("#e9ecef", "mbody")
MBODY_D = c.color("#c3c9cf", "mbody_d")
MFACE   = c.color("#c9d1d8", "mface")
MDARK   = c.color("#3c4650", "mdark")
MGLASS  = c.color("#6b7a88", "mglass")
ACCENT  = c.color("#3d6d9c", "accent")
LED     = c.color("#9fd0ff", "led")
BASKET  = c.color("#7a9b6a", "basket")
BASKET_D= c.color("#5a7a4e", "basket_d")
BASKET_L= c.color("#9fbf8a", "basket_l")
TABLE   = c.color("#9b6b4a", "table")
TABLE_D = c.color("#7a5238", "table_d")
TABLE_L = c.color("#c0936a", "table_l")
LEG     = c.color("#5a432e", "leg")
CLOCK   = c.color("#2a3138", "clock")
CLOCKF  = c.color("#f0f2f4", "clockf")
HAND    = c.color("#20262c", "hand")
LAMP    = c.color("#d9e6f0", "lamp")
LINED   = c.color("#4a5560", "lined")

# ---- base ----
c.rect(0,0,64,64, CEIL)
c.rect(0,0,64,46, WALL)
c.rect(0,46,64,18, FLOOR)

# ---- lighting fixture ----
c.rect(4,2,56,2, LAMP)
c.rect(8,1,48,1, LAMP)

# ---- wall clock (left) ----
c.circle(9, 8, 3, CLOCK)
c.circle(9, 8, 2, CLOCKF)
c.line(9, 8, 9, 7, HAND)
c.line(9, 8, 11, 8, HAND)
c.line(9, 8, 8, 9, HAND)
c.circle(9, 8, 1, CLOCK)

# ---- self-service poster on wall ----
c.rect(50, 4, 8, 8, LAMP)
c.rect(50, 4, 8, 1, ACCENT)
c.rect(50, 11, 8, 1, ACCENT)
c.rect(50, 4, 1, 8, ACCENT)
c.rect(57, 4, 1, 8, ACCENT)
c.rect(52, 6, 4, 1, CLOCK)
c.rect(53, 8, 3, 1, CLOCK)
c.rect(52, 10, 2, 1, CLOCK)

# ---- machine drawing helper ----
def machine(x, top_y, w=16, h=13):
    c.rect(x, top_y, w, h, MBODY)
    c.rect(x, top_y+1, 1, h-2, MBODY_D)
    c.rect(x+1, top_y, w-2, 2, MBODY_D)
    c.rect(x+w-1, top_y+1, 1, h-1, MBODY_D)
    # control strip
    c.rect(x+1, top_y+3, w-2, 3, MFACE)
    c.set(x+w-5, top_y+3, LED)
    c.set(x+w-5, top_y+4, LED)
    c.rect(x+1, top_y+7, w-2, 1, ACCENT)
    # round door
    cx = x + w//2
    cy = top_y + 10
    c.circle(cx, cy, 4, MDARK)
    c.circle(cx, cy, 3, MGLASS)
    c.set(cx-1, cy-1, MBODY)
    c.set(cx, cy-1, MBODY)
    c.rect(x+1, top_y+h-1, w-2, 1, MBODY_D)

# ---- Two rows of front-loading machines ----
# Upper row
machine(4, 13)     # x4  w16 -> 4-19
machine(24, 13)    # 24-39
machine(44, 13)    # 44-59
# upper row bottom edge / shelf between rows
c.rect(0, 26, 64, 2, WALL_SHADE)

# Lower row
machine(4, 30)     # 4-19
machine(24, 30)    # 24-39
machine(44, 30)    # 44-59

# gap shadow between lower machines and floor
c.rect(0, 44, 64, 2, WALL_SHADE)

# ---- floor (baseboard) ----
# soft shadow the machine bank casts onto the floor
c.rect(0, 46, 64, 1, FLOOR_DARK)
c.rect(0, 47, 64, 2, FLOOR_DARK)
# grout lines
for y in range(50,62,4):
    for x in range(0,64,8):
        c.set(x, y, FLOOR_DARK)
    for x in range(4,64,8):
        c.set(x, y+2, FLOOR_DARK)
# floor drain
c.circle(9, 55, 1, FLOOR_DARK)

# ---- folding table (right) ----
tx = 44
ty = 50
tw = 16
# floor shadow under table
c.rect(tx+1, ty+9, tw-2, 2, FLOOR_DARK)
c.rect(tx, ty, tw, 2, TABLE)
c.rect(tx, ty, tw, 1, TABLE_L)
c.rect(tx, ty+2, tw, 1, TABLE_D)
c.rect(tx+1, ty+3, 2, 7, LEG)
c.rect(tx+tw-3, ty+3, 2, 7, LEG)
c.rect(tx+1, ty+9, tw-2, 1, LEG)
c.rect(tx+4, ty-3, 4, 3, LINED)      # folded clothes
c.rect(tx+9, ty-2, 4, 2, BASKET_L)

# ---- laundry basket (left) ----
bx = 8
by = 51
c.rect(bx+1, by+6, 12, 2, FLOOR_DARK)
c.rect(bx, by, 13, 7, BASKET)
c.rect(bx, by, 13, 1, BASKET_L)
c.rect(bx, by+6, 13, 1, BASKET_D)
for i in range(1,6,2):
    c.rect(bx, by+i, 13, 1, BASKET_D)
for x in range(bx+2, bx+12, 4):
    for yy in range(by+1, by+7, 2):
        c.set(x, yy, BASKET_D)
c.rect(bx+2, by-3, 4, 3, LINED)
c.rect(bx+7, by-2, 4, 2, BASKET_L)
c.set(bx+10, by-1, TABLE_L)

finish(c)
