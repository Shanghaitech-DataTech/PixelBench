# Neighborhood laundromat interior, 64x64
c = new_canvas(64, 64, background=None, name="laundromat")

# ---------- palette ----------
WALL      = c.color("#aebfcb")
WALL_D    = c.color("#93a6b3")
CEIL      = c.color("#5a6a76")
CEIL_D    = c.color("#46545f")
LIGHT     = c.color("#f4fafd")
LIGHT_GLOW= c.color("#d3e2ec")
FLOOR_A   = c.color("#8b99a4")
FLOOR_B   = c.color("#7a8894")
FLOOR_LINE= c.color("#687680")

MACH_BODY = c.color("#eef3f6")
MACH_SHADE= c.color("#c8d5dd")
MACH_HI   = c.color("#ffffff")
MACH_OUT  = c.color("#75848f")
PANEL     = c.color("#33404b")
PANEL_D   = c.color("#222c35")
BTN       = c.color("#3fb8af")
LED       = c.color("#8ceadd")
RIM       = c.color("#8b99a3")
RIM_SH    = c.color("#6b7a85")
RIM_HI    = c.color("#aebbc4")
GLASS     = c.color("#2e4a63")
GLASS_HI  = c.color("#4f7ba0")
GLASS_LO  = c.color("#18293a")

CLOCK_RIM = c.color("#3a4752")
CLOCK_FACE= c.color("#f4f7f9")
HAND      = c.color("#2c3740")

BASKET    = c.color("#c08a4e")
BASKET_D  = c.color("#9c6936")
CLOTH_A   = c.color("#e07070")
CLOTH_B   = c.color("#6fa3d8")
CLOTH_C   = c.color("#e0c060")

TABLE     = c.color("#d9bd94")
TABLE_D   = c.color("#b3986f")
TABLE_LEG = c.color("#66737e")

# ---------- room shell ----------
# wall fills everything first, then ceiling and floor
c.rect(0, 0, 64, 64, WALL)
# ceiling band
c.rect(0, 0, 64, 5, CEIL)
# cool white fluorescent fixture
c.rect(8, 1, 48, 2, LIGHT)
c.rect(8, 3, 48, 1, CEIL_D)
c.line(8, 0, 55, 0, CEIL_D)
# glow on the wall just under the light
c.rect(8, 5, 48, 1, LIGHT_GLOW)

# ---------- wall signs ----------
SIGN_BG   = c.color("#e6edf2")
SIGN_EDGE = c.color("#5d6b76")
SIGN_TXT  = c.color("#3a4a57")
c.rect(3, 6, 25, 9, SIGN_BG)
c.rect(3, 6, 25, 9, SIGN_EDGE, fill=False)
c.text(4, 7, "WASH", SIGN_TXT, font="5x7")
c.rect(37, 6, 25, 9, SIGN_BG)
c.rect(37, 6, 25, 9, SIGN_EDGE, fill=False)
c.text(38, 7, "COIN", SIGN_TXT, font="5x7")

# floor with checker tiles (8x6 px tiles, two rows)
c.rect(0, 52, 64, 12, FLOOR_A)
for tx in range(8):
    for ty in range(2):
        if (tx + ty) % 2 == 0:
            c.rect(tx * 8, 52 + ty * 6, 8, 6, FLOOR_B)
c.line(0, 52, 63, 52, FLOOR_LINE)
c.line(0, 58, 63, 58, FLOOR_LINE)

# ---------- wall clock ----------
cx, cy = 32, 10
c.circle(cx, cy, 4, CLOCK_RIM)
c.circle(cx, cy, 3, CLOCK_FACE)
# tick marks
c.set(cx, cy - 3, HAND)
c.set(cx, cy + 3, HAND)
c.set(cx - 3, cy, HAND)
c.set(cx + 3, cy, HAND)
# hands
c.line(cx, cy, cx, cy - 2, HAND)
c.line(cx, cy, cx + 2, cy + 1, HAND)
c.set(cx, cy, HAND)

