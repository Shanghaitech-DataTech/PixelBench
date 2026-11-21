from pixelbench_api import *

# palette letters -> hex (colours already registered by the input image)
COL = {
    'a': '#1d181e',  # near-black outline / trailing edge
    'b': '#7784a2',  # pale grey-blue fur
    'c': '#b572b1',  # light pink-purple highlight along the arm
    'd': '#432f53',  # dark purple arm bone / membrane bone
    'e': '#5f5f7b',  # grey-blue midtone
    'f': '#ae0000',  # red eyes
    'g': '#fff9d6',  # pale yellow fangs
    'h': '#5c436f',  # mid purple membrane
}

# The raised wings need headroom above the ears (they touch y=0 in the input),
# so both frames live on a 27x26 canvas with the bat placed 4 rows down.
# The body keeps the exact same position in both frames.
W, H, DY = 27, 26, 4

# ---------------- frame 1 : the original picture ----------------
f1 = new_canvas(W, H, None, name='frame1')
f1.blit(input_canvas, 0, DY)

# ---------------- frame 2 : wings flapped up ----------------
f2 = new_canvas(W, H, None, name='frame2')
f2.blit(input_canvas, 0, DY)

# strip the drooping wings (everything left of x=9 / right of x=17).
# The body, head, ears and the wing attachments at x=9 / x=17 (the dark arm
# blob on rows 8-11, the black seam on rows 12-14) stay untouched.
f2.clear(0, 0, 9, H)
f2.clear(18, 0, 9, H)

# Raised left wing, one 10-char row per canvas row (x0..x9), rows 0..17.
#   - black claw tip at the top-left corner (the drooping tip sat in the
#     bottom-left corner, so the flap reads as a clean up-down beat)
#   - 'd' arm bone sweeps down-right into the kept shoulder blob at x9,
#     with 'c'/'e' highlight bands hugging it and 'h' membrane inside
#   - 'a' trailing edge runs down the outer side, then curves in to the hip,
#     the membrane stretching across to the flank on rows 15-17
LEFT = [
    ".aa.......",  # 0  claw
    "ahd.......",  # 1
    "ahed......",  # 2
    "ahhd......",  # 3
    "ahhcd.....",  # 4
    "ahecdd....",  # 5
    "ahhecdd...",  # 6
    ".ahhecdd..",  # 7
    ".ahhhecdd.",  # 8  arm meets the kept shoulder 'd' at x9
    "..ahhhecd.",  # 9
    "...ahhecd.",  # 10
    "....ahecd.",  # 11
    "....ahhed.",  # 12  bone beside the kept black seam at x9
    ".....ahed.",  # 13
    "......ahd.",  # 14
    "......ahhh",  # 15  membrane fills the old gap, reaching the flank
    ".......ahh",  # 16
    "........ah",  # 17  hip, beside the leg
]


def stamp(cv, rows, mirror):
    for y, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch == '.':
                continue
            cv.set((W - 1 - i) if mirror else i, y, COL[ch])


stamp(f2, LEFT, mirror=False)   # left wing
stamp(f2, LEFT, mirror=True)    # right wing, mirrored about the body axis
f2.set(17, 14, COL['a'])        # the input's right seam pixel is 'b' here; symmetrise

# sanity: the body (x10..x16) must be pixel-identical in both frames
bad = [(x, y) for y in range(H) for x in range(10, 17) if f1.get(x, y) != f2.get(x, y)]
print("body diffs:", bad)

print("f1:", f1.stats_text())
print("f2:", f2.stats_text())
print(f2.matrix_text())

finish([f1, f2])
