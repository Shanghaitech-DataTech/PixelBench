DARK     = "#241a14"
SKIN     = "#f2c391"
SKIN_SH  = "#d59a68"
BLUSH    = "#e8907f"
HAIR     = "#5c3a22"
HAIR_HI  = "#7d5430"
BROW     = "#3a2416"
WHITE    = "#fafafa"
PUPIL    = "#2d3a52"
MOUTH_IN = "#5a2328"
MOUTH    = "#8c3f3f"
TEETH    = "#fff4e8"
SHIRT    = "#45699f"
SHIRT_D  = "#2f4b76"
SHIRT_L  = "#5d82bb"


def head(emotion):
    c = new_canvas(32, 32, name="p_" + emotion)

    # ---- outfit / shoulders ----
    c.path("M2 32 L2 28 C4 26 7 25 11 25 L21 25 C25 25 28 26 30 28 L30 32 Z", SHIRT)
    c.poly([(12, 25), (20, 25), (16, 29)], SHIRT_D)
    c.line(3, 31, 3, 28, SHIRT_L)
    c.line(29, 31, 29, 28, SHIRT_L)

    # ---- neck ----
    c.rect(13, 22, 6, 4, SKIN)
    c.rect(13, 22, 6, 2, SKIN_SH)

    # ---- hair silhouette + side locks ----
    c.ellipse(15, 13, 10, 9, HAIR)
    c.rect(4, 13, 3, 9, HAIR)
    c.rect(25, 13, 3, 9, HAIR)

    # ---- face ----
    c.ellipse(15, 15, 8, 8, SKIN)
    c.rect(7, 7, 17, 2, SKIN)   # keep forehead clear of ellipse overshoot
    c.ellipse(15, 15, 8, 8, SKIN)

    # ---- fringe ----
    c.rect(6, 6, 19, 3, HAIR)
    c.rect(6, 9, 4, 2, HAIR)
    c.rect(21, 9, 4, 2, HAIR)
    c.rect(14, 9, 3, 1, HAIR)
    c.line(9, 5, 13, 4, HAIR_HI)
    c.line(18, 4, 21, 5, HAIR_HI)
    c.line(5, 14, 5, 19, HAIR_HI)

    # ---- nose + cheeks ----
    c.rect(15, 17, 1, 2, SKIN_SH)
    c.set(14, 19, SKIN_SH)

    if emotion == "calm":
        c.rect(9, 11, 4, 1, BROW)
        c.rect(18, 11, 4, 1, BROW)
        c.line(9, 13, 12, 13, DARK)
        c.line(18, 13, 21, 13, DARK)
        c.rect(9, 14, 4, 3, WHITE)
        c.rect(18, 14, 4, 3, WHITE)
        c.rect(10, 14, 2, 2, PUPIL)
        c.rect(19, 14, 2, 2, PUPIL)
        c.rect(13, 21, 5, 1, MOUTH_IN)
        c.set(12, 21, MOUTH)
        c.set(19, 21, MOUTH)
        c.set(8, 18, BLUSH)
        c.set(22, 18, BLUSH)

    elif emotion == "smile":
        c.rect(10, 10, 3, 1, BROW)
        c.rect(18, 10, 3, 1, BROW)
        c.line(9, 13, 12, 13, DARK)
        c.line(18, 13, 21, 13, DARK)
        c.rect(9, 14, 4, 2, WHITE)
        c.rect(18, 14, 4, 2, WHITE)
        c.rect(10, 14, 2, 2, PUPIL)
        c.rect(19, 14, 2, 2, PUPIL)
        c.rect(8, 17, 3, 2, BLUSH)
        c.rect(20, 17, 3, 2, BLUSH)
        c.path("M11 20 L20 20 C19 24 12 24 11 20 Z", MOUTH_IN)
        c.rect(12, 20, 7, 1, TEETH)

    elif emotion == "angry":
        c.line(8, 11, 12, 13, BROW)
        c.line(8, 12, 12, 14, BROW)
        c.line(22, 11, 18, 13, BROW)
        c.line(22, 12, 18, 14, BROW)
        c.rect(9, 15, 4, 2, WHITE)
        c.rect(18, 15, 4, 2, WHITE)
        c.rect(10, 15, 2, 2, PUPIL)
        c.rect(19, 15, 2, 2, PUPIL)
        c.poly([(11, 20), (20, 20), (18, 23), (13, 23)], MOUTH_IN)
        c.rect(12, 20, 7, 1, TEETH)
        c.set(8, 18, BLUSH)
        c.set(22, 18, BLUSH)

    else:  # surprised
        c.rect(10, 12, 3, 1, BROW)
        c.rect(18, 12, 3, 1, BROW)
        c.set(9, 13, BROW)
        c.set(21, 13, BROW)
        c.rect(9, 14, 4, 4, WHITE)
        c.rect(18, 14, 4, 4, WHITE)
        c.set(9, 14, SKIN)
        c.set(12, 14, SKIN)
        c.set(18, 14, SKIN)
        c.set(21, 14, SKIN)
        c.set(9, 17, SKIN)
        c.set(12, 17, SKIN)
        c.set(18, 17, SKIN)
        c.set(21, 17, SKIN)
        c.rect(10, 15, 2, 2, PUPIL)
        c.rect(19, 15, 2, 2, PUPIL)
        c.ellipse(15, 21, 2, 2, MOUTH_IN)
        c.set(15, 20, MOUTH)
        c.set(8, 18, BLUSH)
        c.set(22, 18, BLUSH)

    c.outline(DARK)
    return c


result = new_canvas(64, 64, name="emotions")
cells = [("calm", 0, 0), ("smile", 32, 0), ("angry", 0, 32), ("surprised", 32, 32)]
for name, dx, dy in cells:
    result.blit(head(name), dx, dy)

view(result)
print(result.stats_text())
finish(result)
