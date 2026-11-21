# character-emotion-set : 64x64, 2x2 grid of the same character in four emotions
# (calm, smiling, angry, surprised).  Each portrait is drawn on its own 32x32
# tile, given a 1px dark outline, then blitted into the 64x64 result on a
# fully transparent background.

OUT     = "#1b1220"   # dark outline
HAIR    = "#6a45b8"
HAIR_D  = "#452a7d"
HAIR_L  = "#9a78e8"
SKIN    = "#f7cfa4"
SKIN_D  = "#dfa273"
SHIRT   = "#2f8b9c"
COLLAR  = "#e9f2f4"
WHITE   = "#ffffff"
IRIS    = "#231636"
MOUTH   = "#7e2f42"
TONGUE  = "#d9677f"
BLUSH   = "#f0999a"

# front hair: dome with a jagged fringe, drawn over the forehead
FRINGE = ("M 4,13 L 4,7 Q 5,2 16,2 Q 27,2 28,7 L 28,13 "
          "L 26,8 L 23,10 L 20,7 L 16,10 L 12,7 L 9,10 L 6,8 Z")


def draw_base(c):
    """Head / hair / neck / shoulders - identical for every emotion."""
    # hair mass behind the head
    c.ellipse(16, 12, 13, 10, HAIR_D)
    # neck
    c.rect(13, 21, 7, 7, SKIN_D)
    # shoulders (shirt)
    c.poly([(2, 31), (2, 29), (5, 27), (10, 26), (22, 26),
            (27, 27), (30, 29), (30, 31)], SHIRT)
    c.rect(2, 31, 29, 1, SHIRT)
    # collar
    c.poly([(10, 26), (14, 26), (12, 30)], COLLAR)
    c.poly([(18, 26), (22, 26), (20, 30)], COLLAR)
    # face
    c.ellipse(16, 14, 9, 9, SKIN)
    # front hair / fringe
    c.path(FRINGE, HAIR)
    c.rect(9, 2, 15, 1, HAIR)          # flat crown so the top reads clean
    # hair highlight
    c.set(9, 6, HAIR_L)
    c.set(10, 5, HAIR_L)
    c.set(11, 5, HAIR_L)
    c.set(12, 4, HAIR_L)
    # nose
    c.set(16, 17, SKIN_D)


def eye_open(c, x0, y=13, h=3):
    c.rect(x0, y, 5, h, WHITE)
    c.rect(x0 + 1, y, 3, h, IRIS)
    c.set(x0 + 1, y, WHITE)
    c.set(x0 + 3, y + h - 1, HAIR_D)


def feat_calm(c):
    # flat, relaxed brows
    c.rect(9, 11, 5, 1, HAIR_D)
    c.rect(18, 11, 5, 1, HAIR_D)
    # relaxed open eyes
    eye_open(c, 10)
    eye_open(c, 18)
    # straight, small mouth
    c.rect(14, 20, 5, 1, MOUTH)


def feat_happy(c):
    # gently arched, raised brows
    c.set(9, 11, HAIR_D); c.rect(10, 10, 3, 1, HAIR_D); c.set(13, 11, HAIR_D)
    c.set(18, 11, HAIR_D); c.rect(19, 10, 3, 1, HAIR_D); c.set(22, 11, HAIR_D)
    # closed, smiling eyes  ^ ^
    for x0 in (10, 18):
        c.set(x0, 15, IRIS)
        c.rect(x0 + 1, 14, 3, 1, IRIS)
        c.set(x0 + 4, 15, IRIS)
    # blush
    c.rect(8, 17, 3, 1, BLUSH)
    c.rect(21, 17, 3, 1, BLUSH)
    # big open smile: teeth line on top, tongue at the bottom
    c.poly([(12, 18), (20, 18), (19, 19), (18, 20), (16, 21),
            (14, 20), (13, 19)], MOUTH)
    c.rect(13, 18, 7, 1, WHITE)
    c.rect(14, 20, 5, 1, TONGUE)


def feat_angry(c):
    # heavy brows slanting down towards the nose
    for i in range(5):
        yy = 10 + i // 2
        c.set(9 + i, yy, HAIR_D)
        c.set(9 + i, yy + 1, HAIR_D)
        c.set(22 - i, yy, HAIR_D)
        c.set(22 - i, yy + 1, HAIR_D)
    # narrowed eyes with a dark upper lid
    for x0 in (10, 18):
        c.rect(x0, 13, 5, 1, HAIR_D)
        c.rect(x0, 14, 5, 2, WHITE)
        c.rect(x0 + 1, 14, 3, 2, IRIS)
        c.set(x0 + 1, 14, WHITE)
    # gritted teeth
    c.rect(12, 20, 9, 2, MOUTH)
    c.rect(13, 20, 7, 1, WHITE)


def feat_surprised(c):
    # high arched brows
    c.set(9, 11, HAIR_D); c.rect(10, 9, 3, 2, HAIR_D); c.set(13, 11, HAIR_D)
    c.set(18, 11, HAIR_D); c.rect(19, 9, 3, 2, HAIR_D); c.set(22, 11, HAIR_D)
    # wide round eyes with small pupils
    for x0 in (10, 18):
        c.rect(x0, 12, 5, 5, WHITE)
        c.rect(x0 + 1, 13, 3, 3, IRIS)
        c.set(x0 + 1, 13, WHITE)
        c.set(x0 + 3, 15, HAIR_D)
    # round open mouth
    c.ellipse(16, 20, 2, 2, MOUTH)
    c.rect(15, 21, 3, 1, TONGUE)


def add_outline(c):
    """Dilate the silhouette by 1px in the dark outline colour."""
    w, h, data = c.to_rgba()

    def op(x, y):
        if x < 0 or y < 0 or x >= w or y >= h:
            return False
        return data[(y * w + x) * 4 + 3] > 0

    oc = new_canvas(w, h)
    for y in range(h):
        for x in range(w):
            if op(x, y):
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and not op(nx, ny):
                        oc.set(nx, ny, OUT)
    oc.blit(c, 0, 0)
    return oc


FEATS = {"calm": feat_calm, "happy": feat_happy,
         "angry": feat_angry, "surprised": feat_surprised}


def make_face(name):
    c = new_canvas(32, 32)
    draw_base(c)
    FEATS[name](c)
    return add_outline(c)


result = new_canvas(64, 64, name="result")
result.blit(make_face("calm"), 0, 0)
result.blit(make_face("happy"), 32, 0)
result.blit(make_face("angry"), 0, 32)
result.blit(make_face("surprised"), 32, 32)

print(result.stats_text())
print(result.matrix_text(region=(32, 8, 63, 27)))
print(result.matrix_text(region=(0, 40, 31, 59)))
save("character-emotion-set", result)
finish(result)
