from pixelbench_api import new_canvas, finish

# ---- palette ----
OUT = (26, 26, 26)          # dark outline
SKIN = (246, 198, 166)
SKIN_S = (224, 172, 140)
HAIR = (78, 46, 28)
HAIR_L = (112, 70, 42)
SHIRT = (58, 110, 140)
SHIRT_S = (42, 86, 112)
WHITE = (252, 250, 248)
MOUTH = (150, 54, 54)
TONGUE = (224, 118, 106)
BLUSH = (240, 150, 140)


def draw_span_rows(c, ox, oy, colr, rows, inset=0):
    for y, spans in rows.items():
        if spans and isinstance(spans[0], (list, tuple)):
            for a, b in spans:
                c.line(ox + a + inset, oy + y, ox + b - inset, oy + y, colr)
        else:
            a, b = spans
            c.line(ox + a + inset, oy + y, ox + b - inset, oy + y, colr)


def draw_base(c, ox, oy):
    # torso / outfit (rounded shoulders)
    torso_full = {
        21: [10, 19], 22: [7, 22], 23: [5, 24],
        24: [4, 25], 25: [4, 25], 26: [4, 25],
        27: [4, 25], 28: [4, 25], 29: [4, 25], 30: [4, 25],
    }
    draw_span_rows(c, ox, oy, OUT, torso_full)
    for y, (a, b) in torso_full.items():
        colr = SHIRT_S if y == 21 else SHIRT
        c.line(ox + a + 1, oy + y, ox + b - 1, oy + y, colr)
    # neck
    c.rect(ox + 12, oy + 18, 8, 3, OUT)
    c.rect(ox + 13, oy + 18, 6, 3, SKIN)
    # face
    face_full = {
        4: [10, 19], 5: [8, 21], 6: [7, 22], 7: [6, 23],
        8: [5, 24], 9: [5, 24], 10: [5, 24], 11: [5, 24],
        12: [5, 24], 13: [5, 24], 14: [5, 24], 15: [6, 23],
        16: [7, 22], 17: [8, 21],
    }
    draw_span_rows(c, ox, oy, OUT, face_full)
    draw_span_rows(c, ox, oy, SKIN, face_full, inset=1)
    # jaw shading
    c.line(ox + 7, oy + 15, ox + 8, oy + 15, SKIN_S)
    c.line(ox + 20, oy + 15, ox + 21, oy + 15, SKIN_S)
    # hair
    hair_full = {
        2: [9, 20], 3: [7, 22], 4: [6, 23], 5: [5, 24],
        6: [4, 25], 7: [4, 25],
        8: [[4, 9], [16, 25]], 9: [[4, 8], [17, 25]],
        10: [[4, 7], [22, 25]], 11: [[4, 7], [22, 25]],
        12: [[5, 7], [22, 24]], 13: [[6, 7], [22, 23]],
    }
    draw_span_rows(c, ox, oy, OUT, hair_full)
    draw_span_rows(c, ox, oy, HAIR, hair_full, inset=1)
    # hair shine
    c.line(ox + 9, oy + 4, ox + 11, oy + 4, HAIR_L)
    c.line(ox + 10, oy + 5, ox + 11, oy + 5, HAIR_L)
    c.line(ox + 13, oy + 5, ox + 14, oy + 5, HAIR_L)


def calm(c, ox, oy):
    # straight brows
    c.line(ox + 10, oy + 9, ox + 13, oy + 9, OUT)
    c.line(ox + 16, oy + 9, ox + 19, oy + 9, OUT)
    # eyes
    c.rect(ox + 10, oy + 11, 4, 2, WHITE)
    c.rect(ox + 11, oy + 11, 2, 2, OUT)
    c.rect(ox + 16, oy + 11, 4, 2, WHITE)
    c.rect(ox + 17, oy + 11, 2, 2, OUT)
    # gentle calm mouth
    c.set(ox + 11, oy + 14, OUT)
    c.line(ox + 12, oy + 15, ox + 17, oy + 15, OUT)
    c.set(ox + 18, oy + 14, OUT)


