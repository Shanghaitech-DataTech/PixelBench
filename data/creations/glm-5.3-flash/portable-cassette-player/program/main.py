# Portable cassette player - 32x32 front-facing icon, transparent background
c = new_canvas(32, 32, background=None, name="cassette-player")

OUT   = c.color("#23262e", "outline")
BODY  = c.color("#b6bfcb", "body")
MID   = c.color("#93a0b0", "body-shadow")
DARK  = c.color("#6d7a8c", "body-deep")
HI    = c.color("#ccd3dd", "highlight")
FRAME = c.color("#333a48", "window-frame")
RING  = c.color("#e9edf4", "reel")
TAPE  = c.color("#3a4150", "tape")
KNOBM = c.color("#6b7686", "knob")
ORNG  = c.color("#e2623c", "accent")
FACE  = c.color("#9aa5b5", "button-face")


def px(points, col=OUT):
    for x, y in points:
        c.set(x, y, col)


# ---- body: rounded rectangle x=4..27, y=3..28 ----
c.rect(6, 3, 20, 1, OUT)       # top edge
c.rect(6, 28, 20, 1, OUT)      # bottom edge
c.rect(4, 5, 1, 22, OUT)       # left edge
c.rect(27, 5, 1, 22, OUT)      # right edge
px([(5, 4), (26, 4), (5, 27), (26, 27)])   # corner curves

c.rect(6, 4, 20, 1, HI)        # top bevel highlight
c.rect(5, 5, 22, 22, BODY)     # main fill
c.rect(5, 5, 1, 22, HI)        # left bevel highlight
c.rect(26, 5, 1, 22, MID)      # right shade
c.rect(6, 27, 20, 1, MID)      # bottom shade

# ---- cassette window (transparent glass) ----
c.clear(7, 7, 18, 11)                      # see-through interior
c.rect(6, 6, 20, 13, FRAME, fill=False)    # bezel


def reel(cx, cy):
    c.circle(cx, cy, 3, RING, fill=True)   # spool flange
    c.circle(cx, cy, 2, TAPE, fill=True)   # wound tape
    px([(cx, cy - 1), (cx, cy + 1), (cx - 1, cy), (cx + 1, cy)], RING)  # spokes
    c.set(cx, cy, OUT)                     # axle


reel(11, 12)
reel(20, 12)

# ---- accent stripe ----
c.rect(6, 19, 20, 1, MID)      # shadow under window
c.rect(6, 20, 20, 1, ORNG)     # stripe

# ---- playback buttons ----
def button(x, w, face):
    c.rect(x, 22, w, 5, face)
    c.rect(x, 26, w, 1, DARK)  # 3d bottom


button(5, 5, FACE)             # rewind
button(11, 4, ORNG)            # play (accent)
button(16, 5, FACE)            # fast-forward

px([(6, 23), (9, 23), (5, 24), (6, 24), (8, 24), (9, 24), (6, 25), (9, 25)])        # REW <<
px([(12, 23), (12, 24), (13, 24), (12, 25)])                                        # PLAY >
px([(16, 23), (19, 23), (16, 24), (17, 24), (19, 24), (20, 24), (16, 25), (19, 25)])  # FF >>

# ---- volume knob ----
c.circle(24, 24, 2, TAPE, fill=True)
c.circle(24, 24, 1, KNOBM, fill=True)
px([(24, 22), (24, 23), (24, 24)], RING)   # pointer

# ---- headphone jack + cable ----
c.rect(21, 2, 3, 1, OUT)       # plug on top edge
cable = [(22, 1), (23, 1), (24, 1), (25, 1), (26, 2), (27, 3), (28, 4), (29, 5), (30, 6),
         (30, 7), (30, 8), (30, 9), (30, 10), (30, 11), (30, 12), (30, 13), (30, 14),
         (30, 15), (30, 16), (29, 17), (29, 18), (29, 19),
         (30, 20), (30, 21), (30, 22), (30, 23), (30, 24), (30, 25), (30, 26),
         (29, 27), (28, 28), (28, 29), (29, 30), (30, 30), (30, 31)]
px(cable)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
