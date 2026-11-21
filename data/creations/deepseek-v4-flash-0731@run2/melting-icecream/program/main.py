from pixelbench_api import *

c = input_canvas.copy(name="output")

BG = c.color((0xfc, 0xfc, 0xfc, 0xff))     # background white
MAIN = c.color((0x95, 0x52, 0x4c))         # chocolate brown (matches original 'r')
LITE = c.color((0xa8, 0x60, 0x57))         # chocolate highlight
DARK = c.color((0x6e, 0x38, 0x38))         # chocolate shadow

W, H = 64, 64

# cone bounds per row (measured on the pristine copy)
LB, RB = {}, {}
for y in range(29, 60):
    lo = hi = None
    for x in range(W):
        if c.get(x, y) != BG:
            if lo is None:
                lo = x
            hi = x
    LB[y] = lo
    RB[y] = hi


def drip(xs, y0, y1, w):
    """Chocolate drip hugging the cone: stem of width 2w+1, rounded drop head."""
    head = w + 2
    # stem
    for y in range(y0, y1 - 2):
        cx = xs(y)
        for dx in range(-w, w + 1):
            c.set(cx + dx, y, MAIN)
        c.set(cx - w, y, LITE)
        c.set(cx + w, y, DARK)
    # rounded head (bulges over the cone rim)
    for yy, rr in ((y1 - 2, head), (y1 - 1, head), (y1, head - 1)):
        cx = xs(yy)
        for dx in range(-rr, rr + 1):
            c.set(cx + dx, yy, MAIN)
        c.set(cx - rr, yy, LITE)
        c.set(cx + rr, yy, DARK)


# ---- drips running down the cone ----
# left side, hugging the left rim
drip(lambda y: LB.get(y, 20) + 1, 32, 48, 1)
# right side, hugging the right rim
drip(lambda y: RB.get(y, 40) - 1, 33, 48, 1)
# short rivulet left-of-centre
drip(lambda y: 27, 34, 41, 0)
# short rivulet right-of-centre
drip(lambda y: 34, 34, 40, 0)
# small drip on the lower right
drip(lambda y: 31, 43, 50, 0)

print(c.matrix_text(region=(14, 29, 48, 53), indices=True))
print(c.stats_text())
finish(c)
