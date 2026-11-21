# Frame 1: original content on a wider canvas (33x44), character at same spot.
W, H = 33, 44
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, 0)

# Frame 2: copy, then redraw the extended-arm region as a horizontal jab.
f2 = f1.copy(name="f2")

cmap = {'a': '#222034', 'e': '#df7126', 'c': '#eec39a', 'f': '#8f563b'}

# Repaint region x12..x32, y9..y14 ('.' = erase to transparent).
rows = {
    9:  "aee" + "a" * 14 + "....",          # deltoid top + arm top outline
    10: "afecc" + "e" * 8 + "acca" + ".aa.",  # arm top row, fist knuckles, whoosh dash
    11: "e" * 13 + "aeea" + "....",          # arm middle + fist middle
    12: "ceeef" + "e" * 7 + "fafea" + ".aa.",  # arm bottom row w/ shadows, whoosh dash
    13: "cce" + "a" * 14 + "....",          # torso + arm bottom outline
    14: "cccf" + "." * 17,                  # torso + pec shadow, old arm outline erased
}
for y, s in rows.items():
    for i, ch in enumerate(s):
        f2.set(12 + i, y, cmap.get(ch))

view(f1)
view(f2)
finish([f1, f2])
