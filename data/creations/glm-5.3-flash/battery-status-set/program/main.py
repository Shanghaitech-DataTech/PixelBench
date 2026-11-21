# battery-status-set -- four battery icons, one horizontal row, 64x64
# states: 100% | 60% | 20% | active charging

W = H = 64

# ---- palette -------------------------------------------------------------
BG     = "#10141d"   # near-black blue backdrop
LINE   = "#e8edf7"   # battery shell / terminal (identical on all four)
EMPTY  = "#202a3c"   # recessed "no charge" well inside the shell
GREEN  = "#3ddc84"   # 100%
AMBER  = "#ffb020"   # 60%
RED    = "#ff4d4d"   # 20%
BOLT_C = "#ffe14d"   # charging bolt

# ---- geometry ------------------------------------------------------------
BODY_W, BODY_H = 12, 12          # shell body
TERM_W, TERM_H = 2, 4            # positive terminal nub, right side
BODY_Y = 26                      # body rows 26..37  (centred on 31.5)
TERM_Y = BODY_Y + (BODY_H - TERM_H) // 2   # 30..33
SLOT   = 16                      # 1 + i*16  ->  x 1..14, 17..30, 33..46, 49..62

# 4 wide x 8 tall lightning bolt, drawn inside the charging cell
BOLT_ROWS = [
    "..##",
    ".##.",
    "##..",
    "####",
    "..##",
    ".##.",
    "##..",
    "#...",
]
BOLT_OX, BOLT_OY = 3, 1          # offset inside the 10x10 interior -> centred

c = new_canvas(W, H, background=BG, name="battery_status_set")


def battery(bx, fill_colour=None, fill_w=0, bolt=False):
    """One battery shell at x=bx. Identical outline for every state."""
    # shell outline (1 px)
    c.rect(bx, BODY_Y, BODY_W, BODY_H, LINE, fill=False)
    # interior well
    c.rect(bx + 1, BODY_Y + 1, BODY_W - 2, BODY_H - 2, EMPTY)
    # charge bar, anchored left, full interior height
    if fill_w > 0 and fill_colour is not None:
        c.rect(bx + 1, BODY_Y + 1, fill_w, BODY_H - 2, fill_colour)
    # terminal
    c.rect(bx + BODY_W, TERM_Y, TERM_W, TERM_H, LINE)
    # charging bolt
    if bolt:
        for r, row in enumerate(BOLT_ROWS):
            for k, ch in enumerate(row):
                if ch == "#":
                    c.set(bx + 1 + BOLT_OX + k, BODY_Y + 1 + BOLT_OY + r, BOLT_C)


# ---- the four states, left to right --------------------------------------
battery(1,  GREEN, 10)      # 100% - full green bar
battery(17, AMBER, 6)       # 60%  - six tenths, amber
battery(33, RED,   2)       # 20%  - thin red sliver
battery(49, bolt=True)      # active charging - lightning bolt

# ---- inspection -----------------------------------------------------------
print(c.stats_text())
print()
print(c.matrix_text(region=(0, 24, 63, 40)))

# ---- export + submit ------------------------------------------------------
print(save("battery_status_set", c, indexed=True))

finish(c)
