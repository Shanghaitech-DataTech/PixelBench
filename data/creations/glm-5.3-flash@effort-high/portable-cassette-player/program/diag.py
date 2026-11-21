from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="cassette-player")

BODY   = c.color("#3d4f78", "body")
BODY_D = c.color("#2b3a5c", "body_dark")
LIGHT  = c.color("#5f74a3", "body_light")
DARK   = c.color("#151c2c", "outline")

c.rect(4, 4, 24, 24, DARK)
print("after outline rect, get(10,10) =", c.get(10, 10))
c.rect(5, 5, 22, 22, BODY)
print("after body rect, get(10,10) =", c.get(10, 10), "BODY =", BODY)
for cx, cy in [(4, 4), (26, 4), (4, 26), (26, 26)]:
    c.clear(cx, cy, 2, 2)
for x, y in [(5, 5), (26, 5), (5, 26), (26, 26)]:
    c.clear(x, y)
print("after corner clears, get(10,10) =", c.get(10, 10))
c.rect(6, 5, 20, 1, LIGHT)
c.rect(6, 26, 20, 1, BODY_D)
c.rect(26, 6, 1, 20, BODY_D)
print("after sheen, get(10,10) =", c.get(10, 10))
print(c.stats_text())
