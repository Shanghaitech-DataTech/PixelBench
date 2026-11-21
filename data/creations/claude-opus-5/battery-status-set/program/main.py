# Battery status set: 100% / 60% / 20% / charging

BG       = "#11151d"
OUTLINE  = "#39425a"
INNER    = "#1b2131"
TICK     = "#242c40"

GREEN    = "#3ddc84"
GREEN_HI = "#8bf5b6"
AMBER    = "#ffc53d"
AMBER_HI = "#ffe28f"
RED      = "#ff5a5f"
RED_HI   = "#ffa0a3"
CYAN     = "#4cc9f0"
CYAN_HI  = "#a7e6fb"
BOLT     = "#ffe066"
BOLT_HI  = "#fff3b0"

# 3x5 glyphs, rows top->bottom
GLYPHS = {
    "0": ["###", "# #", "# #", "# #", "###"],
    "1": [" ##", "  #", "  #", "  #", "  #"],
    "2": ["###", "  #", "###", "#  ", "###"],
    "6": ["###", "#  ", "###", "# #", "###"],
    "Z": [" ##", "## ", "###", " # ", "#  "],   # tiny bolt
}


def glyph(c, x, y, ch, col):
    for ry, row in enumerate(GLYPHS[ch]):
        for rx, p in enumerate(row):
            if p == "#":
                c.set(x + rx, y + ry, col)


def label(c, cx, y, s, col):
    w = len(s) * 3 + (len(s) - 1)
    x = cx - w // 2
    for ch in s:
        glyph(c, x, y, ch, col)
        x += 4


BODY_Y, BODY_H = 14, 32          # outline rect
IN_Y, IN_H = 15, 30             # interior
IN_BOT = IN_Y + IN_H - 1        # 44


def battery(c, x, rows, fill, hi):
    """Identical outline at body x..x+9; `rows` of interior filled from the bottom."""
    # cap
    c.rect(x + 3, BODY_Y - 3, 4, 3, OUTLINE)
    # case + hollow interior
    c.rect(x, BODY_Y, 10, BODY_H, OUTLINE)
    c.rect(x + 1, IN_Y, 8, IN_H, INNER)
    # faint level ticks so the empty part still reads as a battery
    for t in (IN_Y + 6, IN_Y + 12, IN_Y + 18, IN_Y + 24):
        c.line(x + 2, t, x + 7, t, TICK)
    # charge column
    if rows > 0:
        top = IN_BOT - rows + 1
        c.rect(x + 1, top, 8, rows, fill)
        c.line(x + 1, top, x + 8, top, hi)


canvas = new_canvas(64, 64, background=BG, name="battery-status-set")

SLOTS = (3, 19, 35, 51)

battery(canvas, SLOTS[0], 30, GREEN, GREEN_HI)
battery(canvas, SLOTS[1], 18, AMBER, AMBER_HI)
battery(canvas, SLOTS[2], 6, RED, RED_HI)
battery(canvas, SLOTS[3], 14, CYAN, CYAN_HI)

# big lightning bolt in the charging cell
bx = SLOTS[3] + 1          # interior left = 52
canvas.poly([(bx + 5, 16), (bx, 24), (bx + 3, 24), (bx + 1, 30),
             (bx + 7, 22), (bx + 4, 22)], BOLT)
canvas.line(bx + 5, 17, bx + 1, 23, BOLT_HI)

label(canvas, SLOTS[0] + 5, 49, "100", GREEN_HI)
label(canvas, SLOTS[1] + 5, 49, "60", AMBER_HI)
label(canvas, SLOTS[2] + 5, 49, "20", RED_HI)
label(canvas, SLOTS[3] + 5, 49, "Z", BOLT)

view(canvas)
print(canvas.stats_text())
finish(canvas)
