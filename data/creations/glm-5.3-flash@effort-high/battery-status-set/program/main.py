from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, background=None, name="battery_status_set")

OUTLINE = c.color("#3a3f4a", name="outline")
GREEN   = c.color("#4cd964", name="full_green")
YELLOW  = c.color("#f5c542", name="mid_yellow")
RED     = c.color("#e5484d", name="low_red")
DARK    = c.color("#262b33", name="empty_dark")
BOLT    = c.color("#ffd93b", name="bolt_yellow")

Y0 = 27          # top of battery body
BH = 10          # body height
BW = 12          # body width


def battery(cx, mode):
    """cx = horizontal centre of the battery body."""
    x0 = cx - 6
    # interior fill (10 cols wide, 8 rows tall)
    if mode == "full":
        c.rect(cx - 5, Y0 + 1, 10, 8, GREEN)
    elif mode == "mid":
        c.rect(cx - 5, Y0 + 1, 6, 8, YELLOW)
    elif mode == "low":
        c.rect(cx - 5, Y0 + 1, 2, 8, RED)
    elif mode == "charge":
        c.rect(cx - 5, Y0 + 1, 10, 8, DARK)
        # lightning bolt polygon
        c.poly([(cx + 2, 28), (cx - 3, 32), (cx, 32),
                (cx - 1, 35), (cx + 3, 30), (cx, 30)], BOLT, fill=True)
    # identical body outline
    c.rect(x0, Y0, BW, BH, OUTLINE, fill=False)
    # positive terminal nub on the right
    c.rect(cx + 6, Y0 + 3, 2, 4, OUTLINE)


battery(8,  "full")
battery(24, "mid")
battery(40, "low")
battery(56, "charge")

print(c.stats_text())
print(c.matrix_text(region=(0, 24, 63, 40)))
finish(c)
