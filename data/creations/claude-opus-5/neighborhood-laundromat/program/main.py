c = new_canvas(64, 64, name="output")

# ---- palette ----
WALL_T  = "#dfe6ee"   # upper wall, cool white light
WALL    = "#cdd7e2"
WALL_D  = "#b4c0cf"
TILE_A  = "#9fb0c2"   # wall tile line
FLOOR_A = "#8d9aa8"
FLOOR_B = "#7e8b99"
FLOOR_L = "#a7b4c1"
BASE    = "#6d7a88"

MACH_B  = "#aab6c4"   # machine body
MACH_L  = "#c6d2de"   # machine highlight
MACH_D  = "#7d8a99"   # machine shadow
MACH_E  = "#5d6a78"   # machine edge/separator
DOOR_R  = "#4a5563"   # door ring
GLASS   = "#2f3b49"
GLASS_L = "#5c7a92"
PANEL   = "#e3eaf2"
LED     = "#56d9b0"
LED2    = "#f2c14e"

TBL_T   = "#d8b98a"
TBL_S   = "#b4935f"
TBL_L   = "#8d7148"

BSK_A   = "#4fa3d1"
BSK_B   = "#2f7faf"
LIN_A   = "#f4f6f8"
LIN_B   = "#e7a0b4"
LIN_C   = "#9fd0b6"

CLK_F   = "#f6f8fa"
CLK_R   = "#3c4651"
LAMP    = "#fbfde8"
GLOW    = "#eef3e2"

# ---- wall ----
c.rect(0, 0, 64, 48, WALL)
c.rect(0, 0, 64, 14, WALL_T)
c.line(0, 14, 63, 14, TILE_A)
c.line(0, 33, 63, 33, WALL_D)

# ---- ceiling lamps (cool white) ----
for lx in (10, 31, 52):
    c.rect(lx - 4, 1, 9, 2, LAMP)
    c.rect(lx - 5, 3, 11, 1, GLOW)

# ---- floor: tiles in receding rows ----
c.rect(0, 48, 64, 16, FLOOR_A)
JOINT = FLOOR_L
for y in (53, 58):
    c.line(0, y, 63, y, JOINT)
for y0, y1, step, off in ((49, 53, 11, 3), (54, 58, 14, 8), (59, 64, 18, 1)):
    for x in range(off, 64, step):
        c.line(x, y0, x, y1 - 1, JOINT)
c.line(0, 48, 63, 48, BASE)
# cool light pooling on the floor (under the furniture)
c.line(3, 51, 12, 51, FLOOR_L)
c.line(17, 56, 22, 56, FLOOR_L)
c.line(44, 61, 55, 61, FLOOR_L)

def machine(cv, x, y, w, h, led):
    cv.rect(x, y, w, h, MACH_B)
    cv.line(x, y, x + w - 1, y, MACH_L)          # top lit edge
    cv.line(x, y, x, y + h - 1, MACH_L)          # left lit edge
    cv.line(x + w - 1, y, x + w - 1, y + h - 1, MACH_E)  # right separator
    cv.line(x, y + h - 1, x + w - 1, y + h - 1, MACH_D)  # bottom shade
    # control panel
    cv.rect(x + 2, y + 2, w - 4, 3, PANEL)
    cv.set(x + 2, y + 3, MACH_D)
    cv.set(x + w - 3, y + 3, led)
    # porthole door: octagonal ring with dark glass
    cy = y + h - 6
    cx = x + w // 2
    cv.rect(cx - 3, cy - 2, 7, 5, DOOR_R)
    cv.rect(cx - 2, cy - 3, 5, 7, DOOR_R)
    cv.rect(cx - 2, cy - 1, 5, 3, GLASS)
    cv.rect(cx - 1, cy - 2, 3, 5, GLASS)
    cv.set(cx - 1, cy - 1, GLASS_L)
    cv.set(cx + 2, cy, MACH_L)     # latch highlight
    cv.set(cx - 3, cy + 3, MACH_D) # under-door shade


# bank of machines: two stacked rows, 4 per row
for i in range(4):
    mx = 1 + i * 11
    machine(c, mx, 15, 11, 16, LED if i % 2 == 0 else LED2)
    machine(c, mx, 31, 11, 17, LED2 if i % 2 == 0 else LED)

# ---- shadow under the machine bank ----
c.rect(1, 48, 44, 2, BASE)
c.line(1, 50, 43, 50, FLOOR_B)

