# Cheerleader character sheet: 4 views in a 2x2 grid on one 64x64 canvas.
out = new_canvas(64, 64, name="cheerleader_4view")

# Shared palette (kept small; far below the 86 visible-colour limit).
out.color("#241a2e", name="outline")
out.color("#f2b38f", name="skin")
out.color("#d98b67", name="skin_shade")
out.color("#f4c44f", name="hair")
out.color("#d9942b", name="hair_shade")
out.color("#ffe08a", name="hair_hi")
out.color("#e63b63", name="red")
out.color("#b3234b", name="red_dark")
out.color("#f7f3ea", name="white")
out.color("#ff6f9f", name="pink")
out.color("#ffd1e0", name="pink_light")
out.color("#3a6ea5", name="eye")
out.color("#ff8ba0", name="blush")


def add_common_details(c, back=False):
    # Uniform trim and skirt pleats.
    if not back:
        c.line(12, 13, 16, 17, "white")
        c.line(20, 13, 16, 17, "white")
        c.line(11, 13, 21, 13, "white")
    else:
        c.line(16, 13, 16, 19, "white")
        c.line(12, 13, 20, 13, "white")
    c.line(9, 20, 23, 20, "white")
    c.line(11, 21, 9, 24, "red_dark")
    c.line(14, 21, 13, 24, "red_dark")
    c.line(18, 21, 19, 24, "red_dark")
    c.line(21, 21, 23, 24, "red_dark")
    c.line(8, 24, 24, 24, "white")
    # Sock stripes and shoe shine.
    c.line(12, 28, 14, 28, "red")
    c.line(17, 28, 19, 28, "red")
    c.set(12, 30, "white")
    c.set(17, 30, "white")


def pom_details(c, x, y):
    c.line(x - 2, y, x + 2, y, "pink_light")
    c.line(x, y - 2, x, y + 2, "pink_light")
    c.line(x - 2, y - 2, x + 2, y + 2, "white")
    c.line(x - 2, y + 2, x + 2, y - 2, "white")
    c.set(x, y, "red_dark")


def front_view():
    c = new_canvas(32, 32, name="front")
    # Hair and twin tails behind the body.
    c.poly([(11, 5), (7, 4), (4, 8), (4, 14), (7, 18), (10, 16), (11, 11)], "hair")
    c.poly([(21, 5), (25, 4), (28, 8), (28, 14), (25, 18), (22, 16), (21, 11)], "hair")
    c.poly([(9, 5), (6, 3), (7, 7)], "red")
    c.poly([(9, 5), (12, 3), (11, 7)], "red")
    c.poly([(23, 5), (20, 3), (21, 7)], "red")
    c.poly([(23, 5), (26, 3), (25, 7)], "red")
    c.ellipse(16, 7, 7, 6, "hair")

    # Body, arms, legs, clothes and pompoms.
    c.rect(14, 12, 4, 3, "skin")
    c.poly([(11, 13), (8, 14), (6, 20), (8, 21), (11, 16)], "skin")
    c.poly([(21, 13), (24, 14), (26, 20), (24, 21), (21, 16)], "skin")
    c.rect(6, 19, 3, 2, "white")
    c.rect(23, 19, 3, 2, "white")
    c.poly([(11, 12), (21, 12), (23, 20), (9, 20)], "red")
    c.rect(12, 24, 3, 6, "skin")
    c.rect(17, 24, 3, 6, "skin")
    c.rect(12, 28, 3, 3, "white")
    c.rect(17, 28, 3, 3, "white")
    c.rect(11, 30, 5, 2, "red_dark")
    c.rect(16, 30, 5, 2, "red_dark")
    c.poly([(9, 19), (23, 19), (26, 25), (6, 25)], "red")
    c.circle(6, 21, 3, "pink")
    c.circle(26, 21, 3, "pink")

    # Face and bangs.
    c.ellipse(16, 8, 5, 5, "skin")
    c.poly([(11, 4), (21, 4), (21, 7), (20, 7), (19, 9), (17, 6), (16, 9), (14, 6), (12, 9), (11, 7)], "hair")

    c.outline("outline")

    # Inner colour work after the dark silhouette.
    c.line(7, 7, 8, 16, "hair_shade")
    c.line(25, 7, 24, 16, "hair_shade")
    c.line(13, 5, 19, 5, "hair_hi")
    c.set(15, 6, "hair_hi")
    add_common_details(c, back=False)
    pom_details(c, 6, 21)
    pom_details(c, 26, 21)

    # Face.
    c.rect(13, 8, 1, 2, "eye")
    c.rect(18, 8, 1, 2, "eye")
    c.set(13, 8, "white")
    c.set(18, 8, "white")
    c.set(12, 10, "blush")
    c.set(20, 10, "blush")
    c.line(15, 11, 17, 11, "red_dark")
    return c


