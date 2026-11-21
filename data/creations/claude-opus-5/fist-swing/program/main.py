DARK = "c0"      # #222034 outline
SKIN = "c2"      # #eec39a highlight
ORANGE = "c4"    # #df7126 body mid tone
BROWN = "c5"     # #8f563b body shadow
GRAY = "c6"      # #847e87 motion lines

f1 = input_canvas.copy(name="frame1")
f2 = input_canvas.copy(name="frame2")

# --- frame 2: extend the right-side (character's left) arm into a jab ---
# wipe the old bent arm, keep torso (x <= 15) intact
f2.clear(16, 9, 13, 6)          # x 16..28, y 9..14

# shoulder joint tidy-up on the torso edge
f2.set(15, 10, SKIN)
f2.set(15, 11, ORANGE)
f2.set(15, 12, ORANGE)
f2.set(15, 13, BROWN)

# upper arm / forearm, x 16..20
f2.rect(16, 9, 5, 1, DARK)      # top outline
f2.rect(16, 10, 5, 1, SKIN)     # top highlight
f2.rect(16, 11, 5, 1, ORANGE)
f2.rect(16, 12, 5, 1, ORANGE)
f2.rect(16, 13, 5, 1, BROWN)    # underside shadow
f2.rect(16, 14, 5, 1, DARK)     # bottom outline

# wrist: one column narrower top and bottom
f2.set(21, 9, DARK)
f2.set(21, 10, DARK)
f2.set(21, 11, SKIN)
f2.set(21, 12, ORANGE)
f2.set(21, 13, DARK)
f2.set(21, 14, DARK)

# fist, x 22..27 — taller than the wrist so the knuckles read as a mass
f2.rect(22, 9, 6, 1, DARK)
fist = [
    (10, [DARK, SKIN, SKIN, SKIN, SKIN, DARK]),
    (11, [SKIN, SKIN, ORANGE, ORANGE, SKIN, DARK]),
    (12, [SKIN, ORANGE, BROWN, ORANGE, SKIN, DARK]),
    (13, [DARK, ORANGE, BROWN, ORANGE, SKIN, DARK]),
]
for y, row in fist:
    for i, col in enumerate(row):
        f2.set(22 + i, y, col)
f2.rect(22, 14, 6, 1, DARK)

# dashed speed lines trailing the fist
for x in (16, 18, 20):
    f2.set(x, 7, GRAY)
    f2.set(x, 16, GRAY)

view(f1)
view(f2)
finish([f1, f2])
