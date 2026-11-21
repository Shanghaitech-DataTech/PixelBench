from pixelbench_api import *

def build():
    c = new_canvas(64, 32, name="bus")
    BODY = "#3E9BD9"
    BODY_DARK = "#2C7AB5"
    OUTLINE = "#0E3A5C"
    GLASS = "#223B57"
    GLASS_HI = "#4E6E94"
    WHEEL = "#212121"
    HUB = "#6B6B6B"
    HUB_C = "#2E2E2E"

    body_d = "M4 8 H57 A4 4 0 0 1 61 12 V22 A4 4 0 0 1 57 26 H4 A4 4 0 0 1 1 22 V12 A4 4 0 0 1 4 8 Z"
    c.path(body_d, BODY)
    c.path(body_d, OUTLINE, fill=False)
    c.rect(4, 8, 54, 1, BODY_DARK)

    # windows band (rear, middle, front sections)
    c.rect(6, 10, 18, 5, GLASS)
    c.rect(31, 10, 10, 5, GLASS)
    c.rect(52, 10, 4, 5, GLASS)
    for seg in ((6, 18), (31, 10), (52, 4)):
        c.rect(seg[0], 10, seg[1], 1, GLASS_HI)
    for x in (9, 12, 15, 18, 21):
        c.rect(x, 10, 1, 5, BODY)
    for x in (34, 37, 40):
        c.rect(x, 10, 1, 5, BODY)

    # doors
    c.rect(25, 9, 5, 16, BODY_DARK)
    c.rect(26, 10, 3, 4, GLASS)
    c.rect(26, 10, 3, 1, GLASS_HI)
    c.rect(44, 9, 6, 12, BODY_DARK)
    c.rect(45, 10, 4, 4, GLASS)
    c.rect(45, 10, 4, 1, GLASS_HI)

    c.rect(2, 19, 58, 2, "#FFFFFF")
    c.rect(4, 24, 54, 1, BODY_DARK)
    c.rect(1, 22, 60, 1, OUTLINE)

    for cx in (9, 54):
        c.circle(cx, 25, 5, WHEEL)
        c.circle(cx, 25, 2, HUB)
        c.circle(cx, 25, 1, HUB_C)

    c.rect(49, 6, 8, 2, "#101820")
    c.rect(50, 6, 4, 1, "#FF7A1B")
    c.rect(55, 7, 1, 1, "#FF7A1B")

    c.rect(56, 20, 3, 2, "#FFE066")
    c.rect(58, 19, 2, 2, "#FFE066")

    c.rect(2, 9, 2, 2, "#E33")
    c.rect(2, 20, 2, 2, "#E33")

    c.rect(29, 17, 1, 2, "#1E4E7E")
    c.rect(48, 17, 1, 2, "#1E4E7E")

    c.rect(58, 14, 2, 1, "#FFE066")
    return c

if __name__ == "__main__":
    c = build()
    print(c.stats_text())
    finish(c)
