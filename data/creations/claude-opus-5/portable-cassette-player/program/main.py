c = new_canvas(32, 32, name="player")

OL   = c.color("#23262d", "outline")
BD   = c.color("#7c838f", "body")
HL   = c.color("#a9b0bb", "hilite")
SH   = c.color("#5a606b", "shade")
FR   = c.color("#2f333c", "frame")
TP   = c.color("#4a3022", "tape")
TP2  = c.color("#7a5238", "tape2")
HUB  = c.color("#dde1e7", "hub")
HUBS = c.color("#9aa1ac", "hubshade")
BTN  = c.color("#c6ccd6", "button")
BTND = c.color("#8d939e", "buttondark")
ACC  = c.color("#4fd07e", "play")
RED  = c.color("#d9544a", "led")
CAB  = c.color("#1b1e24", "cable")
MET  = c.color("#454b55", "metal")

# ---- headphone jack on top ----
c.rect(21, 3, 3, 2, MET)

# ---- body: rounded rect with outline ----
c.rect(3, 5, 26, 23, BD)
for (x, y) in ((3, 5), (28, 5), (3, 27), (28, 27)):
    c.set(x, y, None)
c.outline(OL)
c.line(5, 6, 26, 6, HL)
c.line(4, 7, 4, 25, HL)
c.line(5, 26, 26, 26, SH)
c.line(27, 8, 27, 25, SH)

# ---- cassette window: frame, then transparent interior ----
c.rect(5, 8, 22, 11, FR)
c.clear(6, 9, 20, 9)

# ---- two tape reels inside the transparent window ----
for cx in (11, 20):
    c.circle(cx, 13, 3, TP)            # wound tape
    c.circle(cx, 13, 2, TP2)           # lighter inner wind
    c.rect(cx - 1, 12, 3, 3, HUB)      # reel hub
    c.set(cx, 13, HUBS)                # hub centre hole
    c.set(cx - 2, 13, HUB)             # spoke teeth
    c.set(cx + 2, 13, HUB)
    c.set(cx, 11, HUB)
    c.set(cx, 15, HUB)
# tape span between the spools
c.line(14, 13, 17, 13, TP)

# ---- playback controls ----
for bx in (5, 10, 15):
    c.rect(bx, 21, 4, 3, BTN)
    c.line(bx, 23, bx + 3, 23, BTND)
c.set(6, 22, OL)
c.line(7, 21, 7, 23, OL)          # rewind
c.line(11, 21, 11, 23, ACC)
c.set(12, 22, ACC)                # play
c.line(16, 21, 16, 23, OL)
c.set(17, 22, OL)                 # fast forward

# ---- volume thumbwheel ----
c.rect(21, 20, 5, 5, MET)
for (x, y) in ((21, 20), (25, 20), (21, 24), (25, 24)):
    c.set(x, y, BD)
c.line(22, 21, 24, 21, HUBS)
c.line(22, 23, 24, 23, HUBS)
c.set(23, 22, HUB)

# ---- speaker grille + power LED ----
c.dither(6, 25, 13, 1, [SH, BD], pattern="checker")
c.set(6, 19, RED)

# ---- headphone cable: continuous 1px lead off the top-right ----
for (x, y) in ((22, 2), (23, 1), (24, 1), (25, 1), (26, 2), (27, 2),
               (28, 3), (28, 4), (29, 5), (29, 6), (30, 7), (30, 8),
               (31, 9)):
    c.set(x, y, CAB)

view(c)
result = c
finish(result)
