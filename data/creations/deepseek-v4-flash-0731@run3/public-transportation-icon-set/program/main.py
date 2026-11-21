from pixelbench_api import new_canvas, finish

BG = "#E8EDF2"
CARD = "#FFFFFF"
CSTROKE = "#B9C4D2"
INK = "#1F3A5F"
ACC = "#F2A53C"

c = new_canvas(64, 64, background=BG, name="transit-set")


def round_rect(cv, x, y, w, h, r, col, fill=True):
    d = (f"M {x+r} {y} H {x+w-r} "
         f"A {r} {r} 0 0 1 {x+w} {y+r} "
         f"V {y+h-r} "
         f"A {r} {r} 0 0 1 {x+w-r} {y+h} "
         f"H {x+r} "
         f"A {r} {r} 0 0 1 {x} {y+h-r} "
         f"V {y+r} "
         f"A {r} {r} 0 0 1 {x+r} {y} Z")
    cv.path(d, col, fill=fill)


def thick_line(cv, x0, y0, x1, y1, col, w=2):
    if abs(x1 - x0) >= abs(y1 - y0):
        for oy in range(w):
            cv.line(x0, y0 + oy, x1, y1 + oy, col)
    else:
        for ox in range(w):
            cv.line(x0 + ox, y0, x1 + ox, y1, col)


def card(tx, ty):
    round_rect(c, tx + 2, ty + 2, 28, 28, 7, CARD, True)
    round_rect(c, tx + 2, ty + 2, 28, 28, 7, CSTROKE, False)


def bus(tx, ty):
    # body
    round_rect(c, tx + 5, ty + 8, 22, 12, 3, INK, True)
    c.rect(tx + 7, ty + 10, 4, 4, CARD)
    c.rect(tx + 13, ty + 10, 4, 4, CARD)
    c.rect(tx + 19, ty + 10, 4, 4, CARD)
    c.rect(tx + 22, ty + 14, 3, 5, CARD)   # door
    for wx in (tx + 10, tx + 21):
        c.circle(wx, ty + 21, 2, INK, True)
        c.set(wx, ty + 21, ACC)


def subway(tx, ty):
    round_rect(c, tx + 6, ty + 7, 20, 18, 4, INK, True)
    round_rect(c, tx + 9, ty + 10, 14, 7, 2, CARD, True)   # windshield
    c.rect(tx + 14, ty + 18, 5, 5, CARD)                  # door
    c.rect(tx + 7, ty + 19, 2, 2, ACC)
    c.rect(tx + 23, ty + 19, 2, 2, ACC)


def bike(tx, ty):
    for wx, wy in ((tx + 10, ty + 20), (tx + 22, ty + 20)):
        c.circle(wx, wy, 5, INK, True)
        c.circle(wx, wy, 3, CARD, True)
        c.set(wx, wy, ACC)
    S = (tx + 11, ty + 11)
    H = (tx + 19, ty + 10)
    B = (tx + 15, ty + 17)
    R = (tx + 10, ty + 20)
    F = (tx + 22, ty + 20)
    thick_line(c, S[0], S[1], H[0], H[1], INK)  # top tube
    thick_line(c, H[0], H[1], B[0], B[1], INK)  # down tube
    thick_line(c, S[0], S[1], B[0], B[1], INK)  # seat tube
    thick_line(c, B[0], B[1], R[0], R[1], INK)  # chain stay
    thick_line(c, H[0], H[1], F[0], F[1], INK)  # fork
    c.rect(tx + 9, ty + 9, 5, 2, INK)          # seat
    thick_line(c, tx + 16, ty + 8, tx + 19, ty + 8, INK)  # handlebar


def pedestrian(tx, ty):
    c.circle(tx + 16, ty + 10, 3, INK, True)   # head
    c.rect(tx + 14, ty + 6, 5, 2, ACC)        # cap
    c.rect(tx + 15, ty + 13, 2, 7, INK)       # torso
    thick_line(c, tx + 15, ty + 15, tx + 11, ty + 17, INK)  # back arm
    thick_line(c, tx + 16, ty + 15, tx + 20, ty + 19, INK)  # front arm
    thick_line(c, tx + 15, ty + 19, tx + 11, ty + 25, INK)  # back leg
    thick_line(c, tx + 16, ty + 19, tx + 21, ty + 25, INK)  # front leg


card(0, 0); bus(0, 0)
card(32, 0); subway(32, 0)
card(0, 32); bike(0, 32)
card(32, 32); pedestrian(32, 32)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))

finish(c)
