# =====================================================================
#  Neighborhood laundromat interior - 64 x 64 pixel art
#  Two rows of front-loading washers, folding table, laundry basket,
#  wall clock, cool white fluorescent lighting.
# =====================================================================

c = new_canvas(64, 64, background=None, name="laundromat")

# ------------------------------------------------------------ palette
CEIL       = c.color("#AFC2D3", "ceil")
WALL_TOP   = c.color("#EAF2F9", "wall_top")
WALL       = c.color("#DDE8F2", "wall")
WALL_LOW   = c.color("#CFDCE8", "wall_low")
CASING     = c.color("#BFD0DF", "light_casing")
CASING_DK  = c.color("#A5B9CB", "light_casing_dk")
LIGHT      = c.color("#FAFDFF", "light_tube")
RIM        = c.color("#3E4E60", "clock_rim")
FACE       = c.color("#FBFDFE", "clock_face")
HAND       = c.color("#33414F", "clock_hand")
FRAME      = c.color("#B4C6D6", "frame")
POSTER_BG  = c.color("#EDF4FA", "poster_bg")
SIGN_BLUE  = c.color("#7FA8CC", "sign_blue")
SKY        = c.color("#C6E0F2", "sky")
SKY_HI     = c.color("#E4F2FC", "sky_hi")
FLOOR      = c.color("#C7D3DF", "floor")
FLOOR_DK   = c.color("#9DAEBF", "floor_dk")
GROUT      = c.color("#B2C0CE", "grout")
SHADOW     = c.color("#A3B4C5", "shadow")
SHADOW2    = c.color("#B7C6D4", "shadow2")
GAP        = c.color("#7E92A5", "machine_gap")
M_DARK     = c.color("#46586B", "machine_edge")
M_BODY     = c.color("#F0F5FA", "machine_body")
M_SHADE    = c.color("#D8E3ED", "machine_shade")
PANEL      = c.color("#DDE7F0", "panel")
PANEL_DK   = c.color("#C2D1DF", "panel_lip")
BTN        = c.color("#8FA6BA", "button")
DISP_RUN   = c.color("#7FE3C4", "disp_run")
DISP_DONE  = c.color("#F2C879", "disp_done")
DISP_OFF   = c.color("#6E8296", "disp_off")
DOOR_RIM   = c.color("#35465A", "door_rim")
GLASS      = c.color("#24374C", "door_glass")
GLASS_HI   = c.color("#6E96BC", "glass_hi")
GLASS_HI2  = c.color("#9CC0DE", "glass_hi2")
CLOTH_W    = c.color("#DCE6EE", "cloth_white")
CLOTH_B    = c.color("#A9C6DC", "cloth_blue")
TABLE_TOP  = c.color("#E8EFF5", "table_top")
TABLE_HI   = c.color("#F5F9FC", "table_hi")
TABLE_EDGE = c.color("#C6D4E1", "table_edge")
TABLE_LEG  = c.color("#9FB2C3", "table_leg")
TOWEL_W    = c.color("#F6FAFD", "towel_white")
TOWEL_WD   = c.color("#D6E2EC", "towel_white_d")
TOWEL_B    = c.color("#BFD8E8", "towel_blue")
TOWEL_BD   = c.color("#9FC0D8", "towel_blue_d")
TOWEL_M    = c.color("#8FB4CE", "towel_mid")
BOTTLE     = c.color("#EDF3F8", "bottle")
BOTTLE_D   = c.color("#CBD9E5", "bottle_shade")
BASKET     = c.color("#6F93AC", "basket")
BASKET_HI  = c.color("#8FB2C8", "basket_hi")
BASKET_DK  = c.color("#55768E", "basket_dk")
CORAL      = c.color("#E4A3A0", "coral")


def cl(v):
    return max(0, min(63, int(round(v))))


# --------------------------------------------------------------- wall
c.rect(0, 0, 64, 28, WALL)
c.rect(0, 0, 64, 7, WALL_TOP)
c.rect(0, 24, 64, 4, WALL_LOW)
c.rect(0, 0, 64, 1, CEIL)

