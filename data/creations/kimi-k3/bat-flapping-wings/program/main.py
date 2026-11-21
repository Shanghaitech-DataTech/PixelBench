# Bat flapping wings: f1 = original content, f2 = wings raised/spread
W, H = 27, 30
OY = 8  # vertical offset of original picture inside the taller canvas

DARK = '#1d181eff'   # a - outline
PURP = '#432f53ff'   # d - wing membrane
PINK = '#b572b1ff'   # c - accent along leading edge
GREY = '#5f5f7bff'   # e
LPUR = '#5c436fff'   # h - lighter purple shading

# ---- Frame 1: original picture, unchanged, on the taller canvas ----
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, OY)

# ---- Frame 2: same body, wings redrawn raised ----
f2 = new_canvas(W, H, name="f2")
f2.blit(input_canvas, 0, OY)

# erase the drooping wings (keep head/body/feet)
f2.clear(0, 14, 9, 16)        # left wing block  (x 0-8,  rows 14-29)
f2.clear(18, 14, 9, 16)       # right wing block (x 18-26, rows 14-29)
f2.set(9, 14, None); f2.set(9, 15, None)    # left wing-top strays
f2.set(17, 14, None); f2.set(17, 15, None)  # right wing-top strays
f2.set(9, 16, None); f2.set(9, 17, None)    # detach left wing from body outline
f2.set(17, 16, None); f2.set(17, 17, None)  # detach right wing from body outline

# raised left wing drawn on its own layer, then mirrored for the right
wing = new_canvas(W, H, name="wingL")
d = ("M 9 14 L 7 10 L 5 6 L 3 3 L 1 1 "   # leading edge up to the tip
     "L 0 3 L 1 5 "                        # tip cap
     "Q 2 6 4 10 "                         # scallop 1 (concave trailing edge)
     "Q 5 11 6 14 "                        # scallop 2
     "Q 7 15 9 18 Z")                      # scallop 3 back to the body
wing.path(d, PURP, fill=True)
wing.path(d, DARK, fill=False)
# pink accent just inside the leading edge
for (x, y) in [(8, 13), (7, 11), (6, 10), (5, 8), (4, 6), (3, 5)]:
    wing.set(x, y, PINK)
# light-purple interior shading
for (x, y) in [(6, 12), (5, 11), (4, 9), (3, 7)]:
    wing.set(x, y, LPUR)

wingR = wing.copy(name="wingR")
wingR.mirror("h")

f2.blit(wing, 0, 0)
f2.blit(wingR, 0, 0)

view(f1)
view(f2)
finish([f1, f2])
