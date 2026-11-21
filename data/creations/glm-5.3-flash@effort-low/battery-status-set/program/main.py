from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="batteries")

OUT = "#2b2b2b"
TIP = "#2b2b2b"
GREEN = "#3fbf4a"
DARKGREEN = "#2e8f38"
RED = "#d94040"
YELLOW = "#f2c020"
ORANGE = "#e08a10"

def battery(x, y):
    """12x14 battery outline at (x,y), tip 4px wide on top."""
    # tip
    c.rect(x + 4, y, 4, 2, TIP)
    # body outline
    c.rect(x, y + 2, 12, 14, OUT, fill=False)
    return x + 1, y + 3  # interior top-left (10 wide x 12 tall interior)

# Battery 1: 100% full green
ix, iy = battery(1, 24)
c.rect(ix, iy, 10, 12, GREEN)
c.rect(ix, iy, 10, 2, DARKGREEN)

# Battery 2: 60%
ix, iy = battery(18, 24)
c.rect(ix, iy, 10, 12, "#ffffff00" if False else None)  # leave transparent
c.rect(ix, iy + 5, 10, 7, GREEN)   # bottom 7 of 12 rows filled (~60%)
c.rect(ix, iy + 5, 10, 1, DARKGREEN)

# Battery 3: 20%
ix, iy = battery(35, 24)
c.rect(ix, iy + 10, 10, 2, RED)

# Battery 4: charging
ix, iy = battery(52, 24)
c.rect(ix, iy, 10, 12, YELLOW)
# lightning bolt
bolt = [(ix+5, iy+1), (ix+3, iy+6), (ix+5, iy+6), (ix+3, iy+11),
        (ix+7, iy+5), (ix+5, iy+5), (ix+7, iy+1)]
c.poly(bolt, ORANGE)

print(c.stats_text())
finish(c)