def back_view():
    c = new_canvas(32, 32, name="back")
    # Longer hair seen from behind.
    c.poly([(11, 4), (7, 4), (4, 9), (5, 17), (9, 21), (11, 15)], "hair")
    c.poly([(21, 4), (25, 4), (28, 9), (27, 17), (23, 21), (21, 15)], "hair")
    c.poly([(9, 5), (6, 3), (7, 7)], "red")
    c.poly([(9, 5), (12, 3), (11, 7)], "red")
    c.poly([(23, 5), (20, 3), (21, 7)], "red")
    c.poly([(23, 5), (26, 3), (25, 7)], "red")
    c.ellipse(16, 8, 8, 7, "hair")

    c.rect(14, 13, 4, 2, "skin")
    c.poly([(11, 13), (8, 14), (6, 20), (8, 21), (11, 16)], "skin")
    c.poly([(21, 13), (24, 14), (26, 20), (24, 21), (21, 16)], "skin")
    c.rect(6, 19, 3, 2, "white")
    c.rect(23, 19, 3, 2, "white")
    c.poly([(11, 12), (21, 12), (23, 20), (9, 20)], "red")
    c.rect(12, 24, 3, 6, "skin")
    c.rect(17, 24, 3, 6, "skin")
    c.rect(12, 28, 3, 3, "white")
    c.rect(17, 28, 3, 3, "white")
    c.rect(11, 30, 5, 2, "red_dark")
    c.rect(16, 30, 5, 2, "red_dark")
    c.poly([(9, 19), (23, 19), (26, 25), (6, 25)], "red")
    c.circle(6, 21, 3, "pink")
    c.circle(26, 21, 3, "pink")

    c.outline("outline")

    c.line(16, 3, 16, 14, "hair_shade")
    c.line(12, 6, 11, 15, "hair_shade")
    c.line(20, 6, 21, 15, "hair_shade")
    c.line(7, 8, 8, 19, "hair_shade")
    c.line(25, 8, 24, 19, "hair_shade")
    c.line(13, 4, 19, 4, "hair_hi")
    add_common_details(c, back=True)
    pom_details(c, 6, 21)
    pom_details(c, 26, 21)
    return c


def left_view():
    c = new_canvas(32, 32, name="left")
    # Ponytail and back hair first; the face is added over the front edge.
    c.ellipse(17, 7, 6, 6, "hair")
    c.poly([(20, 4), (26, 7), (27, 14), (23, 19), (19, 14)], "hair")
    c.poly([(22, 5), (19, 3), (20, 7)], "red")
    c.poly([(22, 5), (25, 3), (24, 7)], "red")

    # Far arm and leg (slightly shaded), then near body parts.
    c.poly([(18, 14), (21, 15), (23, 20), (21, 21), (18, 17)], "skin_shade")
    c.circle(23, 21, 2, "pink")
    c.rect(16, 24, 3, 6, "skin_shade")
    c.rect(16, 28, 3, 3, "white")
    c.rect(13, 30, 6, 2, "red_dark")

    c.rect(14, 12, 3, 3, "skin")
    c.poly([(13, 14), (11, 14), (8, 20), (10, 21), (13, 17)], "skin")
    c.rect(8, 19, 3, 2, "white")
    c.poly([(12, 12), (19, 12), (20, 20), (11, 20)], "red")
    c.rect(12, 24, 3, 6, "skin")
    c.rect(12, 28, 3, 3, "white")
    c.rect(9, 30, 6, 2, "red_dark")
    c.poly([(11, 19), (20, 19), (23, 25), (9, 25)], "red")
    c.circle(8, 21, 3, "pink")

    # Profile face, nose and hair cap.
    c.ellipse(15, 8, 5, 5, "skin")
    c.poly([(11, 8), (8, 9), (11, 10)], "skin")
    c.poly([(10, 5), (17, 2), (22, 5), (21, 9), (19, 7), (17, 9), (15, 6), (13, 8), (11, 8)], "hair")

    c.outline("outline")

    # Details.
    c.line(20, 6, 24, 13, "hair_shade")
    c.line(18, 5, 21, 12, "hair_shade")
    c.line(12, 5, 16, 4, "hair_hi")
    c.line(13, 13, 17, 16, "white")
    c.line(12, 13, 19, 13, "white")
    c.line(11, 20, 20, 20, "white")
    c.line(12, 21, 10, 24, "red_dark")
    c.line(16, 21, 16, 24, "red_dark")
    c.line(20, 21, 22, 24, "red_dark")
    c.line(10, 24, 22, 24, "white")
    c.line(12, 28, 14, 28, "red")
    c.line(16, 28, 18, 28, "red")
    c.set(10, 30, "white")
    c.set(14, 30, "white")
    pom_details(c, 8, 21)
    c.line(22, 20, 24, 22, "pink_light")

    # Profile face features (looking left).
    c.rect(12, 8, 1, 2, "eye")
    c.set(12, 8, "white")
    c.set(13, 10, "blush")
    c.line(10, 11, 12, 11, "red_dark")
    return c


front = front_view()
back = back_view()
left = left_view()
right = left.copy(name="right")
right.mirror("h")

# Compose the required 2x2 character sheet: front/back, left/right.
out.blit(front, 0, 0)
out.blit(back, 32, 0)
out.blit(left, 0, 32)
out.blit(right, 32, 32)

view(out)
print(out.stats_text())
finish(out)
