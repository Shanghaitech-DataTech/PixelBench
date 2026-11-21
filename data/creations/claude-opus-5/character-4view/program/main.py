"""64x64 cheerleader girl, four views in a 2x2 grid of 32x32 cells."""

OUT    = "#241b2b"
SKIN   = "#f9d2ac"
SKIN_D = "#d8a079"
HAIR   = "#8f4e24"
HAIR_D = "#60300f"
HAIR_L = "#b87340"
RED    = "#dc3c54"
RED_D  = "#a7243d"
WHT    = "#f8f3f1"
GRY    = "#c6bcc4"
GOLD   = "#ffd24a"
GOLD_D = "#dba026"
PINK   = "#f0898c"

NEI = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def with_outline(art, name):
    """Return a 32x32 canvas: outward dark outline under the art."""
    pal = {p["index"]: p["rgba"] for p in art.palette()}
    base = new_canvas(32, 32, name=name)
    w, h = 32, 32
    solid = []
    for y in range(h):
        for x in range(w):
            rgba = pal.get(art.get(x, y))
            if rgba and rgba[3] > 0:
                solid.append((x, y))
    for (x, y) in solid:
        for dx, dy in NEI:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                base.set(nx, ny, OUT)
    base.blit(art, 0, 0)
    return base


def pompom(c, x, y):
    c.circle(x, y, 3, GOLD)
    c.set(x, y, GOLD_D)
    c.set(x - 2, y - 1, GOLD_D)
    c.set(x + 2, y + 1, GOLD_D)
    c.set(x - 1, y + 2, GOLD_D)
    c.set(x + 1, y - 2, GOLD_D)


def arm(c, sx, sy, wx, wy, col=SKIN):
    c.line(sx, sy, wx, wy, col)
    c.line(sx + 1, sy, wx + 1, wy, col)


def legs_front(c):
    c.rect(11, 26, 3, 3, SKIN)
    c.rect(17, 26, 3, 3, SKIN)
    c.rect(11, 29, 3, 1, WHT)
    c.rect(17, 29, 3, 1, WHT)
    c.rect(10, 30, 5, 1, WHT)
    c.rect(16, 30, 5, 1, WHT)


def shoe_detail(c):
    c.set(11, 29, GRY)
    c.set(13, 29, GRY)
    c.set(17, 29, GRY)
    c.set(19, 29, GRY)


def body_front(c, back=False):
    c.rect(14, 15, 3, 2, SKIN)
    c.poly([(12, 16), (18, 16), (19, 20), (11, 20)], RED)
    c.rect(12, 21, 7, 1, SKIN)
    c.poly([(12, 22), (18, 22), (20, 26), (10, 26)], RED)
    legs_front(c)


def draw_front():
    a = new_canvas(32, 32, name="fa")
    # hair behind
    a.ellipse(9, 13, 2, 4, HAIR)
    a.ellipse(21, 13, 2, 4, HAIR)
    a.ellipse(15, 10, 5, 5, HAIR)
    # face
    a.ellipse(15, 11, 4, 4, SKIN)
    # fringe
    a.rect(11, 7, 9, 2, HAIR)
    for x in (11, 12, 19, 18):
        a.set(x, 9, HAIR)
    a.set(15, 9, HAIR)
    a.set(14, 9, HAIR)
    body_front(a)
    arm(a, 12, 17, 8, 12)
    arm(a, 18, 17, 22, 12)
    pompom(a, 6, 9)
    pompom(a, 24, 9)

    c = with_outline(a, "front")
    # eyes
    c.rect(12, 11, 2, 2, OUT)
    c.rect(17, 11, 2, 2, OUT)
    c.set(12, 11, WHT)
    c.set(17, 11, WHT)
    c.set(15, 13, PINK)
    c.set(11, 13, PINK)
    c.set(19, 13, PINK)
    # hair highlight
    c.line(12, 7, 18, 7, HAIR_L)
    c.set(11, 8, HAIR_L)
    c.set(19, 8, HAIR_L)
    # uniform: V chevron + waistband
    c.line(12, 17, 15, 19, WHT)
    c.line(18, 17, 15, 19, WHT)
    c.set(15, 18, WHT)
    c.rect(12, 20, 7, 1, RED_D)
    # skirt pleats
    for x, y0 in ((13, 23), (15, 23), (17, 23)):
        c.line(x, y0, x, 25, WHT)
    shoe_detail(c)
    return c


