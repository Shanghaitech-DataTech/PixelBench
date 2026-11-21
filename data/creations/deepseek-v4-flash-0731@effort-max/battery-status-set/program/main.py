from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="battery-status-set")

# palette
OUT   = c.color("#23272e")   # battery outline
GREEN = c.color("#2ecc71")   # charge fill
YELLOW = c.color("#f1c40f")  # charging fill
BOLT  = c.color("#14161a")   # lightning bolt

NUB_Y, NUB_W, NUB_H = 20, 5, 4
BODY_Y, BODY_W, BODY_H = 24, 13, 21   # body rows 24..44, inner rows 25..43 (19 rows)

def battery_outline(x):
    c.rect(x + 4, NUB_Y, NUB_W, NUB_H, OUT)
    c.rect(x, BODY_Y, BODY_W, BODY_H, OUT)
    c.clear(x + 1, BODY_Y + 1, BODY_W - 2, BODY_H - 2)  # hollow inside

def fill_rows(x, rows, colour):
    c.rect(x + 1, BODY_Y + 1 + (19 - rows), 11, rows, colour)

xs = [3, 18, 33, 48]   # four icons, 15px pitch
for x in xs:
    battery_outline(x)

# 100% : all 19 inner rows filled
fill_rows(xs[0], 19, GREEN)

# 60%  : 11 of 19 rows filled from the bottom
fill_rows(xs[1], 11, GREEN)

# 20%  : 4 of 19 rows filled from the bottom
fill_rows(xs[2], 4, GREEN)

# charging: low yellow fill + lightning bolt
fill_rows(xs[3], 4, YELLOW)
ix = xs[3] + 1
iy = BODY_Y + 1
c.poly([(ix + 6, iy + 0), (ix + 1, iy + 11), (ix + 5, iy + 11),
        (ix + 3, iy + 18), (ix + 10, iy + 8), (ix + 6, iy + 8)], BOLT)

print(c.stats_text())
print(c.matrix_text(region=(0, 16, 63, 47), indices=True))
finish(c)
