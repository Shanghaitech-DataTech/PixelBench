# Four battery icons in one horizontal row: 100% / 60% / 20% / charging
c = new_canvas(64, 64, background=None, name="batteries")

OUT   = c.color('#20232e')   # shared outline colour
WHITE = c.color('#ffffff')   # empty interior
GREEN = c.color('#39d353')   # full / charging
AMBER = c.color('#f5b921')   # 60%
RED   = c.color('#e23b33')   # 20%
BOLT  = c.color('#ffdf3d')   # lightning bolt

BW, BH = 11, 20   # battery body size
TOP = 24          # body top row (terminal nub sits 2px above)

def battery(x, pct, fill_col):
    # empty interior (white), so fill level reads clearly
    c.rect(x + 1, TOP + 1, BW - 2, BH - 2, WHITE)
    # charge fill, measured from the bottom of the interior
    fh = round((BH - 2) * pct)
    if fh > 0:
        c.rect(x + 1, TOP + BH - 1 - fh, BW - 2, fh, fill_col)
    # identical outline for every battery
    c.rect(x, TOP, BW, BH, OUT, fill=False)   # body
    c.rect(x + 4, TOP - 2, 3, 2, OUT)         # terminal nub

battery(2,  1.00, GREEN)   # 100%
battery(18, 0.60, AMBER)   # 60%
battery(34, 0.20, RED)     # 20%
battery(50, 0.75, GREEN)   # charging (bolt on top)

# lightning bolt over the 4th battery: yellow fill + dark outline
bolt = [(56, 17), (50, 30), (54, 30), (51, 42), (59, 28), (55, 28), (58, 17)]
c.poly(bolt, BOLT)
c.poly(bolt, OUT, fill=False)

view(c)
finish(c)
