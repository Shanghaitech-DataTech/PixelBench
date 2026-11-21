from pixelbench_api import *

# Transparent 64x64 icon sheet with four matching horizontal batteries.
result = new_canvas(64, 64, background=None, name="battery-status-set")

INK = "#18212b"
EDGE = "#344250"
HI = "#657381"
EMPTY = "#c4ccd3"
EMPTY_DARK = "#96a1aa"
GREEN = "#35c96f"
GREEN_HI = "#68e494"
AMBER = "#f3b63f"
AMBER_HI = "#ffd66e"
RED = "#ee5261"
RED_HI = "#ff7a84"
CHARGE = "#29bfe8"
CHARGE_HI = "#6ee5ff"
BOLT = "#fff16a"
BOLT_SHADOW = "#d5962f"

xs = [0, 16, 32, 48]

# Identical stepped battery shells. Each body is 13x20 and each cap is 3x8.
for x in xs:
    result.rect(x + 1, 21, 11, 1, INK)
    result.rect(x, 22, 13, 20, INK)
    result.rect(x + 1, 42, 11, 1, INK)
    result.rect(x + 13, 28, 2, 8, INK)
    result.rect(x + 15, 30, 1, 4, INK)

    # Metallic rim lighting shared by every icon.
    result.rect(x + 1, 23, 1, 18, EDGE)
    result.rect(x + 2, 23, 9, 1, HI)
    result.rect(x + 2, 40, 9, 1, EDGE)
    result.rect(x + 12, 24, 1, 16, EDGE)
    result.rect(x + 14, 29, 1, 1, HI)

    # Neutral recessed charge well.
    result.rect(x + 2, 24, 9, 16, EMPTY_DARK)
    result.rect(x + 3, 25, 7, 14, EMPTY)

# Charge fills run left-to-right inside the same 9x16 wells.
# 100 percent.
result.rect(2, 24, 9, 16, GREEN)
result.rect(3, 25, 7, 2, GREEN_HI)
result.rect(3, 27, 1, 12, GREEN_HI)

# 60 percent: five of nine inner columns.
result.rect(18, 24, 5, 16, AMBER)
result.rect(19, 25, 4, 2, AMBER_HI)
result.rect(19, 27, 1, 12, AMBER_HI)
result.rect(23, 25, 1, 14, "#d99432")

# 20 percent: two of nine inner columns.
result.rect(34, 24, 2, 16, RED)
result.rect(35, 25, 1, 14, RED_HI)

# Active charging: electric fill plus a high-contrast pixel lightning bolt.
result.rect(50, 24, 9, 16, CHARGE)
result.rect(51, 25, 7, 2, CHARGE_HI)
result.rect(51, 27, 1, 12, CHARGE_HI)
# One-pixel dark offset keeps the bolt readable against the cyan fill.
result.poly([(55, 25), (52, 32), (55, 32), (53, 39), (59, 30), (56, 30), (58, 25)], BOLT_SHADOW)
result.poly([(55, 25), (53, 31), (56, 31), (54, 37), (58, 30), (55, 30), (57, 25)], BOLT)

view(result, scale=8, margin=0)
finish(result)
