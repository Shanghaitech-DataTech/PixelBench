from pixelbench_api import new_canvas, finish

OUT = "#1a1424"  # dark outline
SK  = "#ffd7ab"  # skin
HA  = "#7a4526"  # brown hair
HS  = "#5f3319"  # hair shadow
HL  = "#91572f"  # hair highlight
RD  = "#d92b2b"  # uniform red
R2  = "#a81e1e"  # dark red
WH  = "#f4f1ea"  # white
PM  = "#ffd23e"  # pom-pom yellow
PS  = "#d69c16"  # pom shadow
EY  = "#241c2e"  # eyes / dark
BL  = "#f2a0a0"  # blush


def body(c, side=False):
    # torso
    if side:
        c.rect(11, 13, 9, 6, RD)
        c.rect(11, 18, 9, 1, WH)
        c.rect(9, 14, 2, 4, SK)
        c.rect(20, 14, 2, 4, SK)
        c.poly([(11, 19), (19, 19), (21, 25), (9, 25)], RD)
        for y in range(20, 25):
            for x in (13, 15, 17):
                c.set(x, y, R2)
        c.rect(9, 26, 3, 4, SK)
        c.rect(17, 26, 3, 4, SK)
        c.rect(9, 28, 3, 2, WH)
        c.rect(17, 28, 3, 2, WH)
        c.rect(7, 30, 6, 2, WH)
        c.rect(16, 30, 6, 2, WH)
        c.rect(7, 31, 6, 1, R2)
        c.rect(16, 31, 6, 1, R2)
        c.ellipse(6, 17, 2, 2, PM)
        c.ellipse(23, 18, 2, 2, PM)
        c.set(6, 18, PS)
        c.set(7, 17, PS)
        c.set(22, 19, PS)
        c.set(23, 19, PS)
    else:
        c.rect(11, 13, 10, 6, RD)
        c.rect(11, 18, 10, 1, WH)
        c.rect(9, 14, 3, 3, SK)
        c.rect(20, 14, 3, 3, SK)
        c.poly([(11, 19), (21, 19), (24, 25), (8, 25)], RD)
        for y in range(20, 25):
            for x in (13, 16, 19):
                c.set(x, y, R2)
        c.rect(12, 26, 3, 4, SK)
        c.rect(17, 26, 3, 4, SK)
        c.rect(12, 28, 3, 2, WH)
        c.rect(17, 28, 3, 2, WH)
        c.rect(10, 30, 6, 2, WH)
        c.rect(16, 30, 6, 2, WH)
        c.rect(10, 31, 6, 1, R2)
        c.rect(16, 31, 6, 1, R2)
        c.ellipse(6, 17, 2, 2, PM)
        c.ellipse(25, 17, 2, 2, PM)
        c.set(6, 18, PS)
        c.set(7, 17, PS)
        c.set(24, 17, PS)
        c.set(25, 18, PS)


def head_front(c):
    c.rect(15, 13, 2, 3, SK)          # neck
    c.ellipse(16, 7, 7, 5, HA)         # hair behind
    c.set(14, 3, HL)
    c.set(15, 4, HL)
    c.ellipse(16, 9, 5, 4, SK)         # face
    c.rect(11, 5, 10, 2, HA)           # bangs
    for x in (11, 12, 15, 16, 17, 20, 21):
        c.set(x, 7, HA)
    c.rect(12, 8, 2, 1, HS)
    c.rect(18, 8, 2, 1, HS)
    c.rect(12, 9, 2, 2, EY)
    c.rect(18, 9, 2, 2, EY)
    c.set(11, 11, BL)
    c.set(20, 11, BL)
    c.rect(15, 12, 3, 1, R2)            # mouth
    c.ellipse(7, 9, 2, 4, HA)           # ponytails
    c.ellipse(25, 9, 2, 4, HA)
    c.set(6, 12, HS)
    c.set(24, 12, HS)


def head_back(c):
    c.ellipse(16, 9, 7, 6, HA)          # hair covering head back
    c.set(14, 3, HL)
    c.set(15, 4, HL)
    c.ellipse(7, 9, 2, 4, HA)
    c.ellipse(25, 9, 2, 4, HA)
    c.set(6, 12, HS)
    c.set(24, 12, HS)
    c.rect(12, 13, 2, 2, WH)            # back straps
    c.rect(18, 13, 2, 2, WH)


def head_left(c):
    c.rect(11, 11, 3, 3, SK)            # neck
    c.ellipse(12, 8, 4, 3, SK)          # face
    c.ellipse(14, 8, 5, 4, HA)          # hair over top/back
    c.ellipse(20, 9, 3, 4, HA)          # ponytail behind
    c.set(18, 12, HS)
    c.set(19, 12, HS)
    c.rect(7, 8, 2, 2, EY)
    c.set(8, 10, R2)                     # mouth
    c.set(8, 11, SK)


front = new_canvas(32, 32)
head_front(front)
body(front)
front.outline(OUT)

back = new_canvas(32, 32)
head_back(back)
body(back)
back.outline(OUT)

left = new_canvas(32, 32)
head_left(left)
body(left, side=True)
left.outline(OUT)

right = left.copy("right")
right.mirror("h")

result = new_canvas(64, 64)
result.blit(front, 0, 0)
result.blit(back, 32, 0)
result.blit(left, 0, 32)
result.blit(right, 32, 32)

print(result.stats_text())
print("PALETTE:", [(p["index"], p["name"], p["rgba"]) for p in result.palette()])
print("front:", front.stats_text())
print("left:", left.stats_text())
print("FRONT")
print(front.matrix_text(indices=True))
print("BACK")
print(back.matrix_text(indices=True))
print("LEFT")
print(left.matrix_text(indices=True))

finish(result)
