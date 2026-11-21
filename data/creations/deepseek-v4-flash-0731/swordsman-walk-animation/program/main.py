COL = {
    "O": "#1b1e28",  # outline
    "H": "#e0453f",  # red hair
    "S": "#f5c996",  # skin
    "E": "#20242e",  # eye
    "C": "#3c5a94",  # dark blue cape
    "T": "#93a0b6",  # steel tunic
    "B": "#463a30",  # boots / belt
    "G": "#d8a64a",  # gold hilt
    "M": "#cdd6e2",  # sword blade
}

head_rows = [
    "." * 32,
    "." * 32,
    "." * 32,
    "." * 12 + "H" + "." + "H" + "." + "H" + "." * 15,
    "." * 11 + "O" + "H" * 6 + "O" + "." * 13,
    "." * 10 + "O" + "H" * 7 + "O" + "." * 13,
    "." * 10 + "O" + "H" + "S" * 6 + "O" + "." * 13,
    "." * 10 + "O" + "H" + "S" * 3 + "E" + "S" * 2 + "O" + "." * 13,
    "." * 10 + "O" + "H" + "S" * 6 + "O" + "." * 13,
    "." * 11 + "O" + "H" * 5 + "O" + "." * 14,
    "." * 7 + "C" * 3 + "O" + "T" * 8 + "O" + "." * 12,
    "." * 6 + "C" * 4 + "O" + "T" * 8 + "O" + "." * 12,
    "." * 6 + "C" * 4 + "O" + "T" * 8 + "O" + "." * 12,
    "." * 6 + "C" * 3 + "O" + "T" * 8 + "O" + "." * 13,
    "." * 6 + "C" * 3 + "O" + "T" * 8 + "O" + "." * 13,
    "." * 6 + "C" * 2 + "O" + "T" * 8 + "O" + "." * 14,
    "." * 6 + "C" * 2 + "O" + "T" * 7 + "O" + "." * 15,
    "." * 6 + "C" * 1 + "O" + "T" * 7 + "O" + "." * 16,
]

# Frame A: wide stride  (left leg trailing, right leg forward, feet apart)
legsA = [
    "." * 5 + "C" * 1 + "T" * 2 + "." * 4 + "T" * 3 + "." * 17,
    "." * 5 + "C" * 1 + "T" * 2 + "." * 4 + "T" * 3 + "." * 17,
    "." * 6 + "T" * 2 + "." * 4 + "T" * 3 + "." * 17,
    "." * 6 + "T" * 2 + "." * 5 + "T" * 2 + "." * 17,
    "." * 6 + "T" * 2 + "." * 5 + "T" * 2 + "." * 17,
    "." * 6 + "B" * 2 + "." * 5 + "B" * 2 + "." * 17,
    "." * 7 + "B" + "." * 6 + "B" + "." * 17,
    "." * 7 + "B" + "." * 6 + "B" + "." * 17,
    "." * 7 + "B" + "." * 7 + "B" + "." * 16,
    "." * 8 + "B" + "." * 7 + "B" + "." * 15,
    "." * 32,
    "." * 32,
    "." * 32,
    "." * 32,
]

# Frame B: passing pose (legs near together under the body)
legsB = [
    "." * 6 + "C" * 1 + "T" * 3 + "." * 2 + "T" * 3 + "." * 17,
    "." * 6 + "T" * 3 + "." * 2 + "T" * 3 + "." * 18,
    "." * 7 + "T" * 2 + "." * 3 + "T" * 2 + "." * 18,
    "." * 7 + "T" * 2 + "." * 3 + "T" * 2 + "." * 18,
    "." * 7 + "T" * 2 + "." * 3 + "T" * 2 + "." * 18,
    "." * 8 + "B" * 2 + "." * 3 + "B" * 2 + "." * 17,
    "." * 8 + "B" + "." * 4 + "B" + "." * 18,
    "." * 9 + "B" + "." * 4 + "B" + "." * 17,
    "." * 9 + "B" + "." * 5 + "B" + "." * 16,
    "." * 32,
    "." * 32,
    "." * 32,
    "." * 32,
]

# Frame A sword: held at the hip, long blade angled down-forward
swordA = [
    (13, 12, "S"), (14, 13, "S"), (15, 14, "S"), (16, 15, "S"), (17, 15, "S"),
    (18, 16, "G"), (19, 16, "G"),
    (19, 17, "M"), (20, 18, "M"), (21, 19, "M"), (22, 20, "M"), (23, 21, "M"),
    (24, 22, "M"), (25, 23, "M"),
    (20, 17, "M"), (21, 18, "M"), (22, 19, "M"), (23, 20, "M"), (24, 21, "M"),
]

# Frame B sword: same sword, shifted down one pixel (arm swing with the step)
swordB = [
    (13, 12, "S"), (14, 13, "S"), (15, 14, "S"), (16, 15, "S"), (17, 16, "S"),
    (18, 17, "G"), (19, 17, "G"),
    (19, 18, "M"), (20, 19, "M"), (21, 20, "M"), (22, 21, "M"), (23, 22, "M"),
    (24, 23, "M"), (20, 18, "M"), (21, 19, "M"), (22, 20, "M"), (23, 21, "M"),
]


def frame_canvas(rows, sword):
    for y, r in enumerate(rows):
        if len(r) != 32:
            raise ValueError(("row len", y, len(r)))
    c = new_canvas(32, 32)
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch != ".":
                c.set(x, y, COL[ch])
    for x, y, ch in sword:
        c.set(x, y, COL[ch])
    return c


a = frame_canvas(head_rows + legsA, swordA)
b = frame_canvas(head_rows + legsB, swordB)
result = new_canvas(64, 32)
result.blit(a, 0, 0)
result.blit(b, 32, 0)

print("FRAME A")
print(a.stats_text())
print(a.matrix_text(region=(0, 0, 31, 31)))
print("FRAME B")
print(b.matrix_text(region=(0, 0, 31, 31)))
print("RESULT")
print(result.stats_text())
print(result.matrix_text(region=(0, 0, 63, 31)))

finish(result)
