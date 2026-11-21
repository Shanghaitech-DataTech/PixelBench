OUTLINE = "#231a20"
SKIN = "#f7cfa9"
SKIN_SH = "#d99e74"
HAIR = "#8a5a33"
HAIR_H = "#ab7a4e"
SHIRT = "#2f7d8c"
SHIRT_D = "#1e5564"
COLLAR = "#f2e9d8"
WHITE = "#ffffff"
MOUTH_R = "#8c2f33"
BLUSH = "#e8896f"


def portrait(c, x0, y0, mood):
    # ---- body / outfit (same in all four) ----
    c.rect(x0 + 6, y0 + 23, 20, 8, OUTLINE)          # torso block
    c.rect(x0 + 7, y0 + 24, 18, 6, SHIRT)
    c.rect(x0 + 7, y0 + 28, 18, 2, SHIRT_D)
    c.rect(x0 + 12, y0 + 24, 8, 2, COLLAR)            # collar

    # ---- hair (same in all four) ----
    c.ellipse(x0 + 16, y0 + 13, 10, 9, HAIR)          # hair cap
    c.line(x0 + 13, y0 + 7, x0 + 19, y0 + 7, HAIR_H)  # highlight
    c.rect(x0 + 14, y0 + 2, 4, 3, HAIR)               # tuft
    c.rect(x0 + 14, y0 + 2, 4, 1, HAIR_H)

    # ---- face (same in all four) ----
    c.ellipse(x0 + 16, y0 + 17, 8, 7, SKIN)
    c.set(x0 + 16, y0 + 18, SKIN_SH)                   # small nose dot

    # ---- features (mood) ----
    if mood == "calm":
        # relaxed open eyes + flat brows + calm flat mouth
        c.rect(x0 + 9, y0 + 15, 5, 3, WHITE)
        c.rect(x0 + 18, y0 + 15, 5, 3, WHITE)
        c.rect(x0 + 10, y0 + 16, 2, 2, OUTLINE)
        c.rect(x0 + 20, y0 + 16, 2, 2, OUTLINE)
        c.rect(x0 + 10, y0 + 13, 4, 1, OUTLINE)
        c.rect(x0 + 18, y0 + 13, 4, 1, OUTLINE)
        c.rect(x0 + 13, y0 + 20, 6, 1, OUTLINE)
        c.circle(x0 + 11, y0 + 18, 1, BLUSH)
        c.circle(x0 + 20, y0 + 18, 1, BLUSH)
    elif mood == "smiling":
        # happy closed arc eyes + open smile with teeth
        c.line(x0 + 9, y0 + 17, x0 + 11, y0 + 15, OUTLINE)
        c.line(x0 + 11, y0 + 15, x0 + 13, y0 + 17, OUTLINE)
        c.line(x0 + 18, y0 + 17, x0 + 20, y0 + 15, OUTLINE)
        c.line(x0 + 20, y0 + 15, x0 + 22, y0 + 17, OUTLINE)
        c.ellipse(x0 + 16, y0 + 20, 3, 2, OUTLINE)
        c.rect(x0 + 14, y0 + 20, 6, 1, WHITE)
        c.rect(x0 + 14, y0 + 21, 6, 2, MOUTH_R)
        c.circle(x0 + 11, y0 + 18, 1, BLUSH)
        c.circle(x0 + 20, y0 + 18, 1, BLUSH)
    elif mood == "angry":
        # narrowed eyes + slanted brows (outer high, inner low) + frown
        c.rect(x0 + 9, y0 + 15, 5, 3, WHITE)
        c.rect(x0 + 18, y0 + 15, 5, 3, WHITE)
        c.rect(x0 + 9, y0 + 15, 5, 1, OUTLINE)   # heavy lid
        c.rect(x0 + 18, y0 + 15, 5, 1, OUTLINE)
        c.rect(x0 + 10, y0 + 16, 2, 2, OUTLINE)
        c.rect(x0 + 19, y0 + 16, 2, 2, OUTLINE)
        c.set(x0 + 9, y0 + 12, OUTLINE)
        c.set(x0 + 10, y0 + 13, OUTLINE)
        c.set(x0 + 11, y0 + 14, OUTLINE)
        c.set(x0 + 22, y0 + 12, OUTLINE)
        c.set(x0 + 21, y0 + 13, OUTLINE)
        c.set(x0 + 20, y0 + 14, OUTLINE)
        c.set(x0 + 13, y0 + 21, OUTLINE)
        c.set(x0 + 14, y0 + 20, OUTLINE)
        c.set(x0 + 15, y0 + 20, OUTLINE)
        c.set(x0 + 16, y0 + 19, OUTLINE)
        c.set(x0 + 17, y0 + 20, OUTLINE)
        c.set(x0 + 18, y0 + 20, OUTLINE)
        c.set(x0 + 19, y0 + 21, OUTLINE)
    else:  # surprised
        # wide eyes + raised brows + open "o" mouth
        c.rect(x0 + 9, y0 + 14, 5, 5, WHITE)
        c.rect(x0 + 18, y0 + 14, 5, 5, WHITE)
        c.rect(x0 + 10, y0 + 15, 2, 2, OUTLINE)
        c.rect(x0 + 19, y0 + 15, 2, 2, OUTLINE)
        c.rect(x0 + 11, y0 + 12, 3, 1, OUTLINE)
        c.rect(x0 + 19, y0 + 12, 3, 1, OUTLINE)
        c.ellipse(x0 + 16, y0 + 21, 2, 1, OUTLINE)
        c.rect(x0 + 15, y0 + 21, 3, 1, MOUTH_R)


c = new_canvas(64, 64)
portrait(c, 0, 0, "calm")
portrait(c, 32, 0, "smiling")
portrait(c, 0, 32, "angry")
portrait(c, 32, 32, "surprised")
c.outline(OUTLINE)

print(c.stats_text())
for mood, x0, y0 in [("calm", 0, 0), ("smiling", 32, 0), ("angry", 0, 32), ("surprised", 32, 32)]:
    print("==", mood, "==")
    print(c.matrix_text((x0 + 4, y0 + 6, x0 + 27, y0 + 27)))

finish(c)
