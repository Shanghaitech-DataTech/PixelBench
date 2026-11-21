"""flag-wave (edit) - 3 frames.

The input is native 12x14 pixel art upscaled 4x to 48x56.  Frame 1 is the
original picture.  Frames 2 and 3 continue the loop: the fly end of the flag
swings from its highest point (frame 1) down through level (frame 2) to its
lowest point (frame 3).  The pole / mounting hardware never moves; only the
fabric does.  Frames 2 and 3 are re-drawn on the same 12x14 native grid and
scaled 4x, matching the input's pixel scale exactly.
"""

LW, LH = 12, 14          # native art resolution (input is a 4x upscale)
W, H, F = 48, 56, 4

DARK, RED, LIGHT = 1, 2, 3        # palette: c0 outline, c1 red, c2 light red
SYM = {0: '.', 1: '#', 2: 'R', 3: 'r', 4: 'M', 5: 'P'}

g = [[input_canvas.get(F * x, F * y) for x in range(LW)] for y in range(LH)]

X0, X1 = 5, 11                    # hoist column .. free (fly) edge column
TIP = 11                          # free edge is a solid dark hem column

# top (T) and bottom (B) row of the fabric for each column x = 5..11
T_REST = [4, 4, 3, 2, 1, 0, 0]    # frame 1 state, fly end highest
B_REST = [8, 8, 8, 7, 6, 6, 6]
T_MID = [4, 4, 3, 3, 3, 3, 3]     # frame 2, fabric level, tip starting down
B_MID = [8, 8, 8, 8, 8, 8, 9]
T_LOW = [4, 4, 4, 4, 4, 4, 5]     # frame 3, fly end at its lowest
B_LOW = [8, 8, 9, 9, 10, 10, 11]


def paint(Ts, Bs, name):
    """Draw the fabric for the given edges, then the fixed support on top."""
    c = new_canvas(W, H, name=name)
    for i, x in enumerate(range(X0, X1 + 1)):
        T, B = Ts[i], Bs[i]
        for y in range(T, B + 1):
            col = DARK if (x == TIP or y == T or y == B) else RED
            c.rect(x * F, y * F, F, F, col)
        if x in (6, 7):                        # fold highlight near the hoist
            for y in range(T + 1, min(T + 2, B - 1) + 1):
                c.rect(x * F, y * F, F, F, LIGHT)
    # pole, its red bands and the cross arm: identical in every frame
    for y in range(LH):
        for x in range(LW):
            v = g[y][x]
            if v and (x <= 4 or (x <= 6 and y == 3)):
                c.rect(x * F, y * F, F, F, v)
    return c


def dump(c, title):
    print(title)
    print("     " + "".join(str(x % 10) for x in range(LW)))
    for y in range(LH):
        print(f"{y:3d}  " + "".join(SYM[c.get(F * x, F * y)] for x in range(LW)))


f1 = input_canvas.copy(name="f1")
f2 = paint(T_MID, B_MID, "f2")
f3 = paint(T_LOW, B_LOW, "f3")

dump(paint(T_REST, B_REST, "rest_check"), "--- rebuilt rest state (sanity) ---")
dump(f1, "--- frame 1 (original) ---")
dump(f2, "--- frame 2 (fly end level) ---")
dump(f3, "--- frame 3 (fly end lowest) ---")

for name, c in (("f1", f1), ("f2", f2), ("f3", f3)):
    print(name, c.stats_text())

finish([f1, f2, f3])