# ---- wall clock ----
ccx, ccy = 54, 21
c.circle(ccx, ccy, 6, CLK_R)
c.circle(ccx, ccy, 5, CLK_F)
c.line(ccx, ccy, ccx, ccy - 3, CLK_R)      # minute hand
c.line(ccx, ccy, ccx + 2, ccy + 1, CLK_R)  # hour hand
c.set(ccx, ccy - 4, MACH_E)
c.set(ccx + 4, ccy, MACH_E)
c.set(ccx, ccy + 4, MACH_E)
c.set(ccx - 4, ccy, MACH_E)

# ---- folding table, right wall ----
c.rect(44, 40, 20, 2, TBL_T)      # table top
c.line(44, 42, 63, 42, TBL_S)     # apron
c.rect(47, 43, 2, 13, TBL_L)      # left leg
c.rect(60, 43, 2, 13, TBL_L)
c.line(49, 49, 60, 49, TBL_L)     # cross brace
c.rect(44, 56, 20, 1, BASE)       # contact shadow

# folded laundry stacks on the table
c.rect(47, 36, 7, 4, LIN_A)
c.line(47, 38, 53, 38, LIN_B)
c.line(47, 36, 53, 36, GLOW)
c.rect(56, 37, 6, 3, LIN_C)
c.line(56, 39, 61, 39, BSK_B)

# ---- laundry basket on the floor ----
bx, by = 23, 51
c.poly([(bx, by), (bx + 13, by), (bx + 11, by + 10), (bx + 2, by + 10)], BSK_A)
c.poly([(bx, by), (bx + 13, by), (bx + 11, by + 10), (bx + 2, by + 10)], BSK_B, fill=False)
c.rect(bx + 1, by - 2, 11, 2, LIN_A)       # linen piled above the rim
c.set(bx + 3, by - 3, LIN_A)
c.set(bx + 8, by - 3, LIN_B)
c.set(bx + 9, by - 2, LIN_B)
c.set(bx + 5, by - 2, LIN_C)
c.line(bx + 3, by + 3, bx + 10, by + 3, BSK_B)
c.line(bx + 3, by + 6, bx + 10, by + 6, BSK_B)
c.rect(bx + 1, by + 11, 11, 1, BASE)       # shadow
for wx in (bx + 4, bx + 7, bx + 10):
    c.line(wx, by + 1, wx - 1, by + 9, BSK_B)

# ---- second, smaller basket on the left floor ----
sx, sy = 6, 54
c.poly([(sx, sy), (sx + 9, sy), (sx + 8, sy + 7), (sx + 1, sy + 7)], BSK_B)
c.line(sx + 1, sy + 3, sx + 8, sy + 3, BSK_A)
c.rect(sx + 1, sy - 1, 7, 1, LIN_C)
c.set(sx + 5, sy - 2, LIN_A)
c.rect(sx + 1, sy + 8, 7, 1, BASE)

# ---- coin/soap vending box on the right wall ----
c.rect(46, 29, 7, 10, MACH_B)
c.line(46, 29, 52, 29, MACH_L)
c.line(46, 29, 46, 38, MACH_L)
c.line(53, 29, 53, 39, MACH_E)
c.line(46, 39, 53, 39, MACH_D)
c.rect(47, 31, 5, 3, GLASS)
c.set(48, 31, GLASS_L)
c.rect(47, 36, 5, 1, PANEL)
c.set(51, 37, LED2)

# ---- small detergent bottle beside the table ----
c.rect(41, 52, 4, 5, LED2)
c.rect(42, 50, 2, 2, LIN_A)
c.set(41, 52, "#d9a63c")
c.line(41, 57, 44, 57, BASE)

# ---- row separator across the bank, stronger machine separation ----
c.line(1, 30, 43, 30, MACH_E)
c.line(1, 31, 43, 31, MACH_D)
c.set(0, 15, MACH_E)

# ---- baseboard along the right wall ----
c.rect(44, 46, 20, 2, WALL_D)
c.line(44, 46, 63, 46, TILE_A)

# ---- notice board on the right wall ----
c.rect(45, 5, 13, 8, CLK_F)
c.rect(45, 5, 13, 8, CLK_R, fill=False)
c.line(47, 9, 55, 9, TILE_A)
c.line(47, 11, 54, 11, TILE_A)
c.rect(45, 5, 13, 2, BSK_A)

# ---- cool light pooling on the floor ----
c.line(0, 63, 63, 63, BASE)

view(c)
print(c.stats_text())
finish(c)