# ------------------------------------------- fluorescent light fixture
c.rect(10, 1, 44, 3, CASING)
c.rect(12, 2, 40, 1, LIGHT)
c.set(11, 2, CASING_DK)
c.set(52, 2, CASING_DK)

# --------------------------------------------------------- wall clock
c.circle(32, 8, 4, RIM)
c.circle(32, 8, 3, FACE)
c.set(32, 5, RIM)            # 12 tick
c.set(35, 8, RIM)            # 3 tick
c.set(32, 11, RIM)           # 6 tick
c.set(29, 8, RIM)            # 9 tick
c.set(32, 6, HAND)           # minute hand
c.set(32, 7, HAND)
c.set(33, 8, HAND)           # hour hand
c.set(34, 8, HAND)
c.set(32, 8, HAND)           # pin

# ------------------------------------------------------ poster (left)
c.rect(5, 4, 12, 9, FRAME)
c.rect(6, 5, 10, 7, POSTER_BG)
c.circle(9, 8, 2, SIGN_BLUE)
c.set(8, 7, POSTER_BG)
c.rect(12, 6, 3, 1, SIGN_BLUE)
c.rect(12, 8, 3, 1, SIGN_BLUE)
c.rect(12, 10, 3, 1, SIGN_BLUE)

# ----------------------------------------------------- window (right)
c.rect(46, 4, 14, 9, FRAME)
c.rect(47, 5, 12, 7, SKY)
c.rect(47, 8, 12, 1, FRAME)
c.rect(52, 5, 1, 7, FRAME)
c.set(48, 6, SKY_HI)
c.set(49, 6, SKY_HI)
c.set(48, 7, SKY_HI)
c.set(55, 10, SKY_HI)
c.set(56, 9, SKY_HI)

# -------------------------------------------------------------- floor
c.rect(0, 28, 64, 36, FLOOR)
c.rect(0, 28, 64, 1, FLOOR_DK)
for m in range(-3, 4):
    c.line(cl(32 + m * 2.5), 29, cl(32 + m * 11.0), 63, GROUT)
for y in (35, 42, 50, 58):
    c.rect(0, y, 64, 1, GROUT)
c.rect(0, 29, 64, 1, SHADOW)          # shadow band at wall base

# --------------------------------------------- back row of 4 washers
BACK_XS = [1, 17, 33, 49]
for gx in (14, 30, 46):               # recessed slots between them
    c.rect(gx, 13, 3, 16, GAP)


def back_washer(mx, disp):
    my, w, h = 13, 13, 16
    c.rect(mx, my, w, h, M_DARK)
    c.rect(mx + 1, my + 1, w - 2, h - 2, M_BODY)
    c.rect(mx + w - 3, my + 4, 2, h - 5, M_SHADE)
    c.rect(mx + 1, my + 1, w - 2, 2, PANEL)
    c.rect(mx + 1, my + 3, w - 2, 1, PANEL_DK)
    c.rect(mx + 2, my + 1, 3, 1, disp)
    c.set(mx + 8, my + 1, BTN)
    c.set(mx + 10, my + 1, BTN)
    c.circle(mx + 6, my + 9, 4, DOOR_RIM)
    c.circle(mx + 6, my + 9, 3, GLASS)
    c.set(mx + 4, my + 7, GLASS_HI2)
    c.set(mx + 3, my + 8, GLASS_HI2)
    c.set(mx + 4, my + 9, GLASS_HI)


back_washer(1,  DISP_OFF)
back_washer(17, DISP_RUN)
back_washer(33, DISP_OFF)
back_washer(49, DISP_RUN)

# -------------------------------------------- front row of 2 washers
FRONT_XS = [2, 20]
c.rect(17, 30, 3, 24, SHADOW)         # shadowed slot between them