# ---------- washing machines ----------
def draw_machine(c, x, y):
    # body
    c.rect(x, y, 16, 18, MACH_BODY)
    # shading for cylindrical depth
    c.rect(x + 12, y + 1, 4, 17, MACH_SHADE)
    c.line(x + 1, y + 17, x + 15, y + 17, MACH_SHADE)
    c.line(x + 1, y + 1, x + 11, y + 1, MACH_HI)
    # control panel
    c.rect(x, y, 16, 4, PANEL)
    c.rect(x, y + 4, 16, 1, PANEL_D)
    c.rect(x + 2, y + 1, 2, 2, BTN)
    c.rect(x + 5, y + 1, 2, 2, LED)
    c.rect(x + 8, y + 1, 5, 2, PANEL_D)
    # front-load door
    c.circle(x + 8, y + 11, 5, RIM)
    c.circle(x + 8, y + 11, 4, GLASS)
    # rim highlight and shade
    c.set(x + 4, y + 7, RIM_HI)
    c.set(x + 5, y + 6, RIM_HI)
    c.set(x + 11, y + 15, RIM_SH)
    c.set(x + 12, y + 14, RIM_SH)
    # glass: cool reflection top-left, shadow bottom
    c.set(x + 6, y + 8, GLASS_HI)
    c.set(x + 7, y + 7, GLASS_HI)
    c.set(x + 8, y + 7, GLASS_HI)
    c.set(x + 9, y + 8, GLASS_HI)
    c.set(x + 7, y + 13, GLASS_LO)
    c.set(x + 8, y + 14, GLASS_LO)
    c.set(x + 9, y + 13, GLASS_LO)
    # laundry visible through the glass
    c.set(x + 6, y + 12, CLOTH_A)
    c.set(x + 8, y + 13, CLOTH_B)
    c.set(x + 10, y + 12, CLOTH_C)
    # door latch handle
    c.set(x + 13, y + 10, MACH_OUT)
    c.set(x + 13, y + 11, MACH_OUT)
    # crisp machine outline keeps units separated
    c.rect(x, y, 16, 18, MACH_OUT, fill=False)

# darker wall gaps between machine columns
for gx in (22, 40):
    c.rect(gx, 15, 2, 37, WALL_D)

# two rows, three machines each
for row_y in (15, 34):
    for col_x in (6, 24, 42):
        draw_machine(c, col_x, row_y)

# ---------- laundry basket (foreground left, on the floor) ----------
c.rect(2, 54, 8, 8, BASKET)
c.rect(2, 54, 8, 1, BASKET_D)      # rim
c.line(2, 56, 9, 56, BASKET_D)     # weave grooves
c.line(2, 58, 9, 58, BASKET_D)
c.line(2, 60, 9, 60, BASKET_D)
c.set(2, 61, BASKET_D)
c.set(9, 61, BASKET_D)
# clothes poking out the top
c.set(3, 53, CLOTH_A)
c.set(4, 52, CLOTH_B)
c.set(5, 53, CLOTH_C)
c.set(6, 52, CLOTH_A)
c.set(7, 53, CLOTH_B)

# ---------- folding table (foreground right, on the floor) ----------
# folded laundry stacked on top
c.rect(53, 52, 4, 3, CLOTH_B)
c.rect(53, 52, 4, 1, "#8fbce0")
c.rect(57, 53, 4, 2, CLOTH_A)
c.rect(57, 53, 4, 1, "#e88f8f")
# table top and legs
c.rect(51, 55, 12, 2, TABLE)
c.line(51, 55, 62, 55, TABLE_D)
c.line(52, 57, 52, 61, TABLE_LEG)
c.line(61, 57, 61, 61, TABLE_LEG)
c.line(53, 61, 60, 61, TABLE_D)

# soft shadows grounding the foreground props
c.rect(2, 62, 8, 1, FLOOR_LINE)
c.rect(51, 62, 12, 1, FLOOR_LINE)

# ---------- observation / export ----------
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

finish(c)
