OUT = "#17121c"
ST_L = "#eef3f7"; ST_M = "#aebcc8"; ST_D = "#6d7c8b"
WD_L = "#a9713f"; WD_M = "#7d4f28"; WD_D = "#4f3119"
GD_L = "#f3c75c"; GD_M = "#c8922e"; GD_D = "#8a5f1a"
LE_L = "#7a4530"; LE_D = "#4d2a1d"
BL_L = "#5d93d4"; BL_M = "#3a6cae"; BL_D = "#254a7d"
STR = "#d8d2c4"


def make_sword():
    s = new_canvas(32, 32, name="sword")
    # blade
    s.poly([(15, 2), (18, 8), (18, 20), (12, 20), (12, 8)], OUT)
    s.poly([(15, 4), (17, 9), (17, 19), (13, 19), (13, 9)], ST_M)
    s.line(14, 7, 14, 18, ST_L)
    s.line(16, 10, 16, 18, ST_D)
    s.set(15, 5, ST_L)
    # crossguard
    s.rect(6, 19, 19, 4, OUT)
    s.rect(12, 18, 7, 6, OUT)
    s.line(7, 20, 23, 20, GD_L)
    s.line(7, 21, 23, 21, GD_M)
    s.line(13, 19, 17, 19, GD_L)
    s.line(13, 22, 17, 22, GD_D)
    s.set(6, 20, GD_D); s.set(24, 20, GD_D)
    # grip
    s.rect(13, 22, 5, 7, OUT)
    s.rect(14, 23, 3, 5, LE_L)
    s.line(14, 24, 16, 24, LE_D)
    s.line(14, 26, 16, 26, LE_D)
    # pommel
    s.circle(15, 29, 2, OUT)
    s.circle(15, 29, 1, GD_M)
    s.set(15, 28, GD_L)
    return s


def make_bow():
    b = new_canvas(32, 32, name="bow")
    b.line(11, 3, 11, 29, STR)

    def limb(dx):
        return "M %d 3 C %d 9 %d 23 %d 29" % (11 + dx, 21 + dx, 21 + dx, 11 + dx)

    for dx in (-1, 2):
        b.path(limb(dx), OUT, fill=False)
    b.path(limb(0), WD_L, fill=False)
    b.path(limb(1), WD_M, fill=False)
    # nocks
    b.set(10, 3, OUT); b.set(11, 2, OUT); b.set(12, 2, OUT)
    b.set(10, 29, OUT); b.set(11, 30, OUT); b.set(12, 30, OUT)
    # grip wrap
    b.rect(16, 13, 6, 7, OUT)
    b.rect(17, 14, 4, 5, LE_L)
    b.line(17, 15, 20, 15, LE_D)
    b.line(17, 17, 20, 17, LE_D)
    return b


def make_shield():
    h = new_canvas(32, 32, name="shield")
    h.path("M 4 3 H 27 V 15 C 27 23 20 27 16 29 L 15 29 C 11 27 4 23 4 15 Z", OUT)
    h.path("M 6 5 H 25 V 15 C 25 21.5 19 25 16 27 L 15 27 C 12 25 6 21.5 6 15 Z", GD_M)
    h.path("M 8 7 H 23 V 15 C 23 20 18 23 16 25 L 15 25 C 13 23 8 20 8 15 Z", BL_M)
    h.line(9, 8, 13, 8, BL_L)
    h.line(9, 9, 9, 11, BL_L)
    h.path("M 22 9 V 15 C 22 19.5 18 22 16 24 L 15 24 L 15 23 C 18 21 21 19 21 15 V 9 Z", BL_D)
    # boss
    h.circle(15, 14, 3, OUT)
    h.circle(15, 14, 2, ST_M)
    h.set(14, 13, ST_L)
    h.set(15, 13, ST_L)
    h.set(16, 15, ST_D)
    return h


def make_axe():
    a = new_canvas(32, 32, name="axe")
    # haft
    a.rect(14, 3, 4, 27, OUT)
    a.rect(15, 4, 2, 25, WD_M)
    a.line(15, 4, 15, 28, WD_L)
    # grip wrap at bottom
    a.rect(13, 23, 6, 6, OUT)
    a.rect(14, 24, 4, 4, LE_L)
    a.line(14, 25, 17, 25, LE_D)
    a.line(14, 27, 17, 27, LE_D)

    ah = new_canvas(32, 32, name="axehead")
    ah.path("M 16 9 L 5 3 C 1 8 1 17 5 22 L 16 15 Z", OUT)
    ah.path("M 16 10 L 6.5 4.8 C 3 9 3 16 6.5 20.2 L 16 14 Z", ST_M)
    ah.path("M 6.5 4.8 C 3 9 3 16 6.5 20.2 L 8.4 19.2 C 5.2 15.4 5.2 9.6 8.4 5.8 Z", ST_L)
    ah.path("M 16 13 L 10 16.5 L 11 18 L 16 14.5 Z", ST_D)
    ah.select(0, 0, 16, 32).flip("h").copy_to(16, 0, ah)
    a.blit(ah, 0, 0)
    return a


out = new_canvas(64, 64, name="weapons")
out.blit(make_sword(), 0, 0)
out.blit(make_bow(), 32, 0)
out.blit(make_shield(), 0, 32)
out.blit(make_axe(), 32, 32)

view(out)
print(out.stats_text())
finish(out)