def front_washer(mx, disp, clothes=False):
    my, w, h = 30, 15, 24
    c.rect(mx, my, w, h, M_DARK)
    c.rect(mx + 1, my + 1, w - 2, h - 2, M_BODY)
    c.rect(mx + w - 3, my + 4, 2, h - 6, M_SHADE)
    c.rect(mx + 1, my + 1, w - 2, 3, PANEL)
    c.rect(mx + 1, my + 4, w - 2, 1, PANEL_DK)
    c.rect(mx + 2, my + 1, 4, 1, disp)
    c.set(mx + 9, my + 2, BTN)
    c.set(mx + 11, my + 2, BTN)
    c.set(mx + 13, my + 2, BTN)
    c.circle(mx + 7, my + 12, 5, DOOR_RIM)
    c.circle(mx + 7, my + 12, 4, GLASS)
    c.set(mx + 5, my + 9, GLASS_HI2)
    c.set(mx + 4, my + 10, GLASS_HI2)
    c.set(mx + 5, my + 11, GLASS_HI)
    if clothes:
        c.set(mx + 8, my + 14, CLOTH_W)
        c.set(mx + 9, my + 15, CLOTH_B)
        c.set(mx + 7, my + 15, CLOTH_W)
    c.rect(mx + 2, my + h - 3, w - 4, 1, M_SHADE)


front_washer(2,  DISP_RUN)
front_washer(20, DISP_DONE, clothes=True)
c.rect(2, 54, 33, 1, SHADOW)
c.rect(4, 55, 29, 1, SHADOW2)

# ------------------------------------------------------ folding table
c.rect(40, 54, 22, 1, SHADOW)
c.rect(41, 41, 2, 13, TABLE_LEG)
c.rect(59, 41, 2, 13, TABLE_LEG)
c.rect(43, 48, 16, 1, TABLE_LEG)
c.rect(39, 37, 24, 4, TABLE_TOP)
c.rect(39, 37, 24, 1, TABLE_HI)
c.rect(39, 40, 24, 1, TABLE_EDGE)

# folded towels on the table
c.rect(41, 34, 7, 3, TOWEL_W)
c.rect(41, 36, 7, 1, TOWEL_WD)
c.rect(42, 32, 6, 2, TOWEL_B)
c.rect(42, 33, 6, 1, TOWEL_BD)
c.rect(43, 31, 4, 1, TOWEL_M)
c.rect(50, 34, 6, 3, TOWEL_B)
c.rect(50, 36, 6, 1, TOWEL_BD)
c.rect(51, 33, 4, 1, TOWEL_W)
# detergent jug on the table
c.rect(57, 32, 4, 5, BOTTLE)
c.rect(58, 30, 2, 2, SIGN_BLUE)
c.rect(57, 34, 4, 2, SIGN_BLUE)
c.rect(60, 32, 1, 5, BOTTLE_D)

# ----------------------------------------------------- laundry basket
c.rect(3, 61, 20, 2, SHADOW)
c.rect(7, 50, 4, 3, CLOTH_W)
c.rect(12, 49, 5, 4, CLOTH_B)
c.rect(17, 50, 3, 3, CORAL)
c.set(11, 51, CLOTH_W)
c.set(14, 50, CLOTH_W)
for i, y in enumerate(range(53, 63)):
    inset = i // 3
    x0, x1 = 4 + inset, 21 - inset
    c.rect(x0, y, x1 - x0 + 1, 1, BASKET)
c.rect(4, 53, 18, 1, BASKET_HI)
c.rect(7, 62, 12, 1, BASKET_DK)
for y in range(53, 63):
    inset = (y - 53) // 3
    c.set(21 - inset, y, BASKET_DK)
    if y > 53:
        c.set(4 + inset, y, BASKET_HI)
for y in (56, 58, 60):
    for x in (9, 12, 15, 18):
        c.set(x, y, BASKET_DK)
c.set(19, 53, CORAL)
c.set(19, 54, CORAL)

# ------------------------------------------- detergent jug on floor
c.rect(34, 62, 7, 1, SHADOW)
c.rect(35, 57, 4, 5, BOTTLE)
c.rect(36, 55, 2, 2, SIGN_BLUE)
c.rect(35, 59, 4, 2, TOWEL_B)
c.rect(38, 57, 1, 5, BOTTLE_D)

# ------------------------------------------------------------- report
print(c.stats_text())
print(c.matrix_text(region=(0, 40, 63, 63)))

finish(c)
