from pixelbench_api import new_canvas, finish

OUT = "#1A1410"
SKIN = "#F2C69E"
SKIN_SH = "#D8A878"
HAIR = "#5E3C28"
HAIR_D = "#42271B"
HAIR_H = "#7C5434"
SHIRT = "#3E6DB5"
SHIRT_D = "#2B4E82"
COLLAR = "#F5F7FA"
EYE = "#241812"
MOUTH = "#B03A30"
MOUTH_D = "#641F1C"
BLUSH = "#F2908C"
WHITE = "#FFFFFF"

c = new_canvas(64, 64, name="emotion-set")

def prt(cx, cy, emo):
    # ---- outfit / shoulders ----
    c.rect(cx + 2, cy + 23, 28, 8, OUT)          # outline
    c.rect(cx + 3, cy + 24, 26, 6, SHIRT)
    c.rect(cx + 3, cy + 29, 26, 1, SHIRT_D)
    c.rect(cx + 7,  cy + 24, 18, 1, COLLAR)
    c.rect(cx + 10, cy + 25, 12, 1, COLLAR)
    c.rect(cx + 12, cy + 26, 8, 1, COLLAR)
    # ---- head ----
    c.ellipse(cx + 15, cy + 15, 11, 8, OUT)
    c.ellipse(cx + 15, cy + 15, 10, 7, SKIN)
    # ---- hair ----
    c.rect(cx + 4, cy + 3, 23, 11, OUT)
    c.rect(cx + 5, cy + 4, 21, 9, HAIR)
    c.rect(cx + 4, cy + 11, 3, 5, OUT)
    c.rect(cx + 5, cy + 12, 1, 3, HAIR)
    c.rect(cx + 24, cy + 11, 3, 5, OUT)
    c.rect(cx + 25, cy + 12, 1, 3, HAIR)
    # shine
    for x in (8, 9, 10):
        c.set(cx + x, cy + 6, HAIR_H)
    # ---- brows ----
    if emo in ("calm", "smile"):
        for x in range(9, 13):
            c.set(cx + x, cy + 14, HAIR_D)
        for x in range(19, 23):
            c.set(cx + x, cy + 14, HAIR_D)
    elif emo == "angry":
        for x in range(9, 11):
            c.set(cx + x, cy + 13, HAIR_D)
        for x in range(11, 13):
            c.set(cx + x, cy + 14, HAIR_D)
        for x in range(19, 21):
            c.set(cx + x, cy + 14, HAIR_D)
        for x in range(21, 23):
            c.set(cx + x, cy + 13, HAIR_D)
    else:  # surprised: raised arched brows
        for x in range(9, 13):
            c.set(cx + x, cy + 13, HAIR_D)
        for x in range(19, 23):
            c.set(cx + x, cy + 13, HAIR_D)
    # ---- eyes ----
    if emo == "calm":
        c.set(cx + 10, cy + 16, WHITE)
        c.set(cx + 11, cy + 16, EYE)
        c.set(cx + 20, cy + 16, EYE)
        c.set(cx + 21, cy + 16, WHITE)
    elif emo == "smile":
        for x, y in ((9, 15), (12, 15), (19, 15), (22, 15)):
            c.set(cx + x, cy + y, EYE)
        for x in range(9, 13):
            c.set(cx + x, cy + 16, EYE)
        for x in range(19, 23):
            c.set(cx + x, cy + 16, EYE)
    elif emo == "angry":
        for x in range(9, 12):
            c.set(cx + x, cy + 16, EYE)
        for x in range(20, 23):
            c.set(cx + x, cy + 16, EYE)
    else:  # surprised: wide round eyes
        for x in range(9, 12):
            for y in range(15, 18):
                c.set(cx + x, cy + y, EYE)
        c.set(cx + 9,  cy + 15, WHITE)
        c.set(cx + 10, cy + 16, WHITE)
        c.set(cx + 11, cy + 17, WHITE)
        for x in range(20, 23):
            for y in range(15, 18):
                c.set(cx + x, cy + y, EYE)
        c.set(cx + 20, cy + 15, WHITE)
        c.set(cx + 21, cy + 16, WHITE)
        c.set(cx + 22, cy + 17, WHITE)
    # ---- mouth ----
    if emo == "calm":
        for x in range(13, 19):
            c.set(cx + x, cy + 18, OUT)
        for x in range(14, 18):
            c.set(cx + x, cy + 19, MOUTH)
    elif emo == "smile":
        for x in range(13, 19):
            c.set(cx + x, cy + 18, OUT)
        for x in range(14, 19):
            c.set(cx + x, cy + 19, MOUTH_D)
        for x in range(13, 19):
            c.set(cx + x, cy + 20, MOUTH)
        c.set(cx + 15, cy + 19, WHITE)
        c.set(cx + 16, cy + 19, WHITE)
    elif emo == "angry":
        for x in range(13, 19):
            c.set(cx + x, cy + 18, OUT)
        for x in range(13, 19):
            c.set(cx + x, cy + 19, MOUTH)
        for x in range(14, 18):
            c.set(cx + x, cy + 20, MOUTH_D)
        c.set(cx + 13, cy + 20, OUT)
        c.set(cx + 18, cy + 20, OUT)
    else:  # surprised: open mouth
        for x in range(13, 19):
            c.set(cx + x, cy + 18, OUT)
        for x in range(14, 18):
            c.set(cx + x, cy + 19, MOUTH_D)
        for x in range(13, 19):
            c.set(cx + x, cy + 20, MOUTH)
        c.set(cx + 13, cy + 19, OUT)
        c.set(cx + 18, cy + 19, OUT)
    # blush (smiling)
    if emo == "smile":
        c.set(cx + 7, cy + 17, BLUSH)
        c.set(cx + 8, cy + 17, BLUSH)
        c.set(cx + 23, cy + 17, BLUSH)
        c.set(cx + 24, cy + 17, BLUSH)

prt(0, 0, "calm")
prt(32, 0, "smile")
prt(0, 32, "angry")
prt(32, 32, "surprised")

print(c.stats_text())
print("===== angry =====")
print(c.matrix_text(region=(0, 32, 31, 63)))
for name, (rx, ry) in [("calm", (0, 0)), ("smile", (32, 0)),
                     ("surprised", (32, 32))]:
    print("=====", name, "=====")
    print(c.matrix_text(region=(rx, ry, rx + 31, ry + 31)))

finish(c)