def smile(c, ox, oy):
    # arched brows
    c.set(ox + 10, oy + 9, OUT); c.set(ox + 11, oy + 8, OUT)
    c.set(ox + 12, oy + 8, OUT); c.set(ox + 13, oy + 9, OUT)
    c.set(ox + 16, oy + 9, OUT); c.set(ox + 17, oy + 8, OUT)
    c.set(ox + 18, oy + 8, OUT); c.set(ox + 19, oy + 9, OUT)
    # closed happy eyes
    c.set(ox + 10, oy + 12, OUT); c.set(ox + 11, oy + 11, OUT)
    c.set(ox + 12, oy + 11, OUT); c.set(ox + 13, oy + 12, OUT)
    c.set(ox + 16, oy + 12, OUT); c.set(ox + 17, oy + 11, OUT)
    c.set(ox + 18, oy + 11, OUT); c.set(ox + 19, oy + 12, OUT)
    # blush
    c.set(ox + 7, oy + 14, BLUSH); c.set(ox + 8, oy + 14, BLUSH)
    c.set(ox + 20, oy + 14, BLUSH); c.set(ox + 21, oy + 14, BLUSH)
    # open smiling mouth with tongue
    c.line(ox + 12, oy + 14, ox + 17, oy + 14, OUT)
    c.line(ox + 11, oy + 15, ox + 18, oy + 15, OUT)
    c.line(ox + 11, oy + 16, ox + 18, oy + 16, OUT)
    c.line(ox + 12, oy + 17, ox + 17, oy + 17, OUT)
    c.line(ox + 12, oy + 15, ox + 17, oy + 15, MOUTH)
    c.line(ox + 13, oy + 16, ox + 16, oy + 16, TONGUE)


def angry(c, ox, oy):
    # slanted angry brows
    c.set(ox + 9, oy + 9, OUT); c.set(ox + 10, oy + 9, OUT)
    c.set(ox + 11, oy + 10, OUT); c.set(ox + 12, oy + 10, OUT)
    c.set(ox + 16, oy + 10, OUT); c.set(ox + 17, oy + 10, OUT)
    c.set(ox + 18, oy + 9, OUT); c.set(ox + 19, oy + 9, OUT)
    # narrowed glaring eyes (pupils toward center)
    c.rect(ox + 10, oy + 11, 4, 2, WHITE)
    c.rect(ox + 12, oy + 11, 2, 2, OUT)
    c.rect(ox + 16, oy + 11, 4, 2, WHITE)
    c.rect(ox + 16, oy + 11, 2, 2, OUT)
    # frown
    c.set(ox + 12, oy + 14, OUT)
    c.line(ox + 13, oy + 15, ox + 16, oy + 15, OUT)
    c.set(ox + 17, oy + 14, OUT)
    c.line(ox + 13, oy + 16, ox + 16, oy + 16, MOUTH)


def surprised(c, ox, oy):
    # raised high brows
    c.set(ox + 10, oy + 8, OUT); c.set(ox + 11, oy + 7, OUT)
    c.set(ox + 12, oy + 7, OUT); c.set(ox + 13, oy + 8, OUT)
    c.set(ox + 16, oy + 8, OUT); c.set(ox + 17, oy + 7, OUT)
    c.set(ox + 18, oy + 7, OUT); c.set(ox + 19, oy + 8, OUT)
    # wide eyes
    c.rect(ox + 10, oy + 10, 4, 3, WHITE)
    c.rect(ox + 11, oy + 11, 2, 2, OUT)
    c.rect(ox + 16, oy + 10, 4, 3, WHITE)
    c.rect(ox + 17, oy + 11, 2, 2, OUT)
    # open "o" mouth
    c.line(ox + 12, oy + 14, ox + 17, oy + 14, OUT)
    c.line(ox + 11, oy + 15, ox + 18, oy + 15, OUT)
    c.line(ox + 11, oy + 16, ox + 18, oy + 16, OUT)
    c.line(ox + 12, oy + 17, ox + 17, oy + 17, OUT)
    c.line(ox + 13, oy + 15, ox + 16, oy + 15, MOUTH)
    c.line(ox + 12, oy + 16, ox + 17, oy + 16, MOUTH)


c = new_canvas(64, 64)

draw_base(c, 0, 0)
calm(c, 0, 0)

draw_base(c, 32, 0)
smile(c, 32, 0)

draw_base(c, 0, 32)
angry(c, 0, 32)

draw_base(c, 32, 32)
surprised(c, 32, 32)

print(c.stats_text())
finish(c)
