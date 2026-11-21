# Battery status set -- 64x64, four icons in one horizontal row.
# States: 100% | 60% | 20% | active charging (bolt)
# Every icon shares exactly the same shell geometry.

DARK   = "#1a1c2c"   # outline
INNER  = "#29366f"   # empty interior
GREEN  = "#38b764"   # 100%
LGREEN = "#a7f070"   # 60%
RED    = "#b13e53"   # 20%
YELLOW = "#ffcd75"   # charging bolt

LABELS = True

c = new_canvas(64, 64, name="battery_status_set")

# ---- shared geometry -------------------------------------------------
CAP_TOP, CAP_BOT   = 7, 9        # positive terminal nub
BODY_TOP, BODY_BOT = 10, 46      # outer shell
INN_TOP, INN_BOT   = 11, 45      # interior well
# five 6px bars, 1px gaps, bottom-up  ->  5/5=100%, 3/5=60%, 1/5=20%
SEG = [(40, 45), (33, 38), (26, 31), (19, 24), (12, 17)]
BOLT_Y = 15                      # top of the bolt box (8 x 27)


def shell(x0):
    """Identical battery outline: terminal cap + chamfered body + dark well."""
    c.rect(x0 + 6, CAP_TOP, 4, CAP_BOT - CAP_TOP + 1, DARK)
    c.rect(x0 + 2, BODY_TOP, 12, BODY_BOT - BODY_TOP + 1, DARK)
    for px, py in ((x0 + 2, BODY_TOP), (x0 + 13, BODY_TOP),
                   (x0 + 2, BODY_BOT), (x0 + 13, BODY_BOT)):
        c.set(px, py, None)                      # 1px chamfered corners
    c.rect(x0 + 3, INN_TOP, 10, INN_BOT - INN_TOP + 1, INNER)


def bars(x0, n, colour):
    for i in range(n):
        y0, y1 = SEG[i]
        c.rect(x0 + 3, y0, 10, y1 - y0 + 1, colour)


def bolt(x0, colour):
    rel = [(6, 0), (0, 15), (3, 15), (2, 26), (7, 11), (4, 11)]
    pts = [(x0 + 4 + rx, BOLT_Y + ry) for rx, ry in rel]
    for dx in (-1, 0, 1):                        # dark keying so the bolt
        for dy in (-1, 0, 1):                    # separates from the fill
            if dx or dy:
                c.poly([(x + dx, y + dy) for x, y in pts], DARK, fill=True)
    c.poly(pts, colour, fill=True)


# ---- the four icons --------------------------------------------------
shell(0);   bars(0, 5, GREEN)                    # 100%
shell(16);  bars(16, 3, LGREEN)                  # 60%
shell(32);  bars(32, 1, RED)                     # 20%
shell(48);  bars(48, 2, GREEN); bolt(48, YELLOW) # charging

if LABELS:
    for x0, txt, col, w in ((0, "100", GREEN, 12), (16, "60", LGREEN, 8),
                            (32, "20", RED, 8), (48, "CHG", YELLOW, 12)):
        c.text(x0 + (16 - w) // 2, 49, txt, col, font="8px")

print(c.stats_text())
p = view(c)
print("preview:", p)
save("battery_status_set", c)
finish(c)