def draw_back():
    a = new_canvas(32, 32, name="ba")
    a.ellipse(9, 13, 2, 4, HAIR)
    a.ellipse(21, 13, 2, 4, HAIR)
    a.ellipse(15, 10, 5, 5, HAIR)
    a.rect(11, 10, 9, 5, HAIR)
    body_front(a, back=True)
    arm(a, 12, 17, 8, 12)
    arm(a, 18, 17, 22, 12)
    pompom(a, 6, 9)
    pompom(a, 24, 9)

    c = with_outline(a, "back")
    # hair shading
    c.line(13, 7, 13, 14, HAIR_D)
    c.line(17, 7, 17, 14, HAIR_D)
    c.line(12, 6, 18, 6, HAIR_L)
    # bow on the back of the head
    c.rect(13, 8, 2, 2, RED)
    c.rect(16, 8, 2, 2, RED)
    c.set(15, 9, GOLD)
    c.set(13, 8, RED_D)
    c.set(17, 9, RED_D)
    # back of the uniform: crossed straps
    c.line(12, 17, 18, 19, WHT)
    c.line(18, 17, 12, 19, WHT)
    c.rect(12, 20, 7, 1, RED_D)
    for x in (13, 15, 17):
        c.line(x, 23, x, 25, WHT)
    shoe_detail(c)
    return c


def draw_side():
    """Facing right."""
    a = new_canvas(32, 32, name="sa")
    # far arm raised across the body, with its pompom behind the head
    a.poly([(13, 18), (15, 18), (11, 12), (9, 13)], SKIN_D)
    a.circle(7, 10, 2, GOLD_D)
    # ponytail
    a.ellipse(9, 15, 2, 3, HAIR)
    a.set(9, 18, HAIR)
    # head: hair cap, then the face profile over it
    a.ellipse(15, 10, 4, 4, HAIR)
    a.rect(11, 7, 4, 7, HAIR)
    a.ellipse(16, 11, 3, 3, SKIN)
    a.set(19, 10, SKIN)
    a.set(13, 13, SKIN)
    a.set(13, 12, SKIN)
    # fringe over the forehead
    a.rect(13, 7, 6, 2, HAIR)
    a.set(19, 8, HAIR)
    a.set(19, 9, HAIR)
    a.set(11, 7, None)
    a.set(18, 6, HAIR)
    a.set(17, 6, HAIR)
    a.set(15, 6, HAIR)
    a.set(16, 6, HAIR)
    a.set(13, 6, HAIR)
    a.set(14, 6, HAIR)
    # neck + torso
    a.rect(14, 15, 3, 2, SKIN)
    a.poly([(13, 16), (17, 16), (18, 20), (13, 20)], RED)
    a.rect(13, 21, 5, 1, SKIN)
    a.poly([(13, 22), (17, 22), (19, 26), (11, 26)], RED)
    # legs: far leg set back and darker
    a.rect(13, 26, 2, 3, SKIN_D)
    a.rect(15, 26, 3, 3, SKIN)
    a.rect(13, 29, 2, 1, GRY)
    a.rect(15, 29, 3, 1, WHT)
    a.rect(11, 30, 4, 1, GRY)
    a.rect(15, 30, 6, 1, WHT)
    # near arm out to the side, clear of the chin
    a.poly([(16, 18), (18, 19), (23, 15), (21, 13)], SKIN)
    pompom(a, 26, 12)

    c = with_outline(a, "side_r")
    # separate the arm from the face
    c.line(20, 13, 22, 14, OUT)
    c.set(19, 13, OUT)
    c.set(19, 14, OUT)
    # separate the ponytail from the back of the head
    c.line(11, 13, 11, 15, OUT)
    # profile face details
    c.set(17, 11, OUT)
    c.set(17, 12, OUT)
    c.set(15, 12, PINK)
    c.set(18, 12, SKIN_D)
    # hair highlight and shading
    c.line(13, 7, 18, 7, HAIR_L)
    c.set(12, 8, HAIR_L)
    c.line(12, 10, 12, 12, HAIR_D)
    # uniform
    c.line(14, 17, 16, 19, WHT)
    c.rect(13, 20, 5, 1, RED_D)
    for x in (13, 15, 18):
        c.line(x, 23, x, 25, WHT)
    c.set(13, 29, GRY)
    c.set(16, 29, GRY)
    c.set(18, 29, GRY)
    # hair ribbon at the ponytail base, matching the back view
    c.set(11, 13, RED)
    c.set(10, 13, RED_D)
    return c


front = draw_front()
back = draw_back()
side_r = draw_side()
side_l = side_r.copy(name="side_l")
side_l.mirror("h")

result = new_canvas(64, 64, name="output")
result.blit(front, 0, 0)
result.blit(back, 32, 0)
result.blit(side_l, 0, 32)
result.blit(side_r, 32, 32)

view(result)
print(result.stats_text())
finish(result)
