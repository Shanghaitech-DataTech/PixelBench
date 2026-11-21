c = new_canvas(64, 64, name="battery-status-set")

OUTLINE = "#262626"   # identical dark outline for every battery
GREEN   = "#22c55e"   # 100%
LIME    = "#a3e635"   # 60%
RED     = "#ef4444"   # 20%
BLUE    = "#3b82f6"   # charging fill
YELLOW  = "#facc15"   # lightning bolt

BODY_Y = 21
BODY_H = 22

def battery(x, fill, fill_rect):
    # terminal stub (solid dark, part of the identical outline)
    c.rect(x + 13, 26, 2, 8, OUTLINE)
    # charge fill (inset 1px inside the body outline)
    c.rect(fill_rect[0], fill_rect[1], fill_rect[2], fill_rect[3], fill)
    # body outline, 1px border
    c.rect(x, BODY_Y, 13, BODY_H, OUTLINE, fill=False)

# 100% — full green
battery(3,  GREEN, (4, 22, 11, 20))
# 60%  — lime, bottom 60% of the interior
battery(18, LIME,  (19, 30, 11, 12))
# 20%  — red, bottom 20% of the interior
battery(33, RED,   (34, 38, 11, 4))
# active charging — blue 25% fill + yellow lightning bolt
battery(48, BLUE,  (49, 37, 11, 5))
c.poly([(55, 24), (51, 32), (54, 32), (52, 38), (58, 29), (54, 29)], YELLOW)

print(c.stats_text())
finish(c)
